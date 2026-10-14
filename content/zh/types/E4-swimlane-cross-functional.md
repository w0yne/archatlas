---
code: E4
slug: swimlane-cross-functional
family: E
names:
  en: Swimlane / Cross-functional Flowchart
  zh: 泳道流程图
  aliases:
    en: [swimlane diagram, swim-lane flowchart, cross-functional flowchart, Rummler-Brache diagram, functional flowchart, functional bands (Visio 2007)]
    zh: [泳道图, 跨职能流程图, 跨部门流程图, 职责流程图]
question: "在这个流程中，每一步由哪个角色或系统执行？工作或信息在哪里从一方传递到另一方？"
audiences: [流程负责人, 业务分析师, 开发人员, 测试人员, 运维人员]
level: logical
phases: [discovery, design, review]
scope: "一个从触发到结果的流程，最多约 6 条泳道、20 个步骤，只画主成功路径"
formal:
  kind: convention
  ref: "Informal cross-functional flowchart (Rummler-Brache tradition); formal equivalents are BPMN 2.0.2 pools and lanes and UML 2.5.1 activity partitions"
neighbours: [A5, E1, E2, A6, C3]
status: draft
translationOf: en/types/E4-swimlane-cross-functional.md
sourceRev: 674f366
reviewed: false
---

# 泳道流程图（Swimlane / Cross-functional Flowchart）

> 把流程图划分为并行的泳道，每个角色或系统一条，使它们之间的每一次交接都清晰可见。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **要回答的问题：** 在这个流程中，每一步由哪个角色或系统执行，工作或信息在哪里从一方传递到另一方？
- **视点：** 流程之上的职责分配。Rummler 和 Brache 关注的是“组织架构图上的空白地带”：大多数延误、差错和归属缺口都出现在职能之间的交接处，而泳道让每一次交接都可见 [1][2]。在软件工作中，泳道往往是系统或服务；这时图展示的是各系统自身的步骤以及它们之间的集成点。一个轴是随时间推进的顺序，另一个轴是参与者 [9]。
- **起源：** 源于 20 世纪 40 年代的多栏流程图；“泳道（swim lane）”一词由 Geary Rummler 和 Alan Brache 在《Improving Performance》（1990）中推广；iGrafx 把它引入计算机建模，并于 1996 年注册了该术语商标；Visio 2007 把泳道称为“functional bands”[1][2][3]。
- **不包含：** 消息级细节和时序（E1）、业务级语义，如事件、网关以及代表不同组织的池（A5）、单个参与者内部的复杂逻辑（E2），以及结构（C 系列）。
- **本站采用的定义：** E4 是*非正式的*跨职能流程图（cross-functional flowchart）：在泳道中使用普通流程图形状 [8]。同样的思路在正式表示法中对应 BPMN 的池（Pool）和泳道（A5），以及 UML 活动分区，后者“用泳道表示法呈现”（即带分区的 E2）[4][7]。
- **版本说明：** BPMN 2.0.2 是 OMG formal/13-12-09；据称 ISO/IEC 19510:2013 版与 BPMN 2.0.1 相同，而非 2.0.2 [4]。这一点来自二手综述，未阅读 ISO 原文。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 流程负责人、分析师、开发人员、测试人员和运维人员。是连接业务与 IT 的良好桥梁。
- **典型场景：**
  1. 订单履约：顾客、网店 Web 应用、支付服务商和仓库，从“下单”到“订单已发货”。
  2. 两个应用之间的集成：各系统自身的步骤加上交换点，相当于两个 BPMN 池加消息流。
  3. 跨客服、财务和支付服务商的退款审批。
  4. 跨客服、研发和供应商的事故处理或值班流程。
  5. 现状与目标态的改进对比：统计交接次数，去掉不必要的交接 [2]。
- **不适用的情况：** 超过约 6 条泳道，或流程每一步都跨泳道（合并泳道或拆分流程）；重点是调用与返回的顺序（E1）；整个流程都在一个参与者内部（E2）；自动化或合规要求使用标准（A5）。
- **选 E4 还是 A5（唯一的规则）：** 当主角是业务角色，且表示法必须为业务负责人或工具承载 BPMN 语义（事件、网关、作为参与方的池、消息流）时，选 **A5 BPMN 流程图**。要为工程师画一张轻量的交接图，尤其是以系统为泳道时，选 **E4**。A5 是同一种图的正式兄弟，而不是同一种图。
- **与相邻类型的区别：**
  - 重点是调用顺序以及同步与异步时，选 **E1 时序图**；每个参与方内部的步骤和判断重要时，选 E4。
  - 泳道只是附带、逻辑才是重点时，选 **E2 活动图**；带分区的 E2 在形式上就是同一种图。
  - 顾客情绪和触点重要时，选 **A6 旅程图**（它有自己的可见线）。
  - 表达静态结构而非流程时，选 **C3 容器图**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 非正式约定，与流程图和 BPMN 的用法保持一致 [6][8][9]。
