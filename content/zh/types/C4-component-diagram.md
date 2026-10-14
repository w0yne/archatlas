---
code: C4
slug: component-diagram
family: C
names:
  en: Component Diagram
  zh: 组件图
  aliases:
    en: [C4 model Level 3, White-box View of a Container, Building Block View Level 2 (arc42), Module Diagram, Internal Structure Diagram]
    zh: [C4 模型第 3 层, 容器内部结构图, 模块图, 内部结构图]
question: "在这一个容器内部，它由哪些组件构成？每个组件负责什么、用什么构建？它们彼此之间以及与其他容器之间如何依赖？"
audiences: [软件架构师, 开发人员]
level: logical
phases: [design, build, review]
scope: "恰好一个容器：容器边界内的各个组件，以及与它们直接相连的其他容器、人员和系统。"
formal:
  kind: method
  ref: "C4 model (Simon Brown), Level 3 Component diagram; notation-independent, no versioned standard. Related: UML 2.5.1 component diagram (OMG), a different meaning of 'component'"
neighbours: [C3, C5, C8, E1, D1, G1]
status: draft
translationOf: en/types/C4-component-diagram.md
sourceRev: 6857dea
reviewed: false
---

# 组件图（Component Diagram）

> 深入一个容器内部：它的主要构建块、各自的职责和技术，以及它们之间的依赖。

**关于编号的说明：** 在本目录中，编号 `C4` 指组件图。它是 **C4 model** 的第 3 层；编号与该方法只是同名而已。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
它回答：*在这一个容器内部，主要组件有哪些？每个组件负责什么、用什么构建？谁调用谁，包括它们所依赖的其他容器？* 它是 C4 model 的第 3 层。C4 model 是 Simon Brown 提出的与表示法无关的方法（没有带版本号的标准）[1][4][5]；在 arc42 中，它对应构建块视图（building block view）的第 2 层，即某个第 1 层构建块的白盒 [3]。它是面向开发人员的内部结构视图。它略去其他容器的内部、类（C4 model 第 4 层，即代码图）、部署以及随时间展开的时序 [1][13]。
**本站采用的定义：“组件”有三种含义。** 要说明你画的是哪一种。
- **C4 model 组件（本类型）：** 在一个容器内运行、位于明确定义的接口之后的一组相关功能。它不能单独部署；包、命名空间、文件夹或 JAR 通常*不是*组件 [6]。
- **UML 组件（UML 2.5.1）：** 一个模块化、可替换的部分，具有提供接口和需求接口，可选地带有端口。它可以是逻辑的或物理的，并且可以单独部署，因此 UML 组件既可能对应 C4 model 的*容器*，也可能对应组件 [7][8][9]。此处根据二手参考资料概括，未对照现行规范原文核实。
- **云厂商的用法：** 一种用具体产品和集成点替换通用构建块的视图，即“可视化的物料清单” [10]。它更接近带技术标注的 C3 视图或 G2 图。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 软件架构师和开发人员 [1]；不面向高管或客户。
- **是否推荐？** C4 model 的回答是**不推荐**：只在能增加价值时才画，并考虑为长期维护的文档自动生成它 [1]，因为在活跃开发的代码中组件图变化频繁 [14]。一份关于 2026 年某场演讲的二手摘要提到，大多数团队只需要第 1 层和第 2 层 [20]；该摘要未对照演讲本身核实。
- **适用场景：** 在重大变更前对复杂服务进行设计评审；熟悉一个大型服务（“这个改动该放在哪里？”）；在模块化单体或六边形设计中商定模块边界，并以代码检查加以守护；评审组件对存储、队列和其他服务的依赖；在拆分服务前寻找接缝。
- **不适用场景：** 很薄或 CRUD 式的容器（C3 已足够）；为了“完整”而每个容器画一张；跨容器的流程（E1、E4）；没有稳定的代码结构可供映射；类级别的细节（IDE 生成的类图）[13]；库的设计 [2]。
- **与相邻类型的区别：**
  - 针对整个系统时选 **C3**；只有在 C3 达成一致、且某个容器确实复杂之后才画 C4 [23]。
  - 需要与技术无关、覆盖整个系统的职责划分时，选 **C5**；C4 带技术标注，且按容器绘制。
  - 重点是分层规则时，选 **C8**；组件图可以*展示*分层，但命名的是真实的组件。
  - 需要展示一个场景中经过各组件的路径时，选 **E1**（C4 model 的“动态图”是一种带编号交互的形式 [12]）。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **C4 model 不强制任何表示法**：通常使用普通方框和带标签的箭头；C4 model 的通用表示法规则和评审检查清单适用于每一层 [11][15]。
