import copy
import os
import sys
import types
import unittest
from unittest.mock import MagicMock, patch

from archatlas.check.browser import check_browser, _measure
from archatlas.cli import initial
from archatlas.fonts import FontMetrics
from archatlas.layout import layout
from archatlas.render import render_svg


SVG = ('<svg xmlns="http://www.w3.org/2000/svg" data-archatlas="0.1" '
       'viewBox="0 0 300 200"><title>Example</title><desc>Example diagram</desc></svg>')


def measured():
    return {
        "canvas": [0, 0, 300, 200],
        "shapes": [
            {"id": "n", "role": "node", "parent": "", "kind": "system", "box": [20, 20, 100, 60]},
            {"id": "bg", "role": "label-bg", "parent": "edge", "kind": "", "box": [140, 30, 90, 30]}],
        "texts": [
            {"id": "name", "owner": "n", "role": "name", "box": [30, 30, 80, 20]},
            {"id": "label", "owner": "edge", "role": "edge-label", "box": [145, 35, 80, 20]}]}


class BrowserTests(unittest.TestCase):
    def test_pass_and_actual_overflow_overlap_background(self):
        geometry = measured()
        with patch("archatlas.check.browser._measure", return_value=geometry):
            report = check_browser(SVG)
        self.assertEqual(report["errors"], 0)
        self.assertEqual(report["browser"]["visual_review"], "pending")
        broken = copy.deepcopy(geometry)
        broken["texts"][0]["box"] = [110, 30, 100, 20]
        broken["shapes"][1]["box"] = [140, 30, 5, 30]
        with patch("archatlas.check.browser._measure", return_value=broken):
            report = check_browser(SVG)
        rules = {f["rule"] for f in report["findings"]}
        self.assertTrue({"browser-text-overflow", "browser-text-overlap",
                         "browser-label-background"} <= rules)
        self.assertEqual(report["errors"], len(report["findings"]))

    def test_rejects_unsafe_before_optional_import_or_launch(self):
        for payload in ('<script/>', '<foreignObject/>', '<image href="https://example.org/x"/>',
                        '<a href="https://example.org"/>', '<animateTransform/>',
                        '<rect onload="alert(1)"/>', '<rect fill="URL(https://example.org/x)"/>',
                        '<rect style="fill:red"/>', '<style>@import "https://example.org";</style>',
                        '<html xmlns="http://www.w3.org/1999/xhtml"/>'):
            with self.subTest(payload=payload), patch("archatlas.check.browser._measure") as measure:
                with self.assertRaises(ValueError):
                    check_browser(SVG.replace("</svg>", payload + "</svg>"))
                measure.assert_not_called()
        for svg in ("<!DOCTYPE svg>" + SVG, SVG.replace('data-archatlas="0.1"', ""), "<svg"):
            with self.subTest(svg=svg), patch("archatlas.check.browser._measure") as measure:
                with self.assertRaises(ValueError):
                    check_browser(svg)
                measure.assert_not_called()

    def test_missing_dependency_is_tool_error(self):
        with patch.dict(sys.modules, {"playwright.sync_api": None}):
            with self.assertRaisesRegex(RuntimeError, r"python -m pip install playwright"):
                check_browser(SVG)

    def test_offline_context_waits_for_fonts_measures_supplied_svg_and_closes(self):
        playwright = MagicMock()
        browser = playwright.chromium.launch.return_value
        context = browser.new_context.return_value
        page = context.new_page.return_value
        page.evaluate.return_value = measured()
        manager = MagicMock()
        manager.__enter__.return_value = playwright
        api = types.ModuleType("playwright.sync_api")
        api.sync_playwright = MagicMock(return_value=manager)
        api.Error = type("PlaywrightError", (Exception,), {})
        with patch.dict(sys.modules, {"playwright.sync_api": api}):
            self.assertEqual(_measure(SVG), measured())
        options = browser.new_context.call_args.kwargs
        self.assertTrue(options["offline"])
        self.assertFalse(options["java_script_enabled"])
        self.assertEqual(options["service_workers"], "block")
        pattern, handler = context.route.call_args.args
        self.assertEqual(pattern, "**/*")
        route = MagicMock()
        handler(route)
        route.abort.assert_called_once_with()
        content = page.set_content.call_args.args[0]
        self.assertIn(SVG, content)
        self.assertIn("default-src 'none'", content)
        script = page.evaluate.call_args.args[0]
        for operation in ("document.fonts.ready", "getBBox()", "getScreenCTM()", "matrixTransform"):
            self.assertIn(operation, script)
        self.assertNotIn("data-text-box", script)
        browser.close.assert_called_once_with()
        browser.close.reset_mock()
        page.evaluate.side_effect = api.Error("Measurement failed")
        with patch.dict(sys.modules, {"playwright.sync_api": api}):
            with self.assertRaisesRegex(RuntimeError, "Chromium geometry check failed"):
                _measure(SVG)
        browser.close.assert_called_once_with()
        playwright.chromium.launch.side_effect = api.Error("Executable doesn't exist")
        with patch.dict(sys.modules, {"playwright.sync_api": api}):
            with self.assertRaisesRegex(RuntimeError, "playwright install chromium"):
                _measure(SVG)

    @unittest.skipUnless(os.environ.get("ARCHATLAS_BROWSER_TESTS") == "1",
                         "Set ARCHATLAS_BROWSER_TESTS=1 with the browser extra and Chromium installed")
    def test_real_browser_uses_mutated_svg_geometry(self):
        svg = render_svg(layout(initial("nested"), FontMetrics()))
        self.assertEqual(check_browser(svg)["errors"], 0)
        from xml.etree import ElementTree as ET
        root = ET.fromstring(svg)
        text = next(e for e in root if e.get("data-role") == "name")
        for span in text.iter():
            if "x" in span.attrib:
                span.set("x", "9999")
        # Preserve the default namespace expected by the generated-SVG gate.
        ET.register_namespace("", "http://www.w3.org/2000/svg")
        report = check_browser(ET.tostring(root, encoding="unicode"))
        self.assertIn("browser-canvas-overflow", {f["rule"] for f in report["findings"]})
