---
code: A1
slug: capability-map
family: A
names:
  en: Business Capability Map
  zh: 业务能力图
  aliases:
    en: [capability map, business capability model, capability heat map, capability landscape]
    zh: [能力地图, 业务能力模型, 能力热力图]
question: "业务必须具备哪些能力（不论由谁、以何种方式、用哪个系统来完成）？其中哪些能力强、哪些弱、哪些缺失、哪些具有战略意义？"
audiences: [高管, 业务发起人, 战略与投资组合负责人, 企业架构师, 业务架构师]
level: strategy
phases: [discovery, planning, review]
scope: "一个企业或业务单元，一页呈现 2–3 个能力层级，可选叠加一种评估热力图"
formal:
  kind: standard
  ref: "ArchiMate 3.2 Capability element and Capability Map viewpoint; TOGAF Series Guide: Business Capabilities, Version 2 (G211, 2022) and BIZBOK Guide for content rules"
neighbours: [A2, A5, A3, C1, A7, A8]
status: draft
translationOf: en/types/A1-capability-map.md
sourceRev: 6857dea
reviewed: false
---

# 业务能力图（Business Capability Map）

> 用一页图呈现业务必须具备的全部能力，按分层和层级组织，不含流程、不含组织单元、不含系统。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 业务需要哪些能力，而不论由谁执行、如何执行、用哪个系统执行？叠加热力图后：哪些能力薄弱、缺失、具有战略意义或投入过度？
- **视点：** ArchiMate *Capability Map viewpoint*（干系人：业务经理、企业架构师和业务架构师；目的：设计与决策；范围：战略）[3]。TOGAF 将其放在阶段 B，并在阶段 A 用于愿景和优先级排序，对应的制品名为 *Business Capability Map*（图）和 *Business Capabilities catalog*（目录）[1][2][11]。它没有对应的 C4 model 层级：这张图位于任何系统之上。
- **深层含义：** 能力图展示企业的“静态”面貌；价值流和流程展示其“动态”面貌 [4][3]。它的价值在于稳定：能力模型独立于组织结构、流程、应用和产品组合 [1]，因此可以作为锚点，与组织单元、价值流阶段、应用和举措做交叉映射。能力只说明某种能力必须存在，不说明做得多好；“做得多好”由热力图（heat map）叠加层补充 [1]。
- **不包含：** 顺序与流转、组织单元、角色、系统、技术和产品目录。这些各自属于单独的视图或交叉映射 [1][4]。
- **本站采用的定义：** *模型*是完整且有定义的能力集合（通常 3–6 层 [1]）；*图*是它的一页式呈现（2–3 层 [3]）。ArchiMate 将能力（Capability）定义为“an ability that an active structure element, such as an organization, person, or system, possesses”（主动结构元素，如组织、人员或系统，所具有的一种能力）[3]。
- **版本说明：** 本页依据 ArchiMate 3.2。ArchiMate 4（2026 年 4 月发布）将“层”（layer）更名为“域”（domain）；此点尚未对照现行规范原文核实。

| 概念 | 表达什么 | 命名方式 | 稳定性 |
|---|---|---|---|
| 能力（Capability） | 业务能做*什么* | 名词或动名词（“Order Management”） | 最高 |
| 业务职能（business function） | 按技能归组的行为，“closely aligned to an organization”（与组织紧密对应）[3] | 名词 | 中 |
| 业务流程 | *如何做*：针对一个案例按时间排序的步骤 | 动宾结构（“Handle Return”） | 低 |
| 价值流（A2） | 价值*如何*分阶段地*累积*到干系人 | 动宾结构（“Fulfil Customer Order”） | 高 |
| 组织单元 | 由*谁*来做 | 部门名称 | 最低 [1] |

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 高管和发起人（通常只看第 1 层）、战略与投资组合负责人、企业架构师和业务架构师（看更深层级）[1]。
- **典型场景：**
  1. 年度规划：一家网店用热力图对比能力成熟度与战略重要性，为薄弱而重要的能力块投入资金 [1]。
  2. 网店收购竞争对手后的整合：交叉映射暴露出两套“Customer Management”实现 [1]。
  3. 界定转型范围：哪些能力是新增的（例如客服聊天机器人需要“Automated Customer Assistance”），哪些已经存在 [1]。
  4. 应用组合评审：按能力叠加应用，显示缺口和重叠（派生视图）。
  5. 团队设计：按业务能力组建长期稳定的团队 [7]。
