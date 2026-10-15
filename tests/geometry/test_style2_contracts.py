"""Focus, sequence annotations, exact legend encodings and link identifiers."""
from copy import deepcopy

from archatlas.check import check_svg
from archatlas.cli import initial, failed
from archatlas.layout import layout
from archatlas.layout.base import Box, Connector
from archatlas.render import render_svg
from archatlas.render.legend import entries


def sequence_model():
    model = initial("sequence")
    model["layout"]["focus"] = "payment"
    model["nodes"] = [{"id": id, "kind": "lifeline", "label": label}
                      for id, label in (("client", "Client"), ("payment", "Payment service"),
                                        ("provider", "Provider"), ("audit", "Audit reader"))]
    pairs = [("client", "payment"), ("payment", "provider"), ("provider", "payment"),
             ("payment", "provider"), ("provider", "payment"), ("payment", "client")]
    model["edges"] = [{"from": a, "to": b, "step": i + 1, "label": "Request" if i % 2 else "Result"}
                      for i, (a, b) in enumerate(pairs)]
    model["frames"] = [{"id": "outcome", "operator": "alt", "from_step": 2, "to_step": 5,
                        "operands": [{"guard": "result received", "from_step": 2, "to_step": 3},
                                     {"guard": "timeout and retry allowed", "from_step": 4, "to_step": 5}]},
                       {"id": "retry", "operator": "loop", "guard": "attempt < 2", "from_step": 4, "to_step": 5}]
    model["activations"] = [{"node": "payment", "from_step": 1, "to_step": 6},
                            {"node": "provider", "from_step": 2, "to_step": 5}]
    return model


def test_primary_warning_is_visible_in_strict_qa_and_focus_does_not_mutate_input():
    model = initial("nested")
    model["nodes"][0]["style"] = "primary"
    report = check_svg(render_svg(layout(model)))
    assert "multiple-focus" in {f["rule"] for f in report["findings"]}
    assert failed(report, "warning")
    model = sequence_model()
    before = deepcopy(model)
    scene = layout(model)
    assert model == before
    assert next(b for b in scene.boxes if b.id == "payment").style == "primary"
    assert all(e.style == "primary" for e in scene.edges if e.kind == "lifeline" and e.source == "payment")


def test_fragments_narrow_to_participants_and_annotations_clear_execution_geometry():
    scene = layout(sequence_model())
    report = check_svg(render_svg(scene))
    assert not report["findings"], report
    frame = next(b for b in scene.boxes if b.id == "outcome")
    unused = [b for b in scene.boxes if b.id in ("client", "audit")]
    assert unused[0].x + unused[0].w / 2 < frame.x
    assert unused[1].x + unused[1].w / 2 > frame.x + frame.w
    message_y = [e.points[0][1] for e in scene.edges if e.kind not in ("lifeline", "legend", "frame-separator")]
    assert all(b.h >= 8 or any(b.y <= y <= b.y + b.h for y in message_y)
               for b in scene.boxes if b.role == "activation")
    guard = next(t for t in scene.texts if t.role == "operand-guard")
    x = guard.left + 12
    scene.edges.append(Connector("bad-life", [(x, guard.y - 2), (x, guard.y + guard.h + 2)],
                                  "payment", "payment", kind="lifeline"))
    scene.boxes.append(Box("bad-activation", x, guard.y, 10, guard.h, role="activation"))
    report = check_svg(render_svg(scene))
    assert sum(f["rule"] == "sequence-annotation-overlap" for f in report["findings"]) >= 2


def test_sequence_rhythm_reserves_measured_labels_without_tall_fixed_gaps():
    model = initial("sequence")
    model["edges"] = [{"from": "client", "to": "service", "label": "Submit request", "step": i + 1}
                      for i in range(8)]
    scene = layout(model)
    assert scene.height < 850
    assert not check_svg(render_svg(scene))["errors"]


def test_auto_legend_covers_tints_bands_badges_and_only_used_styles():
    model = initial("nested")
    model["groups"] = [{"id": "a", "kind": "boundary", "title": "A", "tint": "app"},
                       {"id": "b", "kind": "boundary", "title": "B", "tint": "app", "dashed": False},
                       {"id": "c", "kind": "boundary", "title": "C", "tint": "tech", "band": False}]
    model["nodes"][0].update(parent="a", badge=1)
    model["nodes"][1]["parent"] = "b"
    model["meta"]["legend"] = [{"label": "Unused proposed box", "style": "planned", "symbol": "box"}]
    scene = layout(model)
    legend = entries(scene, model)
    assert "Unused proposed box" not in {e["label"] for e in legend}
    zones = {(e["tint"], e["band"], e["dashed"]) for e in legend if e["symbol"] == "zone"}
    assert zones == {("app", True, True), ("app", True, False), ("tech", False, True)}
    assert any(e["symbol"] == "box" and e["style"] == "peer" for e in legend)
    assert any(e["symbol"] == "badge" and e["badge"] == "1" for e in legend)
    assert not check_svg(render_svg(scene))["errors"]
    model = initial("sequence")
    model["edges"].append({"from": "service", "to": "client", "kind": "call", "dashed": True})
    model["meta"].update(legend_mode="replace", legend=[
        {"label": "Call", "kind": "call", "symbol": "line"},
        {"label": "Reply", "dashed": True, "symbol": "line"}])
    lines = [e for e in entries(layout(model), model) if e["symbol"] == "line"]
    assert [(e["label"], e["dashed"]) for e in lines] == [
        ("Call / Numbers show flow order", False), ("Reply / Numbers show flow order", True)]
    model = initial("nested")
    model["edges"].append({"from": "service", "to": "client", "kind": "data"})
    model["meta"].update(legend_mode="replace",
                         legend=[{"label": "Authored data exchange", "kind": "data", "symbol": "line"}])
    assert any(e["label"] == "Authored data exchange" for e in entries(layout(model), model))


def test_edge_badges_are_references_unless_order_is_declared():
    for ordered in (False, True):
        model = initial("nested")
        model["layout"]["ordered"] = ordered
        model["edges"][0]["badge"] = 3
        scene = layout(model)
        assert any(b.role == "edge-badge" for b in scene.boxes)
        labels = [e["label"] for e in entries(scene, model)]
        assert ("Numbers show flow order" if ordered else "Numbers are labels for reference") in labels
        assert not check_svg(render_svg(scene))["errors"]
    model = initial("nested")
    model["edges"][0]["step"] = 1
    model["meta"].update(legend_mode="replace", legend=[])
    assert any("Numbers are labels for reference" in e["label"] and e["symbol"] == "line"
               for e in entries(layout(model), model))


def test_qa_detects_inward_ports_and_accumulated_short_overlaps():
    scene = layout(initial("nested"))
    edge = next(e for e in scene.edges if e.kind != "legend")
    a, b = edge.points[0], edge.points[-1]
    duplicate = deepcopy(edge)
    duplicate.id = "overlap"
    duplicate.points = [(a[0] + i * .5, a[1]) for i in range(5)] + [
        (a[0] + 2, a[1] + 20), (b[0], a[1] + 20), b]
    scene.edges.append(duplicate)
    report = check_svg(render_svg(scene))
    assert "edge-overlap" in {f["rule"] for f in report["findings"]}
    edge.points = [a, (a[0] - 8, a[1]), b]
    report = check_svg(render_svg(scene))
    assert "edge-port-direction" in {f["rule"] for f in report["findings"]}
    assert report["routes"]
