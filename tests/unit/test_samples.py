"""Every type page points at a sample SVG that exists, and every sample belongs to a page.

The samples themselves are rendered by tools/build_samples.py (needs the renderer and installed fonts).
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGES = ROOT / "content/en/types"
SAMPLES = ROOT / "content/public/samples"


class SamplesTest(unittest.TestCase):
    def test_pages_point_at_existing_samples(self):
        for page in sorted(PAGES.glob("*.md")):
            section = page.read_text(encoding="utf-8").split("{#sample}", 1)[1]
            image = re.search(r"!\[[^\]]*\]\(/samples/([^)\s]+)\)", section)
            self.assertIsNotNone(image, page.name)
            self.assertEqual(image.group(1), page.stem + ".svg", page.name)
            self.assertTrue((SAMPLES / image.group(1)).exists(), page.name)

    def test_every_sample_has_a_page(self):
        stems = {page.stem for page in PAGES.glob("*.md")}
        for sample in SAMPLES.glob("*.svg"):
            self.assertIn(sample.name.removesuffix(".zh.svg").removesuffix(".svg"), stems, sample.name)


if __name__ == "__main__":
    unittest.main()
