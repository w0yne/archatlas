---
code: E3
slug: state-machine
family: E
names:
  en: State machine diagram
  zh: 状态机图
  aliases:
    en: [state diagram, statechart, state transition diagram, statechart diagram, state-transition diagram, lifecycle diagram, finite-state machine (FSM) diagram]
    zh: [状态图, 状态迁移图, 状态转换图, 生命周期图]
question: 这一个事物可能处于哪些状态？哪些事件使它在状态之间迁移？每次迁移时发生什么？哪些迁移是不可能的？
audiences: [developers, product]
levels: [logical]
phases: [design, build]
scope: 一个实体、作业、连接或组件的完整生命周期，每个实体一张图
formal: {kind: standard, ref: OMG UML 2.5.1 state machines (behavioral and protocol); Harel statecharts (1987); W3C SCXML 1.0 (2015) for the executable form}
neighbours: [A5, D1, E1, E2]
status: draft
translationOf: en/types/E3-state-machine.md
sourceRev: 7002b1114ff60c6a028194c8376c71eee2b9d52d
reviewed: false
---

# 状态机图（State Machine Diagram）

> 一个实体的生命周期：它的状态、使它在状态之间迁移的事件，以及未画出即表示不允许的迁移。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **要回答的问题：** 这一个事物可能处于哪些状态，哪些事件或条件使它在状态之间迁移，每次迁移时发生什么，哪些迁移是不可能的？
- **视点：** 以单个实体的完整生命周期为中心的行为视图，即它的协议。凡是没画出来的都隐含为禁止，因此这种图能发现缺口（无法离开“Failed”），并支撑幂等、可恢复的工作流 [1][3]。
- **起源：** 有限状态机是经典的自动机理论。David Harel 的状态图（statechart，1987）增加了嵌套状态、并行区域和广播通信，因为扁平的状态图会在规模上爆炸 [1][2][3]。UML 状态机以 Harel 状态图为基础；现行规范是 UML 2.5.1 [4]。W3C 于 2015 年 9 月 1 日将可执行的状态图表示法 SCXML 发布为推荐标准 [7]；XState 是一个广泛使用的“状态图即代码”库 [8]。
- **不包含：** 某个状态内部的步骤（E2）、谁交换哪些消息（E1）、其他实体的状态（每个实体单独画一张）以及数据结构（D1）。
- **本站采用的定义：** *行为状态机（behavioral state machine）*描述实体如何响应事件。*协议状态机（protocol state machine）*描述对一个分类器（classifier）进行操作的合法顺序，标签为 `[precondition] operation / [postcondition]` [5][6]。本页两者都涵盖，默认使用行为形式。“状态机图”是 UML 2 的名称；“状态图（statechart diagram）”是 UML 1.x 的名称 [5]。
- **未对照原文核实：** UML 2.5.1 的条款编号。下文的伪状态规则取自 uml-diagrams.org [12]，并与一张参考卡片上引用的 UML 2.5.1 摘录做了交叉核对。

| 概念 | 表达什么 | 典型单位 |
|---|---|---|
| 状态机图（E3） | 一个实体可能处于哪些状况，以及如何迁移 | 一个实体或组件 |
| 活动图 / 流程图（E2） | 一个从头执行到结束的操作流程的步骤 | 一个操作流程 |
| 时序图（E1） | 一个场景中参与方之间的消息 | 一个场景 |
| BPMN 流程（A5） | 跨业务角色，谁按什么顺序做什么 | 一个业务案例 |

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 开发人员和测试人员（迁移、守卫条件），产品负责人（用通俗事件描述的业务生命周期），运维人员（作业或连接的状态）。
- **典型场景：**
  1. 业务对象生命周期：订单 `Created → Paid → Shipped → Delivered`，以及 `Cancelled` 和 `Refunded`。
  2. 异步作业：`Queued → Running → Succeeded/Failed`，包含重试、暂停/恢复和取消。Kubernetes 的 Pod 阶段（`Pending, Running, Succeeded, Failed, Unknown`）是一个公开示例 [10]。
  3. 协议或连接行为，例如 RFC 793 中的 TCP 连接状态图 [11]。
  4. UI 组件行为，例如客服聊天输入框：空闲、输入中、发送中、出错 [8]。
  5. 发现缺陷：生产环境中出现的不可能迁移、缺失的终止状态。
- **不适用的情况：** 没有持久状态的操作流程（E2）；把几个互不相关的对象画在一页上（应分别画几张图）；所谓的状态其实是由不同人负责的工作流步骤（用 A5 或 E4，再为案例对象配一张小的 E3）。
- **与相邻类型的区别：**
  - 从头执行到结束的操作流程选 **E2 活动图**；长期存在、响应事件的事物选 E3。
  - 一个场景中的消息选 **E1 时序图**；一个场景可能驱动多个 E3 迁移。
  - 跨参与者的业务流程选 **A5 BPMN 流程图**；一个 BPMN 任务常常会改变多个实体的状态。
  - 问题是谁把工作交给谁时，选 **E4 泳道图**。
  - 与 **D1 ER 图**配合使用：每个带 `status` 列的实体都值得配一张小的 E3 [9]。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 在 UML 和 SCXML 中是正式表示法；也常见于非正式的“状态生命周期”图。表示法遵循 [12] 中介绍的 UML 2.5.1，状态图概念取自 [1][3]。
