# E3 — State machine diagram

One request in DS-app: unapproved, approved, executing, unknown, recorded, refused and closed. Unknown outcomes remain held after bounded reconciliation; they do not authorize a fresh write.

DS-app 中的单个请求：未审批、已审批、执行中、未知、已记录、拒绝及关闭。有界对账后仍未知则保持挂起，不授权重新写入。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
