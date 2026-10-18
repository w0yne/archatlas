---
code: A8
slug: target-roadmap
family: A
names:
  en: Target architecture and transition roadmap
  zh: 目标架构与演进路线图
  aliases:
    en: [architecture roadmap, transition architecture, migration roadmap, as-is to-be roadmap, plateau diagram, baseline / target / transition architecture, as-is / to-be roadmap, migration view, capability roadmap]
    zh: [演进路线图, 架构路线图, 迁移路线图, 过渡架构, 现状 / 目标 / 过渡架构, 迁移视图, 平台期图, 能力路线图, 稳定态图]
question: 我们现在在哪里，要去哪里，中间有哪些稳定的过渡状态，哪些工作把我们从一个状态推进到下一个状态，按什么顺序，为什么？
audiences: [leaders, architects]
levels: [strategy]
phases: [initiate, design]
scope: 一个方案或领域在给定时间范围内从基线到目标的演进：各个状态、状态之间的工作包、它们的依赖关系以及每个状态交付的价值。
formal: {kind: standard, ref: 'TOGAF ADM Architecture Roadmap and Transition Architectures (Phases E–F, TOGAF 9.1 text); ArchiMate 3.2 Implementation & Migration elements'}
neighbours: [A1, A7, C1]
status: draft
translationOf: en/types/A8-target-roadmap.md
sourceRev: 88db750
reviewed: false
---

# 目标架构与演进路线图（Target Architecture & Transition Roadmap）

> 用同一套视觉语法画出基线、一个或多个可行的过渡状态和目标，以及把架构从每个状态推进到下一个状态的工作包。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
路线图回答的是：“我们现在在哪里，要去哪里，中间有哪些稳定的步骤，哪些工作推动我们前进？”按 ISO/IEC/IEEE 42010 的说法，它是一种演进 / 迁移视点，关注点是顺序、依赖、每一步的价值与风险，以及每个中间状态的可行性。在 TOGAF 中，阶段 B–D 制定基线架构和目标架构及其差距分析，阶段 E 把差距整合为工作包并识别**过渡架构**（Transition Architecture），阶段 F 最终确定**架构路线图**（Architecture Roadmap）[1][2]。在 ArchiMate 中，它对应迁移视点或实施与迁移视点 [4]。每个过渡状态都是一个决策点：一个连贯的架构，干系人可以在此停下而仍保有已获得的价值 [1][9]。它不包含详细设计、任务级进度安排和论证性的文字。

**本站采用的定义：** **架构路线图**在时间线上展示工作包和过渡架构，并“突出各个工作包在每个阶段的业务价值” [1]。**实施与迁移计划**（Implementation and Migration Plan）是另一个 TOGAF 交付物：即进度计划，包含时间、成本、资源和里程碑 [1][2]。任务甘特图属于那份计划，而不是这张图。TOGAF 要求“一个或多个”过渡架构，而不是固定数量 [1]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：**高管与发起人、架构委员会、项目组合与项目群经理、资金审批委员会，以及查看自身项目所处位置的交付负责人。
- **场景：**网店从单体迁移到模块化服务，新旧系统并行运行（绞杀者模式，strangler fig）[11][14]；合并两套订单系统，存在多条可选过渡路径 [5]；基于能力的投资规划 [1][10]；年度路线图更新；分批次上云，每一批都以一个稳定的混合状态结束。
- **不适用的情况：**只有一次发布，没有有意义的中间状态（画一张标注“目标”的 A7 即可）；受众需要任务日期和人员安排（用项目计划）；目标仍未确定（先用 A7 的多个备选方案把目标定下来）。
- **与相邻类型的区别：**
  - 表达*一个*状态的图景时，选 **A7 概念架构**；A8 把两个或更多状态（或它们之间的差异）放到时间轴上。
  - 作为基于能力的规划的输入时，选 **A1 能力图**（带热力着色）；A8 展示随时间推进的增量。
  - 表达某一时间点的应用资产时，选 **C1 应用全景图**；基线和目标的 C1 视图可以作为 A8 的一部分。
  - **Wardley 地图**帮助判断目标应该是什么；它不展示过渡状态 [12]。
  - **产品路线图**以功能或成果为导向，归产品团队所有；可以借用它的成果式表述来命名步骤 [13]。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：**基线和目标，以紧凑的图景或构建块列表呈现，形状和分层与 A7 / C1 相同；1–N 个过渡状态，每个以其成果命名（“结账作为独立服务运行”，而不是“第二阶段”），并注明时间范围和关键变化；状态之间的工作包，带依赖箭头；每一步所弥合的差距 [1][3]。
