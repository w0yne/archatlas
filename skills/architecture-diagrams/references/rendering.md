# Rendering: model, CLI and fixing loop

SVG is the primary output; model JSON is the editable source. Schema version is
`archatlas: "0.1"`. In a checkout, the authority is
`src/archatlas/model/schema.json`; a packed skill includes it under
`scripts/lib/archatlas/model/schema.json`. Nodes have no absolute-position fields;
edge `waypoints` are the explicit manual routing override.

## 1. Install and invoke

From a reviewed repository checkout, create and activate a virtual environment,
then run `python -m pip install -e .`. Alternatively, `make setup` creates `.venv`,
installs development dependencies and installs the site's Node dependencies;
activate `.venv` afterwards. Neither route needs a published `archatlas` package.
Do not install an unrelated package with that name from PyPI.

Optional extras, from the checkout root:

```sh
python -m pip install -e '.[preview,browser]'
python -m playwright install chromium
```

CairoSVG supplies PNG/contact-sheet rendering and also needs the platform's Cairo
library. Playwright needs Chromium and its platform libraries; follow Playwright's
platform dependency instructions if Chromium cannot launch.

The installed command is `atlas`. From the skill folder, `scripts/atlas` is the
same CLI: it prefers a release bundle's `scripts/lib`, otherwise the installed
library. In an unpacked bundle (or an installed skill folder), set up a virtual environment
in your working folder and install the skill's own core requirements:

```sh
python3 -m venv .atlas-venv
.atlas-venv/bin/python -m pip install -r <skill>/scripts/requirements.txt
.atlas-venv/bin/python <skill>/scripts/atlas fonts doctor
```

Then run every command as `.atlas-venv/bin/python <skill>/scripts/atlas …`. If
`python3 -m venv` or pip is unavailable, or installing is not permitted, do not
install into the system Python. **Required dependency:** the renderer needs
`jsonschema` and its dependencies for model validation. If they or the renderer
library are missing, commands fail with exit 2 and an install hint; automatic
rendering/checks did not run. Keep the model and use the hand-written SVG fallback
in §6 if needed, explicitly reporting that it is not validated renderer output.
**Measurement fallback:** only when required dependencies are available, missing
Pillow/fontTools or fonts/glyphs can produce conservative estimates with warnings
and `measured_with: estimate`; report the actual mode returned by the tool.
Optional preview/browser dependencies are CairoSVG (plus the platform Cairo
library) and Playwright (plus Chromium). Missing optional tools leave SVG work
available but their requested preview/browser command returns 2; contact sheets
also require Pillow. Install extras in the bundle's virtual environment
(`python -m pip install CairoSVG playwright`, then
`python -m playwright install chromium`) or use the reviewed checkout extras above.
A copied checkout skill folder alone does not include `scripts/lib`.

## 2. Working commands

After checkout installation, run from the repository root:

```sh
atlas init C2 -o model.json
atlas render model.json -o out/ --lang en --profile doc
atlas check out/diagram.svg --model model.json --lang en --report out/findings.json
atlas check out/diagram.svg --model model.json --lang en --browser --fail-on warning --report out/browser.findings.json
atlas preview out/diagram.svg -o out/preview.png --scale 1
atlas sheet out/*.svg -o out/sheet.jpg
atlas fonts doctor
```

`init` accepts a shipped type code (case-insensitive) or a layout family. It finds
assets in the checkout/copied skill, or in `--templates DIR`. Unknown/unavailable
codes fail; it does not invent a type-to-template mapping. The output materialises
the template's default-language labels, rather than copying JSON bytes unchanged.
For bilingual work, keep translation keys and sidecar label files in your source.

| Command | Options and output |
|---|---|
| `init TYPE` | `-o model.json` (default); optional `--templates DIR` |
| `render MODEL` | Required `-o`; optional `--lang`, `--profile slide\|doc`, `--namespace`, `--fail-on error\|warning` |
| `check SVG` | Required `--report FILE`; optional `--model`, `--lang`, `--browser`, `--fail-on error\|warning` |
| `preview SVG` | Required `-o FILE`; `--scale` is greater than 0 and at most 4; needs CairoSVG |
| `sheet SVG...` | Required `-o FILE`; downscaled contact sheet, at most 1600px per dimension; needs CairoSVG |
| `fonts doctor` | JSON with selected font families/files, CJK probe coverage, warnings and measurement mode |

`render -o out/` writes `out/diagram.svg` and `out/diagram.findings.json`.
`render -o out/context.svg` writes that file and `out/context.findings.json`.
Render writes the SVG even when checks find defects: inspect its return code and
report before delivery. `check --lang` validates the requested language against
the SVG and uses it to load the supplied model; it does not translate an SVG.
Re-render with `--lang zh` to change language.

