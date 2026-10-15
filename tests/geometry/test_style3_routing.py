"""Generic zone-gap routing and checks against rendered header geometry."""
from copy import deepcopy
from xml.etree import ElementTree as ET

import pytest

from archatlas.check import check_svg
from archatlas.cli import initial
from archatlas.layout import layout
from archatlas.layout.base import Box, Connector, Scene
from archatlas.layout.route import route, backtrack, crosses, segment_hits_rect, _overlap
from archatlas.render import render_svg


def test_zone_gaps_beat_a_clear_outer_detour_without_sharing_strokes():
    source, target = (0, 40, 20, 20), (300, 40, 20, 20)
    zones = [(60, -200, 40, 280), (150, 20, 40, 280)]
    previous = [[(110, 96), (134, 96)]]
    original = deepcopy((zones, previous))
    points = route(source, target, zones, from_port="e", to_port="w", previous=previous)
    segments = list(zip(points, points[1:]))
    length = sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in segments)
    # Previously a 796px outer detour was accepted before visibility search.
    assert length == 432
    assert backtrack(points) == 76
    assert points[0] == (20, 50) and points[-1] == (300, 50)
    assert all(a != b and (a[0] == b[0] or a[1] == b[1]) for a, b in segments)
    assert not any(segment_hits_rect(a, b, rect, padding=8)
                   for a, b in segments for rect in zones)
    assert not any(segment_hits_rect(a, b, rect)
                   for a, b in segments for rect in (source, target))
    assert not any(_overlap(a, b, c, d) for a, b in segments
                   for line in previous for c, d in zip(line, line[1:]))
    assert route(source, target, list(reversed(zones)), from_port="e", to_port="w",
                 previous=previous) == points
    assert (zones, previous) == original


def test_ancestor_header_obstacle_preserves_a_clear_body_exit():
    source, target = (160, 180, 40, 40), (350, 40, 40, 40)
    header = (100, 100, 200, 44)
    points = route(source, target, [header])
    assert not any(segment_hits_rect(a, b, header, padding=8)
                   for a, b in zip(points, points[1:]))
    assert backtrack(points) == 0


def test_crossing_triggers_search_even_without_a_substantial_foldback():
    source, target = (200, 0, 100, 40), (50, 600, 100, 40)
    obstacles = [(80, 40, 100, 60), (34, 550, 350, 30)]
    previous = [[(100, -20), (100, 38)]]
    points = route(source, target, obstacles, previous=previous)
    segments = list(zip(points, points[1:]))
    # The simple left-side exit crosses an existing edge. A bottom exit and
    # independently chosen horizontal/vertical corridors avoid that crossing.
    assert not any(crosses(a, b, *previous[0]) or _overlap(a, b, *previous[0])
                   for a, b in segments)
    assert not any(segment_hits_rect(a, b, rect, padding=8)
                   for a, b in segments for rect in obstacles)
    assert backtrack(points) == 24
    assert sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in segments) == 793


def header_scene(points, *, source="inside", target="outside", kind="call"):
    return Scene("Zone routing", "Generic routing fixture", 600, 400,
                 boxes=[Box("zone", 100, 100, 200, 160, role="group", kind="boundary",
                            header_height=44),
                        Box("inside", 160, 180, 40, 40, parent="zone"),
                        Box("outside", 400, 100, 40, 40)],
                 edges=[Connector("link", points, source, target, kind=kind)])


def header_findings(svg):
    return [finding for finding in check_svg(svg)["findings"]
            if finding["rule"] == "edge-crosses-header"]


@pytest.mark.parametrize("kind", ["call", "message", "lifeline"])
def test_edges_cannot_cross_ancestor_or_frame_headers(kind):
    scene = header_scene([(180, 180), (180, 120), (400, 120)], kind=kind)
    if kind in ("message", "lifeline"):
        scene.boxes[0].kind = "frame"
    findings = header_findings(render_svg(scene))
    assert len(findings) == 1
    assert findings[0]["severity"] == "error"
    assert findings[0]["elements"] == ["link", "zone"]
    assert findings[0]["boxes"] == [(102, 102, 196, 40)]


@pytest.mark.parametrize("reverse", [False, True])
def test_group_border_ports_are_valid_but_crossing_the_group_header_is_not(reverse):
    scene = header_scene([(200, 100), (200, 80), (420, 80), (420, 100)],
                         source="zone")
    if reverse:
        scene.edges[0].points.reverse()
        scene.edges[0].source, scene.edges[0].target = "outside", "zone"
    assert not header_findings(render_svg(scene))
    scene.edges[0].points = [(200, 100), (200, 120), (400, 120)]
    if reverse:
        scene.edges[0].points.reverse()
    assert header_findings(render_svg(scene))
    assert any(f["rule"] == "edge-port-direction" for f in check_svg(render_svg(scene))["findings"])


