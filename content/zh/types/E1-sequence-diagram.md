---
code: E1
slug: sequence-diagram
family: E
names:
  en: Sequence diagram
  zh: 时序图
  aliases:
    en: [UML sequence diagram, runtime view, C4 dynamic diagram, message sequence chart, MSC, C4 dynamic diagram (sequence style), runtime-view scenario, call-flow diagram, ladder diagram]
    zh: [序列图, 运行时视图, 交互时序图, 顺序图, 调用链时序图]
question: 在一个场景中，哪些参与方按什么顺序交换哪些消息？流程在哪里分支、循环或等待？
audiences: [developers, architects]
levels: [logical]
phases: [design, build]
scope: 一个场景（从一个触发到一个结果），同一抽象层级上约 4–8 条生命线，最多约 25 条消息
formal: {kind: standard, ref: 'OMG UML 2.5.1 (formal/2017-12-05), interaction diagrams; ITU-T Z.120 Message Sequence Chart for the telecom ancestor'}
neighbours: [A5, C3, C4, C6, E2, E3, E4, F1, I1]
status: draft
translationOf: en/types/E1-sequence-diagram.md
sourceRev: 4e718f136c12c2c4c1d5f2226ea103f63e35b600
reviewed: false
---

# 时序图（Sequence Diagram）

> 把一个场景画成：参与方横排在顶部，消息按时间顺序自上而下排列，展示谁调用谁，以及流程在哪里分支、重复或等待。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **要回答的问题：** 在这一个场景中，哪些参与方交换哪些消息、顺序如何，流程在哪里分支、循环或等待？
- **视点：** 单个场景的运行时视图。它把静态结构（C2、C3）变成一个随时间展开的故事。arc42 第 6 节“运行时视图（Runtime View）”要求的正是这类图，而且只针对重要场景 [6]。C4 model 认为动态图应“谨慎使用”，只用于交互复杂、值得关注或反复出现的模式 [4]。
- **深层含义：** 时序图是 UML 2.x *交互图（interaction diagram）*的一种；交互图家族还包括通信图、时间图和交互概览图 [3]。C4 动态图既可以画成协作风格（自由布局、带编号的连线），也可以画成时序风格 [4]。
- **不包含：** 完整的静态结构（只出现本场景的参与方）、所有备选路径、内部算法（E2）、对象生命周期（E3）、数据结构（D1）和组织职责（E4、A5）。
- **本站采用的定义：** “时序图”指 UML 2.5.1 表示法 [1][2]，按“UML 作为草图（UML as sketch）”的方式有选择地使用 [5]：保留生命线（lifeline）、消息和交互框，但不强制执行每一条规则。“交互图”是家族名称，不是同义词。
- **电信领域的前身：** ITU-T Z.120 *消息序列图（Message Sequence Chart，MSC）*，现行版本为 Z.120 (02/11) [16]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 开发人员、测试人员、架构师、集成合作方和安全评审人员。业务读者可以看简化版：生命线更少，消息用通俗语言表述。
- **典型场景：**
  1. 商定 API 集成：店面、网关、订单服务、外部支付服务商。
  2. 讲解包含重定向、令牌和回调的认证或授权流程 [7][8]。
  3. 客服聊天机器人中“一个问题是如何被回答的？”：UI、编排器、语言模型、商品搜索服务、再回到模型、再回到 UI，其中包含检索循环。
  4. 事故复盘：重建跨服务的事件顺序。
  5. 异步处理：订单被受理、任务入队，稍后通过 webhook 或回调返回。
- **不适用的情况：** 把系统的全部行为画在一张图上；包含大量判断的人工工作流（A5、E4）；单个对象的生命周期（E3）；超过约 8–10 条生命线或约 25 条消息时，应使用 `ref` 拆分或提高抽象层级。
- **与相邻类型的区别：**
  - 重点是人员或组织之间的交接时，选 **E4 泳道图**或 **A5 BPMN**。
  - 表达单个参与方内部的判断逻辑，选 **E2 活动图**。
  - 空间关系比严格的时间顺序更重要时，选**通信图或 C4 协作风格**的图 [4]。
  - OAuth/OIDC 类流程选 **F1 认证与授权流程图**；它是一种专门化的时序图 [7][8]。
  - 问题是结构而非行为时，选 **C3/C4**。
  - 问题是接口清单及其协议、认证和失败语义，而不是某个场景中的先后顺序时，选 **C6**。
  - 需要用多个场景把逻辑、进程、开发和物理视图串起来时，选 **I1**；一张时序图就是其中的一个场景。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 在 UML 2.5.1 中是正式表示法 [1]。大多数架构时序图是草图，只保留生命线、消息和交互框 [5]。
