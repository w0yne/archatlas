# Enterprise Service Assistant — shared teaching scenario

Version 2 defines one fictional target system: three synthetic tenants, six runtime
units and three tools. Stores, external systems and infrastructure are counted separately.
All 25 core views and four named variants are complete in English and Chinese (58 SVGs).

- `scenario.json`: canonical entities, invariants, flows, deployment and explicitly
  illustrative assumptions. No live implementation or measured score is claimed.
- `glossary.json`: canonical EN/ZH labels and contextual component/projection labels.
- `ASSUMPTIONS.md`: readable assumptions; the site also publishes bilingual reference pages.
- `manifest.json`: explicit view/language/publication contract. G1-AWS remains G1's
  first illustration; G1-generic is the separate vendor-neutral hosting view. E4 does
  not replace the E2 activity sample.
- `views/<id>/<lang>/`: author-owned SVG, model and expected projection. The generator
  validates and copies artwork; it does not auto-layout over it.

Preserve tenant/ACL checks before retrieval and citation access, exact approval binding,
execution-time reauthorization, constrained delegation and idempotent reconciliation.
Model output and guardrails never grant authority. An operator's deployment responsibility
does not grant tenant-content access. The AS delegation contract and chosen AWS region/model
support must be validated before implementation. Historical evaluations remain tied to
their original revisions; targeted contract regressions are not new multi-host quality scores.
