"""Only explain distinct visible encodings; explicit author entries win."""
from .theme import THEMES


def entries(scene, model):
    theme = THEMES[scene.theme]
    zh = model["meta"].get("lang", "").startswith("zh")
    words = {"call": "调用", "data": "数据", "async": "异步", "message": "消息",
             "dependency": "依赖", "assoc": "关联", "dashed": "虚线", "peer": "同级",
             "primary": "重点", "external": "外部", "shared": "共享", "planned": "规划",
             "boundary": "边界", "inferred": "推断", "doc-only": "仅文档", "conflict": "冲突",
             "bidirectional": "双向"}
    local = lambda word: words.get(word, word) if zh else word
    result, labels, covered = [], set(), set()

    def signature(style, dashed):
        return theme[style][1], dashed

    def append(entry, cover=True):
        label = " ".join(entry["label"].split()).casefold()
        if label not in labels:
            labels.add(label)
            result.append(entry)
            if cover:
                covered.add(signature(entry.get("style", "peer"), entry.get("dashed", False)))

    for entry in model["meta"].get("legend", []):
        append(dict(entry), "style" in entry or "dashed" in entry)
    variants = {}
    for edge in scene.edges:
        if edge.kind in ("lifeline", "legend"):
            continue
        key = (theme[edge.style][1], edge.dashed, edge.kind in ("async", "message"),
               edge.direction, edge.kind == "message")
        variants.setdefault(key, []).append(edge)
    auto_colours = set()
    for key, edges in variants.items():
        if len(variants) == 1 and not key[2] and key[3] != "<->":
            continue
        edge = edges[0]
        if signature(edge.style, edge.dashed) in covered:
            continue
        label = " / ".join(local(kind) for kind in dict.fromkeys(e.kind for e in edges))
        if edge.style != "peer":
            label = local(edge.style) + " · " + label
        if edge.dashed:
            label += " · " + local("dashed")
        if edge.direction == "<->":
            label += " · " + local("bidirectional")
        append({"label": label, "style": edge.style, "dashed": edge.dashed,
                "kind": edge.kind, "dir": edge.direction}, cover=False)
        auto_colours.add(signature(edge.style, edge.dashed))
    covered.update(auto_colours)
    styles = {}
    for box in scene.boxes:
        if box.role == "node":
            styles.setdefault((*theme[box.style], box.dashed), box)
    if len(styles) > 1:
        for box in styles.values():
            if signature(box.style, box.dashed) not in covered:
                append({"label": local(box.style) + (" · " + local("dashed") if box.dashed else ""),
                        "style": box.style, "dashed": box.dashed, "symbol": "box"})
    boundaries = {(box.kind, box.dashed) for box in scene.boxes if box.role == "group"}
    if len(boundaries) > 1 and any(dashed for _, dashed in boundaries):
        if signature("peer", True) not in covered:
            append({"label": local("boundary") + " · " + local("dashed"), "dashed": True, "symbol": "box"})
    return result