- **必需元素：**
  - **生命线：** 每个参与方一个方框加一条竖直虚线。使用真实、可命名的角色或系统，并保持同一层级（全部是系统，或全部是容器）。参与者（actor）可以画成小人。
  - **消息：** 自上而下排列的水平箭头，可选编号。
- **箭头语义：**
  - **同步调用：** 实线、实心箭头；调用方等待 [9]。
  - **异步消息：** 实线、开口箭头；调用方不等待 [9]。
  - **返回：** 指回调用方的虚线；显而易见时可省略。其箭头样式因 UML 版本和工具而异，因此“用虚线”是稳妥的规则 [9]。
  - **创建 / 销毁：** 创建消息指向新生命线的头部；用 X 标记销毁。
- **可选元素：**
  - **激活条：** 参与方处理调用期间的细长矩形；收到返回时结束。
  - **组合片段（combined fragment）** [10]：`alt`（带守卫条件的分支）、`opt`、`loop`、`par`、`break`、`critical`、`ref`（引用另一个交互）；较少用的有：`neg`、`assert`、`strict`、`seq`、`ignore`、`consider`。守卫条件写在方括号中；`[else]` 表示其余条件均不满足。
  - 注释、时间约束、门（gate），以及包住整张图的 `sd <name>` 框。
- **细节层级：** 说明生命线是系统、容器还是组件，消息是业务动作还是 API 调用。端点名称可选。
- **命名：** 消息用“动词+对象”（“提交订单”、“GET /orders/{id}”）；返回用名词（“订单确认”）；生命线沿用 C2/C3 中的名称。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **一张图一个场景，在标题中写明，** 并注明变体：“下单：银行卡支付，主成功路径”。
2. **从受众关心的触发点开始；** 省略他们视为理所当然的准备步骤（登录），除非那正是重点。
3. **前置条件按时间顺序放在前面**（先获取令牌，再调用 API）。复用的步骤加注说明（“令牌缓存至过期”），不要重复画。
4. **生命线保持同一抽象层级，** 按首次动作从左到右排列，使箭头尽量不交叉。
5. **如实表达异步：** 用异步箭头加稍后的回调，而不是虚构一个同步返回。用 `loop` 包住完整的重复往返；错误和超时处理若会挤占主成功路径，就放到单独的图中。

