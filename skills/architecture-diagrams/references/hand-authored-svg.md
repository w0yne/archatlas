# Hand-authored SVG

A hand-authored SVG is a first-class path, next to the auto-layout renderer. You place every
shape yourself, use the same visual tokens, and then run the same checker. Paths are relative
to the skill folder.

## When to choose it

- The auto layout distorts the composition the question needs: a figure that should read
  left to right comes out tall and narrow, related parts drift apart, or a slide or page has a
  fixed aspect ratio.
- The arrangement is specific to this diagram (a mirrored before/after, a hub in the centre, a
  hand-placed map) and no layout template expresses it.
- A small figure is quicker to place by hand than to steer with hints and waypoints.
- The renderer cannot run here (missing dependency, no install allowed). The checker needs the
  same dependencies, so report that automatic checks did not run.

Otherwise prefer the renderer: it measures text, routes connectors and writes the annotations
for you. Do not switch paths to chase cosmetic improvements once a rendered result answers the
question. Brief, type choice and text wireframe (Steps 1–3) apply unchanged on both paths.

## Apply the default style

Authority for the tokens: `scripts/lib/archatlas/render/theme.py` in a release bundle, or
`docs/STYLE.md` and `src/archatlas/render/theme.py` in a checkout. Summary (SVG user units):

| Role | Fill | Border | Use |
|---|---|---|---|
| primary | `#1767B5` | `#03172E` | the one focus element when the view has a single subject; white text |
| peer | `#D8E8FF` | `#3D6FB2` | ordinary elements in scope |
| external | `#EDEDED` | `#666A73` | outside parties |
| shared | `#DCF2DC` | `#397645` | shared services |
| planned | `#EBDDF9` | `#7951A5` | proposed elements |
| highlight | `#FFF1C9` | `#936A16` | a legend-explained marker or callout, not a second focus |

- Zones (body / header band / border): app `#F3F8FF`/`#D8E8FF`/`#3D6FB2`, tech
  `#F0F9F0`/`#DCF2DC`/`#397645`, data `#F8F3FD`/`#EBDDF9`/`#7951A5`, business
  `#FFFBEB`/`#FFF1C9`/`#936A16`, security `#FFF4F1`/`#FFE1DC`/`#B34232`, neutral
  `#F7F7F7`/`#EDEDED`/`#666A73`. Zone radius 10, stroke 1.6, padding 24, header band at least 52.
- Cards: radius 8, stroke 1.8 (2.4 for primary). Chips: pills of radius 10, padding 9, gap 6.
  Connectors: stroke 1.8, `#4B5563` (primary flow `#2563EB`); arrowheads and dashes follow the
  notation.
- Text: `#1F2937`, secondary `#4B5563`, canvas white. Title 28 bold; element name and zone title
  16 bold; sub-labels and connector labels 12; chips and legend 11. Contrast at least 4.5:1 for
  ordinary text and 3:1 for meaningful strokes.
- Formal symbols (actors, use-case ellipses, BPMN events and gateways, state initial/final) keep
  their standard geometry. Explain every colour, line style and badge in one legend.

## Write it so the checker can read it

Static SVG only: live `<text>`, a non-empty `<title>` and `<desc>`, a positive `viewBox`,
attributes rather than `style` or `transform`, local `<marker>` definitions, and no scripts,
images, `<use>`, `<style>` or external references. Annotate the parts the checker measures:

| Element | Annotation |
|---|---|
| root `<svg>` | `data-archatlas="0.1"` |
| background `<rect>` | `data-role="canvas"` |
| element box (`rect`, `ellipse`, `path`) | `data-role="node"`, `data-id` (the model's node id), `data-kind`, `data-parent` (zone id) |
| zone box | `data-role="group"`, `data-id`, optional `data-parent`; its header band `data-role="header-band" data-parent="<zone id>"` |
| text | `data-owner` (the box it belongs to); `data-role="name"` or `"sub"` for element text |
| connector | a `<polyline>` with `points`, `data-role="edge"`, `data-id`, `data-from`, `data-to` |
| legend entry N | caption `<text data-role="legend" data-id="legend-N">` plus a swatch painted exactly like what it explains: a box `data-role="legend-swatch" data-id="__legend-swatch-N"`; a zone `data-role="legend-zone"` with that `data-id` and its own header band; a line `<polyline data-role="edge" data-kind="legend" data-id="legend-line-N">` |

Save the figure in the output folder under its stable name, keep the model JSON beside it when
you wrote one, and run:

```sh
scripts/atlas check out/figure.svg --model out/model.json --report out/figure.findings.json
```

Omit `--model` when there is no model. `--browser` refuses hand-authored SVG; it needs a generated one.

## What the check can and cannot judge

- **Checks:** unsafe or external content; title, description and viewBox; text and shapes
  inside the canvas; text contrast; text overlapping other text. With the annotations above it
  also checks measured text fit inside its owner box, membership in the declared zone, text over
  unrelated boxes, connectors running through unrelated boxes, markers, the crossing count
  (a warning above two), legend coverage of every visible encoding, and (with `--model`) that
  node and edge ids and endpoints match the model.
- **Without the annotations** it reports `unsupported-geometry`: the ownership checks did not
  run. Report that; it is not a pass.
- **Cannot judge:** whether the type, boundaries and relationships are true; notation
  conformance; whether a connector visually ends on the right element (it checks the polyline
  you wrote, not your intent); whether the remaining crossings and routes are acceptable to the
  reader; glyph display; overall composition. Those need the semantic and visual review in
  `references/review.md`, with the same stop rule as rendered figures.
