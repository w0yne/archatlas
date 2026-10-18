# H2 — Redacted service evidence and use

脱敏服务证据及用途

Five existing runtime units and the ingestion queue emit already-redacted evidence to the CloudWatch facet of AWS-ops. The aggregate AWS-ops stable label remains unchanged; KMS/Secrets are not asserted to be telemetry collectors. No new collector, alert service or notification component is introduced. Source instrumentation must avoid raw tokens/document text before export; a downstream filter is not assumed to erase earlier exposure. The operator sees health and cost evidence, not implicit tenant content access. Signal arrows are producer→receiver; no tracing or alerting pipeline is claimed implemented.

Missing facts: concrete SLI/SLO definitions and targets, sampling/retention/loss policy, enabled collection configuration, alert thresholds, notification routes and response runbooks.

## Files and integration contract

`en/diagram.svg` and `zh/diagram.svg` are hand-authored source artwork. The adjacent
`diagram.json` uses the existing model schema. `expected.json` pins scenario version 1,
shared entities and applicable invariant IDs. No runtime component, identity or permission
is added by the view-local action/state/gateway/symbol IDs.

For behaviour views, `viewElements` records bilingual labels, a `contextEntity` and
`sourceRefs` for each local semantic/notation element. A context entity is traceability,
not an assignment of RACI accountability. Existing runtime/entity nodes stay in `entities`
and retain their canonical bilingual labels. A future manifest validator must validate
this disjoint union against model node IDs and keep strict entity-label checks; do not
silently accept arbitrary renamed components. Tables use `roleEntities`/`tableSourceRefs`
instead of pretending that cells are runtime nodes. This is sidecar validation metadata,
not an extension of the diagram model schema.

Register the new view/language entries and regenerate published copies only in the
integration change. The C3 published copy is intentionally not updated here. The sample
builder's byte-equality check will require that synchronization. All existing scenario,
glossary, registry, manifest, renderer and site sources are unchanged.
