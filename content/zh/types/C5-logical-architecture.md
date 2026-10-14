---
code: C5
slug: logical-architecture
family: C
names:
  en: Logical Architecture Diagram
  zh: 逻辑架构图
  aliases:
    en: [logical view, functional view, building block view (level 1), logical application architecture, technology-neutral component diagram]
    zh: [逻辑视图, 功能视图, 逻辑组件图]
question: "系统必须具备哪些与技术无关的构建块？每个构建块负责什么？它们通过哪些具名接口相互依赖，又如何依赖外部能力？"
audiences: [解决方案架构师, 开发人员, 技术负责人, 产品负责人, 自建与采购方案评审人员]
level: logical
phases: [planning, design, review]
scope: "一个系统或一个解决方案，分解为若干职责块（一个层级，一页）。"
formal:
  kind: convention
  ref: "none (no graphical standard); closest definitions: Rozanski & Woods Functional viewpoint, arc42 §5 building block view, TOGAF 9.x Logical Application Component"
neighbours: [A7, C1, C2, C3, C4, C6, C7, C8, G1, I1]
status: draft
translationOf: en/types/C5-logical-architecture.md
sourceRev: 6857dea
reviewed: false
---

# 逻辑架构图（Logical Architecture Diagram）

> 一张与技术无关的图，展示系统需要的构建块、每个构建块的职责以及它们之间的具名接口。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->

逻辑架构图回答：*必须存在哪些构建块？每个构建块负责什么？无论日后由哪些产品或主机来实现，它们彼此之间如何依赖？* 它的关注点是职责分配、从需求到构建块的可追溯性、变更影响、自建/采购/复用决策，以及在团队之间划分工作。系统工程指南提醒，从需求直接跳到物理设计是常见错误，因为干系人会退回到熟悉的方案 [6][7]。用 ISO/IEC/IEEE 42010 的术语，它是结构/功能视点下的一个视图 [5]；用 C4 model 的术语，它与容器层并列，但没有 C4 model 所要求的技术标注 [10]。

“逻辑”至少有五种已发表的含义：Kruchten 4+1 视图中的逻辑视图（类级别的对象模型）[1]；TOGAF 的*逻辑应用组件*（Logical Application Component），“独立于特定实现” [2]；系统工程中随后被分配到物理架构的逻辑架构 [6][8]；IEEE 1016 的“Logical”视点（未对照现行标准原文核实）[15]；以及非正式的“软件而非硬件”。

**本站采用的定义：** 把一个系统或解决方案分解为承担职责的构建块，并给出它们的具名接口和依赖关系，且与技术无关；绘制方式应使不止一种物理或部署设计都能实现它。这最接近 Rozanski & Woods 的功能视点（Functional viewpoint）[3] 和 arc42 第 1 层构建块视图 [4]。4+1 逻辑视图（目录编号 I1）意图相同，但粒度更细，达到类级别。

**相关但不同：** 系统工程中的“功能架构”（functional architecture）是一棵为逻辑构建块提供输入的*功能树*，而不是方框图 [6][8]；SEI 的“模块视图”（module view）展示的是*代码单元* [9]。两者都不属于本类型。

**有意略去：** 产品、框架和版本；主机、网络、副本和可用区；运行时进程和并发；数据模式；场景的调用顺序；类级别的细节。只有当基础设施在功能上有意义时（例如会变换数据的消息总线）才出现 [3]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->

