---
code: C8
slug: layered-architecture
family: C
names:
  en: Layered Architecture Diagram
  zh: 分层架构图
  aliases:
    en: [layer diagram, layered view, N-layer architecture, presentation-domain-data layering, hexagonal architecture (variant), ports and adapters (variant), onion architecture (variant), clean architecture (variant)]
    zh: [层次结构图, 技术分层图, 六边形架构, 端口与适配器, 洋葱架构, 整洁架构]
question: "一个应用的代码被划分为哪些职责层？哪些依赖方向是允许的，哪些是禁止的？"
audiences: [开发人员, 技术负责人, 代码评审人员, 架构师, 新成员]
level: logical
phases: [design, build, review]
scope: "一个应用、服务或限界上下文：它的代码层（或环）以及层与层之间的依赖规则。"
formal:
  kind: convention
  ref: "none for the picture; semantics: SEI layered style ('allowed-to-use', CMU/SEI-2000-SR-004), Evans' Layered Architecture pattern, Clean Architecture Dependency Rule"
neighbours: [C3, C4, C5, C7, G1, I2]
status: draft
translationOf: en/types/C8-layered-architecture.md
sourceRev: 674f366
reviewed: false
---

# 分层架构图（Layered Architecture Diagram）

> 一个应用代码的各层（或各环），以及规定哪一层可以依赖哪一层的规则。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->

分层架构图回答的是：*这个应用的代码如何划分为职责层，允许哪些依赖？* 它陈述的是一条**规则**，而不只是一种分组；没有明确的规则，它就退化成一摞彩色方框。SEI 把层之间的关系定义为 **“allowed-to-use”（允许使用）**。桥接（跳过某一层）或向上使用等例外必须画出来，而例外一多，往往说明系统结构不佳 [1]。按 ISO/IEC/IEEE 42010 的说法，它属于模块“使用”视点（module “uses” viewpoint），关注点（concern）是可修改性、可测试性和关注点分离 [14]。按 C4 model 的说法，它位于*单个容器内部*，大致处于组件层级 [12]。

**本站采用的定义。** “layer”一词有三种含义，只有第一种属于本类型。

| 术语 | 含义 | 归属 |
|---|---|---|
| **层**（Layer） | *代码职责*的逻辑划分；所有层可以运行在同一个进程中 [2][9] | **C8**（本类型） |
| **层级（物理分层）**（Tier） | 物理或虚拟的部署位置；各层级运行在不同机器上 [10] | G1 部署图 |
| **ArchiMate 分层视点**（Layered viewpoint） | 业务 / 应用 / 技术三层的企业级概览 [13] | I2 ArchiMate 分层视图 |

另有两种形似之物：“能力堆栈”（没有依赖规则的功能块条带）属于 C5 逻辑视图，OSI 式的协议栈则归入网络图。

**有意不包含：** 服务器、副本和网络（G1）；调用序列（E1）；数据模型（D1）；系统间集成（C6）；单个类。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->

- **受众：** 开发人员、技术负责人、评审人员、记录设计意图的架构师，以及新成员。
- **典型场景：** (1) 为新服务约定内部结构和依赖规则；(2) 入职培训和评审：这段代码应该放在哪里、可以导入什么？(3) 根据图生成架构一致性测试 [7][8]；(4) 重构混乱的代码库：把预期的层与实际的导入关系图并排画出；(5) 向实现者讲解某个框架的参考分层 [11]。
- **不适用的情况：** 服务器、副本、可用性或安全区（G1）；跨系统谁与谁通信（C2/C6）；没有依赖约束的模块清单（C5）；只有一两层的小服务；大型系统的顶层划分，这时应先按领域模块划分，再在每个模块内部分层 [2]。
- **与相邻类型的区别：**
  - 要表达与技术无关、没有强制依赖规则的职责块和接口时，选 **C5 逻辑架构**。
  - 要表达可运行单元或组件时，选 **C3/C4**。一个容器可能包含全部层。
  - 要表达模型*之间*的边界时，选 **C7 限界上下文映射图**。C8 位于单个上下文内部。
  - 要表达层级（物理分层）和机器时，选 **G1 部署图**。要表达 ArchiMate 的业务/应用/技术分层时，选 **I2**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->

