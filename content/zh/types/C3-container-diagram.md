---
code: C3
slug: container-diagram
family: C
names:
  en: Container Diagram
  zh: 容器图
  aliases:
    en: [C4 model Level 2, High-level System Diagram, Building Block View Level 1 (arc42), High-level Technical Architecture Diagram (loose)]
    zh: [C4 模型第 2 层, 运行单元图, 技术架构图（口语，含义宽泛）, 系统架构图（口语，含义宽泛）]
question: "这个系统由哪些独立运行的应用和数据存储构成？各自使用什么技术？它们如何通信？"
audiences: [架构师, 开发人员, 运维与支持人员, 安全评审人员, 技术干系人]
level: logical
phases: [design, build, review, operate]
scope: "一个软件系统：边界内的各个容器，以及与它们直接相连的人员和外部系统。"
formal:
  kind: method
  ref: "C4 model (Simon Brown), Level 2 Container diagram; notation-independent, no versioned standard"
neighbours: [C2, C4, C1, C5, C6, G1, E1, D2, F2, I2]
status: draft
translationOf: en/types/C3-container-diagram.md
sourceRev: 6857dea
reviewed: false
---

# 容器图（Container Diagram）

> 深入一个系统内部：必须运行的应用和数据存储、它们的技术，以及它们如何通信。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
它回答：*这个系统由哪些独立运行的应用和数据存储构成？各自使用什么技术？它们如何通信？* 它是 C4 model 的第 2 层。C4 model 是 Simon Brown 提出的与表示法无关的方法（没有带版本号的标准）[1][6]；本图展示架构的整体形态、职责如何划分以及关键技术选型 [2]。用 arc42 的术语，它是构建块视图（building block view）的第 1 层 [3][4]。它略去部署拓扑（副本、可用区、负载均衡器属于 G1）、每个容器的内部（C4）、类、随时间展开的时序以及数据模型 [2]。
**本站采用的定义：容器不是 Docker 容器。** C4 model 中的容器（container）是系统运行所必需的*应用或数据存储*：服务端 Web 应用、浏览器中的单页应用、移动或桌面应用、批处理进程、无服务器函数、数据库或模式（schema）、对象存储桶、文件共享，甚至一个脚本 [8]。它可能对应、也可能不对应一个 Docker/OCI 容器。JAR、DLL、包、模块和共享库*不是*容器；它们组织的是某个容器内部的代码 [8][15]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 团队内外的技术读者；C4 model 建议所有软件团队都绘制此图 [2]。
- **适用场景：** 新工程师看到的第一张技术图；设计或技术选型评审；在安全、运维或威胁建模工作（F2）之前弄清“运行着什么、谁与谁通信”；变更或故障的影响分析。
- **不适用场景：** 读者看不懂技术名称（C2、A7）；问题是部署位置、容量或环境（G1/G2/G3）；对象是库或 SDK（C4 model 面向软件系统）[4]；技术尚未确定（先画 C5）；为了充实一个只有两个方框的系统而想去编造容器。
- **与相邻类型的区别：**
  - 只关心范围和依赖，或读者是非技术人员时，选 **C2**；应先画它 [10]。涉及许多系统时选 **C1**（C4 model 的系统全景图）[13]。
  - 当某个容器很复杂、开发人员需要了解其组成部分时，选 **C4** [11]；类级别的代码图是可选的，最好由 IDE 生成 [12]。
  - 当问题是*部署在哪里、有多少个、在哪个环境*时，选 **G1**；绝不要把容器图当作部署图 [2][9]。
  - 需要与技术无关的职责划分时，选 **C5**；C3 为每个容器标注技术。
  - 需要完整描述系统*之间*接口的各项属性时，选 **C6**；C3 只停留在一个系统*内部*及其直接邻居。
  - 需要展示单个场景随时间的展开时，选 **E1**（C4 model 的“动态图”是它的一种带编号交互的形式 [14]）。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **C4 model 不强制任何表示法**：形状和颜色可以自由选择，但必须有图例，且图必须能独立成立 [7]。
