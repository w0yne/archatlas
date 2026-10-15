# Model templates

One minimal, valid model per diagram type, using the neutral online-shop scenario. Start from the template of the chosen type with `scripts/atlas init <code> -o out/model.json`, replace the content, render, check. The shipped templates and the installed CLI define the available inputs; `references/rendering.md` lists the supported fields and limits. The notes below describe layout fidelity, not missing schema features.

Every file here renders with `atlas render` with **0 errors and 0 warnings**, and `tools/build_samples.py` renders each one into the type's sample SVG (`content/public/samples/`). Labels are inline English text. For a Chinese sample, `zh/<code>.json` maps each English label text to its Chinese rendering (the loader looks the literal text up in the labels file); `build_samples.py` renders `<code>.zh.svg` when that file exists (see the `zh/` folder). `examples/` keeps its own full worked examples and is not used for the samples.

"Fidelity" says how well the shipped renderer lays the type out:

- **ok** — layout matches what the type page describes.
- **approx.** — renders and checks cleanly, but part of what the page describes is not drawn or is laid out by the generic grid placer. Hand-check before delivering.
- **table only** — the template is a table; `grid_table` can place a small diagram beside it when the page's companion view needs one.

The common types (A1, A5, C1, C2, C3, C5, C8, D1, E1, E3, E4, F1, F3, G1, G2) are written as realistic samples in the default visual style: zones with header bands, one `primary` focus where the view has a single subject, chips, step badges only where order matters, and a legend, staying under the checker's 12-node warning. The others stay minimal.

Node widths are set with `size_hint` so that every template fits the 1120 px document width (a warning means a row is too wide: lower the width or `layout.columns`).

| Type | Layout template | Fidelity | Notes |
| --- | --- | --- | --- |
| A1 capability map | layered | ok | Tier zones with Level-1 groups and Level-2 tiles; the maturity lens is colour plus a chip and its legend. |
| A2 value stream | tree | approx. | One row of four stages; capabilities cross-mapped to a stage go in its `tags`, not beneath it. |
| A3 business context | nested | ok | |
| A4 scenario matrix | grid_table | approx. | Plain table; release tags and significance flags are text, not chips. |
| A5 BPMN process | lanes | approx. | Vertical lanes (`direction: TB`) in a shop pool plus a black-box customer pool; message flows are routed automatically and may wrap around lanes. |
| A6 journey map | grid_table | approx. | Table only; the emotion line is not drawn. |
| A7 conceptual architecture | layered | approx. | Bands inside a boundary work; equal-size columns per band are grid-placed. |
| A8 target roadmap | tree | approx. | Linear chain only; work packages do not hang between states. |
| A9 lean value stream | tree | approx. | Row of steps and queues; data boxes and the timeline row are not drawn. |
| B1 use case diagram | nested | approx. | Actors draw as stick figures and use cases as ellipses; include/extend have no dedicated marker (label a dashed dependency edge); the boundary group is always laid out first. |
| B2 user story map | grid_table | table only | Activities as columns and release slices as rows; no task cards or slice bands. |
| B3 feature tree | tree | ok | Functional decomposition, ranked by edges; no variability markers or constraints. |
| B4 scope diagram | nested | ok | Three boundary regions side by side. |
| C1 application landscape | layered | ok | Used as the `shop-landscape` example. |
| C2 system context | statechart | ok | Ranked left to right inside a boundary zone; `examples/shop-context` keeps its own model. |
| C3 container diagram | statechart | ok | Zones ranked top to bottom by the request path; one `primary` focus and chips. |
| C4 component diagram | nested | ok | |
| C5 logical architecture | statechart | ok | Responsibility zones ranked by dependency; the block table is not drawn. |
| C6 integration interface | grid_table | table only | Interface table; add the interface map as nodes and edges beside it, or as a second view. |
| C7 bounded-context map | nested | approx. | Contexts and role chips work; edge direction between boundaries needs a visual check. |
| C8 layered architecture | layered | ok | |
| D1 entity-relationship | er | ok | Two rows of four entities; place related entities side by side or one above the other. |
| D2 data flow diagram | nested | ok | Processes as `component` (or `process`), data stores as `store`; kinds `process`/`dataset`/`job` draw as cards, not DFD symbols. |
| D3 data lineage and ownership | layered | approx. | Owner in `sub`, classification in `tags` work; flow across layers is vertical only. |
| E1 sequence diagram | sequence | ok | Used as the `shop-sequence` example. |
| E2 activity flowchart | lanes | approx. | Partitions as lanes; no fork/join bars, no top-to-bottom flow. |
| E3 state machine | statechart | ok | Ranked top to bottom by transitions; chips carry state meaning. |
| E4 swimlane | lanes | ok | Vertical lanes (`direction: TB`) with numbered steps. |
| F1 authentication flow | sequence | ok | `alt` frame with guarded operands. |
| F2 threat model data flow | nested | ok | Used as the `shop-trust-boundary` example. |
| F3 access control model | grid_table | ok | Matrix as table. |
| G1 deployment diagram | statechart | ok | Network segments as zones, data services as a separate zone. |
| G2 cloud infrastructure | statechart | ok | Edge, region, zones and managed services; zones sit side by side when their ranks match. |
| G3 network topology | nested | ok | |
| G4 delivery pipeline | tree | approx. | Ranked by edges (the registry hangs off the build); controllers as `lane` groups are not combined with `tree`. |
| H1 RACI matrix | grid_table | ok | The table `title` carries the R/A/C/I legend. |
| H2 observability view | layered | ok | Layers stack top to bottom; edges between layers only. |
| H3 stakeholder map | grid_table | approx. | Two tables; a true 2×2 quadrant is a plain table. |
| I1 four plus one | layered | approx. | An overview index of views and scenarios, not a replacement for the views. |
| I2 ArchiMate layered view | layered | approx. | No ArchiMate glyphs or metamodel validation; relationship types are edge labels. |
