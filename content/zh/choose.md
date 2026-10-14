---
title: 如何选择架构图
description: 按读者和图要回答的问题，选出合适的架构图类型。
translationOf: en/choose.md
sourceRev: 4aff57217f59787fc10713d19948d8dd81a4217f
reviewed: true
---

# 如何选择架构图

很多架构图的问题在画第一个框之前就已经埋下了：一张图想同时回答好几个问题，或者用了对的表示法却给错了读者。本页帮你做到**一个问题一张图**。如果读者需要两个答案，就画两张图。

先用常见需求找到首选；遇到更具体的问题，再展开决策树和参考列表。[不熟悉术语？先读通俗解释。](/zh/use/glossary)

目录中的术语：[应用组合](/zh/use/glossary#estate)、[用户画像](/zh/use/glossary#persona)、[BPMN](/zh/use/glossary#bpmn)、[信任边界](/zh/use/glossary#trust-boundary)、[晋级检查](/zh/use/glossary#promotion-gate)、[精益价值流图](/zh/use/glossary#lean)、[限界上下文](/zh/use/glossary#bounded-context)、[ArchiMate](/zh/use/glossary#archimate)、[Rummler–Brache 泳道图](/zh/use/glossary#rummler-brache)。

<!-- 维护者：修改 types.yaml 和 selection-tree.yaml，不要手改生成块。 -->

## 常见需求：从这里开始

<!-- BEGIN GENERATED: common -->
- **让新开发者了解系统**：先选：[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)。再考虑：[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[E1 时序图](/zh/types/e1-sequence-diagram)。先看系统与周边，再看运行组成和一次请求。
- **向技术负责人介绍全局**：先选：[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)。再考虑：[C1 应用全景图](/zh/types/c1-application-landscape)。如果主题是多个应用的全景而非单个系统，改用 C1。
- **向业务读者说明方案**：先选：[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)。再考虑：[A1 业务能力图](/zh/types/a1-capability-map)。先展示方案的大块组成；讨论业务能力或投资时再用 A1。
- **说明订单状态**：先选：[E3 状态机图](/zh/types/e3-state-machine)。再考虑：[E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)。展示状态及允许的变化；如果要看处理步骤，改用 E2。
- **说明谁能访问什么**：先选：[F3 访问控制模型](/zh/types/f3-access-control-model)。再考虑：[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)。先说明权限与范围；需要解释身份验证和执行位置时加 F1。
- **规划迁移**：先选：[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)。再考虑：[G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)。展示可独立理解的过渡状态，再用现状与目标成对的部署或云架构图补充细节。
- **画数据库或数据模型图**：先选：[D1 实体关系图](/zh/types/d1-entity-relationship)。再考虑：[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)。展示实体与关系；关心血缘和归属时再加 D3。
- **说明发布流程**：先选：[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)。再考虑：[G1 部署图](/zh/types/g1-deployment-diagram)。展示构建、检查和晋级，再用 G1 说明最终部署。
<!-- END GENERATED: common -->

## 先回答四个问题

<!-- BEGIN GENERATED: questions -->
1. 谁来看？看完要做什么（决策、审批、开发、运维、评审）？
2. 这张图要回答哪个问题？在下面选一个分支。
3. 范围是什么：整个企业 / 应用组合、单个系统，还是系统内的一个部件？
4. 画现状、目标，还是两者（分开成两张图）？
<!-- END GENERATED: questions -->

## 决策树：这张图要回答什么？

先找到读者的问题，再顺着它找到一到两种类型。列出两种类型时，后面的说明会告诉你怎么二选一。

<!-- BEGIN GENERATED: tree -->
- **为什么做、价值在哪、投资往哪放？**
  - 组织能做什么、投资往哪放 → [A1 业务能力图](/zh/types/a1-capability-map)
  - 哪些阶段为干系人交付价值 → [A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)。A2 不含时间、把阶段映射到能力；A9 度量处理与等待时间。
  - 用业务语言说明方案是什么 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
  - 如何从现状分步走到目标 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
  - 某类用户（用户画像）的整体体验 → [A6 用户旅程图](/zh/types/a6-journey-map)
  - 谁能影响项目、如何沟通 → [H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
- **要做什么、给谁用、范围内外是什么？**
  - 范围内外是什么、谁与我们对接 → [B4 范围图](/zh/types/b4-scope-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)。强调本期边界用 B4；主题是软件系统及其外部时用 C2。
  - 业务与哪些外部方往来、交换什么 → [A3 业务上下文图](/zh/types/a3-business-context)
  - 哪些角色做什么、在哪个版本 → [A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)、[B2 用户故事地图](/zh/types/b2-user-story-map)。A4 展示多角色覆盖；B2 讲一个端到端故事并按版本切片。
  - 系统支持哪些用户目标、给谁 → [B1 用例图](/zh/types/b1-use-case-diagram)
  - 有哪些功能、拆多细、优先级如何 → [B3 功能树（功能分解）](/zh/types/b3-feature-tree)
  - 一件业务如何在参与方之间流转 → [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)
  - 某类用户完成一项任务时在每个阶段需要什么 → [A6 用户旅程图](/zh/types/a6-journey-map)
- **由哪些部分组成、如何组织？**
  - 企业内的众多应用及其归属 → [C1 应用全景图](/zh/types/c1-application-landscape)
  - 给非技术读者看的主要组成 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
  - 单个系统：用户与外部系统 → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
  - 单个系统：可运行的应用与数据存储 → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
  - 单个应用内部：组件 → [C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)
  - 职责与接口，不含技术选型 → [C5 逻辑架构图](/zh/types/c5-logical-architecture)
  - 领域中的模型边界 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
  - 代码分层与允许的依赖 → [C8 分层架构图](/zh/types/c8-layered-architecture)
  - 业务、应用、技术如何互相支撑 → [I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)
- **各部分 / 各系统之间怎么连接？**
  - 接口的集成方式、协议、认证与失败语义 → [C6 集成与接口图](/zh/types/c6-integration-interface)
  - 企业范围内应用之间的依赖 → [C1 应用全景图](/zh/types/c1-application-landscape)
  - 单个系统内各运行单元如何通信 → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
  - 一个场景中的消息顺序 → [E1 时序图](/zh/types/e1-sequence-diagram)
  - 领域模型与团队之间的关系 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- **有哪些数据、怎么流动、归谁负责？**
  - 有哪些业务对象、如何关联 → [D1 实体关系图](/zh/types/d1-entity-relationship)
  - 数据如何在加工与存储之间流动 → [D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)
  - 数据从哪里来、归谁负责 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
  - 哪些数据跨越信任边界 → [F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
- **事情按什么顺序发生、有哪些状态？**
  - 参与者之间按顺序的消息 → [E1 时序图](/zh/types/e1-sequence-diagram)
  - 一段逻辑的步骤、判断与并行分支 → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)
  - 一个对象的生命周期 → [E3 状态机图](/zh/types/e3-state-machine)
  - 角色或系统之间的交接 → [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)。轻量交接（常以系统为泳道）用 E4；需要 BPMN 语义（池、消息流、事件）时用 A5。
  - 登录与访问判定如何发生 → [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
  - 交付过程在哪里等待 → [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- **谁能做什么、哪里可能出安全问题？**
  - 登录、令牌，以及访问在哪里判定 → [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
  - 威胁与信任边界 → [F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
  - 谁在什么范围内能做什么 → [F3 访问控制模型](/zh/types/f3-access-control-model)
  - 网络暴露面与路径 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- **跑在哪里、怎么发布？**
  - 如何从现有系统迁移到目标 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
  - 软件运行在哪里 → [G1 部署图](/zh/types/g1-deployment-diagram)
  - 使用哪些云服务及其故障边界 → [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)
  - 网络分区与路径 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
  - 变更如何发布到生产 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
  - 如何观测运行中的系统 → [H2 可观测性视图](/zh/types/h2-observability-view)
- **谁负责、怎么运行和监控？**
  - 每项活动由谁负责 → [H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)
  - 需要与谁沟通、如何沟通 → [H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
  - 问题如何被发现与响应 → [H2 可观测性视图](/zh/types/h2-observability-view)
  - 哪些数据归谁 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
  - 运维流程中的交接 → [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)
  - 应用的归属与生命周期状态 → [C1 应用全景图](/zh/types/c1-application-landscape)
  - 发布控制与晋级关卡 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- **怎样把多张图组织成一套架构描述？**
  - 面向不同读者的多张视图并保持一致 → [I1 4+1 视图模型](/zh/types/i1-four-plus-one)
  - 跨业务、应用、技术的企业视图 → [I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)
<!-- END GENERATED: tree -->

## 读者 × 问题

同一个问题，读者不同，需要的图也不同。格子包含经过编排的首选和目录匹配，是建议而不是必填清单。在小屏幕上可使用下面的分读者列表。

<!-- BEGIN GENERATED: matrix -->
| 问题 | 领导与发起人 | 业务负责人与业务分析 | 产品与设计 | 架构师 | 开发与测试 | 运维与 SRE | 安全与合规 |
|---|---|---|---|---|---|---|---|
| 为什么做、价值在哪、投资往哪放？ | [A1 业务能力图](/zh/types/a1-capability-map)、[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A6 用户旅程图](/zh/types/a6-journey-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map) | [A1 业务能力图](/zh/types/a1-capability-map)、[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A6 用户旅程图](/zh/types/a6-journey-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map) | [A6 用户旅程图](/zh/types/a6-journey-map) | [A1 业务能力图](/zh/types/a1-capability-map)、[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap) | – | [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map) | – |
| 要做什么、给谁用、范围内外是什么？ | [A3 业务上下文图](/zh/types/a3-business-context)、[A6 用户旅程图](/zh/types/a6-journey-map)、[B4 范围图](/zh/types/b4-scope-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context) | [A3 业务上下文图](/zh/types/a3-business-context)、[A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A6 用户旅程图](/zh/types/a6-journey-map)、[B1 用例图](/zh/types/b1-use-case-diagram)、[B2 用户故事地图](/zh/types/b2-user-story-map)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context) | [A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A6 用户旅程图](/zh/types/a6-journey-map)、[B1 用例图](/zh/types/b1-use-case-diagram)、[B2 用户故事地图](/zh/types/b2-user-story-map)、[B3 功能树（功能分解）](/zh/types/b3-feature-tree)、[B4 范围图](/zh/types/b4-scope-diagram) | [A3 业务上下文图](/zh/types/a3-business-context)、[B4 范围图](/zh/types/b4-scope-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context) | [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[B1 用例图](/zh/types/b1-use-case-diagram)、[B2 用户故事地图](/zh/types/b2-user-story-map)、[B3 功能树（功能分解）](/zh/types/b3-feature-tree)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context) | – | [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context) |
| 由哪些部分组成、如何组织？ | [A1 业务能力图](/zh/types/a1-capability-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C1 应用全景图](/zh/types/c1-application-landscape)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view) | [A1 业务能力图](/zh/types/a1-capability-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map) | [C5 逻辑架构图](/zh/types/c5-logical-architecture) | [A1 业务能力图](/zh/types/a1-capability-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C1 应用全景图](/zh/types/c1-application-landscape)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)、[C5 逻辑架构图](/zh/types/c5-logical-architecture)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[C8 分层架构图](/zh/types/c8-layered-architecture)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view) | [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)、[C5 逻辑架构图](/zh/types/c5-logical-architecture)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[C8 分层架构图](/zh/types/c8-layered-architecture) | [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram) | [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram) |
| 各部分 / 各系统之间怎么连接？ | [C1 应用全景图](/zh/types/c1-application-landscape) | [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map) | – | [C1 应用全景图](/zh/types/c1-application-landscape)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C6 集成与接口图](/zh/types/c6-integration-interface)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[E1 时序图](/zh/types/e1-sequence-diagram) | [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C6 集成与接口图](/zh/types/c6-integration-interface)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[E1 时序图](/zh/types/e1-sequence-diagram) | [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C6 集成与接口图](/zh/types/c6-integration-interface) | [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram) |
| 有哪些数据、怎么流动、归谁负责？ | – | [D1 实体关系图](/zh/types/d1-entity-relationship)、[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership) | – | [D1 实体关系图](/zh/types/d1-entity-relationship)、[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow) | [D1 实体关系图](/zh/types/d1-entity-relationship) | – | [D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow) |
| 事情按什么顺序发生、有哪些状态？ | [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map) | [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional) | [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[E3 状态机图](/zh/types/e3-state-machine) | [E1 时序图](/zh/types/e1-sequence-diagram)、[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow) | [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[E1 时序图](/zh/types/e1-sequence-diagram)、[E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[E3 状态机图](/zh/types/e3-state-machine)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow) | [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional) | [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow) |
| 谁能做什么、哪里可能出安全问题？ | – | [F3 访问控制模型](/zh/types/f3-access-control-model) | – | [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology) | [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model) | [G3 网络拓扑与连通视图](/zh/types/g3-network-topology) | [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology) |
| 跑在哪里、怎么发布？ | [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G1 部署图](/zh/types/g1-deployment-diagram)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap) | – | – | [G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology) | [G1 部署图](/zh/types/g1-deployment-diagram)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap) | [G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap) | [G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline) |
| 谁负责、怎么运行和监控？ | [C1 应用全景图](/zh/types/c1-application-landscape)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)、[H2 可观测性视图](/zh/types/h2-observability-view)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map) | [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map) | – | [C1 应用全景图](/zh/types/c1-application-landscape)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership) | [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)、[H2 可观测性视图](/zh/types/h2-observability-view) | [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)、[H2 可观测性视图](/zh/types/h2-observability-view) | [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline) |
| 怎样把多张图组织成一套架构描述？ | [I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view) | – | – | [I1 4+1 视图模型](/zh/types/i1-four-plus-one)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view) | [I1 4+1 视图模型](/zh/types/i1-four-plus-one) | – | – |
<!-- END GENERATED: matrix -->

