---
code: C6
slug: integration-interface
family: C
names:
  en: Integration and interface diagram
  zh: 集成与接口图
  aliases:
    en: [integration diagram, interface map, integration architecture, interface catalog, API landscape, integration landscape, application interaction matrix, event topology]
    zh: [集成架构图, 接口关系图, 系统集成图, 接口清单, 应用通信图, 应用交互矩阵, 事件拓扑图, API 全景图]
question: 系统之间有哪些接口？每个接口由谁发起、交换什么、采用哪种集成方式，又受哪份契约、哪些安全措施、哪个服务级别和哪些负责方约束？
audiences: [architects, developers, operations]
levels: [logical, physical]
phases: [design, build]
scope: 一组系统之间的接口（或对单个枢纽、单个合作方的特写），以关系图加一张必备的接口表来呈现。
formal: {kind: convention, ref: none for the diagram; vocabulary from Enterprise Integration Patterns (2003) and TOGAF 9.x Phase C artefacts; contracts in OpenAPI 3.2.x / AsyncAPI 3.1.0}
neighbours: [C1, C2, C3, C5, C7, E1, F2]
status: draft
translationOf: en/types/C6-integration-interface.md
sourceRev: 674f366
reviewed: false
---

# 集成 / 接口图（Integration / Interface Diagram）

> 一张系统间接口的关系图，配一张表，逐个记录每个接口的集成方式、契约、安全、服务级别和负责方。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->

集成关系图（integration diagram）回答的是：*哪些接口连接这些系统，谁调用或发布，交换什么，采用哪种方式，每一端由谁负责？* 它真正的目的是让**耦合可见、可协商**：这是两个团队（或企业与合作方）在写代码之前达成一致的成果物，而它的表格就是契约的骨架。按 ISO/IEC/IEEE 42010 的说法，它的关注点（concern）是互操作性、耦合、交换的安全性、归属和变更影响 [10]。在 SEI Views and Beyond 中，它是一种组件与连接件视图（component-and-connector view），连接件是一等元素 [11]。

没有任何单一标准定义这种图。它汲取了四种传统：
- **Enterprise Integration Patterns**（Hohpe & Woolf，2003）：65 个模式和四种**集成方式**（integration style）：File Transfer、Shared Database、Remote Procedure Invocation、Messaging [1][2]。书中定义了模式图标，但也明确指出并不存在广泛使用的、完整的表示法 [3]。
- **TOGAF 9.x Phase C** 制品：Interface Catalog、Application Communication diagram 和 Application Interaction matrix [4]。第 10 版的原文未经核实。
- **系统工程：** 接口控制文档（Interface Control Document，ICD）记录每个接口的格式、频率和时序 [5]。
- **机器可读契约：** HTTP API 用 OpenAPI（当前版本 3.2.1）[6]，事件驱动 API 用 AsyncAPI（当前版本 3.1.0）[7]，二者均于 2026-10-14 核对。

**本站采用的定义：** C6 关注系统*之间*（包括合作方），C3 关注*单个*系统内部。TOGAF 让 Application Communication diagram 保持在逻辑层，把协议放到技术视图 [4]。因此本页提供一个**逻辑变体**（无协议列）和一个**技术变体**（含协议列）。

**同一类型下的三种变体：** (a) **接口关系图 + 表**（默认）：系统为节点，接口连线带编号，另附表格；(b) **事件 / 异步拓扑**：通道和主题作为一等节点，位于生产者和消费者之间 [8]；(c) **API 全景 / 目录**：一张按负责方、生命周期和消费方列出众多 API 的组合表。

**有意不包含：** 字段级载荷（改为链接 OpenAPI/AsyncAPI/schema 文件）、系统内部（C3–C5）、单个场景中的调用顺序（E1）、主机和网络（G1）、数据血缘（D3）。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->