- **必需项：** 标题“Component diagram for `<Container>` in `<System>`”；**组件**，每个都有名称、类型（“Component”）、技术（例如“web controller”“TypeScript module”）和简短的职责；围绕它们的**容器边界**；**关系**；**图例** [1][11]。
- **辅助元素：** 同一系统中位于边界之外的其他容器（数据存储、队列、服务），以及仅在与某个组件直接相连时才出现的人员和外部系统 [1]。
- **关系：** 一个方向，动词标签与之一致（“调用”“读取”“发布到”）；在连线离开容器处加上协议；若同步和异步同时出现，在图例中区分；不用双向箭头 [10][11]。
- **可选的 UML 接口表示法：** 当读者熟悉 UML 或接口本身是重点（例如六边形架构的端口）时，可以使用提供接口的圆球、需求接口的插座和端口 [8]。它们不属于 C4 model，并且带有 UML 中“组件”的含义。
- **粒度 [16]：** 先确定架构风格（按层、按功能、六边形）；忽略逻辑很少的数据类型、校验器、配置和启动代码；为每个类别定义一条识别规则（注解、名称后缀、包）。通常 5–15 个组件；更多时按功能拆分。
- **工具：** Structurizr DSL [17] 和 C4-PlantUML [18]；同一个模型可同时生成 C3 和 C4 视图 [22]。
- **命名：** 组件按代码中的名称命名（包、模块或类名），以便读者找到它们 [3][16]。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. 只为复杂、易变或陌生的容器绘制 [1][3]。
2. 让组件可被找到：与代码使用相同的名称和模块边界，最好附上指向代码位置的链接 [16]。
3. 当图需要比一次发布活得更久时，自动生成它：基于注解、命名模式或模块布局的规则 [14][16][24]。
4. 展示主要流程以及对其他容器的依赖；这些正是评审者需要的。
5. 把分解的理由写在文字或决策记录中，并在图上注明日期和源代码版本，让过时一目了然 [3][19]。

