---
code: A2
slug: value-stream
family: A
names:
  en: Value stream (business architecture)
  zh: 价值流（业务架构）
  aliases:
    en: [value stream diagram, value stream stages, value stream capability cross-map, value stream, value stream map (TOGAF artifact), value stream / capability cross-map]
    zh: [价值流阶段图, 价值流能力映射, 价值流, 价值流阶段, 价值流—能力映射]
question: 对一个触发干系人而言，价值如何逐阶段累积？每个阶段由哪些能力支撑？
audiences: [leaders, business, architects]
levels: [strategy]
phases: [initiate]
scope: 一条价值流：一个触发干系人、一个价值主张和约 4–8 个阶段，可选在每个阶段下方交叉映射能力
formal: {kind: standard, ref: 'ArchiMate 3.2 Value Stream element and Value Stream viewpoint; TOGAF Series Guide: Value Streams (G178, republished 2022 for TOGAF 10); BIZBOK Guide'}
neighbours: [A1, A5, A6, A9]
status: draft
translationOf: en/types/A2-value-stream.md
sourceRev: a5d2191
reviewed: false
---

# 业务架构价值流（Value Stream）

> 一行从左到右排列的价值阶段，展示触发干系人如何最终获得所承诺的价值；支撑能力堆叠在下方，不标注任何时间。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 企业如何逐阶段地向某一干系人交付价值？每个阶段由哪些能力支撑？价值“always defined from the perspective of the stakeholder”（始终从干系人的角度定义）[1]。
- **视点：** ArchiMate *Value Stream viewpoint*：“a structured overview of a value stream, the capabilities supporting the stages in that value stream, the value created, and the stakeholders involved”（对一条价值流、支撑其各阶段的能力、所创造的价值及相关干系人的结构化概览）（业务经理和架构师；设计与决策；范围：战略）[6]。TOGAF 阶段 B；制品为 *Value Stream Map*（图）、*Value Stream Stages catalog*（目录）和 *Value Stream/Capability matrix*（矩阵）[1][5]。没有对应的 C4 model 层级。
- **深层含义：** 在商业模式层面展示企业的“动态”面貌，与 A1 业务能力图（“静态”面貌）互为搭档 [2][6]。一个阶段可以映射到多个流程，一个流程也可以实现多个阶段 [1][6]。干系人在每个阶段之后都可能停下，因此退出条件比箭头更重要 [1]。
- **不包含：** 决策与网关、每个步骤的角色、系统、持续时间、等待时间和异常。
- **本站采用的定义：** 价值流是“an end-to-end collection of activities that create a result for a customer, who may be the ultimate customer or an internal end-user”（为客户创造结果的端到端活动集合，客户可以是最终客户，也可以是内部最终用户）（BIZBOK）[2]；ArchiMate 的定义是“a sequence of activities that create an overall result for a customer, stakeholder, or end user”（为客户、干系人或最终用户创造整体结果的一系列活动）[6]。“value stream map”一词还有另外两种含义：一是带处理时间和等待时间的**精益价值流图**（Lean value-stream map），有单独的页面（A9）；二是 SAFe 的运营价值流和开发价值流 [9]。TOGAF 和 Business Architecture Guild 都声明其价值流不是精益价值流 [1][2]。切勿在这张图上标注时间。
- **版本说明：** TOGAF 指南编号为 G178，2022 年作为 TOGAF 10 的一部分重新发布 [4]。Value Stream 元素自 ArchiMate 3.1（2019）起存在 [8]；本页依据 3.2。ArchiMate 4（2026 年 4 月发布）尚未对照现行规范原文核实。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 高管、业务架构师和企业架构师、投资组合与战略负责人。
- **典型场景：**
  1. 界定网店平台重构的范围：面向顾客的“Fulfil Customer Order”，阶段为 Discover Product → Place Order → Settle Payment → Fulfil Order → Deliver Goods（模式参照 TOGAF 的“Acquire Retail Product”[1]）。
  2. 找出薄弱的支撑能力：对每个阶段下的能力做热力图，例如 Fulfil Order 下标红的“Inventory Management”[1][3]。
  3. 顾客支持：“Resolve Customer Query”，由顾客触发，客服聊天机器人和客服人员是参与干系人，终点为“Customer issue resolved”。
  4. 由员工或合作伙伴触发的内部价值流，例如面向仓库的“Onboard Supplier”（参见 TOGAF“Recruit Employee”）[1]。
  5. 基于能力的规划：带能力热力图的阶段作为 A8 路线图的输入。