- **何时不用：** 问题是顺序、时间或交接（A2、A5、E4）；问题是系统结构（C 族）；内容是某个项目的功能待办列表（B 族）。如果没有达成一致的定义且本周就要决策，一张带定义的单层图胜过一张层级很深但有争议的图。
- **与相邻类型对比：**
  - 当问题是价值如何逐阶段到达干系人时，选择 **A2 价值流**；两者通常会做交叉映射 [5]。
  - 当问题是步骤、网关或交接时，选择 **A5 BPMN 流程**。
  - 当问题是“谁”时，选择 **A3 业务上下文**（或干系人地图）；能力 × 组织是一张矩阵，而不是合并成一张图。
  - 当读者需要看到系统时，选择 **C1 应用全景图**；能力到应用的叠加是派生视图，必须如此标注。
  - 当问题是“由哪些部分组成”时，选择 **A7 概念架构**：架构展示组件，而一份功能清单则是能力图。
  - 当问题是变化何时发生时，选择 **A8 目标架构与路线图**；现状与目标态的成熟度热力图可作为它的输入。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式或非正式：** ArchiMate 提供正式的 Capability 元素（带阶梯图标的圆角矩形）和 Capability Map viewpoint [3][8]。常见的业务呈现方式是一种惯例：嵌套的方块、无箭头、可选颜色叠加。TOGAF 和 BIZBOK 规定的是内容规则，而非图形 [1][4]。
- **必需：**
  - **能力块：** 每个能力块都有基于业务对象的名称，并在目录中有书面定义，通常写作“Ability to …”（……的能力）[4]。
  - **以嵌套表示层级：** 第 1 层能力块包含其第 2 层子能力；每页 2–3 层 [3]。
  - **第 1 层分层**为若干层带，通常是 *Strategic*（战略类，定方向）、*Core / customer-facing*（核心 / 面向客户）和 *Supporting*（支撑类）[1][4]。TOGAF 指出，不分层的大型模型难以阅读 [1]。
  - **标题**写明范围（企业或单元）和状态（现状或目标态）。
- **可选：**
  - **热力图叠加层**，附图例。TOGAF 的评估维度：成熟度（绿 = 达到期望水平，黄 = 差一级，红 = 差两级或以上，紫 = 期望具备但尚不存在）、战略贡献、绩效、收入贡献、成本贡献、覆盖度、关键性 [1]。每张图只用一个维度。
  - **交叉映射作为单独视图：** 能力 × 组织单元（矩阵）、能力 × 价值流阶段（A2）、能力 × 应用（叠加）。
  - **ArchiMate 呈现：** 能力通过组合（composition）或聚合（aggregation）嵌套；该视点允许使用 Resource 和 Outcome 元素 [3]。
- **连线：** 业务呈现中不画连线；包含即表示分解。ArchiMate 允许能力之间的 *serving*（服务）关系以及由核心元素进行的 *realization*（实现）关系 [3]；这些不要放到面向高管的图上。
- **命名：** 名词、复合名词或动名词（“Order Management”“Market Development”）[1][3]。BIZBOK 模式：对象加动作名词，例如第 1 层“Customer Management” → 第 2 层“Customer Definition”“Customer Matching”“Customer Information Management”[4]。不用部门名称 [1]，不用系统名称（“CRM”是应用；“Customer Management”才是能力）。
- **文字量：** 每个能力块约 2–5 个词；定义放在目录中。同级能力块应是同一类事物、处于同一层级。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **先定义，再画图。** 为每个能力命名并定义，然后把它分解为实现它的角色、流程、信息和工具来检验；以此确认它是能力，而不是流程、职能或服务 [1]。先梳理业务对象，再梳理对它们的动作，最后做分解 [4]。
2. **整个企业一张图，每个能力只出现一次，** 即使有多个单元在执行它。多处执行的情况放在能力 × 组织交叉映射中呈现 [1][4]。
3. **与高层领导自上而下构建，再自下而上细化。** 第 1 层要足够精简，以便高层领导审定 [1]。
4. **把热力图当作决策辅助工具：** 一个明确的评估标准、一个刻度，以及日期或数据来源。同一个模型可以生成不同的热力图 [1]。
5. **以稳定的能力图为锚点**，与价值流 [5]、组织单元、应用和举措做交叉映射 [1][6]。

