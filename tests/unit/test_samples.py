"""Every type page points at a sample SVG that exists, and every sample belongs to a page.

The samples themselves are rendered by tools/build_samples.py (needs the renderer and installed fonts).
"""
import json
import re
import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGES = ROOT / "content/en/types"
SAMPLES = ROOT / "content/public/samples"
sys.path.insert(0, str(ROOT / "tools"))
from scenario_samples import SCENARIO, load_manifest, sample_files

MANIFEST = load_manifest()
HEADLINES = {code: view for view in MANIFEST["views"] for code in view["headlines"]}
MODELS = [*(ROOT / "skills/architecture-diagrams/assets/templates").glob("*.json"),
          *(ROOT / "examples").glob("*/diagram.json"),
          *(source for source, _ in sample_files(MANIFEST) if source.name == "diagram.json")]


class SamplesTest(unittest.TestCase):
    def test_pages_point_at_existing_samples(self):
        for page in sorted(PAGES.glob("*.md")):
            section = page.read_text(encoding="utf-8").split("{#sample}", 1)[1]
            image = re.search(r"!\[[^\]]*\]\(/samples/([^)\s]+)\)", section)
            self.assertIsNotNone(image, page.name)
            code = page.stem.split("-")[0]
            expected = HEADLINES[code]["publication"] + "/en/diagram.svg" if code in HEADLINES else page.stem + ".svg"
            self.assertEqual(image.group(1), expected, page.name)
            self.assertTrue((SAMPLES / image.group(1)).exists(), page.name)

    def test_sample_sections_have_a_caption_and_no_pending_status(self):
        for language in ("en", "zh"):
            for page in sorted((ROOT / "content" / language / "types").glob("*.md")):
                section = page.read_text(encoding="utf-8").split("{#sample}", 1)[1]
                self.assertNotRegex(section, r"(?i)pending|not yet (available|provided)|待生成", page.name)
                caption = [line for line in section.splitlines() if line.startswith("*")]
                self.assertEqual(len(caption), 1, page.name)
                if language == "zh":
                    code = page.stem.split("-")[0]
                    expected = HEADLINES[code]["publication"] + "/zh/diagram.svg" if code in HEADLINES else page.stem + (".zh.svg" if (SAMPLES / (page.stem + ".zh.svg")).exists() else ".svg")
                    self.assertIn("(/samples/" + expected + ")", section, page.name)

    def test_every_sample_has_a_page(self):
        stems = {page.stem for page in PAGES.glob("*.md")}
        for sample in SAMPLES.glob("*.svg"):
            self.assertIn(sample.name.removesuffix(".zh.svg").removesuffix(".svg"), stems, sample.name)

    def test_manifest_owns_bilingual_author_artwork_and_publication_preserves_bytes(self):
        self.assertEqual({v["id"] for v in MANIFEST["views"]}, {"C2", "C3", "E1", "F1", "G1-AWS", "D2", "F2"})
        self.assertEqual(MANIFEST["vendorNeutralG1"]["status"], "P2b")
        for source, relative in sample_files():
            self.assertEqual(source.read_bytes(), (SAMPLES / relative).read_bytes(), str(relative))
        # Each language shares topology and labels from the frozen source (load_manifest
        # validates this); runtime identities and authority checks are not freely invented.
        facts = json.loads((SCENARIO / "scenario.json").read_text())
        self.assertEqual(sum(e["kind"] == "container" for e in facts["entities"].values()), 6)
        self.assertEqual(set(facts["tools"]), {"catalogue.lookup", "ticket.read", "ticket.create"})
        self.assertTrue(facts["tools"]["ticket.create"]["approval"])

    def test_sequence_alternatives_are_structured_operands_with_guards(self):
        """A branch drawn in one undivided frame would read as sequential steps, not as exclusive outcomes."""
        for model in MODELS:
            for frame in json.loads(model.read_text(encoding="utf-8")).get("frames", []):
                where = f"{model.parent.name}/{model.name}:{frame['id']}"
                self.assertIn("operator", frame, where)
                self.assertNotRegex(frame.get("label", ""), r"^(alt|par|loop|opt|break)\b", where)
                if frame["operator"] in ("alt", "par"):
                    self.assertGreaterEqual(len(frame.get("operands", [])), 2, where)


if __name__ == "__main__":
    unittest.main()
