"""Glyph geometry contracts, independent of schema/legend policy."""
import copy
import os
from unittest.mock import patch
from xml.etree import ElementTree as ET

import pytest

from archatlas.check.browser import check_browser
from archatlas.check.report import check_svg, on_shape, shape_box
from archatlas.fonts import FontMetrics
from archatlas.layout.base import Box, Connector
from archatlas.layout.engine import Layout
from archatlas.render import render_svg


@pytest.fixture(scope="module")
def metrics():
    return FontMetrics()


def build(metrics, nodes, edges=(), groups=(), direction="LR"):
    # This worker owns glyphs; schema and semantic legends have separate tests.
    model = {"archatlas": "0.1", "meta": {"title": "Symbols", "type": "B1"},
             "layout": {"template": "nested", "direction": direction},
             "nodes": nodes, "edges": list(edges), "groups": list(groups)}
    engine = Layout(model, metrics)
    engine.graph()
    return engine.finish()


def shapes(svg):
    return {e.get("data-id"): e for e in ET.fromstring(svg).iter() if e.get("data-role") == "node"}


def rules(svg, metrics):
    return {f["rule"] for f in check_svg(svg, metrics)["findings"]}


def test_actor_is_stick_figure_with_owned_label_and_reserved_footprint(metrics):
    label = "Customer service representative"
    scene = build(metrics, [{"id": "human", "kind": "actor", "label": label, "parent": "system"},
                            {"id": "card", "kind": "person", "label": "Architecture person"}],
                  groups=[{"id": "system", "kind": "boundary", "title": "System"}])
    svg = render_svg(scene)
    actor, card = shapes(svg)["human"], shapes(svg)["card"]
    assert actor.tag.endswith("g")
    assert len(actor.findall("{*}circle")) == 1
    assert len(actor.findall("{*}polyline")) == 3
    assert not actor.findall(".//{*}rect")
    assert card.tag.endswith("rect")
    box = next(b for b in scene.boxes if b.id == "human")
    text = next(t for t in scene.texts if t.owner == "human")
    assert " ".join(text.lines) == label
    assert text.y >= box.glyph_rect[1] + box.glyph_rect[3] + 10
    assert text.y + text.h <= box.y + box.h
    assert check_svg(svg, metrics)["errors"] == 0


@pytest.mark.parametrize("direction,port", [("LR", "e"), ("TB", "s")])
def test_actor_connectors_touch_glyph_and_avoid_own_label(metrics, direction, port):
    scene = build(metrics, [{"id": "actor", "kind": "actor", "label": "Support agent"},
                            {"id": "case", "kind": "use_case", "label": "Review request"}],
                  [{"from": "actor", "to": "case", "from_port": port, "dir": "--"}],
                  direction=direction)
    svg = render_svg(scene)
    actor = shapes(svg)["actor"]
    edge = next(e for e in scene.edges if e.source == "actor")
    assert on_shape(edge.points[0], actor)
    report = check_svg(svg, metrics)
    assert report["errors"] == 0, report["findings"]


def test_use_case_ellipse_fits_measured_multiline_text_and_ports(metrics):
    scene = build(metrics, [
        {"id": "a", "kind": "use_case", "label": "Review international shipment eligibility",
         "sub": "Check delivery options", "size_hint": {"width": 150}},
        {"id": "b", "kind": "use_case", "label": "Confirm shipment"}],
        [{"from": "a", "to": "b", "dir": "--"}, {"from": "a", "to": "b", "dir": "--"}])
    svg = render_svg(scene)
    assert all(e.tag.endswith("ellipse") for e in shapes(svg).values())
    assert len(next(t for t in scene.texts if t.id == "a-name").lines) > 1
    assert metrics.measured_with == "pillow"
    report = check_svg(svg, metrics)
    assert report["errors"] == 0, report["findings"]
    # Real primitive mutation: the nominal data-box remains unchanged.
    root = ET.fromstring(svg)
    ellipse = next(e for e in root if e.get("data-id") == "a")
    ellipse.set("ry", "15")
    assert "text-overflow" in rules(ET.tostring(root, encoding="unicode"), metrics)