def test_header_check_uses_svg_band_geometry_and_ignores_legend_samples():
    scene = header_scene([(200, 200), (340, 200), (340, 120), (400, 120)])
    scene.boxes.append(Box("sample", 320, 180, 40, 40, role="legend-zone",
                           header_height=30))
    scene.edges.append(Connector("sample-line", [(140, 120), (240, 120)], "", "", kind="legend"))
    # A real connector crossing even a legend header is a collision; legend
    # sample lines themselves are not routed relationships.
    findings = header_findings(render_svg(scene))
    assert [f["elements"] for f in findings] == [["link", "sample"]]
    scene.boxes.pop()
    svg = render_svg(scene)
    assert not header_findings(svg)
    root = ET.fromstring(svg)
    band = next(e for e in root if e.get("data-role") == "header-band")
    band.set("height", "110")
    assert header_findings(ET.tostring(root, encoding="unicode"))
    root.remove(band)
    assert not header_findings(ET.tostring(root, encoding="unicode"))


def test_header_boundary_travel_and_unbanded_groups_are_clear():
    scene = header_scene([(200, 200), (320, 200), (320, 142), (102, 142)])
    assert not header_findings(render_svg(scene))
    scene.edges[0].points = [(180, 180), (180, 120), (400, 120)]
    scene.boxes[0].band = False
    assert not header_findings(render_svg(scene))


@pytest.mark.parametrize("corridor,warning", [(392, False), (150, True)])
def test_only_geometry_proven_header_reversal_is_discounted(corridor, warning):
    scene = header_scene([(750, 200), (corridor, 200), (corridor, 60), (750, 60)])
    scene.width = 1300
    scene.boxes[0].x, scene.boxes[0].w = 400, 800
    scene.boxes[1].x = 750
    scene.boxes[-1].x, scene.boxes[-1].y = 750, 40
    report = check_svg(render_svg(scene))
    assert report["routes"][0]["header_backtrack"] == 348
    for rule in ("edge-foldback", "edge-detour"):
        assert (rule in {f["rule"] for f in report["findings"]}) is warning
    assert not header_findings(render_svg(scene))
    # Without the band, the same reversal has no geometric justification.
    scene.boxes[0].band = False
    report = check_svg(render_svg(scene))
    assert report["routes"][0]["header_backtrack"] == 0
    assert "edge-foldback" in {f["rule"] for f in report["findings"]}


@pytest.mark.parametrize("theme", ["neutral", "print", "dark"])
def test_rendered_legend_covers_cards_chips_badges_zones_and_edges(theme):
    model = initial("nested")
    model["meta"]["theme"] = theme
    model["groups"] = [{"id": "zone", "title": "Scope", "kind": "boundary"}]
    model["nodes"][0].update(parent="zone", chips=["Property"], badge=1)
    report = check_svg(render_svg(layout(model)))
    assert not [f for f in report["findings"] if f["rule"] == "unexplained-encoding"]


@pytest.mark.parametrize("mutation", ["missing-swatch", "missing-caption", "wrong-paint"])
def test_unexplained_encoding_checks_actual_swatches_and_captions(mutation):
    root = ET.fromstring(render_svg(layout(initial("nested"))))
    swatch = next(e for e in root if e.get("data-role") == "legend-swatch")
    if mutation == "missing-swatch":
        root.remove(swatch)
    elif mutation == "wrong-paint":
        swatch.set("fill", "#ff0000")
    else:
        index = swatch.get("data-id").rsplit("-", 1)[-1]
        caption = next(e for e in root if e.get("data-id") == "legend-" + index)
        root.remove(caption)
    findings = [f for f in check_svg(ET.tostring(root, encoding="unicode"))["findings"]
                if f["rule"] == "unexplained-encoding"]
    assert any(f["elements"] == ["client"] for f in findings)
    assert all(f["severity"] == "error" for f in findings)


def test_vertical_header_needs_a_matching_legend_axis():
    model = initial("lanes")
    model["layout"]["direction"] = "LR"
    root = ET.fromstring(render_svg(layout(model)))
    assert not [f for f in check_svg(ET.tostring(root, encoding="unicode"))["findings"]
                if f["rule"] == "unexplained-encoding"]
    swatch = next(e for e in root if e.get("data-role") == "legend-zone"
                  and e.get("data-band-axis") == "x")
    swatch.set("data-band-axis", "y")
    assert any(f["rule"] == "unexplained-encoding"
               for f in check_svg(ET.tostring(root, encoding="unicode"))["findings"])
