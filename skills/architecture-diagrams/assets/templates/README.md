# Model templates

One minimal, valid model per diagram type, using the neutral online-shop scenario. Start from the template of the chosen type (copy `assets/templates/<code>.json`; `atlas init` currently takes a layout-template name, not a type code), replace the content, render, check.

Every file here renders with `atlas render` with **0 errors**. Labels are inline English text; for bilingual output move them into `labels.<lang>.json` as in `examples/`.

"Fidelity" says how well the current renderer (`w1-renderer` @ `f3864f3`) lays the type out:

- **ok** — layout matches what the type page describes.
- **approx.** — renders and checks cleanly, but part of what the page describes is not drawn or is laid out by the generic grid placer. Hand-check before delivering.
- **table only** — renders as a table; the page's companion diagram cannot be combined with it yet.

Advisory warning `wide-view` = content wider than the 1120 px document width (split the view or reduce columns).

| Type | Layout template | Fidelity | Notes |
| --- | --- | --- | --- |
| A1 capability map | layered | approx. | Level-1 groups inside bands and heat legend are not drawn; bands and Level-2 boxes are. |
| A2 value stream | tree | approx. | One row of stages; cross-mapped capabilities beneath a stage are not ranked. `wide-view` with 5 stages. |
| A3 business context | nested | ok | `label-placement` warning when flows share a side of the subject. |
| A4 scenario matrix | grid_table | approx. | Plain table; release tags and significance flags are text, not chips. |
| A5 BPMN process | lanes | approx. | Lanes stack; nodes are not aligned in time across lanes; pools and `message` edges untested. |
| A6 journey map | grid_table | approx. | Table only; the emotion line is not drawn. |
| A7 conceptual architecture | layered | approx. | Bands inside a boundary work; equal-size columns per band are grid-placed. `wide-view`. |
| A8 target roadmap | tree | approx. | Linear chain only; work packages do not hang between states. `wide-view`. |
| A9 lean value stream | tree | approx. | Row of steps and queues; data boxes and the timeline row are not drawn. `wide-view`. |
| C1 application landscape | layered | ok | Used as the `shop-landscape` example. |
| C2 system context | nested | ok | Used as the `shop-context` example. |
| C3 container diagram | nested | ok | `wide-view` with three columns inside a boundary. |
| C4 component diagram | nested | ok | `wide-view`, as C3. |
| C5 logical architecture | layered | ok | Frames as bands inside a boundary; `wide-view`. |
| C6 integration interface | grid_table | table only | `grid_table` accepts tables only; the companion interface map needs a second view. |
| C7 bounded-context map | nested | approx. | Contexts and role chips work; edge direction between boundaries needs a visual check. |
| C8 layered architecture | layered | ok | |
| D1 entity-relationship | er | ok | Used as the `shop-er` example. Keep to one row of entities, see renderer gaps. |
| D2 data flow diagram | nested | ok | `wide-view`. Node kinds `process`/`dataset`/`job` used by some type pages are not in the schema: use `component`/`store`. |
| D3 data lineage and ownership | layered | approx. | Owner in `sub`, classification in `tags` work; flow across layers is vertical only. |
| E1 sequence diagram | sequence | ok | Used as the `shop-sequence` example. |
| E2 activity flowchart | lanes | approx. | Partitions as lanes; no fork/join bars, no top-to-bottom flow. |
| E3 state machine | statechart | approx. | Grid placement in node order; order the nodes so that transitions are neighbours. |
| E4 swimlane | lanes | approx. | Same limits as A5. |
| F1 authentication flow | sequence | ok | `alt` frame supported. |
| F2 threat model data flow | nested | ok | Used as the `shop-trust-boundary` example. |
| F3 access control model | grid_table | ok | Matrix as table. |
| G1 deployment diagram | nested | ok | `wide-view`. |
| G2 cloud infrastructure | layered | ok | |
| G3 network topology | nested | ok | |
| G4 delivery pipeline | tree | approx. | Linear chain; controllers as `lane` groups not combined with `tree`. `wide-view`. |
| H3 stakeholder map | grid_table | approx. | Two tables; a true 2×2 quadrant is a plain table. |

Types with no page yet have no template. Types the renderer cannot lay out at all: none; every page above renders.
