# D1 — Entity-relationship diagram

A logical entity subset, not complete DDL. Tenant-owned PK/FKs include tenant scope; approval binds the idempotency tuple as well as subject, tool, hash and expiry. Messages/citations remain part of the conversation aggregate.

逻辑实体子集，非完整 DDL。租户记录 PK/FK 含租户范围；审批除主体、工具、hash、有效期外还绑定幂等元组。消息/引用仍属于对话聚合。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
