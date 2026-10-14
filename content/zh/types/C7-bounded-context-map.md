---
code: C7
slug: bounded-context-map
family: C
names:
  en: Bounded context map (DDD)
  zh: 限界上下文映射（DDD）
  aliases:
    en: [context map, DDD context map, strategic design map, team map (organisational variant)]
    zh: [上下文映射图, DDD 战略设计图, 领域上下文图, DDD 上下文映射, 战略设计图, 团队映射图]
question: 在这个系统内部及其周边，存在哪些各自拥有一致语言的不同模型？每条边界上又存在怎样的权力、协调或转换关系？
audiences: [architects, developers, business]
levels: [concept, logical]
phases: [design]
scope: 一个系统或一片系统全景中的限界上下文（或其背后的团队），以及每条边界上的关系；每张图约 5–12 个上下文。
formal: {kind: method, ref: 'Domain-Driven Design: Evans, DDD (2003) and DDD Reference (2015, CC BY 4.0); no graphical standard'}
neighbours: [C5, C6, C8]
status: draft
translationOf: en/types/C7-bounded-context-map.md
sourceRev: a5d2191
reviewed: false
---

# 限界上下文映射图（Bounded Context Map）

> 一张标出一个领域模型在哪里结束、下一个从哪里开始的图，并说明每条边界上适用哪种关系模式（谁适应谁、谁负责转换）。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->

上下文映射图（context map）回答的是：*这里存在哪些拥有各自语言的模型，跨越每条边界时谁必须适应谁？* 限界上下文（bounded context）是一个模型及其术语保持一致的边界 [1][5]。这张图既是技术的，也同样是**社会技术的**：Evans 指出，关系上的约束主要通过非技术渠道显现 [1]；Brandolini 则有意纳入了传统分析会忽略的团队结构和影响力 [3]。按 ISO/IEC/IEEE 42010 的说法，它的关注点（concern）是语言一致性、集成成本、团队耦合以及谁适应谁 [12]。它不是 C4 model 的某个层级：它的元素是模型或团队，而不是可部署单元。

**来源（本站采用的定义）。** Evans 的书（2003 年 8 月出版）提出了 Bounded Context、Context Map、Shared Kernel、Customer/Supplier、Conformist、Anticorruption Layer、Open Host Service、Published Language 和 Separate Ways。**合作关系**（Partnership）和**大泥球**（Big Ball of Mud）*并不*在书中。Evans 的 **DDD Reference（2015）**将二者标为"new since the 2004 book" [1]。Brandolini 于 2009 年在行文中使用了"partnership" [3]，Vernon 于 2013 年将其列入模式 [4]。大泥球源自 Foote & Yoder（1997）[1]。未找到 Evans 更早公开使用"Partnership"的记录。

**两种变体：** **系统全景图**（默认；上下文是软件模型）和**组织 / 团队图**（上下文是团队及其关系）[6]。

**有意不包含：** 各上下文的内部（聚合、实体；请用 Bounded Context Canvas 或 D1）、数据库表、协议细节（C6）、部署单元（G1）、调用顺序（E1）。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->

- **受众：** 架构师、领域专家和产品负责人、技术负责人，以及决定团队边界的工程经理。它常常是战略设计工作坊（例如全景式 EventStorming）的产出 [8]。
- **典型场景：** (1) 在动代码之前拆解单体，或规划模块化单体、服务拆分；(2) 协调多个团队：谁在上游、谁来协商、谁要建防护层 [8]；(3) 集成遗留系统或第三方系统，在防腐层与遵奉之间做决定；(4) 在转型之前"摸清现有地形"，即多厂商系统全景的现状 [1]；(5) 把工作坊中发现的语言边界整理成初稿。
- **不适用的情况：** 只有一个团队、一套词汇的小型应用（C3 容器视图就够了）；纯技术性的集成问题（C6）；部署问题（G1）。如果读者不熟悉 DDD 词汇，用直白的标签（"必须跟随""负责转换"），把模式名称放在图例里。
- **与相邻类型的区别：**
  - 要表达*有哪些系统、如何连接*时，选 **C1/C2**。C7 表达模型在哪里结束。两个系统可以共享一个上下文，一个系统也可以承载多个上下文。
  - 要按可部署单元或职责分组时，选 **C3/C5**。C7 按*语言和模型的有效范围*分组。
  - 要表达技术契约时，选 **C6**。C7 给出解释该契约的模式名称（开放主机服务、防腐层……），该模式可以作为 C6 表格中的一列。
  - 要表达*单个*上下文内部的结构时，选 **C8**。把整个系统按 UI/服务/数据库分层来划分，是寻找上下文的典型错误做法 [5]。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->

