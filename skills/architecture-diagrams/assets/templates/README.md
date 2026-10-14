# Model templates

One minimal, valid model per diagram type, using the neutral online-shop scenario. Start from the template of the chosen type (copy `assets/templates/<code>.json`; `atlas init` currently takes a layout-template name, not a type code), replace the content, render, check.

Every file here renders with `atlas render` with **0 errors and 0 warnings**, and `tools/build_samples.py` renders each one into the type's sample SVG (`content/public/samples/`). Labels are inline English text; for bilingual output move them into `labels.<lang>.json` as in `examples/`.

"Fidelity" says how well the current renderer (main, W1) lays the type out:

- **ok** — layout matches what the type page describes.
- **approx.** — renders and checks cleanly, but part of what the page describes is not drawn or is laid out by the generic grid placer. Hand-check before delivering.
- **table only** — renders as a table; the page's companion diagram cannot be combined with it yet.

Node widths are set with `size_hint` so that every template fits the 1120 px document width (a warning means a row is too wide: lower the width or `layout.columns`).

| Type | Layout template | Fidelity | Notes |
| --- | --- | --- | --- |
| A1 capability map | layered | approx. | Level-1 groups inside bands and heat legend are not drawn; bands and Level-2 boxes are. |
| A2 value stream | tree | approx. | One row of four stages; capabilities cross-mapped to a stage go in its `tags`, not beneath it. |
| A3 business context | nested | ok | |
| A4 scenario matrix | grid_table | approx. | Plain table; release tags and significance flags are text, not chips. |
| A5 BPMN process | lanes | approx. | Lanes stack; nodes are not aligned in time across lanes; pools and `message` edges untested. |
| A6 journey map | grid_table | approx. | Table only; the emotion line is not drawn. |
| A7 conceptual architecture | layered | approx. | Bands inside a boundary work; equal-size columns per band are grid-placed. |
| A8 target roadmap | tree | approx. | Linear chain only; work packages do not hang between states. |
| A9 lean value stream | tree | approx. | Row of steps and queues; data boxes and the timeline row are not drawn. |
| B1 use case diagram | nested | approx. | No UML actor figures, ellipses or include/extend markers; the boundary group is always laid out first. |
| B2 user story map | grid_table | table only | Activities as columns and release slices as rows; no task cards or slice bands. |
| B3 feature tree | tree | ok | Functional decomposition, ranked by edges; no variability markers or constraints. |
| B4 scope diagram | nested | ok | Three boundary regions side by side. |
| C1 application landscape | layered | ok | Used as the `shop-landscape` example. |
| C2 system context | nested | ok | Used as the `shop-context` example. |
| C3 container diagram | nested | ok | |
| C4 component diagram | nested | ok | |
| C5 logical architecture | layered | ok | Frames as bands inside a boundary; |
| C6 integration interface | grid_table | table only | `grid_table` accepts tables only; the companion interface map needs a second view. |
| C7 bounded-context map | nested | approx. | Contexts and role chips work; edge direction between boundaries needs a visual check. |
| C8 layered architecture | layered | ok | |
| D1 entity-relationship | er | ok | Used as the `shop-er` example. Keep to one row of entities, see renderer gaps. |
| D2 data flow diagram | nested | ok | Node kinds `process`/`dataset`/`job` used by some type pages are not in the schema: use `component`/`store`. |
| D3 data lineage and ownership | layered | approx. | Owner in `sub`, classification in `tags` work; flow across layers is vertical only. |
| E1 sequence diagram | sequence | ok | Used as the `shop-sequence` example. |
| E2 activity flowchart | lanes | approx. | Partitions as lanes; no fork/join bars, no top-to-bottom flow. |
| E3 state machine | statechart | approx. | Grid placement in node order; order the nodes so that transitions are neighbours. |
| E4 swimlane | lanes | approx. | Same limits as A5. |
| F1 authentication flow | sequence | ok | `alt` frame supported. |
| F2 threat model data flow | nested | ok | Used as the `shop-trust-boundary` example. |
| F3 access control model | grid_table | ok | Matrix as table. |
| G1 deployment diagram | nested | ok | |
| G2 cloud infrastructure | layered | ok | |
| G3 network topology | nested | ok | |
| G4 delivery pipeline | tree | approx. | Ranked by edges (the registry hangs off the build); controllers as `lane` groups are not combined with `tree`. |
| H1 RACI matrix | grid_table | ok | The table `title` carries the R/A/C/I legend. |
| H2 observability view | layered | ok | Layers stack top to bottom; edges between layers only. |
| H3 stakeholder map | grid_table | approx. | Two tables; a true 2×2 quadrant is a plain table. |
| I1 four plus one | layered | approx. | An overview index of views and scenarios, not a replacement for the views. |
| I2 ArchiMate layered view | layered | approx. | No ArchiMate glyphs or metamodel validation; relationship types are edge labels. |
