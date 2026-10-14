---
code: D2
slug: data-flow-diagram
family: D
names:
  en: Data flow diagram (DFD)
  zh: 数据流图（DFD）
  aliases:
    en: [DFD, data flow chart, data flow model, process model (structured analysis), bubble chart, context diagram (top level)]
    zh: [数据流程图, 数据流向图, 0 层图]
question: 数据从哪里来，经过哪些加工被转换，保存在哪里，又流向哪里？
audiences: [architects, business, security]
levels: [logical]
phases: [requirements, design]
scope: 一个系统，每张图一个层级：一张上下文图，或对单个加工的一次分解（3-9 个加工）
formal: {kind: method, ref: 'Structured Analysis: DeMarco 1978 (Yourdon/DeMarco symbols) and Gane & Sarson 1979; no ISO or OMG standard. Threat-model dialect adds trust boundaries'}
neighbours: [C2, D1, D3, E2, F2]
status: draft
translationOf: en/types/D2-data-flow-diagram.md
sourceRev: 674f366
reviewed: false
---

# 数据流图（Data Flow Diagram）

> 一张描绘哪些数据进入系统、经过哪些加工被转换、在哪里存放、从哪里离开的图，不含控制流，也不含技术。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 数据从哪里来，什么在转换它，它存储在哪里，流向哪里？
- **视点：** 一种功能性的信息流视点。它把系统建模为对数据的一系列转换，不考虑顺序、时序、条件和技术。正因如此，它通常是威胁建模的基础：攻击沿着数据走，并跨越信任边界（trust boundary）[6][7]。ArchiMate 用行为元素之间的 *flow* 关系和对数据对象的 *access* 关系表达同样的思想 [9]。
- **起源：** 20 世纪 70 年代末的结构化分析（Structured Analysis）：Tom DeMarco（1978）[1][2]、Yourdon 和 Constantine，以及 Chris Gane 和 Trish Sarson（1979）[3]。没有国际标准；DFD 是一种方法约定，有一套广为人知的规则。
- **本站采用的定义：** *上下文图*把系统画成一个加工。许多文献称之为"0 层"（level 0）[5][10]；另一些则把第一次分解称为"图 0"（diagram 0）。请写明你采用的约定。
- **不包含：** 控制流和判断（E1、E2）、职责（E4、A5）、数据结构（D1）、部署（G1）、随时间变化的血缘与归属（D3）。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 架构师、分析师、安全评审人员、隐私与审计人员。
- **典型场景：**
  1. 分析网店订单服务如何接收订单、检查库存和支付并保存结果（逻辑层，与技术无关）。
  2. 威胁建模工作坊：一张 1 层 DFD，在互联网、边缘、内部网络和支付服务商之间画出信任边界 [6][7]。
  3. 隐私梳理：客户个人数据从哪里进入、存储在哪里、由谁接收。
  4. 集成分析：订单、支付和仓库发货之间交换哪些数据项。
- **不适用的情况：** 调用顺序或重试（E1）；分支逻辑（E2）；团队之间的交接（E4、A5）；运行时基础设施（G1）。
- **与相邻类型的区别：**
  - 关注人员和系统时，选 **C2 系统上下文图**；关注数据项时，选 0 层 DFD。
  - 要跨作业和运行追踪具体数据集时，选 **D3 血缘**；DFD 是设计期的逻辑模型。
  - 走安全流程时，选 **F2 威胁模型**；它使用本页的方言（DFD 加信任边界），并添加威胁标注。
  - 表达控制流时，选 **E2 活动流程图**。DFD 的箭头是数据，从不表示"然后"。
  - 问题是有哪些业务对象、彼此如何关联，而不是数据如何流动时，选 **D1 实体关系图**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 一种方法约定；选定一套符号并坚持使用 [4][5]。
  - **Yourdon/DeMarco：** 圆（气泡）= 加工；两条平行线 = 数据存储；矩形 = 外部实体。
  - **Gane & Sarson：** 圆角矩形 = 加工（带编号）；开口矩形 = 数据存储（带 D1 这样的编号）；正方形 = 外部实体。
- **必需的四类元素 [4][5][10]：**
  - **外部实体：** 范围之外的数据源或数据汇。
  - **加工：** 转换数据；动词加宾语（"校验订单"），编号为 1、2、2.1。
  - **数据存储：** 静止的数据；复数名词加编号（"Orders"，D1）。
  - **数据流：** 箭头上标注*数据项*（名词："订单表单""支付确认"），绝不写动作。
