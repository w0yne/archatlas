---
code: A3
slug: business-context
family: A
names:
  en: Business context diagram
  zh: 业务上下文图
  aliases:
    en: [business context, business environment diagram, business context (arc42 §3.1)]
    zh: [业务背景图, 业务环境图, 范围图（业务视角）]
question: 我们的系统或举措内部包含什么？外部有哪些人或事物与我们交换什么？
audiences: [leaders, business, architects]
levels: [strategy, concept]
phases: [initiate, requirements]
scope: 一个系统、举措或业务单元，画成黑盒，并画出与它交换信息、货物、资金或义务的每一个外部参与方。
formal: {kind: method, ref: Context-level DFD (Yourdon–DeMarco / Gane–Sarson); arc42 §3.1 business context; C4 model System Context at software level}
neighbours: [B4, C2, H3]
status: draft
translationOf: en/types/A3-business-context.md
sourceRev: 674f366
reviewed: false
---

# 业务上下文图（Business Context Diagram）

> 中间一个黑盒，四周是外部参与方，二者之间的每一项业务交换都用一条带标签的箭头表示。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 系统或举措内部包含什么？外部有哪些人或事物与它交换什么（信息、货物、资金、决策、义务）？
- **关注点：** 它确定**边界**和**业务接口**。按 ISO/IEC/IEEE 42010 的说法，它构建目的、范围和外部依赖这些关注点 [4][7]。在 arc42 中，它是第 3 节的 *business context*（业务上下文）[1]。当主体是软件系统时，C4 model 的 System Context 图（系统上下文图）就是同一个思路 [2]。TOGAF 没有名为“context diagram”的制品；与之最接近的是阶段 A 的 Value Chain 图和 Solution Concept 图 [6]。
- **刻意不包含：** 黑盒内部的任何内容（A7、C3）、协议和通道（arc42 的 *technical* context，即技术上下文；C2/C6）、流程步骤（A5）以及干系人的权力或利益（H3）。
- **本站采用的定义：** 业务上下文图只列出与主体*交换某种东西*的参与方。只有权力或利益关系的参与方（发起人、预算负责人、没有交换关系的审计方）属于干系人地图（H3），那是另一张单独的图。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 高管、业务负责人、分析师、架构师，以及任何刚接触该举措的人。
- **场景：** 项目启动（“网店及其交易往来的各方”）；商业论证评审（谁向谁付款、谁供应什么）；新成员入职；就目标态会增加或去掉哪些合作方达成一致（现状与目标态成对绘制）。
- **何时不用：** 解释内部结构（A7、C5）；规定集成细节（C6）；对干系人排序（H3）。
- **与相邻类型对比：**
  - 当主体是软件系统且读者是技术人员时，选择 **C2 系统上下文图**。
  - 当重点是某个项目阶段的范围内外时，选择 **B4 范围图**。
  - 当问题是必须让谁参与、如何参与时，选择 **H3 干系人地图**；它用坐标轴，而不是流。
  - 当需要展示交付价值的各个阶段，而不仅仅是边界时，选择 **A2 价值流**。
  - 当需要打开黑盒、展示主要组成块时，选择 **A7 概念架构**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：** 一个画成黑盒的中心主体；位于外围的外部参与方（角色、组织、外部系统）；每项交换一条连线，用业务名词标注（“order”“payment”“stock level”）；标题写明范围以及现状/目标态。
