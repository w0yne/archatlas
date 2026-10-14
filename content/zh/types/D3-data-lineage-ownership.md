---
code: D3
slug: data-lineage-ownership
family: D
names:
  en: Data lineage and ownership map
  zh: 数据血缘与归属图
  aliases:
    en: [data lineage diagram, lineage graph, data ownership map, data asset map, data lineage graph, lineage DAG, data provenance graph, data domain map, data stewardship map]
    zh: [数据血缘图, 数据归属图, 数据资产地图, 血缘关系图, 数据溯源图, 数据责任图, 数据分布图]
question: 这个数据集或这个答案从哪里来？它一旦变更，下游会有什么受影响？谁对它负责？
audiences: [architects, security, business]
levels: [logical]
phases: [design, operate]
scope: 一个锚点（一个数据集、报表或答案），向上游或下游追溯有限范围，约 20 个节点，粒度为数据集；归属以叠加层形式呈现
formal: {kind: convention, ref: 'No graphical standard. Runtime lineage metadata is standardised by OpenLineage (Job, Run, Dataset, facets); ownership roles follow data-governance practice (owner, steward)'}
neighbours: [D1, D2, H1]
status: draft
translationOf: en/types/D3-data-lineage-ownership.md
sourceRev: a5d2191
reviewed: false
---

# 数据血缘与数据归属图（Data Lineage and Ownership Map）

> 一张从左到右的图，展示数据集如何经由作业（job）相互派生，并为每个数据集或数据域标注数据所有者与数据管理员。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **要回答的问题：** *血缘*回答一个数据集、报表或答案从哪里来、经过了哪些转换、一旦变更下游有什么会受影响。*归属*回答谁对它的定义、质量和访问负责。
- **视点：** 治理与可信视图，关注溯源、影响与问责。DFD（D2）是描述数据*应当*如何流动的设计模型；血缘则是数据*实际*如何流动的证据，粒度可以是数据集、作业或字段，有时细到每次运行 [2]。
- **标准：** 没有图形标准。元数据由 OpenLineage（LF AI & Data）标准化：一个 **Job** 消费并产出 **Dataset**，一个 **Run** 是作业的一次执行，带有客户端生成的 UUID 运行 id，**facet** 可扩展这三者（schema、源代码位置、统计信息等）[1][2]。Marquez 是其参考实现 [3]。dbt 从模型引用推导出 DAG [4]；DataHub 采集血缘并允许用户编辑，包括字段级血缘 [5]。
- **本站采用的定义：** 两个变体共用一个编号。*血缘图*回答溯源与影响；*归属图*叠加数据所有者（Owner，承担问责）与数据管理员（Steward，负责日常运营）两种角色，依据数据治理实践 [6] 和数据网格（data mesh）的领域归属 [7]。角色定义取自 DAMA-DMBOK 的二手综述，未对照 DMBOK 原文核实。
- **不包含：** 处理逻辑（E2）、数据结构（D1）、运行时基础设施（G1）、访问策略（F3）。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 数据治理人员、数据所有者与数据管理员、隐私与合规官、数据工程师、分析使用者、架构师。
- **典型场景：**
  1. 影响分析：“如果修改 `customer.email` 的类型，哪些看板和模型会出问题？”[4][5]。
  2. 答案可信度：展示客服聊天机器人的某个答案用到了哪些源文档、抽取作业和搜索索引，以及每个来源归谁所有。
  3. 审计与监管证据：个人数据从哪里产生、被复制到哪里、由谁负责 [10][11]。
  4. 数据网格与领域设计：哪个领域拥有哪些数据产品，谁依赖它们 [7]。
  5. 故障排查：某个上游作业失败后，哪些下游数据集已经过期（运行级血缘）[2][3]。
- **不适用的情况：** 新系统的逻辑设计（用 D2）；为大规模数据资产手工绘制表级或字段级血缘（应先自动生成，再做摘要）；没有人会维护时，因为过时的图比没有图更糟。
- **与相邻图型的区别：**
  - 要表达数据按设计应如何流动，选 **D2 数据流图**；要表达观测到的或推导出的溯源，选 D3。
  - 如果只关心归属，选 **H1 RACI 矩阵**；当所有者必须标注在数据流上时，D3 才是合适的位置。
  - 要表达谁可以读写，选 **F3 访问控制模型**；归属是问责，不是权限。
  - 要表达作业顺序和触发关系，选 **E2 活动图/流程图**或编排器的 DAG。
  - 需要表达实体本身的结构时，选 **D1 实体关系图**；D3 表达数据集的来源与归属。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 非正式约定。最站得住的默认做法是采用 OpenLineage 语义、从左到右的 DAG [1][2]。
