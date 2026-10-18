# E2 — Activity diagram or flowchart

UML activity: one start, guarded valid/else decision and named outcomes. Approval, current permission and idempotent execution remain distinct. Ambiguous timeouts use key-based reconciliation under AS-request.

UML 活动：单一起点、有效/否则判断与具名结果。审批、当前权限及幂等执行分别表达；超时不明按 AS-request 进行按键对账。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
