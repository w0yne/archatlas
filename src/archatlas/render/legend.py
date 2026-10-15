"""Legends cover visible encodings; authored captions customize matching swatches."""
from .theme import THEMES
from .legend_text import edge_label, group_label, local, style_label

_SYMBOLS = {"actor": ("Actor", "参与者"), "event": ("Event", "事件"),
            "gateway": ("Gateway", "网关"), "use_case": ("Use case", "用例"),
            "initial": ("Initial state", "初始状态"), "final": ("Final state", "终止状态"),
            "task": ("Task", "任务"), "state": ("State", "状态")}
_ASSETS = {"database": ("Data store (cylinder)", "数据存储（圆柱）"),
           "document": ("Document", "文档"), "queue": ("Queue", "队列"),
           "callout": ("Note or example", "说明或示例")}
_TINTS = {"app": ("blue tint", "蓝色区域"), "tech": ("green tint", "绿色区域"),
          "data": ("purple tint", "紫色区域"), "biz": ("amber tint", "琥珀色区域"),
          "security": ("red tint", "红色区域"), "neutral": ("gray tint", "灰色区域")}
_EVIDENCE = {"inferred": ("Inferred, not verified", "推断，未经核实"),
             "doc-only": ("Documented only, not verified", "仅文档记载，未经核实"),
             "conflict": ("Conflicting evidence", "证据存在冲突")}


