---
code: C1
slug: application-landscape
family: C
names:
  en: Application landscape
  zh: 应用全景图
  aliases:
    en: [application portfolio view, application communication diagram, system landscape diagram, IT landscape, Application Architecture (portfolio sense), Application Landscape Map, Application Cooperation View, System Landscape Diagram (C4 model), Cluster Map]
    zh: [应用地图, 系统全景图, 应用组合图, 应用协作视图, IT 蓝图]
question: 这个范围内有哪些应用，它们如何分组，哪些应用之间存在依赖或数据交换？
audiences: [architects, leaders]
levels: [logical]
phases: [initiate, design]
scope: 在一个明确的范围（企业、部门或产品线）内的多个应用，只画到应用层级。
formal: {kind: method, ref: 'No single notation. Related: TOGAF 9.2 Application Communication diagram and Application Portfolio catalog; ArchiMate 3.2 Application Cooperation viewpoint; C4 model System Landscape diagram'}
neighbours: [A1, A7, A8, C2, C3, C5, C6, I2]
status: draft
translationOf: en/types/C1-application-landscape.md
sourceRev: 9065169
reviewed: false
---

# 应用全景图（Application landscape）

> 一个范围内的应用地图：按一个明确的标准分组，并以主要依赖关系相连。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
它回答的是：*这里有哪些应用，如何分组，哪些应用之间存在依赖或数据交换？*按 ISO/IEC/IEEE 42010 的含义，它是应用组合层面的视点：关注点是重叠、归属、变更影响和集成热点 [9]。TOGAF 将其置于应用架构域（应用组合目录（Application Portfolio catalog）、应用通信图（Application Communication diagram））[2][3]；在 ArchiMate 中，它接近应用协作视点（Application Cooperation viewpoint）[5]。它不包含应用内部结构（C3/C4/C5）、托管部署（G1）、协议、认证或 SLA 等接口属性（C6）、数据模式（D1）以及流程流转（A5）。
**本站采用的定义：**“应用架构”有两层含义：多个应用组成的组合（TOGAF，即本类型）和单个应用的内部设计 [2][10]。多个应用 → C1；单个应用的组成部分 → C3、C5 或 C8。
**本编号下的三种变体：**(a) *分组全景图*：应用按层、领域或能力放入横带（默认）；(b) *通信关系图*：以关系为中心，核心应用居中（TOGAF 应用通信图、ArchiMate 应用协作视图、EAM Pattern Catalog 中的聚类图（cluster map）[14]）；(c) *能力 × 应用矩阵*（A1 的派生视图）：行 = 能力，单元格 = 应用，可选地做成热力图（TOGAF 应用/功能矩阵（Application/Function matrix））[3][11]。C4 model 的**系统全景图**（System Landscape diagram）是 (a)/(b) 的最简形式：在明确的范围内只画人员和软件系统，不含容器和应用组合元数据，即“没有特定焦点的系统上下文图” [1]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：**架构师、IT 管理层、应用组合与集成团队、安全团队（影响范围）、新加入的架构师。
- **场景：**应用组合合理化，例如使用容忍 / 投资 / 迁移 / 淘汰（Tolerate/Invest/Migrate/Eliminate）适配网格 [21]；替换或下线某个应用前的影响检查；并购或平台整合 [20]；共享平台及其上层业务应用的概览；作为目标态路线图（A8）的基线。
- **不适用的情况：**只有一个系统和少数相邻系统（C2）；单个系统的内部结构（C3/C5）；字段级数据流（D2/C6）；没有人会持续更新它，因为过时的全景图会误导读者 [10][12]。
- **与相邻类型的区别：**
  - 以某一个系统为焦点、需要其用户和相邻系统时，选 **C2**。
  - 需要单个系统的运行部件及其技术时，选 **C3**。
  - 每个接口都需要注明协议、认证、频率或 SLA 时，选 **C6**。
  - 问题是业务能力覆盖时，选 **A1**（可把这里的变体 c 作为叠加层）。
  - 需要在一张 ArchiMate 视图中同时呈现业务层、应用层和技术层时，选 **I2**。
  - 非技术读者需要了解一个方案的主要组成，而不是应用清单时，选 **A7**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：**应用方框，按组织内部的叫法命名，且全部属于同一类 [16]；分组框，采用一个明确的标准（层、领域、能力或归属方），每个应用恰好属于一个分组 [10]；有向关系线，带简短标签，说明流动的内容或原因；标题注明类型、范围和日期；覆盖每种颜色、边框和徽标的图例 [15][22]；一句范围说明，写明哪些在范围内、哪些属于外部。
