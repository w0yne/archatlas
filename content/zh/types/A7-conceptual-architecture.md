---
code: A7
slug: conceptual-architecture
family: A
names:
  en: Conceptual architecture (solution overview)
  zh: 概念架构图（方案概览）
  aliases:
    en: [solution overview, solution concept diagram, high-level architecture, architecture on a page, block diagram, functional diagram]
    zh: [方案概览图, 方案总览, 高层架构图, 一页纸架构, 方案构想图, 概念架构图]
question: 这个方案由哪些大的部分组成，每个部分为业务做什么，它们彼此之间以及与外部世界之间如何依赖？
audiences: [leaders, business, architects]
levels: [concept]
phases: [initiate, design]
scope: 把一个方案在其上下文之下展开一层：明确边界内的 5–9 个与技术无关的构建块，用户、渠道和外部系统位于边缘。
formal: {kind: method, ref: 'TOGAF Solution Concept diagram (Phase A artifact, TOGAF 9.1 §35.6.2); informal notation; ArchiMate 3.2 Layered viewpoint as the formal option'}
neighbours: [A1, A8, C1, C2, C3, C5, I2]
status: draft
translationOf: en/types/A7-conceptual-architecture.md
sourceRev: 4e718f136c12c2c4c1d5f2226ea103f63e35b600
reviewed: false
---

# 概念架构图 / 方案概览图（Conceptual Architecture / Solution Overview）