- **必需元素：**
  - **泳道：** 平行的条带，每条标注一个角色、团队或系统，且层级一致。
  - **开始和结束**（端点）。
  - **步骤：** 矩形，以“动词+名词”命名，放在执行者所在的泳道中。
  - **流程箭头，** 以及用菱形表示、出口带标签的**判断**。
- **交接语义：** 跨越泳道边界的箭头表示工作或信息的交接。在 BPMN 中，顺序流只在一个池内，消息流（虚线）连接不同的池；绝不要在池之间画顺序流 [4][5][6]。在非正式的 E4 中，要一致地标示跨系统交互，例如用虚线箭头并标注所传递的数据。
- **可选元素：** 池（按组织或系统归组的泳道组）、顶部的阶段列、文档或数据符号、等待/定时标记、面向业务读者的小型“示例”卡片（输入、证据、输出）。
- **方向：** 最常见的是横向泳道、时间从左到右，适合屏幕；纵向泳道适合竖长的页面 [1][9]。选定一种并保持一致。
- **命名：** 泳道是角色或系统，不是具体的人；步骤标签由一个动词和一个名词组成 [9]。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **展示工作的流转并保持简洁。** 颜色要少，方框尺寸一致，时间沿一个轴、参与者沿另一个轴 [9]。
2. **箭头顺着流向连接到方框的侧边；** 避免连接到顶部和底部，那会让流程变复杂 [9]。
3. **排列泳道以尽量减少交叉：** 发起方在前，其余参与者按参与顺序排列；交互频繁的系统相邻放置。
4. **在每次交接上标注传递的内容**（文档、请求、事件）。问题就出在交接处 [1][2]。
5. **不要强行塞进一页。** 如果必须一页，先画一张更高层级的范围模型 [9]。只画主成功路径，把错误放到单独的图中。

