---
code: I2
slug: archimate-layered-view
family: I
names:
  en: ArchiMate layered view
  zh: ArchiMate 分层视图
  aliases:
    en: [ArchiMate layered viewpoint, business-application-technology view, cross-layer enterprise view]
    zh: [ArchiMate 分层视点, 业务-应用-技术视图, 跨层企业架构视图]
question: 业务行为、应用与技术如何相互支撑？一处变化会影响哪些部分？
audiences: [architects, leaders]
levels: [strategy, concept, logical]
phases: [initiate, design]
scope: enterprise
formal: {kind: standard, ref: 'The Open Group，ArchiMate 3.2（2022），附录 C.1.5 中的资料性分层视点；https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html'}
neighbours: [A7, C1, C8, I1]
status: draft
sourceRev: 88db750
translationOf: en/types/I2-archimate-layered-view.md
reviewed: false
---

# ArchiMate 分层视图（ArchiMate layered view）

**方法参考。** 明确需要时仍可使用；不在默认25项核心目录中。此页与历史链接继续保留。

> 业务、应用、技术元素分层排布，用 ArchiMate 关系说明谁服务谁、谁实现谁。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
**本站采用的定义：** 标准化建模语言 ArchiMate 3.2 中，**附录 C.1.5 的资料性分层视点（Layered Viewpoint）**；它并不代表整套语言 [1]。
它解释选定企业架构层之间的一致性与变更影响：专用层实现服务，服务再服务于其使用方。
层的顺序、数量和性质均可灵活选择。业务/应用/技术是常见排列方式，不是强制的三层带状模板 [1]。
它省略详细执行时序和代码依赖。它不等同于 TOGAF BDAT：ArchiMate 通过分布在各层的被动元素建模信息，并没有独立的核心数据层 [2][8]。
本页**明确针对 3.2**。ArchiMate 4 已于 2026 年 4 月发布；不要假设这里针对特定版本的规则也适用于该版本 [9]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 企业、业务、应用和技术架构师，以及评审特定范围内支撑关系链的负责人。
- **变更影响：** 识别网店中依赖某项技术服务的业务操作。
- **共享服务：** 展示支撑结账和退货的应用。
- **整合：** 比较网店在基线与目标态下的支撑关系链。
- **服务评审：** 发现尚无明确使用方或实现方式的客服聊天机器人服务。
- **不适用：** 详细请求顺序、API 载荷、完整清单，或缺乏领域证据时推断出的业务结构。
- 只需较小范围的依赖切片时，选应用使用视点（Application Usage）或技术使用视点（Technology Usage）；关注实现行为时选服务实现视点（Service Realization）；关注制品分配时选实现与部署视点（Implementation and Deployment）[1]。
- 关注代码层依赖时选 **C8**，关注非正式概念分层时选 **A7**，关注系统组合时选 **C1**，组织多种软件视图时选 **I1**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **本绘图步骤要求具备：** 范围、明确类型的元素、有意义的跨层关系及图例。不存在强制的固定元素清单。
- 按需选择行为主体/角色、流程/功能、组件、服务和节点；信息对象、接口、制品及内部细节均为可选 [3]。
- **服务于（Serving）：** 提供方 → 使用方；实线、开口箭头。它表达功能的提供关系，不表示请求方向。
- **实现（Realization）：** 具体元素 → 抽象元素；虚线、空心三角箭头。功能实现服务；制品实现组件。
- **分配（Assignment）：** 执行方/承载方 → 行为/制品；实线，源端圆点，目标端实心箭头。例如：节点 → 制品。
- **部署：** `Node —Assignment→ Artifact —Realization→ Application Component`；“hosted-on”不是一种通用的 ArchiMate 关系 [3][5]。
- **访问（Access）** 表示对被动结构的读写；**触发（Triggering）** 表示时间或因果依赖；**流（Flow）** 表示传递。应使用各自不同的标准符号 [3]。
- 根据元模型和规范性附录 B，验证源元素/关系/目标元素的组合以及通过推导得到的简化连接。选择全部核心关系类型，并不意味着所有端点组合都合法 [4]。
- 结构元素用名词命名，行为用动作命名。解释嵌套的含义；仅有背景色带并不能建立任何关系。
- 黄/蓝/绿是可选惯例，颜色没有正式语义 [2]。
- 在证据注释或表格中记录不确定性，绝不能把正式表示法中的虚线改作“推断”标记。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- 选择一个范围明确的关注点，避免在一页中罗列整个企业 [1]。
- 区分执行方、行为、服务和使用方，避免用未标明含义的连线笼统表示“支撑” [3][10]。
- 保留标准方向，不要为了模仿 API 请求方向而反转 Serving [10]。
- 验证关系两端的具体类型，避免任意跨层实现关系或通用的承载箭头 [4][5]。
- 让可比较的分组保持一致，颜色只作辅助提示；避免固定层数或仅凭颜色辨别类型 [1][2]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Open Group，C.1.5，表 27 对应示例](https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html) — 经典的专用层/服务层排列，原文明示并非强制要求。**许可：** 尚未确认开放的图片复用许可；仅提供链接；官方 HTML 可能需要登录。
- [Open Group，第 11 章，示例 34](https://pubs.opengroup.org/architecture/archimate3-doc/ch-Relationships-Between-Core-Layers.html) — 具体的跨层示例，使用可选字母标记区分各层。这是相关指导，不是另一个命名的分层视点。**许可：** 尚未确认图片复用许可；仅提供链接。
- [Visual Paradigm，“Layered Viewpoint Example”图](https://circle.visual-paradigm.com/docs/archimate/archimate-viewpoints/archimate-viewpoint-layered-viewpoint/) — 将具体图形与干系人的关注点联系起来；页面引用的是 **3.1**，而非 3.2。**许可：** 尚未核实图片的开放许可；仅提供链接。
- [Open Group 认证证据，§2.11 分层视点](https://certification.opengroup.org/register/archimate/orbus_archimate3_tool_se2.pdf) — 与聚焦视图并列展示的工具渲染示例；它是 **3.1** 的认证提交材料，不能证明符合 3.2。**许可：** 公开托管认证材料不意味着授予复用权；仅提供链接。

已通过文本和搜索索引摘录定位范例，尚未进行图片视觉复核。工具范例可能沿用标准中的示例模型，因此不将它们称为独立案例研究。改编图稿前应核实权利；应创作新场景，而非复制原图。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 明确关注点、边界、基线/目标态及 ArchiMate 版本。
2. 清点有证据支持的业务行为、应用服务和技术支撑。
3. 在排列方框前，指定准确类型并验证关系。
4. 在有助于理解的分层带中对齐提供方和使用方；业务在上、应用居中、技术在下只是可选布局。
5. 使用简短名称、类型图标和少量颜色，必要时加入服务层带。
6. 保留箭头方向与符号，解释嵌套，并单独标注证据。
7. 沿支撑关系链追踪结账关注点，将密集细节拆成聚焦视图。
8. 复核语义有效性和可读性；渲染器输出若使用非正式表示法，必须明确标注。

**自检清单**
- [ ] 范围和版本明确。
- [ ] 组件、行为和服务已区分。
- [ ] 每条关系都适用于其端点类型。
- [ ] Serving 和 Realization 的方向正确。
- [ ] 部署采用制品/分配语义。
- [ ] 未将层数和颜色视为规范性要求。
- [ ] 证据状态未改变正式线型语义。
- [ ] 标签、符号和端点清晰可读。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 组件/行为：实现职责、处理函数、入口点和构建边界。
- 服务/使用方：接口契约、客户端、配置和集成测试。
- 制品/分配：构建输出、镜像引用、部署清单和基础设施定义。
- 信息：模式定义和读写代码；名称本身不能确立业务含义。
- 业务角色/流程/服务：经过验证的需求和领域文档；仅有代码并不足够。
- 记录提交版本、路径/符号、关系类型和置信度。配置不能证明实际运行状态。
- 使用证据注释，不要自动用虚线标记推断；元模型有效性与事实证据需要分别检查。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 这张视图要向哪些人解释哪项业务服务或变更？
2. 采用哪个边界，以及哪个基线或目标态？
3. 哪些业务事实已经确立，而非推断？
4. 关注点是服务支撑、实现、部署，还是需要拆成多个聚焦视图？
5. 读者需要正式的 ArchiMate 3.2 表示法，还是明确标为非正式的概览？

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/I2.json` · 布局模板：`layered` · 业务、应用和技术是 `layer` 分组；关系类型写成边标签，边的 kind 为 `dependency` 或 `assoc`。
近似表示：不绘制正式的 ArchiMate 符号，也不验证元模型；生成正式表示法的图之前，需要单独核实这些能力。

## 来源 {#sources}
<!-- skill: omit -->
1. The Open Group，*ArchiMate 3.2 — Example Viewpoints*，C.1.5/表 27 — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html — 访问于 2026-10-14；官方文本的搜索索引摘录。
2. The Open Group，*ArchiMate 3.2 — Language Structure* — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Language-Structure.html — 访问于 2026-10-14；官方文本的搜索索引摘录。
3. The Open Group，*ArchiMate 3.2 Specification Reference Cards*，N221（2022）— https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — 访问于 2026-10-14；已提取 PDF 全文。
4. The Open Group，*ArchiMate 3.2 — Relationships (Normative)*，附录 B — https://pubs.opengroup.org/architecture/archimate3-doc/ch-relationships-Normative.html — 访问于 2026-10-14；依据搜索索引摘录，未取得完整关系表。
5. The Open Group，*ArchiMate 3.2 — Relationships between Core Layers*，含示例 34 — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Relationships-Between-Core-Layers.html — 访问于 2026-10-14；官方文本的搜索索引摘录。
6. Visual Paradigm，*ArchiMate Viewpoint: Layered Viewpoint* — https://circle.visual-paradigm.com/docs/archimate/archimate-viewpoints/archimate-viewpoint-layered-viewpoint/ — 访问于 2026-10-14；提取的页面文本引用 3.1。
7. *ArchiMate 3.1 Tool — Orbus Software — Tool Certification Supporting Evidence*，§2.11 — https://certification.opengroup.org/register/archimate/orbus_archimate3_tool_se2.pdf — 访问于 2026-10-14；已提取 PDF 文本。
8. The Open Group，*TOGAF Standard — Establishing an Architecture Capability*，§2.1 — https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap02.html — 访问于 2026-10-14；BDAT 架构域官方说明的搜索索引摘录。
9. The Open Group，*ArchiMate Licensed Downloads* — https://www.opengroup.org/archimate-licensed-downloads — 访问于 2026-10-14；提取的官方文本确认第 4 版已于 2026 年 4 月发布。
10. Bizzdesign，*ArchiMate Relationships Point in the Same Direction as the Enterprise* — https://bizzdesign.com/blog/archimate-relationships-point-same-direction-enterprise — 访问于 2026-10-14；已提取关系方向的解释。

**访问限制：** 再次核查时，仍无法直接提取 3.2 的视点章节。本页定义综合了官方文本的搜索索引摘录与可访问的 3.2 参考卡。尚未独立审核附录 B 的完整关系表及图形符号；具体的正式模型应按完整的 3.2 规则验证。

## 示例 {#sample}
<!-- skill: path only -->
![I2 示例：下单的 ArchiMate 风格分层视图（非正式近似）](/samples/I2-archimate-layered-view.svg)
*下单的 ArchiMate 分层视图（非正式近似）：购物者被分配到业务层的“下单”流程；应用服务“订单处理”为它提供服务，并由“订单服务”组件实现，该组件访问“订单数据”；技术层的容器平台为该组件提供服务。连线标注关系类型；没有 ArchiMate 图元，也没有元模型校验。*
