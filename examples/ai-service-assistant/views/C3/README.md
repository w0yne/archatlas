# C3 — Container diagram (C4 model level 2)

Six runtime units, five stores/queues and the model dependency. API is the sole job producer; workers poll, fetch authorized source versions and create embeddings. All original node and edge identities are retained, with two added dependencies.

六个运行单元、五个存储/队列及模型依赖。API 是任务唯一生产者；工作进程轮询、读取授权源版本并创建嵌入。保留原节点与边标识，并补上两条依赖。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