### 反模式
1. **泳道层级混杂：** 角色、团队和系统出现在同一张图中。
2. **步骤放错了泳道，** 或某条泳道里没有任何步骤。
3. **长线在页面上来回折返，** 而不是重新排列泳道。
4. **跨泳道箭头没有标签，** 或使用了 BPMN 符号却不遵守 BPMN 规则（在池之间画顺序流）。
5. **把日历或时间轴刻度与步骤顺序混在一起，** 超过约 6 条泳道，或流程每一步都在泳道之间来回穿梭。泳道数和步骤数是从业者的经验法则，不是标准。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Wikipedia, "Swimlane"](https://en.wikipedia.org/wiki/Swimlane) — 简明的历史，以及横向与纵向布局的理由。CC BY-SA。
- [Mindtools, "Swim Lane / Rummler-Brache Diagrams"](https://www.mindtools.com/abxyani/swim-lanerummler-brache-diagrams/) — 从管理角度阐述职能之间的空白地带。
- [Microsoft Support, "Create a cross-functional flowchart"](https://support.microsoft.com/en-us/visio/create-a-cross-functional-flowchart) — 业务工具中事实上的约定，包含阶段和泳道。
- [Lucid: swimlane diagram tips with Alec Sharp](https://lucid.co/blog/webisodes-with-alec-sharp-swimlane-diagrams) — 关于坐标轴、“动词+名词”标签和箭头连接方式的从业者规则。
- [BPM Tips, "BPMN in practice: pools and lanes"](https://bpmtips.com/bpmn-in-practice-pools-and-lanes/) — 池和泳道的常见错误；把 E4 升级为 A5 时很有用。
- [uml-diagrams.org, UML Activity Diagrams](https://www.uml-diagrams.org/activity-diagrams.html) — 同一概念的活动分区形式，适合以软件为中心的团队。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定流程边界（从触发到结果）和泳道粒度：角色、团队或系统，绝不混用。最好不超过 6 条泳道。两者都写进标题，例如“下单与发货，主成功路径”。
2. 把步骤列成表格（步骤、执行者泳道、输入、输出、下一步）；对照代码或文档核实系统步骤；绘图前先给用户看。
3. 方向：默认横向泳道、时间从左到右；只有竖长的文档才用纵向。
4. 排列泳道以尽量减少交叉。如果两个独立系统之间有交互，把它们画成相邻的泳道组（池），并带有可见的边界。
5. 按时间顺序逐列放置步骤；并行步骤对齐在同一列；每个判断放在做出判断者的泳道中。
6. 交接：跨泳道边界画一条短箭头，标注传递的内容；跨系统消息使用不同的样式（虚线），并在图例中说明。
7. 文字：步骤最多 5 个词，泳道标签最多 3 个词；如有示例卡片，放在主流程之外并标注“示例”。
8. 颜色：泳道用中性色交替着色；最多一种强调色，用于跨边界交接或重点系统。

**自检清单**
- [ ] 每条泳道是同一层级上的一个参与者（全部是角色，或全部是系统）。
- [ ] 每个步骤都位于其执行者的泳道中。
- [ ] 每个跨泳道箭头都是真实的交接，并写明传递的内容。
- [ ] 时间沿一个轴推进；没有向后折返或绕远路的线。
- [ ] 判断的出口都有标签；开始和结束都明确标出。
- [ ] 最多约 6 条泳道和 20 个步骤，否则拆分流程。
- [ ] 如使用 BPMN 符号，则遵守 BPMN 规则（消息流只在池之间）；否则考虑 A5。
- [ ] 只画主成功路径，或把错误处理明确分开。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **系统泳道：** 通过入口点、Dockerfile 和基础设施即代码找到的可运行单元（服务、worker、函数）。
- **步骤：** 处理器、作业和工作流阶段定义（YAML、Step Functions、Airflow）。
- **交接：** 队列和主题的生产者与消费者、出站 HTTP 客户端、webhook、文件投递。
- **人员泳道：** UI 路由、管理页面、审批端点、权限检查中的角色。
- **必须来自人：** UI 操作背后的组织角色、人工步骤、等待时间，以及每次交接的业务含义。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 哪个流程，从什么触发到什么结果？一个场景还是多个变体？（最常见的单个场景）
2. 泳道是什么：角色、团队还是系统；两个系统是否应分为独立的池？（系统，独立的系统各自成池）
3. 为流程负责人或自动化使用严格的 BPMN，还是普通的跨职能流程图？（普通流程图，并提出可升级为 A5）
4. 交接上是否标注传递的数据或文档；是否为业务读者添加示例卡片？（标注交接，不加卡片）
5. 只画主成功路径还是包含异常；画现状流程还是目标流程？（主成功路径，现状）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/E4.json` · 布局模板：`lanes` · 泳道是 `lane` 分组（独立系统用 `pool` 分组包住各自的泳道），步骤和判断是节点，`parent` = 所在泳道，流程箭头是边（`call`），跨系统交接使用 kind `message`，并用 `label` 写明传递的内容。

## 来源 {#sources}
<!-- skill: omit -->
1. Wikipedia, "Swimlane" — https://en.wikipedia.org/wiki/Swimlane — 访问于 2026-10-14
2. Mindtools, "Swim Lane/Rummler-Brache Diagrams" — https://www.mindtools.com/abxyani/swim-lanerummler-brache-diagrams/ — 访问于 2026-10-14
3. Lucen Software, "Swimlane diagram – definitions, uses, examples" — https://www.lucensoftware.com/swimlane-diagram — 访问于 2026-10-14
4. OMG, "About the Business Process Model and Notation Specification Version 2.0.2" — https://www.omg.org/spec/BPMN/2.0.2/About-BPMN — 访问于 2026-10-14
5. BPM Tips, "BPMN in practice — pools and lanes" — https://bpmtips.com/bpmn-in-practice-pools-and-lanes/ — 访问于 2026-10-14
6. HEFLO, "BPMN Pools vs Lanes Explained" — https://www.heflo.com/blog/bpmn-pools-and-lanes — 访问于 2026-10-14
7. uml-diagrams.org, "UML Activity Diagrams"（作为泳道的活动分区）— https://www.uml-diagrams.org/activity-diagrams.html — 访问于 2026-10-14
8. Microsoft Support, "Create a cross-functional flowchart" — https://support.microsoft.com/en-us/visio/create-a-cross-functional-flowchart — 访问于 2026-10-14
9. Lucid, "Webisodes with Alec Sharp: Swimlane Diagrams Tips, Tricks, and Best Practices" — https://lucid.co/blog/webisodes-with-alec-sharp-swimlane-diagrams — 访问于 2026-10-14
10. A. Sharp, P. McDermott, *Workflow Modeling*（Google Books；[9] 中实践所依据的背景书籍，未直接阅读）— https://books.google.com/books/about/Workflow_Modeling.html?id=avcWp_0ZMyoC — 访问于 2026-10-14

## 示例图 {#sample}
<!-- skill: path only -->
![E4 示例：网店订单履约，跨客户、网店 Web 应用、支付服务商和仓库四条泳道，交接均带标签](/samples/E4-swimlane-cross-functional.svg)
*示例图待生成（由渲染器根据 `examples/` 生成）。*
