---
code: A3b
slug: stakeholder-map
family: A
names:
  en: Stakeholder Map (Power–Interest Grid)
  zh: 干系人地图（权力–利益矩阵）
  aliases:
    en: [power/interest grid, power-interest matrix, influence/interest grid, stakeholder matrix, stakeholder catalog (TOGAF 10), stakeholder onion diagram]
    zh: [利益相关者地图, 权力/利益矩阵, 影响力 × 关注度矩阵, 干系人洋葱图]
question: "我们需要谁的支持？各方的权力和利益分别有多大？应如何与他们沟通协作？"
audiences: [发起人, 项目群或项目经理, 首席架构师]
level: strategy
phases: [discovery, planning, review]
scope: "一项举措的全部干系人角色或群体，按权力和利益标绘，并为每个象限制定沟通参与方式。"
formal:
  kind: method
  ref: "Power/interest grid (Johnson & Scholes, Exploring Corporate Strategy, 2nd ed. 1993, after Mendelow 1981); TOGAF Stakeholder Management technique"
neighbours: [A3, H1, A1, I2]
status: draft
translationOf: en/types/A3b-stakeholder-map.md
sourceRev: 6857dea
reviewed: false
---

# 干系人地图（Stakeholder Map）

> 一个以权力对利益构成的 2×2 矩阵，告诉你该对谁重点管理、令其满意、随时告知，或仅需关注。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 这项举措需要谁的支持？各方的权力和利益分别有多大？应如何与每一方沟通协作？
- **关注点：** 它把 ISO/IEC/IEEE 42010 中“干系人 → 关注点”的关联显式化 [7]。它是**项目与治理**类制品：TOGAF 的 Stakeholder Management（干系人管理）技术用它来规划沟通，并决定每个群体获得哪些视图 [1][2]。
- **刻意不包含：** 流和交换（A3）、任何形式的架构内容，以及每项活动的职责（H1 RACI）。
- **本站采用的定义：** Johnson & Scholes 在《Exploring Corporate Strategy》（第 2 版，1993）中发表的权力 × 利益矩阵，是对 **Mendelow（1981）** 的发展。Mendelow 最初的矩阵是**权力 × 动态性**（power × dynamism），用于确定环境扫描的强度 [3][4]。“Mendelow 1991”这一引用年份有误 [3][4]。
- **敏感性：** TOGAF 指出，干系人映射信息可能是敏感的，因此保持非正式 [5]。应将该矩阵视为**内部**资料：它经常是在给真实的人和群体打分。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 发起人、项目群或项目经理、首席架构师；限制传阅范围。
- **场景：** 为网店结账流程改版规划干系人沟通（财务、法务、安全、客服、仓储运营、支付服务商）；在需求冻结前找出隐藏的干系人（数据保护、税务、职工委员会）；决定每个群体收到哪些图；在每个阶段关口重新排序。
- **何时不用：** 在任何会流出核心团队的演示材料中（只用角色，或用一份普通清单）；干系人少于约六个时（一份清单就够了）；要展示谁与系统交换什么时（A3）。
- **与相邻类型对比：**
  - 当问题是谁与系统交互、流动的是什么时，选择 **A3 业务上下文图**；它用流，而不是坐标轴。
  - 当需要的是每项活动的职责，而不是每个干系人的沟通参与方式时，选择 **H1 RACI 矩阵**。
  - 当必须正式追溯干系人 → 驱动因素 → 目标 → 需求时，选择 **ArchiMate Stakeholder / Motivation 视图**（I2）。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：** 两条坐标轴，*Interest →*（利益，x 轴）和 *Power ↑*（权力，y 轴），各分 Low/High 或 1–5；四个带标签的象限：**Key Players**（关键参与者，重点管理）、**Keep Satisfied**（令其满意）、**Keep Informed**（随时告知）、**Minimal Effort**（最少投入，仅需关注）[2][6]；干系人以简短标签标绘。
- 只要这张图可能被传阅，就**标绘角色或群体**，而不是个人姓名。
- **可选的第三维度：** 态度（支持者 / 中立 / 反对者），用标记形状或颜色表示，并附图例 [6][8]。箭头可表示计划中的移动（例如 Keep Informed → Key Players）。
- **配套表格**（TOGAF 干系人目录的列）：干系人 | 参与程度 | 象限 | 主要关注点 | 所需视图 [1][5]。
- **洋葱图变体（BABOK）：** 同心圆环：解决方案、使用它的人、承载它的组织、外部参与方（如客户、监管机构和供应商）[9]。
- **连线：** 干系人之间不画连线；这不是网络图。
- **正式替代方案：** ArchiMate Stakeholder viewpoint，使用 Stakeholder、Driver、Assessment 和 Goal 元素 [10]。
- TOGAF 10 的象限名称和目录列取自 TOGAF 9.2 原文和二手指南；尚未对照现行规范原文核实。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践

1. 打分前广泛收集：使用 42010 的干系人类别 [7] 和 TOGAF 的五类干系人（公司职能部门、最终用户、项目组织、运营、外部）[6]。
2. **与发起人一起打分；绝不编造分数。** 权力和利益是判断，而不是数据。
3. 加上**态度**，并为每个象限附上**沟通参与行动** [8]。
4. **每个阶段重新审视。** 干系人及其权力会变化；映射不是一次性活动 [6][8]。
5. 用这个矩阵来**选择视图**：TOGAF 的最后一步就是为每个群体定制其收到的目录、矩阵和图 [1][2]。

### 反模式

