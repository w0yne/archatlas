# C7 — Bounded context map (DDD)

Each named system is treated as an opaque bounded context with an illustrative team/model contract. DDD ACL means anti-corruption layer; document ACL means access-control list. CF covers protocol adoption, never authority from model output.

各具名系统被视为不透明限界上下文，配有示意团队/模型契约。DDD ACL 指防腐层，文档 ACL 指访问控制列表；CF 仅指协议遵循，不接受模型输出授予权限。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
