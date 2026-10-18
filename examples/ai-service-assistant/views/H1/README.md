# H1 — Responsibility discovery with explicit gaps

明确责任缺口的梳理矩阵

The three human-role names/IDs are unchanged. R is recorded only for execution responsibilities already stated in the frozen facts: employee approval, steward knowledge/ACL and export work, and operator health work. Formal A/C/I assignments are unknown for every row, and release/recovery has no declared R. Question marks mean unassigned/unconfirmed, never “no involvement”. No row is claimed governance-complete, and accountability does not grant content or tool permissions.

Missing facts: formal accountable owners, consultation/information assignments, and release/recovery execution and decision ownership.

The English SVG has one justified `working-note` warning: the activity “Approve own permitted draft” uses **draft** as the business object in I-approval, not as a drawing status. The figure must keep that meaning; all geometry checks are clean.

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
