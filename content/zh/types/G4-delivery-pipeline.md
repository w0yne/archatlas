---
code: G4
slug: delivery-pipeline
family: G
names:
  en: CI/CD and deployment pipeline
  zh: CI/CD 与部署流水线图
  aliases:
    en: [CI/CD pipeline, deployment pipeline, release pipeline, software delivery pipeline, GitOps flow, GitOps delivery view]
    zh: [CI/CD 流水线图, 部署流水线图, 发布流水线, 交付流水线, 软件交付管道图, 发布流水线图, 持续交付流水线, 软件交付流水线图]
question: 一项变更如何成为可信的发布，每次晋级凭借什么证据，出现失败时会怎样？
audiences: [developers, operations, security]
levels: [physical]
phases: [build, operate]
scope: 一条从变更来源到目标环境的发布路径，包括制品、关卡、结果，以及在相关时负责调和期望状态的控制器
formal: {kind: convention, ref: 'No graphical standard. Fowler''s deployment-pipeline description and Humble and Farley''s Continuous Delivery are the practice references; UML activity or BPMN may be used if their semantics are respected; SLSA supplies supply-chain assurance concepts, not notation'}
neighbours: [A9, G1, G2, H2]
status: draft
translationOf: en/types/G4-delivery-pipeline.md
sourceRev: a5d2191
reviewed: false
---

# CI/CD 流水线图（CI/CD and Deployment Pipeline）

> 一张展示变更通往生产环境之路的图：阶段、制品、关卡，以及检查失败时什么会停止、如何恢复。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 一项变更如何成为可信的发布，每次晋级凭借什么证据，失败时会怎样？
- **视点：** 交付、运维和治理。各阶段逐步提升信心；制品标识、关卡和授权比工具标志更重要 [1]。需声明这张图是流程视图、依赖图还是发布状态视图。
- **深层含义：** 流水线阶段不一定是环境，也不一定是应用组件；有些阶段并行运行，有些部署控制器独立于流水线进行调和（reconcile）。GitOps 控制器从仓库拉取期望状态，因此 CI 本身可能从不部署任何东西 [7]。
- **不包含：** 单条 shell 命令、每个单元测试以及应用内部细节。
- **本站采用的定义：** *持续交付*（continuous delivery）指变更始终处于可发布状态，发布与否是业务决策；*持续部署*（continuous deployment）指每项合格的变更都自动发布到生产环境。两者不是同义词；持续部署以持续交付为前提 [1][2]。SLSA v1.2 定义了用于评估供应链安全的 Build 和 Source 两条轨道，它不是绘图表示法；在流水线上画一个“签名”方框并不能获得某个 SLSA 等级 [3]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 开发人员、发布与平台工程师、运维人员、评审人员和变更控制负责人。
- **典型场景：**
  1. 讲解网店店面和订单服务的构建与发布路径。
  2. 找出反馈或审批为何缓慢。
  3. 把同一个经过测试的容器镜像从预发布环境晋级到生产环境。
  4. 高风险发布的渐进式交付与恢复。
  5. 由控制器把清单应用到集群的 GitOps 流程。
- **不适用的情况：** 当部署、授权或验证在别处进行时，把一个简单的构建工作流当作完整的交付系统来展示。
- **与相邻类型的区别：**
  - 结果在哪里运行，选 **G1**。
  - 发布状态及其迁移，选 **E3**。
  - 问题是每一步由谁负责时，选 **H1**。
  - 如果构建身份和证明（attestation）占主导，单独的供应链信任视图比作业图更合适。
  - 问题是从需求到上线的交付流程中时间损耗在哪里（前置时间、等待时间）时，选 **A9**。
  - 需要表达流水线部署到的云服务及其故障边界时，选 **G2**。
  - 需要表达发布后用于验证、并触发恢复的观测信号时，选 **H2**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 非正式的流程图或依赖图约定。厂商的流水线界面有自己的模型 [5][6]；不要把它当作通用规范。
- **发布路径视图的必备元素：**
  - 触发器或变更来源。
  - 阶段和动作，以及它们之间的依赖。
  - 制品标识及其存储位置。
  - 自动和人工关卡，以及目标环境。
  - 成功、失败和停止三种结果；验证和恢复的责任方。
- **连线含义：** 给每条连线标注为*触发*、*依赖于*、*产出或消费制品*、*晋级摘要（digest）*或*部署或调和*。不要用同一种箭头同时表示顺序和制品流。
- **泳道：** 当职责重要时，把参与者或控制器（CI 系统、镜像仓库、审批人、GitOps 控制器）分开。
- **分支：** 扇出和扇入需要声明条件；不要暗示每个分支都总会运行。
- **可选：** 来源证明（provenance）或签名验证、扫描、审批人身份、并发控制、流量百分比、功能开关、前滚或回滚、数据库兼容性、漂移调和。除非有证据，时间和百分比仅作示意。
- **文字预算：** 阶段或动作名称（2–4 个词）；制品标签保持简短（名称加摘要或标签）。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **把能快速建立信心的检查放在前面，** 较慢的放在后面或并行运行；这才是流水线的根本理由，而不是一份固定的产品清单 [1]。
2. **晋级经过测试的不可变制品，** 并让其标识或摘要可见。配置可以因环境而异；针对特定平台的构建是另一个经过测试的制品，而不是变相的“一次构建”。
3. **将人工审批、自动化策略检查和部署健康状况分开。** 工作流文件中出现环境名称，并不能证明需要评审人；保护规则是环境的属性，需要单独配置 [4]。
4. **如实建模恢复。** 部署前的失败会停止晋级；上线后的恢复可能是回滚、前滚、流量切换或数据恢复。对不可逆的数据变更来说，“总是回滚”并不安全。
5. **对于 GitOps，要画出仓库更新和控制器的调和，** 而不是一条从 CI 直接指向集群的箭头 [7]。