**C5 的具名变体。** [进入逻辑架构图 → A7](/zh/types/c5-logical-architecture#variant-a7)。此兼容页保留独立画法、检查项、原锚点和历史下载。

> 用一页纸、以业务语言且不出现产品名称，展示一个方案由什么组成，让发起人和评审者在看详细视图之前先就整体形态达成一致。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
概念架构回答的是：“这个方案由哪些大的部分组成，每个部分做什么，它们彼此如何依赖？”按 ISO/IEC/IEEE 42010 的说法，它是一种概览视点，关注点是范围、主要构建块和方案思路。TOGAF 将其定义为**方案构想图**（Solution Concept diagram），属于阶段 A 的制品：“方案的高层定向”，明确是一张“铅笔草图”，用于“让干系人快速入门并达成一致” [1][2]。C4 model 没有概念层级；A7 位于系统上下文（C2）视图和容器（C3）视图之间 [3]。它不包含产品、版本、协议和部署，也不包含业务能力清单（A1）、产品功能分解（B3）、流程步骤（A5、E4）以及从现状到目标态的路径（A8）。

**本站采用的定义：***表示法*是非正式的（方框、分组、箭头），但*制品*是有定义的（TOGAF 方案构想图）。Azure 把这种与技术无关的层级称为“框图或功能图” [5]。arc42 将它与其构建块视图（building block view）的第 1 层白盒对应 [13]，DoDAF OV-1 是一种相关的作战概念图 [8]。“Marketecture”（营销架构图）是对其劣质版本的贬称 [17]。本页中的 ArchiMate 引用均依据 **ArchiMate 3.2**；参见“表示法”一节中的版本说明。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：**高管、发起人、指导委员会与评审委员会、客户方干系人、新成员；架构师把它用作架构文档包的封面页。
- **场景：**愿景工作坊上让发起人就要建设的内容达成一致（如网店平台重构）；方案建议书中的“一页纸方案”；架构评审的开场页；新人入职；某种反复出现的方案模式的参考图 [14][15][16]。
- **不适用的情况：**工程师需要接口、部署或调用顺序（C3、C5、G1、E1）；真正的问题只是范围（C2）或整个应用资产（C1）；要讲的是迁移（A8）；内容是业务能力清单（A1）或产品功能清单（B3）。
- **与相邻类型的区别：**
  - 受众只需要了解范围时，选 **C2 系统上下文图**；A7 把这个黑盒打开一层。
  - 涉及整个企业的众多系统时，选 **C1 应用全景图**；A7 只针对一个方案。
  - 表达业务必须具备哪些能力时，选 **A1 能力图**；A7 展示由哪些部分来交付这些能力 [9]。
  - 要讲的是随时间推移的变化时，选 **A8 目标架构与路线图**；把这张 A7 复用为目标图景。
  - 一旦读者问起哪个服务调用哪个 API，就改用 **C3 / C5**。
  - 需要在一张视图中用正式的 ArchiMate 关系呈现业务、应用和技术元素时，选 **I2**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：**注明范围和状态的标题；明确的方案边界；5–9 个构建块，用业务语言的名词命名（这是工作经验法则，不是标准）；位于边缘的用户 / 渠道；外部系统各画为单个方框；主要依赖箭头；覆盖每种颜色、形状、边框和线型的**图例** [4][6]。
- **可选：**一种分层方案（渠道 / 应用 / 平台 / 数据 / 基础设施，或 ArchiMate 的业务 / 应用 / 技术），对所有系统统一适用；每个构建块最多 3 个标签；一条带编号的主线流程；新建与既有部分的区分突出；横切带（身份、安全、可观测性）。
- **线条：**有向箭头从请求方指向提供方；不用双向箭头（两个方向都重要时画两条流）；含义不明显时用动词短语标注；只有在图例说明的情况下才使用不同线型 [4][5]。
- **细节程度：**比上下文低一层；技术最多以通用类别出现（“搜索索引”“消息队列”），绝不出现产品名称 [5]。
- **命名：**同级构建块属于同一类（全是组件或全是应用，绝不与功能或步骤混杂）；全称加缩写只出现一次 [4]。
- **形式化选项：**ArchiMate 3.2 的**分层视点**（Layered viewpoint）横跨业务、应用和技术 [6]；ArchiMate 2.x 曾有一个面向非架构师、采用简化表示法的*入门*视点（Introductory viewpoint）[7]。
- **ArchiMate 版本说明：**ArchiMate 4 已于 2026 年 4 月 27 日发布 [10]。一份厂商综述称“层”（layers）改为“域”（domains），且概念集有所精简 [11]；发布公告本身并未列出这些细节，它们**尚未对照现行规范文本核实**。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践

1. 让深度与受众匹配，并写明面向哪类受众：从上下文开始，再往下一层；“分层展开，不要堆砌” [5]。
2. 让图自解释：标题、图例、有类型和名称的元素、带标签的箭头；按 C4 model 的评审清单检查 [4]。
3. 图内和图间的表示法保持一致：同类事物使用相同的颜色、大小写、尺寸和线宽；同级元素外观一致 [4][5]。
4. 抽象的同时保持准确：“不要为不必要的简化牺牲准确性”；通用构建块使用通用图形，而不是厂商图标 [5]。
5. 把理由放在图外：决策写入方案策略正文或 ADR [12]；构建块名称要能追溯到 C2 和 C3 视图。

### 反模式

1. “Marketecture”：只有图标、方框之间没有连线、箭头无标签、抽象层级含混 [17]。
2. 把功能清单画成方框。业务能力应画成能力图（A1），产品功能应画成功能树（B3）；架构视图展示的是组成部分，功能最多作为标签出现 [9]。
3. 同级元素抽象层级混杂，例如一行里同时有一个容器、一个参与者和一个流程步骤 [4]。
4. 方框内写句子或要点列表，图标只作装饰而不表达含义 [5]。
5. 把非重点的子系统完整画出，或者在图上写工作备注（“TBD”“待定”），而不是使用“计划中”之类的图例类别 [4]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [C4 model, System context diagram](https://c4model.com/diagrams/system-context) 与 [System landscape diagram](https://c4model.com/diagrams/system-landscape) — 关于 A7 前后层级最清晰的公开参考：标题、图例、带标签的单向箭头；CC BY 4.0 [18][19]。
- [The Open Group, TOGAF 9 and ArchiMate 1.0 white paper](https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf) — 分层的基线视图与目标视图，所有应用采用同一种分层逻辑；版权归 Open Group [20]。
- [SAP AppHaus, Generate a Solution Concept Diagram](https://apphaus.sap.com/resource/solution-concept-diagram) — 一套实用方法：从能力推导构建块、请求→响应箭头、由干系人验证 [9]。
- [Azure Architecture Center, Browse architectures](https://learn.microsoft.com/en-us/azure/architecture/browse/) — 概览图加带编号的数据流列表；大多处于组件层级，宜参考其结构和图注写法 [15]。
- [AWS Reference Architecture Diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/) — 一页一图、一条带编号的流程；属于物理层级，仅作版式参考 [14]。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定框架：受众、目的、状态（现状或目标）以及方案边界；先写标题。
2. 从需求和能力中列出候选构建块；合并或拆分为 5–9 个同类构建块，每个用 1–4 个词的名词命名。
3. 选定一种分层方案，自上而下：用户 / 渠道 → 方案服务 → 共享平台 → 数据。外部系统位于右侧或底部、边界之外。只有存在一条主导流程时才采用从左到右的布局。
4. 每个构建块恰好放在一个层中，位于边界内或边界外；非重点子系统折叠为一个方框。
5. 最多添加约 10 条有向箭头，请求方 → 提供方；分组级连线止于分组边框；只为含义不明显的箭头加标签；可选地为一条主线流程编号。
6. 文字：构建块名称、可选的一行角色说明、不超过 3 个标签；不写句子；字号层级为标题 > 层标签 > 构建块名称 > 标签。
7. 颜色：默认中性色；方案自有（或新建）的构建块用一种强调色；共享组件用一种样式，且处处一致；外部系统用灰色；颜色与边框或图案搭配使用。
8. 添加图例（颜色、边框、线条、编号）；与上层的 C2 以及下层的 C3 / C5 交叉核对名称。

**自检清单**
- [ ] 标题说明范围以及现状 / 目标态；没有内部版本标签。
- [ ] 5–9 个同类构建块，用受众的语言命名。
- [ ] 方框内没有功能清单、要点或句子；除非有要求，没有产品名称、协议或端口。
- [ ] 边界明确；每个元素恰好属于一个分组，或标为外部。
- [ ] 箭头有方向，终点落在其所指对象上，含义不明显处有标签。
- [ ] 图例解释了每种颜色、形状、边框和线型；同级元素共用一种样式。
- [ ] 图标只用在承载含义的地方。
- [ ] 构建块名称与相邻的 C1 / C2 / C3 视图一致。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **有用：**README 和 `docs/` 中的概述以及现有图表；顶层模块和可部署单元（构建文件、compose 文件、Helm chart、列出服务和数据存储的 IaC）；指明外部系统的客户端 SDK 和配置（支付服务商、仓储系统）；路由和网关定义（渠道）；ADR（方案策略）；CODEOWNERS（与团队对应的构建块）。
- **需要问人：**构建块的业务语言名称、哪些部分对这批受众重要、尚不存在的目标构建块，以及业务眼中的归属。
- 代码提供的是物理层面的证据；要把它提升到概念层级，并与发起人或架构师确认结果。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 谁会读这张图？读完后他们应理解或决定什么？（发起人和评审者，业务 + IT 概览深度）
2. 现状还是目标状态？方案边界在哪里？（目标状态；边界 = 本团队建设或改动的系统）
3. 哪些部分是重点？哪些相邻系统只以单个方框出现？（重点放在方案自有的构建块；其余各画一个方框）
4. 采用哪种分层方案？是否要区分新建与既有部分？（渠道 / 服务 / 平台 / 数据；如有复用则区分）
5. 使用技术类别（“搜索索引”），还是完全不涉及技术？（只用通用类别）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A7.json` · 布局模板：`layered` · 类型为 `layer` 的分组在 `boundary` 分组内渲染为水平横带；构建块在每条横带中为等宽列；外部系统放在边界之外。

## 来源 {#sources}
<!-- skill: omit -->
1. The Open Group, TOGAF Version 9.1 (2011), §35.6.2 Solution Concept Diagram (evaluation copy, third-party hosted) — http://www.crvs-dgb.org/wp-content/uploads/2015/07/I112.pdf — 访问于 2026-10-14
2. The Open Group, World-Class Enterprise Architecture: Framework Guidance and TOGAF 9 Example (white paper, 2010) — https://pubs.opengroup.org/onlinepubs/7698999699/toc.pdf — 访问于 2026-10-14
3. C4 model, Abstractions — https://c4model.com/abstractions — 访问于 2026-10-14
4. C4 model, Notation and Review checklist — https://c4model.com/diagrams/notation ; https://c4model.com/diagrams/checklist — 访问于 2026-10-14
5. Microsoft, Create architecture design diagrams, Azure Well-Architected Framework — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — 访问于 2026-10-14
6. Linked.Archi, ArchiMate 3.2 Example Viewpoints (secondary listing of the spec appendix) — https://meta.linked.archi/archimate3/viewpoints — 访问于 2026-10-14
7. Archi User Guide, Sketch View (quotes the ArchiMate 2.x Introductory viewpoint) — https://www.archimatetool.com/downloads/archi/Archi%20User%20Guide.pdf — 访问于 2026-10-14
8. The Open Group, TOGAF 9 and the US DoDAF 2.0 (white paper; OV-1 High-Level Operational Concept Graphic, a neighbour) — https://pubs.opengroup.org/onlinepubs/7698999499/toc.pdf — 访问于 2026-10-14
9. SAP AppHaus, Generate a Solution Concept Diagram — https://apphaus.sap.com/resource/solution-concept-diagram — 访问于 2026-10-14
10. The Open Group, The Open Group Announces ArchiMate 4 Specification (press release, 27 April 2026) — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — 访问于 2026-10-14
11. Bizzdesign (M. Lankhorst), ArchiMate 4 Specification: What Changed from Version 3.2? — https://bizzdesign.com/blog/archimate-4-changes — 访问于 2026-10-14
12. arc42, Section 4: Solution Strategy — https://docs.arc42.org/section-4/ — 访问于 2026-10-14
13. arc42, Section 5: Building Block View — https://docs.arc42.org/section-5/ — 访问于 2026-10-14
14. AWS Reference Architecture Diagrams — https://docs.aws.amazon.com/reference-architecture-diagrams/ — 访问于 2026-10-14
15. Azure Architecture Center, Browse architectures — https://learn.microsoft.com/en-us/azure/architecture/browse/ — 访问于 2026-10-14
16. Google Cloud Architecture Center — https://cloud.google.com/architecture — 访问于 2026-10-14
17. Simon Brown, Speaking (talk abstracts on "boxes and arrows" and "Marketecture") — https://simonbrown.je/speaking — 访问于 2026-10-14
18. C4 model, System context diagram — https://c4model.com/diagrams/system-context — 访问于 2026-10-14
19. C4 model, System landscape diagram — https://c4model.com/diagrams/system-landscape — 访问于 2026-10-14
20. H. Jonkers, E. Proper, M. Turner, TOGAF 9 and ArchiMate 1.0 (Open Group white paper, 2009) — https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A7 示例：网店的概念架构，含渠道、应用和数据](/samples/A7-conceptual-architecture.svg)
*网店的概念架构：一个边界内有渠道、应用、数据三个条带，构建块为商城前台、订单、商品目录和商城数据。订单向边界外的支付服务商发出支付请求。*