### 反模式
1. **把组织架构图改个标签当作能力。** TOGAF 指出这是常见错误 [1]。
2. **把系统清单当作能力**（以“CRM”“Data Lake”作为能力块）。如果只由 IT 来命名，模型读起来就像一份换了好听标签的系统清单 [9]。
3. **把流程或步骤当作能力**（“Approve refund”）；动宾结构的步骤属于价值流或流程 [1][3]。
4. **重复或相互重叠的同级能力，** 或同一行混入不同种类（能力旁边是团队，再旁边是步骤）[4]。
5. **热力颜色没有图例或评估标准，** 多个维度共用一个色阶，或仅以红/绿作为唯一提示 [1]。另外，避免一页超过 3 层 [3]，也避免在能力块上写“TBD”或工作笔记。

## 范例 {#exemplars}
<!-- skill: omit -->
- [TOGAF Series Guide: Business Capabilities (G189, mirror PDF)](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf) — “ABC Company”第 1 层模型，含战略/核心/支撑分层、以紫色标示缺失能力的成熟度热力图，以及能力 × 组织表。© The Open Group；仅供阅读。
- [Business Architecture Guild reference-model workshop deck](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf) — 以紧凑形式呈现分层图、分解模式和 BIZBOK 原则。© Business Architecture Guild。
- [ArchiMate 3.2 Reference Cards](https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf) — 正式的 Capability 表示法。© The Open Group。
- [Bizzdesign: Business capabilities vs. business functions](https://bizzdesign.com/blog/capabilities-vs-business-functions-same-difference) — 一张高层级的保险业能力图，以及对能力与职能区别的细致说明。厂商博客。
- [SAP LeanIX: Business capability map examples and templates](https://www.leanix.net/en/wiki/ea/business-capability-map-examples-and-templates) — 若干行业的 L1/L2 版式，展示典型的能力块密度 [10]。厂商内容。
- [Martin Fowler bliki: Business Capability Centric](https://martinfowler.com/bliki/BusinessCapabilityCentric.html) — 不是一张图，但展示了能力图在团队设计中的下游用途。

## 绘制方法 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定范围、状态和评估维度，并写进标题，例如“Online shop: business capabilities, current maturity”（网店：业务能力，当前成熟度）。
2. 先起草目录（分层、层级、名称、“Ability to …”定义）；去掉组织、系统和步骤名称以及重复项；画图前先给用户确认。
3. 版式：自上而下三条横向层带（Strategic、Core、Supporting）；第 1 层能力块是各层带内的容器，第 2 层能力块在其中排成网格。最多 3 层；叶子能力块超过约 60 个时，每个第 1 层领域单独一页。
4. 同级能力块大小一致，网格对齐；除非图例说明，否则大小不表达任何含义。
5. 文字：每个能力块 2–5 个词；图上不放项目符号、定义或不常见的缩写。
6. 颜色：中性填充，各层带用浅色调区分；热力图只用一个色阶，外加最多一个额外类别（“期望具备但尚不存在”），图例注明评估标准和来源/日期，并为色盲读者提供文字或图案提示。
7. 不画箭头。交叉映射（价值流、组织、应用）作为单独的图；应用叠加图标注“derived view”（派生视图）。

**自检清单**
- [ ] 每个能力块都是能力：业务对象加动作名词，不含系统、组织单元或步骤。
- [ ] 每个能力只出现一次；同级能力不重叠，且属于同一类、同一层级。
- [ ] 第 1 层已分层；可见层级最多 3 层。
- [ ] 标题写明范围和现状/目标态；没有重复说明图类型的副标题，没有版本标签。
- [ ] 热力颜色有图例，注明评估标准、刻度和来源；只用一个维度。
- [ ] 能力块上没有箭头、项目符号、“TBD”或推理说明文字。
- [ ] 每个能力在配套目录中都有定义。
- [ ] 任何应用叠加都标注为派生视图；基础图不含系统。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **候选能力：** 领域或限界上下文（bounded context）目录（`catalogue/`、`cart/`、`payment/`）、路由和菜单定义、特性开关名称、部署清单中的服务名称、CODEOWNERS、issue 标签和 epic、埋点事件族、README 中的功能概述。把每一项映射为业务对象名词；去掉技术模块（auth、logging）。
- **应用叠加：** 哪些仓库或服务实现了哪个能力。
- **必须来自人：** 没有软件支撑的能力（Brand Management、Supplier Management）、定义和分层、哪些能力具有战略意义、成熟度和投资评分、目标态能力。
- 任何从代码推导出的清单都标注为“candidate, to validate with the business”（候选，待业务确认）。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 范围和状态：整个企业、一个单元还是一个产品领域；现状、目标态还是两者？（一个单元，现状）
2. 这张图要支持哪项决策：投资、整合、转型范围还是团队设计？（投资，由此确定热力图维度）
3. 是否有现成的能力清单或参考模型需要对齐？（根据文档和访谈起草一份，标注为候选）
4. 画几层？第 1 层是否分为 Strategic / Core / Supporting？（2 层，分层）
5. 如果做热力图：用哪一个评估标准和刻度，由谁评分，截至何时？（成熟度，TOGAF 四色刻度，注明日期）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A1.json` · 版式模板：`layered` · 分层成为 `layer` 分组（层带），第 1 层能力成为其中带标题栏的分组，第 2 层能力是网格中大小一致的节点；热力值映射到样式令牌，并自动生成图例。

## 来源 {#sources}
<!-- skill: omit -->
1. TOGAF Series Guide: Business Capabilities (G189, June 2018), The Open Group (mirror PDF) — https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf — 访问于 2026-10-14
2. The Open Group, TOGAF Series Guide: Business Capabilities, Version 2 (G211, 2022; supersedes G189; part of TOGAF 10) — https://publications.opengroup.org/g211 — 访问于 2026-10-14
3. ArchiMate 3.1 Specification (C197, 2019), §7.3.1 Capability, §8.3.2 Business Function, App. C.3.2 Capability Map Viewpoint (mirror PDF; the elements cited are unchanged in 3.2) — https://university.sk/wp-content/uploads/2020/01/ARCHIMATE_v3_1_specifikacia.pdf — 访问于 2026-10-14
4. Business Architecture Guild, "Business Architecture Reference Model Workshop" (2019; BIZBOK Guide principles and patterns) — https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf — 访问于 2026-10-14
5. TOGAF Series Guide: Value Streams (G178, republished 2022 for TOGAF 10) — https://publications.opengroup.org/g178 — 访问于 2026-10-14
6. Bizzdesign, "Business capabilities vs. business functions: Same difference?" — https://bizzdesign.com/blog/capabilities-vs-business-functions-same-difference — 访问于 2026-10-14
7. S. Narayan, "Business Capability Centric", martinfowler.com bliki (2016) — https://martinfowler.com/bliki/BusinessCapabilityCentric.html — 访问于 2026-10-14
8. ArchiMate 3.2 Specification Reference Cards (N221, 2022) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — 访问于 2026-10-14
9. Capstera, "Common Business Capabilities: A Practitioner's List" — https://capstera.com/knowledge-hub/articles/list-of-common-business-capabilities — 访问于 2026-10-14
10. SAP LeanIX, "Business Capability Map Examples & Templates" — https://www.leanix.net/en/wiki/ea/business-capability-map-examples-and-templates — 访问于 2026-10-14
11. The Open Group / OMG BASIG, "Advancement of Business Architecture in the TOGAF Standard" (TOGAF 9.2 Phase B artifacts: Business Capability Map, Business Capabilities catalog) — https://www.omg.org/cgi-bin/doc?basig%2F18-09-03.pdf= — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A1 示例：网店业务能力，按 Strategic、Core、Supporting 分层，叠加当前成熟度热力图](/samples/A1-capability-map.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
