# C3 — Corrected container dependencies

补齐依赖的容器图

All twelve prior node IDs and all existing edge IDs/endpoints are retained. CON-17 adds C-api→Q-ingest (enqueue); CON-18 adds C-ingest→X-model (embeddings). Receive-jobs text is attached to its queue link, publishing text has clear right clearance, and the model sits beside ingestion/evaluation instead of beneath long vertical links. The canvas height is 1280 instead of 1630; width 1720 keeps 1440-wide text readable. This is still six runtime units, five stores/queues, and one external model dependency; other external interfaces remain in C2/F1.

Missing fact to reconcile: the frozen FL-ingest currently shows worker publication while this required projection shows API-enqueued work. Add or distinguish the API initiation and worker version-publication paths in shared facts before claiming complete cross-view consistency. No shared scenario file is changed here.

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
