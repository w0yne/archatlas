"""Legends remain complete and use real swatches under authored replacement."""
from copy import deepcopy
from xml.etree import ElementTree as ET

import pytest

from archatlas.cli import initial
from archatlas.layout import layout
from archatlas.layout.base import Box, Connector, Scene, Text
from archatlas.render import render_svg
from archatlas.render.legend import entries


def model():
    result = initial("nested")
    result["meta"].update(legend_mode="replace", legend=[])
    return result


def test_replace_retains_every_zone_card_chip_badge_and_edge_encoding():
    data = model()
    data["groups"] = [
        {"id": "app", "kind": "boundary", "title": "Application", "tint": "app"},
        {"id": "data", "kind": "boundary", "title": "Data", "tint": "data", "dashed": False},
        {"id": "tech", "kind": "layer", "title": "Infrastructure", "tint": "tech", "band": False},
    ]
    data["nodes"] = [
        {"id": "client", "kind": "external", "label": "Client"},
        {"id": "service", "kind": "component", "label": "Service", "style": "primary", "parent": "app",
         "badge": 1, "chips": ["HTTP", {"label": "Shared", "style": "shared"}]},
        {"id": "store", "kind": "store", "label": "Store", "parent": "data"},
        {"id": "queue", "kind": "queue", "label": "Queue", "style": "highlight", "parent": "tech"},
    ]
    data["edges"] = [{"from": "client", "to": "service"},
                     {"from": "service", "to": "store", "kind": "data", "style": "primary"},
                     {"from": "service", "to": "queue", "kind": "async", "dashed": True, "badge": 2}]
    scene = layout(data)
    legend = entries(scene, data)
    assert len(legend) == 13  # three lines, three zones, four nodes, two chips, one shared badge glyph
    assert {item["symbol"] for item in legend} == {"line", "zone", "box", "badge"}
    assert {(item["tint"], item["band"], item["dashed"]) for item in legend if item["symbol"] == "zone"} == {
        ("app", True, True), ("data", True, False), ("tech", False, False)}
    assert {item["shape"] for item in legend if item["symbol"] == "box"} == {"card", "database", "queue"}
    assert {item["style"] for item in legend if item.get("node_kind") == "chip"} == {"peer", "shared"}
    badge = next(item for item in legend if item["symbol"] == "badge")
    assert "Node badges identify elements" in badge["label"]
    assert "Numbers are labels for reference" in badge["label"]
    # Every laid-out caption has a glyph; asking again ignores generated swatches.
    for i, item in enumerate(legend):
        if item["symbol"] == "line":
            assert any(edge.id == f"legend-line-{i}" for edge in scene.edges)
        else:
            assert any(box.id == f"__legend-swatch-{i}" for box in scene.boxes)
    data["meta"]["legend_mode"] = "auto"
    assert entries(scene, data) == legend


def test_authored_selectors_merge_by_visual_meaning_without_unused_or_text_entries():
    data = model()
    data["meta"]["legend"] = [
        {"label": "Request", "symbol": "line"},
        {"label": "Send", "kind": "call"},
        {"label": "Send", "kind": "call"},
        {"label": "Not rendered", "symbol": "box", "style": "planned"},
        {"label": "Unbound prose"}, {"label": "Unbound text", "symbol": "text"},
    ]
    scene = layout(data)
    legend = entries(scene, data)
    assert [item["label"] for item in legend if item["symbol"] == "line"] == ["Send"]
    assert len(legend) == 3
    assert all(item["symbol"] != "text" and "Unbound" not in item["label"] and "Not rendered" not in item["label"] for item in legend)
    caption = next(item["label"] for item in legend if item["symbol"] == "box")
    data["meta"]["legend"].append({"label": caption.upper(), "symbol": "text"})
    assert len(entries(scene, data)) == len(legend)
    assert any(item["label"] == caption.upper() and item["symbol"] == "box" for item in entries(scene, data))


