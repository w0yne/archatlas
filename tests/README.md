# Renderer verification

Install with `python -m pip install -e '.[test,preview]'`, then run `pytest tests`.
The preview extra is optional for rendering SVG and checking geometry.

`fixtures/` contains six newly authored, generic models. The pipeline test lays
them out with discovered fonts, checks actual emitted SVG geometry and compares
two renders byte for byte. Font tests inspect cmap coverage and exercise CJK and
Latin runs. Install Noto Sans and Noto Sans CJK for reproducible measured CI.

`golden/` deliberately uses `FontMetrics(paths=[])`, which selects the documented
conservative estimator. This makes the serialization/structure baseline stable
across OS font installations. It does **not** establish measured text quality;
the separate real-font pipeline test does that. Every estimated SVG retains its
warning and `measured_with=estimate` metadata.

Update golden files only after inspecting the model/geometry changes:

```python
from pathlib import Path
from archatlas.fonts import FontMetrics
from archatlas.layout import layout
from archatlas.model import load
from archatlas.render import render_svg

for path in sorted(Path("tests/fixtures").glob("*.json")):
    svg = render_svg(layout(load(path), FontMetrics(paths=[])))
    Path("tests/golden", path.stem + ".svg").write_text(svg, encoding="utf-8")
```

Scope: nested/grouped architecture, horizontal band layers, sequence messages
with range frames and activations, globally ranked lane flow, rectangular tables, entity
cards with multiplicity labels, rounded-state transitions and directed trees.
These are diagram layout templates, not complete UML/BPMN/ER conformance tools.
Advanced gateways, fragment operands, inheritance and executable semantics need
a notation-aware author/reviewer. Model IDs and topology are stable across
translations; all label lengths are measured again.

Static QA reports geometry and accessibility checks. It does not claim a visual
review, prove semantics, or support arbitrary hand-edited SVG transforms/CSS.
For actual Chromium geometry, install `archatlas[browser]` and run
`playwright install --with-deps chromium`, then `atlas check diagram.svg --browser
--report findings.json`. Browser checks block network access, await fonts and
measure actual bounds; they still do not claim visual review. Set
`ARCHATLAS_BROWSER_TESTS=1` to enable the real-browser regression test. Missing
dependencies/browser produce tool error (2). Font-subset embedding remains
unimplemented. SVG is live text and needs the fonts reported by `atlas fonts doctor`.

SVG IDs use a deterministic content prefix and separate shape/text/marker
namespaces. Distinct diagrams can be inlined together. If the **same** diagram
is inserted more than once, render each instance with a different `--namespace`.
Explicit font runs preserve CJK fallback in CairoSVG as well as browser viewers.
The `doc` profile grows beyond its preferred width as needed; its warning limit
is controlled by the theme's `wide_view_ratio` (default 1.5 × 1120px). Grid
columns wrap at that limit. `slide` keeps 1440×810 and reports overflow instead
of shrinking labels.

`atlas init C2` resolves shipped type templates by filename/model metadata;
layout families such as `nested` still work. Use `--templates DIR` when assets
are outside the checkout or copied skill. Initialized models contain resolved
default-language labels. `atlas check --lang zh --model diagram.json` checks the
requested locale and rejects a mismatched SVG language.

Schema 0.1 remains compatible and adds:

- `nodes[].rank`: nonnegative minimum flow rank, propagated downstream.
- `process`, `dataset`, `job`, `pipeline`: descriptive node kinds using ordinary
  cards; they do not imply executable BPMN or a new formal notation.
- `grid_table` accepts nodes/edges/groups beside tables; blank column headings
  are allowed.
- `layout.spacing` overrides theme tokens: `node_gap`, `rank_gap`,
  `boundary_gap`, `gap_ratio`, `group_padding`, `group_header`, `document_width`,
  `wide_view_ratio`, `label_width`, `label_clearance`. Gap minima also account for
  measured labels, node proportions and busy boundary crossings.
- `meta.legend[]` may specify `kind`, `dir` and `symbol` (`line`/`box`) as well as
  label/style/dashed. Explicit entries take precedence over automatic entries.

Flow ranks use longest paths after deterministic feedback-edge removal, then
barycentre ordering. Statecharts retain feedback edges for routing; trees reject
cycles. Lane tasks share the global rank axis, including nested groups. Rank
ordering is heuristic, not globally optimal; long-edge crossing minimization and
full UML/BPMN semantics remain out of scope.