### 反模式
1. **把整个系统塞进一张时序图：** 生命线或消息过多。
2. **抽象层级混杂：** 浏览器、数据库表和合作公司并排出现。
3. **调用与返回混淆：** 返回箭头画成实线，激活条从不结束。
4. **虚构的参与方，** 并非真实的系统或角色。
5. **时间顺序与真实依赖相矛盾**（在获取令牌之前就使用令牌），或者消息名称已经与代码不一致。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Microsoft identity platform: OAuth 2.0 authorization code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow) — 一张跨用户代理、应用、身份平台和 API 的带编号时序图，协议细节依然易读。厂商文档。
- [IETF RFC 6749 section 4.1](https://datatracker.ietf.org/doc/html/rfc6749) — 经典的 ASCII 流程图，以字母 (A) 到 (F) 标注；步骤标签精确而简洁。公开标准。
- [C4 model: Dynamic diagram](https://c4model.com/diagrams/dynamic) — 同一场景分别用协作风格和时序风格绘制，并给出范围方面的指导。
- [uml-diagrams.org: combined fragments](https://www.uml-diagrams.org/sequence-diagrams-combined-fragment.html) — `alt`、`opt`、`loop`、`par`、`break` 的完整示例。
- [Mermaid sequence diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html) 和 [PlantUML sequence diagrams](https://plantuml.com/sequence-diagram) — 图即代码（diagrams as code）的参考，涵盖激活条、交互框、自动编号和注释。开源工具。
- [RFC 9293 (TCP), three-way handshake figure](https://datatracker.ietf.org/doc/html/rfc9293) — 一个极小的交互；两条生命线就可能足够。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定场景、触发点、终点和抽象层级（系统、容器或组件）。决定只画主成功路径，还是再加一条关键备选路径。
2. 按首次动作的顺序列出参与方；上限约 6–8 个。把非重点子系统合并为一条生命线。
3. 先把消息列表写成带编号的文本（发送方、接收方、同步 / 异步 / 返回），并对照代码或文档核实。绘图前先给用户看。
4. 布局：时间自上而下；发起方位于最左侧。用浅色背景带按所属系统给生命线分组（“店内”与“外部”）。
5. 交互框：`loop` 包住重复的往返，`alt [condition]` 表示分支，`opt` 表示可选步骤，`ref` 指向另一张图。超时后重试一次：两种结果都要表达时，用 `alt [收到回复] … [else：超时] 重试一次`；有上限的重试，用 `loop [直到确认，最多 2 次]` 包住整个往返；只有图中只画重试这一支时才用 `opt [超时]`，并写明守卫条件。只有发送方不等待结果时（事件、通知、写入队列、webhook、回调），才把消息标为异步（开口箭头，kind 为 `async`）；不要凭空添加异步消息。
6. 文字：消息最多 6 个词；只有受众需要时才写端点、载荷或技术，以等宽小字后缀形式出现。
7. 颜色：生命线用中性色；最多一种强调色，用于跨系统边界或异步的消息，并在图例中说明。
8. 读者不熟悉 UML 时添加图例（同步、异步、返回、交互框），并加一行说明文字，写明场景及其假设。

**自检清单**
- [ ] 标题是场景加变体（主成功路径或错误路径）。
- [ ] 每条生命线都是真实、可命名的参与方，且处于同一抽象层级。
- [ ] 前置条件在依赖它的步骤之前；复用已注明，没有重复画。
- [ ] 同步调用用实心箭头，异步用开口箭头，返回用虚线；激活条在返回处结束。
- [ ] 交互框包住完整的往返；守卫条件写在方括号中。
- [ ] 最多约 8 条生命线和约 25 条消息，否则用 `ref` 拆分。
- [ ] 跨边界的消息可以辨认。
- [ ] 消息名称与代码或文档中的接口一致，或是有意做了概括。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **追踪路径：** 路由处理器、服务调用、出站客户端（HTTP 或 SDK）、队列 `send`、消费者处理器、存储写入、响应或流。为每一跳记录文件和行号。
- **同步还是异步：** 查找重试、超时和流式响应（SSE、websocket），据此选择箭头样式和循环。
- **同样有用：** OpenAPI 规范、链路追踪 span、覆盖整个场景的集成测试。
- **必须来自人：** 哪个场景对受众重要，以及技术步骤对应的业务名称。
- 把已追踪的跳标为“来自代码”，未核实的跳标为“推断”。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 这张图要展示哪一个场景，从哪里开始、到哪里结束？（讨论最多的用户旅程，例如下单）
2. 读者是谁：业务人员（系统和通俗动作）还是工程师（带端点的容器或组件）？（工程师，容器级）
3. 只画主成功路径，还是再加一条重要的备选或错误路径？（主成功路径，错误放在单独的图中）
4. 是否要出现准备步骤（登录、获取令牌）？（不要，从它们之后开始）
5. 显示接口和端点名称，还是做概括？（做概括，除非工程师会拿它对照代码）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/E1.json` · 布局模板：`sequence` · 生命线是从左到右排列的 `lifeline` 节点；消息是带 `step` 编号的 `edges`，kind 为 `call`、`async` 或 `message`（返回消息是同一条边反向并加 `dashed: true`）；`frames` 用 `operator` 加步骤范围（`from_step`、`to_step`）和 `guard` 标出 `loop` / `alt` / `opt` / `par` 区域；`alt` 或 `par` 框列出 `operands`，每个操作数有各自的守卫条件和步骤范围，以虚线分隔成独立区域；`activations` 承载执行条。

## 来源 {#sources}
<!-- skill: omit -->
1. OMG, UML 2.5.1 specification page (formal/17-12-05, December 2017) — https://www.omg.org/spec/UML/2.5.1/About-UML — 访问于 2026-10-14
2. Wikipedia, "Sequence diagram"（引用 UML 2.5.1 formal/2017-12-05）— https://en.wikipedia.org/wiki/Sequence_diagram — 访问于 2026-10-14
3. Lucidchart, "Interaction Diagram Tutorial"（时序图与通信图；交互图家族）— https://www.lucidchart.com/pages/uml-interaction-diagram — 访问于 2026-10-14
4. C4 model, "Dynamic diagram" — https://c4model.com/diagrams/dynamic — 访问于 2026-10-14
5. M. Fowler, "UmlAsSketch" — https://martinfowler.com/bliki/UmlAsSketch.html — 访问于 2026-10-14
6. arc42, "6 – Runtime view" — https://docs.arc42.org/section-6/ — 访问于 2026-10-14
7. Microsoft Learn, "Microsoft identity platform and OAuth 2.0 authorization code flow" — https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow — 访问于 2026-10-14
8. IETF, RFC 6749 "The OAuth 2.0 Authorization Framework" — https://datatracker.ietf.org/doc/html/rfc6749 — 访问于 2026-10-14
9. Sparx Systems, "Sequence Diagram — UML 2 Tutorial" — https://sparxsystems.com/resources/tutorials/uml2/sequence-diagram.html — 访问于 2026-10-14
10. uml-diagrams.org, "Sequence diagram combined fragment" — https://www.uml-diagrams.org/sequence-diagrams-combined-fragment.html — 访问于 2026-10-14
11. Mermaid, "Sequence diagrams" — https://mermaid.js.org/syntax/sequenceDiagram.html — 访问于 2026-10-14
12. PlantUML, "Sequence Diagram" — https://plantuml.com/sequence-diagram — 访问于 2026-10-14
13. SequenceDiagram.org — https://sequencediagram.org/ — 访问于 2026-10-14
14. Thoughtworks Technology Radar, "Diagrams as code" — https://www.thoughtworks.com/en-us/radar/techniques/diagrams-as-code — 访问于 2026-10-14
15. IETF, RFC 9293 "Transmission Control Protocol" — https://datatracker.ietf.org/doc/html/rfc9293 — 访问于 2026-10-14
16. ITU-T, Recommendation Z.120 "Message Sequence Chart (MSC)", status page（Z.120 (02/11) 现行有效）— https://www.itu.int/rec/t-rec-z.120 — 访问于 2026-10-14

注：UML 2.5.1 的条款原文未亲自阅读；元素语义取自来源 9 和 10，未对照原文核实。

### F1 · 认证与授权流程图 {#variant-f1}

编辑归组保留独立语义；使用本变体的画法与检查项。

1. 选定一种客户端类型和一个受保护操作；在标题中写明受众以及是现状还是提议（“网店：已登录用户的订单历史，现状”）。
2. 根据证据，识别签发方、调用方、接收 API 和受保护资源。
3. 先追踪凭证的签发与校验，再把权限执行作为单独一步。
4. 布局：参与方从左到右排列（人、客户端、签发方、API、资源），交互从上到下；每张图一个场景。任何下游交换（API 到 API）放到单独的图或框中。
5. 浏览器重定向与后端通道调用使用不同线型，并用一行图例说明。
6. 添加一个 `alt` 框，包含允许和拒绝两种结果；拒绝分支在受保护操作之前结束。
7. 标签：简短的动词加凭证用途；为箭头编号。颜色标示职责（签发、校验、执行），而非产品；最多 3 种颜色加中性色。

**自检清单**
- [ ] 客户端类型和场景已明确。
- [ ] 人的身份与机器身份已区分。
- [ ] 每份凭证都有签发方和预期接收方。
- [ ] 标签中授权码、ID 令牌、访问令牌和会话没有混用。
- [ ] 校验和执行都可见。
- [ ] 拒绝分支没有继续进入受保护操作。
- [ ] 浏览器交换和后端通道交换画法一致；箭头连接在生命线上。
- [ ] 未经核实的外部配置已在图上或图注中说明。

[完整方法与历史样例](/zh/types/f1-authentication-authorization-flow#meaning).

## 示例图 {#sample}
<!-- skill: path only -->
![E1 · 企业服务助手](/samples/ai-service-assistant/E1/zh/diagram.svg)
*在一个场景中，各参与者按什么顺序交换哪些消息？*

[SVG](/samples/ai-service-assistant/E1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/E1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

[历史 shop 回归样例](/samples/E1-sequence-diagram.zh.svg) · [全部29幅视图](/zh/use/ai-service-assistant) · [示意假设](/zh/use/ai-service-assistant-assumptions).
