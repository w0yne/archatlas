import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from archatlas.cli import main


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
            self.assertEqual(main(["check", str(root / "out/diagram.svg"), "--report", str(root / "report.json"), "--browser"]), 2)
