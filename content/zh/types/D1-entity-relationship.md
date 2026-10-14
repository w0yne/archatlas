---
code: D1
slug: entity-relationship
family: D
names:
  en: Entity-relationship diagram
  zh: 实体关系图
  aliases:
    en: [ER diagram, ERD, data model diagram, conceptual data model, logical data model, information model, domain model (UML class style), crow's foot diagram]
    zh: [ER 图, 数据模型图, 概念数据模型, 逻辑数据模型, E-R 图, 信息模型, 领域模型]
question: 系统保存哪些业务事物的信息？它们之间如何关联？每个关系两端各允许多少个实例（基数）？
audiences: [architects, developers, business]
levels: [concept, logical]
phases: [design, build]
scope: 一个主题域或限界上下文，约 5-15 个实体，按一个明确声明的层级（概念或逻辑）绘制
formal: {kind: method, ref: 'Chen 1976; crow''s foot (Everest 1976), Barker, IDEF1X (FIPS PUB 184, 1993) and UML 2.5.1 class diagrams are separate defined notations; the conceptual/logical/physical levels are a modelling convention'}
neighbours: [D2, D3, E3, F3]
status: draft
translationOf: en/types/D1-entity-relationship.md
sourceRev: 674f366
reviewed: false
---

# 实体关系图（Entity-Relationship Diagram）

> 一张描绘系统所保存数据的事物及其相互关系的图，按一个明确的详略层级、用一种表示法绘制。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 系统保存哪些业务事物的信息，它们如何关联（以及各有多少）？这是"领域中什么为真"的视图，与流程和时间无关。
- **视点：** 信息视点。ArchiMate 中的对应物是 Information Structure 示例视点 [12]。TOGAF 把 Conceptual Data diagram 和 Logical Data diagram 列为两个独立的 Phase C 制品 [10][11]。C4 model 没有数据层级；C4 网站建议用 ER 图或类图作为补充。
- **起源：** Peter Chen，"The Entity-Relationship Model"，ACM TODS 1(1)，1976 [1][2]。鸦脚表示法（crow's foot notation）可追溯到 Gordon Everest 1976 年的"inverted arrow" [3]；Barker 表示法约于 1981 年出自 CACI，并经 Oracle 推广 [5]；IDEF1X 是 1993 年的美国联邦标准 FIPS PUB 184 [4]；UML 类图由 UML 2.5.1 定义 [7]。没有哪一种是"唯一的" ER 标准。
- **本站采用的定义：** *概念*层 = 实体、关系、基数（cardinality），没有键和类型；*逻辑*层 = 增加标识符、关键属性，并解析 N:M 关系，仍与平台无关；*物理*层 = 表、列、类型、索引 [8][9]。物理层属于数据库设计：应从 schema 生成，而不是手绘。
- **不包含：** 行为（E2、E3）、数据移动（D2）、血缘与归属（D3）、存储运行在哪里（G1）、访问规则（F3）。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 架构师、开发人员、分析师和治理负责人；产品负责人和业务专家仅限概念层。
- **典型场景：**
  1. 在开发之前与业务方约定网店的词汇（客户、订单、支付、发货）。
  2. 划定新服务的持久化边界和聚合。
  3. 向新团队或集成方讲解现有 schema（逆向得到的逻辑视图）。
  4. 数据迁移或整合：映射两个系统的实体。
  5. 租户或权限设计：把租户、所有者和共享关系明确画出来。
- **不适用的情况：** 谁在什么时候做什么（E1、E2、A5）；把大型数据库的所有表全部倒出来（用 SchemaSpy 或 tbls 生成 [13][14]）；数据如何在系统之间移动（D2、C6）。
- **与相邻类型的区别：**
  - 数据在*移动*时，选 **D2 数据流图**；D1 表达数据的*结构*。
  - 表达单个实体的生命周期时，选 **E3 状态机图**。常见搭配：D1，再为每个带状态字段的实体配一张 E3。
  - 要表达上下文之间如何关联时，选 **C7 限界上下文映射图**；每个上下文画一张 D1，而不是画一张企业级 ER 图。
  - 表达权限时，选 **F3 访问控制模型**；用户-角色-权限-资源这条链本身就是一张小 ER 图。
  - 问题是数据从哪里来、派生出什么、归谁负责，而不是实体之间如何关联时，选 **D3 数据血缘与归属图**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 每种表示法都有定义，但层级划分是约定 [8][9]。选定一种表示法，在图例中写明，绝不把 Chen 菱形与鸦脚混用。
- **必需：**
  - **实体：** 单数业务名词（`Customer`、`Order`），大小写保持一致。
  - **关系：** 连线用可单向读通的动词短语标注（"Customer *places* Order"）。
  - **两端都标基数，** 包括最小值和最大值。在鸦脚表示法中，外侧符号是最大值，内侧是最小值；Mermaid 的 `erDiagram` 文档规定 `|o` 为零或一，`||` 为恰好一，`}o` 为零或多，`}|` 为一或多 [6]。
- **可选（逻辑层）：** 主键和少量定义性属性；标识性（实线）与非标识性（虚线）关系 [6]；用于 N:M 的关联实体；子类型和超类型。外键是关系型数据库的手段，只属于逻辑层或物理层。
- **UML 变体：** 带多重性（`0..1`、`1`、`*`、`1..*`）的类，组合、聚合、泛化 [7]。
- **图例：** 表示法（"鸦脚；内侧为最小值，外侧为最大值"）和层级（"概念"或"逻辑"）。
- **规模：** 概念层每个视图约 5-15 个实体（经验法则，不是标准）；逻辑层只展示能解释含义的属性（"often a small subset of attributes is enough" [6]）。
- **命名：** 使用用户的语言，而不是表前缀（`tbl_cust`）；连线上写动词，在有更准确动词时不用笼统的"has"。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **在标题中写明层级**（"概念模型：订单管理"），并按该层级绘制 [8][9]。
2. **每张图一个主题域。** 按限界上下文或业务职能切分；共享实体用引用，而不是重复绘制。
3. **与领域专家一起建模**，并把每个关系大声读出来（"每个 Order 恰好由一个 Customer 下达"）。
4. **标出可选性**（最小值 0 还是 1）；它承载着否则会藏在代码里的业务规则。
5. **只在逻辑层解析 N:M，** 并以真实事物命名关联实体（`OrderLine`，而不是 `OrderProduct`）。横切模式（租户键、软删除、审计）只注明一次，不要在每个实体上重复。

### 反模式
1. **数据库倒出：** 100 多张表连同所有列；面面俱到是可理解性的敌人 [15]。
2. **层级混杂：** 在面向业务的概念模型上出现外键、类型和索引。
3. **连线没有标签，或某一端缺少基数。**
4. **技术化或无意义的名称：** `data`、`info`、`item2`、表前缀。
5. **把流程编码成实体**（`ApprovalStep1`、`ApprovalStep2`），或混用表示法却没有图例。同样要避免在真正的图更能展示关系链的地方用文字列出实体清单。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Chen's original paper (1976, author PDF)](https://www.csc.lsu.edu/~chen/pdf/erd-5-pages.pdf) — 奠基性文献；说明了为什么基本元素是实体和关系，而不是记录。
- [Mermaid entity relationship diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) — 简明的鸦脚表示法参考，附基数表；是图即代码的良好范本。
- [Chinook sample database](https://github.com/lerocha/chinook-database) — 一个小而真实的 schema（艺术家、专辑、曲目、发票），适合学习阅读 ERD；MIT 许可（LICENSE 文件已于 2026-10-14 核查）。
- [IDEF1X, FIPS PUB 184](https://www.idef.com/wp-content/uploads/2016/02/Idef1x.pdf) — 一份严谨的逻辑模型标准，展示了"逻辑"可以意味着什么；美国政府出版物。
- [Barker's notation (Wikipedia)](https://en.wikipedia.org/wiki/Barker's_notation) — 子类型方框嵌在超类型内、可选/必选用半实半虚线表示，是鸦脚之外的另一种选择。
- [SchemaSpy](https://github.com/schemaspy/schemaspy) 和 [tbls](https://github.com/k1LoW/tbls) — 自动生成的物理 ER 图和表文档；说明物理层应该放在哪里。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定层级和范围。面向业务受众默认用概念层，面向工程师用逻辑层；选定一个主题域或限界上下文。
2. 从需求中的名词或 schema、ORM 模型中收集候选实体；合并同义词；去掉技术性表（迁移、锁、缓存），除非它们就是主题。
3. 上限约 12 个实体；其余的移到另一个视图，或用"见图 X"占位。
4. 先写关系语句（"每个 Order 恰好由一个 Customer 下达"），再画图。
5. 布局：连接最多的实体居中；父实体在上、子实体在下，使一对多关系向下展开；关联实体放在其两个父实体之间；使用正交连线，通过调整顺序消除交叉。
6. 文字：实体名加 3-5 个定义性属性（逻辑层），或不加属性（概念层）；每条连线都有动词。
7. 颜色：最多 2-3 种有含义的填充色（例如核心数据、参考数据、外部拥有的数据），每种都写进图例；不用装饰性颜色。
8. 加图例说明表示法和层级，并为每个横切模式加一条注释。

**自检清单**
- [ ] 标题写明了层级和范围。
- [ ] 每条连线都有动词标签，两端都有基数。
- [ ] 概念图上没有外键、类型或索引细节。
- [ ] N:M 关系一致地要么保留（概念层），要么解析为具名关联实体（逻辑层）。
- [ ] 名称是业务术语；同一事物在每张图上名称相同。
- [ ] 最多约 15 个实体，否则拆图。
- [ ] 只用一种表示法，并配图例。
- [ ] 关系语句大声读出来是正确的，并经专家或代码证据确认。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **强证据：** DDL 加最新的迁移（以当前 schema 为准，而不是最初的 DDL）；ORM 或实体类及其关系声明；GraphQL 和 OpenAPI 资源 schema；外键和唯一约束（基数的证据）。
- **弱证据，标为推断：** 没有外键的 `xxx_id` 列、JSON 大字段、文档型存储。
- **必须来自人：** 技术性表的业务名称、业务方期望的可选性、哪些实体对受众重要。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 读者是谁：业务干系人（概念层）还是工程师（逻辑层）？是否要显示属性或键？（工程师，逻辑层，仅关键属性）
2. 哪个主题域或限界上下文？相邻领域是用占位表示还是省略？（一个上下文，相邻领域用占位）
3. 是否有可遵循的事实来源（schema、ORM、术语表），还是我们在设计目标模型？（遵循现有 schema，标为推断）
4. 你们组织使用哪种表示法？（鸦脚表示法）
5. 租户、所有权、审计或版本控制是标在实体上，还是只注明一次？（只注明一次）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/D1.json` · 布局模板：`er` · 实体成为 kind 为 `entity` 的 `nodes`（属性字符串放在 `attributes` 中，`PK`/`FK` 等键标记在前），限界上下文或主题域成为 `boundary` 分组，关系成为 `dir` 为 `--` 的边，其 `cardinality{from,to}` 携带最小值/最大值，`label` 为动词；层级写在标题中。

## 来源 {#sources}
<!-- skill: omit -->
1. P. P.-S. Chen, "The entity-relationship model — toward a unified view of data", ACM TODS 1(1):9–36, 1976 — https://dl.acm.org/doi/10.1145/320434.320440 — 访问于 2026-10-14
2. Chen 1976, author PDF — https://www.csc.lsu.edu/~chen/pdf/erd-5-pages.pdf — 访问于 2026-10-14
3. Redgate, "Crow's Foot Notation" (history: Everest 1976, secondary source) — https://www.red-gate.com/blog/crow-s-foot-notation/ — 访问于 2026-10-14
4. NIST FIPS PUB 184, Integration Definition for Information Modeling (IDEF1X), 21 December 1993 (date from the publication record; the PDF text was not machine-readable in this check) — https://www.idef.com/wp-content/uploads/2016/02/Idef1x.pdf — 访问于 2026-10-14
5. Wikipedia, "Barker's notation" (secondary source) — https://en.wikipedia.org/wiki/Barker's_notation — 访问于 2026-10-14
6. Mermaid, "Entity Relationship Diagrams" (cardinality table, identifying lines, attribute quote re-checked) — https://mermaid.js.org/syntax/entityRelationshipDiagram.html — 访问于 2026-10-14
7. OMG, Unified Modeling Language 2.5.1 — https://www.omg.org/spec/UML/2.5.1/About-UML — 访问于 2026-10-14
8. AWS, "Logical vs Physical Data Model" — https://aws.amazon.com/compare/the-difference-between-logical-and-physical-data-model/ — 访问于 2026-10-14
9. ThoughtSpot, "Conceptual vs Logical vs Physical Data Models" — https://www.thoughtspot.com/data-trends/data-modeling/conceptual-vs-logical-vs-physical-data-models — 访问于 2026-10-14
10. The Open Group, TOGAF V9 sample catalogs, matrices and diagrams (Phase C data; TOGAF 10 naming not verified against the primary text) — http://www.togaf.info/togaf9/togafSlides9/TOGAF-V9-Sample-Catalogs-Matrics-Diagrams-v2.pdf — 访问于 2026-10-14
11. QualiWare CoE, "TOGAF Artifacts" — https://coe.qualiware.com/resources/togaf/togaf-artifacts/ — 访问于 2026-10-14
12. The Open Group, ArchiMate 3.2 Specification, Example Viewpoints — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html — 访问于 2026-10-14
13. SchemaSpy — https://github.com/schemaspy/schemaspy — 访问于 2026-10-14
14. tbls — https://github.com/k1LoW/tbls — 访问于 2026-10-14
15. M. Fowler, "UmlAsSketch" — https://martinfowler.com/bliki/UmlAsSketch.html — 访问于 2026-10-14
16. Chinook database (MIT licence file checked) — https://github.com/lerocha/chinook-database — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![D1 示例：网店逻辑模型，包含 Customer、Order、OrderLine、Product、Payment 和 Shipment，采用鸦脚表示法](/samples/D1-entity-relationship.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
