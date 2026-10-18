# D3 — Data lineage and ownership map

Steward accountability, technical custody and tenant-confidential versus deidentified classification are specified in AS-data. Ownership is not a read grant, and derived chunks retain source ACL restrictions.

AS-data 明确数据管理责任、技术保管及租户保密/去标识分类。数据归属不等于读取授权，派生分块保留源 ACL 限制。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
