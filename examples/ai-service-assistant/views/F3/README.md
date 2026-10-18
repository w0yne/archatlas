# F3 — Access-control model

Explicit grants are unioned, then intersected with current tenant/resource constraints; policy denial wins. Steward reads require ACL permission. Operator rights never automatically grant tenant content access.

显式授权取并集，再与当前租户/资源约束相交；策略拒绝优先。知识管理员读取须满足 ACL，运维权限不自动授予租户内容访问。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
