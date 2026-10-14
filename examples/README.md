# Worked examples

Six small diagrams of one neutral scenario, each as a semantic model plus English and Chinese labels. They show what a correct, checked output looks like for a type, and they are the fixtures the skill points at.

## The scenario

An **online shop** sells goods to customers. Customers browse a web storefront (and a mobile app), place orders through an order API that keeps its data in a shop database, and pay through an external payment provider. Parcels go out through an external carrier; receipts go out through an external email service. An optional **support chatbot** answers customer questions next to human support agents. Orders, customers, products and order lines are the core data; returns are handled by support and the warehouse.

All examples and all templates in `skills/architecture-diagrams/assets/templates/` use only this scenario. Nothing here describes a real company or product.

## Examples

| Folder | Type | Template | Question it answers |
| --- | --- | --- | --- |
| `shop-landscape/` | C1 application landscape | `layered` | Which applications exist, which are shared, what is outside? |
| `shop-context/` | C2 system context | `nested` | Who uses the shop and which outside systems does it depend on? |
| `shop-sequence/` | E1 sequence | `sequence` | In what order do the parties talk when an order is placed? |
| `shop-er/` | D1 entity-relationship | `er` | Which business objects exist and how are they related? |
| `shop-trust-boundary/` | F2 data flow with trust boundaries | `nested` | Which flows cross a trust boundary during checkout? |
| `shop-swimlane/` | A5/E4 swimlane process | `lanes` | Who does what in a return, and where does it change hands? |

Each folder holds:

- `diagram.json` — the model (`archatlas: "0.1"`). Labels are keys, not text.
- `labels.en.json`, `labels.zh.json` — one label file per language; the keys match the model.
- `expected.md` — what a correct rendering must show and must not show (the review rubric).
- `out/diagram.en.svg`, `out/diagram.zh.svg` — generated output.

## Regenerate and check

```sh
atlas render shop-er/diagram.json --lang en -o shop-er/out/diagram.en.svg
atlas render shop-er/diagram.json --lang zh -o shop-er/out/diagram.zh.svg
atlas check shop-er/out/diagram.en.svg --report /tmp/shop-er.en.json --fail-on warning
```

Output is deterministic: rendering the same model, language and output name twice gives identical bytes. All twelve SVGs pass `atlas check` with 0 errors and 0 warnings.

## Profile

All six use the `doc` profile (width grows with content, at most about 1120 px for a page column). The fixed `slide` profile (1440×810) clips the landscape, sequence and swimlane examples at the current renderer's node sizes; see the work-package report.