- **没有正式标准。** 常见表示法：Evans/Vernon 风格的方框加带标签连线；DDD Crew 的模式图形 [7]；Context Mapper 的 CML 文本及其生成的图 [6]。
- **必需：** 每个上下文一个具名方框，使用业务名称（它会成为通用语言），绝不用技术名称。每个关系画一条线，**每条线都标注模式**，并为所用缩写配图例。
- **方向 = 影响力，而不是数据流。** 非对称连线从**上游 → 下游** [6]，数据可以沿这条线双向流动。
- **角色标在方框边缘；关系是连线** [6]：
  - *上游侧角色：* **OHS** 开放主机服务（Open Host Service，面向众多消费方的一个开放协议），**PL** 发布语言（Published Language，有文档的交换语言，常与 OHS 搭配）。
  - *下游侧角色：* **CF** 遵奉者（Conformist，原样采用上游模型），**ACL** 防腐层（Anticorruption Layer，转换为自己的术语）。
  - *对称关系（无 U/D）：* **P** 合作关系（Partnership，团队同成同败，共同规划），**SK** 共享内核（Shared Kernel，一小块明确共享的模型和代码子集）。
  - *特化的上游–下游关系：* **C/S** 客户/供应商（Customer/Supplier，下游的优先级进入上游的规划）。
  - *无关系：* **各行其道**（Separate Ways）。*圈起来的混乱：* **大泥球**（Big Ball of Mud，画出边界，不在内部建模）。
- **一致性规则：** 对称的一对（P、SK）绝不再标 U/D。一条线*要么*是对称的，*要么*是上游–下游的 [6]。
- 组织变体中的**团队关系**：相互依赖、上游/下游、自由 [1][7]。
- **可选：** 核心/支撑/通用分类、各上下文的负责团队、AS-IS/TO-BE 标记、未解决重叠处的警示标记 [3]。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### 最佳实践

1. 从语言出发，而不是从技术出发：边界出现在同一个词含义不同的地方 [5]。
2. 先如实绘制 AS-IS 现状，再提出 TO-BE，并让未解决的重叠保持可见 [1][3]。
3. 按*真实*的权力结构选择每个模式。让每个上下文的负责团队可见 [3][9]。
4. 让图保持小巧，一张图回答一个问题，只纳入回答该问题所需的模式 [7]。
5. 把映射图以带版本的文本保存在仓库中（CML 或图即代码），并在 Bounded Context Canvas 上分别描述每个上下文 [6][7]。

### 反模式

1. **把上下文等同于微服务。** 服务边界与上下文边界相关 [10]。一个服务不应跨越两个上下文，但一个上下文可以包含多个服务 [11]。
2. **连线不标模式**，或只因为术语表里有就选了某个模式。
3. **把层称作上下文：** 按 UI / 服务 / 数据库切分 [5]。
4. **箭头含义错误或画成期望状态：** 箭头画成数据流，或把期望中的集成画得好像已经存在。
5. **角色不一致：** 在合作关系的一对上标 U/D，共享内核庞大且变化频繁，或者把遗留系统画成边界清晰，而不是圈起来的大泥球。

## 范例 {#exemplars}
<!-- skill: omit -->

