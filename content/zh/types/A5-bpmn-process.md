---
code: A5
slug: bpmn-process
family: A
names:
  en: Business process diagram (BPMN)
  zh: 业务流程图（BPMN）
  aliases:
    en: [BPMN diagram, BPMN collaboration diagram, BPMN process diagram, process map, swimlane process diagram, process flow diagram]
    zh: [BPMN 流程图, 业务流程建模图, BPMN 协作图, 业务流程图, 协作图]
question: 一项业务工作的单个实例如何从触发走到结果：每一步由谁完成，在哪里分支，又如何与外部参与方交互？
audiences: [business, product, developers]
levels: [concept, logical]
phases: [requirements, design]
scope: 一个业务流程（一类实例）在一个分解层级上的视图：参与方画为池，执行者画为泳道。
formal: {kind: standard, ref: 'OMG BPMN 2.0.2 (formal/13-12-09, Jan 2014); ISO/IEC 19510:2013 is identical to BPMN 2.0.1 (same notation)'}
neighbours: [A1, A2, A6, A9, E1, E2, E3, E4]
status: draft
translationOf: en/types/A5-bpmn-process.md
sourceRev: a5d2191
reviewed: false
---

# 业务流程图 / BPMN 泳道图（Business Process Diagram, BPMN）

> 用标准 BPMN 画出的一个业务流程：一个实例从触发出发，经过任务和网关，到达有名称的结束状态；池表示参与方，泳道表示执行者。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
BPMN 流程图回答的是：“一个订单、请求或案件如何从触发走到某个结果，每一步由谁完成？”按 ISO/IEC/IEEE 42010 的说法，它服务于行为（流程）视点。TOGAF 称之为流程图（Process Flow diagram），属于阶段 B 业务架构的制品 [12]。ArchiMate 把同一流程表示为单个业务流程（Business Process）元素，由 BPMN 展开细节 [13]。C4 model 没有流程层级。BPMN 本身不涵盖组织模型、功能分解、数据模型、战略和业务规则，并且“不是数据流语言” [2 §7.2]。

**本站采用的定义：**当前版本为 **BPMN 2.0.2**（OMG，2014 年 1 月）[1]。ISO/IEC 19510:2013 与 **BPMN 2.0.1** 相同，而非 2.0.2；两者表示法一致，2.0.2 只增加了澄清说明 [3]。**池（Pool）**是一个参与方（participant，即独立的一方或流程）。**泳道（lane）**是一个池内部的划分（角色、部门或系统）[2 §10]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：**流程负责人、分析师、运营人员、审计人员；以及对流程做自动化或验证的开发与测试人员。高管只需要一页由折叠子流程组成的顶层图。
- **场景：**现状 / 目标态流程再设计；网店从下单到发货，顾客和支付服务商作为外部池；划定自动化范围（用户任务与服务任务）；推导验收测试（从开始到某个结束状态的一条路径 = 一个测试）。
- **不适用的情况：**读者需要的是业务*做什么*（A1、A2）；问题关乎客户体验（A6）；流程主要是系统间调用（E4、E1）；工作属于非结构化的案件处理；或者流程很简单而读者从未接触过 BPMN。
- **与相邻类型的区别：**
  - 问题是存在哪些价值阶段、不涉及控制流和角色时，选 **A2 价值流**。
  - 关注客户体验时选 **A6 旅程图**；A5 是其背后的组织逻辑。
  - 泳道是系统、读者是工程师时，选 **E4 泳道流程图**。A5 有形式化语义（池、消息流）；E4 只是非正式约定。
  - 软件各部分之间的精确消息顺序选 **E1 时序图**，单个对象的生命周期选 **E3 状态机图**。
  - 只有一个执行者、5–8 个步骤，或读者不熟悉 BPMN 时，选**普通流程图**（ISO 5807 [14]）。
  - 问题是交付过程中等待时间积压在哪里（精益价值流图），而不是谁做哪一步时，选 **A9**。
  - 读者不需要 BPMN 的池、事件或消息流，只需要一段流程的普通流程图时，选 **E2**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **图的种类：***流程*图（一个池含若干泳道）或*协作*图（多个池由消息流相连）；*编排*图（Choreography）很少面向业务读者使用 [2 §7.4]。
