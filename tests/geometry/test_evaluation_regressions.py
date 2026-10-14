"""Contracts exposed by the first full skill evaluation."""
from copy import deepcopy
from xml.etree import ElementTree as ET

import pytest

from archatlas.check import check_svg
from archatlas.cli import initial, failed
from archatlas.fonts import FontMetrics
from archatlas.layout import layout
from archatlas.layout.route import route, _overlap
from archatlas.model import validate, ModelError
from archatlas.render import render_svg


def sequence():
    model = initial("sequence")
    model["edges"] = [
        {"from": "client", "to": "service", "step": 1, "label": "Request", "kind": "call"},
        {"from": "service", "to": "client", "step": 2, "label": "Accepted", "kind": "reply"},
        {"from": "service", "to": "client", "step": 3, "label": "Rejected", "kind": "async"},
    ]
    model["frames"] = [{
        "id": "result", "operator": "alt", "from_step": 1, "to_step": 3,
        "operands": [{"guard": "valid", "from_step": 1, "to_step": 2},
                     {"guard": "else", "from_step": 3, "to_step": 3}],
    }, {"id": "retry", "operator": "loop", "guard": "attempt < 3",
        "from_step": 1, "to_step": 2}]
    return model


def test_nested_structured_frames_guards_separators_and_message_markers():
    metrics = FontMetrics()
    scene = layout(sequence(), metrics)
    svg = render_svg(scene)
    report = check_svg(svg, metrics)
    assert not report["findings"], report
    root = ET.fromstring(svg)
    assert len([e for e in root.iter() if e.get("data-role") == "frame-separator"]) == 1
    assert {"alt", "[valid]", "[else]", "loop [attempt < 3]"} <= {
        "".join(e.itertext()) for e in root.iter() if e.tag.endswith("}text")}
    messages = {e.get("data-id"): e for e in root.iter() if e.get("data-role") == "edge"}
    assert messages["edge-2"].get("stroke-dasharray")
    assert not messages["edge-3"].get("stroke-dasharray")
    for key in ("edge-2", "edge-3"):
        marker = next(e for e in root.iter() if e.get("id") == messages[key].get("marker-end")[5:-1])
        assert list(marker)[0].get("fill") == "none"


def test_alt_ranges_and_nested_operand_boundaries_are_validated():
    model = sequence()
    model["frames"][0]["operands"][1]["from_step"] = 2
    with pytest.raises(ModelError, match="partition"):
        validate(model)
    model = sequence()
    model["frames"][1]["to_step"] = 3
    with pytest.raises(ModelError, match="one operand"):
        validate(model)
    model = sequence()
    model["frames"][0]["operands"] = model["frames"][0]["operands"][:1]
    with pytest.raises(ModelError):
        validate(model)


def test_frame_reserves_space_for_long_guards_and_a_final_self_call():
    model = sequence()
    model["frames"] = [{"id": "retry", "operator": "loop",
                        "guard": "AuthorizationAuthenticationServiceUnavailable",
                        "from_step": 1, "to_step": 3}]
    model["edges"][-1]["from"] = model["edges"][-1]["to"]
    metrics = FontMetrics()
    scene = layout(model, metrics)
    report = check_svg(render_svg(scene), metrics)
    assert not report["errors"], report
    frame = next(b for b in scene.boxes if b.id == "retry")
    last = next(e for e in scene.edges if e.id == "edge-3")
    assert max(p[1] for p in last.points) < frame.y + frame.h


def test_long_identifiers_widen_nodes_and_cells_without_word_breaks():
    word = "AuthenticationAuthorizationService"
    for template in ("nested", "grid_table"):
        model = initial(template)
        if template == "nested":
            model["nodes"][0].update(label=word, size_hint={"width": 80})
        else:
            model["tables"][0]["rows"][0][0] = word
        metrics = FontMetrics()
        scene = layout(model, metrics)
        text = next(t for t in scene.texts if t.source == word)
        assert text.lines == [word]
        assert not check_svg(render_svg(scene), metrics)["errors"]
        assert not any(w["rule"] == "font-wrap-overflow" for w in scene.warnings)
    text.lines = ["Authentication", "AuthorizationService"]
    text.runs = []
    assert "intra-word-break" in {f["rule"] for f in check_svg(render_svg(scene), metrics)["findings"]}


def test_cjk_estimate_cannot_pass_strict_check_on_a_measured_host():
    model = initial("nested")
    model["meta"]["lang"] = "zh"
    model["nodes"][0]["label"] = "认证服务"
    svg = render_svg(layout(model, FontMetrics(paths=[], lang="zh")))
    assert "Noto Sans CJK SC" in svg
    report = check_svg(svg, FontMetrics())
    assert "cjk-measurement-estimate" in {f["rule"] for f in report["findings"]}
    assert failed(report, "warning")


def test_shared_port_is_reallocated_and_bad_manual_routes_are_reported():
    previous = [[(20, 10), (100, 10)]]
    points = route((0, 0, 20, 20), (100, 0, 20, 20), [],
                   from_port="e", to_port="w", previous=previous)
    assert points[0] != previous[0][0]
    assert not any(_overlap(a, b, c, d) for a, b in zip(points, points[1:])
                   for c, d in zip(previous[0], previous[0][1:]))
    scene = layout(initial("nested"))
    duplicate = deepcopy(scene.edges[0])
    duplicate.id = "duplicate"
    scene.edges.append(duplicate)
    a, b = duplicate.points[0], duplicate.points[-1]
    duplicate.points = [a, (a[0], a[1] - 600), (b[0], a[1] - 600),
                        (b[0] + 20, a[1] - 600), (b[0], a[1] - 600), b]
    rules = {f["rule"] for f in check_svg(render_svg(scene))["findings"]}
    assert {"edge-u-turn", "edge-overlap", "edge-detour"} <= rules
    # A route can fold back across several bends without an adjacent U-turn,
    # and still be well below the old 2x-distance detour threshold.
    duplicate.points = [(318, 241.2), (334, 241.2), (334, 195.2),
                        (835.375, 195.2), (835.375, 241.2), (851.375, 241.2)]
    rules = {f["rule"] for f in check_svg(render_svg(scene))["findings"]}
    assert "edge-foldback" in rules


def test_inferred_nodes_and_documented_edges_have_dashes_and_evidence_legend():
    model = initial("nested")
    model["nodes"][0]["evidence"] = {"status": "inferred"}
    model["edges"][0]["evidence"] = {"status": "doc-only"}
    scene = layout(model)
    assert next(b for b in scene.boxes if b.id == "client").dashed
    assert scene.edges[0].dashed
    legends = [" ".join(t.lines) for t in scene.texts if t.role == "legend"]
    assert any("Inferred, not verified" in label for label in legends)
    assert any("Documented only, not verified" in label for label in legends)
