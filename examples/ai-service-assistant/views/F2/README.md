# F2 — Threat-model data-flow diagram with trust boundaries

DF identifiers trace data flows to threat hypotheses; they are not message order. DF-6 abstracts proof delivery through Agent (F1), and DF-4 reads current approval through the BFF. Proposed controls still require implementation validation.

DF 标识将数据流对应到威胁假设，不是消息顺序。DF-6 抽象经 Agent 传递证明（F1），DF-4 经 BFF 读取当前审批；拟议控制仍需实施验证。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
