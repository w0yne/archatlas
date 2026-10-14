"""Font tests use generated public fixtures, never host-specific font paths."""

import builtins
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from archatlas.fonts import FontMetrics
from archatlas.fonts.coverage import CJK_SAMPLE, font_info
from archatlas.fonts.discover import discover


HAS_FONT_LIBRARIES = (
    importlib.util.find_spec("PIL") is not None
    and importlib.util.find_spec("fontTools") is not None
)


class EstimateTests(unittest.TestCase):
    def test_explicit_empty_paths_bypass_discovery(self):
        with patch("archatlas.fonts.discover.subprocess.run") as run:
            metrics = FontMetrics(paths=[])
        run.assert_not_called()
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertEqual(metrics.padding_factor, 1.12)
        self.assertEqual(metrics.family, "sans-serif")
        self.assertGreater(metrics.width("中文 API"), 0)
        self.assertTrue(metrics.warnings)
        json.dumps(metrics.doctor())

    def test_missing_optional_dependencies_degrade(self):
        original_import = builtins.__import__
        for missing in ("PIL", "fontTools"):
            def guarded(name, *args, **kwargs):
                if name == missing or name.startswith(missing + "."):
                    raise ImportError("optional dependency unavailable")
                return original_import(name, *args, **kwargs)

            with self.subTest(missing=missing), patch("builtins.__import__", guarded):
                metrics = FontMetrics(paths=[])
                self.assertGreater(metrics.width("Example 中文"), 0)
                self.assertEqual(metrics.measured_with, "estimate")
                self.assertIn("font-dependency", [w["rule"] for w in metrics.warnings])

    def test_wrap_preserves_words_and_newlines(self):
        metrics = FontMetrics(paths=[])
        limit = metrics.width("alpha beta")
        self.assertEqual(metrics.wrap("alpha beta gamma", limit), ["alpha beta", "gamma"])
        self.assertEqual(metrics.wrap("one\n\n二三\n", 100), ["one", "", "二三", ""])
        self.assertEqual(metrics.wrap("", 100), [""])

    def test_kinsoku_and_word_splitting(self):
        metrics = FontMetrics(paths=[])
        for text in ("甲乙，丙丁。戊己", "甲（乙丙）丁", "甲乙 ，丙丁"):
            lines = metrics.wrap(text, 48)
            self.assertEqual("".join(lines).replace(" ", ""), text.replace(" ", ""))
            for line in lines:
                self.assertFalse(line.startswith(tuple("，。、）")))
                self.assertFalse(line.endswith("（"))
                self.assertLessEqual(metrics.width(line), 48)
        lines = metrics.wrap("abcdefghij", 30)
        self.assertEqual("".join(lines), "abcdefghij")
        self.assertTrue(all(metrics.width(line) <= 30 for line in lines))

    def test_indivisible_units_warn_without_losing_text(self):
        metrics = FontMetrics(paths=[])
        self.assertEqual(metrics.wrap("甲，乙", 1), ["甲，", "乙"])
        self.assertEqual(metrics.wrap("e\u0301x", 1), ["e\u0301", "x"])
        self.assertIn("font-wrap-overflow", [w["rule"] for w in metrics.warnings])

    def test_numeric_validation_and_width_contract(self):
        metrics = FontMetrics(paths=[])
        self.assertEqual(metrics.width(""), 0.0)
        self.assertEqual(metrics.width("a\nabc"), metrics.width("abc"))
        self.assertEqual(metrics.width("abc", 32), metrics.width("abc", 16) * 2)
        for invalid in (0, -1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                metrics.width("x", invalid)
            with self.assertRaises(ValueError):
                metrics.wrap("x", invalid)

    def test_missing_fontconfig_uses_os_paths(self):
        with patch("archatlas.fonts.discover.subprocess.run", side_effect=FileNotFoundError), \
                patch("archatlas.fonts.discover._os_font_roots", return_value=[]):
            self.assertEqual(discover(), [])


@unittest.skipUnless(HAS_FONT_LIBRARIES, "Pillow and fontTools are optional")
class MeasuredTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temporary.name)
        cls.latin = cls.make_font("latin.ttf", "Noto Sans", range(32, 127), 500)
        cls.cjk = cls.make_font("cjk.ttf", "Noto Sans CJK SC",
                               {ord(c) for c in CJK_SAMPLE + "甲乙丙丁戊己"}, 1000)

    @classmethod
    def tearDownClass(cls):
        font_info.cache_clear()
        cls.temporary.cleanup()

    @classmethod
    def make_font(cls, filename, family, codepoints, advance):
        from fontTools.fontBuilder import FontBuilder
        from fontTools.pens.ttGlyphPen import TTGlyphPen

        points = sorted(codepoints)
        cmap = {code: f"uni{code:04X}" for code in points}
        order = [".notdef", *cmap.values()]
        builder = FontBuilder(1000, isTTF=True)
        builder.setupGlyphOrder(order)
        builder.setupCharacterMap(cmap)
        glyphs = {}
        for name in order:
            pen = TTGlyphPen(None)
            pen.moveTo((0, 0))
            pen.lineTo((advance - 50, 0))
            pen.lineTo((advance - 50, 700))
            pen.lineTo((0, 700))
            pen.closePath()
            glyphs[name] = pen.glyph()
        builder.setupGlyf(glyphs)
        builder.setupHorizontalMetrics({name: (advance, 0) for name in order})
        builder.setupHorizontalHeader(ascent=800, descent=-200)
        builder.setupNameTable({"familyName": family, "styleName": "Regular",
                                "uniqueFontIdentifier": family,
                                "fullName": family, "psName": family.replace(" ", "")})
        builder.setupOS2(sTypoAscender=800, sTypoDescender=-200,
                         usWinAscent=800, usWinDescent=200)
        builder.setupPost()
        builder.setupMaxp()
        path = cls.root / filename
        builder.save(path)
        return path

    def test_real_cmap_and_mixed_font_measurement(self):
        metrics = FontMetrics(paths=[self.cjk, self.latin])
        self.assertAlmostEqual(metrics.width("API中文", 20), 70)
        self.assertAlmostEqual(metrics.width("API中文", 12.5), 43.75, places=2)
        self.assertEqual(metrics.measured_with, "pillow")
        self.assertEqual(metrics.padding_factor, 1)
        self.assertEqual(metrics.family, '"Noto Sans", "Noto Sans CJK SC", sans-serif')
        report = metrics.doctor()
        self.assertTrue(report["cjk_coverage"]["complete"])
        self.assertEqual(report["mode"], "pillow")
        self.assertEqual(report["warnings"], [])
        json.dumps(report)
        self.assertNotIn(ord("中"), font_info(str(self.latin))[2])
        self.assertIn(ord("中"), font_info(str(self.cjk))[2])

    def test_missing_glyph_uses_estimate_instead_of_notdef(self):
        metrics = FontMetrics(paths=[self.latin])
        self.assertFalse(metrics.doctor()["cjk_coverage"]["complete"])
        self.assertEqual(metrics.width("中", 16), 16)
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertEqual(metrics.padding_factor, 1.12)
        metrics.width("中", 16)
        self.assertEqual(len([w for w in metrics.warnings
                              if w["rule"] == "font-missing-glyph"]), 1)

    def test_measured_wrap(self):
        metrics = FontMetrics(paths=[self.latin, self.cjk])
        self.assertEqual(metrics.wrap("API 中文服务", 48), ["API 中", "文服务"])
        lines = metrics.wrap("甲乙，丙丁。戊己", 48)
        self.assertEqual("".join(lines), "甲乙，丙丁。戊己")
        self.assertTrue(all(metrics.width(line) <= 48 for line in lines))
        self.assertTrue(all(not line.startswith(("，", "。")) for line in lines))

    def test_collection_selects_sc_face_and_matches_svg_family(self):
        from fontTools.ttLib import TTCollection, TTFont

        jp = self.make_font("jp.ttf", "Noto Sans CJK JP",
                            {ord(c) for c in CJK_SAMPLE}, 600)
        path = self.root / "regional.ttc"
        collection = TTCollection()
        collection.fonts = [TTFont(jp), TTFont(self.cjk)]
        try:
            collection.save(path)
        finally:
            collection.close()
        metrics = FontMetrics(paths=[path, self.latin])
        self.assertAlmostEqual(metrics.width("中文"), 32)
        self.assertIn('"Noto Sans CJK SC"', metrics.family)
        self.assertNotIn("CJK JP", metrics.family)
        self.assertEqual(metrics.doctor()["fonts"][1]["index"], 1)

    def test_fontconfig_and_os_fallback_discover_real_fonts(self):
        output = f"{self.latin}\t0\tNoto Sans\tRegular\n"
        with patch("archatlas.fonts.discover.subprocess.run",
                   return_value=subprocess.CompletedProcess([], 0, output, "")):
            self.assertEqual(discover()[0].family, "Noto Sans")
        with patch("archatlas.fonts.discover.subprocess.run", side_effect=FileNotFoundError), \
                patch("archatlas.fonts.discover._os_font_roots", return_value=[self.root]):
            metrics = FontMetrics()
            self.assertGreater(metrics.width("中文 API"), 0)
            self.assertEqual(metrics.measured_with, "pillow")

    def test_unreadable_font_degrades(self):
        path = self.root / "broken.ttf"
        path.write_bytes(b"not a font")
        metrics = FontMetrics(paths=[path])
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertIn("font-unreadable", [w["rule"] for w in metrics.warnings])


if __name__ == "__main__":
    unittest.main()
