"""Semantic colour tokens; no per-project palettes."""
SPACING = {
    "node_gap": 48, "rank_gap": 48, "boundary_gap": 112, "gap_ratio": 0.25,
    "group_padding": 24, "group_header": 52, "document_width": 1120, "wide_view_ratio": 1.5,
    "label_width": 120, "label_clearance": 12,
}
THEMES = {
    "neutral": {
        "canvas": "#ffffff", "text": "#172b4d", "muted": "#42526e",
        "primary": ("#e7efff", "#2455a4"), "peer": ("#f7f9fc", "#52647d"),
        "external": ("#fff5df", "#805d12"), "shared": ("#e2f3ec", "#22644d"),
        "planned": ("#f3eafa", "#75458b"), "boundary": ("#ffffff", "#52647d"),
    },
    "print": {
        "canvas": "#ffffff", "text": "#111111", "muted": "#333333",
        **{key: ("#ffffff", "#333333") for key in ("primary", "peer", "external", "shared", "planned", "boundary")},
    },
    "dark": {
        "canvas": "#111827", "text": "#f8fafc", "muted": "#d1d5db",
        "primary": ("#172b4d", "#93b8ff"), "peer": ("#1f2937", "#b8c8db"),
        "external": ("#352c18", "#edcc85"), "shared": ("#18382e", "#8ed7b9"),
        "planned": ("#34233d", "#d5a9ec"), "boundary": ("#111827", "#b8c8db"),
    },
}

for theme in THEMES.values():
    theme["spacing"] = dict(SPACING)
