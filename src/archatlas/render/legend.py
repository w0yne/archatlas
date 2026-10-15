"""Legends describe actual scene encodings; authored captions can override them."""
from .theme import THEMES
from .legend_text import edge_label, group_label, local, style_label

_FORMAL = {"actor", "event", "gateway", "use_case", "initial", "final"}
_SYMBOLS = {"actor": ("Actor", "参与者"), "event": ("Event", "事件"),
            "gateway": ("Gateway", "网关"), "use_case": ("Use case", "用例"),
            "initial": ("Initial state", "初始状态"), "final": ("Final state", "终止状态")}
_ASSETS = {"database": ("Data store (cylinder)", "数据存储（圆柱）"),
           "document": ("Document", "文档"), "queue": ("Queue", "队列"),
           "callout": ("Note or example", "说明或示例")}
_TINTS = {"app": ("blue tint", "蓝色区域"), "tech": ("green tint", "绿色区域"),
          "data": ("purple tint", "紫色区域"), "biz": ("amber tint", "琥珀色区域"),
          "security": ("red tint", "红色区域"), "neutral": ("gray tint", "灰色区域")}


def entries(scene, model):
    theme = THEMES[scene.theme]
    ordered = model["layout"].get("ordered", model["layout"]["template"] == "sequence")
    numbers = local(model, ("Numbers show flow order", "编号表示流程顺序") if ordered else
                    ("Numbers are labels for reference", "编号仅用于引用，不表示顺序"))

    def key(entry):
        symbol, style = entry.get("symbol", "line"), entry.get("style", "peer")
        dashed = entry.get("dashed", False)
        if symbol == "text":
            return symbol, entry["label"].casefold()
        if symbol == "line":
            kind = entry.get("kind", "call")
            return symbol, theme["lines"][style], dashed, kind in ("async", "reply", "message"), kind == "message", entry.get("dir", "->")
        if symbol == "zone":
            body, header, stroke = theme["zones"][entry["tint"]]
            return symbol, body, header if entry["band"] else None, stroke, dashed, entry.get("node_kind") == "frame"
        if symbol == "badge":
            return symbol, theme[style], entry.get("badge_role", "badge")
        return (symbol, theme[style], dashed, entry.get("shape", "card"), entry.get("node_kind", ""),
                entry.get("event_type", ""), style == "primary")

    actual, badge_values, visible = {}, {}, []

    def record(entry):
        signature = key(entry)
        visible.append(dict(entry))
        if entry["symbol"] == "badge":
            badge_values.setdefault(signature, set()).add(entry["badge"])
        if signature not in actual:
            actual[signature] = entry
        elif entry["label"] not in actual[signature]["label"].split(" / "):
            actual[signature]["label"] += " / " + entry["label"]

    for edge in scene.edges:
        if edge.kind in ("legend", "lifeline", "frame-separator"):
            continue
        record({"label": edge_label(edge, model), "symbol": "line", "style": edge.style,
                "dashed": edge.dashed, "kind": edge.kind, "dir": edge.direction})
    for box in scene.boxes:
        if box.role == "node":
            label = style_label(box.style, model)
            if box.shape in _ASSETS:
                label += " · " + local(model, _ASSETS[box.shape])
            elif box.kind in _SYMBOLS:
                label += " · " + local(model, _SYMBOLS[box.kind])
            if box.dashed:
                label += local(model, (" (dashed)", "（虚线）"))
            record({"label": label, "symbol": "box", "style": box.style, "dashed": box.dashed,
                    "shape": box.shape, "node_kind": box.kind if box.kind in _FORMAL else "",
                    "event_type": box.event_type})
        elif box.role == "group":
            tint_label = _TINTS[box.tint] if scene.theme == "neutral" else ("zone tint", "区域色调")
            label = group_label(box.kind, model) + " · " + local(model, tint_label)
            if box.dashed:
                label += local(model, (" (dashed)", "（虚线）"))
            if not box.band:
                label += local(model, (" (no header band)", "（无标题带）"))
            record({"label": label, "symbol": "zone", "style": box.style, "tint": box.tint,
                    "band": box.band, "dashed": box.dashed, "node_kind": box.kind})
        elif box.role in ("badge", "edge-badge"):
            value = next(t.source for t in scene.texts if t.owner == box.id)
            record({"label": numbers if box.role == "edge-badge" else local(model, ("Node badges identify elements", "节点徽章用于标识元素")),
                    "symbol": "badge", "style": box.style, "badge": value, "badge_role": box.role})

    result, covered, seen, authored_positions = [], set(), set(), {}

    def append(entry):
        signature = key(entry)
        item = signature, " ".join(entry["label"].split()).casefold()
        if item not in seen:
            seen.add(item)
            result.append(entry)
            covered.add(signature)

    fields = ("style", "dashed", "kind", "dir", "shape", "tint", "band", "badge")
    for authored in model["meta"].get("legend", []):
        if authored.get("symbol") == "text" or not any(field in authored for field in fields):
            append({"label": authored["label"], "symbol": "text"})
            continue
        symbol = authored.get("symbol", "line")
        # Reuse the matching glyph instead of drawing an assumed default swatch.
        # A typed entry that matches no visible encoding is omitted.
        for candidate in visible:
            if candidate["symbol"] == symbol and all(
                    field not in authored or (str(authored[field]) in badge_values.get(key(candidate), set()) if field == "badge"
                                               else authored[field] == candidate.get(field))
                    for field in fields):
                selected = {**candidate, "label": authored["label"]}
                if "badge" in authored:
                    selected["badge"] = str(authored["badge"])
                signature = key(selected)
                if signature in authored_positions:
                    result[authored_positions[signature]] = selected
                else:
                    authored_positions[signature] = len(result)
                    append(selected)
    if model["meta"].get("legend_mode", "auto") != "replace":
        for signature, entry in actual.items():
            if signature not in covered:
                append(entry)
        evidence_labels = {"inferred": ("Inferred, not verified", "推断，未经核实"),
                           "doc-only": ("Documented only, not verified", "仅文档记载，未经核实"),
                           "conflict": ("Conflicting evidence", "证据存在冲突")}
        for collection in ("nodes", "edges"):
            for status in dict.fromkeys(item.get("evidence", {}).get("status") for item in model.get(collection, [])):
                if status in evidence_labels:
                    append({"label": local(model, evidence_labels[status]) +
                            local(model, (" — elements", "（元素）") if collection == "nodes" else (" — relationships", "（关系）")),
                            "symbol": "text"})
    # Identifier semantics remain explicit even when authors replace style captions.
    if any(edge.numbered for edge in scene.edges) and not any(entry["label"] == numbers for entry in result):
        append({"label": numbers, "symbol": "text"})
    return result