- **必需项：** **容器**，每个都有名称、明确的类型（“Container”）、技术和一句话职责 [7]；**数据存储**，同样具备这四个字段（常用圆柱体，在图例中说明）；可见的**系统边界**，并标注系统名称；**关系**；**标题**“Container diagram for <System>”；**图例**（形状、颜色、边框、线条、箭头、缩写）[2][24]。
- **辅助元素：** C2 中与容器直接相连的人员和外部系统；绝不画外部系统的内部 [2][15]。
- **关系：** 每条线一个方向；意图标签与方向一致（“读写”“向……发布订单事件”）；容器之间的连线要加上协议或技术（JSON/HTTPS、SQL、AMQP）[7][8]。依赖方向或数据流方向都可以，只要保持一致 [16]；不用双向箭头 [5]。
- **建模规则 [8][17][18]：** 浏览器中的单页应用及其后端是两个容器；你拥有的托管云数据库和存储桶是容器，而不是外部系统；同一团队的微服务是容器（API 加其存储，归为一组），而由不同团队拥有的服务则成为单独的软件系统；把每个队列或主题建模为独立的容器，而不是一个“消息总线”方框（这是作者的建议），或者只在箭头标签上标出。
- **方框文字：** 很多渲染器依次输出名称、`[Container: technology]` 和描述。这是渲染器的惯例，尚未在 C4 model 原文中核实为规则。
- **工具：** Structurizr DSL [20] 和 C4-PlantUML [21] 支持完整的元素集；Mermaid 的 C4 model 语法标为实验性 [22]。
- **规模：** 通常 5–12 个方框；超过十来个时，按领域拆分，或只画一个服务及其直接邻居 [19]。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. 先画 C2，再画 C3，并沿用相同的系统名称、人员和外部系统 [2][19]。
2. 始终标出技术和协议；技术选型是这一层的主要价值 [7]。
3. 为每个容器写一句职责说明，按角色命名，并与代码和文档中的名称一致 [7]。
4. 保持与部署无关；副本、可用区和负载均衡器放到 G1 [2]。
5. 从同一个模型生成各视图（图即代码），使 C2、C3 和 C4 保持一致、不发生漂移 [23][26]。