def test_ellipse_corner_text_cannot_pass_rectangular_owner_check(metrics):
    scene = build(metrics, [{"id": "case", "kind": "use_case", "label": "X"}])
    box = next(b for b in scene.boxes if b.id == "case")
    text = next(t for t in scene.texts if t.owner == "case")
    text.anchor = "start"
    text.x, text.y = box.x + 5, box.y + 5
    assert "text-overflow" in rules(render_svg(scene), metrics)


def test_actor_owner_and_label_obstacle_checks_are_not_skipped(metrics):
    scene = build(metrics, [{"id": "actor", "kind": "actor", "label": "Support agent"}])
    text = next(t for t in scene.texts if t.owner == "actor")
    broken = copy.deepcopy(scene)
    next(t for t in broken.texts if t.owner == "actor").y -= 50
    assert "text-overflow" in rules(render_svg(broken), metrics)
    scene.boxes.extend([Box("left", text.left - 80, text.y, 20, 20),
                        Box("right", text.left + text.w + 60, text.y, 20, 20)])
    scene.edges.append(Connector("cross", [(text.left - 60, text.y + 10),
                                          (text.left + text.w + 60, text.y + 10)], "left", "right"))
    assert "arrow-through-label" in rules(render_svg(scene), metrics)


def test_bpmn_start_end_are_unfilled_circles_with_distinct_strokes(metrics):
    scene = build(metrics, [{"id": kind, "kind": "event", "label": kind, **options}
                            for kind, options in [("start", {"event_type": "start"}),
                                                  ("end", {"event_type": "end"}), ("legacy", {})]])
    svg = render_svg(scene)
    nodes = shapes(svg)
    for node in nodes.values():
        assert node.tag.endswith("ellipse")
        assert node.get("rx") == node.get("ry")
        assert node.get("fill") != node.get("stroke")
        assert len(node) == 0  # No filled UML final-state inner disk.
    assert float(nodes["end"].get("stroke-width")) > float(nodes["start"].get("stroke-width"))
    assert nodes["legacy"].get("stroke-width") == nodes["start"].get("stroke-width")
    assert check_svg(svg, metrics)["errors"] == 0


def test_browser_owner_checks_use_glyph_geometry(metrics):
    scene = build(metrics, [{"id": "actor", "kind": "actor", "label": "Agent"},
                            {"id": "case", "kind": "use_case", "label": "Review request"}])
    svg = render_svg(scene)
    geometry = {"canvas": [0, 0, scene.width, scene.height], "shapes": [], "texts": []}
    for id, e in shapes(svg).items():
        geometry["shapes"].append({"id": id, "role": "node", "parent": "", "kind": e.get("data-kind"),
                                   "tag": e.tag.rsplit("}", 1)[-1], "box": shape_box(e)})
    for text in scene.texts:
        if text.owner:
            geometry["texts"].append({"id": text.id, "owner": text.owner, "role": text.role, "box": text.rect})
    with patch("archatlas.check.browser._measure", return_value=geometry):
        assert check_browser(svg)["errors"] == 0
    actor = next(t for t in geometry["texts"] if t["owner"] == "actor")
    x, y, w, h = actor["box"]
    actor["box"] = (x + 40, y - 30, w, h)
    case = next(s for s in geometry["shapes"] if s["id"] == "case")
    x, y, w, h = case["box"]
    case["box"] = (x, y + h / 2 - 8, w, 16)
    with patch("archatlas.check.browser._measure", return_value=geometry):
        findings = check_browser(svg)["findings"]
    assert {f["elements"][1] for f in findings if f["rule"] == "browser-text-overflow"} == {"actor", "case"}


@pytest.mark.skipif(os.environ.get("ARCHATLAS_BROWSER_TESTS") != "1", reason="Optional Chromium check")
def test_real_browser_symbol_geometry(metrics):
    scene = build(metrics, [{"id": "actor", "kind": "actor", "label": "Support agent"},
                            {"id": "case", "kind": "use_case", "label": "Review shipment eligibility"}])
    report = check_browser(render_svg(scene))
    assert report["errors"] == 0, report["findings"]