For render/check: **0** means no finding reaches the chosen failure threshold;
warnings may still exist at the default `error` threshold. **1** means findings
at/above that threshold. **2** means tool/input/dependency failure. Other commands
return 0 on success and 2 on tool/input failure. `--embed-font-subset` is accepted
by render but is **not implemented** and returns 2. Browser checking is implemented;
a missing browser/dependency returns 2 and records `browser.status: tool-error`.

## 3. Model fields

Required: `archatlas`, `meta` with `type`/`title`, and `layout` with `template`.
Use `init` for a complete starting model. The following is a summary, not a
replacement for schema validation.

- **layout:** template, direction (`LR|TB`), columns (maximum 1–8), profile,
  spacing overrides. `slide`/`slide-16x9` keeps 1440×810; overflow is reported.
  `doc`/`doc-1120xN` prefers 1120px width and grows as needed; the default wide-view
  warning limit is 1.5 times the preferred width. It does not paginate or shrink text.
- **nodes:** id, kind, label; optional sub (keep brief), parent group, tags (small
  text labels), chips (short labels, each a string or `{label, style}`), badge (step or
  reference number 1–999, or 1–4 characters), shape (`card|database|document|queue|callout`),
  style, size_hint, evidence, attributes (ER field strings), rank (minimum flow rank,
  integer 0–100). Styles: primary/peer/external/shared/planned/highlight (`highlight` is the
  one warm emphasis colour for the subject of the figure).
  Kinds: person, system, container, component, store, queue, external, actor,
  lifeline, state, entity, task, event, gateway, band, initial, final, note,
  process, dataset, job, pipeline, use_case, document, callout. `store` draws a cylinder,
  `queue` a queue, `document` a folded card and `callout` a note card by default.
- **glyphs:** actor is a stick figure with its label below; person stays a card.
  use_case is an ellipse. An event may set event_type=start/end (thin/thick BPMN
  border); initial/final are UML state symbols. Descriptive kinds such as dataset
  and pipeline remain cards, not a promise of complete formal notation. Formal symbols
  (actor, event, gateway, use_case, initial, final) keep their shape and take no chips or badge.
- **groups:** id, title, kind (`boundary|layer|pool|lane|frame`), optional parent,
  style, dashed, tint (`app|tech|data|biz|security|neutral`, a colour role) and band
  (header band, default true). Explicit pool models in lanes reject sequence calls across pool
  boundaries and messages within one pool; messages require a dashed directed arrow.
- **edges:** from/to; optional id, label, kind (`call|data|async|message|dependency|assoc`),
  dir (`->|<->|--`), step, from_port/to_port (`n|e|s|w|auto`), style, dashed,
  evidence, waypoints (`[[x,y],…]`), cardinality (`{from,to}` strings such as
  `1..1`/`0..*`). Crow's-foot markers are not implemented.
- **evidence:** status (`verified|inferred|doc-only|conflict`), optional refs with
  required path and optional url/ref/line_start/line_end. Non-verified edges are
  dashed unless explicitly overridden.
- **tables:** id, optional title, non-empty columns array, rows of matching length;
  column headings may be empty strings. grid_table can place tables beside a
  small nodes/edges/groups diagram. Merged cells are not supported.
- **sequence:** frames (`id`, `from_step`, `to_step`, `operator` of `loop|alt|opt|par|break|critical|seq|strict`,
  `guard`, optional `label`) and activations (`node,from_step,to_step`). `alt` and `par` frames list
  `operands` (`guard,from_step,to_step`) that partition the frame's steps; each operand is drawn as a
  region with its own guard, split by a dashed separator. Frames must nest or be disjoint.
- **meta:** type, title, optional subtitle (one short line of context, not the diagram type), lang,
  audience, state, legend.
- **allow:** element/rule/reason explanations. These are retained for review;
  they do not suppress errors or change the CLI failure threshold.

IDs match `^[A-Za-z][A-Za-z0-9_-]*$` and are unique across nodes, groups, tables,
frames and explicit/generated edge IDs. An omitted edge id becomes `edge-1`, etc.

### Visual components

The default style is one family: tinted zones with header bands for boundaries and layers, solid
blue for the subject's peers, one warm highlight for the subject, green for shared, gray for
external, purple for planned. Components are visual, not facts: explain every colour, chip colour
and badge in the legend (`meta.legend`), and see "Visual hierarchy" in `principles.md`.

