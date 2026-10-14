"""CairoSVG must place mixed-font lines like a browser, without losing spaces."""
from io import BytesIO
import shutil
import subprocess
from xml.etree import ElementTree as ET

import pytest

from archatlas.cli import initial
from archatlas.fonts import FontMetrics
from archatlas.layout import layout
from archatlas.render import render_svg


def mixed_scene(anchor):
    metrics = FontMetrics()
    model = initial("nested")
    model["nodes"][0].update(label="Online shop 网店系统\n支付 API 服务",
                             size_hint={"width": 400})
    scene = layout(model, metrics)
    if scene.measured_with != "pillow":
        pytest.skip("Mixed-script raster comparison needs measured Latin and CJK fonts")
    text = next(t for t in scene.texts if t.id == "client-name")
    text.anchor, text.x, text.y = anchor, 350, 20
    scene.texts, scene.boxes, scene.edges = [text], [], []
    scene.width, scene.height = 800, 110
    return scene, text, metrics


@pytest.mark.parametrize("anchor", ["start", "middle", "end"])
def test_mixed_lines_have_explicit_start_positions_and_independent_spaces(anchor):
    scene, text, metrics = mixed_scene(anchor)
    root = ET.fromstring(render_svg(scene))
    element = next(e for e in root if e.tag.endswith("}text"))
    assert element.get("text-anchor") == "start"
    for i, span in enumerate(element):
        left = text.x - metrics.width(text.lines[i], text.size, weight=text.weight) * {"start": 0, "middle": .5, "end": 1}[anchor]
        assert float(span.get("x")) == pytest.approx(left, abs=.001)
        assert "".join(span.itertext()) == text.lines[i]
        assert any(run.text == " " for run in span)
        offset = 0
        for run in span:
            assert float(run.get("x")) == pytest.approx(left + offset, abs=.001)
            offset += metrics.width(run.text, text.size, weight=text.weight)


@pytest.mark.parametrize("anchor", ["start", "middle", "end"])
def test_cairo_mixed_run_ink_matches_measured_positions_and_rsvg(anchor):
    cairo = pytest.importorskip("cairosvg")
    from PIL import Image
    scene, text, metrics = mixed_scene(anchor)
    root = ET.fromstring(render_svg(scene))
    element = next(e for e in root if e.tag.endswith("}text"))
    # Hide other runs without removing their text or positions. Their advance
    # still participates in layout; only this run contributes visible pixels.
    runs = [(i, run) for i, span in enumerate(element) for run in span]
    for _, run in runs:
        run.set("fill", "none")
    for line_index, run in runs:
        if run.text.isspace():
            continue
        run.set("fill", "#000000")
        svg = ET.tostring(root)
        rendered = [Image.open(BytesIO(cairo.svg2png(bytestring=svg))).convert("L")]
        rsvg = shutil.which("rsvg-convert")
        if rsvg:
            png = subprocess.run([rsvg], input=svg, capture_output=True, check=True).stdout
            rendered.append(Image.open(BytesIO(png)).convert("L"))
        bounds = []
        left, width = float(run.get("x")), metrics.width(run.text, text.size, weight=text.weight)
        for image in rendered:
            box = image.point(lambda value: 255 if value < 220 else 0).getbbox()
            assert box is not None
            x0, _, x1, _ = box
            assert left - 2 <= x0 <= left + 3, (anchor, run.text, left, box)
            assert left + width - 4 <= x1 <= left + width + 2, (anchor, run.text, left, width, box)
            bounds.append((x0, x1))
        if len(bounds) == 2:
            assert bounds[0] == pytest.approx(bounds[1], abs=2)
        run.set("fill", "none")