- **可选：**一次只用一种元数据叠加层：生命周期（计划中 / 运行中 / 退役中）、来源方式（自建 / 外购 / SaaS）或归属方，以标签或单一色阶呈现 [10]；共享平台横带；位于边缘、样式更低调的外部服务；只有当数据存储是共享集成点时才使用数据存储图形。
- **接口：**TOGAF 的应用通信图确实会画出应用之间的接口 [3][13]。与 C6 的分界取决于*属性的详细程度*（协议、认证、SLA、频率），而不在于是否出现接口。
- **箭头语义：**选定一种并写入图例：“A → B = A 依赖 / 调用 B”（C4 model、Azure 指南 [15]），或“A → B = 数据从 A 流向 B”（ArchiMate 流）。两者绝不混用；避免双向箭头。
- **分组：**“渠道 / 业务应用 / 共享平台 / 外部”这组横带是一种常见模式，而不是标准。要问清哪条分组轴最契合问题。
- **ArchiMate 映射（如需正式模型）：**每个应用对应一个应用组件（Application Component），用 `serving` 表示“使用其服务”，用 `flow` 表示数据流动 [8]。注明版本：大多数工具实现的是 ArchiMate 3.2（2022）；ArchiMate 4（2026 年 4 月发布）把“层”更名为“域”，并合并了各层专属的行为元素 [6][7]。ArchiMate 4 的细节取自已发表的综述，尚未对照现行规范文本核实。
- **相关的 TOGAF 制品：**接口目录、应用/功能矩阵、应用/组织矩阵和应用交互矩阵、应用与用户位置图 [3][4]。这些名称出自 TOGAF 9.x 资料，尚未对照现行 TOGAF 10 文本核实。
- **细节与命名：**只画到应用层级。如果想在方框里列出模块或功能，应改画 C3 或 C5 图。同级元素使用同一类名称；绝不用能力名称给应用命名 [11]。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. 动手画之前先确定范围、分组轴和清单来源；先摆放分组，再摆放应用 [10][12]。
2. 把元数据当作叠加层，而不是几何结构：每张视图一种状态，并以图例说明；第二种状态需要第二张视图 [10]。
3. 用聚焦视图控制密度：一张总览图，再每个领域一张图，而不是一张拥挤的海报 [12][22]。
4. 以枢纽应用为布局锚点：连接最多的应用居中，连接两个枢纽的应用放在两者之间，只连接一个枢纽的应用放在该枢纽旁边 [13]。
5. 保持图的鲜活：从目录或代码中导出应用和集成关系，由人来负责分组、归属和生命周期，并在图上注明更新负责人和日期 [10][19]。