- **受众：** 集成架构师和解决方案架构师、双方开发人员、对端负责人、运维人员、安全评审人员，以及排定依赖进度的项目经理。
- **典型场景：** (1) 为一条新流程连接多个系统，例如从结账到支付再到仓库；(2) 与外部合作方准备接口协议，以表格作为议程；(3) 为迁移或整合盘点接口，范围"尽早"确定 [4]；(4) 安全与韧性评审：找出未认证、未限流或在关键路径上同步调用的接口；(5) 在事件驱动的系统群中找出谁生产、谁消费哪个事件。
- **不适用的情况：** 没有外部依赖的单个系统（C2/C5）；单个服务的内部（C4）；调用顺序或错误路径（E1）；字段级载荷文档（链接规范即可）；所有内部函数调用（那是依赖图）。
- **与相邻类型的区别：**
  - 需要知道有哪些应用、而不是每条连线上的契约时，选 **C1 应用全景图**。
  - 每个相邻系统只需一行用途说明时，选 **C2 系统上下文图**。
  - 表达*单个*系统内部可运行单元之间的通信时，选 **C3 容器图**。
  - 要解释契约*为什么*是这个样子（防腐层、开放主机服务）时，选 **C7 限界上下文映射图**。其模式可以作为本表的一列。
  - 表达一条调用链的时间顺序时，选 **E1 时序图**。主题是数据及其存储时，选 **D2/D3**。做信任边界分析时，选 **F2 威胁模型**，它以本表的认证列作为输入。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->

- **节点：** 系统；外部方用不同样式并注明所属组织；**承载含义的中介基础设施**（消息代理、API 网关、集成平台、文件共享）画成节点，不要藏在连线里 [12]。
- **连线：** 每个接口或接口组一条，带稳定的 **ID**（I-01…）和动宾短语标签（"授权支付"）。连线是单向的，标签与箭头方向一致，不用空泛的"使用"标签，图例解释每种线型 [13][14]。
- **箭头与线型：** 箭头只有一种含义，要么是*发起方 → 提供方*，要么是*数据流向*；异步路径画成**生产者 → 通道 → 消费者** [8]。线型是约定，所以要写进图例：实线 = 同步，虚线 = 异步消息或事件，点线加文件标记 = 批量/文件传输。
- **接口表（必备）。** 集成方式是**第一列**，其余各列依次如下：

| 列 | 要求 | 说明 |
|---|---|---|
| 集成方式 | R | 文件传输 / 共享数据库 / RPC-API / 消息 [2]。共享数据库是一种耦合被隐藏的接口。 |
| ID · 发起方 → 提供方 | R | 与连线对应；事件则写生产者和每个消费者。 |
| 用途 | R | 一行：该接口为何存在。 |
| 交互模式 | R | 请求-应答、命令、事件通知、事件携带状态传输、发布-订阅、批量 [15]。 |
| 协议 / 传输 | R* | *逻辑变体中省略 [4]。 |
| 格式 + 契约链接 | R | 链接到 OpenAPI / AsyncAPI / schema 文件 [6][7]；不要内联字段。 |
| 认证 / 授权 | R | 机制和身份。 |
| 流量 · SLA / 限制 | R | 示例数字标注"示意"。 |
| 失败语义 | 关键接口必填 | 重试、幂等、顺序、死信、去重 [16]。 |
| 负责方（提供方）· 负责方（消费方） | R | **双方**都要有具名团队或角色 [9]。 |
| 生命周期 / 版本 | O | 规划中 / 在用 / 已弃用；契约版本 [9]。 |
| 数据分级 | O | 供 F 族安全视图使用。 |

- **事实来源：** 仓库中的机器可读契约（OpenAPI 3.2.x、AsyncAPI 3.1.0）；据此生成或交叉核对表格 [6][7][14]。第 1 层展示全部系统，约 8–15 个节点（经验值）；第 2 层完整展示单个枢纽或合作方。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### 最佳实践

1. 先确定集成方式（文件、共享数据库、RPC、消息），再讨论产品 [1][2]。
2. 把异步通道画成节点，并写明投递语义（点对点或发布-订阅）、顺序和重复处理 [8][16]。
3. 区分命令和事件；对事件还要说明是哪一种：通知、事件携带状态传输还是事件溯源。只写"事件"会掩盖差异很大的耦合 [15]。
4. 契约保持机器可读、契约优先，并由契约派生表格。每个接口双方都有负责方，并标明生命周期状态 [6][9][14]。
5. 说明逻辑放在哪里：智能端点与哑管道，还是由中心枢纽路由和转换。据此标注中间件节点 [12]。