- **必需元素：**
  - **数据集**（源、中间、输出）：矩形，标注业务名称加技术定位符，例如“Customer master (crm.customers)”。
  - **作业：** 使用有区分度的形状（圆角矩形或箭头形），以“动词+对象”命名。
  - **有向边**：数据集到作业再到数据集；作业消费输入、产出输出。
  - **使用方**位于右侧边缘：报表、应用、模型、人员。
- **归属叠加层（归属变体）：** 在每个数据集或数据域下标注数据所有者与数据管理员；可选为每个所属领域使用一条色带或一种颜色；附角色图例。
- **可选元素：** 粒度标记（数据集或字段）；新鲜度或运行状态；分级标签（个人、机密）；派生数据（如嵌入向量和索引）的标记；应用到数据连线上的 CRUD 字母，参照 TOGAF 应用/数据矩阵 [8]。
- **箭头语义：** “派生自 / 供给”，绝不是“调用”或“触发”。
- **相关 TOGAF 制品：** 数据分发图（Data Dissemination）、数据生命周期图（Data Lifecycle）、数据安全图（Data Security），以及应用/数据矩阵 [8][9]（TOGAF 10 中的命名未对照原文核实）。
- **规模与命名：** 每张图约 20 个节点；只对一个关键字段展示字段级血缘。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **先生成，再整理。** 从流水线和数据目录（OpenLineage、dbt、采集工具）中获取血缘，再为人绘制易读的摘要。
2. **把所有者挂到节点上，** 按数据集或数据域，使用组织自身的治理角色。
3. **纳入派生存储和二级存储：** 缓存、搜索与向量索引、数据抽取。溯源通常就是在这些地方断掉的。
4. **在可信度要紧时标出版本或运行：** 哪个版本的源供给了哪个输出。
5. **按问题划定范围：** 一个使用方的上游或一个源的下游，绝不画整个数据资产。标记敏感数据，便于隐私评审复用这张图 [10]。

### 反模式
1. **只有技术血缘，没有所有者；** 没人能据此采取行动。
2. **手工绘制覆盖全部资产的血缘，** 几周内就过时。
3. **把边画成控制或调用；** 那是编排，不是溯源。
4. **隐藏派生数据：** 索引或嵌入向量没有追溯到源文档。
5. **把归属和访问权限混在一起，** 或者把只*展示*数据的应用画得像数据所有者。在一个应用中展示、但由另一个应用维护的数据，归维护方所有。