- **图例（必需）：**新建 / 变更 / 保留 / 退役，对应 TOGAF 的新建 / 保留 / 过渡 / 替换标记 [8]；各类线条的含义；已承诺与指示性的区分。
- **可选：**按领域或能力划分的泳道；里程碑和实施事件；每个状态的业务价值或 KPI；临时（过渡性）组件，须明确标注 [14]；决策未定时的备选路径 [5]；风险标记。
- **配套表格** [8]：差距分析矩阵（基线 × 目标构建块，含“新增”和“消除”）；合并后的差距、解决方案与依赖矩阵；过渡架构状态演进表（服务 × 过渡，单元格标注新建 / 保留 / 过渡 / 替换）。
- **ArchiMate 3.2 元素** [3]：稳定态（Plateau，“在有限时间段内存在的、相对稳定的架构状态”）、差距（Gap）、工作包（Work Package）、交付物（Deliverable）、实施事件（Implementation Event）。稳定态之间通常以触发关系串联，差距与它所比较的两个稳定态相关联，工作包实现交付物；这是工具中的常见解读，**尚未对照现行规范文本核实**。
- **ArchiMate 版本说明：**ArchiMate 4 已于 2026 年 4 月 27 日发布 [6]。一份厂商综述称差距（Gap）已被弃用（改为对两个稳定态之间差异的评估（Assessment）来建模），且“层”改为“域” [7]；发布公告并未列出这些细节，因此它们**尚未对照现行规范文本核实**。本页依据 ArchiMate 3.2；正式图表应注明所用版本。
- **时间轴：**按季度或年份如实标注间距；超出承诺期限的事项标为指示性。工作包是有名称的工作单元，而不是任务。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践

1. 每个中间状态都能独立成立：可运行、有价值，并且可以作为停止点 [1][9][10]。
2. 用成果为步骤命名，而不是“第 n 阶段”或功能清单 [13]。
3. 明确画出依赖关系；工作的顺序取决于选择哪条过渡路径 [5][8]。
4. 为过渡性架构做规划并把它画出来；隐藏的临时集成会让路线图看起来比实际更便宜 [11][14]。
5. 每个状态都复用 A7 / C1 的形状、分层和颜色，使变化一目了然；明确标注基线、每个过渡状态和目标 [5]。

### 反模式

1. 只有目标，没有路径；或者从基线一步跳到目标的“大爆炸”式切换 [11]。
2. 不可行的中间状态：某一步无法独立运行，或要等到后续步骤才产生价值 [1]。
3. 用功能 / 日期清单或项目甘特图冒充架构路线图 [1][13]。
4. 每个状态使用不同的表示法，以致没人能看出变化了什么 [5]。
5. 在时间轴远端给出虚假的精确度，或者在图上写工作备注（“TBD”“待厂商确认”）和内部版本标签。