def test_ambiguous_symbol_note_cannot_replace_specific_card_meanings():
    data = model()
    data["meta"]["legend"] = [
        {"label": "Subject", "symbol": "box", "style": "primary"},
        {"label": "Persistent storage", "symbol": "box"}]
    legend = entries(layout(data), data)
    assert "Subject" in [entry["label"] for entry in legend]
    assert "Persistent storage" not in [entry["label"] for entry in legend]


def test_print_merges_identical_colors_and_shapes_but_keeps_actual_stroke_variants():
    data = model()
    scene = Scene("Encoding", "Encoding", 800, 600, theme="print")
    scene.boxes = [Box("peer", 0, 0, 100, 50), Box("external", 0, 0, 100, 50, style="external"),
                   Box("primary", 0, 0, 100, 50, style="primary"),
                   Box("task", 0, 0, 100, 50, kind="task"), Box("state", 0, 0, 100, 50, kind="state"),
                   Box("pill", 0, 0, 100, 50, role="chip")]
    scene.edges = [Connector("call", [], "", ""), Connector("data", [], "", "", kind="data"),
                   Connector("async", [], "", "", kind="async"),
                   Connector("reply", [], "", "", kind="reply"),
                   Connector("assoc", [], "", "", direction="--", kind="assoc"),
                   Connector("plain", [], "", "", direction="--", kind="async")]
    legend = entries(scene, data)
    boxes = [item for item in legend if item["symbol"] == "box"]
    lines = [item for item in legend if item["symbol"] == "line"]
    assert len(boxes) == 4  # ordinary, thick focus, rounded task/state, pill
    assert any("Elements in scope" in item["label"] and "External participant" in item["label"] for item in boxes)
    assert any("Task" in item["label"] and "State" in item["label"] for item in boxes)
    assert len(lines) == 3  # filled, open, unadorned; semantic kind alone is not a glyph


def test_zone_aliases_merge_only_when_tint_band_and_boundary_are_identical():
    data = model()
    scene = Scene("Zones", "Zones", 800, 600, theme="print", boxes=[
        Box("app", 0, 0, 100, 50, role="group", kind="boundary", tint="app"),
        Box("tech", 0, 0, 100, 50, role="group", kind="layer", tint="tech"),
        Box("dash", 0, 0, 100, 50, role="group", kind="boundary", dashed=True),
        Box("band", 0, 0, 100, 50, role="group", kind="boundary", band=False),
        Box("frame", 0, 0, 100, 50, role="group", kind="frame"),
    ])
    legend = entries(scene, data)
    assert len(legend) == 4
    assert "System boundary" in legend[0]["label"] and "Architecture layer" in legend[0]["label"]
    scene.theme = "neutral"
    assert len(entries(scene, data)) == 5


def test_line_markers_directions_and_dashes_match_svg_visual_distinctions():
    data = model()
    scene = Scene("Edges", "Edges", 800, 600)
    for direction, kind, dashed in [
        ("->", "call", False), ("->", "data", False), ("->", "dependency", False),
        ("->", "assoc", False), ("->", "async", False), ("->", "reply", False),
        ("->", "message", False), ("<->", "async", False), ("<->", "message", False),
        ("--", "call", False), ("--", "async", False), ("--", "message", False),
        ("->", "call", True),
    ]:
        scene.edges.append(Connector(str(len(scene.edges)), [], "", "", direction=direction,
                                     kind=kind, dashed=dashed))
    legend = entries(scene, data)
    assert len(legend) == 7  # filled/open/circle-start/bidirectional/plain/circle-only/dashed
    assert any("Data flow" in item["label"] and "Depends on" in item["label"] for item in legend)
    assert all(item["symbol"] == "line" for item in legend)


