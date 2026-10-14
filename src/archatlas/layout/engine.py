"""Small family-specific layouts sharing measurement and resolved geometry."""
import math
from statistics import median

from .base import Box, Connector, Scene, Text
from .route import route, segment_hits_rect
from .rank import rank_graph
from ..fonts.measure import FontMetrics
from ..model.validate import ModelError, validate
from ..render.theme import THEMES
from ..render.legend import entries as legend_entries


def intersects(a, b, pad=0):
    x, y, w, h = a
    u, v, r, s = b
    return x < u + r + pad and u < x + w + pad and y < v + s + pad and v < y + h + pad


def text_box(metrics, id, value, x, y, width, size=16, owner="", role="label", anchor="start", style="peer"):
    width = max(width, metrics.required_width(value, size))
    lines = metrics.wrap(value, width, size) or [""]
    measured = max(metrics.width(line, size) for line in lines)
    return Text(id, lines, x, y, measured, len(lines) * size * 1.4, size, owner, role, anchor, style, source=value)


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
        self.spacing = {**THEMES[model["meta"].get("theme", "neutral")]["spacing"],
                        **model["layout"].get("spacing", {})}
        widths = [n.get("size_hint", {}).get("width", 200) for n in model.get("nodes", [])]
        self.gap = max(self.spacing["node_gap"], median(widths or [200]) * self.spacing["gap_ratio"])
        labels = [metrics.width(e["label"], 12) for e in model.get("edges", []) if e.get("label")]
        if labels:
            self.gap = max(self.gap, min(max(labels), self.spacing["label_width"]) +
                           2 * self.spacing["label_clearance"])
            self.gap = max(self.gap, max(metrics.required_width(e["label"], 12)
                                        for e in model.get("edges", []) if e.get("label")) +
                           2 * self.spacing["label_clearance"])
        self.rank_gap = max(self.gap, self.spacing["rank_gap"])
        self.pad, self.header = self.spacing["group_padding"], self.spacing["group_header"]
        self.document_width = self.spacing["document_width"]
        self.nodes = {n["id"]: n for n in model.get("nodes", [])}
        self.groups = {g["id"]: g for g in model.get("groups", [])}
        self.items = {**self.nodes, **self.groups}
        crossings = {}
        for edge in model.get("edges", []):
            if edge.get("label"):
                a, b = (self.items[id].get("parent") for id in (edge["from"], edge["to"]))
                if a != b:
                    pair = tuple(sorted((a or "", b or "")))
                    crossings[pair] = crossings.get(pair, 0) + 1
        if max(crossings.values(), default=0) >= 3:
            self.gap = max(self.gap, self.spacing["boundary_gap"])
            self.rank_gap = max(self.rank_gap, self.gap)
        self.children = {}
        for item in list(self.groups.values()) + list(self.nodes.values()):
            self.children.setdefault(item.get("parent"), []).append(item["id"])
        self.dimensions = {}
        self.offsets = {}
        self.node_text = {}
        self.node_sources = {}
        meta = model["meta"]
        self.scene = Scene(meta["title"], meta.get("description") or meta["title"], 1120, 810,
                           meta.get("theme", "neutral"), family=metrics.family,
                           measured_with=metrics.measured_with, allow=model.get("allow", []), lang=meta.get("lang", "en"))
        title = text_box(metrics, "figure-title", meta["title"], 32, 24, self.document_width - 80, 28, role="title")
        self.scene.texts.append(title)
        self.top = title.y + title.h + 36

    def measure_node(self, node):
        metrics = self.metrics
        width = node.get("size_hint", {}).get("width", 230 if node.get("style") == "primary" else 200)
        padding = 16 * metrics.padding_factor
        symbol = node["kind"] in ("event", "gateway")
        if symbol:
            width = node.get("size_hint", {}).get("width", 80 if node["kind"] == "gateway" else 64)
            if "width" not in node.get("size_hint", {}):
                # Keep short words whole in compact event/gateway symbols.
                word_width = max((metrics.width(word, 16) for word in node["label"].split()), default=0)
                width = max(width, min(140, word_width + 2 * padding))
        wrap_width = max(24, width - 2 * padding)
        fields = [(node["label"], 16), (node.get("sub", ""), 12)]
        fields += [(value, 12) for value in node.get("attributes", [])]
        fields += [(" · ".join(node.get("tags", [])), 11)]
        width = max(width, max((metrics.required_width(value, size) + 2 * padding
                               for value, size in fields if value), default=width))
        wrap_width = max(24, width - 2 * padding)
        lines = []
        for role, value, size in [("name", node["label"], 16), ("sub", node.get("sub", ""), 12)]:
            if value:
                lines.append((role, metrics.wrap(value, wrap_width, size), size))
        for index, attribute in enumerate(node.get("attributes", [])):
            lines.append((f"attribute-{index}", metrics.wrap(attribute, width - 2 * padding, 12), 12))
        if node.get("tags"):
            lines.append(("tags", metrics.wrap(" · ".join(node["tags"]), width - 2 * padding, 11), 11))
        height = max(76, sum(len(x[1]) * x[2] * 1.4 + 6 for x in lines) + padding * 2)
        height = max(height, node.get("size_hint", {}).get("height", 0))
        if node["kind"] in ("initial", "final"):
            width = height = 32
        elif symbol:
            text_w = max((metrics.width(line, size) for _, wrapped, size in lines for line in wrapped), default=0)
            text_h = sum(len(wrapped) * size * 1.4 + 6 for _, wrapped, size in lines) - 6
            required = text_w + text_h if node["kind"] == "gateway" else math.hypot(text_w, text_h)
            width = height = max(width, node.get("size_hint", {}).get("height", 0), required + padding)
        elif node["kind"] in ("actor", "use_case"):
            text_w = max((metrics.width(line, size) for _, wrapped, size in lines for line in wrapped), default=0)
            text_h = max(0, sum(len(wrapped) * size * 1.4 + 6 for _, wrapped, size in lines) - 6)
            if node["kind"] == "actor":
                width = max(width, 56 + 2 * padding, text_w + 2 * padding)
                height = max(height, 80 + 10 + text_h + padding)
            else:
                # An inscribed rectangle occupies 1/sqrt(2) of each ellipse axis.
                width = max(width, math.sqrt(2) * (text_w + 2 * padding))
                height = max(height, math.sqrt(2) * (text_h + 2 * padding))
        self.node_text[node["id"]] = lines
        self.node_sources[node["id"]] = {"name": node["label"], "sub": node.get("sub", ""),
            "tags": " · ".join(node.get("tags", [])),
            **{f"attribute-{i}": value for i, value in enumerate(node.get("attributes", []))}}
        return width, height

    def arrange(self, ids, vertical=False, columns=None):
        if not ids:
            return {}, (160, 64)
        cols = 1 if vertical else min(columns or self.model["layout"].get("columns", 3), len(ids))
        limit = 1440 if self.model["layout"].get("profile") in ("slide", "slide-16x9") \
            else self.document_width * self.spacing["wide_view_ratio"]
        while cols > 1:
            widths = [max(self.dimensions[id][0] for i, id in enumerate(ids) if i % cols == col)
                      for col in range(cols)]
            if sum(widths) + (cols - 1) * self.gap + 80 + 2 * self.pad <= limit:
                break
            cols -= 1
        rows = math.ceil(len(ids) / cols)
        col_widths = [max(self.dimensions[id][0] for i, id in enumerate(ids) if i % cols == col)
                      for col in range(cols)]
        row_heights = [max(self.dimensions[id][1] for id in ids[row * cols:(row + 1) * cols])
                       for row in range(rows)]
        offsets = {}
        for i, id in enumerate(ids):
            col, row = i % cols, i // cols
            offsets[id] = (sum(col_widths[:col]) + col * self.gap, sum(row_heights[:row]) + row * self.gap)
        return offsets, (sum(col_widths) + (cols - 1) * self.gap, sum(row_heights) + (rows - 1) * self.gap)

    def measure_group(self, id):
        ids = self.children.get(id, [])
        for child in ids:
            if child in self.groups:
                self.measure_group(child)
        group = self.groups[id]
        vertical = self.template == "lanes" and group["kind"] == "lane" and self.model["layout"].get("direction", "TB") == "TB"
        if self.template in ("statechart", "tree"):
            offsets = self.rank_positions(ids)
            w = max((x + self.dimensions[child][0] for child, (x, y) in offsets.items()), default=160)
            h = max((y + self.dimensions[child][1] for child, (x, y) in offsets.items()), default=64)
        else:
            offsets, (w, h) = self.arrange(ids, vertical=vertical)
        title_width = self.metrics.width(group["title"], 16)
        w = max(w, min(title_width, 700), self.metrics.required_width(group["title"], 16))
        title = self.metrics.wrap(group["title"], w, 16)
        header = max(self.header, len(title) * 22.4 + 24)
        self.dimensions[id] = (w + 2 * self.pad, h + header + self.pad)
        self.offsets[id] = {child: (x + self.pad, y + header) for child, (x, y) in offsets.items()}

    def place(self, id, x, y):
        item = self.items[id]
        w, h = self.dimensions[id]
        style = item.get("style", "peer")
        if id in self.groups:
            box = Box(id, x, y, w, h, "group", item["kind"], style, item.get("parent", ""),
                      item.get("dashed", item["kind"] == "boundary"))
            self.scene.boxes.append(box)
            self.scene.texts.append(text_box(self.metrics, id + "-title", item["title"],
                                            x + self.pad, y + 12, w - 2 * self.pad, 16, id, "group-title"))
            for child, (dx, dy) in self.offsets[id].items():
                self.place(child, x + dx, y + dy)
        else:
            box = Box(id, x, y, w, h, kind=item["kind"], style=style, parent=item.get("parent", ""),
                      dashed=item.get("evidence", {}).get("status") not in (None, "verified"),
                      event_type=item.get("event_type", ""))
            self.scene.boxes.append(box)
            texts = self.node_text[id]
            total = sum(len(lines) * size * 1.4 + 6 for _, lines, size in texts) - 6
            small_state = item["kind"] in ("initial", "final")
            ty = y + h + 10 if small_state else y + (h - total) / 2
            if item["kind"] == "actor":
                ty = box.glyph_rect[1] + box.glyph_rect[3] + 10
            for role, lines, size in texts:
                tw = max(self.metrics.width(line, size) for line in lines)
                self.scene.texts.append(Text(id + "-" + role, lines, max(tw / 2 + 8, x + w / 2), ty, tw,
                                             len(lines) * size * 1.4, size, "" if small_state else id,
                                             "state-label" if small_state else role, "middle", style,
                                             source=self.node_sources[id][role]))
                ty += len(lines) * size * 1.4 + 6

    def graph(self):
        for id, node in self.nodes.items():
            self.dimensions[id] = self.measure_node(node)
        # Peer nodes in a view have consistent dimensions within each style.
        for style in {n.get("style", "peer") for n in self.nodes.values()}:
            ids = [id for id, n in self.nodes.items() if n.get("style", "peer") == style
                   and n["kind"] not in ("gateway", "event", "initial", "final", "actor", "use_case")]
            if ids:
                size = tuple(max(self.dimensions[id][i] for id in ids) for i in (0, 1))
                self.dimensions.update({id: size for id in ids})
        roots = self.children.get(None, [])
        if self.template == "lanes":
            offsets = self.lane_positions()
        else:
            for id, group in self.groups.items():
                if not group.get("parent"):
                    self.measure_group(id)
        if self.template in ("tree", "statechart"):
            offsets = self.rank_positions(roots)
        elif self.template != "lanes":
            vertical = self.template == "layered" or \
                (self.template == "lanes" and self.model["layout"].get("direction") == "LR") or \
                (self.template == "grid_table" and self.model["layout"].get("direction", "TB") == "TB") or \
                (self.template not in ("lanes", "layered") and self.model["layout"].get("direction") == "TB")
            offsets, _ = self.arrange(roots, vertical=vertical,
                                     columns=len(roots) if self.template == "lanes" else None)
        for id, (x, y) in offsets.items():
            self.place(id, 40 + x, self.top + y)
        self.connect()

    def lane_positions(self):
        """Use one global time axis, with independent cross-axis lane packing."""
        ids = list(self.nodes)
        layers = rank_graph(ids, [(a, b) for a, b in self.projected_edges(ids)],
                            {id: n["rank"] for id, n in self.nodes.items() if "rank" in n})
        horizontal = self.model["layout"].get("direction", "TB") == "LR"
        axis, cross_axis = (0, 1) if horizontal else (1, 0)
        axis_padding = self.pad if horizontal else self.header
        maximum_depth = max((len(self.ancestors(id)) - 1 for id in ids), default=0)
        flow, positions = 0, {}
        for layer in layers:
            span = max((self.dimensions[id][axis] for id in layer), default=0)
            for id in layer:
                positions[id] = flow + (span - self.dimensions[id][axis]) / 2
            flow += span + self.rank_gap
        flow = max(0, flow - self.rank_gap)

        def coordinates(along, across):
            return (along, across) if horizontal else (across, along)

        def measure_group(id, depth):
            children = self.children.get(id, [])
            direct = [child for child in children if child in self.nodes]
            groups = [child for child in children if child in self.groups]
            offsets = {}
            bands = [[node for node in layer if node in direct] for layer in layers]
            cross_span = max((sum(self.dimensions[n][cross_axis] for n in band) +
                              max(0, len(band) - 1) * self.gap for band in bands), default=0)
            inset = self.header if horizontal else self.pad
            for band in bands:
                used = sum(self.dimensions[n][cross_axis] for n in band) + max(0, len(band) - 1) * self.gap
                cursor = inset + (cross_span - used) / 2
                for node in band:
                    along = positions[node] + (maximum_depth - depth + 1) * axis_padding
                    offsets[node] = coordinates(along, cursor)
                    cursor += self.dimensions[node][cross_axis] + self.gap
            cursor = inset + cross_span + (self.gap if direct and groups else 0)
            for group in groups:
                measure_group(group, depth + 1)
                offsets[group] = coordinates(axis_padding, cursor)
                cursor += self.dimensions[group][cross_axis] + self.gap
            if groups:
                cursor -= self.gap
            cross_size = max(cursor + self.pad, 96)
            along_size = flow + (maximum_depth - depth + 1) * axis_padding + self.pad
            title_width = self.metrics.required_width(self.groups[id]["title"], 16) + 2 * self.pad
            if horizontal:
                along_size = max(along_size, title_width)
            else:
                cross_size = max(cross_size, title_width)
            self.dimensions[id] = coordinates(along_size, cross_size)
            self.offsets[id] = offsets

        offsets, cursor = {}, 0
        for id in self.children.get(None, []):
            if id in self.groups:
                measure_group(id, 1)
                offsets[id] = coordinates(0, cursor)
            else:
                offsets[id] = coordinates(positions[id] + maximum_depth * axis_padding, cursor)
            cursor += self.dimensions[id][cross_axis] + self.gap
        return offsets

    def projected_edges(self, ids):
        def member(id):
            while id not in ids and self.items.get(id, {}).get("parent"):
                id = self.items[id]["parent"]
            return id if id in ids else None
        edges = []
        for edge in self.model.get("edges", []):
            source, target = member(edge["from"]), member(edge["to"])
            if source is not None and target is not None and (source != target or edge["from"] == edge["to"]):
                edges.append((source, target))
        return edges

    def rank_positions(self, ids):
        edges = self.projected_edges(ids)
        layers = rank_graph(ids, edges, {id: self.items[id]["rank"] for id in ids if "rank" in self.items[id]})
        ranks = {id: index for index, layer in enumerate(layers) for id in layer}
        if self.template == "tree" and any(ranks[a] >= ranks[b] for a, b in edges):
            raise ModelError("tree requires an acyclic graph; use statechart for cycles")
        vertical = self.model["layout"].get("direction") == "TB"
        flow_axis, cross_axis = (1, 0) if vertical else (0, 1)
        largest_cross = max((sum(self.dimensions[id][cross_axis] for id in layer) +
                             max(0, len(layer) - 1) * self.gap for layer in layers), default=0)
        result, flow = {}, 0
        for layer in layers:
            used = sum(self.dimensions[id][cross_axis] for id in layer) + max(0, len(layer) - 1) * self.gap
            cross = (largest_cross - used) / 2
            span = max((self.dimensions[id][flow_axis] for id in layer), default=0)
            for id in layer:
                position = (flow + (span - self.dimensions[id][flow_axis]) / 2, cross)
                result[id] = position[::-1] if vertical else position
                cross += self.dimensions[id][cross_axis] + self.gap
            flow += span + self.rank_gap
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
            obstacles = [b.rect for b in self.scene.boxes if b.id not in excluded and b.role != "label-bg"
                         and not (b.role == "group" and b.kind == "lane")]
            obstacles += [t.rect for t in self.scene.texts if t.role in ("group-title", "edge-label")
                          and t.owner not in (source.id, target.id)]
            obstacles += [t.rect for t in self.scene.texts
                          if t.owner in boxes and boxes[t.owner].kind == "actor"]
            same = [e for e in edges if (e["from"], e["to"]) == (edge["from"], edge["to"])]
            slot = sum(1 for e in edges[:i] if (e["from"], e["to"]) == (edge["from"], edge["to"]))
            points = route(source.glyph_rect, target.glyph_rect, obstacles, from_port=edge.get("from_port", "auto"),
                           to_port=edge.get("to_port", "auto"), slot=slot, slots=len(same),
                           previous=previous, waypoints=edge.get("waypoints", ()))
            points[0] = self.glyph_port(source, points[0], points[1])
            points[-1] = self.glyph_port(target, points[-1], points[-2])
            previous.append(points)
            self.add_edge(id, edge, points)
            value = edge.get("label", "")
            if "step" in edge:
                value = f"{edge['step']}. {value}".strip()
            if edge.get("cardinality"):
                for end, point, neighbour in (("from", points[0], points[1]), ("to", points[-1], points[-2])):
                    cardinality = edge["cardinality"].get(end)
                    if cardinality:
                        self.cardinality_label(id + "-" + end, cardinality, point, neighbour)
            if value:
                self.edge_label(id, value, points)

    @staticmethod
    def glyph_port(box, point, neighbour):
        """Extend the final orthogonal segment from bounds to the visible stroke."""
        x, y, w, h = box.glyph_rect
        cx, cy = x + w / 2, y + h / 2
        vertical = point[0] == neighbour[0]
        axis = 1 if vertical else 0
        outward = neighbour[axis] > point[axis]
        candidates = []
        if box.kind in ("use_case", "event", "initial", "final"):
            offset = (point[0] - cx) / (w / 2) if vertical else (point[1] - cy) / (h / 2)
            radius = (h if vertical else w) / 2 * math.sqrt(max(0, 1 - offset ** 2))
            center = cy if vertical else cx
            candidates = [center - radius, center + radius]
        elif box.kind == "actor":
            (hx, hy, radius), parts = box.actor_parts
            offset = point[0] - hx if vertical else point[1] - hy
            if abs(offset) <= radius:
                delta = math.sqrt(max(0, radius ** 2 - offset ** 2))
                center = hy if vertical else hx
                candidates.extend((center - delta, center + delta))
            cross_axis = 1 - axis
            for part in parts:
                for a, b in zip(part, part[1:]):
                    if a[cross_axis] == b[cross_axis]:
                        if abs(point[cross_axis] - a[cross_axis]) < 1e-6:
                            candidates.extend((a[axis], b[axis]))
                    elif min(a[cross_axis], b[cross_axis]) <= point[cross_axis] <= max(a[cross_axis], b[cross_axis]):
                        fraction = (point[cross_axis] - a[cross_axis]) / (b[cross_axis] - a[cross_axis])
                        candidates.append(a[axis] + fraction * (b[axis] - a[axis]))
        if not candidates:
            return point
        result = list(point)
        result[axis] = max(candidates) if outward else min(candidates)
        return tuple(result)

    def cardinality_label(self, id, value, point, neighbour):
        text = text_box(self.metrics, id, value, 0, 0, 70, 12, role="cardinality", anchor="middle")
        dx, dy = neighbour[0] - point[0], neighbour[1] - point[1]
        candidates = []
        if dx == 0:
            sign = 1 if dy > 0 else -1
            # Centre the text on an outward offset; dy<0 must subtract its height.
            for distance in (text.h / 2 + 12, text.h / 2 + 28):
                for side in (1, -1):
                    candidates.append((point[0] + side * (text.w / 2 + 12),
                                       point[1] + sign * distance - text.h / 2))
        else:
            sign = 1 if dx > 0 else -1
            for distance in (text.w / 2 + 12, text.w / 2 + 28):
                for side in (1, -1):
                    candidates.append((point[0] + sign * distance,
                                       point[1] + (12 if side == 1 else -text.h - 12)))
        occupied = [b.glyph_rect for b in self.scene.boxes if b.role != "group"]
        occupied += [t.rect for t in self.scene.texts]
        for x, y in candidates:
            if x - text.w / 2 >= 8 and y >= self.top - 10 and not any(
                    intersects((x - text.w / 2, y, text.w, text.h), rect, 3) for rect in occupied):
                text.x, text.y = x, y
                self.scene.texts.append(text)
                return
        text.x, text.y = candidates[0]
        self.scene.texts.append(text)
        self.scene.warnings.append({"rule": "label-placement", "elements": [id],
                                   "message": "No clear multiplicity slot; increase spacing or revise ports"})

    def add_edge(self, id, edge, points):
        status = edge.get("evidence", {}).get("status", "verified")
        dashed = edge.get("dashed", status != "verified" or edge.get("kind") in ("message", "reply"))
        self.scene.edges.append(Connector(id, points, edge["from"], edge["to"], edge.get("style", "peer"),
                                           edge.get("dir", "--" if self.template == "er" else "->"),
                                           dashed, edge.get("kind", "call")))

    def edge_label(self, id, value, points):
        segments = sorted(zip(points, points[1:]), key=lambda ab: -(abs(ab[0][0] - ab[1][0]) + abs(ab[0][1] - ab[1][1])))
        longest = segments[0]
        label_width = min(self.spacing["label_width"], max(16, abs(longest[0][0] - longest[1][0]) - 24)) \
            if longest[0][1] == longest[1][1] else self.spacing["label_width"]
        text = text_box(self.metrics, id + "-label", value, 0, 0, label_width, 12, id, "edge-label", "middle")
        candidates = []
        for a, b in segments:
            for fraction in (0.5, 0.35, 0.65):
                mx, my = a[0] + (b[0] - a[0]) * fraction, a[1] + (b[1] - a[1]) * fraction
                if a[1] == b[1]:
                    for offset in (1, 2, 3):
                        clearance = self.spacing["label_clearance"] * offset
                        candidates.extend([(mx, my - text.h - clearance), (mx, my + clearance)])
                else:
                    for offset in (1, 2, 3):
                        clearance = self.spacing["label_clearance"] * offset
                        candidates.extend([(mx + text.w / 2 + clearance, my - text.h / 2),
                                           (mx - text.w / 2 - clearance, my - text.h / 2)])
        occupied = [b.glyph_rect for b in self.scene.boxes if b.role != "group"]
        occupied += [t.rect for t in self.scene.texts]
        chosen = None
        for x, y in candidates:
            rect = (x - text.w / 2 - 5, y - 4, text.w + 10, text.h + 8)
            crossed = any(segment_hits_rect(a, b, rect, padding=2) for edge in self.scene.edges if edge.id != id
                          and edge.kind not in ("lifeline", "legend") for a, b in zip(edge.points, edge.points[1:]))
            if x - text.w / 2 > 0 and y > 8 and not crossed and not any(intersects(rect, b, 3) for b in occupied):
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
            self.place(id, 40 + i * (width + self.gap), self.top)
            centers[id] = 40 + i * (width + self.gap) + width / 2
        edges = sorted(enumerate(self.model.get("edges", [])), key=lambda pair: pair[1].get("step", pair[0] + 1))
        frames = sorted(enumerate(self.model.get("frames", [])),
                        key=lambda pair: (pair[1]["from_step"], -pair[1]["to_step"], pair[0]))
        bands, frame_info = {}, {}
        right = max(centers.values()) + width / 2 + 24
        frame_words = [self.metrics.required_width(value, 12)
                       for _, frame in frames
                       for value in [frame.get("label", ""), frame.get("guard", ""),
                                     *(operand["guard"] for operand in frame.get("operands", []))]]
        right = max(right, max(frame_words, default=0) + 48 + 24 * len(frames))
        for _, frame in frames:
            parents = [info for info in frame_info.values()
                       if info["frame"]["from_step"] <= frame["from_step"] and
                       info["frame"]["to_step"] >= frame["to_step"]]
            parent = parents[-1] if parents else None
            depth = len(parents)
            left, frame_right = 24 + depth * 12, right - depth * 12
            title = frame.get("operator", "")
            if frame.get("guard"):
                title += " [" + frame["guard"].strip("[]") + "]"
            if frame.get("label"):
                title += (" · " if title else "") + frame["label"]
            heading = text_box(self.metrics, frame["id"] + "-title", title,
                               left + 12, 0, frame_right - left - 24, 12, frame["id"], "group-title")
            info = {"frame": frame, "left": left, "right": frame_right, "heading": heading,
                    "parent": parent, "guards": []}
            frame_info[frame["id"]] = info
            bands.setdefault(frame["from_step"], []).append((info, heading, False))
            for index, operand in enumerate(frame.get("operands", [])):
                guard = text_box(self.metrics, frame["id"] + f"-guard-{index + 1}",
                                 "[" + operand["guard"].strip("[]") + "]", left + 12, 0,
                                 frame_right - left - 24, 12, frame["id"], "operand-guard")
                info["guards"].append(guard)
                bands.setdefault(operand["from_step"], []).append((info, guard, index > 0))
        ys, cursor = {}, self.top + height + 32
        for i, edge in edges:
            step = edge.get("step", i + 1)
            for info, text, separator in bands.get(step, []):
                text.y = cursor + 8
                if text is info["heading"]:
                    info["top"] = cursor
                if separator:
                    self.scene.edges.append(Connector(text.id + "-separator",
                        [(info["left"], cursor), (info["right"], cursor)], "", "",
                        direction="--", dashed=True, kind="frame-separator"))
                self.scene.texts.append(text)
                cursor += text.h + 16
            label = f"{step}. {edge.get('label', '')}".strip()
            label_height = len(self.metrics.wrap(label, max(self.metrics.required_width(label, 12),
                                                          min(120, width + self.gap - 24)), 12)) * 16.8
            ys[step] = cursor + label_height + 24
            ending = sum(info["frame"]["to_step"] == step for info in frame_info.values())
            cursor = ys[step] + max(64 if edge["from"] == edge["to"] else 48, 32 + ending * 12 + 12)
        bottom = cursor + 24
        for node in nodes:
            x = centers[node["id"]]
            self.scene.edges.append(Connector(node["id"] + "-lifeline",
                                               [(x, self.top + height), (x, bottom)],
                                               node["id"], node["id"], direction="--", dashed=True, kind="lifeline"))
        for info in reversed(list(frame_info.values())):
            last = next(edge for i, edge in edges if edge.get("step", i + 1) == info["frame"]["to_step"])
            info["bottom"] = max(ys[info["frame"]["to_step"]] + (64 if last["from"] == last["to"] else 32),
                                 max((child["bottom"] + 12 for child in frame_info.values()
                                      if child["parent"] is info), default=0))
        frame_boxes = []
        for info in frame_info.values():
            frame_boxes.append(Box(info["frame"]["id"], info["left"], info["top"],
                                   info["right"] - info["left"], info["bottom"] - info["top"],
                                   "group", "frame", parent=info["parent"]["frame"]["id"] if info["parent"] else ""))
        self.scene.boxes = frame_boxes + self.scene.boxes
        self.scene.edges.sort(key=lambda e: 0 if e.kind == "lifeline" else 1)
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

    def table(self, width=None):
        width = self.document_width - 80 if width is None else width
        y = self.top
        for table in self.model.get("tables", []):
            if table.get("title"):
                title = text_box(self.metrics, table["id"] + "-title", table["title"], 40, y, width, 16, role="table-title")
                self.scene.texts.append(title)
                y += title.h + 16
            count = len(table["columns"])
            rows = [table["columns"], *table["rows"]]
            widths = [max(110, min(250, width / count),
                          max(self.metrics.required_width(row[c], 13) + 24 for row in rows))
                      for c in range(count)]
            for r, row in enumerate([table["columns"], *table["rows"]]):
                wrapped = [self.metrics.wrap(value, widths[c] - 24, 13) for c, value in enumerate(row)]
                h = max(48, max(len(lines) for lines in wrapped) * 18.2 + 24)
                for c, lines in enumerate(wrapped):
                    id = f"__{table['id']}-r{r}-c{c}"
                    x = 40 + sum(widths[:c])
                    cell_w = widths[c]
                    style = "primary" if r == 0 else "peer"
                    self.scene.boxes.append(Box(id, x, y, cell_w, h, "cell", style=style))
                    w = max(self.metrics.width(line, 13) for line in lines)
                    self.scene.texts.append(Text(id + "-text", lines, x + 12, y + 12, w, len(lines) * 18.2,
                                                13, id, "cell-text", style=style, source=row[c]))
                y += h
            y += 48

    def mixed_table(self):
        available = (self.document_width - self.gap - 80) * 0.6
        table_width = max((sum(max(110, min(250, available / len(t["columns"])),
                                  max(self.metrics.required_width(row[c], 13) + 24
                                      for row in [t["columns"], *t["rows"]]))
                              for c in range(len(t["columns"])))
                           for t in self.model.get("tables", [])), default=0)
        self.graph()
        shift = table_width + self.gap
        for box in self.scene.boxes:
            box.x += shift
        for text in self.scene.texts:
            if text.role != "title":
                text.x += shift
        for edge in self.scene.edges:
            edge.points = [(x + shift, y) for x, y in edge.points]
        self.table(available)

    def finish(self):
        scene = self.scene
        bottom = max([self.top] + [b.y + b.h for b in scene.boxes] + [t.y + t.h for t in scene.texts]
                     + [p[1] for e in scene.edges for p in e.points])
        right = max([self.document_width - 40] + [b.x + b.w for b in scene.boxes] + [t.left + t.w for t in scene.texts]
                    + [p[0] for e in scene.edges for p in e.points])
        legend = legend_entries(scene, self.model)
        x, y = 40, bottom + 40
        for i, entry in enumerate(legend):
            label = text_box(self.metrics, f"legend-{i}", entry["label"], x + 40, y, 260, 11, role="legend")
            if x + label.w + 50 > right and x != 40:
                x, y = 40, y + 48
                label.x, label.y = x + 40, y
            if entry.get("symbol") == "box":
                scene.boxes.append(Box(f"__legend-swatch-{i}", x, y + 2, 28, 16, "legend-swatch",
                                       style=entry.get("style", "peer"), dashed=entry.get("dashed", False)))
            else:
                scene.edges.append(Connector(f"legend-line-{i}", [(x, y + 10), (x + 28, y + 10)], "", "",
                                             entry.get("style", "peer"), entry.get("dir", "--"),
                                             entry.get("dashed", False), "legend", entry.get("kind", "")))
            scene.texts.append(label)
            x += label.w + 76
        profile = self.model["layout"].get("profile", "doc")
        scene.width = 1440 if profile in ("slide", "slide-16x9") else max(self.document_width, right + 40)
        scene.height = 810 if profile in ("slide", "slide-16x9") else max(300, y + 68)
        if profile in ("doc", "doc-1120xN") and scene.width > self.document_width * self.spacing["wide_view_ratio"]:
            scene.warnings.append({"rule": "wide-view", "message": "Content exceeds the theme's wide-view limit; split the view or configure the target width"})
        for text in scene.texts:
            text.runs = [self.metrics.runs(line) for line in text.lines]
            text.line_widths = [self.metrics.width(line, text.size) for line in text.lines]
            for runs in text.runs:
                offset = 0
                for run in runs:
                    run["offset"] = offset
                    offset += self.metrics.width(run["text"], text.size)
        scene.warnings.extend(self.metrics.warnings)
        scene.family, scene.measured_with = self.metrics.family, self.metrics.measured_with
        for node in self.nodes.values():
            if node.get("evidence", {}).get("status") not in (None, "verified"):
                scene.warnings.append({"rule": "evidence", "message": node["evidence"]["status"], "elements": [node["id"]]})
        return scene


def layout(model, metrics=None):
    validate(model)
    engine = Layout(model, metrics or FontMetrics(lang=model["meta"].get("lang", "en")))
    if engine.template == "sequence":
        engine.sequence()
    elif engine.template == "grid_table":
        if engine.nodes or engine.groups:
            engine.mixed_table()
        else:
            engine.table()
    else:
        engine.graph()
    return engine.finish()