Layout hints that follow from the engine: `nested` and `layered` place children in declaration
order on a grid (`layout.columns`), so order siblings by flow; `statechart` ranks nodes by their
edges inside each group, which suits flow diagrams with zones (use `direction` `LR` or `TB`);
`lanes` with `direction: TB` draws vertical swimlanes. Edge labels widen the gaps between ranks:
put a protocol or role in a chip and keep labels for the exchange itself. The checker warns above
12 nodes in one view; richness comes from zones, chips and badges rather than more boxes.

### Meaningful legends and languages

`meta.legend` holds authored entries: label plus optional style, dashed, kind,
dir and symbol (`line|box`). Set `meta.legend_mode: "replace"` to use only those
entries. Default `auto` supplements them with semantic defaults for the diagram.

`meta.legend_labels` can map `edges`, `styles` and `groups` keys to reader-facing
text. For example, under meta:

```json
{"legend_labels":{"edges":{"call":"@legend.request","reply":"@legend.reply"},"styles":{"primary":"@legend.shop"},"groups":{"boundary":"@legend.trust"}}}
```

`reply` overrides a dashed, verified sequence-call legend; it is not an edge kind.
Use business meanings, not style identifiers. Default meanings have EN/ZH forms.
All authored legend labels use the same localisation as node labels: a matching
key in `labels.<lang>.json` beside the model resolves to text; `@key` fails when
missing; otherwise a string is literal. Inline top-level `labels` is allowed,
and the external file wins. Titles, subtitles, tags, attributes and table text
also resolve this way. `--lang` does not translate literal English automatically.
IDs/topology remain the same; each language is measured and laid out afresh.

## 4. Layout, fonts and routing

| Family | Implemented layout |
|---|---|
| nested | Containment groups with headers and connectors |
| layered | Stacked bands with child rows |
| lanes | Shared dependency ranks across lanes, including nested groups |
| sequence | Lifelines, ordered steps, range frames, activations |
| grid_table | Tables, optionally beside a small diagram |
| er | Entity cards and textual cardinality endpoints |
| statechart | Ranked states/branches; feedback edges retained for routing |
| tree | Longest-path ranks; cycles rejected |

Flow ranking uses deterministic feedback-edge removal and barycentre ordering;
rank hints are minima, not fixed coordinates. Layout/routing is heuristic, not a
minimum-crossing guarantee. Automatic routes avoid unrelated shapes where possible,
penalise crossings/shared segments/reused ports and remove retraced spurs. Manual
waypoints preserve author coordinates and can still produce findings.

`layout.spacing` overrides theme tokens: node_gap, rank_gap, boundary_gap,
gap_ratio, group_padding, group_header, document_width, wide_view_ratio,
label_width, label_clearance. Measured labels and busy boundaries can require more
space than a gap minimum. Themes are neutral, print and dark.

Pillow/fontTools measure installed fonts and CJK/Latin fallback runs. Missing
fonts or glyphs trigger a conservative estimate, extra padding and warnings;
reports identify `measured_with: estimate`. `fonts doctor` checks a CJK probe,
not all Unicode. SVG keeps live text, so matching appearance needs matching fonts.
Label backgrounds use the same text box/anchor as the label. SVG is deterministic
for the same inputs, fonts and renderer, with no scripts/foreignObject/external
resources. For repeated inline copies of one diagram, use distinct `--namespace` values.

## 5. Check, fix and review

Reports contain counts plus `findings[]` with id/severity/rule/elements/boxes/message.
`check --model` validates the model and compares node/edge IDs and endpoints;
it is not a semantic proof or a full text-by-text comparison against the model.
Static checks cover text fit, owner/group membership, label backgrounds, overlaps,
ports, lines through unrelated boxes/labels, marker references, contrast, canvas
bounds, crossing counts and some label hygiene. Boundary violations are errors.

`--browser` adds actual Chromium text/shape bounds after fonts are ready, with
network access blocked. It does not prove glyph identity, semantic correctness
or visual quality. Formal notation completeness, unexplained meanings, peer-kind
consistency and other human judgments still need review.

Fix errors in the model, re-render, and run check again on the new SVG with the
same language. Fix warnings or record element-specific reasons; a reason does not
turn an exit 1 into 0. After automated checks, make previews and follow `review.md`.
The CLI's `visual_review: pending` never means that somebody looked at the image.

## 6. Fallback

If the renderer cannot run, report the missing dependency and keep the model.
A hand-written SVG is a fallback, not a validated renderer output. Use live text,
explicit background, title/description, local markers and conservative text space;
then measure and inspect it with available tools. The static checker requires
Archatlas ownership metadata and refuses to claim complete checks for arbitrary
SVG/CSS/transforms. If no rasteriser is available, say “preview not produced” and
“visual review pending”.