- **上下文级 DFD 规则（Yourdon–DeMarco、Gane–Sarson）：** 主体是单一处理，外部方是终端（terminator）；每条流的一端都是该处理，因此外部方之间绝不相连 [3][5]。
- **arc42 规则：** 业务上下文可以是一张图，**也可以**是一张 *partner | input | output*（合作方 | 输入 | 输出）表；通道和格式放在技术上下文中 [1]。
- **C4 model 规则：** 只有人员和软件系统；不写技术或协议 [2]。
- **箭头语义：** 表示业务交换的方向，而不是调用或控制的方向。双向交换画两条带标签的箭头，或一条箭头带两个标签。
- **可选：** 对外部方分组（客户 / 合作伙伴 / 监管机构 / 内部但不在范围内）；用线型区分流的种类（信息、资金、货物），并在图例中说明；给流编号，对应一张交换表。
- **详细程度：** 约 5–15 个外部参与方；标签 1–3 个词；不写协议或文件格式名称。
- **正式替代方案：** ArchiMate 业务层：主体周围是 Business Actor / Role / Collaboration，使用 Flow 或 Serving 关系，交换的事物用 Business Object 表示。
- **术语说明：** “Level 0 DFD”有歧义。有些作者用它指上下文图，另一些作者用它指上下文图下面的第一层分解 [5]。说“上下文级 DFD”（context-level DFD）可避免混淆。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践

1. 中心保持为**黑盒**。画在里面的任何东西都属于其他图类型 [2][3]。
2. 每条流都用**所交换的事物**标注，绝不用“uses”或“integrates”。所有读者都应看出哪些数据、货物或资金跨越了边界 [1]。
3. **业务上下文与技术上下文分开。** 通道和协议放在第二个视图或表格中 [1]。
4. 找出不显眼的参与方：监管机构、税务机关、支付和身份服务商、运维和支持。可使用检查清单，例如 42010 的干系人类别（用户、运维人员、采购方、所有者、供应商、维护人员）[8] 和 TOGAF 的五类干系人 [9]。
5. 在标题中写明**现状或目标态**；当目标态改变了合作方集合时，成对绘制。

### 反模式

1. **一张图回答两个问题：** 在中心辐射式的上下文图上再涂上权力/利益颜色。应拆分为 A3 和 H3。
2. 把内部子系统画成外部参与方，或画成中心里面的方框。每个元素要么是主体，要么明确属于外部。
3. 外部参与方之间相互连线。上下文级 DFD 禁止这样做 [3][5]；如果这些交接很重要，就画 A2 或 E4。
4. 只画了最终用户，遗漏了监管机构、财务、物流和支持。
5. 外部方种类混杂：角色旁边是部门，再旁边是产品，再旁边是流程步骤。

