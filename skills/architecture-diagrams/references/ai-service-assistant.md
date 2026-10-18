# Enterprise Service Assistant worked example

This fictional target design illustrates multi-tenant knowledge answers and approved
service-ticket actions. It is not an implemented or benchmarked system.

In a release bundle, the shared source is `assets/examples/ai-service-assistant/`.
In a repository checkout, it is `examples/ai-service-assistant/` at the repository root.
Read `README.md` and `scenario.json` there before adapting a view. `manifest.json`
enumerates the exact view/language pairs, publication paths and remaining scope.

Start with C2, C3, E1 and G1-AWS; add F1 for delegated identity and F2 for threat
boundaries. D2 focuses on the knowledge-answer data flow. G1-AWS is the G2 named
implementation variant and the G1 headline illustration; G1-generic is the separate vendor-neutral
hosting sample. All 25 core and four named-variant views have EN and ZH versions live under `views/<view>/<lang>/`.

The SVGs are hand-authored source artwork. Their models and expected-entity mappings
refer to the same stable scenario IDs; do not infer that automatic rendering will
reproduce their composition. Check any adapted SVG against its model and review the image.

Preserve tenant/ACL checks, approval binding and fresh authorization, the issuer/
audience/actor distinction, explicit AS-delegation assumptions and bounded idempotent
execution. Model output and guardrails never grant permissions. The six runtime units
exclude stores, external systems and managed infrastructure. Do not add a service or
change authority independently in one view; first revise the shared facts coherently.

Scenario version 2 resolves teaching assumptions centrally; read ASSUMPTIONS.md and
glossary.json with the scenario. Parameters and ownership are illustrative, not observed.
