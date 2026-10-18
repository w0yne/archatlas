---
title: 企业服务助手：29幅架构视图
sidebar: false
aside: false
translationOf: en/use/ai-service-assistant.md
sourceRev: 7002b1114ff60c6a028194c8376c71eee2b9d52d
reviewed: false
---

# 企业服务助手：29幅架构视图

25个核心视图与4个具名变体，每种语言29幅原创手工 SVG。所有实体、行为及参数均来源于同一虚构场景；补充参数明确为示意假设，不是实施或实测结果。

[场景假设与规则](/zh/use/ai-service-assistant-assumptions) · [Manifest](/samples/ai-service-assistant/manifest.json) · [词表](/samples/ai-service-assistant/glossary.json)

<section class="sample-view" id="view-a1">

## A1 · 业务能力图

![A1 · 企业服务助手](/samples/ai-service-assistant/A1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/A1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/A1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

组织“能做什么”（与由谁、用什么系统做无关）？哪些能力要加强，投资该往哪放？

<section class="sample-view" id="view-a2">

## A2 · 价值流（业务架构）

![A2 · 企业服务助手](/samples/ai-service-assistant/A2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/A2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/A2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

从触发到交付价值，干系人经过哪些价值阶段？每个阶段由哪些能力支撑？

<section class="sample-view" id="view-a5">

## A5 · 业务流程图（BPMN）

![A5 · 企业服务助手](/samples/ai-service-assistant/A5/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/A5/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/A5/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

一件业务如何从开始走到结束？每一步谁做、在哪分支、参与方之间传递什么？

<section class="sample-view" id="view-a6">

## A6 · 用户旅程图

![A6 · 企业服务助手](/samples/ai-service-assistant/A6/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/A6/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/A6/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

人物画像、情绪与改进机会是示意假设，不是用户调研。现有管理员/运维角色负责建议改进，不因此获得额外内容权限。

<section class="sample-view" id="view-a8">

## A8 · 目标架构与演进路线图

![A8 · 企业服务助手](/samples/ai-service-assistant/A8/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/A8/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/A8/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

只读回答、审批写入及评测门禁是示意过渡稳定态，不是已承诺日期。每个工作包仅引入下一稳定态所需能力。

<section class="sample-view" id="view-b2">

## B2 · 用户故事地图

![B2 · 企业服务助手](/samples/ai-service-assistant/B2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/B2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/B2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

用户端到端要做哪些事？最小可用的第一个版本是什么？后续如何切片交付？

<section class="sample-view" id="view-c1">

## C1 · 应用全景图

![C1 · 企业服务助手](/samples/ai-service-assistant/C1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

企业或产品线有哪些应用？各归谁、处于什么状态、如何互相依赖？

<section class="sample-view" id="view-c2">

## C2 · 系统上下文图（C4 模型第 1 层）

![C2 · 企业服务助手](/samples/ai-service-assistant/C2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

我们的软件系统是什么？谁在用？依赖哪些外部系统？

<section class="sample-view" id="view-c3">

## C3 · 容器图（C4 模型第 2 层）

![C3 · 企业服务助手](/samples/ai-service-assistant/C3/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

六个运行单元、五个存储/队列及模型依赖。API 是任务唯一生产者；工作进程轮询、读取授权源版本并创建嵌入。保留原节点与边标识，并补上两条依赖。

<section class="sample-view" id="view-c4">

## C4 · 组件图（C4 模型第 3 层）

![C4 · 企业服务助手](/samples/ai-service-assistant/C4/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C4/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C4/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

P-plan、P-retrieve、P-compose 投影为 C-agent 内无序号的逻辑模块，不新增运行服务。模块名与职责是示意假设，不是源码观测。

<section class="sample-view" id="view-c5">

## C5 · 逻辑架构图

![C5 · 企业服务助手](/samples/ai-service-assistant/C5/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C5/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C5/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

只从职责看、不涉及技术选型，系统要有哪些模块和接口？

<section class="sample-view" id="view-c6">

## C6 · 集成与接口图

![C6 · 企业服务助手](/samples/ai-service-assistant/C6/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C6/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C6/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

接口认证、生产/消费方向、有界重试、归属和容量见 AS-interfaces 示意契约。队列由工作进程轮询，不是代理主动推送。

<section class="sample-view" id="view-c7">

## C7 · 限界上下文映射（DDD）

![C7 · 企业服务助手](/samples/ai-service-assistant/C7/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C7/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C7/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

各具名系统被视为不透明限界上下文，配有示意团队/模型契约。DDD ACL 指防腐层，文档 ACL 指访问控制列表；CF 仅指协议遵循，不接受模型输出授予权限。

<section class="sample-view" id="view-d1">

## D1 · 实体关系图

![D1 · 企业服务助手](/samples/ai-service-assistant/D1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/D1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/D1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

逻辑实体子集，非完整 DDL。租户记录 PK/FK 含租户范围；审批除主体、工具、hash、有效期外还绑定幂等元组。消息/引用仍属于对话聚合。

<section class="sample-view" id="view-d2">

## D2 · 数据流图（DFD）

![D2 · 企业服务助手](/samples/ai-service-assistant/D2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/D2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/D2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

检索前明确执行 tenant/ACL 过滤，打开引用时再次核对当前权限。此逻辑 DFD 聚焦知识回答，工单写入与评测另图表达。

<section class="sample-view" id="view-d3">

## D3 · 数据血缘与归属图

![D3 · 企业服务助手](/samples/ai-service-assistant/D3/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/D3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/D3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

AS-data 明确数据管理责任、技术保管及租户保密/去标识分类。数据归属不等于读取授权，派生分块保留源 ACL 限制。

<section class="sample-view" id="view-e1">

## E1 · 时序图

![E1 · 企业服务助手](/samples/ai-service-assistant/E1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/E1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/E1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

在一个场景中，各参与者按什么顺序交换哪些消息？

<section class="sample-view" id="view-e2">

## E2 · 活动图 / 流程图

![E2 · 企业服务助手](/samples/ai-service-assistant/E2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/E2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/E2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

UML 活动：单一起点、有效/否则判断与具名结果。审批、当前权限及幂等执行分别表达；超时不明按 AS-request 进行按键对账。

<section class="sample-view" id="view-e3">

## E3 · 状态机图

![E3 · 企业服务助手](/samples/ai-service-assistant/E3/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/E3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/E3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

DS-app 中的单个请求：未审批、已审批、执行中、未知、已记录、拒绝及关闭。有界对账后仍未知则保持挂起，不授权重新写入。

<section class="sample-view" id="view-e4">

## E4 · 泳道流程图（跨职能流程图）

![E4 · 企业服务助手](/samples/ai-service-assistant/E4/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/E4/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/E4/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

一个流程中，每一步由哪个角色或系统完成？在哪里交接？

<section class="sample-view" id="view-f1">

## F1 · 认证与授权流程图

![F1 · 企业服务助手](/samples/ai-service-assistant/F1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/F1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/F1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

交换请求为允许/拒绝分支共有的前提；Agent 是认证后的交换客户端。工具证明绑定 issuer、audience、subject、actor、tenant、scopes；核验不能代替当前授权，AS 委托支持是实施前提。

<section class="sample-view" id="view-f2">

## F2 · 威胁建模数据流图（含信任边界）

![F2 · 企业服务助手](/samples/ai-service-assistant/F2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/F2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/F2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

DF 标识将数据流对应到威胁假设，不是消息顺序。DF-6 抽象经 Agent 传递证明（F1），DF-4 经 BFF 读取当前审批；拟议控制仍需实施验证。

<section class="sample-view" id="view-f3">

## F3 · 访问控制模型

![F3 · 企业服务助手](/samples/ai-service-assistant/F3/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/F3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/F3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

显式授权取并集，再与当前租户/资源约束相交；策略拒绝优先。知识管理员读取须满足 ACL，运维权限不自动授予租户内容访问。

<section class="sample-view" id="view-g1-aws">

## G1-AWS · 云基础设施架构图

![G1-AWS · 企业服务助手](/samples/ai-service-assistant/G1-AWS/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/G1-AWS/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/G1-AWS/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

AWS 实现变体保持为 G1 首图。应用服务跨双 AZ；Aurora 托管存储跨三 AZ；OpenSearch 是双 AZ 区域感知而非 Standby。区域托管服务位于客户子网外，CloudFront 为全球服务。

<section class="sample-view" id="view-g1-generic">

## G1-generic · 部署与云架构图

![G1-generic · 企业服务助手](/samples/ai-service-assistant/G1-generic/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/G1-generic/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/G1-generic/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

对同一冻结部署进行供应商中立的软件承载分配，不另建架构，也不将 AWS 图改名复制。六个运行单元和五个存储保留标识，作为 G1 AWS 首图的补充。

<section class="sample-view" id="view-g3">

## G3 · 网络拓扑与连通视图

![G3 · 企业服务助手](/samples/ai-service-assistant/G3/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/G3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/G3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

逻辑可达视图；中间路由、DNS、TLS/443、私有端点、逐 AZ NAT 和 SG/NACL 返回路径见 AS-network。虚构地址及规则不是实际部署观测。

<section class="sample-view" id="view-g4">

## G4 · CI/CD 与部署流水线图

![G4 · 企业服务助手](/samples/ai-service-assistant/G4/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/G4/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/G4/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

版本化 prompt/模型包、不可变摘要、离线门禁、管理员审批及运维发布。同一制品经预发布及 5% 灰度晋级；恢复兼容配置指针，不自动回滚数据库。

<section class="sample-view" id="view-h1">

## H1 · RACI 责任矩阵

![H1 · 企业服务助手](/samples/ai-service-assistant/H1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/H1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/H1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

示意治理：每项活动设一个 A，至少一个 R。知识管理员对发布/恢复审批最终负责，运维执行受限工作流；问责职责不授予数据面权限。

<section class="sample-view" id="view-h2">

## H2 · 可观测性视图

![H2 · 企业服务助手](/samples/ai-service-assistant/H2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/H2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/H2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

导出前脱敏。示意 SLO、成本目标、有界传输、采样/保留及 CloudWatch→SNS→运维响应见 AS-observe，均非实测保证。

