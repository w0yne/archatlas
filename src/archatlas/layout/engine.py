"""Small family-specific layouts sharing measurement and resolved geometry."""
import math

from .base import Box, Connector, Scene, Text
from .route import route
from ..fonts.measure import FontMetrics
from ..model.validate import ModelError, validate

GUTTER = 112
PAD = 24
HEADER = 52


def intersects(a, b, pad=0):
    x, y, w, h = a
    u, v, r, s = b
    return x < u + r + pad and u < x + w + pad and y < v + s + pad and v < y + h + pad


def text_box(metrics, id, value, x, y, width, size=16, owner="", role="label", anchor="start", style="peer"):
    lines = metrics.wrap(value, width, size) or [""]
    measured = max(metrics.width(line, size) for line in lines)
    return Text(id, lines, x, y, measured, len(lines) * size * 1.4, size, owner, role, anchor, style)


class Layout:
    def __init__(self, model, metrics):
        self.model, self.metrics = model, metrics
        # Resolve all glyph fallbacks before selecting padding and SVG font stack.
        def prime(value):
            if isinstance(value, str):
                metrics.width(value, 16)
            elif isinstance(value, list):
                for child in value:
                    prime(child)
            elif isinstance(value, dict):
                for child in value.values():
                    prime(child)
        prime(model)
        self.template = model["layout"]["template"]
        self.nodes = {n["id"]: n for n in model.get("nodes", [])}
        self.groups = {g["id"]: g for g in model.get("groups", [])}
        self.items = {**self.nodes, **self.groups}
        self.children = {}
        for item in list(self.groups.values()) + list(self.nodes.values()):
            self.children.setdefault(item.get("parent"), []).append(item["id"])
        self.dimensions = {}
        self.offsets = {}
        self.node_text = {}
        meta = model["meta"]
        self.scene = Scene(meta["title"], meta.get("description") or meta["title"], 1120, 810,
                           meta.get("theme", "neutral"), family=metrics.family,
                           measured_with=metrics.measured_with, allow=model.get("allow", []), lang=meta.get("lang", "en"))
        title = text_box(metrics, "figure-title", meta["title"], 32, 24, 1040, 28, role="title")
        self.scene.texts.append(title)
        self.top = title.y + title.h + 36

    def measure_node(self, node):
        metrics = self.metrics
        width = node.get("size_hint", {}).get("width", 230 if node.get("style") == "primary" else 200)
        padding = 16 * metrics.padding_factor
        lines = []
        for role, value, size in [("name", node["label"], 16), ("sub", node.get("sub", ""), 12)]:
            if value:
                lines.append((role, metrics.wrap(value, width - 2 * padding, size), size))
        for index, attribute in enumerate(node.get("attributes", [])):
            lines.append((f"attribute-{index}", metrics.wrap(attribute, width - 2 * padding, 12), 12))
        if node.get("tags"):
            lines.append(("tags", metrics.wrap(" · ".join(node["tags"]), width - 2 * padding, 11), 11))
        height = max(76, sum(len(x[1]) * x[2] * 1.4 + 6 for x in lines) + padding * 2)
        height = max(height, node.get("size_hint", {}).get("height", 0))
        if node["kind"] in ("initial", "final"):
            width = height = 32
        elif node["kind"] in ("gateway", "event"):
            # Leave a generous interior for text in non-rectangular symbols.
            width = height = max(width, height) * 1.35
        self.node_text[node["id"]] = lines
        return width, height

    def arrange(self, ids, vertical=False, columns=None):
        if not ids:
            return {}, (160, 64)
        cols = 1 if vertical else min(columns or self.model["layout"].get("columns", 3), len(ids))
        rows = math.ceil(len(ids) / cols)
        col_widths = [max(self.dimensions[id][0] for i, id in enumerate(ids) if i % cols == col)
                      for col in range(cols)]
        row_heights = [max(self.dimensions[id][1] for id in ids[row * cols:(row + 1) * cols])
                       for row in range(rows)]
        offsets = {}
        for i, id in enumerate(ids):
            col, row = i % cols, i // cols
            offsets[id] = (sum(col_widths[:col]) + col * GUTTER, sum(row_heights[:row]) + row * GUTTER)
        return offsets, (sum(col_widths) + (cols - 1) * GUTTER, sum(row_heights) + (rows - 1) * GUTTER)

    def measure_group(self, id):
        ids = self.children.get(id, [])
        for child in ids:
            if child in self.groups:
                self.measure_group(child)
        group = self.groups[id]
        vertical = self.template == "lanes" and group["kind"] == "lane" and self.model["layout"].get("direction", "TB") == "TB"
        offsets, (w, h) = self.arrange(ids, vertical=vertical)
        title_width = self.metrics.width(group["title"], 16)
        w = max(w, min(title_width, 700))
        title = self.metrics.wrap(group["title"], w, 16)
        header = max(HEADER, len(title) * 22.4 + 24)
        self.dimensions[id] = (w + 2 * PAD, h + header + PAD)
        self.offsets[id] = {child: (x + PAD, y + header) for child, (x, y) in offsets.items()}

    def place(self, id, x, y):
        item = self.items[id]
        w, h = self.dimensions[id]
        style = item.get("style", "peer")
        if id in self.groups:
            box = Box(id, x, y, w, h, "group", item["kind"], style, item.get("parent", ""),
                      item.get("dashed", item["kind"] == "boundary"))
            self.scene.boxes.append(box)
            self.scene.texts.append(text_box(self.metrics, id + "-title", item["title"],
                                            x + PAD, y + 12, w - 2 * PAD, 16, id, "group-title"))
            for child, (dx, dy) in self.offsets[id].items():
                self.place(child, x + dx, y + dy)
        else:
            box = Box(id, x, y, w, h, kind=item["kind"], style=style, parent=item.get("parent", ""),
                      dashed=item.get("evidence", {}).get("status") not in (None, "verified"))
            self.scene.boxes.append(box)
            texts = self.node_text[id]
            total = sum(len(lines) * size * 1.4 + 6 for _, lines, size in texts) - 6
            small_state = item["kind"] in ("initial", "final")
            ty = y + h + 10 if small_state else y + (h - total) / 2
            for role, lines, size in texts:
                tw = max(self.metrics.width(line, size) for line in lines)
                self.scene.texts.append(Text(id + "-" + role, lines, max(tw / 2 + 8, x + w / 2), ty, tw,
                                             len(lines) * size * 1.4, size, "" if small_state else id,
                                             "state-label" if small_state else role, "middle", style))
                ty += len(lines) * size * 1.4 + 6

    def graph(self):
        for id, node in self.nodes.items():
            self.dimensions[id] = self.measure_node(node)
        # Peer nodes in a view have consistent dimensions within each style.
        for style in {n.get("style", "peer") for n in self.nodes.values()}:
            ids = [id for id, n in self.nodes.items() if n.get("style", "peer") == style
                   and n["kind"] not in ("gateway", "event", "initial", "final")]
            if ids:
                size = tuple(max(self.dimensions[id][i] for id in ids) for i in (0, 1))
                self.dimensions.update({id: size for id in ids})
        for id, group in self.groups.items():
            if not group.get("parent"):
                self.measure_group(id)
        roots = self.children.get(None, [])
        if self.template == "tree" and not self.groups:
            offsets = self.tree_positions(roots)
        else:
            vertical = self.template == "layered" or \
                (self.template == "lanes" and self.model["layout"].get("direction") == "LR") or \
                (self.template not in ("lanes", "layered") and self.model["layout"].get("direction") == "TB")
            offsets, _ = self.arrange(roots, vertical=vertical,
                                     columns=len(roots) if self.template == "lanes" else None)
        for id, (x, y) in offsets.items():
            self.place(id, 40 + x, self.top + y)
        self.connect()

    def tree_positions(self, ids):
        parents = {id: set() for id in ids}
        for edge in self.model.get("edges", []):
            parents[edge["to"]].add(edge["from"])
        rank, remaining = {}, set(ids)
        while remaining:
            ready = [id for id in ids if id in remaining and not (parents[id] & remaining)]
            if not ready:
                raise ModelError("tree requires an acyclic graph; use statechart for cycles")
            for id in ready:
                rank[id] = max((rank[p] + 1 for p in parents[id]), default=0)
                remaining.remove(id)
        max_w = max((s[0] for s in self.dimensions.values()), default=200)
        max_h = max((s[1] for s in self.dimensions.values()), default=80)
        count, result = {}, {}
        for id in ids:
            r = rank[id]
            offset = count.get(r, 0)
            result[id] = (r * (max_w + GUTTER), offset * (max_h + GUTTER))
            count[r] = offset + 1
        if self.model["layout"].get("direction") == "TB":
            result = {id: (count_at * (max_w + GUTTER), rank[id] * (max_h + GUTTER))
                      for id, count_at in ((id, result[id][1] / (max_h + GUTTER)) for id in ids)}
        return result

    def ancestors(self, id):
        result = {id}
        while self.items.get(id, {}).get("parent"):
            id = self.items[id]["parent"]
            result.add(id)
        return result

    def connect(self):
        boxes = {b.id: b for b in self.scene.boxes}
        previous = []
        edges = self.model.get("edges", [])
        for i, edge in enumerate(edges):
            id = edge.get("id", f"edge-{i + 1}")
            source, target = boxes[edge["from"]], boxes[edge["to"]]
            excluded = self.ancestors(source.id) | self.ancestors(target.id)
            obstacles = [b.rect for b in self.scene.boxes if b.id not in excluded and b.role != "label-bg"]
            obstacles += [t.rect for t in self.scene.texts if t.role in ("group-title", "edge-label")
                          and t.owner not in (source.id, target.id)]
            same = [e for e in edges if (e["from"], e["to"]) == (edge["from"], edge["to"])]
            slot = sum(1 for e in edges[:i] if (e["from"], e["to"]) == (edge["from"], edge["to"]))
            points = route(source.rect, target.rect, obstacles, from_port=edge.get("from_port", "auto"),
                           to_port=edge.get("to_port", "auto"), slot=slot, slots=len(same),
                           previous=previous, waypoints=edge.get("waypoints", ()))
            previous.append(points)
            self.add_edge(id, edge, points)
            value = edge.get("label", "")
            if "step" in edge:
                value = f"{edge['step']}. {value}".strip()
            if value:
                self.edge_label(id, value, points)
            if edge.get("cardinality"):
                for end, point, neighbour in (("from", points[0], points[1]), ("to", points[-1], points[-2])):
                    value = edge["cardinality"].get(end)
                    if value:
                        dx, dy = neighbour[0] - point[0], neighbour[1] - point[1]
                        length = abs(dx) + abs(dy) or 1
                        tx, ty = point[0] + 26 * dx / length, point[1] + 26 * dy / length + 12
                        if dx == 0:
                            tx += 24
                        self.scene.texts.append(text_box(self.metrics, id + "-" + end, value,
                                                        tx, ty, 70, 12, role="cardinality", anchor="middle"))

    def add_edge(self, id, edge, points):
        status = edge.get("evidence", {}).get("status", "verified")
        dashed = edge.get("dashed", status != "verified" or edge.get("kind") == "message")
        self.scene.edges.append(Connector(id, points, edge["from"], edge["to"], edge.get("style", "peer"),
                                           edge.get("dir", "--" if self.template == "er" else "->"),
                                           dashed, edge.get("kind", "call")))

    def edge_label(self, id, value, points):
        segments = sorted(zip(points, points[1:]), key=lambda ab: -(abs(ab[0][0] - ab[1][0]) + abs(ab[0][1] - ab[1][1])))
        longest = segments[0]
        label_width = min(200, max(48, abs(longest[0][0] - longest[1][0]) - 24)) \
            if longest[0][1] == longest[1][1] else 200
        text = text_box(self.metrics, id + "-label", value, 0, 0, label_width, 12, id, "edge-label", "middle")
        candidates = []
        for a, b in segments:
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            if a[1] == b[1]:
                candidates.extend([(mx, my - text.h - 10), (mx, my + 10)])
            else:
                candidates.extend([(mx + text.w / 2 + 12, my - text.h / 2),
                                   (mx - text.w / 2 - 12, my - text.h / 2)])
        occupied = [b.rect for b in self.scene.boxes if b.role != "group"]
        occupied += [t.rect for t in self.scene.texts if t.role in ("group-title", "edge-label")]
        chosen = None
        for x, y in candidates:
            rect = (x - text.w / 2 - 5, y - 4, text.w + 10, text.h + 8)
            if x - text.w / 2 > 0 and y > self.top - 10 and not any(intersects(rect, b, 3) for b in occupied):
                chosen = x, y
                break
        if chosen is None:
            chosen = candidates[0]
            self.scene.warnings.append({"rule": "label-placement", "message": "No clear label slot; revise topology or waypoints",
                                        "elements": [id]})
        text.x, text.y = chosen
        self.scene.texts.append(text)
        # Background and text use precisely the same measured box/anchor.
        self.scene.boxes.append(Box("__" + id + "-background", text.left - 5, text.y - 4,
                                    text.w + 10, text.h + 8, "label-bg", parent=id))

    def sequence(self):
        nodes = list(self.nodes.values())
        if not nodes:
            raise ModelError("Sequence requires participants")
        for node in nodes:
            self.dimensions[node["id"]] = self.measure_node(node)
        width = max(w for w, _ in self.dimensions.values())
        height = max(h for _, h in self.dimensions.values())
        centers = {}
        for i, node in enumerate(nodes):
            id = node["id"]
            self.dimensions[id] = (width, height)
            self.place(id, 40 + i * (width + GUTTER), self.top)
            centers[id] = 40 + i * (width + GUTTER) + width / 2
        edges = sorted(enumerate(self.model.get("edges", [])), key=lambda pair: pair[1].get("step", pair[0] + 1))
        ys, y = {}, self.top + height + 100
        for i, edge in edges:
            step = edge.get("step", i + 1)
            ys[step] = y
            y += max(96, len(self.metrics.wrap(edge.get("label", ""), width + GUTTER - 40, 12)) * 16.8 + 55)
        bottom = y + 24
        for node in nodes:
            x = centers[node["id"]]
            self.scene.edges.append(Connector(node["id"] + "-lifeline",
                                               [(x, self.top + height), (x, bottom)],
                                               node["id"], node["id"], direction="--", dashed=True, kind="lifeline"))
        for frame in self.model.get("frames", []):
            top, end = ys[frame["from_step"]] - 64, ys[frame["to_step"]] + 38
            box = Box(frame["id"], 24, top, max(centers.values()) + width / 2, end - top, "group", "frame")
            self.scene.boxes.insert(0, box)
            self.scene.texts.append(text_box(self.metrics, box.id + "-title", frame["label"],
                                            box.x + 12, top + 8, box.w - 24, 12, box.id, "group-title"))
        for index, activation in enumerate(self.model.get("activations", [])):
            top, end = ys[activation["from_step"]] - 6, ys[activation["to_step"]] + 6
            self.scene.boxes.append(Box(f"__activation-{index + 1}", centers[activation["node"]] - 5,
                                       top, 10, end - top, "activation", parent=activation["node"]))
        for i, edge in edges:
            id = edge.get("id", f"edge-{i + 1}")
            y = ys[edge.get("step", i + 1)]
            a, b = centers[edge["from"]], centers[edge["to"]]
            if a != b:
                sign = 1 if b > a else -1
                for activation in self.model.get("activations", []):
                    if activation["from_step"] <= edge.get("step", i + 1) <= activation["to_step"]:
                        if activation["node"] == edge["from"]:
                            a += 5 * sign
                        if activation["node"] == edge["to"]:
                            b -= 5 * sign
            points = [(a, y), (b, y)] if a != b else [(a, y), (a + width / 2 + 28, y),
                                                                    (a + width / 2 + 28, y + 32), (a, y + 32)]
            self.add_edge(id, edge, points)
            label = f"{edge.get('step', i + 1)}. {edge.get('label', '')}".strip()
            self.edge_label(id, label, points)

    def table(self):
        y = self.top
        for table in self.model.get("tables", []):
            if table.get("title"):
                title = text_box(self.metrics, table["id"] + "-title", table["title"], 40, y, 1040, 16, role="table-title")
                self.scene.texts.append(title)
                y += title.h + 16
            count = len(table["columns"])
            cell_w = max(110, min(250, 1040 / count))
            for r, row in enumerate([table["columns"], *table["rows"]]):
                wrapped = [self.metrics.wrap(value, cell_w - 24, 13) for value in row]
                h = max(48, max(len(lines) for lines in wrapped) * 18.2 + 24)
                for c, lines in enumerate(wrapped):
                    id = f"__{table['id']}-r{r}-c{c}"
                    x = 40 + c * cell_w
                    style = "primary" if r == 0 else "peer"
                    self.scene.boxes.append(Box(id, x, y, cell_w, h, "cell", style=style))
                    w = max(self.metrics.width(line, 13) for line in lines)
                    self.scene.texts.append(Text(id + "-text", lines, x + 12, y + 12, w, len(lines) * 18.2,
                                                13, id, "cell-text", style=style))
                y += h
            y += 48

    def finish(self):
        scene = self.scene
        bottom = max([self.top] + [b.y + b.h for b in scene.boxes] + [t.y + t.h for t in scene.texts]
                     + [p[1] for e in scene.edges for p in e.points])
        right = max([1080] + [b.x + b.w for b in scene.boxes] + [t.left + t.w for t in scene.texts]
                    + [p[0] for e in scene.edges for p in e.points])
        legend = list(self.model["meta"].get("legend", []))
        zh = self.model["meta"].get("lang", "").startswith("zh")
        words = {
            "call": "调用", "data": "数据", "async": "异步", "message": "消息",
            "dependency": "依赖", "assoc": "关联", "dashed": "虚线",
            "primary": "重点", "external": "外部", "shared": "共享", "planned": "规划",
            "boundary": "边界", "inferred": "推断", "doc-only": "仅文档", "conflict": "冲突",
        }
        local = lambda word: words.get(word, word) if zh else word
        seen = set()
        for edge in scene.edges:
            if edge.kind == "lifeline":
                continue
            key = (edge.kind, edge.dashed, edge.style)
            if key not in seen:
                text = local(edge.kind) + (" · " + local("dashed") if edge.dashed else "")
                if edge.style != "peer":
                    text = local(edge.style) + " · " + text
                legend.append({"label": text, "style": edge.style, "dashed": edge.dashed})
                seen.add(key)
        for style in sorted({node.get("style", "peer") for node in self.nodes.values()} - {"peer"}):
            legend.append({"label": local(style), "style": style})
        if any(box.role == "group" and box.dashed for box in scene.boxes):
            legend.append({"label": local("boundary"), "dashed": True})
        statuses = sorted({n.get("evidence", {}).get("status") for n in self.nodes.values()
                           if n.get("evidence", {}).get("status") not in (None, "verified")})
        for status in statuses:
            legend.append({"label": local(status), "style": "planned", "dashed": True})
        x, y = 40, bottom + 40
        for i, entry in enumerate(legend):
            label = text_box(self.metrics, f"legend-{i}", entry["label"], x + 40, y, 260, 11, role="legend")
            if x + label.w + 50 > right and x != 40:
                x, y = 40, y + 48
                label.x, label.y = x + 40, y
            scene.edges.append(Connector(f"legend-line-{i}", [(x, y + 10), (x + 28, y + 10)], "", "",
                                         entry.get("style", "peer"), "--", entry.get("dashed", False), "legend"))
            scene.texts.append(label)
            x += label.w + 76
        profile = self.model["layout"].get("profile", "doc")
        scene.width = 1440 if profile in ("slide", "slide-16x9") else max(1120, right + 40)
        scene.height = 810 if profile in ("slide", "slide-16x9") else max(300, y + 68)
        if profile in ("doc", "doc-1120xN") and scene.width > 1120:
            scene.warnings.append({"rule": "wide-view", "message": "Content exceeds document width; split the view for narrow pages"})
        scene.warnings.extend(self.metrics.warnings)
        scene.family, scene.measured_with = self.metrics.family, self.metrics.measured_with
        for text in scene.texts:
            text.runs = [self.metrics.runs(line) for line in text.lines]
        for node in self.nodes.values():
            if node.get("evidence", {}).get("status") not in (None, "verified"):
                scene.warnings.append({"rule": "evidence", "message": node["evidence"]["status"], "elements": [node["id"]]})
        return scene


def layout(model, metrics=None):
    validate(model)
    engine = Layout(model, metrics or FontMetrics())
    if engine.template == "sequence":
        engine.sequence()
    elif engine.template == "grid_table":
        engine.table()
    else:
        engine.graph()
    return engine.finish()
