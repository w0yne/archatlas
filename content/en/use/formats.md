---
title: Formats and troubleshooting
---
# Formats and troubleshooting

## Initial format

The initial implementation target is **SVG with editable text**, accompanied by model JSON. Keep both: the model carries semantic relationships, while SVG is the rendered result. HTML is a viewing wrapper.

**Not yet promised:** draw.io export, editable PowerPoint export, lossless import, or round-trip editing. Embedding one SVG image in a slide is not equivalent to native editable shapes.

## Rendering and checks

A complete release provides local rendering/checking helpers. Review its command help and dependency instructions. The workflow is model → layout → SVG → structure/geometry checks → visual review.

## Missing fonts or Chinese glyphs

Check the actual font selected by the renderer and glyph coverage. An estimator or fallback font must be reported. Do not fix clipping by shrinking all labels; adjust wrapping and layout, then render again.

## No browser or no image input

Text and geometry checks can still run. Generate a preview when supported, and hand it to a human or image-capable reviewer. Report **visual review pending**, never visual pass based solely on a successful command.

## A diagram is too dense

Return to the reader's question. Collapse non-focus detail or separate concerns into different views. Keep the full-size image available rather than making labels unreadable on a small screen.
