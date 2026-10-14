import copy
import json
from pathlib import Path
import tempfile
import unittest

from archatlas.cli import initial
from archatlas.layout import layout
from archatlas.layout.route import segment_hits_rect
from archatlas.model import load, validate, ModelError
from archatlas.render import render_svg
from archatlas.render.legend import entries
from archatlas.check import check_svg

ROOT = Path(__file__).resolve().parents[2]


class SemanticLegendTests(unittest.TestCase):
    def labels(self, model):
        return [entry["label"] for entry in entries(layout(model), model)]

    def test_domain_defaults_never_emit_renderer_tokens(self):
        for family, code, expected in [
            ("er", "D1", "Relationship"), ("statechart", "E3", "State transition"),
            ("nested", "D2", "Data flow"), ("tree", "B3", "Decomposes into"),
            ("lanes", "A5", "Sequence flow"), ("nested", "C2", "System interaction"),
            ("lanes", "E4", "Handoff or next step"), ("lanes", "E2", "Control flow"),
        ]:
            model = initial(family)
            model["meta"]["type"] = code
            labels = self.labels(model)
            self.assertIn(expected, labels)
            self.assertFalse(set(labels) & {"call", "primary", "peer", "assoc", "dependency", "data"})

    def test_sequence_reply_is_distinct_from_inferred_request(self):
        model = initial("sequence")
        model["edges"].append({"from": "service", "to": "client", "dashed": True})
        self.assertIn("Request", self.labels(model))
        self.assertIn("Reply (dashed)", self.labels(model))
        model["edges"][1]["evidence"] = {"status": "inferred"}
        self.assertIn("Request (unverified)", self.labels(model))
        self.assertNotIn("Reply (dashed)", self.labels(model))
        model["meta"]["lang"] = "zh"
        self.assertIn("请求（未经核实）", self.labels(model))

    def test_authored_meanings_localize_and_replace_mode_is_exact(self):
        model = initial("nested")
        model["meta"].update(type="C2", legend_labels={
            "edges": {"call": "@request"}, "styles": {"primary": "@focus"}})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "diagram.json"
            path.write_text(json.dumps(model))
            (path.parent / "labels.zh.json").write_text(json.dumps({"request": "提交订单", "focus": "网店"}))
            resolved = load(path, "zh")
            self.assertIn("提交订单", self.labels(resolved))
            self.assertIn("网店", self.labels(resolved))
            resolved["meta"].update(legend_mode="replace", legend=[{"label": "实线表示提交订单"}])
            self.assertEqual(self.labels(resolved), ["实线表示提交订单"])
            resolved["meta"]["legend"] = []
            self.assertEqual(self.labels(resolved), [])

    def test_trust_and_deployment_boundaries_have_different_meanings(self):
        for code, expected in (("F2", "Trust boundary"), ("G1", "Deployment boundary")):
            model = initial("nested")
            model["meta"]["type"] = code
            model["groups"] = [{"id": "scope", "kind": "boundary", "title": "Scope"}]
            model["nodes"][1]["parent"] = "scope"
            self.assertIn(expected, self.labels(model))

    def test_minimum_and_maximum_cardinality_strings_are_preserved(self):
        model = initial("er")
        model["edges"][0]["label"] = "places"
        model["edges"][0]["cardinality"] = {"from": "1..1", "to": "0..*"}
        scene = layout(model)
        self.assertEqual({t.lines[0] for t in scene.texts if t.role == "cardinality"}, {"1..1", "0..*"})
        report = check_svg(render_svg(scene))
        self.assertEqual((report["errors"], report["warnings"]), (0, 0), report["findings"])

    def test_actor_association_label_uses_visible_glyph_clearance(self):
        model = load(ROOT / "skills/architecture-diagrams/assets/templates/I2.json")
        report = check_svg(render_svg(layout(model)))
        self.assertEqual((report["errors"], report["warnings"]), (0, 0), report["findings"])

    def test_reviewed_state_and_component_edges_leave_their_actual_sources(self):
        for code, source, target, unrelated in [
            ("E3", "new", "cancelled", "i"), ("C4", "svc", "pay", "repo")
        ]:
            scene = layout(load(ROOT / "skills/architecture-diagrams/assets/templates" / (code + ".json")))
            boxes = {box.id: box for box in scene.boxes}
            edge = next(e for e in scene.edges if (e.source, e.target) == (source, target))
            arrivals = [other.points[-1] for other in scene.edges if other.target == source and other.id != edge.id]
            self.assertNotIn(edge.points[0], arrivals)
            for a, b, c in zip(edge.points, edge.points[1:], edge.points[2:]):
                self.assertGreaterEqual((b[0] - a[0]) * (c[0] - b[0]) +
                                        (b[1] - a[1]) * (c[1] - b[1]), 0,
                                        "Automatic route must not contain a retraced spur")
            x, y, w, h = boxes[source].rect
            px, py = edge.points[0]
            self.assertTrue(abs(px - x) < 1 or abs(px - x - w) < 1 or abs(py - y) < 1 or abs(py - y - h) < 1)
            self.assertFalse(any(segment_hits_rect(a, b, boxes[unrelated].rect, 2)
                                 for a, b in zip(edge.points, edge.points[1:])))
            label = next(t for t in scene.texts if t.owner == edge.id and t.role == "edge-label")
            for other in scene.edges:
                if other.id != edge.id and other.kind != "legend":
                    self.assertFalse(any(segment_hits_rect(a, b, label.rect, 2)
                                         for a, b in zip(other.points, other.points[1:])))
            self.assertEqual(render_svg(scene), render_svg(layout(load(
                ROOT / "skills/architecture-diagrams/assets/templates" / (code + ".json")))))


class PoolFlowTests(unittest.TestCase):
    def model(self):
        return {"archatlas": "0.1", "meta": {"type": "A5", "title": "Return request"},
                "layout": {"template": "lanes", "direction": "LR"},
                "groups": [{"id": "customer", "kind": "pool", "title": "Customer"},
                           {"id": "shop", "kind": "pool", "title": "Shop"},
                           {"id": "support", "kind": "lane", "title": "Support", "parent": "shop"}],
                "nodes": [{"id": "review", "kind": "task", "label": "Review return", "parent": "support"},
                          {"id": "end", "kind": "event", "event_type": "end", "label": "Resolved",
                           "parent": "support"}],
                "edges": [{"from": "customer", "to": "review", "kind": "message"},
                          {"from": "review", "to": "end"}]}

    def test_pool_message_and_sequence_flow_boundaries(self):
        model = self.model()
        validate(model)
        scene = layout(model)
        message = next(e for e in scene.edges if e.source == "customer")
        self.assertTrue(message.dashed)
        self.assertEqual(message.kind, "message")
        for mutation in ("cross-call", "same-pool-message", "solid-message"):
            broken = copy.deepcopy(model)
            if mutation == "cross-call":
                broken["edges"][0]["kind"] = "call"
            elif mutation == "same-pool-message":
                broken["edges"][1]["kind"] = "message"
            else:
                broken["edges"][0]["dashed"] = False
            with self.subTest(mutation=mutation), self.assertRaises(ModelError):
                validate(broken)

    def test_event_variant_is_not_accepted_on_other_shapes(self):
        model = initial("nested")
        model["nodes"][0]["event_type"] = "end"
        with self.assertRaises(ModelError):
            validate(model)