- **必需元素：**
  - **状态：** 圆角矩形，以状况命名（“等待付款”，而不是“付款”）。
  - **初始伪状态：** 实心圆，每个区域最多一个，有一条出向迁移，可以带效果（effect），但不能带触发器或守卫条件 [12]。
  - **迁移：** 标注为 `event [guard] / effect` 的箭头。
  - **终止状态：** 靶心，表示生命周期可以在此结束。
- **可选但很有用：**
  - **复合（嵌套）状态，** 使共有的出口（取消）只需从超状态画一次。
  - **正交区域**（并行状态，用虚线分隔）。
  - 状态内部的 **entry / exit / do 行为**。
  - **选择（choice）与连接（junction）伪状态，** 进出区域的分叉/汇合，**历史状态（history）**（浅历史、深历史），入口/出口点，终结（terminate）。
  - **定时迁移，** 例如 `after 30 s` [3][12]。
- **箭头语义：** 当事件发生且守卫条件成立时，从源状态迁移到目标状态并执行效果。它不是数据流，也不是调用。
- **图例：** 如果读者不熟悉 UML，要解释 `event [guard] / effect` 和所用颜色（成功终止、失败终止）。
- **命名：** 状态用形容词或分词（“Pending”、“Approved”）；事件用过去时的事实或命令（“PaymentReceived”、“cancel”）；守卫条件是布尔表达式。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **一个实体，一张图。** 写明它是哪个实体以及它的权威数据源（例如订单服务中的 `order.status`）。
2. **状态以状况命名，事件以发生的事情命名。** 绝不让同一个动词兼作两者（“Review”与“In review”）。
3. **画出所有终止状态和错误状态，并为每个非终止状态提供出路**（取消、超时、重试）。
4. **用一行说明每个状态的含义；在重要时用注释列出被禁止的迁移**（“不允许从 Delivered 迁移到 Cancelled；请使用 Refund”）。Kubernetes 对 Pod 阶段就是这样做的 [10]。
5. **用层级和并行区域代替组合爆炸式的扁平状态，** 这正是 Harel 最初的动机 [1][3]。尽可能让模型可执行（SCXML、XState），使图始终与实际一致 [7][8]。