## 范例 {#exemplars}
<!-- skill: omit -->
- [arc42 — Example business context: HTML Sanity Checker](https://docs.arc42.org/examples/business-context-1/) — 极简的黑盒业务上下文，旁边附有单独的技术上下文示例。
- [C4 model — System context diagram](https://c4model.com/diagrams/system-context) — 关于范围、受众（“everybody”，所有人）以及不在图上写技术的权威指南；同一思路用于软件层面（CC BY 4.0）。
- [arc42 — 3. Context and scope](https://docs.arc42.org/section-3/) — 解释业务上下文与技术上下文的划分，以及合作方/输入/输出表的形式。
- [Wikipedia — Data-flow diagram](https://en.wikipedia.org/wiki/Data-flow_diagram) — 上下文级 DFD 及其表示法规则（CC BY-SA 4.0）。

## 绘制方法 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确认主体（一个系统、举措或业务单元）以及现状还是目标态。把标题写成一句结论（“The online shop and the seven parties it trades with”，网店及与其交易往来的七方）。
2. 列出外部参与方，合并重复项，每组只放一类（角色、组织、外部系统），总共 5–15 个。
3. 把交换列为 *参与方 → 主体：名词* 和 *主体 → 参与方：名词*。去掉任何属于协议的内容。
4. 版式：主体居中且在视觉上占主导；客户和渠道在左，合作伙伴和服务商在右，监管机构在上，内部但不在范围内的在下；箭头短而直，不交叉。
5. 文字量：参与方名称 ≤ 3 个词，流标签 ≤ 3 个词，画布上不写句子。
6. 颜色：主体用一种中性填充，参与方分组最多 3 种填充；用线型（而不是颜色）区分流的种类，并始终附图例。
7. 可选：给流编号，并在注释中附一张 *partner | input | output* 表。

**自检清单**

- [ ] 中心是黑盒；里面什么都没画。
- [ ] 每组中的外部参与方都是同一类事物。
- [ ] 每条箭头都有业务名词标签和明确的方向；没有协议名称。
- [ ] 已考虑监管机构、财务、物流和支持（纳入或有意排除）。
- [ ] 没有外部方到外部方的流。
- [ ] 标题写明范围和现状/目标态；没有重复说明图类型的副标题。
- [ ] 这里不编码干系人的权力或利益（那是 H3）。
- [ ] 图例说明了每种线型和填充。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **来自代码：** README 中的集成章节；对外调用的客户端模块和 SDK 依赖（支付、电子邮件、物流、身份）；webhook 处理器；揭示外部调用方的 API 网关或路由定义；合作方端点的环境变量名称；OpenAPI/AsyncAPI 契约目录；提到外部参与方的 ADR。
- **局限：** 代码揭示的是*技术*合作方，而不是业务交换。资金、货物、法律义务以及与 IT 没有关联的参与方（税务机关、电话预约的快递员）必须来自人。从代码推导出的参与方标注“observed in code”（代码中观察到），绘图者提出的任何内容标注“proposed”（建议）。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 你需要的是谁与主体交换什么（本图）、必须让谁参与以及如何参与（H3），还是两者分别画成两张图？（先画上下文图，干系人矩阵单独画。）
2. 中心的主体是什么：一个系统、一个项目还是一个业务单元；现状还是目标态？（读者将要讨论的系统，现状。）
3. 以下是按客户 / 合作伙伴 / 监管机构 / 内部但不在范围内分组的候选参与方；有没有遗漏，比如某个监管机构？（纳入支付、物流和税务相关方。）
4. 流只表示信息，还是也表示资金和货物？（三者都表示，用线型区分。）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A3.json` · 布局模板：`nested` · 主体是一个样式为 `primary` 的 `system` 节点，外部方是它周围的 `external` 或 `actor` 节点，每项交换是一条带标签的边，其 `kind` 为 `data`、`call` 或 `message`（流的类型写在标签里）。

## 来源 {#sources}
<!-- skill: omit -->
1. arc42 — "3. Context and scope" — https://docs.arc42.org/section-3/ — 访问于 2026-10-14
2. C4 model — "System context diagram" — https://c4model.com/diagrams/system-context — 访问于 2026-10-14
3. BAwiki — "Context Diagram" — http://www.bawiki.com/wiki/Context-Diagram.html — 访问于 2026-10-14
4. ISO/IEC/IEEE 42010:2022 preview — https://webstore.ansi.org/preview-pages/iso/preview_iso+iec+ieee+42010-2022.pdf — 访问于 2026-10-14
5. Wikipedia — "Data-flow diagram" (DeMarco 1979; Yourdon/Constantine; Gane & Sarson) — https://en.wikipedia.org/wiki/Data-flow_diagram — 访问于 2026-10-14
6. The Open Group — TOGAF Standard 10, Architecture Content ch. 3 "Architectural Artifacts" (Value Chain, Solution Concept) — https://pubs.opengroup.org/togaf-standard/architecture-content/chap03.html — 访问于 2026-10-14（需登录；尚未对照现行规范原文核实）
7. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/ieee-1471/cm/ — 访问于 2026-10-14
8. ISO/IEC/IEEE 42010 — "Architecture Descriptions" (stakeholder and concern checklists) — http://www.iso-architecture.org/ieee-1471/ads/ — 访问于 2026-10-14
9. TOGAF Exam Preparation Guide — "Stakeholder Management" (five stakeholder groups) — https://togafguide.wordpress.com/stakeholder-management/ — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A3 示例：网店作为黑盒，与客户、支付服务商、仓库、快递公司和税务机关交换订单、付款、库存和支持请求](/samples/A3-business-context.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
