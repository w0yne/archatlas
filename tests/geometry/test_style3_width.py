"""The wrap width (layout.max_width) is a packing constraint, never a request to shrink fonts."""
import pytest

from archatlas.cli import initial
from archatlas.layout import layout
from archatlas.render import render_svg
from archatlas.check import check_svg


@pytest.mark.parametrize("template", ["nested", "layered", "statechart"])
@pytest.mark.parametrize("direction", ["LR", "TB"])
def test_rows_wrap_within_profile_and_preserve_reading_order(template, direction):
    model = initial(template)
    model["layout"].update(columns=8, direction=direction, max_width=1120)
    model["nodes"] = [{"id": f"n{i}", "kind": "state" if template == "statechart" else "component",
                       "label": f"Element {i}", "parent": "inner"} for i in range(8)]
    model["groups"] = [{"id": "outer", "kind": "boundary", "title": "Outer"},
                       {"id": "inner", "parent": "outer", "kind": "boundary", "title": "Inner"}]
    model["edges"] = []
    scene = layout(model)
    boxes = [b for b in scene.boxes if b.role == "node"]
    assert max(b.x + b.w for b in scene.boxes if b.role == "group") <= 1080
    assert [b.id for b in sorted(boxes, key=lambda b: (b.y, b.x))] == [f"n{i}" for i in range(8)]
    assert not check_svg(render_svg(scene))["errors"]


def test_max_width_is_a_setting_with_a_wide_default():
    def rows(**layout):
        model = initial("layered")
        model["layout"].update(columns=6, **layout)
        model["groups"] = [{"id": "band", "kind": "layer", "title": "Band"}]
        model["nodes"] = [{"id": f"n{i}", "kind": "component", "label": f"Element {i}", "parent": "band"} for i in range(6)]
        model["edges"] = []
        return len({b.y for b in layout_boxes(model)})
    assert rows() == 1
    assert rows(max_width=700) > 1


def layout_boxes(model):
    return [b for b in layout(model).boxes if b.role == "node"]


def test_horizontal_state_ranks_wrap_without_changing_edges():
    model = initial("statechart")
    model["layout"].update(direction="LR", max_width=1120)
    model["nodes"] = [{"id": f"s{i}", "kind": "state", "label": f"State {i}"} for i in range(7)]
    model["edges"] = [{"from": f"s{i}", "to": f"s{i+1}"} for i in range(6)]
    scene = layout(model)
    nodes = [b for b in scene.boxes if b.role == "node"]
    assert max(b.x + b.w for b in nodes) <= 1080
    assert len({b.y for b in nodes}) > 1
    assert [(e.source, e.target) for e in scene.edges if e.source] == [(f"s{i}", f"s{i+1}") for i in range(6)]


def test_wrapped_ranks_use_each_rows_own_height():
    model = initial("statechart")
    model["layout"].update(direction="LR", max_width=1120)
    model["nodes"] = [{"id": "a", "kind": "state", "label": "Entry", "style": "external"},
                      {"id": "b", "kind": "state", "label": "Expanded scope",
                       "size_hint": {"width": 800, "height": 800}}]
    model["edges"] = [{"from": "a", "to": "b"}]
    scene = layout(model)
    boxes = {b.id: b for b in scene.boxes}
    assert boxes["a"].y < 200
    assert 0 < boxes["b"].y - boxes["a"].y - boxes["a"].h < 200


def test_sequence_keeps_native_fonts_and_warns_about_scaled_readability():
    model = initial("sequence")
    model["nodes"] = [{"id": f"p{i}", "kind": "lifeline", "label": f"Participant {i}"} for i in range(9)]
    model["edges"] = [{"from": "p0", "to": "p8", "label": "Deliver result"}]
    model["frames"] = []
    scene = layout(model)
    assert min(t.size for t in scene.texts) >= 11
    assert "scaled-text-too-small" in {w["rule"] for w in scene.warnings}


def test_repository_polling_frames_include_only_actual_endpoint_interval():
    # Replay the two polling ranges of the repository sequence with generic labels.
    model = initial("sequence")
    ids = ["client", "front", "queue", "worker", "store", "results"]
    model["nodes"] = [{"id": id, "kind": "lifeline", "label": id, "size_hint": {"width": 130}} for id in ids]
    pairs = [("client", "front"), ("front", "queue"), ("front", "client"),
             ("worker", "queue"), ("worker", "store"), ("results", "store"), ("results", "client")]
    model["edges"] = [{"from": a, "to": b, "step": i + 1, "label": "Exchange"} for i, (a, b) in enumerate(pairs)]
    model["frames"] = [{"id": "worker-poll", "operator": "loop", "guard": "poll", "from_step": 4, "to_step": 5},
                       {"id": "result-poll", "operator": "loop", "guard": "poll", "from_step": 6, "to_step": 7}]
    scene = layout(model)
    boxes = {b.id: b for b in scene.boxes}
    center = lambda id: boxes[id].x + boxes[id].w / 2
    first, second = boxes["worker-poll"], boxes["result-poll"]
    assert first.x > center("front")
    assert first.x + first.w < center("results")
    # A push to the leftmost client really does need the wider interval.
    assert second.x < center("client") < center("results") < second.x + second.w


def test_horizontal_lanes_reserve_side_headers_for_cross_lane_messages():
    model = initial("lanes")
    model["layout"]["direction"] = "LR"
    scene = layout(model)
    groups = {b.id: b for b in scene.boxes if b.role == "group"}
    assert all(b.header_width > 0 for b in groups.values())
    for node in (b for b in scene.boxes if b.role == "node"):
        group = groups[node.parent]
        assert node.x >= group.x + group.header_width
    assert not check_svg(render_svg(scene))["findings"]


@pytest.mark.parametrize("grouped", [False, True])
def test_independent_entity_clusters_keep_their_relationships_local(grouped):
    model = initial("er")
    model["nodes"] = [{"id": f"e{i}", "kind": "entity", "label": f"Entity {i}"} for i in range(7)]
    model["edges"] = [{"from": f"e{a}", "to": f"e{b}"} for a, b in
                      [(0, 1), (1, 2), (1, 3), (4, 5), (5, 6)]]
    if grouped:
        model["groups"] = [{"id": "data", "kind": "boundary", "title": "Data"}]
        for node in model["nodes"]:
            node["parent"] = "data"
    scene = layout(model)
    boxes = {b.id: b for b in scene.boxes}
    assert boxes["e1"].x == boxes["e3"].x
    assert boxes["e4"].y == boxes["e5"].y == boxes["e6"].y
    assert boxes["e4"].y > boxes["e3"].y
    assert not check_svg(render_svg(scene))["findings"]