- **威胁模型补充：** 在权限或归属发生变化的地方画**信任边界**（虚线或框）；可选地在跨边界的数据流上标注协议和认证 [6][7][8]。
- **有效性规则 [10]：**
  - 平衡：子图的外部输入和输出等于其父加工的数据流。
  - 每个加工至少有一个输入和一个输出（没有只有输入的"黑洞"，也没有只有输出的"奇迹"）。
  - 不存在存储到存储、实体到实体或实体到存储的数据流；中间必须有一个加工。
  - 数据流是单向的；请求数据和响应数据画两条箭头。
- **图例：** 符号集、层级约定以及信任边界的画法。不要混用符号集。
- **规模：** 每张图 5-9 个加工是从业者的经验法则；与其挤在一起，不如分解。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **从上下文图开始，** 先就范围和外部实体达成一致，再逐层分解。
2. **数据流用数据名词命名，加工用动宾结构命名；** 为加工编号，以便追溯到需求或威胁。
3. **每张图保持 5-9 个加工；** 分解而不是堆砌。
4. **安全评审时画出信任边界，** 并让 DFD 与系统放在一起、随系统一起更新；pytm 等图即代码工具可以做到这一点 [7][12]。
5. **隐私评审时** 为承载个人数据或敏感数据的数据流加标记，并在图例中解释该标记。

### 反模式
1. **把控制流当作数据流：** 箭头标注"然后""成功时""调用"。
2. **缺少加工：** 存储直接连到另一个存储或外部实体。
3. **黑洞和奇迹：** 没有输出或没有输入的加工。
4. **层级不平衡：** 子图引入了父图中没有的数据流。
5. **在逻辑 DFD 上出现技术名称**（消息代理、对象存储），或用一张包含 30 个加工的巨图代替分层。只在标为"物理 DFD"的图上写技术名称。

