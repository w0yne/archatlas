import copy
import unittest

from archatlas.check import check_svg
from archatlas.cli import initial
from archatlas.fonts import FontMetrics
from archatlas.layout import layout
from archatlas.model import validate
from archatlas.render import render_svg
from archatlas.render.legend import entries


class LayoutRefinements(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metrics = FontMetrics()

    def scene(self, model):
        return layout(model, self.metrics)

    def assert_clean(self, model):
        scene = self.scene(model)
        report = check_svg(render_svg(scene), self.metrics)
        self.assertEqual((report["errors"], report["warnings"]), (0, 0), report["findings"])
        return scene

    def test_vertical_cardinalities_stay_outside_both_nodes(self):
        model = initial("er")
        model["layout"]["direction"] = "TB"
        model["edges"][0].update(label="owns", cardinality={"from": "1", "to": "0..*"},
                                 from_port="s", to_port="n")
        scene = self.assert_clean(model)
        nodes = {b.id: b for b in scene.boxes}
        labels = {t.id: t for t in scene.texts}
        self.assertGreater(labels["edge-1-from"].y, nodes["client"].y + nodes["client"].h)
        self.assertLess(labels["edge-1-to"].y + labels["edge-1-to"].h, nodes["service"].y)
        model["edges"][0].update({"from": "service", "to": "client", "from_port": "n", "to_port": "s"})
        self.assert_clean(model)

    def test_lane_time_axis_uses_dependencies_not_input_order(self):
        model = initial("lanes")
        model["layout"]["direction"] = "LR"
        model["nodes"].append({"id": "finish", "kind": "task", "label": "Finish", "parent": "first"})
        model["nodes"] = [model["nodes"][2], model["nodes"][0], model["nodes"][1]]
        model["edges"].append({"from": "service", "to": "finish"})
        boxes = {b.id: b for b in self.assert_clean(model).boxes}
        self.assertLess(boxes["client"].x, boxes["service"].x)
        self.assertLess(boxes["service"].x, boxes["finish"].x)
        self.assertEqual(boxes["client"].y, boxes["finish"].y)

    def test_parallel_lanes_align_equal_ranks(self):
        model = initial("lanes")
        model["layout"]["direction"] = "LR"
        model["nodes"] = [{"id": "a", "kind": "task", "label": "A", "parent": "first"},
                          {"id": "b", "kind": "task", "label": "B", "parent": "second"},
                          {"id": "c", "kind": "task", "label": "C", "parent": "first"},
                          {"id": "d", "kind": "task", "label": "D", "parent": "second"}]
        model["edges"] = [{"from": "a", "to": "c"}, {"from": "b", "to": "d"}]
        boxes = {b.id: b for b in self.assert_clean(model).boxes}
        self.assertEqual(boxes["a"].x, boxes["b"].x)
        self.assertEqual(boxes["c"].x, boxes["d"].x)
        model["groups"][0]["parent"] = "pool"
        model["groups"].append({"id": "pool", "kind": "pool", "title": "Order process"})
        for direction, axis in (("LR", "x"), ("TB", "y")):
            model["layout"]["direction"] = direction
            boxes = {b.id: b for b in self.assert_clean(model).boxes}
            self.assertEqual(getattr(boxes["a"], axis), getattr(boxes["b"], axis))
            self.assertEqual(getattr(boxes["c"], axis), getattr(boxes["d"], axis))

    def test_statechart_cycles_keep_all_edges_and_are_deterministic(self):
        model = initial("statechart")
        model["nodes"].append({"id": "done", "kind": "state", "label": "Done"})
        model["edges"] += [{"from": "service", "to": "done"}, {"from": "done", "to": "client"}]
        scene = self.scene(model)
        self.assertEqual(len([e for e in scene.edges if e.kind != "legend"]), 3)
        self.assertEqual(render_svg(scene), render_svg(self.scene(model)))
        boxes = [b for b in scene.boxes if b.role == "node"]
        self.assertEqual(len({b.x for b in boxes}), 3)

    def test_symbol_defaults_and_spacing_tokens(self):
        model = initial("nested")
        model["nodes"][0].update(kind="event", label="Start")
        model["nodes"][1].update(kind="gateway", label="OK?")
        scene = self.assert_clean(model)
        self.assertTrue(all(b.w < 140 for b in scene.boxes if b.role == "node"))
        model = initial("nested")
        before = self.scene(model)
        model["layout"]["spacing"] = {"node_gap": 160, "document_width": 1400, "wide_view_ratio": 1.25}
        after = self.scene(model)
        self.assertGreater(after.boxes[1].x - after.boxes[0].x, before.boxes[1].x - before.boxes[0].x)
        self.assertEqual(after.width, 1400)

    def test_mixed_table_and_graph_preserve_every_cell_and_edge(self):
        model = initial("grid_table")
        graph = initial("nested")
        model.update(nodes=graph["nodes"], edges=graph["edges"])
        model["tables"][0]["columns"][0] = ""
        scene = self.assert_clean(model)
        cells = [b for b in scene.boxes if b.role == "cell"]
        nodes = [b for b in scene.boxes if b.role == "node"]
        self.assertEqual(len(cells), 9)
        self.assertEqual(len(nodes), 2)
        self.assertLess(max(b.x + b.w for b in cells), min(b.x for b in nodes))
        self.assertEqual(len([e for e in scene.edges if e.kind != "legend"]), 1)

    def test_legend_reuses_author_entries_and_visual_variants(self):
        model = initial("nested")
        model["nodes"][1].pop("style")
        self.assertEqual({entry["symbol"] for entry in entries(self.scene(model), model)}, {"line", "box"})
        model["edges"][0]["dashed"] = True
        model["meta"]["legend"] = [{"label": "Proposed call", "dashed": True},
                                  {"label": "Proposed call", "dashed": True}]
        self.assertEqual(sum(entry["label"] == "Proposed call" for entry in entries(self.scene(model), model)), 1)
        model = initial("nested")
        model["nodes"][1].pop("style")
        model["edges"].append({"from": "service", "to": "client", "kind": "async"})
        legend = entries(self.scene(model), model)
        self.assertEqual({e["kind"] for e in legend if e["symbol"] == "line"}, {"call", "async"})
        model["meta"]["theme"] = "print"
        model["nodes"][1]["style"] = "primary"
        self.assertTrue(any(e.get("symbol") == "box" for e in entries(self.scene(model), model)))

    def test_new_semantic_kinds_and_rank_are_additive(self):
        model = initial("tree")
        for kind in ("process", "dataset", "job", "pipeline"):
            model["nodes"][0]["kind"] = kind
            model["nodes"][1]["rank"] = 2
            validate(model)
            self.assert_clean(copy.deepcopy(model))
