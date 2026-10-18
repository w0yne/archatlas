# C6 — Integration and interface diagram

Interface authentication, producer/consumer direction, bounded retries, ownership and capacity are illustrative contracts in AS-interfaces. Queue delivery is polled by the worker, not broker-initiated push.

接口认证、生产/消费方向、有界重试、归属和容量见 AS-interfaces 示意契约。队列由工作进程轮询，不是代理主动推送。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
