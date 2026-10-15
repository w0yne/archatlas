"""Styled components preserve measured ownership, ports and notation."""
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest

from archatlas.check import check_svg
from archatlas.check.report import on_shape
from archatlas.cli import initial
from archatlas.layout import layout
from archatlas.model import load, validate, ModelError
from archatlas.model.loader import resolve
from archatlas.render import render_svg

FIXTURE = Path(__file__).parents[1] / "fixtures/styles/components.json"


@pytest.mark.parametrize("theme", ["neutral", "print", "dark"])
def test_components_have_valid_owned_geometry_and_contrast(theme):
    model = load(FIXTURE)
    model["meta"]["theme"] = theme
    scene = layout(model)
    svg = render_svg(scene)
    assert render_svg(layout(model)) == svg
    report = check_svg(svg)
    assert not report["errors"], report["findings"]
    root = ET.fromstring(svg)
    assert any(e.get("data-role") == "header-band" for e in root)
    assert any(e.get("data-role") == "chip" for e in root)
    assert any(e.get("data-role") == "badge" for e in root)
    assert any(e.get("data-role") == "legend-panel" for e in root)
    shapes = {e.get("data-id"): e for e in root if e.get("data-role") == "node"}
    assert shapes["orders"].get("data-shape") == "database"
    assert shapes["receipt"].get("data-shape") == "document"
    for edge in scene.edges:
        if edge.source in shapes:
            assert on_shape(edge.points[0], shapes[edge.source])
            assert on_shape(edge.points[-1], shapes[edge.target])
    primary_name = next(e for e in root if e.get("data-id") == "api-name")
    assert primary_name.get("font-weight") == "700"
    if theme == "neutral":
        assert primary_name.get("fill") == "#ffffff"


def test_chip_overflow_and_badge_mutations_are_visible_to_qa():
    root = ET.fromstring(render_svg(layout(load(FIXTURE))))
    chip = next(e for e in root if e.get("data-role") == "chip")
    chip.set("width", "5")
    report = check_svg(ET.tostring(root, encoding="unicode"))
    assert "text-overflow" in {f["rule"] for f in report["findings"]}


def test_new_text_localizes_and_formal_symbols_reject_visual_overrides():
    model = initial("nested")
    model["meta"]["subtitle"] = "@subtitle"
    model["nodes"][0].update(chips=["@chip", {"label": "@chip", "style": "highlight"}], badge="@b")
    translated = resolve(model, {"subtitle": "处理边界", "chip": "共享", "b": "一"})
    assert translated["meta"]["subtitle"] == "处理边界"
    assert translated["nodes"][0]["chips"] == ["共享", {"label": "共享", "style": "highlight"}]
    assert translated["nodes"][0]["badge"] == "一"
    for field, value in (("shape", "document"), ("chips", ["HTTP"]), ("badge", 1)):
        invalid = initial("nested")
        invalid["nodes"][0].update(kind="actor", **{field: value})
        with pytest.raises(ModelError, match="Formal symbols"):
            validate(invalid)