- **必需：**开始事件（细线圆），标注其触发；任务（圆角矩形，动词 + 宾语）；排他（XOR）网关和并行（AND）网关（菱形）；每个不同的结束状态一个结束事件（粗线圆）；一个流程池，含 2–5 条泳道。
- **可选：**折叠子流程（[+] 标记）、调用活动、中间事件（双线圆）、数据对象 / 数据存储、文本注释、表示外部参与方的黑盒池。
- **一致性级别：**面向业务读者时保持在**描述性**（Descriptive）子类之内。循环与多实例标记、包容网关和基于事件的网关，以及大多数中间事件属于**分析性**（Analytic）子类 [2 §2, Tables 2.1–2.2][4]。
- **顺序流**（sequence flow，实线、实心箭头）在一个池内排列步骤的先后；可以跨泳道，但绝不能跨越池的边界 [2 §7.2.1]。
- **消息流**（message flow，虚线、起点空心圆、空心箭头）**只连接两个不同的池**，不得连接同一池内的对象 [2 §9.4]。
- **关联**（association，点线）把注释和数据连接到流对象。三种连接线的线型不得改动 [2 §7.5]。
- **规模：**每个流程层级最多约 10 个活动 [5]；超过 50 个元素的模型应分解 [10]。幻灯片上每页 5–9 个活动是可读性经验法则，不属于 BPMN 规范。
- **命名** [5][6][7]：活动用动词 + 宾语（“拣货”）；消息开始事件用“接收订单”；结束事件用结束状态短语（“订单已发货”）；XOR 网关写成问题（“支付已授权？”），出口标“是 / 否”；AND 网关不加标签；消息流用名词（“支付请求”）；泳道用角色命名，绝不用人名。
- **图例：**熟悉 BPMN 的读者不需要图例；业务读者则提供 4–6 项图例，只列实际用到的图形符号。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践

1. 仅凭打印出的页面就只有一种理解：每个层级都有明确的开始和结束事件，每个节点都位于一条从开始到结束的连续路径上 [4][5][7]。
2. 从左到右，主成功路径直穿中央，分支与汇合对称成对，通过调整泳道和池的顺序消除交叉 [7]。
3. 一个流程池，内部角色作为泳道；外部参与方作为黑盒池，只通过消息流连接 [5][9]。
4. 一页由折叠子流程组成的顶层图，然后每个子流程一页子图 [4][5]。
5. 默认图形尺寸，尽量少用颜色：最多一处浅色突出，例如主成功路径，或目标态中发生变化的步骤 [7]。

### 反模式

