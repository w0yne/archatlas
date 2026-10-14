import copy
import json
from pathlib import Path
import unittest
from xml.etree import ElementTree as ET

from archatlas.check import check_svg
from archatlas.cli import initial
from archatlas.fonts import FontMetrics
from archatlas.layout import layout
from archatlas.layout.base import Box, Text
from archatlas.model import load
from archatlas.render import render_svg

ROOT = Path(__file__).resolve().parents[1]


class PipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metrics = FontMetrics()

    def svg(self, model=None):
        return render_svg(layout(model or initial("nested"), self.metrics))

    def rules(self, svg):
        return {f["rule"] for f in check_svg(svg, self.metrics)["findings"]}

    def test_six_measured_examples_and_eight_template_smokes(self):
        for path in sorted((ROOT / "fixtures").glob("*.json")):
            with self.subTest(example=path.stem):
                svg = self.svg(load(path))
                report = check_svg(svg, self.metrics)
                self.assertEqual(report["errors"], 0, report["findings"])
                self.assertEqual(svg, self.svg(load(path)))
        for template in ("nested", "layered", "sequence", "lanes", "grid_table", "er", "statechart", "tree"):
            with self.subTest(template=template):
                self.assertEqual(check_svg(self.svg(initial(template)), self.metrics)["errors"], 0)

    def test_mixed_cjk_labels_are_measured_without_overflow(self):
        model = initial("nested")
        model["nodes"][0]["label"] = "顾客通过 Web 客户端提交订单，系统校验库存。"
        model["nodes"][1]["label"] = "订单处理 Checkout service"
        model["edges"][0]["label"] = "提交订单 API"
        scene = layout(model, self.metrics)
        report = check_svg(render_svg(scene), self.metrics)
        self.assertEqual(report["errors"], 0, report["findings"])
        name = next(t for t in scene.texts if t.id == "client-name")
        self.assertTrue(name.runs)
        self.assertEqual("".join(run["text"] for line in name.runs for run in line),
                         "".join(name.lines))
        if self.metrics.measured_with == "pillow":
            self.assertTrue(all(run["family"] != "sans-serif" for line in name.runs for run in line))
        if self.metrics.doctor().get("measured_with") == "estimate":
            self.assertTrue(self.metrics.warnings)

    def test_actual_text_mutation_is_detected_without_trusting_metadata(self):
        root = ET.fromstring(self.svg())
        name = next(e for e in root.iter() if e.get("data-role") == "name")
        list(name)[0].text = "A" * 100
        self.assertIn("text-overflow", self.rules(ET.tostring(root, encoding="unicode")))

    def test_background_alignment_for_all_text_anchors(self):
        for anchor in ("start", "middle", "end"):
            scene = layout(initial("nested"), self.metrics)
            label = next(t for t in scene.texts if t.role == "edge-label")
            label.anchor = anchor
            bg = next(b for b in scene.boxes if b.role == "label-bg")
            bg.x = label.left - 5
            self.assertNotIn("label-background", self.rules(render_svg(scene)))
            bg.x += 12
            self.assertIn("label-background", self.rules(render_svg(scene)))

    def test_overlap_and_arrow_obstacle_mutations_are_detected(self):
        scene = layout(initial("nested"), self.metrics)
        scene.boxes[1].x = scene.boxes[0].x + 10
        self.assertIn("shape-overlap", self.rules(render_svg(scene)))
        scene = layout(initial("nested"), self.metrics)
        a, b = scene.edges[0].points[0], scene.edges[0].points[-1]
        scene.boxes.append(Box("blocker", (a[0] + b[0]) / 2 - 10, a[1] - 10, 20, 20))
        self.assertIn("arrow-through-box", self.rules(render_svg(scene)))
        scene.texts.append(copy.deepcopy(scene.texts[1]))
        scene.texts[-1].id = "colliding-text"
        self.assertIn("text-overlap", self.rules(render_svg(scene)))

    def test_endpoint_and_boundary_membership_checks(self):
        scene = layout(initial("nested"), self.metrics)
        scene.edges[0].points[-1] = (scene.edges[0].points[-1][0] - 12, scene.edges[0].points[-1][1])
        self.assertIn("edge-port", self.rules(render_svg(scene)))
        scene = layout(load(ROOT / "fixtures/trust.json"), self.metrics)
        node = next(b for b in scene.boxes if b.id == "browser")
        node.x += 2000
        self.assertIn("boundary-membership", self.rules(render_svg(scene)))

    def test_colour_and_marker_variants_are_safe_when_inlined(self):
        first = self.svg()
        model = initial("nested")
        model["edges"][0].update(style="shared", dir="<->")
        second = self.svg(model)
        a, b = ET.fromstring(first), ET.fromstring(second)
        ids_a, ids_b = [{e.get("id") for e in root.iter() if e.get("id")} for root in (a, b)]
        self.assertFalse(ids_a & ids_b)
        edge = next(e for e in b.iter() if e.get("data-role") == "edge")
        marker_id = edge.get("marker-end")[5:-1]
        marker = next(e for e in b.iter() if e.get("id") == marker_id)
        self.assertEqual(list(marker)[0].get("fill"), edge.get("stroke"))
        self.assertEqual(edge.get("marker-start"), edge.get("marker-end"))
        edge.set("marker-end", "url(#missing)")
        self.assertIn("marker-reference", self.rules(ET.tostring(b, encoding="unicode")))

    def test_contrast_and_svg_active_content_are_rejected(self):
        root = ET.fromstring(self.svg())
        name = next(e for e in root.iter() if e.get("data-role") == "name")
        name.set("fill", "#ffffff")
        self.assertIn("text-contrast", self.rules(ET.tostring(root, encoding="unicode")))
        ET.SubElement(root, "script").text = "alert(1)"
        self.assertIn("unsafe-svg", self.rules(ET.tostring(root, encoding="unicode")))
        model = initial("nested")
        model["nodes"][0]["label"] = '<script>& "quoted"'
        self.assertNotIn("unsafe-svg", self.rules(self.svg(model)))

    def test_theme_contrast_passes_and_dark_canvas_is_explicit(self):
        for theme in ("neutral", "print", "dark"):
            model = load(ROOT / "fixtures/context.json")
            model["meta"]["theme"] = theme
            report = check_svg(self.svg(model), self.metrics)
            self.assertFalse([f for f in report["findings"] if "contrast" in f["rule"]])

    def test_golden_svg_is_deterministic_with_explicit_estimator(self):
        for path in sorted((ROOT / "fixtures").glob("*.json")):
            model = load(path)
            svg = render_svg(layout(model, FontMetrics(paths=[])))
            self.assertEqual(svg, (ROOT / "golden" / (path.stem + ".svg")).read_text())

    def test_state_symbols_and_tree_cycle_contract(self):
        model = initial("statechart")
        model["nodes"] = [{"id": "start", "kind": "initial", "label": "Start"},
                          {"id": "open", "kind": "state", "label": "Open"},
                          {"id": "done", "kind": "final", "label": "Done"}]
        model["edges"] = [{"from": "start", "to": "open", "label": "create"},
                          {"from": "open", "to": "done", "label": "complete"}]
        report = check_svg(self.svg(model), self.metrics)
        self.assertEqual(report["errors"], 0, report["findings"])
        tree = initial("tree")
        tree["edges"].append({"from": "service", "to": "client"})
        with self.assertRaisesRegex(ValueError, "acyclic"):
            layout(tree, self.metrics)

    def test_sequence_lifelines_stay_behind_activations(self):
        root = ET.fromstring(self.svg(load(ROOT / "fixtures/sequence.json")))
        positions = {e.get("data-id"): i for i, e in enumerate(root) if e.get("data-id")}
        self.assertLess(positions["checkout-lifeline"], positions["__activation-1"])
        self.assertLess(positions["__activation-1"], positions["edge-1"])

    def test_model_ids_cannot_collide_with_internal_svg_ids(self):
        model = initial("nested")
        model["nodes"] = [{"id": name, "kind": "component", "label": name}
                          for name in ("title", "peer-arrow", "edge-1-background", "figure-title")]
        model["edges"] = [{"from": "title", "to": "peer-arrow", "label": "request"}]
        report = check_svg(self.svg(model), self.metrics)
        self.assertFalse([f for f in report["findings"] if f["rule"] in ("unique-ids", "label-background")])
