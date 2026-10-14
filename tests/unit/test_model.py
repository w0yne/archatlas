import copy
import json
from pathlib import Path
import tempfile
import unittest

from archatlas.cli import initial
from archatlas.model import ModelError, load, validate


class ModelTests(unittest.TestCase):
    def test_schema_and_relationship_invariants(self):
        original = initial("nested")
        validate(original)
        for change in ("duplicate", "missing", "cycle", "columns"):
            model = copy.deepcopy(original)
            if change == "duplicate":
                model["nodes"][1]["id"] = "client"
            elif change == "missing":
                model["edges"][0]["to"] = "absent"
            elif change == "cycle":
                model["groups"] = [{"id": "group", "kind": "boundary", "title": "Group", "parent": "group"}]
            else:
                model = initial("grid_table")
                model["tables"][0]["rows"][0].append("extra")
            with self.subTest(change=change), self.assertRaises(ModelError):
                validate(model)

    def test_localization_keeps_topology_and_fails_explicit_missing_key(self):
        model = initial("nested")
        model["nodes"][0]["label"] = "@client_label"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "diagram.json"
            path.write_text(json.dumps(model))
            with self.assertRaises(ModelError):
                load(path)
            (root / "labels.zh.json").write_text(json.dumps({"client_label": "顾客客户端"}))
            result = load(path, "zh")
            self.assertEqual(result["nodes"][0]["label"], "顾客客户端")
            self.assertEqual(result["edges"], model["edges"])
            self.assertEqual(result["nodes"][0]["id"], "client")

    def test_invalid_sequence_ranges_and_unknown_fields_fail(self):
        model = initial("sequence")
        model["activations"] = [{"node": "client", "from_step": 1, "to_step": 2}]
        with self.assertRaises(ModelError):
            validate(model)
        model = initial("nested")
        model["nodes"][0]["x"] = 200
        with self.assertRaises(ModelError):
            validate(model)
