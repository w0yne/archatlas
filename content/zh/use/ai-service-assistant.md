---
title: 企业服务助手：七幅视图
sidebar: false
aside: false
translationOf: en/use/ai-service-assistant.md
sourceRev: 4e718f136c12c2c4c1d5f2226ea103f63e35b600
reviewed: false
---

# 企业服务助手：七幅视图

虚构教学设计。每种语言七幅手工视图共用同一版本化事实源；这是文档候选，不是实施或性能验证。AWS 变体作为 G1 首图，独立供应商中立 G1 样例后续补充。[Manifest](/samples/ai-service-assistant/manifest.json)。

<section class="sample-view" id="view-c2">

## C2

![C2 · 企业服务助手](/samples/ai-service-assistant/C2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

一个自有系统及其直接邻居。箭头表示发起方到依赖方；此层不含协议或内部存储。人员是角色而非真实个人，三个租户均为合成数据。

<section class="sample-view" id="view-c3">

## C3

![C3 · 企业服务助手](/samples/ai-service-assistant/C3/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/C3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/C3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

聚焦内部容器：六个运行单元、五个存储/队列及外部模型依赖。身份、文档源、工单这三种外部接口见 C2/F1；摄取进程连接文档源，工具网关连接工单。Agent 内含逻辑模型网关，不是第七个服务。本图只画关键依赖：C-api 另负责批准反馈导出至 DS-eval，C-ingest 生产版本任务并消费 Q-ingest，C-eval 将经门禁的配置建议写入 DS-eval。检索与引用访问均检查当前 tenant/ACL。MCP 为 Model Context Protocol。

<section class="sample-view" id="view-e1">

## E1

![E1 · 企业服务助手](/samples/ai-service-assistant/E1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/E1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/E1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

员工只审批本人当前有权执行的操作。BFF 存储 tenant、主体、工具、规范参数 hash、有效期和幂等键。工具网关取得该绑定，并在写入前再次核对当前策略；拒绝、过期或参数改变的草稿不会进入工单系统。调用幂等连接器前先持久化执行意图，超时结果不明时按键对账。委托 token 的前提见 F1；最终结果经 BFF 返回界面，此处省略该返回跳。

<section class="sample-view" id="view-f1">

## F1

![F1 · 企业服务助手](/samples/ai-service-assistant/F1/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/F1/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/F1/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

本图是下游委托；前置登录由 BFF 使用授权码 + PKCE 完成，并核对 state 与 nonce。ID/access token 保留在服务端，浏览器仅持安全会话 cookie。AS 明确签发 agent 范围的主体 token，Agent 以 agent-client 身份认证并交换。工具 token 由 enterprise-as 签发给 mcp-tool-gateway，包含员工主体、agent actor、已验证 tenant、许可 scopes 与短有效期。先核验签名、issuer、audience 和有效期，再执行当前策略与审批检查。AS 委托能力与工单连接器 scopes 都是未验证的教学假设；不支持时须重设身份方案，不能转发 audience 不符的 token。实线是后通道请求，虚线是应答；浏览器重定向属于前置登录而非本图。

<section class="sample-view" id="view-g1-aws">

## G1-AWS

![G1-AWS · 企业服务助手](/samples/ai-service-assistant/G1-AWS/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/G1-AWS/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/G1-AWS/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

AWS 实现变体 G2，同时作为 G1 首图，仅维护这一幅拓扑。G1 核心画法仍供应商中立；独立通用样例排入 P2b。ALB 与每个 ECS 应用服务跨两个 AZ；C-ingest、C-eval 使用独立任务身份，调度至任一 AZ。Aurora 有跨 AZ 读节点，其托管存储跨三个 AZ。OpenSearch 使用双 AZ 区域感知与副本，不是 Multi-AZ with Standby。CloudFront 为全球服务；S3、SQS、Bedrock、KMS、CloudWatch、Secrets Manager 是客户子网外的区域托管服务。实施前核对模型可用性、配额与端点路由。取舍：托管 ECS 减少集群控制面维护；搜索索引增加运维成本；单区域降低复杂度，但不承诺区域灾备。图形均为原创通用形状，无厂商素材。

<section class="sample-view" id="view-d2">

## D2

![D2 · 企业服务助手](/samples/ai-service-assistant/D2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/D2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/D2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

知识回答功能的第 1 层分解，采用 Gane–Sarson 符号：圆角处理框、开口存储、矩形外部实体。箭头标数据而非控制步骤。P-ingest 属于 C-ingest；检索和生成属于 C-agent；引用授权属于 C-api。过滤权限来自已验证会话，不接受用户自选 tenant。源 ACL 随版本与分块传播，打开引用时再次检查当前策略。本图范围不含工单操作与评测闭环，不声称分解整个 C2 系统。输入是原文+ACL、员工问题+身份及模型草稿；输出是含依据的提示与已授权回答/引用，DS-app 接收审计记录。

<section class="sample-view" id="view-f2">

## F2

![F2 · 企业服务助手](/samples/ai-service-assistant/F2/zh/diagram.svg)

[SVG](/samples/ai-service-assistant/F2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/F2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

</section>

聚焦工单写入的威胁 DFD；DF 编号是引用标识，不是消息时序。TB-1 是不可信内容，TB-2 是已验证租户/审批权限，TB-3 是工具执行权限，工单系统在外部。DF-6 抽象经 Agent 传递的证明，不代表 AS 直接 HTTP 调用网关（见 F1）。DF-4 是经 BFF API 取得的逻辑当前审批记录。下表记录拟议控制与威胁假设，均未声称实现或验证。检索与引用路径也须租户隔离（D2）。

| 威胁 / 数据流 | 假设及影响 | 拟议应对 | 责任方 / 尚需验证 |
|---|---|---|---|
| T1 · DF-1 / TB-1 | 提示注入请求未授权工具 | 模型无授权权力；仅允许三种工具 | Agent 负责人 / 恶意文档测试 |
| T2 · DF-2–5 / TB-2 | 审批后篡改草稿或重放 | 绑定租户、主体、规范 hash、有效期和幂等键；再次授权 | API 负责人 / hash、过期及租户拒绝测试 |
| T3 · DF-6 / TB-3 | 混淆代理使用错误 audience 或 actor | 核验 AS 签名、issuer、audience、actor、tenant、scopes；连接器前拒绝 | 身份负责人 / audience 及跨租户测试 |
| T4 · DF-7–8 | 超时导致重复写入 | 持久意图、连接器幂等及按键查询 | 工具负责人 / 超时对账测试 |
| T5 · DF-4 / DS-app | 运维或模型直接访问审批记录 | 受限服务身份、BFF 策略检查、审计与脱敏 | 平台负责人 / IAM 及日志审查 |

以上均为假设及拟议应对，**尚无验证证据**。

## 共享不变量

- **I-tenant**: 从已验证会话确定租户与主体。检索前执行当前 tenant/ACL 过滤，打开引用时再次核对当前权限；租户之间不共享内容。
- **I-approval**: 审批绑定租户、主体、工具、规范参数 SHA-256 hash、有效期与幂等键。审批是持久记录而非模型文本；执行前重新授权，拒绝过期、篡改或跨租户请求。
- **I-authority**: 模型输出、检索文档和 guardrails 均不授予权限。Guardrails 过滤内容，BFF 与网关的确定性检查执行权限控制。
- **I-delegation**: BFF 是机密 OIDC 客户端（授权码 + PKCE；verifier 保留在服务端）。Agent 服务是已认证的 token exchange 客户端。企业 AS 必须明确支持所需的受限委托（RFC 8693）；这是前提，不是任意 IdP 的通用能力。
- **I-tokens**: AS 签发 BFF access token（aud=application-api、sub=员工）及缩权的 agent 主体 token（aud=agent-service）。Agent 以 agent-client 身份认证，仅交换此有效主体 token；AS 签发工具 token：iss=enterprise-as、aud=mcp-tool-gateway、sub=员工、act=agent-client、tenant、许可 scopes 与短有效期。网关核验签名、issuer、audience、有效期、委托 actor、tenant 与当前策略；任一不符在工单调用前拒绝。工单使用独立受限连接器凭据，绝不转发模型或 BFF token。
- **I-idempotency**: 发送前持久化执行意图与幂等键。假设工单服务支持按该键幂等创建；超时结果不明时按键对账，绝不盲重试非幂等写入。
- **I-ingest**: 文档版本携带源 ACL；重试有界、失败进入 DLQ；完整索引的版本才可检索，撤权或删除同步失效检索与引用访问。
- **I-eval**: 反馈先存 DS-app。管理员批准去标识或合成数据导出至 DS-eval。离线 C-eval 使用评测专用身份及版本化 prompt/model/dataset，不可写生产工具；按质量、安全、延迟与 token 成本门禁晋级，不声称实测分数。
- **I-operator**: 运维默认只见服务健康与脱敏遥测，不获得租户内容权限。日志不含原始 token 与文档正文；管理变更审计且不绕过数据面检查。
- **I-bounds**: 仅三种工具：catalogue.lookup、ticket.read、ticket.create。写请求要求发起员工在当前权限内审批；无任意脚本、采购、自主退款或无限循环。
