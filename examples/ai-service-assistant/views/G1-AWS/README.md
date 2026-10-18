# G1-AWS — Cloud infrastructure architecture

The AWS implementation variant is the first G1 illustration. Application services span two AZs; Aurora managed storage spans three; OpenSearch uses two-AZ zone awareness, not Standby. Regional managed services are outside customer subnets, CloudFront is global.

AWS 实现变体保持为 G1 首图。应用服务跨双 AZ；Aurora 托管存储跨三 AZ；OpenSearch 是双 AZ 区域感知而非 Standby。区域托管服务位于客户子网外，CloudFront 为全球服务。

These are original hand-authored EN/ZH SVGs for scenario version 2. Facts and teaching
choices live in [scenario.json](../../scenario.json), the [shared glossary](../../glossary.json)
and [assumptions](../../ASSUMPTIONS.md). They are illustrative, not deployed or measured.

`diagram.json` uses the unchanged diagram model schema. `expected.json` maps shared
entities and semantic/notation projections to central facts. `viewElements` are actions,
states or symbols, never new runtime components or implicit permission grants. The sample
builder checks and copies the artwork byte-for-byte. Published copies and all 29 view pairs
are registered by the manifest. Historical shop fixtures remain unchanged.