- [Context Mapper examples](https://github.com/ContextMapper/context-mapper-examples) — 文本模型与生成的映射图并排展示，含 AS-IS/TO-BE、系统图和团队图（Apache-2.0）。
- [DDD Crew, Context Mapping](https://github.com/ddd-crew/context-mapping) — 速查表和模式图形，含团队关系（README 写的是 CC BY 4.0，仓库元数据写的是 CC BY-SA 4.0；复用图形前请核实）。
- [Brandolini, "Strategic Domain Driven Design with Context Mapping"](https://www.infoq.com/articles/ddd-contextmapping) — 一张逐步演进的 AS-IS 映射图实例，带警示标记和团队背景（许可未核查）。
- [Microsoft, "Use domain analysis to model microservices"](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) — 从领域草图到上下文，再到关系清单，最后到服务边界（Microsoft Learn 条款）。
- [Evans, DDD Reference (2015)](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) — 一份简短 PDF 中的权威模式定义（CC BY 4.0）。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->

1. 以语言簇列出候选上下文：同一个名词（"订单""产品"）含义或字段不同，就是边界的信号。
2. 用业务名词为每个上下文命名；已知的话加上负责团队；只有在有证据时才标核心/支撑/通用分类。
3. 选择变体：系统全景图（默认）或组织/团队图。
4. 对每一对有交互的上下文，问"谁必须适应谁？"。在对称（P、SK）、上游–下游（含角色）或各行其道之间选择。未知的一对标为"不明"。
5. 布局：上游放在下游的上方或左侧，使影响力从上到下或从左到右阅读。OHS/PL 标签放在上游方框边缘，CF/ACL 放在下游方框边缘。对称的一对并排放置，用无向线连接。
6. 外部系统和大泥球放在外围，用虚线轮廓。
7. 文字：方框 = 名称，可加一行小字写团队；连线标签只写模式缩写；不用技术徽标。
8. 颜色只表达一种含义（分类*或*团队）；外部系统用灰色；琥珀色只用于问题。
9. 标题写明范围和状态（AS-IS/TO-BE）；图例只列出所用缩写；超过约 12 个上下文就按问题拆图。

**自检清单**
- [ ] 每个方框都是模型/语言边界，而不是层、工具或服务器。
- [ ] 每条线都有模式，或明确标为"不明"。
- [ ] 非对称箭头从上游指向下游，并在图例中说明。
- [ ] 没有对称的一对（P、SK）同时带有 U/D 角色。
- [ ] 角色（OHS、PL、CF、ACL）标在正确的一侧。
- [ ] 已声明 AS-IS 或 TO-BE；未来的集成没有画成现状。
- [ ] 每个上下文名称一致，并有负责方（或标"负责方未知"）。
- [ ] 没有表格或部署名称；颜色只有一种含义。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->

- 线索而非证明：顶层模块或包（候选上下文）；两个模块中同名但字段不同的实体（语言边界）；有版本、多消费方的 OpenAPI/AsyncAPI/protobuf 文件和 topic 名称（OHS+PL）。
- 适配器、转换器或 `legacy` 包以及映射类（ACL）；共享的 `common`/`shared-domain` 库（共享内核候选，或一种坏味道）。
- 部署清单列出的是服务，即候选的*实现*；多个服务可能属于同一个上下文。
- CODEOWNERS 和团队目录（归属）；术语表、ADR 和已有的 CML 文件（以它们为事实来源）。
- 需要问人：团队之间的权力与协商关系，今天真实存在的是哪种模式，以及预期的 TO-BE。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->

1. 这张图要回答什么问题（拆分单体、协调团队、规划集成），范围是什么？（默认：一片系统全景，集成规划。）
2. AS-IS 还是 TO-BE；系统全景图还是团队图？（默认：AS-IS 系统全景图。）
3. 哪些术语在业务的不同部分含义不同，每种含义归谁？（默认：从"产品""订单""客户"开始。）
4. 对每个依赖：谁适应谁？目前是否有协商过的契约、已发布的 API 或转换层？（默认：确认前标为"不明"。）
5. 受众是否了解 DDD 模式名称？（默认：使用模式缩写，并配直白的图例。）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->

模型模板：`assets/templates/C7.json` · 布局模板：`nested` · 每个上下文是一个 `boundary` 分组，其中为每个关键模型放一个 `component` 节点（团队放在节点的 `sub`，OHS/ACL 等角色标签放在其 `tags`）；`edges` 携带模式标签，`dir` 为 `->` 表示上游→下游，`--` 表示对称。

## 来源 {#sources}
<!-- skill: omit -->

1. Evans, *Domain-Driven Design Reference: Definitions and Pattern Summaries* (2015, CC BY 4.0) — https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf — 访问于 2026-10-14
2. Wikipedia, "Domain-driven design" (Evans' book, August 2003) — https://en.wikipedia.org/wiki/Domain-driven_design — 访问于 2026-10-14（二手来源）
3. Brandolini, "Strategic Domain Driven Design with Context Mapping", InfoQ (2009) — https://www.infoq.com/articles/ddd-contextmapping — 访问于 2026-10-14
4. Vernon, *Implementing Domain-Driven Design* (2013), sample pages — https://ptgmedia.pearsoncmg.com/images/9780321834577/samplepages/0321834577.pdf — 访问于 2026-10-14
5. Fowler, "BoundedContext" (2014) — https://martinfowler.com/bliki/BoundedContext.html — 访问于 2026-10-14
6. Context Mapper, Context Map and language semantics — https://contextmapper.org/docs/context-map/ — 访问于 2026-10-14
7. DDD Crew, Context Mapping — https://github.com/ddd-crew/context-mapping — 访问于 2026-10-14
8. DDD Crew, DDD Starter Modelling Process — https://github.com/ddd-crew/ddd-starter-modelling-process — 访问于 2026-10-14
9. Avanscoperta, "Context Mapping in DDD" — https://www.avanscoperta.it/en/context-mapping/ — 访问于 2026-10-14
10. Lewis & Fowler, "Microservices" (2014) — https://martinfowler.com/articles/microservices.html — 访问于 2026-10-14
11. Microsoft Learn, "Identify microservice boundaries" — https://learn.microsoft.com/en-us/azure/architecture/microservices/model/microservice-boundaries — 访问于 2026-10-14
12. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/ieee-1471/cm — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->

![C7 示例：网店上下文映射图——Catalogue（OHS、PL）是 Ordering（CF）的上游；Ordering 与 Payments 为合作关系；Ordering 作为 Fulfilment 的供应方；Fulfilment 以 ACL 对接遗留仓储系统（大泥球）；Payments 以 ACL 对接外部支付服务商（OHS）；Customer Support 遵奉 Ordering](/samples/C7-bounded-context-map.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
