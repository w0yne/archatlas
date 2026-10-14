---
code: G2
slug: cloud-infrastructure-architecture
family: G
names:
  en: Cloud infrastructure architecture
  zh: 云基础设施架构图
  aliases:
    en: [cloud architecture diagram, cloud solution architecture, provider infrastructure view, provider-specific infrastructure view, cloud reference architecture]
    zh: [云架构图, 云解决方案架构图, 云服务架构图, 云参考架构]
question: 哪些云能力实现了该工作负载，又是哪些取舍让这种编排符合其需求？
audiences: [architects, operations, security]
levels: [physical]
phases: [design, operate]
scope: 一个云服务商上的一个工作负载（或已说明的多云划分），展示所选服务、职责、主要请求与数据路径，以及真实的位置边界或故障边界
formal: {kind: convention, ref: 'No single standard. Provider icon sets and provider architecture-centre guidance are conventions; Well-Architected frameworks are design-review guidance, not drawing notations'}
neighbours: [C3, C5, G1, G3, G4]
status: draft
translationOf: en/types/G2-cloud-infrastructure-architecture.md
sourceRev: 1ed1739
reviewed: false
---

# 云基础设施架构图（Cloud Infrastructure Architecture）

> 针对一个工作负载的图：展示实现它的云服务、为何如此编排，以及真实的归属边界和故障边界在哪里。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 哪些云能力实现了这个工作负载，又是哪些取舍让这种编排符合其可靠性、安全、运维、性能和成本目标？
- **视点：** 架构描述中的技术或基础设施关注点。这是一个非正式的、按关注点划分的图类：云服务商的图标库用于识别服务，Well-Architected 框架用于指导评审而非绘图 [1][2][3][4]。并非所有云架构图都是“物理”的：基于托管服务的设计可能有意隐藏机器。
- **深层含义：** 有价值的内容在于服务和边界为何如此编排，而不在于出现了多少熟悉的图标。服务选型应依据需求以及故障或成本假设。
- **不包含：** 源码模块、每个 API 端点、详细的路由表和防火墙规则表（G3），以及软件实例的部署位置（G1），除非它们决定了编排方式。
- **本站采用的定义：** 本页讨论的是*单个工作负载的云架构*。*参考架构*（reference architecture）是另一种状态：一种可复用的、推荐的编排方式，并附有明确的假设。用 `reference | proposed solution | declared implementation | observed deployment` 记录状态，而不要把这些名称混为一谈。截至 2026-10-14 的核查，AWS 描述了六大支柱，Azure 五大，Google Cloud 六大 [1][2][3]；数量会变化，也不是绘图方法。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 云与平台架构师、运维人员、安全评审人员、合作伙伴，以及需要了解主要取舍的决策者。
- **典型场景：**
  1. 为网店的店面和 API 评估落地模式。
  2. 将订单处理和后台作业迁移到托管服务。
  3. 为某个可用性目标选择生产基线。
  4. 解释客服聊天机器人、向量存储和模型端点如何组合。
  5. 并排比较成本与弹性方案。
- **不适用的情况：** 用作业务概览，或用来证明已部署、合规、服务可用性或量化的 SLA。
- **与相邻类型的区别：**
  - 哪些软件实例运行在哪些主机上，选 **G1**。
  - 路由、分段和可达性，选 **G3**。
  - 与云服务商无关的软件结构，选 **C3** 或 **C5**。
  - 交付机制，选 **G4**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 非正式。图标只是约定，厂商标志并不证明适用性。
- **必备元素：**
  - 工作负载、范围、云服务商和设计状态（参考、提议、声明、观察）。
  - 所选服务，每项都写明其在工作负载中的角色（“托管队列：后台作业”）。
  - 主要的请求与数据路径。
  - 有实质意义的归属、位置和故障边界；假设；图例。
- **箭头：** 说明它们表示请求、事件、复制、配置还是依赖。将运行时路径与管理路径和交付路径分开。
- **分组：** 使用云服务商的真实语义。账号、项目或订阅、区域、可用区、VPC 或 VNet 以及服务边界不能互换。一些托管服务或全局服务位于客户网络之外；应正确画出私有端点和服务本身，而不是把一切都包进一个网络框里。
- **可选：** 服务规格档位、扩缩容边界、冗余、备份与恢复、身份与密钥、遥测、数据生命周期、对成本敏感的依赖。当它们能回答所选关注点时才纳入。
- **文字预算：** 每项服务约 3–6 个词（名称加角色）；取舍和假设写在图旁。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **从需求以及故障或成本假设出发，** 再选择服务 [1][2][3]。
2. **尊重示例的适用范围。** Azure 的基础 Web 应用页面明确说明它用于学习和概念验证，而非生产，因此照搬这张图并不能得到生产基线 [5]。
3. **只有当可用区或区域隔离确实存在且重要时才画出；** 重复的图标并不能证明有复制、备份或恢复。
4. **把备选方案分开。** 不要用同一种样式画已建成的路径和提议的服务。
5. **链接而不是吸收**详细的安全视图和网络视图；用文字说明责任共担的划分。

### 反模式
1. **图标大杂烩：** 罗列产品，却没有说明其在工作负载中的角色。
2. **把一切放进一个 VPC 框，** 包括全局服务或云服务商托管的服务。
3. **无标签的箭头**，混杂了运行时、管理和交付路径。
4. **没有机制支撑的可用性声明：** 两个图标，却没有复制。
5. **罗列防火墙规则**，而不是展示服务编排。