### 反模式

1. **只有连线没有表格：** 拓扑对所有要紧的事都保持沉默。
2. **同步与异步不加区分：** 潜在耦合和级联故障很晚才暴露 [16]。
3. **隐藏的集成：** 通过无人负责的共享数据库或文件投放进行集成。文件传输需要约定名称、位置、格式、时间和清理方式 [2]。
4. **箭头含义混用**（有时表示"调用"，有时表示"发送数据"），以及把命令和通知都叫作"事件" [15]。
5. **遗漏认证和限流，或 SLA 数字没有来源**；在图上画字段列表而不是链接契约。

## 范例 {#exemplars}
<!-- skill: omit -->

- [Enterprise Integration Patterns, integration styles](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html) — 表格第一列背后的词汇，并坦率说明了表示法的缺失（许可未核查）。
- [Azure Architecture Center, message broker and events for enterprise integration](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/integration/queues-events) — 区分同步/异步、带有消息代理和事件路由节点的参考架构（Microsoft Learn 条款）。
- [Azure Architecture Center, interservice communication](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication) — 对同步 API 与消息机制的取舍做了清晰讨论（Microsoft Learn 条款）。
- [AsyncAPI document concepts](https://www.asyncapi.com/docs/concepts/asyncapi-document) 和 [spec examples](https://github.com/asyncapi/spec) — 以通道、操作、消息和绑定作为契约（仓库为 Apache-2.0）。
- [EventCatalog](https://www.eventcatalog.dev) — 开源的生产者/消费者可视化工具，带负责方；可作为事件拓扑变体的参照（许可未核查）。
- [Backstage descriptor format](https://backstage.io/docs/features/software-catalog/descriptor-format/) — 带负责方、生命周期以及 provides/consumes 关系的 API 实体；可作为 API 全景变体的数据模型（Apache-2.0 项目）。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->

1. 确定范围、受众、变体（关系图、事件拓扑、API 全景）、逻辑还是技术、现状还是规划。
2. **先建接口清单再画图**：ID、集成方式，然后是其余各列。未知项留"?"交给用户确认；绝不臆造协议、SLA 或负责方。
3. 按领域或信任区对系统分组；超过约 15 个节点就拆图。
4. 按发起方向从左到右布局（店面前端在左、核心系统居中、合作方在右），或按纵向分区带布局（内部 | 中间件 | 外部）。消息代理和网关放在它们所中介的双方之间。
5. 节点：名称，可附负责方标签。外部系统用虚线边框，并注明所属组织。
6. 连线：ID 徽标加 2–4 个词的标签；线型区分同步/异步/批量；箭头为发起方 → 提供方，或生产者 → 通道 → 消费者。
7. 颜色编码归属领域或信任区（3–4 种低饱和色），另加一种警示色标出风险；绝不按技术着色。
8. 加标题（类型 + 范围）、图例，并在旁边或下方附上使用相同 ID 的表格。

**自检清单**
- [ ] 每条连线都有 ID 和标签；每个 ID 在表中恰好对应一行，反之亦然。
- [ ] 每一行都填了集成方式；共享数据库和文件投放没有被隐藏。
- [ ] 箭头只有一种语义；每个标签与其箭头方向一致。
- [ ] 同步与异步在视觉上可区分；异步路径画出了通道。
- [ ] 认证、SLA/限制和双方负责方均已填写或标为未知。
- [ ] 契约列链接到 OpenAPI/AsyncAPI/schema 文件；图上没有字段列表。
- [ ] 外部系统明显可区分；图上没有工作备注或"TBD"。
- [ ] 示意性数字已注明。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->

- 强证据：OpenAPI 文件（paths、servers、securitySchemes）、AsyncAPI 文件（channels、operations、bindings）、`.proto` 和 GraphQL schema、带认证和限流插件的 API 网关/ingress 路由、IaC 中的消息代理 topic/queue 定义、Kubernetes `Service`/`Ingress`/`NetworkPolicy`、环境变量中的端点 URL（`*_URL`、`*_HOST`）、HTTP/gRPC 客户端和生成的 SDK、契约测试、`catalog-info.yaml` 的 `providesApis`/`consumesApis`、CODEOWNERS。
- 条件允许时，用运行时链路追踪（OpenTelemetry 服务图）交叉核对现状 [14]。
- 代码里没有的（需要问人）：SLA 和流量、对端的归属、契约中的认证安排、数据分级、规划中的接口。共享数据库和文件投放类接口往往只出现在脚本或定时任务中；推断出的行标为"待确认"。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->

1. 范围内有哪些系统和外部方，谁来读这张图？（默认：内部架构师和开发人员；外部方画成具名方框。）
2. 现状还是规划？是否已有接口来源（OpenAPI/AsyncAPI、网关导出、电子表格）？（默认：现状，从仓库推断并由你确认。）
3. 以哪些集成方式为主？中间是否有消息代理、网关或集成平台？（默认：API 加一个消息代理。）
4. 哪种变体：接口关系图、事件拓扑还是 API 全景；逻辑还是技术？（默认：接口关系图，技术变体，附完整表格。）
5. 除必填列外，哪些列最重要？采用什么 ID 规则？（默认：必填列，ID 为 I-01…）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->

模型模板：`assets/templates/C6.json` · 布局模板：`grid_table` · `tables[]` 中的接口表（集成方式为首列）是主要输出；`grid_table` 只接受表格，所以配套的关系图是另一个模型，其边的 `step` 或 `label` 携带对应表行的接口 ID。

## 来源 {#sources}
<!-- skill: omit -->

1. Enterprise Integration Patterns, Messaging Patterns index — https://www.enterpriseintegrationpatterns.com/patterns/messaging/ — 访问于 2026-10-14
2. Enterprise Integration Patterns, Integration Styles — https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html — 访问于 2026-10-14
3. Hohpe & Woolf, Enterprise Integration Patterns, sample pages (diagram notation) — https://ptgmedia.pearsoncmg.com/images/9780321200686/samplepages/0321200683.pdf — 访问于 2026-10-14
4. The TOGAF Standard 9.2, Architectural Artifacts (Interface Catalog, Application Communication diagram, Application Interaction matrix) — https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap31.html — 访问于 2026-10-14（仅检索摘录；TOGAF 10 原文未核实）
5. Wikipedia, "Interface control document" (cites NASA Systems Engineering Handbook) — https://en.wikipedia.org/wiki/Interface_control_document — 访问于 2026-10-14（二手来源）
6. OpenAPI Initiative, OpenAPI Specification versions (3.2.1 current) — https://spec.openapis.org/oas/ — 访问于 2026-10-14
7. AsyncAPI, Specification reference (3.1.0 current) — https://www.asyncapi.com/docs/reference/specification/latest — 访问于 2026-10-14
8. Enterprise Integration Patterns, Message Channel / Publish-Subscribe Channel — https://www.enterpriseintegrationpatterns.com/patterns/messaging/ — 访问于 2026-10-14
9. Backstage, Descriptor format of catalog entities — https://backstage.io/docs/features/software-catalog/descriptor-format/ — 访问于 2026-10-14
10. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/42010/cm/ — 访问于 2026-10-14
11. SEI, Views and Beyond Collection — https://www.sei.cmu.edu/library/views-and-beyond-collection — 访问于 2026-10-14
12. Lewis & Fowler, "Microservices" (smart endpoints and dumb pipes) — https://martinfowler.com/articles/microservices.html — 访问于 2026-10-14
13. C4 model, Review checklist — https://c4model.com/diagrams/checklist — 访问于 2026-10-14
14. C4 model, FAQ — https://c4model.com/diagrams/faq — 访问于 2026-10-14
15. Fowler, "What do you mean by 'Event-Driven'?" — https://martinfowler.com/articles/201701-event-driven.html — 访问于 2026-10-14
16. Azure Architecture Center, "Interservice communication in microservices" — https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->

![C6 示例：网店接口关系图与接口表——结账调用支付服务商（RPC），订单事件经消息代理发往仓库（消息），仓库每晚发送库存文件（文件传输），客服聊天机器人读取订单状态（RPC）](/samples/C6-integration-interface.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
