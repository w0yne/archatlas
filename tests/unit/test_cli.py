import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from archatlas.cli import main, initial
from archatlas.model import load


class CLITests(unittest.TestCase):
    def test_offline_render_check_and_explicit_optional_limit(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            root = Path(temp)
            self.assertEqual(main(["init", "nested", "-o", str(root / "model.json")]), 0)
            self.assertEqual(main(["render", str(root / "model.json"), "-o", str(root / "out")]), 0)
            self.assertEqual(main(["check", str(root / "out/diagram.svg"), "--report", str(root / "findings.json")]), 0)
            self.assertEqual(json.loads((root / "findings.json").read_text())["errors"], 0)
            model = json.loads((root / "model.json").read_text())
            model["nodes"][0]["id"] = "another"
            model["edges"][0]["from"] = "another"
            (root / "mismatch.json").write_text(json.dumps(model))
            self.assertEqual(main(["check", str(root / "out/diagram.svg"), "--model", str(root / "mismatch.json"),
                                   "--report", str(root / "mismatch.findings.json")]), 1)
            self.assertEqual(main(["render", str(root / "model.json"), "-o", str(root), "--embed-font-subset"]), 2)
            with patch("archatlas.check.browser._measure", side_effect=RuntimeError("Browser unavailable")):
                self.assertEqual(main(["check", str(root / "out/diagram.svg"), "--report",
                                       str(root / "report.json"), "--browser"]), 2)
            report = json.loads((root / "report.json").read_text())
            self.assertEqual(report["browser"]["status"], "tool-error")
            self.assertEqual(report["visual_review"], "pending")

    def test_init_uses_shipped_type_model(self):
        source = Path(__file__).resolve().parents[2] / "skills/architecture-diagrams/assets/templates/A1.json"
        original = source.read_bytes()
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "model.json"
            self.assertEqual(main(["init", "a1", "-o", str(destination)]), 0)
            self.assertEqual(load(destination), load(source))
        self.assertEqual(source.read_bytes(), original)

    def test_init_explicit_templates_resolves_labels_and_metadata_filename(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            assets = root / "templates"
            assets.mkdir()
            model = initial("nested")
            model["meta"].update(type="X42", title="@title")
            model["nodes"][0]["label"] = "@client"
            source = assets / "X42-example.json"
            source.write_text(json.dumps(model))
            (assets / "labels.en.json").write_text(json.dumps({"title": "Example", "client": "Reader"}))
            original = source.read_bytes()
            destination = root / "elsewhere/model.json"
            self.assertEqual(main(["init", "X42", "--templates", str(assets), "-o", str(destination)]), 0)
            self.assertEqual(load(destination)["nodes"][0]["label"], "Reader")
            self.assertEqual(load(destination)["meta"]["title"], "Example")
            self.assertEqual(source.read_bytes(), original)
            self.assertFalse(destination.with_name("labels.en.json").exists())
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(["init", "missing", "--templates", str(assets), "-o", str(destination)]), 2)

    def test_copied_skill_and_vendored_library_discovery(self):
        from archatlas.cli import template_directories
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp) / "architecture-diagrams"
            assets = skill / "assets/templates"
            assets.mkdir(parents=True)
            with patch("archatlas.cli.__file__", str(skill / "scripts/lib/archatlas/cli.py")):
                self.assertIn(assets, template_directories())
            with patch("sys.argv", [str(skill / "scripts/atlas")]):
                self.assertIn(assets, template_directories())

    def test_check_language_and_translated_model(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()):
            root = Path(temp)
            model = initial("nested")
            model["meta"]["title"] = "@title"
            model["nodes"][0]["label"] = "@client"
            model_path = root / "model.json"
            model_path.write_text(json.dumps(model))
            (root / "labels.en.json").write_text(json.dumps({"title": "Diagram", "client": "Reader"}))
            (root / "labels.zh.json").write_text(json.dumps({"title": "系统", "client": "用户"}))
            svg = root / "diagram.svg"
            report_path = root / "findings.json"
            self.assertEqual(main(["render", str(model_path), "--lang", "zh", "-o", str(svg)]), 0)
            args = ["check", str(svg), "--model", str(model_path), "--report", str(report_path)]
            with patch("archatlas.cli.load", wraps=load) as loader:
                self.assertEqual(main(args + ["--lang", "zh"]), 0)
                loader.assert_called_once_with(str(model_path), "zh")
            self.assertEqual(main(args), 0)  # Infer locale from the supplied SVG.
            self.assertEqual(main(args + ["--lang", "en"]), 1)
            report = json.loads(report_path.read_text())
            self.assertIn("language-mismatch", [f["rule"] for f in report["findings"]])
            self.assertEqual(main(["check", str(svg), "--lang", "en", "--report", str(report_path)]), 1)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(args + ["--lang", "../en"]), 2)

    def test_browser_findings_merge_and_unsafe_svg_never_launches(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()):
            root = Path(temp)
            main(["init", "nested", "-o", str(root / "model.json")])
            main(["render", str(root / "model.json"), "-o", str(root)])
            svg = root / "diagram.svg"
            svg.write_text(svg.read_text().replace('lang="en"', 'lang="zh"'))
            report_path = root / "report.json"
            args = ["check", str(svg), "--lang", "en", "--browser", "--report", str(report_path)]
            browser_result = {
                "findings": [{"id": "finding-1", "rule": "browser-text-overflow", "severity": "error",
                              "message": "Overflow", "elements": [], "boxes": []}],
                "browser": {"status": "checked", "visual_review": "pending"}}
            with patch("archatlas.check.browser.check_browser", return_value=browser_result) as browser:
                self.assertEqual(main(args), 1)
                browser.assert_called_once_with(svg.read_text())
            report = json.loads(report_path.read_text())
            self.assertEqual(report["errors"], sum(f["severity"] == "error" for f in report["findings"]))
            self.assertEqual(report["warnings"], sum(f["severity"] == "warning" for f in report["findings"]))
            self.assertEqual(len({f["id"] for f in report["findings"]}), len(report["findings"]))
            svg.write_text(svg.read_text().replace("</svg>", "<script>alert(1)</script></svg>"))
            with patch("archatlas.check.browser.check_browser") as browser:
                self.assertEqual(main(args), 1)
                browser.assert_not_called()
            self.assertEqual(json.loads(report_path.read_text())["browser"]["status"], "blocked")