- **何时不用：** 详细工作流、SLA 或某个团队的操作规程（A5、E2）；时间、浪费或等待分析（A9）；系统结构（C 族）；异常和分支（A5、E 族）。
- **与相邻类型的区别：**
  - 关注“有哪些能力、水平如何”时，选择 **A1 业务能力图**；两者通过交叉映射结合 [1][3]。
  - 问题是当前运营流程中的时间和浪费在哪里时，选择 **A9 精益价值流图**。
  - 关注一个案例的任务顺序、决策、角色或异常时，选择 **A5 BPMN 流程** [6]。
  - 关注客户体验（情绪、触点）时，选择 **A6 旅程图**；A2 讲的是企业如何交付价值，由外向内，但不涉及体验。
  - 关注变化何时发生时，选择 **A8 目标架构与路线图**；带能力热力图的 A2 是它的输入。
  - 波特价值链（Porter value chain）是关于基本活动和支持活动的经济学视图，不是干系人价值流 [1][2]。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式或非正式：** ArchiMate 表示法是正式的（V 形箭头状的 Value Stream 元素，阶段之间为 *flow*（流）关系，能力 *serve*（服务）阶段）[6][7]。BIZBOK 和 TOGAF 的呈现方式是 V 形箭头加阶段表，能力堆叠在每个阶段下方：内容是标准的，图形是惯例 [1][2]。
- **必需的表头：** 价值流**名称**，采用动宾结构、主动语态，以发起干系人的口吻来写（“Fulfil Customer Order”）[1][6]；简短**描述**；**触发干系人**（“there must be a clearly defined triggering stakeholder”，必须有明确定义的触发干系人）[1]；以干系人语言表述的**价值主张** [1][2]。
- **每个阶段必需**（TOGAF 的六要素 [1]）：两到三个词的名称；描述；参与干系人；进入条件（触发该阶段的条件或状态变化）；退出条件（即下一阶段的进入条件）；价值项（新增的价值）。
- **阶段数量：** 约 4–8 个；保持简洁，不要深入到操作细节 [1]。
- **箭头：** 从左到右首尾相接的 V 形箭头，或 ArchiMate 阶段之间的 *flow* [6]。它们表示价值移交，而非控制流。不画网关或分支。
- **可选的能力交叉映射：** 能力堆叠在每个阶段下方；在 ArchiMate 中能力 *serve* 该阶段，可用分组（grouping）使图更紧凑 [6][8]。热力图只用于能力，绝不用于阶段 [1][3]。
- **可选的结果：** 价值流 *realizes*（实现）一个 Outcome；从最后一个阶段画 flow 到结果是元模型错误 [10]。
- **可选的阶段表：** 放在阶段行下方（进入条件、退出条件、价值项、干系人），使 V 形箭头保持简短。
- **图例：** 只要能力带有热力颜色就需要图例（评估标准、刻度、来源）。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **先从外部、由客户触发的价值流入手**，再做内部价值流 [1]。
2. **先明确干系人和价值，** 再定义阶段 [1][2]。
3. **把进入条件和退出条件写成可观察的状态变化**（“Order placed”“Payment authorised”），并让每个退出条件衔接下一个阶段的进入条件 [1]。
4. **先交叉映射能力，再做热力图**，以找出投资方向 [1][3]。
5. **价值流和能力一起起草；** TOGAF 指出：“one should not exist without the other for very long”（二者不应长期脱离对方而单独存在）[1]。

### 反模式
1. **在业务阶段上标注精益时间**（处理时间、等待时间、前置时间）。那是另一种图（A9）；TOGAF 指出精益 VSM 不适合做能力交叉映射 [1]。
2. **阶段过多或细到任务级**（检查、审批、发邮件），把价值流变成了流程 [1][6]。
3. **把组织单元当作阶段**（“Finance step”），或没有触发干系人 [1][2]。
4. **在价值流内部画分支或网关；** 应通过退出条件来表达中途停止的可能 [1]。
5. 在 ArchiMate 中**从最后一个阶段画 flow 到结果**（应使用 *realizes*）[10]；此外还有过长的回流线、未加说明的图标以及图上的工作笔记。

