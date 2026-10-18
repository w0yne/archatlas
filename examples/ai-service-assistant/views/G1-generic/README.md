# G1-generic — Vendor-neutral hosting allocation

供应商中立的软件承载分配

This is a different hosting/allocation composition, not a renamed copy of the AWS service diagram. All six runtime units and five stores/queues use their stable names and IDs. Generic compute groups abstract the same frozen deployment; no alternative provider/platform is introduced. Zone means availability/failure zone within the same single region. Every application service has at least two instances across two zones; batch jobs may run in either zone. Managed database storage remains three-zone as in the frozen facts, distinct from application placement. Only representative communications are shown; C3 is the dependency companion. External IdP, model and Service Desk are outside this hosting-focused view and remain in C2/C3/F1.

Integration: register id `G1-generic`, code `G1`, languages en/zh. Preserve G1-AWS as the first G1 headline sample; add this as a separate generic companion, not a duplicate headline override. No new deployment fact is proposed.

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