- **受众：** 解决方案架构师、开发人员和技术负责人、产品负责人（需求覆盖）、比较自建/采购方案的评审人员。不面向高管（用 A7 或 C1）或运维人员（用 G1）。
- **典型场景：** (1) 把每种技术或厂商方案映射到同一张逻辑视图上进行比较；(2) 把需求转化为构建块，使每条需求恰好落到一个负责方；(3) 沿构建块边界在团队之间划分工作和归属；(4) 在展示过上下文图之后，回答“系统由什么构成？”；(5) 评审合作方的提案，找出缺口和重叠。
- **不适用场景：** 受众需要主机、扩缩容或可用区（G1/G2）；技术已经确定且读者是开发人员（C3/C4）；需要调用顺序或错误路径（E1）；系统只是一个小进程（一份简短的模块清单就够了 [4]）；方框里只会罗列功能特性（那是能力地图，A1）。
- **与相邻类型的区别：**
  - 当读者想要粗粒度、业务层面且不含接口的构建块时，选 **A7 概念架构**。
  - 当可运行单元及其技术和协议很重要时，选 **C3 容器图**；C4 model 要求每个容器都标注技术 [10]。
  - 当你位于*一个*容器内部且组件带有技术标注时，选 **C4 组件图**；C4 model 的组件不能单独部署 [11]。判断规则：与技术无关且覆盖整个系统 → C5；带技术标注且按容器绘制 → C4。
  - 当每个接口的协议、认证和 SLA 很重要时，选 **C6 集成/接口**。
  - 当重点是代码内部允许依赖的*规则*时，选 **C8 分层架构**；C5 可以按带状分组，但不声明这样的规则。
  - 当问题是各部分运行在哪里时，选 **G1 部署**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->

- **没有标准表示法。** 默认使用普通方框。UML 组件图（推荐用于功能视图 [3]）、ArchiMate 的应用组件和应用接口 [12]，或 Capella 逻辑架构图 [8] 都是可选的正式表示法。ArchiMate 3.2（2022）为现行版本；ArchiMate 4 已于 2026 年 4 月发布公告，将“层”（layer）更名为“域”（domain）[13]。
- **ArchiMate 的注意事项：** 其应用组件（Application Component）“与实现结构对齐” [12]，因此要保持逻辑性，应命名*类型*而非实例，并且不使用 Node 和 System Software。TOGAF 的*逻辑*应用组件才是与实现无关的术语 [2]。
- **必需项：** 标明类型和范围的标题（“Logical view: online shop”）[10]；一个系统边界；构建块，带名词短语名称和一句简短职责；外部能力位于边界之外，使用有区别的样式；每个依赖上都有标签，写明所交换的操作或信息；说明每种形状、颜色和线型的图例 [10][14]。
- **可选项：** 按职责簇分组的框；少量编号的关键交互；在图例中定义的“计划中”标记。
- **配套表格：** 构建块 | 职责 | 提供的接口 | 需要的接口。这就是 Rozanski & Woods 的元素模板和 arc42 的黑盒表 [3][4]。
- **箭头语义：** 每张图只用一种含义。优先采用*依赖/调用*（消费方 → 提供方），数据流留给 D2。标签必须与箭头方向一致；避免只写“使用” [14]。
- **细节程度：** 低于“整个系统”、高于“类”；一页；始终先完成第 1 层，只在风险值得时才深入 [4]。
- **命名：** 构建块用表示职责的名词（“Checkout”“Order Management”），绝不用产品名；接口用动词 + 名词（“reserve stock”）；外部方用角色名（“Payment Provider”），而非品牌名。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### 最佳实践

1. 动笔之前，在标题或图注中写明“逻辑”的定义和范围 [1][6]。
2. 给每个构建块一项职责，并说明为何这样切分系统；隐藏黑盒的内部运作 [4]。
3. 从接口所服务的职责推导接口。凭直觉连接构建块会产生缺失或无用的接口 [7]。
4. 把逻辑模型作为稳定的锚点，在单独的步骤中把它分配到物理单元 [6][7]。
5. 在图旁用表格列出每个构建块的入站和出站接口，并对照 C4 model 检查清单评审（标题、图例、每条线都有标签、方向与标签一致）[3][14]。

### 反模式

