"""Every type page points at a sample SVG that exists, and every sample belongs to a page.

The samples themselves are rendered by tools/build_samples.py (needs the renderer and installed fonts).
"""
import json
import re
import unittest
import sys
import yaml
from unittest.mock import patch
import tempfile
import shutil
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
        registry = yaml.safe_load((ROOT / "content/data/types.yaml").read_text())["types"]
        core = {t["code"] for t in registry if t["catalogRole"] == "core"}
        self.assertEqual({v["code"] for v in MANIFEST["views"] if v["catalogRole"] == "core"}, core)
        self.assertEqual(len(MANIFEST["views"]), 29)
        self.assertEqual({v["code"] for v in MANIFEST["views"] if v["catalogRole"] == "variant"}, {"F1", "F2", "E4", "G2"})
        self.assertEqual(MANIFEST["vendorNeutralG1"]["status"], "complete")
        self.assertEqual(HEADLINES["G1"]["id"], "G1-AWS")
        self.assertEqual(HEADLINES["E2"]["id"], "E2")
        for source, relative in sample_files():
            self.assertEqual(source.read_bytes(), (SAMPLES / relative).read_bytes(), str(relative))
        # Each language shares topology and labels from the frozen source (load_manifest
        # validates this); runtime identities and authority checks are not freely invented.
        facts = json.loads((SCENARIO / "scenario.json").read_text())
        self.assertEqual(sum(e["kind"] == "container" for e in facts["entities"].values()), 6)
        self.assertEqual(set(facts["tools"]), {"catalogue.lookup", "ticket.read", "ticket.create"})
        self.assertTrue(facts["tools"]["ticket.create"]["approval"])

    def test_projection_contract_rejects_invented_components_and_label_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "scenario"
            shutil.copytree(SCENARIO, dest)
            with patch("scenario_samples.SCENARIO", dest):
                path = dest / "views/E3/en/diagram.json"
                original = path.read_text()
                model = json.loads(original)
                model["nodes"][1]["label"] = "Unregistered state"
                path.write_text(json.dumps(model))
                with self.assertRaisesRegex(ValueError, "Label drift"):
                    load_manifest()
                path.write_text(original)
                model = json.loads(original)
                model["nodes"][1]["kind"] = "container"
                path.write_text(json.dumps(model))
                with self.assertRaisesRegex(ValueError, "Invalid semantic projection"):
                    load_manifest()

    def test_shared_policy_and_responsibility_tables_are_not_independent_grants(self):
        facts = json.loads((SCENARIO / "scenario.json").read_text())
        policy = facts["assumptions"]["AS-policy"]["details"]["roleMatrix"]
        roles = ["R-employee", "R-steward", "R-operator"]
        raci = facts["assumptions"]["AS-raci"]["details"]["rows"]
        for lang in ("en", "zh"):
            acl = json.loads((SCENARIO / f"views/F3/{lang}/diagram.json").read_text())["tables"][0]["rows"]
            self.assertEqual([row[1:] for row in acl], [policy[role] for role in roles])
            matrix = json.loads((SCENARIO / f"views/H1/{lang}/diagram.json").read_text())["tables"][0]["rows"]
            self.assertEqual([row[1:] for row in matrix], [row[1:] for row in raci])
        for row in raci:
            self.assertEqual(sum("A" in cell for cell in row[1:]), 1, row)
            self.assertTrue(any("R" in cell for cell in row[1:]), row)
        self.assertEqual(facts["flows"]["FL-ingest"]["path"][:4], ["R-steward", "C-api", "Q-ingest", "C-ingest"])
    def test_sequence_alternatives_are_structured_operands_with_guards(self):
        """A branch drawn in one undivided frame would read as sequential steps, not as exclusive outcomes."""
        for model in MODELS:
            for frame in json.loads(model.read_text(encoding="utf-8")).get("frames", []):
                where = f"{model.parent.name}/{model.name}:{frame['id']}"
                self.assertIn("operator", frame, where)
                self.assertNotRegex(frame.get("label", ""), r"^(alt|par|loop|opt|break)\b", where)
                if frame["operator"] in ("alt", "par"):
                    self.assertGreaterEqual(len(frame.get("operands", [])), 2, where)

    def test_ai_data_flows_have_no_miracle_or_black_hole_processes(self):
        for view in MANIFEST["views"]:
            if view["code"] not in {"D2", "F2"}:
                continue
            for lang in view["languages"]:
                model = json.loads((SCENARIO / view["source"] / lang / "diagram.json").read_text())
                kinds = {n["id"]: n["kind"] for n in model["nodes"]}
                for node, kind in kinds.items():
                    if kind == "process":
                        self.assertTrue(any(e["to"] == node for e in model["edges"]), node)
                        self.assertTrue(any(e["from"] == node for e in model["edges"]), node)
                for edge in model["edges"]:
                    self.assertIn("process", (kinds[edge["from"]], kinds[edge["to"]]), edge["id"])
                    self.assertEqual(edge["kind"], "data")


if __name__ == "__main__":
    unittest.main()