- **没有图形标准。** 带依赖箭头的 UML 包可以表达这条规则。语义来自 SEI、Evans 和 Martin [1][3][6]。
- **必需：** 层画成条带（或环），每层有**名称和一行职责说明**。用一句话陈述**依赖规则**，并写明**变体**。只为*允许的*依赖画箭头。加图例：实线 = 源代码依赖，虚线 = 仅运行时装配（依赖注入）[9]。
- **变体选择**（只选一种）：
  - **严格（封闭）：** 一层只使用紧邻的下一层。箭头只连接相邻条带；代价是会出现透传层 [10]。
  - **宽松（开放）：** 一层可以使用任何更低的层，因此箭头可以跨越条带。代价是耦合更多 [10]。
  - **向内依赖（六边形 / 洋葱 / 整洁）：** 源代码依赖*指向核心*。适配器依赖核心所拥有的端口 [4][5][6]。核心画在中央，驱动方适配器在左，被驱动方适配器在右；六边形这个形状本身并无含义 [4]，整洁架构的四个环也只是一个示例 [6]。
  - *分段层*（同一条带内并列的对等部分，见 SEI [1]）可以与任一堆栈变体组合使用。
- **箭头方向提醒：** 在向内依赖变体中，箭头从“Persistence adapter”指向“Domain”，尽管运行时调用的方向相反。在图例中写明“箭头 = 源代码依赖”。
- **可选：** 一条表示横切关注点（日志、安全、配置）的竖条；每层 1–5 个真实模块名作为标签；最多三条禁止的捷径，用红色虚线箭头加“×”标出；外部系统放在框外。
- **详略程度：** 3–5 层，每层 2–5 个元素。超过约 6 层通常意味着存在透传层 [10]。
- **命名：** 按职责命名（“Domain”“Application”“Adapters”），不按框架命名。与仓库中的包名保持一致，以便规则可以被测试。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### 最佳实践

1. 把规则写在图旁边，再让它可执行，例如 ArchUnit `layeredArchitecture()` / `onionArchitecture()` 或 import-linter 的分层契约 [7][8]。
2. 让领域层不引用 UI、基础设施和框架。隔离领域正是分层的意义所在 [3][5]。
3. 跨边界传递简单数据，而不是框架的行对象或 ORM 实体；在控制流向外时使用依赖倒置 [6][9]。
4. 在较大的系统中，先按领域或组件拆分，再在*各部分内部*分层 [2]。
5. 把预期的层与实际的导入关系图并排画出，并列出主要违规 [1]。

### 反模式

1. **把层画成层级（物理分层）：** 在分层图里画服务器和副本，或把部署称为“三层分层” [2][10]。
2. **有箭头却没有明确规则，或规则人人都在违反：** 大量透传层，或严格分层迫使人写代理方法 [1][10]。
3. **反向依赖：** 数据层导入 UI 类型，或领域层依赖持久化注解 [6]。
4. **大型系统以按层分包作为顶层结构** [2]。
5. **把能力堆栈当作对代码有约束力的东西来呈现**，或把整洁架构的环当作必须照搬的四环模板 [6]。

## 范例 {#exemplars}
<!-- skill: omit -->

