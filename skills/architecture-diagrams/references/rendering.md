# Rendering: model JSON, layout templates, CLI, checks

SVG is the primary format. You write a **model** (what the diagram means); the renderer lays it out and draws it; the checker finds defects. Never place nodes by absolute coordinates unless a model field explicitly allows waypoints.

> Status: the model schema below is frozen at `archatlas: "0.1"` (file `src/archatlas/model/schema.json`; the schema is the authority — validate with it, do not trust this summary over it). If `scripts/atlas --help` disagrees with this page, the real output wins.

## 1. Workflow
```
scripts/atlas init <code> -o model.json        # copies assets/templates/<code>.json (e.g. C2, E1)
# edit model.json (+ optional labels.en.json / labels.zh.json beside it)
scripts/atlas render model.json -o out/         # writes out/diagram.svg and out/diagram.findings.json
scripts/atlas check  out/diagram.svg --model model.json --report out/findings.json
scripts/atlas preview out/diagram.svg -o out/preview.png     # needs CairoSVG (archatlas[preview])
scripts/atlas sheet  out/*.svg -o out/sheet.jpg              # contact sheet; needs CairoSVG too
scripts/atlas fonts doctor                                   # usable fonts and CJK glyph coverage
```
`render` runs the checks as well and prints a one-line summary (`errors`, `warnings`, `visual_review: pending`). `--fail-on error|warning` sets the threshold for exit code 1. Exit codes: 0 clean; 1 findings at or above `--fail-on` (default `error`); 2 tool error. If an older renderer rejects a type code in `init`, copy `assets/templates/<code>.json` instead.
**Unavailable options:** `check --browser` and `render --embed-font-subset` are not implemented and exit with code 2; do not rely on them.

## 2. Model (version 0.1)
Required top level: `archatlas: "0.1"`, `meta` (`type`, `title`), `layout` (`template`).

```json
{
  "archatlas": "0.1",
  "meta":   {"type": "C2", "title": "Shop context", "audience": "business and IT", "state": "as-is", "lang": "en",
             "legend": [{"label": "External system", "style": "external"}]},
  "layout": {"template": "nested", "direction": "TB", "profile": "slide"},
  "groups": [{"id": "shopb", "title": "Shop", "kind": "boundary"}],
  "nodes":  [{"id": "buyer", "kind": "person", "label": "Buyer"},
             {"id": "shop",  "kind": "system", "label": "Shop", "sub": "web store", "parent": "shopb", "style": "primary"},
             {"id": "pay",   "kind": "external", "label": "Payment provider", "style": "external"}],
  "edges":  [{"from": "buyer", "to": "shop", "label": "Places order", "dir": "->"},
             {"from": "shop",  "to": "pay",  "label": "Charges card", "evidence": {"status": "inferred"}}]
}
```
- **layout.template** (set it explicitly; there is no inference): `nested`, `layered`, `sequence`, `lanes`, `grid_table`, `er`, `statechart`, `tree`. Optional `direction` (`LR`|`TB`), `columns` (1–8), `profile` (`slide` = 1440×810, `doc` = 1120 wide, variable height).
- **nodes**: `id`, `kind`, `label`; optional `sub` (one short line), `parent` (a group id), `tags[]` (small chips), `style` (`primary|peer|external|shared|planned`), `size_hint {width,height}`, `evidence`, `attributes[]` (ER field strings). Kinds: person, system, container, component, store, queue, external, actor, lifeline, state, entity, task, event, gateway, band, initial, final, note.
- **groups**: `id`, `title`, `kind` (`boundary|layer|pool|lane|frame`); optional `parent`, `style`, `dashed` (use dashed frames for trust boundaries).
- **edges**: `from`, `to`; optional `id`, `label`, `kind` (`call|data|async|message|dependency|assoc`), `dir` (`->`, `<->`, `--`), `step` (integer; numbers key steps, and orders sequence messages), `from_port`/`to_port` (`n|e|s|w|auto`), `style`, `dashed`, `evidence`, `waypoints` (`[[x,y],…]` manual override), `cardinality {from,to}` (ER).
- **evidence**: `status` (`verified|inferred|doc-only|conflict`), optional `refs [{path,url,ref,line_start,line_end}]`. Non-verified edges render dashed unless `dashed` says otherwise.
- **tables**: `[{id,title,columns[],rows[[]]}]` — every row has as many cells as columns (matrices, RACI, interface tables).
- **sequence extras**: `frames [{id,label,from_step,to_step}]` (alt/opt/loop boxes), `activations [{node,from_step,to_step}]`.
- **allow**: `[{element, rule, reason}]` — element-specific explanations for an intentional finding. Never allow a whole rule.
- IDs (nodes and groups share one namespace) match `^[A-Za-z][A-Za-z0-9_-]*$`. Layout is derived from groups, parents, edges and steps; you describe structure, not positions.

