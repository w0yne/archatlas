---
code: G3
slug: network-topology
family: G
names:
  en: Network topology and connectivity view
  zh: 网络拓扑与连通视图
  aliases:
    en: [network topology diagram, network diagram, logical network diagram, VPC topology, connectivity view, physical network diagram, routing view, VPC or VNet topology, hybrid connectivity diagram]
    zh: [网络拓扑图, 网络架构图, 逻辑网络图, 网络连通图, 物理网络图, 网络连通视图, 路由视图, 混合网络连接图]
question: 在正常和故障情况下，什么可以与什么通信，经由哪些路径和控制？
audiences: [operations, security, architects]
levels: [physical]
phases: [design, operate]
scope: 一种声明的视图（物理链路、逻辑邻接或一条流量路径），覆盖重要的网络、网段、网关和端点
formal: {kind: convention, ref: 'No graphical standard. RFC 1918, RFC 5737 and RFC 3849 govern addressing and documentation ranges; provider networking documentation defines platform semantics'}
neighbours: [F2, G1, G2]
status: draft
translationOf: en/types/G3-network-topology.md
sourceRev: 88db750
reviewed: false
---

# 网络拓扑图（Network Topology and Connectivity View）

> 一张关于网络、网段和网关的视图，说明哪些部分相连、某条流量走哪条路径，且绝不超出配置所能支撑的范围。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 什么可以与什么通信，经由哪些路径和控制，链路或可用区故障时会发生什么？
- **视点：** 连通性、隔离和运维关注点。这个视图可以是物理的（线缆、站点、设备）、逻辑的（网络与邻接关系），或者是单条流量路径；每种都需要自己的图例。它是一个非正式的图类，不限于云，也不是单一的表示法。
- **深层含义：** 逻辑连通不等于物理布线，也不等于有权使用某个应用。一条对等连接（peering）线可能只提供有限的邻接；路由、转发和过滤决定了可用路径。可达并不能证明用户已获授权。
- **不包含：** 业务逻辑、应用内部细节和完整的规则表；这些属于证据表。
- **本站采用的定义：** *拓扑*（topology）展示哪些元素相连；*流量路径*（traffic flow）展示某类流量所走的路径。私有 IPv4 地址遵循 RFC 1918，公开示例则使用 RFC 5737（IPv4）和 RFC 3849（IPv6）规定的文档地址段 [1][2][3]。配置体现意图；观察到的行为需要另行提供经授权的证据。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 网络与安全工程师、平台运维人员、架构师，以及需要接入该环境的合作伙伴。
- **典型场景：**
  1. 在网店总部与其云网络之间开通专线。
  2. 设计店面、后台和数据网络之间的中心辐射（hub-and-spoke）或对等连接。
  3. 为调用支付服务商的服务设计私有出站路径。
  4. 排查聊天机器人服务为何无法访问订单 API。
  5. 评审可用区之间的分段与故障切换。
- **不适用的情况：** 在没有证据的情况下声称应用权限、服务健康状况或实测流量，或用布线图回答云路由问题。
- **与相邻类型的区别：**
  - 问题是哪些软件运行在哪里时，选 **G1**。
  - 云服务的编排及其取舍，选 **G2**。
  - 问题是信任边界和威胁时，选 **F2**。
  - 随时间展开的请求顺序，选 **E1**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 非正式。在标题中声明视图类型：物理、逻辑或流量路径。
- **必备元素：**
  - 范围和视图类型。
  - 重要的网络或网段、网关和端点。
  - 连接，以及解释所选路径所需的路由、转发或过滤边界。
  - 方向语义和图例。
- **线条：** 在拓扑视图中，线条表示邻接，不一定意味着数据包方向。在流量路径视图中，要说明箭头表示谁发起连接、路由路径还是双向交换。单向的请求箭头不能暗示无法返回响应。应在拓扑上叠加一条编号的示例路径，而不是把两者混在一起。
- **可选：** 脱敏后的 CIDR、VLAN 或 VRF、端口和协议、路由表引用、DNS、地址转换、对等连接或中转网关、VPN 或专用线路、IPv6 出站、故障域、检测设备。
- **注意：** “公有、私有和数据子网”并不是必须遵循的三分法；仅凭公有子网的路由也不能证明某个工作负载拥有公网地址或开放端口 [4]。控制平面的中心不一定是数据包中转网络 [6]。
- **文字预算：** 网络名称，以及在安全的前提下标注其文档地址段 CIDR；规则放在表格中。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **展示真实路径，** 在重要时包括回程路由、DNS 和出站，而不只是入站箭头 [4][5][6]。
2. **不要从对等连接线推断传递可达性。** 核查云服务商的对等连接和中转行为；Google Cloud 的中心辐射页面明确指出 VPC 对等连接不具有传递性 [6]。
3. **把 NAT 视为众多机制之一。** 私有端点、IPv6 出站和有意隔离的网络需要不同的路径 [4][7]。
4. **把事实分开：** 拓扑邻接、防火墙放行和观察到的流量是三件不同的事。
5. **在公开示例中使用文档地址段，** 默认绝不公开真实的地址规划或规则清单 [2][3]。

