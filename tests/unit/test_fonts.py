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
from archatlas.fonts.coverage import CJK_SAMPLE, font_info, font_weight
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
        self.assertTrue(metrics.family.startswith('"Noto Sans CJK SC",'))
        self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])
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
                self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])
                self.assertTrue(metrics.family.startswith('"Noto Sans CJK SC",'))
                self.assertTrue(metrics.runs("中")[0]["family"].startswith('"Noto Sans CJK SC",'))
                zh = FontMetrics(paths=[], lang="zh-CN")
                self.assertTrue(zh.family.startswith('"Noto Sans CJK SC",'))

    def test_language_and_detected_cjk_select_explicit_stack(self):
        zh = FontMetrics(paths=[], lang="zh")
        for family in ("Noto Sans CJK SC", "Source Han Sans SC",
                       "PingFang SC", "Microsoft YaHei"):
            self.assertIn(f'"{family}"', zh.family)
        for text in ("中文", "中文 API", "甲，乙", "𠀀"):
            for method in ("width", "wrap", "runs", "required_width"):
                with self.subTest(text=text, method=method):
                    metrics = FontMetrics(paths=[])
                    args = (text, 32) if method == "wrap" else (text,)
                    getattr(metrics, method)(*args)
                    self.assertTrue(metrics.family.startswith('"Noto Sans CJK SC",'))
                    self.assertEqual(metrics.measured_with, "estimate")
                    self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])

    def test_wrap_preserves_words_and_newlines(self):
        metrics = FontMetrics(paths=[])
        limit = metrics.width("alpha beta")
        self.assertEqual(metrics.wrap("alpha beta gamma", limit), ["alpha beta", "gamma"])
        self.assertEqual(metrics.wrap("one\n\n二三\n", 100), ["one", "", "二三", ""])
        self.assertEqual(metrics.wrap("", 100), [""])

    def test_kinsoku_and_intact_words(self):
        metrics = FontMetrics(paths=[])
        for text in ("甲乙，丙丁。戊己", "甲（乙丙）丁", "甲乙 ，丙丁"):
            lines = metrics.wrap(text, 48)
            self.assertEqual("".join(lines).replace(" ", ""), text.replace(" ", ""))
            for line in lines:
                self.assertFalse(line.startswith(tuple("，。、）")))
                self.assertFalse(line.endswith("（"))
                self.assertLessEqual(metrics.width(line), 48)
        lines = metrics.wrap("abcdefghij", 30)
        self.assertEqual(lines, ["abcdefghij"])
        for word in ("Checkout", "Shipped", "PaymentReceived", "vet_specialties",
                     "hard-hyphen-word", "e\u0301x"):
            self.assertEqual(metrics.wrap(word, 1), [word])
            self.assertEqual(metrics.wrap(f"before {word} after", 1),
                             ["before", word, "after"])
            self.assertEqual(metrics.required_width(word), metrics.width(word))

    def test_soft_hyphens_are_the_only_latin_hyphenation(self):
        metrics = FontMetrics(paths=[])
        text = "Pay\u00adment\u00adReceived"
        self.assertEqual(metrics.width(text), metrics.width("PaymentReceived"))
        self.assertEqual(metrics.wrap(text, 1000), ["PaymentReceived"])
        self.assertEqual(metrics.wrap(text, 80), ["Pay-", "ment-", "Received"])
        self.assertEqual(metrics.wrap(text, 1), ["Pay-", "ment-", "Received"])
        self.assertEqual(metrics.runs(text), [{"text": "PaymentReceived", "family": "sans-serif"}])
        self.assertEqual(metrics.required_width(text), metrics.width("Received"))
        self.assertEqual(metrics.required_width("abcd\u00ade"), metrics.width("abcd-"))
        self.assertEqual(metrics.wrap("a\u00ad", 1), ["a"])
        self.assertEqual(metrics.wrap("甲（乙\u00ad）丙", 32), ["甲", "（乙）", "丙"])

    def test_required_width_matches_wrap_boundaries(self):
        metrics = FontMetrics(paths=[])
        for text, widest in (("a PaymentReceived b", "PaymentReceived"),
                             ("甲，乙", "甲，"), ("甲（乙）丙", "（乙）"),
                             ("a\nvet_specialties", "vet_specialties"),
                             ("", ""), ("  \n ", "")):
            with self.subTest(text=text):
                required = metrics.required_width(text)
                self.assertEqual(required, metrics.width(widest))
                lines = metrics.wrap(text, max(1, required))
                self.assertTrue(all(metrics.width(line) <= max(1, required) for line in lines))

    def test_indivisible_units_warn_without_losing_text(self):
        metrics = FontMetrics(paths=[])
        self.assertEqual(metrics.wrap("甲，乙", 1), ["甲，", "乙"])
        self.assertEqual(metrics.wrap("e\u0301x", 1), ["e\u0301x"])
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
            with self.assertRaises(ValueError):
                metrics.required_width("x", invalid)

    def test_missing_fontconfig_uses_os_paths(self):
        with patch("archatlas.fonts.discover.subprocess.run", side_effect=FileNotFoundError), \
                patch("archatlas.fonts.discover._os_font_roots", return_value=[]):
            self.assertEqual(discover(), [])

    def test_weight_estimates_and_validation(self):
        metrics = FontMetrics(paths=[], lang="zh")
        self.assertEqual(metrics.width("API中文", weight=700), metrics.width("API中文"))
        self.assertEqual(metrics.wrap("Check\u00adout", 96, weight=700), ["Check-", "out"])
        self.assertEqual(metrics.required_width("Check\u00adout", weight=700), 96)
        self.assertTrue(metrics.runs("中", weight=700)[0]["family"].startswith('"Noto Sans CJK SC",'))
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])
        for invalid in (0, 500, "bold", None):
            with self.subTest(weight=invalid):
                for name, args in (("width", ("",)), ("wrap", ("", 100)),
                                   ("required_width", ("",)), ("runs", ("",))):
                    with self.assertRaises(ValueError):
                        getattr(metrics, name)(*args, weight=invalid)


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
        font_weight.cache_clear()
        cls.temporary.cleanup()

    @classmethod
    def make_font(cls, filename, family, codepoints, advance, weight=400):
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
        style = "Bold" if weight == 700 else "Regular"
        name = f"{family} {style}"
        builder.setupNameTable({"familyName": family, "styleName": style,
                                "uniqueFontIdentifier": name,
                                "fullName": name, "psName": name.replace(" ", "")})
        builder.setupOS2(sTypoAscender=800, sTypoDescender=-200,
                         usWinAscent=800, usWinDescent=200, usWeightClass=weight,
                         fsSelection=0x20 if weight == 700 else 0x40)
        builder.font["head"].macStyle = 1 if weight == 700 else 0
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
        self.assertTrue(metrics.family.startswith('"Noto Sans CJK SC",'))
        self.assertIn('"Noto Sans"', metrics.family)
        self.assertEqual(metrics.runs("API中文"),
                         [{"text": "API", "family": "Noto Sans"},
                          {"text": "中文", "family": "Noto Sans CJK SC"}])
        report = metrics.doctor()
        self.assertTrue(report["cjk_coverage"]["complete"])
        self.assertEqual(report["mode"], "pillow")
        self.assertEqual(report["warnings"], [])
        json.dumps(report)
        self.assertNotIn(ord("中"), font_info(str(self.latin))[2])
        self.assertIn(ord("中"), font_info(str(self.cjk))[2])

    def test_bold_face_advances_drive_all_text_apis(self):
        bold = self.make_font("latin-bold.ttf", "Noto Sans", range(32, 127), 750, 700)
        cjk_bold = self.make_font("cjk-bold.ttf", "Noto Sans CJK SC",
                                  {ord(c) for c in CJK_SAMPLE}, 1200, 700)
        metrics = FontMetrics(paths=[bold, cjk_bold, self.latin, self.cjk])
        for weight, advance in ((700, 69), (400, 50), (700, 69)):
            with self.subTest(weight=weight):
                self.assertEqual(metrics.runs("API中", weight),
                                 [{"text": "API", "family": "Noto Sans"},
                                  {"text": "中", "family": "Noto Sans CJK SC"}])
                self.assertAlmostEqual(metrics.width("API中", 20, weight), advance)
                self.assertAlmostEqual(metrics.width("API中", 12.5, weight),
                                       advance * 12.5 / 20, delta=1 / 64)
        self.assertEqual(metrics.wrap("Checkout Shipped", 128), ["Checkout Shipped"])
        self.assertEqual(metrics.wrap("Checkout Shipped", 128, weight=700), ["Checkout", "Shipped"])
        self.assertEqual(metrics.wrap("Check\u00adout", 72, weight=700), ["Check-", "out"])
        self.assertEqual(metrics.required_width("Check\u00adout", weight=700), 72)
        self.assertEqual(metrics.required_width("Checkout Shipped", weight=700), 96)
        self.assertEqual(metrics.measured_with, "pillow")
        self.assertEqual(metrics.warnings, [])

    def test_bold_fallback_family_matches_measured_face(self):
        bold = self.make_font("fallback-bold.ttf", "Fallback Sans", range(32, 127), 750, 700)
        metrics = FontMetrics(paths=[self.latin, bold, self.cjk])
        self.assertEqual(metrics.width("API", weight=700), 36)
        self.assertEqual(metrics.runs("API", weight=700),
                         [{"text": "API", "family": "Fallback Sans"}])
        self.assertEqual(metrics.width("API"), 24)
        self.assertEqual(metrics.runs("API"), [{"text": "API", "family": "Noto Sans"}])
        self.assertEqual(metrics.measured_with, "pillow")
        # Regular CJK coverage cannot stand in for a measured bold CJK face.
        self.assertEqual(metrics.width("中文", weight=700), 32)
        self.assertTrue(metrics.runs("中文", weight=700)[0]["family"].startswith('"Noto Sans CJK SC",'))
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertIn("font-weight-unavailable", [w["rule"] for w in metrics.warnings])
        self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])

    def test_unavailable_bold_is_estimated_not_reported_as_regular_measurement(self):
        metrics = FontMetrics(paths=[self.latin])
        self.assertEqual(metrics.width("API"), 24)
        self.assertEqual(metrics.width("API", weight=700), 48)
        self.assertEqual(metrics.runs("API", weight=700),
                         [{"text": "API", "family": "sans-serif"}])
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertIn("font-weight-unavailable", [w["rule"] for w in metrics.warnings])

    def test_missing_glyph_uses_estimate_instead_of_notdef(self):
        metrics = FontMetrics(paths=[self.latin])
        self.assertFalse(metrics.doctor()["cjk_coverage"]["complete"])
        self.assertEqual(metrics.width("中", 16), 16)
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertEqual(metrics.padding_factor, 1.12)
        self.assertTrue(metrics.runs("中")[0]["family"].startswith('"Noto Sans CJK SC",'))
        self.assertEqual(metrics.runs("API")[0]["family"], "Noto Sans")
        self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])
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
        for word in ("Checkout", "Shipped", "PaymentReceived", "vet_specialties",
                     "hard-hyphen"):
            self.assertEqual(metrics.wrap(word, 1), [word])
            self.assertEqual(metrics.required_width(word), metrics.width(word))
        self.assertEqual(metrics.wrap("Check\u00adout", 48), ["Check-", "out"])
        self.assertEqual(metrics.required_width("Check\u00adout"), 48)

    def test_cjk_measurement_failure_warns_even_with_verified_coverage(self):
        metrics = FontMetrics(paths=[self.latin, self.cjk])
        face = metrics._choice("中")
        with patch.object(metrics._font_cache[(face, 16)], "getlength",
                          side_effect=OSError("measurement unavailable")):
            self.assertEqual(metrics.width("中"), 16)
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])
        self.assertEqual(metrics.runs("中"), [{"text": "中", "family": "Noto Sans CJK SC"}])

    def test_probe_coverage_does_not_hide_missing_actual_cjk(self):
        metrics = FontMetrics(paths=[self.latin, self.cjk])
        self.assertTrue(metrics.doctor()["cjk_coverage"]["complete"])
        self.assertEqual(metrics.wrap("中文𠀀", 16), ["中", "文", "𠀀"])
        self.assertEqual(metrics.measured_with, "estimate")
        self.assertIn("cjk-glyph-coverage", [w["rule"] for w in metrics.warnings])
        self.assertEqual(metrics.runs("中")[0]["family"], "Noto Sans CJK SC")
        self.assertTrue(metrics.runs("𠀀")[0]["family"].startswith('"Noto Sans CJK SC",'))

    def test_measured_cjk_run_keeps_its_actual_family(self):
        han = self.make_font("han.ttf", "Fixture Han", {ord(c) for c in CJK_SAMPLE}, 750)
        metrics = FontMetrics(paths=[han, self.latin], lang="zh")
        self.assertEqual(metrics.width("中文"), 24)
        self.assertEqual(metrics.runs("中文"), [{"text": "中文", "family": "Fixture Han"}])
        self.assertTrue(metrics.family.startswith('"Noto Sans CJK SC",'))
        self.assertEqual(metrics.measured_with, "pillow")
        self.assertEqual(metrics.warnings, [])

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