- [Fowler, PresentationDomainDataLayering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) — 极简的三层讲解，说明层不是层级（物理分层），并提醒不要用于顶层划分（许可未核查）。
- [Microsoft .NET, Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures) — 传统 N 层架构与整洁架构并列；实线表示编译时依赖，虚线表示运行时依赖（Microsoft Learn 条款）。
- [Android, Guide to app architecture](https://developer.android.com/topic/architecture) — UI 层 / 可选的领域层 / 数据层，箭头定义为类依赖（Android 内容许可；此处未核查）。
- [Cockburn, Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — 关于为何以及何时放弃堆栈隐喻的一手资料（许可未核查）。
- [R. C. Martin, The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) — 同心环与依赖规则（Dependency Rule）（许可未核查）。
- [ArchUnit user guide](https://www.archunit.org/userguide/html/000_Index.html) — 以代码表达分层和洋葱规则：图即测试（Apache-2.0 项目）。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->

1. 把范围限定为一个应用或服务（例如网店后端）。如果是整个系统群，先提供 C2/C3/C7。
2. 列出顶层包及其相互之间的导入关系图。根据*实际*名称提出分层建议；不要硬套模板。
3. 选择变体：如果基础设施实现的是领域所拥有的接口，用向内依赖；否则用堆栈，并在严格和宽松之间选择。
4. 每层：名称 + 5–10 个词的职责说明 + 2–5 个真实模块标签（总计不超过约 25 个标签）。
5. 堆栈布局：纵向，入口（web/API）在顶部，持久化和外部客户端在底部。向内布局：核心居中，驱动方适配器在左，被驱动方适配器在右。条带等高，外部系统放在框外。
6. 箭头：每个允许的依赖一条，从使用方指向被使用方（或指向核心）。禁止的捷径最多三条，用红色虚线加“×”。
7. 横切关注点只以侧栏形式出现一次，不要从每个元素都拉箭头过去。
8. 图注：一句话规则 + 变体名称 + 箭头图例。颜色：每类层用一种中性色调，领域层突出，红色只用于违规；不用技术徽标。

**自检清单**
- [ ] 只有一个应用或服务；没有服务器、副本或子网。
- [ ] 已写明变体；已陈述依赖规则；箭头含义写在图例中。
- [ ] 每层都有职责说明和至少一个真实模块名。
- [ ] 箭头与实际导入关系图一致，或标为“预期”。
- [ ] 没有透传层；3–5 层。
- [ ] “层级（物理分层）”（tier）只用于物理部署；未与 ArchiMate 分层视点混淆。
- [ ] 名称与仓库包名一致，以便生成一致性规则。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->

- 构建结构：Maven/Gradle 模块及其依赖、`.csproj` ProjectReferences、Go 导入、`package.json` workspaces、Python 顶层包、Rust workspace crates。
- 包树名称（`controller/service/repository`、`domain/application/infrastructure`、`adapters/in|out`、`ports`）。
- 已有的一致性规则（ArchUnit 测试、`.importlinter`）[7][8]。依赖注入的组合根（composition root）显示了向内依赖在运行时于何处装配。
- ADR 和 README 中的架构章节。
- 反证：`docker-compose` 和 Kubernetes 文件描述的是层级（物理分层）和可部署单元（C3/G1），而不是层。
- 需要问人：*预期的*规则、可接受的例外，以及应当画预期结构还是实际结构。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->

1. 这张图针对哪个应用或服务，谁来读？（默认：一个后端服务；开发人员和评审人员。）
2. 画预期设计、代码中的实际结构，还是两者并排？（默认：两者并排，并列出违规。）
3. 适用哪条规则：只能用相邻层、可以用任何更低的层，还是一切都向内依赖领域层？（默认：从代码推导；不明确时用严格堆栈。）
4. 已经在用哪些层名和包名，哪些横切关注点必须出现？（默认：仓库中的名称；认证、日志、配置。）
5. 是否需要我根据图同时生成一致性规则文件（ArchUnit 或 import-linter）？（默认：作为下一步提供。）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->

模型模板：`assets/templates/C8.json` · 布局模板：`layered` · 每个 kind 为 `layer` 的 `groups[]` 条目成为一条带 `component` 节点（作为模块标签）的条带；kind 为 `dependency` 的 `edges` 表示允许的依赖（实线）或运行时依赖（`dashed` 虚线）；`meta.description` 保存变体和规则语句。

## 来源 {#sources}
<!-- skill: omit -->

1. SEI, "Documenting Architectural Layers", CMU/SEI-2000-SR-004 (mirror) — https://pdfs.semanticscholar.org/a9b3/df89f07b4da137de51ed22b84d58c280f910.pdf — 访问于 2026-10-14
2. Fowler, "PresentationDomainDataLayering" (2015) — https://martinfowler.com/bliki/PresentationDomainDataLayering.html — 访问于 2026-10-14
3. Evans, DDD Reference (2015), "Layered Architecture" — https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf — 访问于 2026-10-14
4. Cockburn, "Hexagonal Architecture" (2005) — https://alistair.cockburn.us/hexagonal-architecture/ — 访问于 2026-10-14
5. Palermo, "The Onion Architecture: part 1" (2008) — https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/ — 访问于 2026-10-14
6. R. C. Martin, "The Clean Architecture" (2012) — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — 访问于 2026-10-14
7. ArchUnit user guide — https://www.archunit.org/userguide/html/000_Index.html — 访问于 2026-10-14
8. Import Linter documentation — https://import-linter.readthedocs.io/en/stable/ — 访问于 2026-10-14
9. Microsoft Learn, "Common web application architectures" — https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures — 访问于 2026-10-14
10. Microsoft Learn, "N-tier architecture style" — https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier — 访问于 2026-10-14
11. Android Developers, "Guide to app architecture" — https://developer.android.com/topic/architecture — 访问于 2026-10-14
12. C4 model, Component diagram — https://c4model.com/diagrams/component — 访问于 2026-10-14
13. Visual Paradigm, "Full ArchiMate Viewpoints Guide" (Layered viewpoint; secondary) — https://www.visual-paradigm.com/guide/archimate/full-archimate-viewpoints-guide — 访问于 2026-10-14（未对照 ArchiMate 3.2 规范原文核实）
14. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/ieee-1471/cm — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->

![C8 示例：网店后端的分层——web/API 适配器层（店面、结账端点）、应用层（下单、更新购物车）、领域层（购物车、订单、定价）、基础设施层（持久化、支付服务商客户端、仓库客户端），图注中陈述了严格堆栈规则](/samples/C8-layered-architecture.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
