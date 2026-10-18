# F1 — Authentication and authorization flow

The exchange request is common to both allow and deny paths. Agent is the authenticated exchange client. Tool proof binds issuer, audience, subject, actor, tenant and scopes; verification never replaces current authorization. AS delegation support is an implementation prerequisite.

交换请求为允许/拒绝分支共有的前提；Agent 是认证后的交换客户端。工具证明绑定 issuer、audience、subject、actor、tenant、scopes；核验不能代替当前授权，AS 委托支持是实施前提。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