1. 在上下文图上涂上权力/利益颜色：一张图回答两个问题 [5]。
2. 在传阅的演示材料中把具名个人放进“Minimal Effort”象限 [5]。
3. 矩阵没有附带任何行动；分析始终没有转化为沟通参与。
4. 只标绘了最终用户，遗漏了监管机构、财务、运营和供应商。
5. 把权力 × 利益矩阵归于“Mendelow 1991”[3][4]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [NN/g — Stakeholder Analysis for UX Projects](https://www.nngroup.com/articles/stakeholder-analysis/) — 带态度维度的权力/利益矩阵，并建议定期重新审视。
- [Votito — Stakeholder mapping origins](https://www.votito.com/methods/stakeholder-mapping/) — 公开资料中对 Mendelow、Johnson & Scholes 与 Freeman 三者区别的清晰梳理。
- [TOGAF 10 — Stakeholder Management](https://pubs.opengroup.org/togaf-standard/adm-techniques/chap03.html) — 示例干系人表和权力矩阵（需登录；© The Open Group）。
- [BAwiki — Stakeholder Onion Diagram](http://bawiki.com/wiki/Stakeholder-Onion-Diagram.html) — 逐步构建洋葱图。

## 绘制方法 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确认谁会看到这张图。如果它可能流出核心团队，只用角色或群体，并去掉态度。
2. 借助上述检查清单，以角色或群体的形式收集干系人；目标 6–20 个。
3. 与用户一起给权力和利益打分（High/Low 或 1–5）。绝不猜测。
4. 画一个正方形 2×2 矩阵；坐标轴标签为 *Interest →* 和 *Power ↑*；象限名称写在各角。
5. 标绘简短标签（≤ 3 个词）；态度用标记形状表示，并附图例；可选用箭头表示计划中的移动。
6. 关注点和沟通参与行动放在配套表格中，不要放在矩阵上。
7. 颜色：象限用中性色（最多给 Key Players 加一种浅色调）；态度标记优先用形状，其次用颜色。
8. 只要出现真实的群体或姓名，就加页脚“Internal — stakeholder analysis”（内部——干系人分析）。

**自检清单**

- [ ] 坐标轴和四个象限都有标签。
- [ ] 每个点都是角色或群体，否则该图已标注为内部资料。
- [ ] 分数来自用户，而不是绘图者。
- [ ] 已考虑监管机构、财务、运营和供应商。
- [ ] 每个象限在配套表格中都有沟通参与行动。
- [ ] 该矩阵与上下文图是两张独立的图。
- [ ] 任何出处说明都写作“Johnson & Scholes, after Mendelow 1981”。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **来自代码：** 几乎没有。CODEOWNERS、团队标签和 issue 负责人可提示内部群体；ADR 的决策者可提示谁拥有决策权。
- **局限：** 权力、利益、态度和外部干系人只能来自访谈和发起人。绝不推断；要去问。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 谁会看到这张图？（仅核心团队；否则用角色代替姓名。）
2. 矩阵、洋葱图，还是两者？（矩阵。）
3. 权力和利益用哪种刻度？（High/Low。）
4. 是否展示态度？（是，仅限内部版本。）
5. 以下是根据标准群体整理的候选清单；还缺谁？（补充监管机构和供应商。）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A3b.json` · 版式模板：`grid_table` · 一个 2×2 的 `tables[]` 条目承载四个象限；干系人是带态度标记的单元格条目，配套表格是第二张表。

## 来源 {#sources}
<!-- skill: omit -->
1. The Open Group — TOGAF Standard 10, ADM Techniques ch. 3 "Stakeholder Management" — https://pubs.opengroup.org/togaf-standard/adm-techniques/chap03.html — 访问于 2026-10-14（需登录；尚未对照现行规范原文核实）
2. The Open Group — TOGAF 9.2 ch. 21 "Stakeholder Management" — https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap21.html — 访问于 2026-10-14
3. Mendelow, A. L. — "Environmental Scanning — The Impact of the Stakeholder Concept", ICIS 1981 Proceedings, paper 20 — https://aisel.aisnet.org/icis1981/20/ — 访问于 2026-10-14
4. Votito — "Stakeholder Mapping — Power Interest Matrix origins" — https://www.votito.com/methods/stakeholder-mapping/ — 访问于 2026-10-14
5. The Open Group — TOGAF Standard 10, Architecture Content ch. 3 "Architectural Artifacts" (Stakeholder catalog) — https://pubs.opengroup.org/togaf-standard/architecture-content/chap03.html — 访问于 2026-10-14（需登录）；TOGAF 9.2 ch. 31 — https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap31.html — 访问于 2026-10-14
6. TOGAF Exam Preparation Guide — "Stakeholder Management" (quadrant names, five stakeholder groups) — https://togafguide.wordpress.com/stakeholder-management/ — 访问于 2026-10-14
7. ISO/IEC/IEEE 42010 — conceptual model and stakeholder checklists — http://www.iso-architecture.org/ieee-1471/cm/ and http://www.iso-architecture.org/ieee-1471/ads/ — 访问于 2026-10-14
8. NN/g — "Stakeholder Analysis for UX Projects" — https://www.nngroup.com/articles/stakeholder-analysis/ — 访问于 2026-10-14
9. IIBA — BABOK Guide v3, 10.43 "Stakeholder List, Map, or Personas" — https://www.iiba.org/my-iiba/search-the-babok-guide/babok-guide/techniques/stakeholder-list-map-or-personas/ — 访问于 2026-10-14
10. The Open Group — ArchiMate 3.2 Specification, Appendix C "Example Viewpoints" (Stakeholder viewpoint) — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html — 访问于 2026-10-14（需登录；尚未对照现行规范原文核实）

## 示例 {#sample}
<!-- skill: path only -->
![A3b 示例：网店结账流程改版的权力–利益矩阵，以角色形式标绘财务、支付服务商、客服、仓储运营和数据保护](/samples/A3b-stakeholder-map.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