### 反模式
1. 只有一堆方框而没有关系：那是目录，不是全景图 [10]。
2. 把技术部件（缓存、队列、负载均衡器）画成与应用同级，或者在一行中混杂能力、流程和应用 [11]。
3. 同时通过颜色、边框、图标和标签编码多种状态 [10]。
4. 图面拥挤时删掉集成关系；应改为连接到分组边框 [10]。
5. 在图上写工作备注、决策或理由；应把它们放在正文或决策记录中 [23]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [C4 model: System landscape diagram](https://c4model.com/diagrams/system-landscape) — 最精简的全景图表示法，带有精确的范围规则（网站内容采用 CC BY 4.0）。
- [Structurizr: enterprise usage](https://docs.structurizr.com/workspaces/enterprise) — 由各团队维护的定义自动生成的全景图，而非手工绘制。
- [TU München EAM Pattern Catalog v1.0](https://www.cs.cit.tum.de/fileadmin/w00cfj/sebis/_my_direct_uploads/EAMPatternCatalogV1.0.pdf) — 聚类图、流程支撑图和信息流视图，每种都与干系人关注点相对应（© TU München；可阅读，勿复制）。
- [ArchiSurance case study](https://github.com/archimate-models/archisurance) — 用 ArchiMate 应用协作视图呈现的基线与目标应用架构（许可：请查看仓库）。
- [Dragon1: how to create an application landscape diagram](https://www.dragon1.com/tutorials/how-to-create-an-application-landscape-diagram) — 从授权、数据收集到布局与维护的完整过程。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 用一句话写明范围和视角（哪个范围；什么算作一个应用），并放进标题或图例。
2. 盘点应用：名称、一行用途说明、归属方、生命周期；把每个应用标为内部、共享平台或外部。
3. 选择变体（分组全景图、通信关系图、能力矩阵）和一条分组轴；每个应用只有一个主分组。
4. 布局：(a) 用自上而下的横带（渠道 → 业务应用 → 共享平台；外部放在侧边或底部）；(b) 枢纽居中；(c) 用网格。示例：一家网店，网店前台和移动 App 在上方，商品目录、购物车与结账、订单管理和客户支持（含客服聊天机器人）在中间，身份和数据平台在下方，支付服务商和仓储系统在边缘。
5. 视觉权重：主角更大，同级元素大小和样式一致，“其他应用”小而低调；共享应用在各处保持同一样式。
6. 线条：只画问题所需的依赖；标签写流动的内容（1–3 个词，如“订单”“库存水平”），不写协议；每个箭头终止于确切的方框，分组级连线终止于分组边框。
7. 最多一种元数据叠加层；颜色加第二种提示（标签或图案）；全部写入图例。
8. 文字预算：方框 = 名称加至多 3 个词的描述；不写要点列表、功能清单或备注。

**自检清单**
- [ ] 标题注明类型和范围；图例解释了每种颜色、线条和徽标。
- [ ] 每个方框都是同一类的应用；没有混入能力、组件或步骤。
- [ ] 每个应用恰好属于一个分组，每个分组都有清晰的标准。
- [ ] 每条线都只有一个方向并带标签；只用一种箭头约定，且已写明。
- [ ] 没有内部结构、托管节点或协议细节（C3、G1、C6）。
- [ ] 最多一种状态叠加层；同级元素外观一致。
- [ ] 图上没有工作备注、TBD 或理由说明。
- [ ] 每个元素都能追溯到一条清单记录、清单文件或目录条目，否则标为计划中。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 服务目录文件（例如 Backstage `catalog-info.yaml`：system、owner、lifecycle、`dependsOn`、提供和消费的 API）[17]。
- Kubernetes 标签，如 `app.kubernetes.io/part-of` 和 `name`、ingress 路由、网络策略 [18]；compose 文件（把服务归并到其所属应用）。
- API 规范（OpenAPI、AsyncAPI、protobuf）和内部客户端库提供“提供方–消费方”配对；`CODEOWNERS` 提供归属方。
- 基础设施即代码的资源标签（`application`、`owner`）能提供清单，但依赖信息较弱；CI 流水线显示哪些应用仍在使用。
- 代码里没有的：没有代码仓库的外购和 SaaS 应用、分组轴、业务归属和生命周期决策。需要问人，或使用资产清单或采购清单。凡是从代码得到的内容，都视为待确认的候选项。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 哪个范围？这里什么算作一个应用？（一条产品线；一个团队负责的系统 = 一个应用）
2. 这张图要支持哪项决策：合理化、影响分析、新人入职还是集成规划？（影响分析）
3. 采用哪种变体和分组轴：层、领域、能力还是归属方？（按层分组的全景图）
4. 叠加层要显示哪一个属性：生命周期、来源方式、归属方，还是不显示？现状还是目标状态？（不显示；现状）
5. 箭头表示“依赖于”还是“数据流向”？画出所有连接，还是只画跨分组的连接？（依赖于；只画问题所需的连接）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/C1.json` · 布局模板：`statechart`（从左到右；`layered` 模板则把同样的层自上而下堆叠）· 类型为 `layer` 的分组渲染为按分组间连线分层的分区；`system` 和 `external` 节点放在各自的横带中；边在横带之间布线（变体 c 使用以 `grid_table` 渲染的 `tables[]`）。

## 来源 {#sources}
<!-- skill: omit -->
1. C4 model — System landscape diagram — https://c4model.com/diagrams/system-landscape — 访问于 2026-10-14
2. The Open Group — TOGAF Standard, 10th Edition launch — https://www.opengroup.org/open-group-announces-launch-togaf-standard-10th-edition — 访问于 2026-10-14
3. TOGAF Standard Courseware V9.1 — Sample catalogs, matrices and diagrams — http://www.togaf.info/togafSlides91/TOGAF-V91-Sample-Catalogs-Matrics-Diagrams-v3.pdf — 访问于 2026-10-14
4. QualiWare CoE — TOGAF artifacts — https://coe.qualiware.com/resources/togaf/togaf-artifacts — 访问于 2026-10-14
5. The Open Group — ArchiMate 3.2 Specification reference cards — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — 访问于 2026-10-14
6. The Open Group — ArchiMate 4 Specification announcement — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — 访问于 2026-10-14
7. Bizzdesign — What really changes in ArchiMate 4 — https://bizzdesign.com/blog/archimate-4-changes — 访问于 2026-10-14
8. Bizzdesign — Practical ArchiMate viewpoints for the application layer — https://bizzdesign.com/blog/practical-archimate-viewpoints-for-the-application-layer — 访问于 2026-10-14
9. IEEE SA — ISO/IEC/IEEE 42010:2022 — https://standards.ieee.org/ieee/42010/6846 — 访问于 2026-10-14
10. Catio — Application landscape diagrams — https://www.catio.tech/blog/application-landscape-diagram — 访问于 2026-10-14
11. Sparx Systems — Application landscape view guide — https://www.sparxsystems.us/application-portfolio-management/application-landscape-view-guide — 访问于 2026-10-14
12. Dragon1 — How to create an application landscape diagram — https://www.dragon1.com/tutorials/how-to-create-an-application-landscape-diagram — 访问于 2026-10-14
13. Orbus Software — Landscape diagrams part 6: application communication diagram — https://www.orbussoftware.com/resources/blog/detail/landscape-diagrams-pt6-application-communication-diagram — 访问于 2026-10-14
14. TU München sebis — EAM Pattern Catalog v1.0 — https://www.cs.cit.tum.de/fileadmin/w00cfj/sebis/_my_direct_uploads/EAMPatternCatalogV1.0.pdf — 访问于 2026-10-14
15. Microsoft Learn — Create architecture design diagrams (Azure Well-Architected) — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — 访问于 2026-10-14
16. Martin Fowler — Application Boundary — https://martinfowler.com/bliki/ApplicationBoundary.html — 访问于 2026-10-14
17. Backstage — System model — https://backstage.io/docs/features/software-catalog/system-model — 访问于 2026-10-14
18. Kubernetes — Recommended labels — https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/ — 访问于 2026-10-14
19. Structurizr — Enterprise usage — https://docs.structurizr.com/workspaces/enterprise — 访问于 2026-10-14
20. ArchiSurance case study — https://github.com/archimate-models/archisurance — 访问于 2026-10-14
21. LeanIX — Gartner TIME model — https://www.leanix.net/en/wiki/apm/gartner-time-model — 访问于 2026-10-14
22. C4 model — Notation — https://c4model.com/diagrams/notation — 访问于 2026-10-14
23. Working Software — Misuses and mistakes of the C4 model — https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![C1 示例：网店的应用全景图，分四层](/samples/C1-application-landscape.zh.svg)
*网店的应用全景图，分四层，每层是一个着色分区：渠道（网页商城、移动应用、客服聊天组件）、业务应用（商城、后台、客服机器人）、共享平台（身份认证、通知、搜索）和外部服务（支付服务商、承运商、邮件服务）。标签说明接入类型或归属，深色卡片是本图主体（商城），层间箭头标明流转内容。*
