---
code: C2
slug: system-context
family: C
names:
  en: System context diagram (C4 model level 1)
  zh: 系统上下文图（C4 模型第 1 层）
  aliases:
    en: [system context diagram, system environment diagram, context-level DFD, C4 model Level 1, Structured-analysis Context Diagram]
    zh: [系统上下文图, 系统环境图, 上下文级数据流图, C4 模型第 1 层]
question: 这是什么系统？谁在使用它？它依赖哪些其他系统，或与哪些系统交换信息？
audiences: [leaders, business, architects, developers, security]
levels: [concept]
phases: [initiate, requirements, design]
scope: 把一个软件系统视为黑盒，连同与它直接相连的人员和外部系统。
formal: {kind: method, ref: 'C4 model (Simon Brown), Level 1 System Context diagram; notation-independent, no versioned standard'}
neighbours: [A3, A7, B4, C1, C3, C6, D2]
status: draft
translationOf: en/types/C2-system-context.md
sourceRev: 7002b1114ff60c6a028194c8376c71eee2b9d52d
reviewed: false
---

# 系统上下文图（System Context Diagram）

> 一个系统作为一个方框居中，四周是它的用户以及与它交互的系统。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
它回答：*这是什么系统？谁在使用它？它依赖哪些其他系统，或与哪些系统交换信息？* 其关注点是范围与边界：就系统止于何处达成一致，并且技术人员和非技术人员都能读懂 [1]。它是 C4 model 的第 1 层。C4 model 由 Simon Brown 提出，是一种与表示法无关的方法，而非有版本的标准 [2][6][7]；同一思想也见于结构化分析中的上下文图（上下文级 DFD；“0 层”这一叫法有人指它，也有人指它下面的一层）[10]、系统工程中的关注系统（system of interest）上下文 [11]，以及 arc42 第 3 节“上下文与范围”（Context and Scope）[8]。ISO/IEC/IEEE 42010 不规定表示法；本图是上下文视点下的一个视图 [19]。它有意略去方框内部的一切、技术选型、协议和部署，以及所有不直接相连的系统 [1][13]。
**本站采用的定义：** *软件系统*（software system）是一个团队构建、拥有并能看到其内部的东西；该团队拥有的数据库或队列属于方框内部，而不是邻居 [4]。产品领域、限界上下文（bounded context）和能力通常不是软件系统 [4]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 所有人；C4 model 建议所有团队都绘制此图 [1]。
- **适用场景：** 任何架构文档或 README 的第一张图；项目启动时对齐范围；新成员入职；安全工作的起点（在威胁建模前找出所有入站和出站方）；变更影响分析（一次发布会影响哪些邻居）。
- **不适用场景：** 内部结构（C3/C4/C5）、运行时流程（E1）、数据存储与模式（D1/D2）、托管部署（G1），或几十个对等系统而没有单一焦点（C1）。C4 model 指出，对于高度定制的套装产品，此图的价值较小，但第 1 层和第 2 层仍可能有所帮助 [6]。
- **与相邻类型的区别：**
  - 当企业或部门范围内的许多系统都很重要时，选 **C1**；C4 model 的系统全景图（System Landscape diagram）是两者之间的桥梁，即“没有特定焦点的系统上下文图” [5]。
  - 一旦需要展示方框内部的应用、数据存储或技术，就选 **C3**。
  - 在协商范围内外时，选 **B4**（单独的范围图，划出范围内与范围外区域）。
  - 当问题是数据流与数据存储时，选 **D2**：DFD 的连线标注数据，C2 的连线标注意图。
  - 需要按接口说明协议、同步/异步、认证和 SLA 时（arc42 的“技术上下文”），选 **C6**。
  - 关注组织、角色和干系人利益而非系统时，选 **A3**。
  - 领导需要用业务语言了解方案的主要组成，而不是系统的用户和外部系统时，选 **A7**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需项 [2][3]：** 标明类型和范围的标题（“`<系统名>`：系统上下文图”）；**恰好一个**在范围内的系统，标注类型并附一句话描述；**人员**以角色表示，而非具名个人；直接相连的**外部系统**，标注类型并附描述；**关系**各自只有一个方向，并带有与方向一致的意图标签（动词短语）；说明形状、颜色、边框、线型和箭头的**图例**；解释所有缩写。