## 范例 {#exemplars}
<!-- skill: omit -->
- [TOGAF Series Guide: Value Streams (G178, mirror PDF)](https://governance.foundation/assets/frameworks/togaf/g178_2%20-%20Value%20Streams.pdf) — “Acquire Retail Product”和“Recruit Employee”，含完整阶段表和能力交叉映射；附录 A 比较了价值链、价值网络和精益 VSM。© The Open Group；仅供阅读。
- [Business Architecture Guild reference-model workshop deck](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf) — 价值流的构成（“Settle Claim” → “Claimant Made Whole”）、外部与内部触发、阶段模板。© Business Architecture Guild。
- [The Open Group blog: ArchiMate 3.1, the new version of the standard](https://blog.opengroup.org/2019/11/05/archimate-3-1-specification-the-new-version-of-the-standard) — 一张 ArchiMate 价值流交叉映射图，含阶段、价值流动以及实现某一结果的分组能力。© The Open Group。
- [SAFe: Operational Value Streams](https://framework.scaledagile.com/operational-value-streams) — 该术语在敏捷领域的含义，便于识别和区分。© Scaled Agile。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确认图类型：关注干系人、价值或能力 → 本页；关注时间、浪费或等待 → A9。不清楚就问。
2. 表头：动宾结构的名称、触发干系人、价值主张。标题要传达核心信息，例如“Fulfil Customer Order: shopper receives paid goods in five stages”（履行顾客订单：顾客经五个阶段收到已付款的商品）。
3. 以表格起草 4–8 个阶段（名称、进入条件、退出条件、价值项、参与方）；检查每个退出条件是否等于下一个阶段的进入条件。
4. 版式：一行大小相同的 V 形箭头，从左到右；干系人在左端，价值主张在右端；每个 V 形箭头 2–3 个词，不用项目符号。
5. 交叉映射（可选）：每个阶段一列，下方放 2–6 个能力块，使用 A1 中的名称；被多个阶段使用的能力以相同样式重复出现。
6. 颜色：阶段用中性色；热力颜色只用于能力块，并附图例（评估标准、刻度、来源）。
7. 进入条件/退出条件/价值项放在阶段行下方的紧凑表格或正文中，不要放进 V 形箭头里。

**自检清单**
- [ ] 图上任何地方都没有时间、持续时间或等待时间。
- [ ] 展示了触发干系人和价值主张；名称为动宾结构。
- [ ] 4–8 个阶段，名称为 2–3 个词；没有组织单元、任务或网关。
- [ ] 退出条件衔接下一个阶段的进入条件。
- [ ] 能力块使用 A1 中的名称；热力颜色有图例。
- [ ] 严格从左到右，没有回流线；图上没有工作笔记。
- [ ] 标题或图例写明现状或目标态。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **有限但有用：** 领域状态枚举和状态迁移（`OrderStatus: placed → paid → picked → shipped → delivered`）可提示进入条件和退出条件；埋点漏斗事件和路由顺序（catalogue → cart → checkout）可提示面向客户的阶段；README 和产品文档。
- **能力交叉映射：** 领域目录和服务可提示候选能力（见 A1）。
- **必须来自人：** 触发干系人、价值主张、价值项、哪些阶段重要以及所有热力图评分。从代码推导出的阶段标注为候选。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 问题是干系人价值和支撑能力，还是流程中的时间和浪费？（价值和能力；否则改用 A9）
2. 谁触发这条价值流？对他们而言“完成”意味着什么？（顾客；“收到正确的商品，且支付安全”）
3. 现状、目标态，还是两者？（现状）
4. 是否交叉映射能力？对照哪份能力清单？（是，若有 A1 能力图则对照它）
5. 是否对能力做热力图？用哪一个评估标准？（除非某项决策需要，否则不做热力图）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A2.json` · 布局模板：`tree` · 阶段是由边串联、排成一行从左到右的 `task` 节点；与某个阶段交叉映射的能力列在该节点的 `tags` 中。

## 来源 {#sources}
<!-- skill: omit -->
1. TOGAF Series Guide: Value Streams (G178, Oct 2017, updated Jun 2018), The Open Group (mirror PDF), incl. §2.1–3.1 and App. A.3 "Lean Value Stream" — https://governance.foundation/assets/frameworks/togaf/g178_2%20-%20Value%20Streams.pdf — 访问于 2026-10-14
2. Business Architecture Guild, "Business Architecture Reference Model Workshop" (2019; BIZBOK value stream definitions, anatomy, templates) — https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf — 访问于 2026-10-14
3. TOGAF Series Guide: Business Capabilities (G189, 2018), §4.2.2 Capability/Value Stream Mapping (mirror PDF) — https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf — 访问于 2026-10-14
4. The Open Group Publications, TOGAF Series Guide: Value Streams (G178; republished 25 Apr 2022; part of TOGAF 10) — https://publications.opengroup.org/g178 — 访问于 2026-10-14
5. The Open Group / OMG BASIG, "Advancement of Business Architecture in the TOGAF Standard" (TOGAF 9.2 Phase B catalogs, matrices, diagrams) — https://www.omg.org/cgi-bin/doc?basig%2F18-09-03.pdf= — 访问于 2026-10-14
6. ArchiMate 3.1 Specification (C197, 2019), §7.3.2 Value Stream, App. C.3.3 Value Stream Viewpoint (mirror PDF) — https://university.sk/wp-content/uploads/2020/01/ARCHIMATE_v3_1_specifikacia.pdf — 访问于 2026-10-14
7. ArchiMate 3.2 Specification Reference Cards (N221, 2022) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — 访问于 2026-10-14
8. "ArchiMate 3.1 Specification: The New Version of the Standard", The Open Group Blog (5 Nov 2019) — https://blog.opengroup.org/2019/11/05/archimate-3-1-specification-the-new-version-of-the-standard — 访问于 2026-10-14
9. Scaled Agile, "Operational Value Streams" and "Development Value Streams" — https://framework.scaledagile.com/operational-value-streams ; https://framework.scaledagile.com/development-value-streams — 访问于 2026-10-14
10. "The Value Management Platform and ArchiMate", CEUR-WS Vol-2574 (value stream realizes outcome) — https://ceur-ws.org/Vol-2574/paper2.pdf — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A2 示例：网店从购物者到收到商品的价值流](/samples/A2-value-stream.svg)
*网店的价值流：购物者触发五个“动词+名词”阶段（选择商品、下单、付款、打包、送货），最终交付的价值是“收到商品”。图上没有时间；带时间的是精益价值流图（A9）。*
