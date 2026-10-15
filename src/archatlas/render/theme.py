"""One default visual language: saturated focus, tinted zones and asset cards."""
SPACING = {
    "node_gap": 48, "rank_gap": 48, "boundary_gap": 112, "gap_ratio": 0.25,
    "group_padding": 24, "group_header": 52, "document_width": 1120, "wide_view_ratio": 1.5,
    "label_width": 120, "label_clearance": 12,
}
THEMES = {
    "neutral": {
        "canvas": "#ffffff", "text": "#1F2937", "muted": "#4B5563",
        "primary": ("#1767B5", "#03172E"), "peer": ("#D8E8FF", "#3D6FB2"),
        "external": ("#EDEDED", "#666A73"), "shared": ("#DCF2DC", "#397645"),
        "planned": ("#EBDDF9", "#7951A5"), "highlight": ("#FFF1C9", "#936A16"),
        "boundary": ("#F3F8FF", "#3D6FB2"), "on_primary": "#ffffff",
    },
    "print": {
        "canvas": "#ffffff", "text": "#111111", "muted": "#333333",
        **{key: ("#ffffff", "#333333") for key in ("primary", "peer", "external", "shared", "planned", "highlight", "boundary")},
        "on_primary": "#111111",
    },
    "dark": {
        "canvas": "#111827", "text": "#f8fafc", "muted": "#d1d5db",
        "primary": ("#172b4d", "#93b8ff"), "peer": ("#1f2937", "#b8c8db"),
        "external": ("#352c18", "#edcc85"), "shared": ("#18382e", "#8ed7b9"),
        "planned": ("#34233d", "#d5a9ec"), "boundary": ("#111827", "#b8c8db"),
        "highlight": ("#352c18", "#edcc85"), "on_primary": "#f8fafc",
    },
}

for theme in THEMES.values():
    theme["spacing"] = dict(SPACING)
    theme["components"] = {
        "card_radius": 8, "zone_radius": 10, "pill_radius": 10,
        "card_stroke": 1.8, "primary_stroke": 2.4, "zone_stroke": 1.6,
        "edge_stroke": 1.8, "chip_gap": 6, "chip_padding": 9,
        "chip_vertical_padding": 5, "badge_diameter": 30, "badge_padding": 10,
        "asset_cap": 12, "document_fold": 18,
    }
    theme["zones"] = {
        key: (theme["boundary"][0], theme[style][0], theme[style][1])
        for key, style in (("app", "peer"), ("tech", "shared"), ("data", "planned"),
                           ("biz", "highlight"), ("security", "highlight"), ("neutral", "external"))
    }
    theme["lines"] = {key: theme[key][1] for key in
                      ("primary", "peer", "external", "shared", "planned", "highlight")}

THEMES["neutral"]["zones"] = {
    "app": ("#F3F8FF", "#D8E8FF", "#3D6FB2"),
    "tech": ("#F0F9F0", "#DCF2DC", "#397645"),
    "data": ("#F8F3FD", "#EBDDF9", "#7951A5"),
    "biz": ("#FFFBEB", "#FFF1C9", "#936A16"),
    "security": ("#FFF4F1", "#FFE1DC", "#B34232"),
    "neutral": ("#F7F7F7", "#EDEDED", "#666A73"),
}
THEMES["neutral"]["lines"].update(peer="#4B5563", primary="#2563EB")


def node_shape(node):
    return node.get("shape", {"store": "database", "queue": "queue",
                             "document": "document", "note": "callout",
                             "callout": "callout"}.get(node["kind"], "card"))


def node_style(node):
    return node.get("style", "highlight" if node_shape(node) == "callout" else
                    "external" if node["kind"] == "external" else "peer")