1. **技术泄漏：** 边界内出现产品名，会把 C5 变成一张弱化的 C3，也无法用于方案比较 [6]。
2. **假定一对一部署：** 一个逻辑构建块可能对应一个容器、一个容器的一部分，或多个容器 [11]。
3. **类图粒度：** 没有架构意义的类属于更低的层级 [11]。
4. **方框里罗列功能特性，或混用不同种类的元素**（参与者、步骤和构建块并列）：结构被文字淹没。
5. **箭头无标签或含义混杂**，以及在图上写状态备注（“TBD”）而不是放进图例 [14]。

## 范例 {#exemplars}
<!-- skill: omit -->

- [Kruchten, "Architectural Blueprints – The 4+1 View Model"](https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf) — 经典的逻辑视图；展示了本站定义所粗化的类级别解读（许可未核查）。
- [arc42 §5 Building block view](https://docs.arc42.org/section-5/) 和 [arc42 examples](https://examples.arc42.org/) — 第 1 层白盒加黑盒职责表；说明何时停止深入（arc42 模板为 CC BY-SA 4.0；示例的许可未核查）。
- [Rozanski & Woods architecture description template](https://www.viewpoints-and-perspectives.info/vpandp/wp-content/themes/secondedition/doc/registered/RozanskiAndWoods-Architecture-Description-Template.pdf) — 现成的元素模板：职责、入站和出站接口（许可未核查）。
- [SEBoK, Logical Architecture Model Development](https://sebokwiki.org/wiki/Logical_Architecture_Model_Development) — 系统工程中的含义，以及从逻辑到物理的分配步骤（许可未核查）。
- [Capella / Arcadia method](https://mbse-capella.org/arcadia.html) — 一套完整的方法，把逻辑架构作为独立的工程层级（开源工具；许可未核查）。
- [C4 model, Component](https://c4model.com/abstractions/component) — 本身不是 C5，但对什么是组件、什么不是组件给出了最清楚的公开说明；可作对照。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->

1. 确定定义和范围：针对一个系统或解决方案，“逻辑 = 与技术无关的职责块和接口”。
2. 列出需求/能力；把每一项分配给恰好一个构建块；按内聚性分组；用名词命名构建块。
3. 从职责推导每个依赖，并用操作或信息为其加标签；去掉背后没有需求支撑的依赖。
4. 把外部能力（身份、支付服务商、仓储）放在边界之外。
5. 布局：按依赖自上而下（面向消费方的构建块在上，提供方在下），或按请求流自左向右；2–5 个框，每个约 3–7 个构建块（经验法则）。
6. 文字：构建块 = 名称（≤3 个词）+ 最多一行职责；接口标签 ≤3 个词；细节放进配套表格。
7. 颜色只编码角色（内部 / 外部 / 计划中），绝不编码技术；加上图例。
8. 箭头：一种含义（依赖），正交走线，终止于方框或分组边框。
9. 如果之后确定了技术，就重画为 C3/C4，而不是在 C5 上加标签。

**自检清单**
- [ ] 标题写明类型和范围；图例解释了每种形状、颜色和线条。
- [ ] 边界内没有产品、框架或主机名称。
- [ ] 每个构建块只有一项职责；没有需求无人负责或被重复负责。
- [ ] 每条线都有标签，且标签与箭头方向一致。
- [ ] 同级元素属于同一种类；没有混入参与者、步骤或功能清单。
- [ ] 外部能力位于边界之外，且样式明显不同。
- [ ] 两种不同的物理设计都能实现这张图。
- [ ] 图上没有状态备注；每个徽标或编号都有解释。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->

- 有用的：顶层模块/包结构；接口和端口定义、`.proto` 和 OpenAPI 文件；import/依赖关系图；README 和 ADR（预期职责）；路由或菜单定义（功能 → 构建块）；CODEOWNERS；目录描述文件，例如 Backstage 的 `catalog-info.yaml` [16]。
- 单独使用会误导的：`docker-compose.yml`、Kubernetes 清单和 IaC 描述的是容器和部署（C3/G1）；只用它们来检查每个可运行单元是否都对应到某个构建块。
- 要问人的：预期职责、切分的理由、计划中的构建块以及可接受的外部能力。把从代码推导出的构建块视为待确认的草稿。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->

1. 这张图要帮助做出什么决定（方案比较、工作划分、需求覆盖、新成员熟悉），谁来读？（默认：架构师和开发人员；需求覆盖。）
2. 一个系统还是多个？哪部分展开细节，哪部分折叠成一个方框？（默认：整个系统、一个层级；外部方折叠。）
3. 你指的是哪种“逻辑”：职责块、类级别模型，还是功能树？（默认：职责块；另外两种分别转向类图/ER 图或功能分解。）
4. 技术选型是否已经确定？（默认：否；如果是，建议改画 C3/C4，并在表格中保留映射关系。）
5. 必须出现哪些外部能力，以及哪 3–6 个关键交互？（默认：身份、支付服务商、主要的购买请求。）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->

模型模板：`assets/templates/C5.json` · 布局模板：`layered` · 类型为 `frame` 的分组成为一个 `boundary` 内由职责块组成的水平带；外部方位于其外部，类型为 `dependency` 的 `edges` 带操作标签。

## 来源 {#sources}
<!-- skill: omit -->

1. Kruchten, "Architectural Blueprints – The 4+1 View Model of Software Architecture" (1995) — https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf — 访问于 2026-10-14
2. The TOGAF Standard 9.1, Glossary (Logical/Physical Application Component) — https://pubs.opengroup.org/architecture/togaf91-doc/arch/apdxa.html — 访问于 2026-10-14（仅检索摘录；未核实 TOGAF 10 原文）
3. Rozanski & Woods, Architecture Description Template (Functional View) — https://www.viewpoints-and-perspectives.info/vpandp/wp-content/themes/secondedition/doc/registered/RozanskiAndWoods-Architecture-Description-Template.pdf — 访问于 2026-10-14
4. arc42 documentation, "5 – Building block view" — https://docs.arc42.org/section-5/ — 访问于 2026-10-14
5. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/42010/cm/ — 访问于 2026-10-14
6. SEBoK, "Logical Architecture Model Development" — https://sebokwiki.org/wiki/Logical_Architecture_Model_Development — 访问于 2026-10-14
7. Samares Engineering, "Consistency between functional and logical architectures" — https://www.samares-engineering.com/en/2020/07/21/part-4-consistency-between-functional-and-logical-architectures — 访问于 2026-10-14
8. Capella MBSE Tool, "Arcadia" — https://mbse-capella.org/arcadia.html — 访问于 2026-10-14
9. SEI, Views and Beyond Collection — https://www.sei.cmu.edu/library/views-and-beyond-collection — 访问于 2026-10-14
10. C4 model, Notation — https://c4model.com/diagrams/notation — 访问于 2026-10-14
11. C4 model, Component — https://c4model.com/abstractions/component — 访问于 2026-10-14
12. ArchiMate 3.2 Specification, Application Layer — https://pubs.opengroup.org/architecture/archimate32-doc/ch-Application-Layer.html — 访问于 2026-10-14（仅检索摘录）
13. The Open Group, "The Open Group Announces ArchiMate 4 Specification" — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — 访问于 2026-10-14（仅检索摘录）
14. C4 model, Review checklist — https://c4model.com/diagrams/checklist — 访问于 2026-10-14
15. Wikipedia, "Software design description" (IEEE 1016-2009 viewpoints) — https://en.wikipedia.org/wiki/Software_design_description — 访问于 2026-10-14（二手资料）
16. Backstage, Descriptor format of catalog entities — https://backstage.io/docs/features/software-catalog/descriptor-format/ — 访问于 2026-10-14

## 示例图 {#sample}
<!-- skill: path only -->

![C5 示例：一家网店的逻辑视图，包括商品目录、购物车、结账、订单管理、履约和客户支持等构建块，支付服务商、仓储和身份位于边界之外](/samples/C5-logical-architecture.svg)
*示例图待生成（由渲染器根据 `examples/` 生成）。*