### 反模式
1. 把“容器”当成 Docker，或把共享库、模块或 JAR 画成容器 [8][15]。
2. 用一个“消息总线”方框掩盖谁向哪个主题发布、谁从哪个主题消费 [18]。
3. 在容器图上画部署细节（集群、子网、实例数量）[2]。
4. 方框只有名称（没有类型、技术或职责）、标签写“使用”、箭头无标签或双向、没有图例 [15][24]。
5. 编造额外的层级（“子系统”），或为整个分布式环境画一张巨大的图 [15][19][25]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [C4 model: Container diagram](https://c4model.com/diagrams/container) — 权威定义、范围规则以及带图例的参考示例（CC BY 4.0）。
- [C4 model: Container abstraction](https://c4model.com/abstractions/container) — “不是 Docker”的定义，并列出哪些算作容器（CC BY 4.0）。
- [LikeC4: Big Bank showcase](https://likec4.dev/showcases/bigbank) — 每个容器都有类型、技术和描述，每个箭头都有用途和协议（许可：请查看网站）。
- [Simon Brown: Diagramming distributed architectures with the C4 model](https://dev.to/simonbrown/diagramming-distributed-architectures-with-the-c4-model-51cm) — 如何围绕一个服务及其邻居截取视图。
- [godatadriven/c4-model-example](https://github.com/godatadriven/c4-model-example) — 一个小型 Structurizr DSL 工作区，从同一模型生成上下文、容器和组件视图（许可：请查看仓库）。

## 绘图步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确认系统边界和 C2 中的邻居；如果没有 C2，先把它们列出来。
2. 盘点运行单元和存储（例如网店：Web Shop 单页应用、Mobile App、Shop API、Order Worker、Order Database、Search Index、Product Image Bucket，以及一个“order placed”主题）。
3. 与用户一起确定：同一团队的服务 = 容器；由不同团队拥有的服务 = 单独的系统。
4. 每个容器写四个字段：名称、类型、技术、一句话职责。
5. 每条关系写成动词短语 + 协议（“Sends payment requests to — JSON/HTTPS”）；全图使用同一种方向约定。
6. 布局自上而下或自左向右：先是人员和客户端应用，中间是应用容器，最后是存储和主题；外部系统（Payment Provider、Warehouse System、Customer Support System、Email Service）放在边界之外、与其连接方向相对应的一侧。
7. 文字预算：名称 2–4 个词，技术一行，描述约 12 个词以内，箭头标签约 6 个词以内再加协议。
8. 颜色：3–4 种语义色（容器、存储、外部系统、人员），再加形状提示；在图例中说明。
9. 加上标题、图例和日期；不写状态备注或 TODO；方框超过约 12 个 → 拆成多个视图。

**自检清单**
- [ ] 标题、类型、范围和图例可见；系统边界明确。
- [ ] 每个方框都是必须运行的应用或数据存储；没有库、包、类、服务器或子网。
- [ ] 每个容器都标出名称、类型、技术和职责。
- [ ] 每个箭头只有一个方向，意图标签与之一致，容器之间标有协议。
- [ ] 没有部署细节，也没有外部系统的内部。
- [ ] 数据存储和队列遵循同一条明示的规则。
- [ ] 名称与代码和 C2 图一致；解释了缩写。
- [ ] 颜色不是唯一的区分手段；方框约十来个或更少。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- Compose 文件、Helm chart、Kubernetes Deployment/StatefulSet、Procfile：每个服务对应一个*候选*容器。一个 compose 服务不一定就是一个容器（sidecar、初始化作业）；仅供本地使用的辅助程序不属于系统。
- Dockerfile 和构建文件（`package.json`、`pom.xml`、`go.mod`、`pyproject.toml`）：各容器的技术。
- 基础设施即代码：托管数据库、存储桶、队列和函数（都是容器）[8]。
- API 规范（OpenAPI、AsyncAPI、protobuf）和连接配置（`DATABASE_URL`、消息代理和服务 URL）：谁调用谁、用什么协议。
- 服务目录和追踪数据可用于自动生成视图 [26]。
- 代码中没有的：职责的措辞、哪些依赖是外部的、团队归属（决定微服务如何建模时需要）以及各项选择背后的理由。要去问人。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 哪个系统在范围内？我们是否已有它的上下文图？（先画或确认 C2）
2. 谁会读这张图？他们看完后要做什么决定？（开发和运维人员评审设计）
3. 这是一个团队的产品，还是多个团队的服务？（一个团队：服务即容器）
4. 队列和主题是画成独立方框还是只写在箭头标签上？技术是否已最终确定？（独立方框；未定的选择在图例中标为“proposed”）
5. 我可以读取仓库和部署文件吗？你需要可编辑的源文件吗？（可以；图即代码的源文件加 SVG）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/C3.json` · 布局模板：`nested` · 系统用一个 `boundary` 分组，内含 `container`、`store` 和 `queue` 节点；`person` 和 `external` 节点在其外部；连线带标签和协议。

## 参考来源 {#sources}
<!-- skill: omit -->
1. C4 model — Home — https://c4model.com/ — 访问于 2026-10-14
2. C4 model — Container diagram — https://c4model.com/diagrams/container — 访问于 2026-10-14
3. arc42 — Section 5, Building block view — https://docs.arc42.org/section-5/ — 访问于 2026-10-14
4. C4 model — FAQ — https://c4model.com/faq — 访问于 2026-10-14
5. Microsoft Learn — Create architecture design diagrams (Azure Well-Architected) — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — 访问于 2026-10-14
6. C4 model — History — https://c4model.com/history — 访问于 2026-10-14
7. C4 model — Notation — https://c4model.com/diagrams/notation — 访问于 2026-10-14
8. C4 model — Container (abstraction) — https://c4model.com/abstractions/container — 访问于 2026-10-14
9. C4 model — Deployment diagram — https://c4model.com/diagrams/deployment — 访问于 2026-10-14
10. C4 model — System context diagram — https://c4model.com/diagrams/system-context — 访问于 2026-10-14
11. C4 model — Component diagram — https://c4model.com/diagrams/component — 访问于 2026-10-14
12. C4 model — Code diagram — https://c4model.com/diagrams/code — 访问于 2026-10-14
13. C4 model — System landscape diagram — https://c4model.com/diagrams/system-landscape — 访问于 2026-10-14
14. C4 model — Dynamic diagram — https://c4model.com/diagrams/dynamic — 访问于 2026-10-14
15. Working Software — Misuses and mistakes of the C4 model — https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model — 访问于 2026-10-14
16. C4 model — Diagrams FAQ — https://c4model.com/diagrams/faq — 访问于 2026-10-14
17. C4 model — Microservices — https://c4model.com/abstractions/microservices — 访问于 2026-10-14
18. C4 model — Queues and topics — https://c4model.com/abstractions/queues-and-topics — 访问于 2026-10-14
19. S. Brown — Diagramming distributed architectures with the C4 model — https://dev.to/simonbrown/diagramming-distributed-architectures-with-the-c4-model-51cm — 访问于 2026-10-14
20. Structurizr — DSL language reference — https://docs.structurizr.com/dsl/language — 访问于 2026-10-14
21. C4-PlantUML — https://github.com/plantuml-stdlib/C4-PlantUML — 访问于 2026-10-14
22. Mermaid — C4 diagrams — https://mermaid.js.org/syntax/c4.html — 访问于 2026-10-14
23. C4 model — Tooling — https://c4model.com/tooling — 访问于 2026-10-14
24. C4 model — Review checklist — https://c4model.com/diagrams/checklist — 访问于 2026-10-14
25. C4 model — Abstractions FAQ — https://c4model.com/abstractions/faq — 访问于 2026-10-14
26. Structurizr — Automation and other tooling — https://docs.structurizr.com/getting-started/other — 访问于 2026-10-14

## 示例图 {#sample}
<!-- skill: path only -->
![C3 示例：一家网店的容器图，包括 Web 和移动客户端、商店 API、订单处理程序、订单数据库、搜索索引和“订单已下达”主题](/samples/C3-container-diagram.svg)
*示例图待生成（由渲染器根据 `examples/` 生成）。*
