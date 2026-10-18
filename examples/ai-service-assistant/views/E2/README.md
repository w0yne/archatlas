# E2 — Approved ticket execution activity

审批后工单执行活动

UML activity: one initial node, actions, a guarded decision and named success/refusal finals. The P-plan, P-approve and P-execute labels and identities come directly from the frozen scenario. Local action/symbol IDs describe behaviour, not additional services. The false branch rejects before Service Desk. Timeout reconciliation is a referenced sub-activity under I-idempotency, not a blind retry. The request starts as an attempt to perform a permitted, human-approved action; this is not a separate human approval workflow.

No additional permission or runtime fact is required. Concrete UI cancellation policy and reconciliation timing are not asserted.

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
