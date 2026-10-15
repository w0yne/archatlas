# Visual language

Archatlas uses one default style inspired by an illustrated architecture-diagram
guide: saturated focus cards, soft zones, clear header bands, compact annotations
and semantic legends. The model's default theme name remains `neutral`. Legacy
`print` and `dark` values map the same components to compatible palettes; they
do not define separate rich/simple workflows.

Tokens live in [theme.py](../src/archatlas/render/theme.py); author-facing fields
live in [schema.json](../src/archatlas/model/schema.json). Dimensions below are
SVG user units.

| Semantic role | Fill | Border | Intended meaning |
| --- | --- | --- | --- |
| `primary` | `#1767B5` | `#03172E` | Element in focus; white text |
| `peer` | `#D8E8FF` | `#3D6FB2` | Ordinary element in scope |
| `external` | `#EDEDED` | `#666A73` | External participant |
| `shared` | `#DCF2DC` | `#397645` | Shared element |
| `planned` | `#EBDDF9` | `#7951A5` | Proposed element |
| `highlight` | `#FFF1C9` | `#936A16` | Highlighted element or callout |

The canvas is white, text is `#1F2937`, and secondary text is `#4B5563`.
Borders and secondary text are darker than the guide's original pastel strokes
to support contrast checks: 4.5:1 for ordinary text, 3:1 for large text and
meaningful strokes. Preserve the soft fills without relying on color alone.

| Group `tint` | Body | Header | Border |
| --- | --- | --- | --- |
| `app` | `#F3F8FF` | `#D8E8FF` | `#3D6FB2` |
| `tech` | `#F0F9F0` | `#DCF2DC` | `#397645` |
| `data` | `#F8F3FD` | `#EBDDF9` | `#7951A5` |
| `biz` | `#FFFBEB` | `#FFF1C9` | `#936A16` |
| `security` | `#FFF4F1` | `#FFE1DC` | `#B34232` |
| `neutral` | `#F7F7F7` | `#EDEDED` | `#666A73` |

Groups default to `app`; an explicit group style supplies a corresponding tint
unless `tint` overrides it. `band: true` adds a measured header within the group;
`false` removes the band while retaining the title and containment. Layer groups
use these same components. Tint never classifies the contents or establishes a
trust boundary by itself.

| Typography | Size | Weight |
| --- | --- | --- |
| Figure title | 28 | 700 |
| Node name / group title | 16 | 700 |
| Optional figure subtitle | 14 | 400 |
| Node `sub` / attributes / connector labels | 12 | 400 |
| Chips / legend | 11 | 400 |
| Badge | 11 | 700 |

Measure the actual installed face at the requested weight, including Latin/CJK
fallback runs. Regular-face advances are not substitutes for bold measurements.
Missing dependencies, glyphs or weight-specific faces produce explicit estimate
warnings and conservative padding. SVG text remains live; installed fonts still
affect display. Wrap at supported word/CJK boundaries and grow the layout rather
than silently cutting words.

| Component | Tokens and author interface |
| --- | --- |
| Card | Radius 8; stroke 1.8, or 2.4 for primary. Use `style` for emphasis; ordinary cards default to `peer`, explicitly external kinds to `external`. |
| Zone | Radius 10; stroke 1.6; padding 24; header reservation starts at 52 and grows with measured text. |
| Chip | Rounded pill, radius 10, horizontal padding 9, gap 6. Node `chips` accepts strings or `{"label": "HTTPS", "style": "shared"}`; omitted style is `peer`. Rows wrap inside the card. Existing `tags` also become chips on cards. |
| Badge | Node `badge`: integer 1–999 or string of 1–4 characters. A measured circle reserves space inside the card; explain its step/reference meaning. |
| Asset | Node `shape`: `card`, `database`, `document`, `queue`, or `callout`. Asset cap token: 12. Defaults: `store` → cylinder, `queue` → queue, `document` → folded document. `shape: "card"` can retain a rectangular store. |
| Callout | `note` / `callout` defaults to a callout card and `highlight` style. Use normal `label`, `sub`, chips and containment for a short explanation or example. |
| Connector | Stroke 1.8; default peer line `#4B5563`, primary line `#2563EB`. Measured label pills separate text from the route. Direction, open/filled arrowheads and dashes follow the relationship notation. |
| Legend | A light panel groups compact swatches and semantic labels. Use `meta.legend` or `meta.legend_labels` for precise meanings. An authored label with no encoding fields is a text note, not an invented line symbol. |