## 按读者浏览

<!-- BEGIN GENERATED: audiences -->
<details><summary>领导与发起人</summary>

- **为什么做、价值在哪、投资往哪放？** ：[A1 业务能力图](/zh/types/a1-capability-map)、[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A6 用户旅程图](/zh/types/a6-journey-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
- **要做什么、给谁用、范围内外是什么？** ：[A3 业务上下文图](/zh/types/a3-business-context)、[A6 用户旅程图](/zh/types/a6-journey-map)、[B4 范围图](/zh/types/b4-scope-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- **由哪些部分组成、如何组织？** ：[A1 业务能力图](/zh/types/a1-capability-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C1 应用全景图](/zh/types/c1-application-landscape)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)
- **各部分 / 各系统之间怎么连接？** ：[C1 应用全景图](/zh/types/c1-application-landscape)
- **事情按什么顺序发生、有哪些状态？** ：[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- **跑在哪里、怎么发布？** ：[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G1 部署图](/zh/types/g1-deployment-diagram)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- **谁负责、怎么运行和监控？** ：[C1 应用全景图](/zh/types/c1-application-landscape)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)、[H2 可观测性视图](/zh/types/h2-observability-view)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
- **怎样把多张图组织成一套架构描述？** ：[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)

</details>

<details><summary>业务负责人与业务分析</summary>

- **为什么做、价值在哪、投资往哪放？** ：[A1 业务能力图](/zh/types/a1-capability-map)、[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A6 用户旅程图](/zh/types/a6-journey-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
- **要做什么、给谁用、范围内外是什么？** ：[A3 业务上下文图](/zh/types/a3-business-context)、[A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A6 用户旅程图](/zh/types/a6-journey-map)、[B1 用例图](/zh/types/b1-use-case-diagram)、[B2 用户故事地图](/zh/types/b2-user-story-map)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- **由哪些部分组成、如何组织？** ：[A1 业务能力图](/zh/types/a1-capability-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- **各部分 / 各系统之间怎么连接？** ：[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- **有哪些数据、怎么流动、归谁负责？** ：[D1 实体关系图](/zh/types/d1-entity-relationship)、[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- **事情按什么顺序发生、有哪些状态？** ：[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)
- **谁能做什么、哪里可能出安全问题？** ：[F3 访问控制模型](/zh/types/f3-access-control-model)
- **谁负责、怎么运行和监控？** ：[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)

</details>

<details><summary>产品与设计</summary>

- **为什么做、价值在哪、投资往哪放？** ：[A6 用户旅程图](/zh/types/a6-journey-map)
- **要做什么、给谁用、范围内外是什么？** ：[A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A6 用户旅程图](/zh/types/a6-journey-map)、[B1 用例图](/zh/types/b1-use-case-diagram)、[B2 用户故事地图](/zh/types/b2-user-story-map)、[B3 功能树（功能分解）](/zh/types/b3-feature-tree)、[B4 范围图](/zh/types/b4-scope-diagram)
- **由哪些部分组成、如何组织？** ：[C5 逻辑架构图](/zh/types/c5-logical-architecture)
- **事情按什么顺序发生、有哪些状态？** ：[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[E3 状态机图](/zh/types/e3-state-machine)

</details>

<details><summary>架构师</summary>

- **为什么做、价值在哪、投资往哪放？** ：[A1 业务能力图](/zh/types/a1-capability-map)、[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- **要做什么、给谁用、范围内外是什么？** ：[A3 业务上下文图](/zh/types/a3-business-context)、[B4 范围图](/zh/types/b4-scope-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- **由哪些部分组成、如何组织？** ：[A1 业务能力图](/zh/types/a1-capability-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C1 应用全景图](/zh/types/c1-application-landscape)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)、[C5 逻辑架构图](/zh/types/c5-logical-architecture)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[C8 分层架构图](/zh/types/c8-layered-architecture)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)
- **各部分 / 各系统之间怎么连接？** ：[C1 应用全景图](/zh/types/c1-application-landscape)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C6 集成与接口图](/zh/types/c6-integration-interface)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[E1 时序图](/zh/types/e1-sequence-diagram)
- **有哪些数据、怎么流动、归谁负责？** ：[D1 实体关系图](/zh/types/d1-entity-relationship)、[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
- **事情按什么顺序发生、有哪些状态？** ：[E1 时序图](/zh/types/e1-sequence-diagram)、[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
- **谁能做什么、哪里可能出安全问题？** ：[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- **跑在哪里、怎么发布？** ：[G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- **谁负责、怎么运行和监控？** ：[C1 应用全景图](/zh/types/c1-application-landscape)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- **怎样把多张图组织成一套架构描述？** ：[I1 4+1 视图模型](/zh/types/i1-four-plus-one)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)

</details>

<details><summary>开发与测试</summary>

- **要做什么、给谁用、范围内外是什么？** ：[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[B1 用例图](/zh/types/b1-use-case-diagram)、[B2 用户故事地图](/zh/types/b2-user-story-map)、[B3 功能树（功能分解）](/zh/types/b3-feature-tree)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- **由哪些部分组成、如何组织？** ：[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)、[C5 逻辑架构图](/zh/types/c5-logical-architecture)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[C8 分层架构图](/zh/types/c8-layered-architecture)
- **各部分 / 各系统之间怎么连接？** ：[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C6 集成与接口图](/zh/types/c6-integration-interface)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[E1 时序图](/zh/types/e1-sequence-diagram)
- **有哪些数据、怎么流动、归谁负责？** ：[D1 实体关系图](/zh/types/d1-entity-relationship)
- **事情按什么顺序发生、有哪些状态？** ：[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[E1 时序图](/zh/types/e1-sequence-diagram)、[E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[E3 状态机图](/zh/types/e3-state-machine)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
- **谁能做什么、哪里可能出安全问题？** ：[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model)
- **跑在哪里、怎么发布？** ：[G1 部署图](/zh/types/g1-deployment-diagram)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- **谁负责、怎么运行和监控？** ：[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)、[H2 可观测性视图](/zh/types/h2-observability-view)
- **怎样把多张图组织成一套架构描述？** ：[I1 4+1 视图模型](/zh/types/i1-four-plus-one)

</details>

<details><summary>运维与 SRE</summary>

- **为什么做、价值在哪、投资往哪放？** ：[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- **由哪些部分组成、如何组织？** ：[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- **各部分 / 各系统之间怎么连接？** ：[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C6 集成与接口图](/zh/types/c6-integration-interface)
- **事情按什么顺序发生、有哪些状态？** ：[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)
- **谁能做什么、哪里可能出安全问题？** ：[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- **跑在哪里、怎么发布？** ：[G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- **谁负责、怎么运行和监控？** ：[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)、[H2 可观测性视图](/zh/types/h2-observability-view)

</details>

<details><summary>安全与合规</summary>

- **要做什么、给谁用、范围内外是什么？** ：[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- **由哪些部分组成、如何组织？** ：[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- **各部分 / 各系统之间怎么连接？** ：[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- **有哪些数据、怎么流动、归谁负责？** ：[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
- **事情按什么顺序发生、有哪些状态？** ：[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
- **谁能做什么、哪里可能出安全问题？** ：[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- **跑在哪里、怎么发布？** ：[G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- **谁负责、怎么运行和监控？** ：[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)

</details>

<!-- END GENERATED: audiences -->

## 按生命周期阶段

<!-- BEGIN GENERATED: phases -->
- **立项** ：[A1 业务能力图](/zh/types/a1-capability-map)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C1 应用全景图](/zh/types/c1-application-landscape)
<details><summary>其他可选类型</summary>

[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A3 业务上下文图](/zh/types/a3-business-context)、[A6 用户旅程图](/zh/types/a6-journey-map)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[B4 范围图](/zh/types/b4-scope-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)、[H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)

</details>

- **需求** ：[B1 用例图](/zh/types/b1-use-case-diagram)、[B4 范围图](/zh/types/b4-scope-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
<details><summary>其他可选类型</summary>

[A3 业务上下文图](/zh/types/a3-business-context)、[A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A6 用户旅程图](/zh/types/a6-journey-map)、[B2 用户故事地图](/zh/types/b2-user-story-map)、[B3 功能树（功能分解）](/zh/types/b3-feature-tree)、[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)

</details>

- **设计** ：[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[D1 实体关系图](/zh/types/d1-entity-relationship)、[E1 时序图](/zh/types/e1-sequence-diagram)
<details><summary>其他可选类型</summary>

[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)、[C1 应用全景图](/zh/types/c1-application-landscape)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)、[C5 逻辑架构图](/zh/types/c5-logical-architecture)、[C6 集成与接口图](/zh/types/c6-integration-interface)、[C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)、[C8 分层架构图](/zh/types/c8-layered-architecture)、[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[E3 状态机图](/zh/types/e3-state-machine)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model)、[G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)、[I1 4+1 视图模型](/zh/types/i1-four-plus-one)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)

</details>

- **构建** ：[C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)、[E1 时序图](/zh/types/e1-sequence-diagram)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
<details><summary>其他可选类型</summary>

[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[C6 集成与接口图](/zh/types/c6-integration-interface)、[C8 分层架构图](/zh/types/c8-layered-architecture)、[D1 实体关系图](/zh/types/d1-entity-relationship)、[E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[E3 状态机图](/zh/types/e3-state-machine)、[F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)、[F3 访问控制模型](/zh/types/f3-access-control-model)

</details>

- **发布与运营** ：[G1 部署图](/zh/types/g1-deployment-diagram)、[G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)、[H2 可观测性视图](/zh/types/h2-observability-view)
<details><summary>其他可选类型</summary>

[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)、[D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)、[H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)

</details>

<!-- END GENERATED: phases -->

## 大家口中的叫法

有些日常叫法并不对应某一种图。有人这样要图时，先问清楚他指的是哪一种，或者自己选一种并说明选的是哪一种。

<!-- BEGIN GENERATED: terms -->
- *系统架构图（system architecture diagram）* → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[G1 部署图](/zh/types/g1-deployment-diagram)。先用 C2 看系统与周边，再用 C3 看运行组成；A7 是概念方案概览，G1 展示部署。
- *技术架构图（technical architecture diagram）* → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)。带技术选型的容器图（C3），或基础设施视图（G1、G2）。
- *应用架构图（application architecture diagram）* → [C1 应用全景图](/zh/types/c1-application-landscape)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)。多应用全景用 C1，单个系统的可运行应用与数据存储用 C3。单个运行应用的内部组件是 C4，不是 C3。
- *业务架构图（business architecture diagram）* → [A1 业务能力图](/zh/types/a1-capability-map)、[A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)。是一类图而不是一张图：能力（A1）、价值流（A2）、流程（A5）。
- *上下文图（context diagram）* → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[A3 业务上下文图](/zh/types/a3-business-context)、[B4 范围图](/zh/types/b4-scope-diagram)。软件系统与外部（C2）；业务往来（A3）；范围内外（B4）。
- *0 层数据流图（DFD level 0）* → [D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)、[C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)。存在两种编号习惯：有人把只有一个处理的上下文级数据流图（类似 C2）叫作 0 层，也有人指它下面的第一层分解（D2）。请改说“上下文级数据流图”或“第一层数据流图”。
- *流程图（flowchart）* → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)。一段处理逻辑（E2）；有 BPMN 语义的业务流程（A5）；角色 / 系统间交接（E4）。
- *泳道图（swimlane diagram）* → [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)。轻量交接（E4），或 BPMN 的池 / 泳道与消息流（A5）。
- *物理架构图（physical architecture diagram）* → [G1 部署图](/zh/types/g1-deployment-diagram)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)。软件部署到基础设施（G1）或网络（G3），需说明是哪种。
- *模块图（module diagram）* → [C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)、[C5 逻辑架构图](/zh/types/c5-logical-architecture)、[C8 分层架构图](/zh/types/c8-layered-architecture)。单个容器内部组件（C4）、与技术无关的职责模块（C5）或代码分层（C8）。
- *功能架构图（functional architecture diagram）* → [C5 逻辑架构图](/zh/types/c5-logical-architecture)、[B3 功能树（功能分解）](/zh/types/b3-feature-tree)。逻辑职责划分（C5）；系统工程意义上的功能分解（B3）。
- *价值流图（value stream map）* → [A2 价值流（业务架构）](/zh/types/a2-value-stream)、[A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)。业务架构价值流，不含时间（A2）；或含处理时间与前置时间的精益价值流图（A9）。
- *参考架构（reference architecture）* → [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)。是一种状态（参考 / 方案 / 已实现 / 实测），不是图的类型。先选视图，再标明状态。
- *交互图（interaction diagram）* → [E1 时序图](/zh/types/e1-sequence-diagram)。UML 中是时序图、通信图、时间图、交互概览图的统称；通常选时序图。
- *分层图（layered diagram）* → [C8 分层架构图](/zh/types/c8-layered-architecture)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)、[I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)。带依赖规则的代码分层（C8）、概念分层（A7）或 ArchiMate 业务 / 应用 / 技术分层（I2）。
- *数据地图（data map）* → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)、[D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)。数据来源与归属（D3），或数据在加工之间如何流动（D2）。
- *全局图 / 架构概览 / 系统概览（big picture / architecture overview / system overview）* → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)、[C1 应用全景图](/zh/types/c1-application-landscape)、[A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)。单个系统先用 C2，多应用用 C1，业务层方案概览用 A7。
- *数据库图 / 数据模式（database diagram / schema）* → [D1 实体关系图](/zh/types/d1-entity-relationship)。添加字段和键之前，先确定概念、逻辑还是物理层次。
- *AWS / Azure / GCP 架构图（AWS / Azure / GCP architecture diagram）* → [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)。展示云服务组成；实际关心软件部署位置时用 G1。
- *Kubernetes 架构图（Kubernetes diagram）* → [G1 部署图](/zh/types/g1-deployment-diagram)。先看工作负载部署；只有关心路由与网络隔离时才加 G3。
- *微服务架构图（microservices diagram）* → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)。运行服务与存储用 C3，单次跨服务交互用 E1。
- *工作流 / 用户流程（workflow / user flow）* → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)、[E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)、[A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)、[A6 用户旅程图](/zh/types/a6-journey-map)。先确认是逻辑步骤、角色交接、严格记法的业务流程，还是用户体验。
- *基础设施图（infrastructure diagram）* → [G1 部署图](/zh/types/g1-deployment-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)、[G3 网络拓扑与连通视图](/zh/types/g3-network-topology)。部署位置、云服务组成和网络连通回答不同问题，先确定目的。
- *技术栈图（tech stack diagram）* → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)、[G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)。把技术对应到运行职责或云服务，而不是堆放标志。
<!-- END GENERATED: terms -->

下面这些叫法只对应一种类型：

<!-- BEGIN GENERATED: aliases -->
- 4+1 架构视图模型 → [I1 4+1 视图模型](/zh/types/i1-four-plus-one)
- API 全景图 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- ArchiMate 分层视点 → [I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)
- BPMN 协作图 → [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)
- BPMN 流程图 → [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)
- C4 模型第 1 层 → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- C4 模型第 2 层 → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- C4 模型第 3 层 → [C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)
- C4 第二层 → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- CI/CD 流水线图 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- DDD 上下文映射 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- DDD 战略设计图 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- E-R 图 → [D1 实体关系图](/zh/types/d1-entity-relationship)
- ER 图 → [D1 实体关系图](/zh/types/d1-entity-relationship)
- IT 蓝图 → [C1 应用全景图](/zh/types/c1-application-landscape)
- RACI 职责分配矩阵 → [H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)
- UML 活动图 → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)
- UML 用例图 → [B1 用例图](/zh/types/b1-use-case-diagram)
- 一页纸架构 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
- 上下文映射图 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- 上下文级数据流图 → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- 业务-应用-技术视图 → [I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)
- 业务场景地图 → [A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)
- 业务场景清单 → [A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)
- 业务流程图 → [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)
- 业务流程建模图 → [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)
- 业务环境图 → [A3 业务上下文图](/zh/types/a3-business-context)
- 业务背景图 → [A3 业务上下文图](/zh/types/a3-business-context)
- 业务能力模型 → [A1 业务能力图](/zh/types/a1-capability-map)
- 事件拓扑图 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- 云参考架构 → [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)
- 云服务架构图 → [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)
- 云架构图 → [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)
- 云解决方案架构图 → [G2 云基础设施架构图](/zh/types/g2-cloud-infrastructure-architecture)
- 交互时序图 → [E1 时序图](/zh/types/e1-sequence-diagram)
- 交付流水线 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- 价值流 → [A2 价值流（业务架构）](/zh/types/a2-value-stream)
- 价值流—能力映射 → [A2 价值流（业务架构）](/zh/types/a2-value-stream)
- 价值流程图 → [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- 价值流能力映射 → [A2 价值流（业务架构）](/zh/types/a2-value-stream)
- 价值流阶段 → [A2 价值流（业务架构）](/zh/types/a2-value-stream)
- 价值流阶段图 → [A2 价值流（业务架构）](/zh/types/a2-value-stream)
- 体验旅程图 → [A6 用户旅程图](/zh/types/a6-journey-map)
- 信任边界图 → [F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
- 信息模型 → [D1 实体关系图](/zh/types/d1-entity-relationship)
- 克鲁岑 4+1 视图模型 → [I1 4+1 视图模型](/zh/types/i1-four-plus-one)
- 六边形架构 → [C8 分层架构图](/zh/types/c8-layered-architecture)
- 内部结构图 → [C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)
- 利益相关者矩阵 → [H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
- 功能分解图 → [B3 功能树（功能分解）](/zh/types/b3-feature-tree)
- 功能特性树 → [B3 功能树（功能分解）](/zh/types/b3-feature-tree)
- 功能视图 → [C5 逻辑架构图](/zh/types/c5-logical-architecture)
- 协作图 → [A5 业务流程图（BPMN）](/zh/types/a5-bpmn-process)
- 参与者—用例图 → [B1 用例图](/zh/types/b1-use-case-diagram)
- 发布流水线 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- 发布流水线图 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- 可观测性架构图 → [H2 可观测性视图](/zh/types/h2-observability-view)
- 含信任边界的数据流图 → [F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
- 团队映射图 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- 场景覆盖矩阵 → [A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)
- 基于关系的授权模型 → [F3 访问控制模型](/zh/types/f3-access-control-model)
- 基于属性的授权模型 → [F3 访问控制模型](/zh/types/f3-access-control-model)
- 处理逻辑图 → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)
- 委托访问流程图 → [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
- 威胁建模数据流图 → [F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
- 安全数据流图 → [F2 威胁建模数据流图（含信任边界）](/zh/types/f2-threat-model-data-flow)
- 客户旅程图 → [A6 用户旅程图](/zh/types/a6-journey-map)
- 容器内部结构图 → [C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)
- 容器视图 → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- 层次结构图 → [C8 分层架构图](/zh/types/c8-layered-architecture)
- 干系人图 → [H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
- 平台期图 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 序列图 → [E1 时序图](/zh/types/e1-sequence-diagram)
- 应用交互矩阵 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- 应用协作视图 → [C1 应用全景图](/zh/types/c1-application-landscape)
- 应用地图 → [C1 应用全景图](/zh/types/c1-application-landscape)
- 应用组合图 → [C1 应用全景图](/zh/types/c1-application-landscape)
- 应用通信图 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- 战略设计图 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- 技术分层图 → [C8 分层架构图](/zh/types/c8-layered-architecture)
- 技术架构图（口语，含义宽泛） → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- 持续交付流水线 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- 授权模型 → [F3 访问控制模型](/zh/types/f3-access-control-model)
- 接口关系图 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- 接口清单 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- 控制流图 → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)
- 控制流程图 → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)
- 故事地图 → [B2 用户故事地图](/zh/types/b2-user-story-map)
- 数据分布图 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- 数据归属图 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- 数据模型图 → [D1 实体关系图](/zh/types/d1-entity-relationship)
- 数据流向图 → [D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)
- 数据流程图 → [D2 数据流图（DFD）](/zh/types/d2-data-flow-diagram)
- 数据溯源图 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- 数据血缘图 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- 数据责任图 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- 数据资产地图 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- 整洁架构 → [C8 分层架构图](/zh/types/c8-layered-architecture)
- 方案总览 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
- 方案构想图 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
- 方案概览图 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
- 未来状态图 → [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- 权力利益矩阵 → [H3 干系人地图（权力-利益矩阵）](/zh/types/h3-stakeholder-map)
- 权限模型 → [F3 访问控制模型](/zh/types/f3-access-control-model)
- 架构路线图 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 概念数据模型 → [D1 实体关系图](/zh/types/d1-entity-relationship)
- 概念架构图 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
- 泳道流程图 → [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)
- 洋葱架构 → [C8 分层架构图](/zh/types/c8-layered-architecture)
- 活动图 → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)
- 混合网络连接图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 演进路线图 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 物料与信息流图 → [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- 物理网络图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 特性树 → [B3 功能树（功能分解）](/zh/types/b3-feature-tree)
- 状态图 → [E3 状态机图](/zh/types/e3-state-machine)
- 状态转换图 → [E3 状态机图](/zh/types/e3-state-machine)
- 状态迁移图 → [E3 状态机图](/zh/types/e3-state-machine)
- 现状 / 目标 / 过渡架构 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 现状图 → [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- 生命周期图 → [E3 状态机图](/zh/types/e3-state-machine)
- 用户故事映射 → [B2 用户故事地图](/zh/types/b2-user-story-map)
- 监控架构图 → [H2 可观测性视图](/zh/types/h2-observability-view)
- 程序流程图 → [E2 活动图 / 流程图](/zh/types/e2-activity-flowchart)
- 稳定态图 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 端口与适配器 → [C8 分层架构图](/zh/types/c8-layered-architecture)
- 精益价值流映射 → [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- 精益价值流程图 → [A9 精益价值流图（VSM）](/zh/types/a9-lean-value-stream-map)
- 系统上下文图 → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- 系统全景图 → [C1 应用全景图](/zh/types/c1-application-landscape)
- 系统架构图（口语，含义宽泛） → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- 系统环境图 → [C2 系统上下文图（C4 模型第 1 层）](/zh/types/c2-system-context)
- 系统集成图 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- 组件视图 → [C4 组件图（C4 模型第 3 层）](/zh/types/c4-component-diagram)
- 统一登录流程图 → [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
- 网络拓扑图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 网络架构图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 网络连通图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 网络连通视图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 职责流程图 → [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)
- 能力地图 → [A1 业务能力图](/zh/types/a1-capability-map)
- 能力热力图 → [A1 业务能力图](/zh/types/a1-capability-map)
- 能力路线图 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 范围上下文图 → [B4 范围图](/zh/types/b4-scope-diagram)
- 范围内外图 → [B4 范围图](/zh/types/b4-scope-diagram)
- 范围边界图 → [B4 范围图](/zh/types/b4-scope-diagram)
- 血缘关系图 → [D3 数据血缘与归属图](/zh/types/d3-data-lineage-ownership)
- 角色-场景矩阵 → [A4 业务场景矩阵（角色 × 活动）](/zh/types/a4-scenario-matrix)
- 角色权限矩阵 → [F3 访问控制模型](/zh/types/f3-access-control-model)
- 调用链时序图 → [E1 时序图](/zh/types/e1-sequence-diagram)
- 责任分配矩阵 → [H1 RACI 责任矩阵](/zh/types/h1-raci-matrix)
- 跨层企业架构视图 → [I2 ArchiMate 分层视图](/zh/types/i2-archimate-layered-view)
- 跨职能流程图 → [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)
- 跨部门流程图 → [E4 泳道流程图（跨职能流程图）](/zh/types/e4-swimlane-cross-functional)
- 路由视图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 身份认证流程图 → [F1 认证与授权流程图](/zh/types/f1-authentication-authorization-flow)
- 软件与基础设施映射图 → [G1 部署图](/zh/types/g1-deployment-diagram)
- 软件交付流水线图 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- 软件交付管道图 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- 迁移视图 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 迁移路线图 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 过渡架构 → [A8 目标架构与演进路线图](/zh/types/a8-target-roadmap)
- 运行单元图 → [C3 容器图（C4 模型第 2 层）](/zh/types/c3-container-diagram)
- 运行时视图 → [E1 时序图](/zh/types/e1-sequence-diagram)
- 逻辑数据模型 → [D1 实体关系图](/zh/types/d1-entity-relationship)
- 逻辑构件视图 → [C5 逻辑架构图](/zh/types/c5-logical-architecture)
- 逻辑组件图 → [C5 逻辑架构图](/zh/types/c5-logical-architecture)
- 逻辑网络图 → [G3 网络拓扑与连通视图](/zh/types/g3-network-topology)
- 逻辑视图 → [C5 逻辑架构图](/zh/types/c5-logical-architecture)
- 遥测流水线图 → [H2 可观测性视图](/zh/types/h2-observability-view)
- 部署架构图 → [G1 部署图](/zh/types/g1-deployment-diagram)
- 部署流水线图 → [G4 CI/CD 与部署流水线图](/zh/types/g4-delivery-pipeline)
- 部署视图 → [G1 部署图](/zh/types/g1-deployment-diagram)
- 集成架构图 → [C6 集成与接口图](/zh/types/c6-integration-interface)
- 需求分解结构 → [B3 功能树（功能分解）](/zh/types/b3-feature-tree)
- 需求树 → [B3 功能树（功能分解）](/zh/types/b3-feature-tree)
- 顺序图 → [E1 时序图](/zh/types/e1-sequence-diagram)
- 顾客旅程地图 → [A6 用户旅程图](/zh/types/a6-journey-map)
- 领域上下文图 → [C7 限界上下文映射（DDD）](/zh/types/c7-bounded-context-map)
- 领域模型 → [D1 实体关系图](/zh/types/d1-entity-relationship)
- 高层架构图 → [A7 概念架构图（方案概览）](/zh/types/a7-conceptual-architecture)
<!-- END GENERATED: aliases -->

## 全部类型

<!-- BEGIN GENERATED: catalogue -->
| 代码 | 类型 | 回答的问题 |
|---|---|---|
| [A1](/zh/types/a1-capability-map) | 业务能力图 | 组织“能做什么”（与由谁、用什么系统做无关）？哪些能力要加强，投资该往哪放？ |
| [A2](/zh/types/a2-value-stream) | 价值流（业务架构） | 从触发到交付价值，干系人经过哪些价值阶段？每个阶段由哪些能力支撑？ |
| [A3](/zh/types/a3-business-context) | 业务上下文图 | 业务或项目与哪些外部方打交道？彼此交换什么（货物、资金、信息、义务）？ |
| [A4](/zh/types/a4-scenario-matrix) | 业务场景矩阵（角色 × 活动） | 哪些角色参与哪些业务活动？每个场景在哪个版本支持？ |
| [A5](/zh/types/a5-bpmn-process) | 业务流程图（BPMN） | 一件业务如何从开始走到结束？每一步谁做、在哪分支、参与方之间传递什么？ |
| [A6](/zh/types/a6-journey-map) | 用户旅程图 | 某个角色在某个场景中经历哪些阶段？做什么、想什么、感受如何，机会点在哪？ |
| [A7](/zh/types/a7-conceptual-architecture) | 概念架构图（方案概览） | 方案由哪些大块组成？每一块在业务上起什么作用？ |
| [A8](/zh/types/a8-target-roadmap) | 目标架构与演进路线图 | 现状是什么、目标是什么、经过哪些可独立交付价值的过渡态、每一步交付什么？ |
| [A9](/zh/types/a9-lean-value-stream-map) | 精益价值流图（VSM） | 物料与信息如何在交付过程中流动？时间花在处理上还是等待上？ |
| [B1](/zh/types/b1-use-case-diagram) | 用例图 | 系统支持哪些用户目标（用例）？分别给哪些参与者？ |
| [B2](/zh/types/b2-user-story-map) | 用户故事地图 | 用户端到端要做哪些事？最小可用的第一个版本是什么？后续如何切片交付？ |
| [B3](/zh/types/b3-feature-tree) | 功能树（功能分解） | 产品包含哪些功能？拆到可估算的哪一层？优先级如何？ |
| [B4](/zh/types/b4-scope-diagram) | 范围图 | 这一期做什么、不做什么？与哪些外部方对接？ |
| [C1](/zh/types/c1-application-landscape) | 应用全景图 | 企业或产品线有哪些应用？各归谁、处于什么状态、如何互相依赖？ |
| [C2](/zh/types/c2-system-context) | 系统上下文图（C4 模型第 1 层） | 我们的软件系统是什么？谁在用？依赖哪些外部系统？ |
| [C3](/zh/types/c3-container-diagram) | 容器图（C4 模型第 2 层） | 系统由哪些独立运行的应用和数据存储组成？各用什么技术？如何通信？ |
| [C4](/zh/types/c4-component-diagram) | 组件图（C4 模型第 3 层） | 某个容器内部有哪些组件？各自负责什么？谁调用谁？ |
| [C5](/zh/types/c5-logical-architecture) | 逻辑架构图 | 只从职责看、不涉及技术选型，系统要有哪些模块和接口？ |
| [C6](/zh/types/c6-integration-interface) | 集成与接口图 | 系统之间有哪些接口？用什么集成方式、方向、协议、认证方式和失败语义？ |
| [C7](/zh/types/c7-bounded-context-map) | 限界上下文映射（DDD） | 领域中有哪些模型边界？它们之间用什么关系模式连接？ |
| [C8](/zh/types/c8-layered-architecture) | 分层架构图 | 代码分几层？每层负责什么？允许哪些依赖方向？ |
| [D1](/zh/types/d1-entity-relationship) | 实体关系图 | 系统管理哪些业务对象？它们之间是什么关系、基数如何？ |
| [D2](/zh/types/d2-data-flow-diagram) | 数据流图（DFD） | 数据从哪来、经过哪些加工、存在哪、流到哪？ |
| [D3](/zh/types/d3-data-lineage-ownership) | 数据血缘与归属图 | 某份数据或结果从哪里来、又派生出什么？由谁负责？ |
| [E1](/zh/types/e1-sequence-diagram) | 时序图 | 在一个场景中，各参与者按什么顺序交换哪些消息？ |
| [E2](/zh/types/e2-activity-flowchart) | 活动图 / 流程图 | 一段处理逻辑由哪些步骤、判断和并行分支组成？ |
| [E3](/zh/types/e3-state-machine) | 状态机图 | 一个对象有哪些状态？什么事件使它迁移？哪些迁移不允许？ |
| [E4](/zh/types/e4-swimlane-cross-functional) | 泳道流程图（跨职能流程图） | 一个流程中，每一步由哪个角色或系统完成？在哪里交接？ |
| [F1](/zh/types/f1-authentication-authorization-flow) | 认证与授权流程图 | 谁向谁证明了什么身份？传递了什么授权？访问在哪里被真正允许或拒绝？ |
| [F2](/zh/types/f2-threat-model-data-flow) | 威胁建模数据流图（含信任边界） | 哪些数据跨越了权限或信任的变化？安全属性可能在哪里失效？ |
| [F3](/zh/types/f3-access-control-model) | 访问控制模型 | 在什么规则下，主体可以在什么范围内对资源执行什么操作？ |
| [G1](/zh/types/g1-deployment-diagram) | 部署图 | 软件实例运行在哪里、哪个环境？部署位置如何满足运行要求？ |
| [G2](/zh/types/g2-cloud-infrastructure-architecture) | 云基础设施架构图 | 用哪些云服务承载工作负载？哪些故障边界与权衡使这种安排满足需求？ |
| [G3](/zh/types/g3-network-topology) | 网络拓扑与连通视图 | 什么能与什么通信？经过哪些路径与控制？正常与故障时分别如何？ |
| [G4](/zh/types/g4-delivery-pipeline) | CI/CD 与部署流水线图 | 一次变更如何成为可信的发布？每次晋级依据什么证据？失败时怎么办？ |
| [H1](/zh/types/h1-raci-matrix) | RACI 责任矩阵 | 每项活动或决策，谁执行（R）、谁最终负责（A）、谁被咨询（C）、谁被告知（I）？ |
| [H2](/zh/types/h2-observability-view) | 可观测性视图 | 哪些证据反映服务对用户的表现？它如何到达分析与告警？问题如何送达能处理的人？ |
| [H3](/zh/types/h3-stakeholder-map) | 干系人地图（权力-利益矩阵） | 谁能影响或受影响于这个项目？各自权力与关注度如何？应如何沟通？ |
| [I1](/zh/types/i1-four-plus-one) | 4+1 视图模型 | 不同干系人如何通过各自关心的视图理解同一套架构，并保持视图之间一致？ |
| [I2](/zh/types/i2-archimate-layered-view) | ArchiMate 分层视图 | 业务、应用与技术如何互相支撑？一处变化会影响哪些部分？ |
<!-- END GENERATED: catalogue -->
