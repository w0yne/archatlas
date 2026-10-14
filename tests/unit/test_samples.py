"""Every type page points at a sample SVG that exists, and every sample belongs to a page.

The samples themselves are rendered by tools/build_samples.py (needs the renderer and installed fonts).
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGES = ROOT / "content/en/types"
SAMPLES = ROOT / "content/public/samples"
MODELS = [*(ROOT / "skills/architecture-diagrams/assets/templates").glob("*.json"), *(ROOT / "examples").glob("*/diagram.json")]


class SamplesTest(unittest.TestCase):
    def test_pages_point_at_existing_samples(self):
        for page in sorted(PAGES.glob("*.md")):
            section = page.read_text(encoding="utf-8").split("{#sample}", 1)[1]
            image = re.search(r"!\[[^\]]*\]\(/samples/([^)\s]+)\)", section)
            self.assertIsNotNone(image, page.name)
            self.assertEqual(image.group(1), page.stem + ".svg", page.name)
            self.assertTrue((SAMPLES / image.group(1)).exists(), page.name)

    def test_sample_sections_have_a_caption_and_no_pending_status(self):
        for language in ("en", "zh"):
            for page in sorted((ROOT / "content" / language / "types").glob("*.md")):
                section = page.read_text(encoding="utf-8").split("{#sample}", 1)[1]
                self.assertNotRegex(section, r"(?i)pending|not yet (available|provided)|待生成", page.name)
                caption = [line for line in section.splitlines() if line.startswith("*")]
                self.assertEqual(len(caption), 1, page.name)
                if language == "zh":
                    expected = page.stem + (".zh.svg" if (SAMPLES / (page.stem + ".zh.svg")).exists() else ".svg")
                    self.assertIn("(/samples/" + expected + ")", section, page.name)

    def test_every_sample_has_a_page(self):
        stems = {page.stem for page in PAGES.glob("*.md")}
        for sample in SAMPLES.glob("*.svg"):
            self.assertIn(sample.name.removesuffix(".zh.svg").removesuffix(".svg"), stems, sample.name)

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