1. 在池之间画顺序流，或在同一池的泳道之间画消息流；两者都违反规范 [2 §9.4]。
2. 在单个流程中给每个部门画一个池，这会打破实例，把内部交接变成消息流 [5]。
3. 结束事件和网关不加标签：模型能通过校验，却没有向读者传达任何信息 [6]。
4. 无必要地向业务读者展示专用图形符号；例如消息开始事件的信封被理解为“电子邮件”。除非类型会改变含义，否则用普通开始圆加标签 [4]。
5. 把异常画进主路径，直到主成功路径被淹没；应放在边界事件上或单独一张图中。也要避免流程图习惯，如不分类型的菱形、把数据流画成顺序流 [2 §7.2]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [OMG, BPMN 2.0 by Example (dtc/10-06-02)](https://www.omg.org/spec/BPMN/2.0/About-BPMN) — 官方非规范性示例，涵盖流程图、协作图和编排图 [15]。版权归 OMG。
- [Camunda, BPMN 2.0 Symbols reference](https://camunda.com/en/bpmn/reference) — 每个符号配一个小而真实的模型；可免费查看，复用前请核对条款 [8]。
- [Camunda, Creating readable process models](https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models) — 对称性、主成功路径和标签方面的布局前后对比 [7]。
- [Trisotech / Bruce Silver, BPMN Style Rules](https://www.trisotech.com/bpmn-style-rules) — 同一模型应用风格规则前后的对比，并逐条图示标签规则 [5]。
- [BPMN 2.0 Poster (Berliner BPM-Offensive)](https://bpm-conference.org/BPMNPoster) — 一页式符号总览，提供多种语言版本免费下载；是读者图例的良好参照 [11]。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定框架：流程名称、触发、一个实例是什么、2–4 个结束状态、现状还是目标态、面向业务还是技术受众。
2. 选择种类：流程图（一个池含泳道）或协作图（为外部参与方加上黑盒池）。若只有一个执行者且读者不熟悉 BPMN，建议用普通流程图；若参与者主要是系统，建议用 E4。
3. 列出同一实例的 5–9 个顶层活动（动词 + 宾语）；超过 10 个的部分归入折叠子流程，各配子图。
4. 泳道：2–5 个角色或部门，绝不用人名；第一个活动所在的泳道放在最上方，其余按交叉最少排序。
5. 从左到右布局：主成功路径在主泳道中排成一条线；分支放在上方或下方；汇合与分支对称；外部池放在上方或下方，按首次接触的顺序排列，使消息流短且竖直。
6. 网关：XOR 写成问题，出口标“是 / 否”或结束状态；AND 不加标签；每个分支都要汇合，除非每条分支各自以结束事件终止。
7. 事件与消息：开始事件标注其触发；每个结束状态一个结束事件；消息流只在池之间，每条用名词命名。
8. 文字：每个标签约 5 个词，图形中不写句子，最多 2 条注释；标题承载要传达的信息，并注明现状 / 目标态。
9. 颜色：白底黑字，最多一处浅色突出，黑盒池用一种中性底色；图例只列用到的图形符号。

**自检清单**
- [ ] 每条顺序流都留在一个池内；每条消息流都连接两个不同的池。
- [ ] 每条路径都从有标签的开始事件走到有标签的结束事件。
- [ ] 结束状态互不相同；XOR 网关有标签，AND 网关没有。
- [ ] 活动均为动词 + 宾语、粒度一致，每页约 10 个或更少。
- [ ] 泳道是同一类的角色、部门或系统；没有人名。
- [ ] 没有改动线型，没有自创图形。
- [ ] 每个专用图形符号都确有必要并列入图例，否则改用普通符号加标签。
- [ ] 流向从左到右，没有长长的回折线。
- [ ] 标题说明流程以及现状 / 目标态；图上没有 TBD 或状态备注。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **强：**可执行的 BPMN 文件（`*.bpmn`、`*.bpmn20.xml`）；工作流或编排定义（step functions、持久化工作流、DAG、saga 编排器）；带迁移表的状态枚举。面向业务读者时需加以简化。
- **中：**状态枚举（候选结束状态）、角色和权限（候选泳道）、队列、主题和 webhook（通往外部池的消息流）、定时任务（定时开始事件）、审批和通知代码、BDD feature 文件（路径）。
- **弱：**README、`docs/`、ADR。
- **需要问人：**系统之外的手工工作、每一步实际由谁执行、人工异常处理、现状下的变通做法以及目标态意图。代码推导的步骤与访谈得出的步骤要在备注中区分，不放在图上。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 哪个流程？一个实例是什么？可能有哪些结果？（主成功结果加一个拒绝结果）
2. 当前流程（现状）还是目标流程（目标态）？（设计变更时用目标态）
3. 谁来读：不熟悉 BPMN 的业务读者，还是分析师和开发人员？（描述性 BPMN 图形加一个小图例）
4. 哪些角色在做这些工作？哪些外部参与方作为独立的池出现？（一个池含泳道；外部参与方作为黑盒池）
5. 只画主成功路径，还是也画主要异常？（主成功路径加最多一个关键分支；错误放在单独的图中）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A5.json` · 布局模板：`lanes` · 类型为 `pool` 和 `lane` 的分组渲染为横带；`task`、`event` 和 `gateway` 节点在各泳道内从左到右放置；`message` 边只在池之间布线。

## 来源 {#sources}
<!-- skill: omit -->
1. OMG, About the BPMN Specification Version 2.0.2 — https://www.omg.org/spec/BPMN/2.0.2/About-BPMN — 访问于 2026-10-14
2. OMG, Business Process Model and Notation (BPMN) v2.0.2, formal/13-12-09 (§2 Conformance, §7.2, §7.4, §7.5, §9.4, §10) — https://www.omg.org/spec/BPMN/2.0.2/PDF — 访问于 2026-10-14
3. ISO, ISO/IEC 19510:2013 Object Management Group Business Process Model and Notation — https://www.iso.org/standard/62652.html — 访问于 2026-10-14
4. Bruce Silver, *BPMN Method and Style*, 2nd ed., 2011 — https://www.methodandstyle.com/books/bpmn-method-and-style — 访问于 2026-10-14
5. Bruce Silver / Trisotech, BPMN Style Rules — https://www.trisotech.com/bpmn-style-rules — 访问于 2026-10-14
6. Bruce Silver, Standardizing BPMN Labels — https://www.methodandstyle.com/blog/standardizing-bpmn-labels — 访问于 2026-10-14
7. Camunda Docs, Creating readable process models — https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models — 访问于 2026-10-14
8. Camunda, BPMN 2.0 Symbols reference — https://camunda.com/en/bpmn/reference — 访问于 2026-10-14
9. Camunda, BPMN 2.0 Examples — https://camunda.com/bpmn/examples/ — 访问于 2026-10-14
10. Mendling, Reijers, van der Aalst, Seven Process Modeling Guidelines (7PMG), *Information and Software Technology* 52(2), 2010 — https://www.semanticscholar.org/paper/Seven-process-modeling-guidelines-(7PMG)-Mendling-Reijers/5c4a08a28b46fec62a0b45a26647330a0e69feb8 — 访问于 2026-10-14
11. BPM Conference, BPMN 2.0 Poster (Berliner BPM-Offensive) — https://bpm-conference.org/BPMNPoster — 访问于 2026-10-14
12. The Open Group, TOGAF 9.1 Sample Catalogs, Matrices and Diagrams (Process Flow diagram) — http://www.togaf.info/togafSlides91/TOGAF-V91-Sample-Catalogs-Matrics-Diagrams-v3.pdf — 访问于 2026-10-14
13. The Open Group, ArchiMate 3.2 Specification Reference Cards — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — 访问于 2026-10-14
14. ISO, ISO 5807:1985 Documentation symbols and conventions for data, program and system flowcharts — https://www.iso.org/standard/11955.html — 访问于 2026-10-14
15. OMG, About BPMN 2.0 (informative documents, incl. BPMN 2.0 by Example) — https://www.omg.org/spec/BPMN/2.0/About-BPMN — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A5 示例：网店从下单到发货（目标态）——网店池含结账、仓库和客户支持三条泳道；客户和支付服务商作为黑盒池，以消息流相连；结束状态为“订单已发货”和“订单已取消”](/samples/A5-bpmn-process.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
