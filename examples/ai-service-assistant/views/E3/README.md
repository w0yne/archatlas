# E3 — Conceptual tool-request state machine

工具请求概念状态机

The subject is one tool request recorded in DS-app. Conditions and transitions are a conceptual projection of I-approval and I-idempotency, not invented persisted enum values. The initial transition has no trigger/guard. Every non-terminal condition has an outgoing transition, including unknown results that await a key-based lookup. Refused and recorded outcomes close separately. A recorded outcome may be a known failure; it is not a claim that every request created a ticket. There is no Unapproved→Executing shortcut.

Missing facts: actual persisted status enum, reconciliation deadline and closure policy. These must be agreed before treating the diagram as an implementation specification.

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
