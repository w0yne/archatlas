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
with range frames and activations, simple lane flow, rectangular tables, entity
cards with multiplicity labels, rounded-state transitions and directed trees.
These are diagram layout templates, not complete UML/BPMN/ER conformance tools.
Advanced gateways, fragment operands, inheritance and executable semantics need
a notation-aware author/reviewer. Model IDs and topology are stable across
translations; all label lengths are measured again.

Static QA reports geometry and accessibility checks. It does not claim a visual
review, prove semantics, or support arbitrary hand-edited SVG transforms/CSS.
The optional browser checker and font-subset embedding are not implemented yet;
their CLI switches explicitly return tool error (2). SVG is live text and needs
the fonts reported by `atlas fonts doctor` on the viewing system.

SVG IDs use a deterministic content prefix and separate shape/text/marker
namespaces. Distinct diagrams can be inlined together. If the **same** diagram
is inserted more than once, render each instance with a different `--namespace`.
Explicit font runs preserve CJK fallback in CairoSVG as well as browser viewers.
The `doc` profile grows when content cannot fit 1120px and reports a warning;
`slide` keeps 1440×810 and reports overflow instead of shrinking labels.

`atlas init` currently takes a layout family (for example `nested`), not a
catalogue code. Catalogue aliases and the packaged skill templates are integrated
by the content/package work. Font embedding and browser QA are extension points,
not silent fallback paths. Layout is shared by family-specific methods in one
engine; the exporter-neutral Scene is the stable integration seam.