### 反模式
1. **为简化路由而凭空画一条直连线；** 应通过选择一条路径来简化。
2. **把对等连接画成全网状，** 却没有说明中转机制。
3. **没有含义的箭头：** 邻接、请求和流量用同一种样式混画。
4. **跨云服务商照搬特定云的边界**（把 VPC 图套用到另一家云服务商的网络模型上）。
5. **把被放行的路径解读为健康的服务：** 一条防火墙规则并不能证明目标端在监听。

## 范例 {#exemplars}
<!-- skill: omit -->
- [AWS: VPC with servers in private subnets and NAT](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html) — 将图与路由表关联，并把互联网出站与私有服务端点路径分开。AWS 文档。
- [Azure: Hub-spoke network topology](https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke) — 对网络分组，并比较连接辐射网络的多种方式，而不是把所有对等连接视为等同。
- [Google Cloud: Hub-and-spoke network architecture](https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology) — 比较 Network Connectivity Center、对等连接和 VPN，并区分控制平面中心与数据平面中转网络。
- 仅提供链接；如需借鉴思路，请重新设计地址和布局，注明概念出处，并查看各厂商的插图使用条款。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 先确定视图类型：物理链路、逻辑连通或单条流量路径。写进标题，例如“网店网络：逻辑，预期”。
2. 盘点范围（站点、账号、网络）、网段、网关以及问题所需的端点；其余省略。
3. 阅读路由、过滤和转发声明；将声明与观察分开，并说明画的是哪一种。
4. 布局：用嵌套边界表示网络和网段；只有当拓扑确实是这种形状时才采用中心辐射或分层布局。外部网络（互联网、办公室、合作伙伴）放在外侧的左边或上方。
5. 线条：连通性用一种样式；对流量路径，添加编号箭头并说明谁发起。当路径依赖响应、DNS 和出站时，把它们画出来。
6. 文字：简短名称，必要时加文档地址段 CIDR；端口和规则放在附表中。
7. 颜色：内部用中性色，所解释的路径用一种强调色，外部网络用不同样式；不要只靠颜色区分允许与拒绝。

**自检清单**
- [ ] 视图已声明为物理、逻辑或流量路径。
- [ ] 每条线或箭头在图例中都有明确含义。
- [ ] 每条所示路径背后的路由、过滤和转发约束都有证据。
- [ ] 当路径依赖回程、DNS 和出站时，已对其加以考虑。
- [ ] 没有在缺乏机制的情况下把对等连接画成或描述为可传递的。
- [ ] 没有仅凭子网名称推断 NAT 或公网暴露。
- [ ] 边界采用所述云服务商或协议的语义。
- [ ] 地址可以安全公开（文档地址段），并已说明假设。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **网络声明：** Terraform、CloudFormation 或 CDK 中的网络、子网、路由表及其关联、对等连接和中转挂载。
- **控制：** 安全组、网络 ACL、防火墙策略、Kubernetes NetworkPolicy、Ingress 和 Service 对象、DNS 配置。
- **局限：** 仅凭 Kubernetes 名称无法确定底层路由。
- **必须由人提供：** 物理链路、运营商线路、真实的地址规划、观察到的流量、经验证的故障切换。
- 状态文件和防火墙导出可能是敏感的；请索取经脱敏和授权的证据，绝不通过扫描来探查。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 物理链路、逻辑连通还是单条请求路径？（逻辑连通）
2. 哪些站点、网络、云服务商和环境在范围内？（办公室、云网络、一家支付服务商）
3. 哪些入站、出站、私有连接和检测需求重要？（到支付服务商的私有出站）
4. 可以展示真实的地址和规则吗？（不可以，仅用文档地址段）
5. 这是配置意图，还是经验证的运行拓扑？（意图）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/G3.json` · 布局模板：`nested` · 网络和网段成为嵌套的 `boundary` 分组，网关和端点成为 `component` 节点，连通性使用 `assoc` 边（`dir` 为 `--`），流量路径使用带 `step` 编号的 `call` 或 `data` 边；CIDR 写在 `sub` 中，视图类型写在标题中。

## 来源 {#sources}
<!-- skill: omit -->
1. IETF, RFC 1918, "Address Allocation for Private Internets" — https://www.rfc-editor.org/rfc/rfc1918 — 访问于 2026-10-14
2. IETF, RFC 5737, "IPv4 Address Blocks Reserved for Documentation" — https://www.rfc-editor.org/rfc/rfc5737 — 访问于 2026-10-14
3. IETF, RFC 3849, "IPv6 Address Prefix Reserved for Documentation" — https://www.rfc-editor.org/rfc/rfc3849 — 访问于 2026-10-14
4. AWS, "Example: VPC with servers in private subnets and NAT" — https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html — 访问于 2026-10-14
5. Microsoft, "Hub-spoke network topology in Azure" — https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke — 访问于 2026-10-14
6. Google Cloud, "Hub-and-spoke network architecture" — https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology — 访问于 2026-10-14
7. AWS, "NAT gateways" — https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![G3 · 企业服务助手](/samples/ai-service-assistant/G3/zh/diagram.svg)
*逻辑可达视图；中间路由、DNS、TLS/443、私有端点、逐 AZ NAT 和 SG/NACL 返回路径见 AS-network。虚构地址及规则不是实际部署观测。*

[SVG](/samples/ai-service-assistant/G3/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/G3/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

[历史 shop 回归样例](/samples/G3-network-topology.svg) · [全部29幅视图](/zh/use/ai-service-assistant) · [示意假设](/zh/use/ai-service-assistant-assumptions).