def entries(scene, model):
    theme = THEMES[scene.theme]
    tokens = theme["components"]
    ordered = model["layout"].get("ordered", model["layout"]["template"] == "sequence")
    numbers = local(model, ("Numbers show flow order", "编号表示流程顺序") if ordered else
                    ("Numbers are labels for reference", "编号仅用于引用，不表示顺序"))

    def key(entry):
        """Compare rendered appearance, including shape and marker variants."""
        symbol, style = entry["symbol"], entry.get("style", "peer")
        dashed = entry.get("dashed", False)
        kind = entry.get("node_kind", "")
        if symbol == "line":
            marker = entry.get("kind", "call")
            direction = entry.get("dir", "->")
            end = ("open" if marker in ("async", "reply", "message") else "filled") if direction != "--" else None
            start = end if direction == "<->" else "circle" if marker == "message" else None
            return symbol, theme["lines"][style], dashed, start, end
        if symbol == "zone":
            body, header, stroke = theme["zones"][entry["tint"]]
            return symbol, body, header if entry["band"] else None, stroke, dashed, kind == "frame", \
                entry.get("band_axis", "y") if entry["band"] else None
        fill, stroke = theme[style]
        weight = tokens["primary_stroke"] if style == "primary" else tokens["card_stroke"]
        if symbol == "badge":
            return symbol, fill, stroke, weight, dashed
        shape = entry.get("shape", "card")
        radius = tokens["pill_radius"] if kind == "chip" else 12 if kind in ("task", "state") else tokens["card_radius"]
        glyph = ("rect", radius)
        if shape in ("database", "document"):
            glyph = (shape,)
        elif kind == "actor":
            glyph, fill = (kind,), "none"
        elif kind == "gateway":
            glyph = (kind,)
        elif kind in ("event", "initial", "final", "use_case"):
            glyph = ("ellipse", kind == "final", kind != "use_case")
            if kind == "event":
                weight = 4 if entry.get("event_type") == "end" else 1.5
            if kind == "initial":
                fill = stroke
        # Queue rails and callout accents are drawn on top of the base glyph.
        return symbol, fill, stroke, weight, dashed, glyph, shape if shape in ("queue", "callout") else None

    def normalized(label):
        return " ".join(label.split()).casefold()

    def merge(labels, label):
        if normalized(label) not in {normalized(value) for value in labels}:
            labels.append(label)

    actual, captions, required, visible, badge_values = {}, {}, {}, [], {}

    def record(entry, explanations=()):
        signature = key(entry)
        visible.append(entry)
        actual.setdefault(signature, dict(entry))
        merge(captions.setdefault(signature, []), entry["label"])
        for explanation in explanations:
            merge(required.setdefault(signature, []), explanation)
        if entry["symbol"] == "badge":
            badge_values.setdefault(signature, set()).add(entry["badge"])

    def evidence(item):
        status = item.get("evidence", {}).get("status")
        return [local(model, _EVIDENCE[status])] if status in _EVIDENCE else []

    edges = {edge.get("id", f"edge-{i + 1}"): edge for i, edge in enumerate(model.get("edges", []))}
    nodes = {node["id"]: node for node in model.get("nodes", [])}
    texts = {text.owner: text.source for text in scene.texts if text.source}
    for edge in scene.edges:
        if edge.kind in ("legend", "lifeline", "frame-separator"):
            continue
        explanations = evidence(edges.get(edge.id, {}))
        if edge.numbered and not edge.badge:
            explanations.append(numbers)
        record({"label": edge_label(edge, model), "symbol": "line", "style": edge.style,
                "dashed": edge.dashed, "kind": edge.marker_kind or edge.kind, "dir": edge.direction}, explanations)
    for box in scene.boxes:
        if box.role == "node":
            label = style_label(box.style, model)
            if box.shape in _ASSETS:
                label += " · " + local(model, _ASSETS[box.shape])
            elif box.kind in _SYMBOLS:
                label += " · " + local(model, _SYMBOLS[box.kind])
                if box.kind == "event":
                    label += local(model, (" (end)", "（结束）") if box.event_type == "end" else (" (start)", "（开始）"))
            if box.dashed:
                label += local(model, (" (dashed)", "（虚线）"))
            record({"label": label, "symbol": "box", "style": box.style, "dashed": box.dashed,
                    "shape": box.shape, "node_kind": box.kind if box.kind in _SYMBOLS else "",
                    "event_type": box.event_type}, evidence(nodes.get(box.id, {})))
        elif box.role == "chip":
            record({"label": local(model, ("Tag or property", "标签或属性")) + " · " + style_label(box.style, model),
                    "symbol": "box", "style": box.style, "dashed": box.dashed,
                    "shape": box.shape, "node_kind": "chip"})
        elif box.role == "group":
            tint_label = _TINTS[box.tint] if scene.theme == "neutral" else ("zone tint", "区域色调")
            label = group_label(box.kind, model) + " · " + local(model, tint_label)
            if box.dashed:
                label += local(model, (" (dashed)", "（虚线）"))
            if not box.band:
                label += local(model, (" (no header band)", "（无标题带）"))
            record({"label": label, "symbol": "zone", "style": box.style, "tint": box.tint,
                    "band": box.band, "band_axis": "x" if box.header_width else "y",
                    "dashed": box.dashed, "node_kind": box.kind})
        elif box.role in ("badge", "edge-badge"):
            label = numbers if box.role == "edge-badge" else local(model, ("Node badges identify elements", "节点徽章用于标识元素"))
            record({"label": label, "symbol": "badge", "style": box.style,
                    "dashed": box.dashed, "badge": texts.get(box.id, ""), "badge_role": box.role}, [label])

    # Authored selectors only rename encodings that exist. Symbol-only selectors
    # are valid; free prose cannot invent a glyph or suppress uncovered encodings.
    fields = ("style", "dashed", "kind", "dir", "shape", "tint", "band", "badge")
    authored_captions, authored_order, specificity = {}, [], {}
    for authored in model["meta"].get("legend", []):
        symbol = authored.get("symbol", "line")
        text_only = symbol == "text" or ("symbol" not in authored and not any(field in authored for field in fields))
        precision = sum(field in authored for field in fields)
        if not text_only and not precision and len({
                key(candidate) for candidate in visible if candidate["symbol"] == symbol}) != 1:
            # A symbol alone cannot tell which of several different encodings a
            # prose caption describes. Keep their known meanings instead.
            continue
        for candidate in visible:
            signature = key(candidate)
            if text_only:
                matches = normalized(authored["label"]) in {normalized(label) for label in captions[signature]}
            else:
                matches = candidate["symbol"] == symbol and all(
                    field not in authored or (str(authored[field]) in badge_values.get(signature, set()) if field == "badge"
                                               else authored[field] == candidate.get(field))
                    for field in fields)
            if not matches:
                continue
            if precision < specificity.get(signature, -1):
                continue
            if signature not in authored_captions:
                authored_order.append(signature)
            # Later author captions retain the established override behavior,
            # but never produce a second swatch for the same encoding.
            authored_captions[signature] = authored["label"]
            specificity[signature] = precision
            if "badge" in authored:
                actual[signature]["badge"] = str(authored["badge"])

    result = []
    for signature in authored_order + [signature for signature in actual if signature not in authored_captions]:
        labels = [authored_captions[signature]] if signature in authored_captions else list(captions[signature])
        for explanation in required.get(signature, []):
            merge(labels, explanation)
        result.append({**actual[signature], "label": " / ".join(labels)})
    return result