## 范例 {#exemplars}
<!-- skill: omit -->
- [AWS: Web Application Architecture](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/web-application-architecture/web-application-architecture.html) — 跨多可用区的 Web 层级和应用层级，配合托管数据服务，并附说明。AWS 文档；AWS 允许在其工具包条款下使用其图标 [4]。
- [Azure: Basic web application](https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/basic-web-app) — 简洁地展示运行时、身份和监控的角色，并对生产用途的限制写得格外清楚。
- [Google Cloud: Three-tier web app template](https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app) — 前端、API、缓存和数据路径作为一个服务组合，并关联到可配置的部署。
- 厂商页面仍属厂商资料：复制图稿前请查看具体页面或图标包的条款。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 在标题中写明工作负载、约束、受众、云服务商和状态，例如“托管平台上的网店店面：提议”。
2. 先列出职责（提供页面、接收订单、运行作业、存储数据、认证）；再选择服务，每个角色一项。
3. 布局：沿主要请求路径从左到右排列（客户端、边缘、计算、数据）。支撑服务（身份、密钥、监控）放在下方或上方的条带中，而不是主行里。
4. 只对真实边界分组：云服务商账号或项目、区域、可用区，以及服务真正接入的网络。托管服务或全局服务放在网络框之外。
5. 连线：每条箭头都标明含义；运行时用一种线型，异步事件或复制用另一种，管理用第三种。
6. 文字：服务名加角色，约 3–6 个词；在图旁用简短注释写出两三个关键取舍。
7. 颜色：中性填充，数据层级以及外部或托管服务使用不同的浅色调；只有当云服务商图标有助于识别且复用条款允许时才使用，否则使用带标签的普通形状。

**自检清单**
- [ ] 标题附近写明了状态（参考、提议、声明或观察）。
- [ ] 每项服务都有其在工作负载中的角色，而不只是产品名。
- [ ] 图例中解释了每种箭头类型。
- [ ] 区域、可用区和网络边界符合云服务商的语义。
- [ ] 托管服务或全局服务没有被放进它们不属于的子网。
- [ ] 可用性或弹性声明写明了机制，否则不写。
- [ ] 图附有假设以及两三个取舍。
- [ ] 图标或图稿的复用依据已说明。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **服务：** 基础设施即代码（IaC）模块和资源类型、云服务商版本、已配置的服务规格档位和规模、资源引用。
- **连接关系：** 事件订阅、端点、队列和主题名称、扩缩容和备份声明、各环境变体。
- **工作负载角色：** 应用代码能说明角色，但不能证明托管服务已经开通。
- **必须由人提供：** 在仓库之外管理的基础（账号、着陆区、共享网络）、实际规模和成本、需求与取舍。
- IaC 工具生成的依赖图不是完成的架构。将结果标为“声明”；绝不为了探查而执行部署操作。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 这是可复用的参考模式，还是某个实际工作负载的架构？（一个工作负载）
2. 适用哪些云服务商、区域和数据驻留约束？（一个云服务商、一个区域，已说明）
3. 哪些质量目标驱动设计，哪些折中可以接受？（可用性和成本；接受单区域）
4. 哪些基础设施已在别处管理？（显示为外部）
5. 路由、部署和恢复是否应作为单独的视图？（是，加链接）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/G2.json` · 布局模板：`layered` · 各层级（边缘、计算、数据、支撑）成为 `layer` 分组，云服务商边界（账号、区域、可用区）成为 `boundary` 分组，服务是节点，其角色写在 `sub` 中，箭头使用带明确标签的 `call`、`data` 或 `async` 边类型；设计状态由节点的 `style` 和 `evidence` 承载。

## 来源 {#sources}
<!-- skill: omit -->
1. AWS, Architecture Center (Well-Architected, six pillars) — https://aws.amazon.com/architecture/ — 访问于 2026-10-14
2. Microsoft, "Azure Well-Architected Framework pillars" (five pillars) — https://learn.microsoft.com/en-us/azure/well-architected/pillars — 访问于 2026-10-14
3. Google Cloud, "Well-Architected Framework" (six pillars) — https://docs.cloud.google.com/architecture/framework — 访问于 2026-10-14
4. AWS, "Architecture Icons" — https://aws.amazon.com/architecture/icons/ — 访问于 2026-10-14
5. Microsoft, "Basic web application" (Azure Architecture Center) — https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/basic-web-app — 访问于 2026-10-14
6. AWS, "Web Application Architecture" (first published 19 November 2021) — https://docs.aws.amazon.com/reference-architecture-diagrams/latest/web-application-architecture/web-application-architecture.html — 访问于 2026-10-14
7. Google Cloud, "Three-tier web app template" — https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app — 访问于 2026-10-14
8. ISO/IEC/IEEE 42010:2022，仅公开范围部分；页面返回 HTTP 403，未审阅全文 — https://www.iso.org/standard/74393.html — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![G2 示例：网店在通用云上的基础设施（拟议）](/samples/G2-cloud-infrastructure-architecture.svg)
*通用云上的拟议基础设施：边缘是 CDN，区域 A（可用区 1 和 2）运行应用服务，托管数据库在可用区 2 有副本。箭头分别标注“转发请求”和“读写”。*
