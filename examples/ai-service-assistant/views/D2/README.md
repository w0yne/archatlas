# D2 — Data flow diagram (DFD)

Tenant/ACL filtering is explicit before retrieval and current access is checked again when a citation is opened. This logical DFD covers knowledge answering; ticket writes and evaluation are separate views.

检索前明确执行 tenant/ACL 过滤，打开引用时再次核对当前权限。此逻辑 DFD 聚焦知识回答，工单写入与评测另图表达。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