### 反模式
1. **一排线性的方框，** 掩盖了依赖、制品和并行分支。
2. **把生成证明画成信任：** 下游无人验证的证明不提供任何保证 [3]。
3. **按工具名称画关卡：** “production”暗示了一个可能并不存在的审批。
4. **把回滚当作唯一的失败路径。**
5. **一种箭头表示一切：** 触发、依赖和制品流混在一起。

## 范例 {#exemplars}
<!-- skill: omit -->
- [AWS CodePipeline: pipeline structure reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html) — 阶段与动作图，含串行和并行动作以及明确的人工审批；这是一种产品模型，而非通用表示法。
- [Google Cloud: CI/CD for containerised apps](https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke) — 将构建、镜像仓库、预发布晋级和生产审批分开。
- [Google Cloud: Modern CI/CD with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture) — 区分基础设施交付与应用交付，并将演示版与隔离的多项目变体进行对比。
- [Argo CD: architectural overview](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/) — 部署侧的补充：仓库状态和调和控制器解释了基于拉取的交付。
- 厂商资料：仅提供链接，改编图形前请查看各页面的许可。参考资料可能包含不适合生产的学习捷径。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 选定一条变更路径及其触发器；在标题中说明是现状还是提议，例如“网店订单服务：当前发布路径”。
2. 追踪作业依赖以及实际的制品产出与消费；看每个作业需要什么，而不是工具叫什么。
3. 标出目标环境、审批人或控制器，以及存在于仓库之外的缺口（分支保护、环境评审人）。
4. 布局：作为依赖图从左到右排列；阶段作为列，并行作业纵向堆叠，当职责重要时每个控制器单独一条泳道。制品存储和镜像仓库放在主行下方。
5. 连线：依赖和触发用实线，制品流用另一种样式，部署或调和用第三种。标注分支条件。
6. 在每个关卡处展示停止行为，并单独画出一条带标签的部署后恢复路径。
7. 文字：每个阶段 2–4 个词；制品标签带标签名或摘要。颜色：自动阶段用中性色，人工关卡用一种强调色，未核实或未知的关卡用不同样式。不要只靠颜色区分。

**自检清单**
- [ ] 已区分持续集成、持续交付和自动部署。
- [ ] 触发、依赖和制品流使用分别标注的连线。
- [ ] 经过测试的制品的标识在晋级过程中可见。
- [ ] 每个人工或自动关卡都有证据，或标为未知。
- [ ] 并行分支和汇合说明了其条件。
- [ ] 部署前的失败会停止晋级，且停止已画出。
- [ ] 部署后的恢复遵守数据和状态约束。
- [ ] 没有遗漏 GitOps 调和或外部发布机制。
- [ ] 没有仅凭图本身暗示任何保证等级。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **流水线定义：** CI 系统的工作流文件、可复用工作流、作业依赖（`needs`）和条件、制品上传与下载。
- **发布路径：** 镜像仓库引用和摘要、部署命令和清单、GitOps 应用和控制器设置、数据迁移、健康关卡、恢复脚本。
- **局限：** 声明 `environment: production` 并不能证明有审批；分支保护、环境评审人、运行器隔离和云权限通常位于仓库之外。
- **必须由人提供：** 谁审批、执行哪些策略、恢复实践。
- 不要为了了解架构而运行流水线。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 范围是仅 CI、按需发布，还是自动部署到生产？（按需发布）
2. 应追踪哪个变更来源和制品？（订单服务的容器镜像）
3. 工作流文件之外存在哪些审批和环境策略？（询问；确认前标为未知）
4. 是推送式部署，还是由控制器调和期望状态？（以仓库中的实际情况为准）
5. 失败的上线和不兼容的数据迁移如何处理？（分别展示前滚和数据恢复）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/G4.json` · 布局模板：`tree` · 触发器是 `event` 节点，阶段和作业是沿 `dependency` 边从左到右排列的 `task` 节点，制品和镜像仓库是通过 `data` 边连接的 `store` 节点，部署或调和步骤使用 `call` 边，控制器或审批人成为 `lane` 分组；关卡状态用节点的 `style`（尚未通过用 `planned`）或 `tags` 表示。

## 来源 {#sources}
<!-- skill: omit -->
1. M. Fowler, "Deployment Pipeline" (30 May 2013) — https://www.martinfowler.com/bliki/DeploymentPipeline.html — 访问于 2026-10-14
2. M. Fowler, "Continuous Delivery"（讨论 Humble 和 Farley 2010 年的著作；2026-10-14 核查了交付与部署的区别） — https://martinfowler.com/bliki/ContinuousDelivery.html — 访问于 2026-10-14
3. OpenSSF, "SLSA specification v1.2" and "Build: Provenance" — https://slsa.dev/spec/v1.2/ ; https://slsa.dev/spec/v1.2/build-provenance — 访问于 2026-10-14
4. GitHub Docs, "Deployments and environments" — https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments — 访问于 2026-10-14
5. AWS, "CodePipeline concepts" and "Pipeline structure reference" — https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html ; https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html — 访问于 2026-10-14
6. Google Cloud, "CI/CD pipeline for developing and delivering containerized apps" — https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke — 访问于 2026-10-14
7. Argo CD, "Architectural Overview" — https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/ — 访问于 2026-10-14
8. Google Cloud, "Modern CI/CD with GKE: Build a CI/CD system" — https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![G4 示例：网上商城发布路径，从提交经构建、测试和扫描到镜像仓库中的镜像，先晋级到预发布环境，人工审批后再到生产环境，由 GitOps 控制器应用清单](/samples/G4-delivery-pipeline.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
