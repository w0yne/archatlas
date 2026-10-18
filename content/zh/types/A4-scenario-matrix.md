---
code: A4
slug: scenario-matrix
family: A
names:
  en: Business scenario matrix (role × activity)
  zh: 业务场景矩阵（角色 × 活动）
  aliases:
    en: [scenario coverage matrix, role-activity matrix, business scenario map, role–activity scope matrix, actor–goal matrix]
    zh: [业务场景地图, 场景覆盖矩阵, 业务场景清单, 角色-场景矩阵]
question: 对每个角色而言，方案支持哪些业务活动？通过哪些场景支持？在哪个发布版本中提供？哪些组合是有意不覆盖的？
audiences: [business, product]
levels: [concept]
phases: [requirements]
scope: 一个方案或业务领域：4–8 个角色 × 4–8 项业务活动，每个单元格写明场景并标注发布版本。
formal: {kind: convention, ref: none (table convention; cell content follows Cockburn's user-goal level)}
neighbours: [A6, B1, B2, H1]
status: draft
translationOf: en/types/A4-scenario-matrix.md
sourceRev: 4e718f136c12c2c4c1d5f2226ea103f63e35b600
reviewed: false
---

# 业务场景矩阵（Business Scenario Matrix）

**B2 的具名变体。** [进入用户故事地图 → A4](/zh/types/b2-user-story-map#variant-a4)。此兼容页保留独立画法、检查项、原锚点和历史下载。

> 纵向是角色，横向是业务活动，每个单元格写明方案支持的场景及其提供时间。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 对每个角色而言，方案支持哪些业务活动？通过哪些具体场景支持？在哪个发布版本中提供？同样重要的是：哪些角色 × 活动组合是**有意不覆盖**的？
- **关注点：** 面向业务和产品干系人的功能范围与分期（ISO/IEC/IEEE 42010 关注点 [13]）。它是一份**用户目标级（user-goal level）的范围契约**：缺口、重叠和分期一目了然，而扁平的待办列表会把这些掩盖掉 [10]。架构师用它为 Kruchten 4+1 模型中的“+1”视图挑选场景 [14]。
- **刻意不包含：** 步骤顺序（A5、E 族）、UI、数据、技术设计、情绪（A6）以及价值阶段的流转（A2）。
- **本站采用的定义：** “business scenario map”并不是英语中约定俗成的图类型术语。本页指的是一种非正式的角色 × 活动覆盖矩阵。它**不是** TOGAF 的 *Business Scenario*（业务场景，一种产出文档的需求技术：问题、环境、目标、参与者、结果）[1][2][3]，不是 IBM 的 *scenario map*（旅程图的一种变体，见 A6）[4]，不是未来预测中的 2×2 情景矩阵 [5]，也不是 SAP 的“business scenario”流程层级 [6]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 业务负责人、产品经理和项目经理、业务分析师；挑选关键场景的架构师。
- **场景：** 网店第 1 版范围研讨会（顾客、客服人员、仓库文员、财务 × 浏览、下单、支付、履约、退货）；发布评审时暴露出退货环节的缺口（例如“Track return via support chatbot”只计划在 R2 中提供）；为评审挑选 5–8 个对架构有重要影响的场景 [14]；验收规划，每个已覆盖的单元格都成为一个端到端测试。
- **何时不用：** 只有一个角色（B2 或 A6）；问题是场景*如何*流转（A5、E4）；条目低于用户目标级（点击、字段）；没有人来决定分期（矩阵会变成愿望清单）。
- **与相邻类型的区别：**
  - 需要一份正式、面向开发人员、带系统边界和 include/extend 的参与者目标清单时，选择 **B1 用例图**；它不擅长展示分期和缺口 [9]。
  - 需要沿着**单个用户的叙事线**、在故事级别按发布切片做交付规划时，选择 **B2 用户故事地图**；需要在业务活动级别覆盖多个角色时，选择 A4 [10][11]。
  - 需要展示单个用户画像随时间的体验时，选择 **A6 旅程图**；A4 没有时间轴，也没有情绪。
  - 需要展示业务能做什么、而不考虑角色或发布版本时，选择 **A1 业务能力图**。
  - 当单元格必须承载职责（R/A/C/I）而不是所支持的场景时，选择 **H1 RACI 矩阵**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
没有现成的标准；以下惯例来自用例和用户故事地图的实践 [7][8][10][11]。

- **行 = 角色**，且为同一类（业务角色；不写具名人员，不写系统）。外部系统最多作为备注。
- **列 = 业务活动**，处于同一层级，按叙事或价值顺序从左 → 右排列：价值流阶段（A2）、第 1/2 层能力（A1）或用户故事地图的主干（backbone）活动 [10][11]。
- **单元格：** 0–3 个场景短语，每个都是**用户目标级的动词 + 宾语**。Cockburn 的检验标准：完成后主要参与者能否“go away happy”（满意离开）？[7][8]
- 每个场景都有**发布标记**（R1/R2/R3 或 MVP/Next/Later），用填充、标签或两者表示，并附图例。
- **空单元格有两种含义，都要在图例中说明：** 空白 = 不适用；斜线填充或“—” = 在业务范围内但有意不支持。
- **连线：** 不画。跨角色的交接属于 A5/E4 的问题。
- **可选：** 行分组（顾客 / 员工 / 合作伙伴）、按阶段划分的列带、对架构有重要影响的场景标记、场景编号、每个发布版本的计数。
- **规模：** 约 4–8 × 4–8；每个单元格 ≤ 3 个短语，每个短语 ≤ 6 个词。更大时按业务领域拆分。
- **命名：** 角色用单数名词（“Support agent”），活动用动宾结构的阶段名（“Pay order”），场景用主动的目标表述（“Pay with saved card”）。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践

1. **先确定目标层级。** 单元格保持在用户目标级；子功能级的内容放到用例中 [7][8]。
2. **先广度，后深度。** 先敲定目标清单，再写细节；这个矩阵正是那份广度优先的制品 [7][8]。
3. **按叙事顺序排列各列**，让读者能像走读用户故事地图主干一样走读它 [10][11]。
4. **为每个单元格做出发布决策**，包括“不计划”。第 1 版应端到端覆盖主要角色，就像一副行走骨架（walking skeleton）[10][12]。
5. **向上追溯：** 每个场景都支撑一个明确的业务目标 [1][2]；绘图者提出的场景标注为建议。

### 反模式

1. 单元格里史诗（epic，“Manage orders”）与点击操作（“Upload photo”）混杂 [8]。
2. 没有发布标记，矩阵读起来像一张没有边界的愿望清单。
3. 行中混杂角色、部门、具名人员和系统。
4. 列是系统模块或菜单，把矩阵变成了功能清单（应使用 B3 或 A1）。
5. 在英语中不加定义地称之为“scenario map”；读者会以为是 TOGAF Business Scenario、旅程图或未来预测的 2×2 矩阵 [1][4][5]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Jeff Patton — The New User Story Backlog Is a Map](https://jpattonassociates.com/the-new-backlog/) — 主干、行走骨架和发布切片；是列顺序和发布线的参照模型。
- [NN/g — Mapping User Stories in Agile](https://www.nngroup.com/articles/user-story-mapping/) — 清晰地拆解了活动、步骤和细节的构成。
- [The Open Group — TOGAF 7 Business Scenarios (public text)](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/bus_scen/bus_scen.htm) — TOGAF 业务场景在形式上究竟是什么，用于避免名称冲突（© The Open Group）。
- [TOGAF 9 — Business Use-Case Diagram artifact](https://pubs.opengroup.org/architecture/togaf90-doc/epf/TOGAF9/workproducts/Business%20Use-Case%20Diagram_74D9B44D.html) — 正式的图形化相邻类型（B1）。
- [P. Kruchten — The "4+1" View Model of Software Architecture](https://arxiv.org/pdf/2006.04975) — 说明场景目录为何对架构重要。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定范围（方案或业务领域，现状/目标态）以及发布版本的命名方式。
2. 选定一种列来源（价值流阶段、能力或主干活动）；4–8 列，按叙事顺序排列。
3. 列出 4–8 个角色作为行，按外部/内部分组，主要角色放在最上面。
4. 每个单元格写 0–3 个场景，采用用户目标级的动词 + 宾语；合并或剔除概要级和子功能级的条目。
5. 为每个场景指定发布版本；有意不支持的单元格用斜线填充，不适用的单元格留空。
6. 版式：横向网格，表头行和表头列加粗，可选按阶段划分的细列带，不画箭头。
7. 颜色：发布版本用一个顺序色阶（最深 = R1）或 3 种区分明显的填充；“不支持”用中性灰色斜线；对架构有重要影响的场景用描边标记；图例放在右下角。
8. 文字量：每个场景 ≤ 6 个词，每个单元格 ≤ 3 个场景；可选页脚写明每个发布版本的计数。

**自检清单**

- [ ] 所有行都是同一类角色：没有系统，没有具名人员。
- [ ] 所有列都是同一层级的业务活动，按叙事顺序排列。
- [ ] 每个场景都是用户目标级的动词 + 宾语；没有点击操作，没有史诗。
- [ ] 每个场景都有发布标记；图例说明了每种填充、斜线和空白。
- [ ] 第 1 版端到端覆盖主要角色。
- [ ] 单元格中没有步骤序列、UI 或技术术语。
- [ ] 标题写明范围和现状/目标态，且不单独使用“scenario map”这一术语。
- [ ] 矩阵控制在约 8 × 8 以内，否则按业务领域拆分。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **来自代码（现状矩阵）：** 角色来自 RBAC 定义、权限枚举和种子数据；活动和场景来自路由、菜单、API operation ID、埋点事件、BDD `*.feature` 文件和验收测试名称；发布线索来自特性开关、里程碑和 epic 标签；README 功能清单和 ADR 提供背景。
- **局限：** 目标范围、计划场景的发布版本分配、业务活动列以及有意排除的内容都来自人。单元格标注“observed in code”（代码中观察到）或“proposed”（建议）。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 是要就多个角色的范围和分期达成一致（本矩阵），按故事切片规划单个用户的流程（B2），还是展示正式的用例（B1）？（本矩阵。）
2. 列是什么：价值流阶段、能力，还是按用户顺序排列的主要活动？（按用户顺序排列的主要活动。）
3. 哪些角色作为行？是否纳入顾客和合作伙伴等外部参与方？（是，单独分组。）
4. 用哪些发布标签？“不支持”是否要与“不适用”区分？（R1/R2/R3；是。）
5. 是否标记驱动架构决策的 5–8 个场景？（是。）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A4.json` · 布局模板：`grid_table` · 一个 `tables[]` 条目：行表头是角色，列表头是活动，每个单元格承载带发布标签和可选重要性标志的场景条目。

## 来源 {#sources}
<!-- skill: omit -->
1. The Open Group — TOGAF Standard 10, "Business Scenarios" — https://pubs.opengroup.org/togaf-standard/business-architecture/business-scenarios.html — 访问于 2026-10-14（需登录；尚未对照现行规范原文核实）
2. The Open Group — TOGAF 7 "Business Scenarios" (public) — https://www.opengroup.org/architecture/togaf7-doc/arch/p4/bus_scen/bus_scen.htm — 访问于 2026-10-14
3. The Open Group — "TOGAF Series Guide: Business Scenarios" (G176) — https://publications.opengroup.org/g176 — 访问于 2026-10-14
4. Carrier Management — "Design Thinking Basics" (IBM as-is / to-be scenario maps) — https://www.carriermanagement.com/features/2020/05/08/206437.htm — 访问于 2026-10-14
5. Futures Platform — "2x2 Scenario Planning Matrix" — https://www.futuresplatform.com/blog/2x2-scenario-planning-matrix-guideline — 访问于 2026-10-14
6. SAP Community — "Business Scenario Design Guidelines" — https://community.sap.com/t5/technology-q-a/business-scenario-design-guidelines/qaq-p/9243459 — 访问于 2026-10-14
7. A. Cockburn — use case guidelines from *Writing Effective Use Cases* (2001) — https://pja.mykhi.org/mgr/blokowe/INN/sorcersoft.org/io/uml/UC-guidelines.html — 访问于 2026-10-14
8. A. Cockburn — *Writing Effective Use Cases* (draft) — https://people.inf.elte.hu/molnarba/Informaciorendszerek_ELTE/Writing_effective_Use_cases_Cockburn.pdf — 访问于 2026-10-14
9. The Open Group — TOGAF 9 "Artifact: Business Use-Case Diagram" — https://pubs.opengroup.org/architecture/togaf90-doc/epf/TOGAF9/workproducts/Business%20Use-Case%20Diagram_74D9B44D.html — 访问于 2026-10-14
10. J. Patton — "The New User Story Backlog is a Map" — https://jpattonassociates.com/the-new-backlog/ — 访问于 2026-10-14
11. NN/g — "Mapping User Stories in Agile" — https://www.nngroup.com/articles/user-story-mapping/ — 访问于 2026-10-14
12. Agile Alliance — glossary "Story Mapping" — https://agilealliance.org/glossary/story-mapping/ — 访问于 2026-10-14
13. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/ieee-1471/cm/ — 访问于 2026-10-14
14. P. Kruchten — "Architectural Blueprints — The '4+1' View Model of Software Architecture", IEEE Software 12(6), 1995 — https://arxiv.org/pdf/2006.04975 — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A4 示例：三个角色对三项活动的场景矩阵，带发布标记](/samples/A4-scenario-matrix.svg)
*三个角色（顾客、客服人员、商城管理员）对三项活动（浏览、下单、退货）的场景矩阵。有内容的单元格是“动词+宾语”的场景，并带发布标记（R1、R2）。空白表示不适用，短横线表示在范围内但有意不支持。*