## 范例 {#exemplars}
<!-- skill: omit -->
- [The Open Group, TOGAF 9 and ArchiMate 1.0 white paper](https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf) — 图 22 用完全相同的形状画出基线、目标和两个备选的过渡稳定态；版权归 Open Group [5]。
- [TOGAF 9.1 Migration Planning Techniques (secondary mirror)](https://coe.qualiware.com/resources/togaf/9-1/part3-admguide/migration-planning-techniques) — 状态演进表和差距分析表格，带新建 / 保留 / 过渡 / 替换标记 [8]。
- [Martin Fowler, Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html) — 渐进式替换，其中“投入和回报逐步且可见地发生” [11]。
- [Cartwright, Horn & Lewis, Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html) — 带有日后会被丢弃的临时组件的中间状态 [14]。
- [Linked.Archi, ArchiMate 3.2 Example Viewpoints](https://meta.linked.archi/archimate3/viewpoints) — 迁移视点和实施与迁移视点的元素集；可作为正式稳定态图的检查清单 [4]。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确认各个状态：基线的日期和范围、目标的时间范围，以及受众关心多少个过渡状态（通常 2–4 个；TOGAF 只要求一个或多个）。
2. 为基线和目标绘制或复用 A7 / C1 视图，使用相同的构建块和分层；列出差距（新建 / 变更 / 保留 / 退役）。
3. 把差距归并为工作包，并注明它们之间的依赖。
4. 在存在连贯且有价值的架构之处切分过渡状态；每个状态以其成果命名，列出 2–4 项关键变化以及任何临时组件。
5. 布局 (a) 面向高管的**状态条带**：缩略图从左到右排列，基线 → T1 → T2 → 目标，工作包放在每个箭头下方。布局 (b) 面向项目组合经理的**泳道路线图**：每个领域一行，x 轴为时间，工作包为横条，稳定态为里程碑线。
6. 文字：稳定态标题不超过 6 个词；工作包为 2–5 个词的名词短语；每个状态最多一个价值标签；不写段落。
7. 颜色：只用一种编码，即每个构建块的状态：新建（强调色）、变更（浅强调色）、保留（中性色）、退役中（灰色斜线填充）、临时（虚线边框）；超出承诺期限的部分用虚线框出“指示性”区域；颜色与图案搭配使用。
8. 图例放在右下角；标题注明范围和时间范围，例如“网店：2026–2028 演进路线图”。差距矩阵或状态演进表作为附录提供，不放进图中。

**自检清单**
- [ ] 基线、每个过渡状态和目标都有标注；目标不是唯一的状态。
- [ ] 每个过渡状态都可运行，并写明其交付的价值。
- [ ] 所有状态共用一套形状、分层和颜色图例。
- [ ] 每个差距都由一个工作包弥合，每个工作包都弥合一个差距。
- [ ] 依赖关系已画出，顺序与之相符。
- [ ] 临时组件可见且有标注。
- [ ] 超出承诺期限的事项标为指示性。
- [ ] 没有任务、人天或设计细节；图上没有工作备注或版本标签。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **基线：**来自 IaC、Helm 或 compose 文件的可部署单元、数据存储和集成；依赖清单；`@deprecated` 标记和已弃用的模块。
- **中间状态与方向：**让新旧路径并行运行的功能开关；迁移脚本；网关或代理中的绞杀者路由规则；ADR（“我们将替换 X”）；史诗（epic）、里程碑、发布分支和标签。
- **需要问人：**目标状态本身、每一步的业务价值、优先级和资金、承诺期限，以及对组织变革的依赖。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 目标的时间范围和范围是什么？目标已达成共识，还是仍是一组备选方案？（已达成共识的目标，2–3 年时间范围）
2. 有多少个中间状态是重要的？是什么让每个状态值得停下来？（2 个过渡状态，各带一个价值标签）
3. 谁来读：高管、项目组合经理，还是两者都有？（面向高管的状态条带）
4. 哪些硬性约束决定了顺序：合同、监管期限、厂商支持终止？（不预设约束；只考虑依赖关系）
5. 用正式的 ArchiMate（稳定态、工作包；3.2 或 4），还是带图例的简化约定？（简化约定，采用 ArchiMate 3.2 术语）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A8.json` · 布局模板：`tree` · 各状态是从左到右排成一条链的 `state` 节点（基线 → 目标），工作包是相邻状态之间的 `task` 节点，以 `dependency` 边相连；节点的 `style`（`planned`、`shared`、`external`）标示构建块的状态。

## 来源 {#sources}
<!-- skill: omit -->
1. The Open Group, TOGAF Version 9.1 (2011): Ch. 13 Phase E, Ch. 14 Phase F, §3.74 Transition Architecture, §36.2.7 Architecture Roadmap, Ch. 32 Capability-Based Planning (evaluation copy, third-party hosted) — http://www.crvs-dgb.org/wp-content/uploads/2015/07/I112.pdf — 访问于 2026-10-14
2. The Open Group, World-Class Enterprise Architecture: Framework Guidance and TOGAF 9 Example (2010) — https://pubs.opengroup.org/onlinepubs/7698999699/toc.pdf — 访问于 2026-10-14
3. The Open Group, ArchiMate 3.2 Specification Reference Cards (N221, 2022) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — 访问于 2026-10-14
4. Linked.Archi, ArchiMate 3.2 Example Viewpoints — https://meta.linked.archi/archimate3/viewpoints — 访问于 2026-10-14
5. H. Jonkers, E. Proper, M. Turner, TOGAF 9 and ArchiMate 1.0 (Open Group white paper, 2009) — https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf — 访问于 2026-10-14
6. The Open Group, The Open Group Announces ArchiMate 4 Specification (press release, 27 April 2026) — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — 访问于 2026-10-14
7. Bizzdesign (M. Lankhorst), ArchiMate 4 Specification: What Changed from Version 3.2? — https://bizzdesign.com/blog/archimate-4-changes — 访问于 2026-10-14
8. TOGAF 9.1 Part III Ch. 27 Gap Analysis and Ch. 28 Migration Planning Techniques (secondary HTML mirror) — https://coe.qualiware.com/resources/togaf/9-1/part3-admguide/migration-planning-techniques — 访问于 2026-10-14
9. Conexiam, TOGAF ADM Phase E – Build the Architecture Roadmap — https://conexiam.com/togaf-adm-phase-e-build-the-architecture-roadmap — 访问于 2026-10-14
10. Conexiam, Unlocking the Power of Capability-Based Planning: A Quick Guide — https://conexiam.com/unlocking-the-power-of-capability-based-planning-a-quick-guide — 访问于 2026-10-14
11. Martin Fowler, Strangler Fig Application — https://martinfowler.com/bliki/StranglerFigApplication.html — 访问于 2026-10-14
12. Learn Wardley Mapping, Introduction — https://learnwardleymapping.com/introduction/ — 访问于 2026-10-14
13. Marty Cagan (SVPG), The Alternative to Roadmaps (2015) — https://www.svpg.com/the-alternative-to-roadmaps/ — 访问于 2026-10-14
14. I. Cartwright, R. Horn, J. Lewis, Transitional Architecture, Patterns of Legacy Displacement (2022) — https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A8 · 企业服务助手](/samples/ai-service-assistant/A8/zh/diagram.svg)
*只读回答、审批写入及评测门禁是示意过渡稳定态，不是已承诺日期。每个工作包仅引入下一稳定态所需能力。*

[SVG](/samples/ai-service-assistant/A8/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/A8/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

[历史 shop 回归样例](/samples/A8-target-roadmap.svg) · [全部29幅视图](/zh/use/ai-service-assistant) · [示意假设](/zh/use/ai-service-assistant-assumptions).