- **第 1 层的连线上不写协议或技术。** 上下文图关注的是人员和系统，而不是技术或协议 [1]。协议写在 C3 的连线上，或放在单独的技术上下文表（arc42 [8]）或接口表（C6）中。
- **标签：** “向……下订单”“向……发送支付请求”“向……报告库存水平”；避免只写“使用” [2]。力求不超过六个词（这是经验法则，不是硬性规则 [18]）。
- **箭头语义：** 要么是“发起方 → 依赖方”（C4 model、Azure 指南 [9]），要么是“数据从 → 流向”（arc42 业务上下文提示 [8]）。选定一种，在图例中写明，绝不混用。不使用未加说明的双向箭头；改画两条线或注明请求/响应 [9]。
- **可选项：** 按明确标准将许多相似邻居分组 [8]；把“本组织”画成一个普通分组框（Structurizr 已将旧的“企业边界”标为弃用，改用分组 [12]）；用图注说明交换的主要数据。
- **形状与颜色：** 方框和连线；范围内系统、外部系统、人员各用一种样式；使用通用形状而非厂商图标 [9]；灰度打印后仍须可读。
- **工具：** C4-PlantUML 支持第 1 层并可生成图例 [14]；Mermaid 的 C4 model 语法标为实验性 [15]。
- **规模：** 约 3–7 个邻居时可读性好；外部系统超过约 12 个时，应分组，或检查是否混用了层级（经验法则 [18]）。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. 让图能独立成立：有标题、标注类型的元素、带标签的连线和图例，无需额外叙述 [2]。
2. 让非技术人员也能读懂：用平实的动词、通用形状，不写技术名称 [1][9]。
3. 展示每一个真实的外部接口，包括手工、基于文件和批处理的接口 [8]。
4. 把许多相似邻居归入带标签的分组，而不是删掉它们 [8]。
5. 把业务上下文（始终需要）与技术上下文（仅当通道重要时，以表格或 C3/C6 视图呈现）分开 [8]。

