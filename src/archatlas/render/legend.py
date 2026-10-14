"""Only explain distinct visible encodings; explicit author entries win."""
from .theme import THEMES
from .legend_text import FAMILY_RELATIONS, TYPE_RELATIONS, edge_label, group_label, local, style_label


def entries(scene, model):
    theme = THEMES[scene.theme]
    result, labels, covered = [], set(), set()

    def signature(style, dashed, symbol="line"):
        return theme[style][1], dashed, symbol

    def append(entry, cover=True):
        label = " ".join(entry["label"].split()).casefold()
        if label not in labels:
            labels.add(label)
            result.append(entry)
            if cover:
                covered.add(signature(entry.get("style", "peer"), entry.get("dashed", False),
                                      entry.get("symbol", "line")))

    for entry in model["meta"].get("legend", []):
        append(dict(entry), any(k in entry for k in ("style", "dashed", "symbol", "kind", "dir")))
    if model["meta"].get("legend_mode", "auto") == "replace":
        return result
    variants = {}
    for edge in scene.edges:
        if edge.kind in ("lifeline", "legend"):
            continue
        key = (theme[edge.style][1], edge.dashed, edge.kind in ("async", "message"),
               edge.direction, edge.kind == "message")
        variants.setdefault(key, []).append(edge)
    auto_colours = set()
    for key, edges in variants.items():
        has_meaning = (model["layout"]["template"] in FAMILY_RELATIONS or
                       model["meta"]["type"].upper() in TYPE_RELATIONS or
                       model["meta"].get("legend_labels", {}).get("edges"))
        if len(variants) == 1 and not key[2] and key[3] != "<->" and not has_meaning:
            continue
        edge = edges[0]
        if signature(edge.style, edge.dashed) in covered:
            continue
        label = " / ".join(dict.fromkeys(edge_label(e, model) for e in edges))
        append({"label": label, "style": edge.style, "dashed": edge.dashed,
                "kind": edge.kind, "dir": edge.direction}, cover=False)
        auto_colours.add(signature(edge.style, edge.dashed))
    covered.update(auto_colours)
    styles = {}
    for box in scene.boxes:
        if box.role == "node":
            styles.setdefault((*theme[box.style], box.dashed), box)
    if len(styles) > 1 or model["meta"].get("legend_labels", {}).get("styles"):
        for box in styles.values():
            if signature(box.style, box.dashed, "box") not in covered:
                append({"label": style_label(box.style, model) +
                        (local(model, (" (dashed)", "（虚线）")) if box.dashed else ""),
                        "style": box.style, "dashed": box.dashed, "symbol": "box"})
    groups = {}
    for box in scene.boxes:
        if box.role == "group":
            groups.setdefault(box.dashed, []).append(box)
    explicit = model["meta"].get("legend_labels", {}).get("groups")
    if groups and (explicit or model["meta"]["type"].upper() in ("F2", "G1", "G3", "A5") or len(groups) > 1):
        for dashed, boxes in groups.items():
            if signature("peer", dashed, "box") not in covered:
                append({"label": " / ".join(dict.fromkeys(group_label(b.kind, model) for b in boxes)),
                        "dashed": dashed, "symbol": "box"})
    return result