## 范例 {#exemplars}
<!-- skill: omit -->
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — 解释了为什么 DFD 是威胁建模中最常用的系统模型，以及应展示哪些元素（包括信任边界）；OWASP 网站采用 CC 许可。
- [Microsoft Learn: create a threat model using data-flow diagram elements](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/) — 一个免费课程模块，定义了每种元素以及信任边界的语义。
- [Lucidchart: data flow diagram symbols](https://www.lucidchart.com/pages/data-flow-diagram/data-flow-diagram-symbols) — 并排展示各套符号；适合用来做图例。厂商内容。
- [University of Cape Town notes, chapter 6](https://www.cs.uct.ac.za/mit_notes/software/pdfs/Chp06.pdf) — 关于上下文图、分层和平衡的严谨教材（已核对平衡和"level 0"的措辞）。
- [Visual Paradigm: what is a data flow diagram](https://www.visual-paradigm.com/guide/data-flow-diagram/what-is-data-flow-diagram/) — 从上下文图到 2 层的分层实例，附命名规则。厂商内容。
- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) — 一个开源工具，可绘制威胁模型 DFD，并按元素列出威胁。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定目的：分析（逻辑层，与技术无关）、安全评审（加信任边界）或隐私（标记个人数据流）。声明符号集和层级约定。
2. 先画上下文图：一个加工（即系统本身），外部实体分列左右，数据流用名词标注。
3. 1 层：3-9 个带编号的加工；输入在左，输出在右，存储放在中间或下方一行；存储只能经由加工访问。
4. 布局：从左到右，外部实体在两侧；信任边界用虚线矩形框住各区域（互联网、边缘、内部、合作方）。
5. 文字：加工 = 动词 + 宾语，最多 4 个词；数据流 = 数据名词，最多 3 个词；存储 = 复数名词加编号。
6. 颜色：元素用中性色；跨边界或敏感的数据流用一种强调色，并在图例中说明。
7. 渲染前先与父图核对平衡；有不一致先修正。
8. 需求或威胁的引用作为编号注释放在图外。

**自检清单**
- [ ] 只有四类元素，安全 DFD 再加上信任边界。
- [ ] 每个箭头都带数据名词；没有"然后""调用"或"下一步"。
- [ ] 没有存储到存储、实体到实体或实体到存储的数据流。
- [ ] 每个加工都既有输入又有输出。
- [ ] 子图与其父加工保持平衡。
- [ ] 层级已编号，并写明了层级约定。
- [ ] 只用一套符号，并配图例。
- [ ] 每张图最多 9 个加工。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **外部实体：** 入站路由和处理器、webhook 接收端、消息消费者；出站 SDK 客户端和 base-URL 配置表明数据流向哪里。
- **存储：** 数据库和 ORM 模型、对象存储桶、缓存。
- **数据流上的数据项：** 请求和响应 schema（OpenAPI、DTO）、事件载荷 schema。
- **信任边界：** 网络和基础设施即代码（子网、安全组、ingress）、认证中间件、租户检查。
- 代码展示的是*调用*：把它们转换为数据移动，去掉没有移动有意义数据的调用。
- **必须来自人：** 哪些数据在业务意义上是敏感的，以及预期的逻辑分解。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 这张 DFD 用于什么：分析、威胁建模会议还是隐私评审？（分析）
2. 系统边界是什么，外部实体有哪些？（订单服务；客户、支付服务商、仓库）
3. 逻辑（与技术无关）还是物理（具名的存储和服务）？（逻辑）
4. 哪个层级：仅上下文图、1 层，还是深入单个加工？（上下文图加 1 层）
5. 用哪套符号，哪些数据应标为敏感？（Gane & Sarson；个人数据和支付数据）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/D2.json` · 布局模板：`nested` · 外部实体是 `external` 节点，加工是 `component` 节点，存储是 `store` 节点（存储编号如 D1 放在 `sub`），信任边界是围绕各区域的 `boundary` 分组，数据流是 `data` 边，其 `label` 为数据名词，`dir` 为 `->`。

## 来源 {#sources}
<!-- skill: omit -->
1. T. DeMarco, *Structured Analysis and System Specification* (Google Books record) — https://books.google.com/books/about/Structured_Analysis_and_System_Specifica.html?id=7o0-AAAAIAAJ — 访问于 2026-10-14
2. Wikipedia, "Structured analysis" (secondary source) — https://en.wikipedia.org/wiki/Structured_analysis — 访问于 2026-10-14
3. C. Gane, T. Sarson, *Structured Systems Analysis: Tools and Techniques*, 1979 (ACM DL record) — https://dl.acm.org/doi/10.5555/578524 — 访问于 2026-10-14
4. Lucidchart, "Data Flow Diagram Symbols" — https://www.lucidchart.com/pages/data-flow-diagram/data-flow-diagram-symbols — 访问于 2026-10-14
5. Visual Paradigm, "What is Data Flow Diagram?" — https://www.visual-paradigm.com/guide/data-flow-diagram/what-is-data-flow-diagram/ — 访问于 2026-10-14
6. Microsoft Learn, "Create a Threat Model Using Data-Flow Diagram Elements" (trust boundary element confirmed) — https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/ — 访问于 2026-10-14
7. OWASP Cheat Sheet Series, "Threat Modeling" (DFDs, trust boundaries, store models with the system; the page does not name specific tools) — https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html — 访问于 2026-10-14
8. OWASP, "Threat Modeling Process" (DFDs highlight privilege or trust boundaries) — https://owasp.org/www-community/Threat_Modeling_Process — 访问于 2026-10-14
9. The Open Group, ArchiMate 3.2 Reference Cards (flow, triggering) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — 访问于 2026-10-14
10. University of Cape Town, "Chapter 6. Data-Flow Diagrams" (context diagram "sometimes called a level 0" DFD; balancing section; the terms black hole and miracle are common in the wider literature but not found in this text) — https://www.cs.uct.ac.za/mit_notes/software/pdfs/Chp06.pdf — 访问于 2026-10-14
11. OWASP Threat Dragon — https://owasp.org/www-project-threat-dragon/ — 访问于 2026-10-14
12. OWASP pytm, "A Pythonic framework for threat modeling" — https://github.com/OWASP/pytm — 访问于 2026-10-14
13. Microsoft Threat Modeling Tool overview — https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![D2 示例：网店 1 层数据流图，客户、支付服务商和仓库为外部实体，包含带编号的订单加工、一个 Orders 存储和一条信任边界](/samples/D2-data-flow-diagram.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
