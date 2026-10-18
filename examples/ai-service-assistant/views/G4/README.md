# G4 — Evaluation-gated configuration promotion

经评测门禁的配置晋级

Scope is versioned prompt/model configuration, not an invented application-image CI pipeline. DS-eval supplies versioned inputs, C-eval runs under its isolated identity, and quality/safety/latency/token-cost gates control promotion. Solid arrows carry artifacts or evidence; dashed arrows show gate/hand-off dependencies. A failed or unspecified gate holds the candidate. The tested version is the intended promotion identity; digest/registry details are not fabricated. C-agent is the existing target. Redacted health evidence informs a recovery decision whose owner/action remains unknown. The context entity attached to a local action is traceability, not assigned accountability.

Missing facts: CI/change trigger, gate thresholds, immutable artifact/digest contract, approver, deployer and actual promotion mechanism, post-release recovery policy and responsible owner. No rollback or automatic deployment guarantee is asserted.

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