### 反模式
1. **状态以动作命名**（“Approve”），或事件以状态命名 [12]。
2. **缺少终止状态或失败状态；** 无法从“Failed”恢复。
3. **一张巨型图混合了多个对象的状态，** 或混入了由不同人负责的工作流步骤。
4. 同一触发器的多条迁移上，**守卫条件重叠或不完备**。
5. **布尔标志大杂烩：** 若干标志组合隐含了谁也没画出的状态。另一种是只画枚举：没有迁移的状态列表不是状态机。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Harel (1987), "Statecharts: a visual formalism for complex systems"](https://www.sciencedirect.com/science/article/pii/0167642387900359) — 原始文献，含层级与正交性的完整示例。© Elsevier；仅供阅读。
- [statecharts.dev, "What is a statechart?"](https://statecharts.dev/what-is-a-statechart.html) — 对嵌套、并行区域、守卫条件、延迟迁移和历史状态最清晰的现代讲解。
- [Kubernetes, "Pod Lifecycle"](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) — 文档精确的生命周期，在图旁用文字定义每个阶段。文档采用 CC BY 4.0 许可。
- [RFC 793, TCP connection state diagram](https://www.rfc-editor.org/rfc/rfc793.txt) — 经典的协议状态机，带事件/动作标签，以 ASCII 绘制。
- [XState](https://github.com/statelyai/xstate) 和 [W3C SCXML Recommendation](https://www.w3.org/news/2015/state-chart-xml-scxml-state-machine-notation-for-control-abstraction-is-a-w3c-recommendation/) — 可执行的状态图，图由代码实际运行的模型生成。
- [uml-diagrams.org, State Machine Diagrams](https://www.uml-diagrams.org/state-machine-diagrams.html) — 关于伪状态、区域和迁移语法的完整参考。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 选定一个实体及其权威数据源（状态字段、枚举、工作流引擎），两者都写进标题，例如“订单生命周期（订单服务，`order.status`）”。
2. 列出各个状态，每个附一行含义说明；合并同义状态；把状态和步骤区分开。
3. 把迁移列成表格（源状态、事件、守卫条件、效果、目标状态），如果存在，要包括取消、超时、重试和暂停/恢复。绘图前先把表格给用户看。
4. 用层级分组：例如“Active”包含“Running”和“Paused”，使共有的出口只需从超状态画一次。
5. 布局：初始伪状态在左上；主生命周期作为从左到右（或自上而下）的主干；终止状态和错误状态沿底边或右边排列；重试和恢复画成短的弧形回边，而不是长长的环路。
6. 文字：状态名最多 3 个词；迁移标签最多 6 个词（`event [guard]`）；较长的效果放进脚注表格。
7. 颜色：中性填充；成功终止用一种强调色，失败终止用另一种，并在图例中说明，图例同时解释标签语法。
8. 如果存在被禁止的迁移，添加一条简短的“禁止迁移”注释。

**自检清单**
- [ ] 恰好一个实体；已写明其权威数据源。
- [ ] 每个区域一个初始伪状态；至少一个终止状态，或明确注明“永不结束”。
- [ ] 每个状态都是状况，每个事件都是发生的事情；没有以动作命名的状态。
- [ ] 每个非终止状态都有出口（适用时包括取消或超时）。
- [ ] 同一事件的多条迁移，其守卫条件互斥且完备。
- [ ] 尽可能用层级代替重复的迁移。
- [ ] 每条迁移都与代码或明确的规则一致；推断出的迁移已标注。
- [ ] 在重要之处写明了被禁止的迁移。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **状态：** 状态枚举、数据库检查约束、状态名常量。
- **迁移：** 更新前的守卫代码，例如 `if status in (...)`；名为 `pause`、`resume`、`cancel`、`retry` 的服务方法；工作流定义（XState、SCXML、Step Functions、Temporal、YAML）；以及断言迁移的测试。
- 枚举列出的是状态，不是迁移：要追踪状态字段的每一个写入方。只在一处发现的迁移标为*推断*。
- **必须来自人：** 计划中但尚未实现的迁移，以及每个状态的业务含义。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 画哪个实体的生命周期，它的状态存储在哪里？（状态列最多的实体，例如订单）
2. 画代码中的现有行为，还是预期的目标设计？（现有行为，并标出缺口）
3. 必须出现哪些异常路径：取消、超时、重试、暂停/恢复、人工干预？（取消、超时、重试）
4. 是否明确展示被禁止的迁移？（是，用一条简短注释）
5. 读者是谁：业务读者（通俗的状态和事件）还是工程师（`event [guard] / effect`、嵌套状态）？（工程师）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/E3.json` · 布局模板：`statechart` · 状态是 `state` 节点（伪状态用 `initial` 和 `final`），复合状态是 `frame` 分组，每条迁移是 kind 为 `call` 的边，`label` = `event [guard] / effect`；`evidence.status` 区分已核实与推断的迁移。

## 来源 {#sources}
<!-- skill: omit -->
1. D. Harel, "Statecharts: a visual formalism for complex systems", *Science of Computer Programming* 8(3), 1987 — https://www.sciencedirect.com/science/article/pii/0167642387900359 — 访问于 2026-10-14
2. Harel 1987 PDF (state-machine.com) — https://www.state-machine.com/doc/Harel87.pdf — 访问于 2026-10-14
3. statecharts.dev, "What is a statechart?" — https://statecharts.dev/what-is-a-statechart.html — 访问于 2026-10-14
4. OMG, UML 2.5.1 — https://www.omg.org/spec/UML/2.5.1/About-UML — 访问于 2026-10-14
5. Wikipedia, "UML state machine"（行为状态机与协议状态机）— https://en.wikipedia.org/wiki/UML_state_machine — 访问于 2026-10-14
6. uml-diagrams.org, "Protocol state machine diagrams" — https://www.uml-diagrams.org/protocol-state-machine-diagrams.html — 访问于 2026-10-14
7. W3C, "State Chart XML (SCXML) … is a W3C Recommendation" (1 September 2015) — https://www.w3.org/news/2015/state-chart-xml-scxml-state-machine-notation-for-control-abstraction-is-a-w3c-recommendation/ — 访问于 2026-10-14
8. XState (Stately) — https://github.com/statelyai/xstate — 访问于 2026-10-14
9. QualiWare CoE, "TOGAF Artifacts"（数据生命周期图；TOGAF 10 中的命名未核实）— https://coe.qualiware.com/resources/togaf/togaf-artifacts/ — 访问于 2026-10-14
10. Kubernetes, "Pod Lifecycle" — https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ — 访问于 2026-10-14
11. IETF, RFC 793 "Transmission Control Protocol"（连接状态图）— https://www.rfc-editor.org/rfc/rfc793.txt — 访问于 2026-10-14
12. uml-diagrams.org, "UML State Machine Diagrams" — https://www.uml-diagrams.org/state-machine-diagrams.html — 访问于 2026-10-14

## 示例图 {#sample}
<!-- skill: path only -->
![E3 · 企业服务助手](/samples/ai-service-assistant/E3/zh/diagram.svg)
*DS-app 中的单个请求：未审批、已审批、执行中、未知、已记录、拒绝及关闭。有界对账后仍未知则保持挂起，不授权重新写入。*

[SVG](/samples/ai-service-assistant/E3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/E3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

[历史 shop 回归样例](/samples/E3-state-machine.zh.svg) · [全部29幅视图](/zh/use/ai-service-assistant) · [示意假设](/zh/use/ai-service-assistant-assumptions).
