"""Invariants of the generated skill type references.

Runs with `python3 -m unittest discover -s tests/unit` or pytest; needs PyYAML.
The vocabulary test also needs the model schema (`src/archatlas/model/schema.json`, or the file named
by ARCHATLAS_SCHEMA); it is skipped while the renderer is not merged.
"""
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import build_skill_refs as br  # noqa: E402

SCHEMA = Path(os.environ.get("ARCHATLAS_SCHEMA", ROOT / "src/archatlas/model/schema.json"))


class SkillRefsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs, cls.problems = br.build_all()

    def test_pages_build_within_budget(self):
        self.assertEqual(self.problems, [])
        self.assertEqual(len(self.outputs), len(list(br.PAGES.glob("*.md"))))

    def test_committed_references_are_current(self):
        for name, text in self.outputs.items():
            self.assertEqual((br.OUT / name).read_text(encoding="utf-8"), text, name)
        self.assertEqual({p.name for p in br.OUT.glob("*.md")}, set(self.outputs))

    def test_references_keep_recipe_and_drop_sources(self):
        for name, text in self.outputs.items():
            self.assertIn("\n## Drawing recipe\n", text, name)
            self.assertIn("**Self-check**", text, name)
            self.assertNotIn("## Sources", text, name)
            self.assertNotRegex(text, r"\[\d+\]", name)

    def test_over_budget_section_is_an_error_not_a_truncation(self):
        page = next(br.PAGES.glob("C2-*.md"))
        long_choose = page.read_text(encoding="utf-8").replace("## Notation and elements {#notation}",
                                                               "\n".join(f"- extra {i}" for i in range(20)) + "\n\n## Notation and elements {#notation}", 1)
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / page.name
            copy.write_text(long_choose, encoding="utf-8")
            _, problems = br.build_page(copy)
        self.assertTrue(any("section `choose`" in p and "budget 12" in p for p in problems), problems)

    @unittest.skipUnless(SCHEMA.exists(), "model schema not available")
    def test_template_sections_use_schema_vocabulary(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        defs = schema["$defs"]
        words = set(schema["properties"]) | set(schema["properties"]["layout"]["properties"]["template"]["enum"])
        for name in ("node", "edge", "group", "table", "evidence"):
            words |= set(defs[name]["properties"])
        for name in ("node", "edge", "group"):
            for prop in defs[name]["properties"].values():
                words |= set(prop.get("enum", []))
        words |= set(defs["evidence"]["properties"]["status"]["enum"])
        for name in ("frames", "activations"):
            words |= set(schema["properties"][name]["items"]["properties"])
        # Prose-level values the pages quote; everything else in the Template line must be schema vocabulary.
        words |= {"meta.description", "evidence.status", "cardinality{from,to}", "dashed: true", "tables[]", "groups[]",
                  "->", "--", "event [guard] / effect", "PK", "FK", "OHS", "ACL", "Row", "alt", "loop", "opt", "par"}
        unknown = []
        for page in sorted(br.PAGES.glob("*.md")):
            line = next(l for l in page.read_text(encoding="utf-8").split("\n") if l.startswith("Model template:"))
            line = re.sub(r"`assets/templates/[A-Z]\d+\.json`", "", line)
            for token in re.findall(r"`([^`]+)`", line):
                if re.fullmatch(r"[A-Z]\d+", token):
                    continue  # a store id such as D1
                if token not in words:
                    unknown.append(f"{page.name}: `{token}`")
        self.assertEqual(unknown, [], "not in the model schema")


if __name__ == "__main__":
    unittest.main()