### Labels and languages
Labels are strings. A string equal to a key in `labels.<lang>.json` (next to the model) is replaced by that translation; otherwise it is literal. `@key` forces a lookup and fails if missing. An inline top-level `labels` object may supply translations; the external language file wins. Titles, group titles, edge labels, tags, attributes and table cells all use this. IDs and topology never change between languages; text width may, so the renderer re-lays-out per language and the checks run per language: `atlas render model.json --lang zh -o out/zh/`.

## 3. Choosing a template
| Template | Use for |
|---|---|
| `layered` | landscapes, logical and layered architecture, capability maps, cloud reference views (bands × columns) |
| `nested` | context / container / component, deployment, network, trust-boundary frames (containment tree plus connectors between leaves) |
| `lanes` | swimlane / BPMN / activity (pools and lanes via `groups`, nodes via `parent`, message flows between pools) |
| `sequence` | sequence and authentication/authorization flows (lifelines are nodes of kind `lifeline`; messages are edges with `step`) |
| `grid_table` | matrices and tables (RACI, RBAC, scenario map, interface table) |
| `er` | entity-relationship, lineage (nodes of kind `entity` with `attributes`; edges with `cardinality`) |
| `statechart` | state machines (`state`, `initial`, `final`; edges labelled with events) |
| `tree` | feature trees, value-stream and roadmap rows, delivery pipelines |
The type reference (`references/types/<code>-<slug>.md`, section "Template") names the template and the starting model for each type. Unsupported features are reported by the renderer; do not fake them with absolute shapes.

## 4. What the renderer guarantees (so you do not have to)
- Text is measured with an installed font (CJK and Latin runs separately), wrapped by measured width with CJK line-break rules; if no font is found it falls back to a conservative estimate, adds padding and records `measured_with: estimate` — tell the user.
- Label backgrounds are derived from the same measured lines and anchor as their text.
- Connectors leave from box sides (ports) and are routed straight → one elbow → corridor → around obstacles, avoiding unrelated boxes and labels; group-level connections end on the group border.
- One arrow-marker set per SVG with a unique prefix; marker colour follows the edge style; double-headed arrows come from `dir: "<->"`.
- A legend is generated from the styles actually used; keep `meta.legend` for custom entries.
- Output is deterministic (stable ids, sorted serialisation, no timestamps), contains live text, `<title>`/`<desc>`, no scripts, no `foreignObject`, no external references.
- Type scale tokens and spacing come from the theme (`neutral`, `print`, `dark`); default background is explicit.

## 5. Checks (`atlas check`)
Findings file: `id, severity (error|warning|info), rule, element ids, boxes, message`. Rules include:
- **structure** — schema valid, unique ids, edge endpoints exist, markers resolve, no script / `foreignObject` / external URL, non-empty title and description;
- **text-fit** — measured text inside its owner's padded interior; label background matches its text;
- **overlap** — text–text, text–shape (non-owner), node–node unless contained;
- **arrow** — segment through an unrelated box, arrowhead not on its port, arrow crossing a group border it should not, edge crossings (warning);
- **contrast** — text ≥4.5:1 (large text ≥3:1), strokes ≥3:1;
- **hygiene** (warnings) — bullet characters or sentences in labels (`label-hygiene`), status words such as `TBD`, `draft`, `pending`, `v2` (`working-note`), more than 12 nodes per view (`view-density`), elements outside their declared group (`boundary-membership`);
- **planned, not yet checked** — unexplained markers, a subtitle restating the type, sibling-kind mismatch in a row, peers of different size, browser-based text boxes and glyph coverage (`--browser` is unavailable). Check these by eye.
Fix errors; fix or explain warnings. To explain an intentional one, add an `allow` entry for that element with a reason.

## 6. Fallback (no renderer available)
Say so. Deliver the model JSON plus a hand-written SVG and state clearly that the automated checks did not run. For the SVG:
- one `<svg viewBox>` with an explicit white background, `<title>` and `<desc>`; live `<text>` with a font stack including a CJK font; no scripts, no external references;
- one `<defs>` with the arrow markers; unique marker ids; group elements with ids matching the model;
- text sized from the type scale (title 26–28, name 14–16, body 12–13, note 11); estimate width as 1.0 × size per CJK character and 0.55 × size per Latin character, and pad boxes by at least 12 %;
- a white 90 % background rectangle under every connector label, sized to its text at the same anchor;
- measure twice: no text outside its box, no label over a line, no arrow through an unrelated box.

## 7. Local preview and screenshots
Rasterise only for review. Use whatever the host offers (headless browser, `rsvg-convert`, `resvg`); if none is available say "preview not produced" and follow the "cannot read images" path in `review.md`.