## 范例 {#exemplars}
<!-- skill: omit -->
- [OpenLineage object model](https://openlineage.io/docs/spec/object-model) — 关于血缘最清晰的词汇体系（Job、Run、Dataset、facet），并说明为什么逐次运行的证据很重要。开放标准。
- [Marquez](http://marquezproject.ai/) — 参考实现，其血缘界面展示作业与数据集的依赖关系及运行元数据。
- [dbt: getting started with data lineage](https://www.getdbt.com/blog/getting-started-with-data-lineage) — 从模型引用推导出的 DAG；“自动生成、始终最新”的典型案例。厂商内容。
- [DataHub lineage docs](https://docs.datahub.com/docs/features/feature-guides/lineage) — 数据集级与字段级血缘，支持手工编辑；给出自动血缘与人工整理血缘如何结合的指导。
- [Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html) — 按领域归属、数据即产品；归属叠加层的依据。
- [ICO guidance on documenting processing activities](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/documentation/how-do-we-document-our-processing-activities/) — 监管机构期望如何记录数据流和责任；采用表格形式，但可直接映射到这种图。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定问题和方向：上游追溯（“X 从哪里来？”）、下游影响（“什么依赖 X？”）或归属总览（“谁拥有什么？”）；写进标题。
2. 选择粒度：默认数据集级，只对一个关键字段做字段级。
3. 收集节点：源、作业、中间数据、输出、使用方，以及派生存储（索引、缓存、嵌入向量）。
4. 布局：从左到右的 DAG；归属变体增加横向色带，每个所属领域一条。作业形状要与数据集形状明显不同。
5. 叠加归属：在每个数据集下或每条领域色带上标注数据所有者与数据管理员，并附角色图例。
6. 文字：数据集写业务名称加定位符，作业写“动词+对象”；分级用小标签表示。
7. 颜色：每个所属领域一种颜色，或用一种强调色标示敏感数据；没有图例时不要两者同时使用。
8. 在页脚标注证据：由工具 X 于日期 Y 生成、从代码推断，或经所有者确认。

**自检清单**
- [ ] 标题中写明了问题（上游、下游或归属）。
- [ ] 边表示“派生自 / 供给”，而不是“调用 / 触发”。
- [ ] 每个数据集都有所有者，或标注为“所有者未知”。
- [ ] 派生存储（索引、缓存、嵌入向量）已追溯到其来源。
- [ ] 粒度一致（数据集级或字段级，不混用）。
- [ ] 标明了血缘的来源和日期（自动生成或推断）。
- [ ] 最多约 20 个节点；否则按领域或使用方拆分。
- [ ] 敏感数据标签和颜色在图例中有说明。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **流水线：** dbt 模型和 `ref()` 调用、工作流或编排器 DAG、ETL 脚本、SQL `INSERT ... SELECT` 和 `CREATE TABLE AS`。
- **生产者与消费者：** 采集作业、事件发布者与订阅者。
- **元数据：** OpenLineage 发送端配置、数据目录配置、数据契约文件。
- **派生存储：** 构建索引（搜索或向量）的作业及其源路径。
- **归属线索：** `CODEOWNERS`、数据目录元数据、数据契约中的所有者。
- **必须来自人或数据目录：** 承担问责的业务所有者、数据分级与法律依据，以及仓库之外的使用方。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 这张图必须回答什么：某样东西从哪里来、变更后什么会出问题，还是谁负责？（变更后什么会出问题）
2. 以哪个数据集、报表或答案为锚点，向上游或下游追溯多远？（一张报表，向上游两跳）
3. 数据集级还是字段级？（数据集级）
4. 是否标注数据所有者与数据管理员，权威名单在哪里？（是，来自数据目录或数据契约）
5. 是否突出个人数据或索引等派生存储？（派生存储要突出，个人数据用标签表示）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/D3.json` · 布局模板：`layered` · 数据集是 `store` 节点，作业是 `component` 节点（所有者和管理员放在 `sub`，分级放在 `tags`），所属领域是 `lane` 或 `layer` 分组，“供给”关系是从生产者指向使用方的 `data` 边 `->`，证据来源和日期写入 `meta.description`。

## 参考来源 {#sources}
<!-- skill: omit -->
1. OpenLineage, Object Model（Job、带 UUID 运行 id 的 Run、Dataset、facet；已复核）— https://openlineage.io/docs/spec/object-model — 访问于 2026-10-14
2. OpenLineage, specification (GitHub) — https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.md — 访问于 2026-10-14
3. Marquez Project — http://marquezproject.ai/ — 访问于 2026-10-14
4. dbt Labs, "Getting started with data lineage" — https://www.getdbt.com/blog/getting-started-with-data-lineage — 访问于 2026-10-14
5. DataHub, "About DataHub Lineage" — https://docs.datahub.com/docs/features/feature-guides/lineage — 访问于 2026-10-14
6. OvalEdge, "The DAMA-DMBOK Data Governance Framework"（关于数据所有者与数据管理员的二手综述）— https://www.ovaledge.com/blog/dama-dmbok-data-governance-framework — 访问于 2026-10-14
7. Z. Dehghani, "Data Mesh Principles and Logical Architecture", martinfowler.com — https://martinfowler.com/articles/data-mesh-principles.html — 访问于 2026-10-14
8. The Open Group, TOGAF V9 sample catalogs, matrices and diagrams — http://www.togaf.info/togaf9/togafSlides9/TOGAF-V9-Sample-Catalogs-Matrics-Diagrams-v2.pdf — 访问于 2026-10-14
9. QualiWare CoE, "TOGAF Artifacts"（数据生命周期图；该制品清单也见于第三方 TOGAF 学习指南）— https://coe.qualiware.com/resources/togaf/togaf-artifacts/ — 访问于 2026-10-14
10. ICO, "How do we document our processing activities?" — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/documentation/how-do-we-document-our-processing-activities/ — 访问于 2026-10-14
11. Data Protection Commission (Ireland), "Records of Processing (Article 30) Guidance" — https://www.dataprotection.ie/en/dpc-guidance/records-of-processing-article-30-guidance — 访问于 2026-10-14

## 示例图 {#sample}
<!-- skill: path only -->
![D3 示例：网店血缘，从订单表和支付表经夜间销售作业流向营收看板和客服聊天机器人搜索索引，每个数据集下标注所有者和管理员](/samples/D3-data-lineage-ownership.svg)
*示例图待生成（由渲染器根据 `examples/` 生成）。*