### 反模式
1. 边界混乱：把内部数据库或队列画成外部系统，或把其他团队的系统画进方框内 [4]。
2. 混入第 2 层内容：容器、数据库、端口、负载均衡器、技术名称 [17][18]。
3. 在连线上写协议（“REST”“HTTPS”“Kafka”）；这些应放在 C3 或接口表中 [1]。
4. 标签含糊或缺失（“使用”）、没有方向、没有图例 [2][3]。
5. 用具名个人代替角色，画出不直接相连的间接系统，或把设想中的集成画成已上线 [17]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [C4 model: System context diagram](https://c4model.com/diagrams/system-context) — 权威的、刻意保持简洁的示意图，附图例（CC BY 4.0）。
- [Structurizr examples: Big Bank plc](https://github.com/structurizr/examples) — 同一模型渲染为全景、上下文、容器和部署视图（许可：请查看仓库）。
- [arc42 section 3: Context and Scope](https://docs.arc42.org/section-3) — 业务上下文与技术上下文、合作方 / 输入 / 输出表格形式及实用提示（CC BY-SA 4.0）。
- [Azure Well-Architected: Create architecture design diagrams](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams) — 关于上下文图的厂商中立建议：黑盒、用户角色、明确边界、通用形状。
- [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML) — 用文本宏忠实绘制带图例的第 1 层（MIT）。Mermaid 的 C4 model 语法标为实验性，只宜作为草稿途径。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 用一句话写明系统名称，以及所属团队构建和拥有的内容（例如“网店（Online Shop）：浏览商品目录、加入购物车、结账”）。
2. 以角色列出人员（顾客（Shopper）、客服人员（Customer Support Agent）、商品目录管理员（Catalogue Manager））；将相似角色分组。
3. 列出直接相连的外部系统（支付服务商（Payment Provider）、仓储系统（Warehouse System）、带客服聊天机器人的客服系统（Customer Support System）、邮件服务（Email Service））；去掉所有不直接相连的系统；把相似系统归组。
4. 按所选的箭头约定为每条连线确定方向，并写一个不超过六个词的意图标签。不写协议。
5. 布局：系统方框居中且更大；人员在上方；上游来源在一侧，下游消费方在另一侧；共享服务（身份、邮件）在下方。默认自上而下，宽幅幻灯片用自左向右。连线短而直；宁可移动方框，也不要绕线。
6. 样式：范围内系统用饱和色，外部系统用灰色，人员样式有区分；三种字号（标题 > 名称 > 描述）。
7. 文字预算：每个元素 = 名称 + 类型 + 不超过约 12 个词的描述；方框内不写项目符号列表，不写技术。
8. 加上标题、日期和图例（形状、颜色、箭头含义）；然后给出下一步建议：深入到 C3、补充技术上下文表（C6），或扩展到 C1。

**自检清单**
- [ ] 恰好一个在范围内的系统；看不到它的任何内部。
- [ ] 每个邻居都直接相连，且类型标为人员或外部系统。
- [ ] 每条连线只有一个方向，并有具体的意图标签；没有光秃秃的“使用”。
- [ ] 图上任何地方都没有协议、端口、数据库、队列或产品技术栈。
- [ ] 人员是角色；相似的邻居已归组，而非删掉。
- [ ] 有标题（类型 + 范围）和图例；写明箭头约定；解释了缩写。
- [ ] 归属检查：方框内没有暗中属于外部的东西，反之亦然。
- [ ] 非技术读者能用一句话讲清这张图；邻居约 12 个或更少。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- README、文档、服务目录条目（系统、负责人、消费和提供的 API、`dependsOn`）[16]。
- 第三方端点的配置和环境变量（身份签发方、邮件主机、支付 API 基础 URL）；包清单中的 SDK。
- API 规范：OpenAPI 的 servers、安全方案和回调；与其他团队共享的 AsyncAPI 通道。
- 出站调用点、生产和消费的主题、定时导入和导出；入口（谁调用进来）和出口规则。
- 角色和权限定义、UI 路由分组和运维手册可提供候选的人员角色。
- 代码中没有的：业务用户是谁、什么算“外部”、归属关系。每个从代码推断出的邻居都要找人确认。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 系统叫什么？用一句话说它做什么？你的团队究竟拥有什么？（你们仓库中的可部署部分）
2. 谁会读这张图？（业务和技术读者都有，所以图上不写技术）
3. 哪些用户和运维角色与它交互？有没有非人类的调用方？（最终用户加一个支持或管理员角色）
4. 哪些外部系统调用它、被它调用或与它交换文件？各自归谁所有？（所有直接相连的系统，超过约 12 个时归组）
5. 箭头表示“谁调用谁”还是“哪些数据流动”？是现状还是目标态？（谁调用谁；现状，计划中的连线在图例中标注）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/C2.json` · 布局模板：`statechart` · 系统是 `boundary` 分组（含同一平台的其他系统）内样式为 `primary` 的 `system` 节点，左侧 `person` 节点、右侧 `external` 节点按连线自动分层；`sub` 简短说明，标签（chips）标注角色，`edges` 带意图标签且没有技术字段。

## 来源 {#sources}
<!-- skill: omit -->
1. C4 model — System context diagram — https://c4model.com/diagrams/system-context — 访问于 2026-10-14
2. C4 model — Notation — https://c4model.com/diagrams/notation — 访问于 2026-10-14
3. C4 model — Review checklist — https://c4model.com/diagrams/checklist — 访问于 2026-10-14
4. C4 model — Software system — https://c4model.com/abstractions/software-system — 访问于 2026-10-14
5. C4 model — System landscape diagram — https://c4model.com/diagrams/system-landscape — 访问于 2026-10-14
6. C4 model — FAQ — https://c4model.com/faq — 访问于 2026-10-14
7. C4 model — History — https://c4model.com/history — 访问于 2026-10-14
8. arc42 — Section 3, Context and scope — https://docs.arc42.org/section-3 — 访问于 2026-10-14
9. Microsoft Learn — Create architecture design diagrams (Azure Well-Architected) — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — 访问于 2026-10-14
10. E. Yourdon — Just Enough Structured Analysis, ch. 9 (online edition) — https://www.businessanalystlearnings.com/s/Yourdon-DFD.pdf — 访问于 2026-10-14
11. SEBoK — Introduction to Systems Engineering Fundamentals (system context) — https://sebokwiki.org/wiki/Introduction_to_Systems_Engineering_Fundamentals — 访问于 2026-10-14
12. Structurizr — Diagram notation — https://docs.structurizr.com/ui/diagrams/notation — 访问于 2026-10-14
13. Structurizr — DSL language reference — https://docs.structurizr.com/dsl/language — 访问于 2026-10-14
14. C4-PlantUML — https://github.com/plantuml-stdlib/C4-PlantUML — 访问于 2026-10-14
15. Mermaid — C4 diagrams — https://mermaid.js.org/syntax/c4 — 访问于 2026-10-14
16. Backstage — System model — https://backstage.io/docs/features/software-catalog/system-model — 访问于 2026-10-14
17. Working Software — Misuses and mistakes of the C4 model — https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model — 访问于 2026-10-14
18. Visual Paradigm — C4 context diagram guide — https://www.visual-paradigm.com/guide/c4-context-diagram-the-best-way-for-beginners-to-visualize-software-architecture — 访问于 2026-10-14
19. IEEE SA — ISO/IEC/IEEE 42010:2022 — https://standards.ieee.org/ieee/42010/6846 — 访问于 2026-10-14

### A3 · 业务上下文图 {#variant-a3}

编辑归组保留独立语义；使用本变体的画法与检查项。

1. 确认主体（一个系统、举措或业务单元）以及现状还是目标态。把标题写成一句结论（“The online shop and the seven parties it trades with”，网店及与其交易往来的七方）。
2. 列出外部参与方，合并重复项，每组只放一类（角色、组织、外部系统），总共 5–15 个。
3. 把交换列为 *参与方 → 主体：名词* 和 *主体 → 参与方：名词*。去掉任何属于协议的内容。
4. 版式：主体居中且在视觉上占主导；客户和渠道在左，合作伙伴和服务商在右，监管机构在上，内部但不在范围内的在下；箭头短而直，不交叉。
5. 文字量：参与方名称 ≤ 3 个词，流标签 ≤ 3 个词，画布上不写句子。
6. 颜色：主体用一种中性填充，参与方分组最多 3 种填充；用线型（而不是颜色）区分流的种类，并始终附图例。
7. 可选：给流编号，并在注释中附一张 *partner | input | output* 表。

**自检清单**

- [ ] 中心是黑盒；里面什么都没画。
- [ ] 每组中的外部参与方都是同一类事物。
- [ ] 每条箭头都有业务名词标签和明确的方向；没有协议名称。
- [ ] 已考虑监管机构、财务、物流和支持（纳入或有意排除）。
- [ ] 没有外部方到外部方的流。
- [ ] 标题写明范围和现状/目标态；没有重复说明图类型的副标题。
- [ ] 这里不编码干系人的权力或利益（那是 H3）。
- [ ] 图例说明了每种线型和填充。

[完整方法与历史样例](/zh/types/a3-business-context#meaning).

### B4 · 范围图 {#variant-b4}

编辑归组保留独立语义；使用本变体的画法与检查项。

1. 选择交付范围或一种明确命名的上下文变体，说明受众和基线。
2. 确定举措／主体，解释其边界含义。
3. 收集已约定的纳入项、排除项、依赖和未解决决策。
4. 将外部系统的所有权与范围内的集成工作分开。
5. 绘制带标签的范围区域；上下文配图则以主体为中心，对相关邻居分组。
6. 使用简短标签、克制的颜色和明确的连线含义；契约放在表格中。
7. 核对证据和配套视图；记录分歧，不编造共识。

**自检清单**
- [ ] 已命名变体、主体／举措和基线。
- [ ] 交付、系统、所有权与信任边界有明确区别。
- [ ] 纳入／排除项有决策证据，或标为未确定。
- [ ] 外部依赖没有被误认为范围外的集成工作。
- [ ] 箭头方向和标签符合所选约定。
- [ ] 上下文细节与 DFD 编号适当且明确。
- [ ] 相关交换、假设、标签和连线端点清晰可读。

[完整方法与历史样例](/zh/types/b4-scope-diagram#meaning).

## 示例图 {#sample}
<!-- skill: path only -->
![C2 · 企业服务助手](/samples/ai-service-assistant/C2/zh/diagram.svg)
*我们的软件系统是什么？谁在用？依赖哪些外部系统？*

[SVG](/samples/ai-service-assistant/C2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

[历史 shop 回归样例](/samples/C2-system-context.zh.svg) · [全部29幅视图](/zh/use/ai-service-assistant) · [示意假设](/zh/use/ai-service-assistant-assumptions).