### 反模式
1. 组件实际上是类（几十个方框），或实际上是没有职责的文件夹 [6]。
2. 在一张图中混入多个容器的内部 [1]。
3. 编造“子组件”层级，而不是另画一张图 [19][21]。
4. 把共享库画成独立的容器或组件；它们是在组件内部复用的代码 [19]。
5. 把技术物料清单当作组件图展示，却不说明采用的是哪种含义 [10]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [C4 model: Component diagram](https://c4model.com/diagrams/component) — 范围、受众以及“对大多数团队不推荐”的回答，附带图例的参考示例（CC BY 4.0）。
- [C4 model: Component abstraction](https://c4model.com/abstractions/component) — 什么是组件、什么不是组件（CC BY 4.0）。
- [Structurizr: component finder introduction](https://docs.structurizr.com/java/component/introduction) — 用明确的规则从真实代码中推导组件，以及应忽略哪些内容。
- [arc42 section 5: Building block view](https://docs.arc42.org/section-5/) — C4 model 之外的对应做法，带黑盒模板以及关于细化哪些构建块的建议（CC BY-SA 4.0）。
- [uml-diagrams.org: component diagram reference](https://www.uml-diagrams.org/component-diagrams-reference.html) — 提供接口和需求接口、端口和装配连接器，适用于需要 UML 表示法时。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确认是哪一个容器以及绘制原因（评审、熟悉、重构）；如果没有 C3，先确认 C3。
2. 识别该容器的风格（分层、功能模块、六边形、模块化单体）；代码不明确时询问。
3. 列出候选项：入口点（controller、handler、consumer、scheduler）、应用逻辑、出站适配器（repository、client）。去掉 DTO、工具类、配置和启动代码。
4. 归并为 5–15 个使用代码名称的组件，例如网店的 Shop API：Catalogue Handler、Cart Handler、Checkout Handler、Pricing、Checkout Service、Order Repository、Payment Client、Warehouse Client、Event Publisher。
5. 布局：画出容器边界；入口点在上方或左侧，逻辑在中间，适配器在下方或右侧；其他容器（Order Database、“order placed”主题）和外部系统（Payment Provider、Warehouse System）放在边界之外、靠近连接它们的适配器。分层代码用自上而下，请求流用自左向右。
6. 只画主要调用路径，不画每一个 import；用动词标签；在连线离开容器处标注协议。
7. 文字预算：名称 1–3 个词，技术一行，描述约 10 个词以内，箭头标签约 5 个词以内；不列类清单。
8. 颜色：组件、其他容器、外部系统三种样式，再加形状提示；配图例。
9. 加上标题、图例、日期和源代码版本；提供可编辑或可重新生成的源文件。

**自检清单**
- [ ] 范围内恰好一个容器；有边界、标题和图例。
- [ ] 每个组件都是位于接口之后的内聚部分，而不是类、文件夹或库。
- [ ] 组件名称能在仓库中找到。
- [ ] 每个箭头只有一个方向和与之一致的标签；离开容器的连线标有协议。
- [ ] 展示了对其他容器、存储和队列的依赖；主要流程一目了然。
- [ ] 没有部署细节、没有类、没有其他容器的内部。
- [ ] 5–15 个方框；否则按功能拆分。
- [ ] 如果出现了 UML 表示法，图上说明了采用哪种“组件”含义。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 源代码树：顶层包、模块、命名空间；工作区或模块声明（在模块化单体中是强信号）[24]。
- 注解和命名后缀（`@Controller`、`@Repository`、路由器、`*Handler`、`*Client`）：组件查找器使用的规则 [16]。
- import 或依赖关系图以及架构测试能显示真实的连线；把它们当作需要筛选的候选项。
- 依赖注入的装配和消息处理器的注册能显示组件和异步入口点。
- 出站客户端、repository 和生产者能显示对其他容器的依赖。
- 代码中没有的：预期的职责、哪些接缝在架构上重要、计划中的组件。要去问人。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 应该打开哪个容器？为什么？（最复杂或改动最多的那个，用于设计评审）
2. 它的结构风格是什么？组件应来自代码还是来自目标设计？（从代码推导）
3. 要多深：约 5 个粗粒度组件，还是多达约 15 个？（5–9 个）
4. 必须出现哪些相邻容器和外部系统？（组件直接调用的那些）
5. 是否需要 UML 接口表示法？你需要可重新生成的源文件吗？（不用 UML；图即代码的源文件）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/C4.json` · 布局模板：`nested` · 容器用一个 `boundary` 分组，内含 `component` 节点；其他 `container`、`store`、`queue` 和 `external` 节点在其外部；叶子节点之间的连线带标签。

## 来源 {#sources}
<!-- skill: omit -->
1. C4 model — Component diagram — https://c4model.com/diagrams/component — 访问于 2026-10-14
2. C4 model — FAQ — https://c4model.com/faq — 访问于 2026-10-14
3. arc42 — Section 5, Building block view — https://docs.arc42.org/section-5/ — 访问于 2026-10-14
4. C4 model — History — https://c4model.com/history — 访问于 2026-10-14
5. C4 model — Home — https://c4model.com/ — 访问于 2026-10-14
6. C4 model — Component (abstraction) — https://c4model.com/abstractions/component — 访问于 2026-10-14
7. uml-diagrams.org — UML component — https://www.uml-diagrams.org/component.html — 访问于 2026-10-14
8. uml-diagrams.org — UML component diagram reference — https://www.uml-diagrams.org/component-diagrams-reference.html — 访问于 2026-10-14
9. OMG — Unified Modeling Language 2.5.1 — https://www.omg.org/spec/UML/2.5.1/About-UML — 访问于 2026-10-14
10. Microsoft Learn — Create architecture design diagrams (Azure Well-Architected) — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — 访问于 2026-10-14
11. C4 model — Notation — https://c4model.com/diagrams/notation — 访问于 2026-10-14
12. C4 model — Dynamic diagram — https://c4model.com/diagrams/dynamic — 访问于 2026-10-14
13. C4 model — Code diagram — https://c4model.com/diagrams/code — 访问于 2026-10-14
14. C4 model — Diagrams FAQ — https://c4model.com/diagrams/faq — 访问于 2026-10-14
15. C4 model — Review checklist — https://c4model.com/diagrams/checklist — 访问于 2026-10-14
16. Structurizr — Component finder introduction — https://docs.structurizr.com/java/component/introduction — 访问于 2026-10-14
17. Structurizr — DSL language reference — https://docs.structurizr.com/dsl/language — 访问于 2026-10-14
18. C4-PlantUML — https://github.com/plantuml-stdlib/C4-PlantUML — 访问于 2026-10-14
19. Working Software — Misuses and mistakes of the C4 model — https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model — 访问于 2026-10-14
20. daily.dev — Summary of "The C4 Model" (S. Brown, S. Kaiser, GOTO 2026) — https://daily.dev/posts/the-c4-model-visualizing-software-architecture-simon-brown-susanne-kaiser-goto-2026-xuw6udw2z — 访问于 2026-10-14
21. C4 model — Abstractions FAQ — https://c4model.com/abstractions/faq — 访问于 2026-10-14
22. godatadriven/c4-model-example — https://github.com/godatadriven/c4-model-example — 访问于 2026-10-14
23. C4 model — Container diagram — https://c4model.com/diagrams/container — 访问于 2026-10-14
24. S. Brown — Reverse-engineering architecture diagrams (talk) — https://www.youtube.com/watch?v=2Cz9ZDIlBeM — 访问于 2026-10-14

## 示例图 {#sample}
<!-- skill: path only -->
![C4 示例：网店 Shop API 的组件图，包括各处理器、结账逻辑、仓储库以及连接支付服务商和仓储系统的客户端](/samples/C4-component-diagram.svg)
*示例图待生成（由渲染器根据 `examples/` 生成）。*
