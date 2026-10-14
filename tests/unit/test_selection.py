"""Invariants of the content model and the generated selection guide.

Runs with `python3 -m unittest discover -s tests/unit` or pytest; needs PyYAML.
"""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import build_selection as bs  # noqa: E402

V4_CODES = ([f"A{i}" for i in range(1, 9)] + [f"B{i}" for i in range(1, 5)]
            + [f"C{i}" for i in range(1, 9)] + [f"D{i}" for i in range(1, 4)]
            + [f"E{i}" for i in range(1, 5)] + [f"F{i}" for i in range(1, 4)]
            + [f"G{i}" for i in range(1, 5)] + ["H1", "H2", "I1", "I2"])


class ContentModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat, cls.tree = bs.load()
        cls.codes = {t["code"] for t in cls.cat["types"]}

    def test_all_guide_types_present(self):
        self.assertEqual(len(V4_CODES), 38)
        self.assertLessEqual(set(V4_CODES), self.codes)
        for t in self.cat["types"]:
            if t["code"] not in V4_CODES:
                self.assertIn("split_from", t, f"{t['code']} is new but not recorded as a split")

    def test_every_alias_maps_to_one_existing_type(self):
        owners = {}
        for row in bs.alias_index(self.cat):
            self.assertIn(row["code"], self.codes)
            key = bs.norm(row["text"])
            self.assertEqual(owners.setdefault(key, row["code"]), row["code"], row["text"])
        for term in self.cat["terms"]:
            self.assertTrue(term["types"])
            self.assertLessEqual(set(term["types"]), self.codes, term["en"])

    def test_tree_reaches_every_type(self):
        reached = {c for leaves in self.tree["root"].values() for leaf in leaves for c in leaf["types"]}
        self.assertEqual(reached, self.codes)

    def test_generated_outputs_are_current_and_idempotent(self):
        md = bs.CHOOSE_MD.read_text(encoding="utf-8")
        first = bs.build(self.cat, self.tree, md)
        second = bs.build(self.cat, self.tree, first[bs.CHOOSE_MD])
        self.assertEqual(first, second)
        for path, text in first.items():
            self.assertEqual(path.read_text(encoding="utf-8"), text, f"{path} is stale; run tools/build_selection.py")

    def test_validation_rejects_unreached_type_and_shared_alias(self):
        cat = copy.deepcopy(self.cat)
        tree = copy.deepcopy(self.tree)
        tree["root"]["views"] = [leaf for leaf in tree["root"]["views"] if "I1" not in leaf["types"]]
        with self.assertRaisesRegex(bs.ModelError, "does not reach.*I1"):
            bs.validate(cat, tree)
        cat["types"][1]["aliases"]["en"].append(cat["types"][0]["aliases"]["en"][0])
        with self.assertRaisesRegex(bs.ModelError, "move it to terms"):
            bs.validate(cat, self.tree)


if __name__ == "__main__":
    unittest.main()