@pytest.mark.parametrize("ordered,phrase", [(False, "Numbers are labels for reference"), (True, "Numbers show flow order")])
@pytest.mark.parametrize("lang", ["en", "zh"])
def test_evidence_and_inline_number_semantics_attach_to_visible_swatches(ordered, phrase, lang):
    data = model()
    data["layout"]["ordered"] = ordered
    data["meta"].update(lang=lang, legend=[{"label": "Connection", "symbol": "line"},
                                         {"label": "Element", "symbol": "box"}])
    data["nodes"][0]["evidence"] = {"status": "inferred"}
    data["edges"][0].update(step=1, evidence={"status": "doc-only"})
    legend = entries(layout(data), data)
    line = next(item for item in legend if item["symbol"] == "line")
    assert (phrase if lang == "en" else "编号表示流程顺序" if ordered else "编号仅用于引用，不表示顺序") in line["label"]
    assert ("Documented only, not verified" if lang == "en" else "仅文档记载，未经核实") in line["label"]
    inferred = next(item for item in legend if item["symbol"] == "box" and item["dashed"])
    assert ("Inferred, not verified" if lang == "en" else "推断，未经核实") in inferred["label"]
    assert all(item["symbol"] != "text" for item in legend)


def test_unused_evidence_does_not_invent_legend_entries():
    data = model()
    data["nodes"][0]["evidence"] = {"status": "conflict"}
    data["edges"][0]["evidence"] = {"status": "inferred"}
    scene = Scene("Empty", "Empty", 800, 600)
    assert entries(scene, data) == []


def test_badge_values_select_real_values_and_share_one_swatch():
    data = model()
    scene = Scene("Badges", "Badges", 800, 600)
    for i in (1, 2):
        scene.boxes.append(Box(str(i), 0, 0, 30, 30, role="badge", style="highlight"))
        scene.texts.append(Text(str(i), [str(i)], 0, 0, 10, 15, owner=str(i), source=str(i)))
    data["meta"]["legend"] = [{"symbol": "badge", "badge": 2, "label": "Reference"},
                                {"symbol": "badge", "badge": 3, "label": "Unused"}]
    legend = entries(scene, data)
    assert len(legend) == 1
    assert legend[0]["badge"] == "2"
    assert legend[0]["label"] == "Reference / Node badges identify elements"


def test_swatch_svg_keeps_chip_card_zone_and_formal_shape_geometry():
    data = model()
    data["nodes"][0].update(chips=[{"label": "Transport", "style": "highlight"}])
    data["groups"] = [{"id": "scope", "kind": "boundary", "title": "Scope"}]
    data["nodes"][1]["parent"] = "scope"
    scene = layout(data)
    legend = entries(scene, data)
    root = ET.fromstring(render_svg(scene))
    for i, entry in enumerate(legend):
        if entry["symbol"] == "line":
            continue
        swatch = next(element for element in root if element.get("data-id") == f"__legend-swatch-{i}")
        role = "group" if entry["symbol"] == "zone" else "chip" if entry.get("node_kind") == "chip" else "node"
        original = next(element for element in root if element.get("data-role") == role and element.get("data-style") == entry["style"])
        assert {attr: swatch.get(attr) for attr in ("fill", "stroke", "stroke-width", "stroke-dasharray", "rx")} == {
            attr: original.get(attr) for attr in ("fill", "stroke", "stroke-width", "stroke-dasharray", "rx")}


@pytest.mark.parametrize("kind", ["actor", "gateway", "event", "initial", "final", "use_case", "task", "state"])
def test_formal_shapes_are_preserved_in_swatch_entries(kind):
    data = model()
    scene = Scene("Symbols", "Symbols", 800, 600,
                  boxes=[Box("symbol", 0, 0, 100, 80, kind=kind)])
    legend = entries(scene, data)
    assert len(legend) == 1
    assert legend[0]["node_kind"] == kind
    if kind == "event":
        scene.boxes.append(Box("end", 0, 0, 100, 80, kind=kind, event_type="end"))
        assert len(entries(scene, data)) == 2


def test_legend_does_not_mutate_inputs():
    data = model()
    scene = layout(data)
    before = deepcopy((scene, data))
    entries(scene, data)
    assert (scene, data) == before
