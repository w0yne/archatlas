---
code: B4
slug: scope-diagram
family: B
names:
  en: Scope diagram
  zh: 范围图
  aliases:
    en: [in-scope out-of-scope diagram, scope boundary map]
    zh: [范围内外图, 范围边界图]
question: "这项举措纳入或排除哪些内容？哪些外部依赖仍需要开展工作？"
audiences: [leaders, product, architects]
level: concept
phases: [initiate, requirements]
scope: system
formal:
  kind: convention
  ref: "Scope modeling — https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-41-scope-modelling/"
neighbours: [C2, A3, B1, D2, C6]
status: draft
sourceRev: a082cec
translationOf: en/types/B4-scope-diagram.md
reviewed: false
---

# 范围图（Scope diagram）

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
范围图回答：**一项举措纳入或排除哪些内容，哪些依赖影响这份约定？** 它关注变更和交付的责任范围，而不只是软件运行的位置 [1][2]。
**本站采用的定义：** 非正式的纳入／排除范围图，可配合上下文图使用。它不是 C4 model 系统上下文图或 DFD 的另一个名称。
支付服务商可以位于网店系统边界之外，但与它集成的工作仍属于结账项目范围。系统边界、交付边界、所有权边界和信任边界是不同事实。
上下文视图则描述主体及其环境：C4 model 上下文强调人员／系统；arc42 区分领域交换和技术通道；DFD 上下文强调跨越整个系统加工边界的数据 [3–6]。
范围图不表达详细行为、部署或完整接口契约。图本身不能证明干系人已经达成共识；应链接对应的决策基线。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 发起人、产品负责人、分析师、架构师，以及交付／集成团队。
- **场景：** 约定结账版本的纳入项；记录客服聊天机器人的排除项；估算前识别集成工作；比较现状与拟议范围；暴露未解决的边界决策。
- **何时不用：** 规定顺序、实现单元、防火墙规则，或表达整个企业全景。
- 需要表达单个系统直接相关的外部用户／依赖时，选择 **C2 系统上下文图**。
- 需要表达领域参与方和交换时，选择 **A3 业务上下文图**；需要技术通道／契约时，选择 **C6 集成关系／接口视图**。
- 需要数据源、数据接收方和转换时，选择 **D2 数据流图**；明确其上下文／分解层级编号。
- 需要参与者目标时，选择 **B1 用例图**；需要多个同级系统时，选择 **C1 应用全景图**。
- 范围图和上下文图可以配套使用；不要默默混合两者的边界与箭头含义。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **范围图核心：** 有名称的举措／发布版本及基线；纳入的能力／工作；明确排除项，或说明排除项尚未确定；说明边界含义 [1][2]。
- **可选：** 假设、未确定范围、前置依赖、负责人，以及验收／决策记录链接。
- **箭头：** 表达纳入／排除通常不需要箭头。若用来表示前置条件或依赖，应标明该关系；它不自动表示数据流。
- **上下文配图：** 命名单一主体和相关邻居；不要把所有外部系统都标成“项目排除项”。
- **C4 model 上下文：** 直接相关的人员／软件系统、带标签的单向关系和图例；不展示内部组件 [3][4]。
- **arc42 上下文：** 区分领域输入／输出与技术通道；选择技术关注点时才纳入相应技术细节 [5]。
- **DFD 上下文：** 一个加工代表整个系统；带名称的箭头沿数据流向，而不是控制顺序。内部功能／数据存储属于分解图；按选定约定可以表达外部数据存储 [6]。
- **编号：** Yourdon 将上下文之下的分解图称为 *Figure 0*；其他来源将上下文称为 *level 0*。应说明编号方案，不要把“DFD 0”当作无歧义名称 [6]。
- **图例与细节：** 若展示交付、系统、所有权和信任边界，应分别标识。标签简短，契约／假设放入配套表格。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- 对齐边界和变更基线；不要把作者的推断当作已接受的范围 [1][2]。
- 区分排除的能力与外部依赖；不要因为服务商在系统之外，就漏掉集成工作。
- 为上下文配图中的交换写出有意义的名称；避免没有说明的“连接到”连线 [3][4]。
- 分开业务和技术关注点；不要在 C4 model 上下文图中加入内部组件／协议细节 [3][5]。
- 分解 DFD 时保留上下文数据接口；避免层级编号不一致，或用箭头表达“下一步”[6]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [PMI，Three proven ways business analysts help prevent scope creep，图 2](https://www.pmi.org/learning/library/business-analysts-help-prevent-scope-creep-9352) — 已填入具体内容的产品上下文图，展示如何通过边界问题支持范围分析。**许可：** 未确认开放图片许可；仅提供链接。
- [arc42，HTML Sanity Checker 业务上下文](https://docs.arc42.org/examples/business-context-1/) — 图与邻居表共同明确外部交换和约束。**许可：** 页面声明 CC BY-SA 4.0；改编前核对具体资源条款，并保留署名及相同方式共享要求。
- [arc42，HTML Sanity Checker 技术上下文](https://docs.arc42.org/examples/technical-context-1/) — 同一个公开项目的技术配图，将通道／制品与领域交换区分开。**许可：** 页面声明 CC BY-SA 4.0；改编前检查各项资源。
- [C4 model，系统上下文图示例](https://c4model.com/diagrams/system-context) — 单系统视图和图例展示了相邻的上下文关注点。**许可：** 本次未核实具体资源的复用许可；仅提供链接。

这些是**用于范围讨论的上下文范例**，不是四张相同类型的纳入／排除图。arc42 的配套视图来自同一项目，不是独立案例。已查阅正文和图示描述；不声称做过视觉审查。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 选择交付范围或一种明确命名的上下文变体，说明受众和基线。
2. 确定举措／主体，解释其边界含义。
3. 收集已约定的纳入项、排除项、依赖和未解决决策。
4. 将外部系统的所有权与范围内的集成工作分开。
5. 绘制带标签的范围区域；上下文配图则以主体为中心，对相关邻居分组。
6. 使用简短标签、克制的颜色和明确的连线含义；契约放在表格中。
7. 核对证据和配套视图；记录分歧，不编造共识。

**自检清单**
- [ ] 已命名变体、主体／举措和基线。
- [ ] 交付、系统、所有权与信任边界有明确区别。
- [ ] 纳入／排除项有决策证据，或标为未确定。
- [ ] 外部依赖没有被误认为范围外的集成工作。
- [ ] 箭头方向和标签符合所选约定。
- [ ] 上下文细节与 DFD 编号适当且明确。
- [ ] 相关交换、假设、标签和连线端点清晰可读。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 处理程序、API 契约、外部客户端、事件和操作文档可识别候选交换。
- 部署／构建证据有助于定位所选系统内的实现，而不是确定项目范围。
- 需求、已接受的决策和发布计划确定纳入／排除项。
- 缺少代码不证明某项被排除；测试样例不等于生产依赖。
- 记录 `边界/元素/连线 | 路径:行号/章节 | 版本/环境 | verified/inferred/doc-only/conflict`。
- 用权威需求和所有权证据确认边界决策。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 决策关注交付承诺，还是系统环境？
2. 应展示哪项举措／哪个主体、哪个基线和哪种边界？
3. 哪些纳入项和排除项已经达成共识？
4. 哪些外部依赖带来集成工作或约束？
5. 受众是否还需要领域交换或技术通道？

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/B4.json` · 布局模板：`nested` · 范围区域是 `boundary` 分组（范围内；范围外，`dashed`；依赖，样式 `external`），其中包含 `component` 节点。
若节点和箭头描述的是运行中的系统边界，应另用上下文视图。

## 来源 {#sources}
<!-- skill: omit -->
1. IIBA — *BABOK Guide, 10.41 Scope Modelling* — https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-41-scope-modelling/ — 访问于 2026-10-14，通过官方索引摘要获取；未取得完整章节。
2. PMI — *Three proven ways business analysts help prevent scope creep* — https://www.pmi.org/learning/library/business-analysts-help-prevent-scope-creep-9352 — 访问于 2026-10-14；已查阅文章正文和图 2／3 的描述。
3. C4 model — *System context diagram* — https://c4model.com/diagrams/system-context — 访问于 2026-10-14。
4. C4 model — *Notation* — https://c4model.com/diagrams/notation — 访问于 2026-10-14。
5. arc42 — *Section 3: Context and Scope* — https://docs.arc42.org/section-3/ — 访问于 2026-10-14。
6. Ed Yourdon — *Just Enough Structured Analysis, Chapter 9*，2006-01-31 修订版，公开 PDF 镜像 — https://www.businessanalystlearnings.com/s/Yourdon-DFD.pdf — 访问于 2026-10-14；相关正文确认了上下文与 Figure 0 的区别，以及外部数据存储的限定说明。
7. arc42 — *Example Business Context: HTML Sanity Checker* — https://docs.arc42.org/examples/business-context-1/ — 访问于 2026-10-14。
8. arc42 — *Example Technical Context: HTML Sanity Checker* — https://docs.arc42.org/examples/technical-context-1/ — 访问于 2026-10-14。

## 示例 {#sample}
<!-- skill: path only -->
![B4 示例：一次结账版本的范围](/samples/B4-scope-diagram.svg)
*一次结账版本交付包含支付集成和订单确认，排除会员积分计划，并将外部服务商记录为依赖。*