`meta.subtitle`, node labels, `sub` and chip labels use the existing localization
mechanism. Keep subtitles short and informative. Formal UML/BPMN symbols retain
their established geometry: `actor`, `event`, `gateway`, `use_case`, `initial`
and `final` reject shape overrides, chips and badges. Their existing tags remain
plain labels.

This additive example keeps `archatlas: "0.1"`:

```json
{
  "archatlas": "0.1",
  "meta": {
    "type": "C3", "title": "Order processing", "lang": "en",
    "subtitle": "Runtime responsibilities",
    "legend": [{"label": "1: Request entry point"}]
  },
  "layout": {"template": "nested", "direction": "LR", "profile": "doc"},
  "groups": [
    {"id": "service", "kind": "boundary", "title": "Order service",
     "tint": "app", "band": true}
  ],
  "nodes": [
    {"id": "api", "kind": "container", "label": "Order API",
     "sub": "Accepts orders", "style": "primary", "parent": "service",
     "badge": 1, "chips": [{"label": "HTTPS", "style": "shared"}, "Stateless"]},
    {"id": "db", "kind": "store", "label": "Orders",
     "parent": "service", "chips": ["Relational"]},
    {"id": "rule", "kind": "callout", "label": "Idempotent requests",
     "sub": "Repeated keys return the original order.",
     "style": "highlight", "parent": "service"}
  ],
  "edges": [{"from": "api", "to": "db", "kind": "data", "label": "Stores"}]
}
```

These components express supplied facts; they do not infer protocols, ownership,
security properties, evidence, deployment status or new connections. A badge does
not establish execution order, and a callout does not create an edge. Explain
meaningful colors and symbols in the legend; keep evidence status explicit.

The shared vocabulary does not reproduce every hand-composed guide diagram.
Diagram-specific manual composition, 3D forms, cloud silhouettes and chevrons are
outside this component set. Automatic layouts still need semantic and visual
review; a successful geometry check alone is not a visual pass.

## Focus, sequence fragments and link identifiers

Use `layout.focus: "node-id"` to select a subject without changing the input
node records. It renders that node as `primary`; in a sequence, its participant
header, lifeline and activations share the emphasis. Other explicit primary
nodes remain visible. QA reports `multiple-focus` when more than one node is
primary, including a selected focus; it does not silently recolor the model.
`highlight` remains a general annotation/category color, so the renderer does
not infer focus from that color or from free-text legend captions.

Sequence fragments span the interval from their first involved participant to
their last, with room for self-calls and nested fragments. A participant between
those endpoints can remain inside the interval even if it sends no message in
that fragment. Guard/header rows reserve annotation gutters; lifelines and
activation rectangles are segmented around them and message-label backgrounds.
This preserves the model's activation ranges, rather than inventing execution
events. Labels use the available message span and measured height to give the
sequence a compact vertical rhythm. Select a focus explicitly when it matters.

An edge may carry `badge: 3` (or a short string), rendered beside its label.
Existing edge `step` numbers still render as text; an explicit badge replaces
that displayed identifier while sequence step ordering remains unchanged. Outside sequence views,
numbers are labels for reference by default: they do not establish temporal
order. Set `layout.ordered: true` to declare flow order; sequence views default
to ordered. The legend states the numbering meaning even in `legend_mode:
"replace"`. Node badges identify elements independently of link numbering.

Automatic legends cover all visible node encodings, zone tints, header bands,
dashed boundaries and badges, including a sole peer color. They reuse actual
glyphs and paint, including asset silhouettes. Author entries override captions
when their encoding fields match a visible encoding; typed entries with no
match are omitted. A bare label or symbol-only entry is a text note. For precise
zone captions, use `symbol: "zone"` with `tint`, `band` and/or `dashed`; badge
entries can use `symbol: "badge"` and `badge`. The legacy `replace` mode still
suppresses automatic style completion, so its author remains responsible for
omitted meanings. Numbering meaning is always retained.

Routing checks retain detour, foldback, crossing and overlap findings. They
also check inward endpoint directions and sum shared lengths across segments,
so splitting an overlap into short pieces does not hide it. Reports include
per-edge length, endpoint distance, backtracking and bend count. A long monotone
relationship can still be a placement problem even when its detour ratio is one;
passing geometry QA does not certify the composition.
