---
code: G1
slug: deployment-diagram
family: G
names:
  en: Deployment Diagram
  zh: 部署图
  aliases:
    en: [deployment view, software-to-infrastructure mapping, runtime infrastructure view, physical architecture diagram]
    zh: [部署视图, 软件与基础设施映射图, 物理架构图]
question: "软件实例和制品运行在哪里，这种部署位置如何支撑容量、故障切换和归属等运维需求？"
audiences: [开发人员, 平台与基础设施工程师, 运维人员, 架构师, 安全评审人员]
level: physical
phases: [design, delivery, operations, review]
scope: "一个具名环境（例如生产环境），展示承载节点以及部署在其上的软件实例"
formal:
  kind: standard
  ref: "OMG UML 2.5.1 Deployments (nodes, execution environments, artifacts, deployment); C4 model deployment diagram as a pragmatic variant; arc42 section 7 for documentation"
neighbours: [C3, G2, G3, G4, E1]
status: draft
translationOf: en/types/G1-deployment-diagram.md
sourceRev: 72ec5c8
reviewed: false
---

# 部署图（Deployment Diagram）

> 针对一个环境的图：把软件实例映射到承载它们的节点上，只保留在运维上有意义的连接。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 每个软件部分运行在哪里，这种部署位置对扩缩容、故障、归属和地理位置意味着什么？
- **视点：** 架构描述意义上的部署视图或运维视图（ISO/IEC/IEEE 42010，仅公开范围部分 [6]）。UML 2.5.1 定义了正式元素（节点、设备、执行环境、制品、部署关系）[1]。C4 model 提供了一种务实的变体，把软件系统和容器的*实例*映射到一个环境中的部署节点上；它是一种辅助图，而不是第五个缩放层级 [2]。arc42 把部署（第 7 节）与运行时行为（第 6 节）分开 [3]。
- **深层含义：** 这是一种分配视图。静态模型中的逻辑职责落实到执行基础设施上，而部署位置会带来相应后果。C4 的"容器"是可部署的软件构件；Docker 容器只是运行它的一种方式。
- **不包含：** 方法调用、源文件、业务旅程、完整的网络规则集（G3）以及云服务的取舍（G2）。
- **本站采用的定义：** *部署节点*（deployment node）是承载软件的任何事物：设备、虚拟机、托管平台或嵌套的执行环境 [1][2]。它不一定是物理服务器。"部署"指分配，而不是随时间变化的行为。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 开发人员、平台工程师、运维人员、架构师和安全评审人员。
- **典型场景：**
  1. 网上商城生产环境的部署就绪评审。
  2. 将逻辑服务落地到托管容器平台上。
  3. 发现共享的故障域（两个"副本"在同一台主机或同一块磁盘上）。
  4. 为订单数据库规划副本和故障切换。
  5. 在云服务旁边布置门店设备或边缘缓存。
- **不适用的情况：** 解释客户旅程（使用 E1 或 A 类视图），或在没有复制和恢复行为证据的情况下声称具备灾难恢复能力。
- **与相邻图类的区别：**
  - 逻辑软件容器，选 **C3**；G1 在此基础上补充它们运行在哪里。
  - 问题是哪些云服务及其取舍适合该工作负载时，选 **G2**。
  - 问题是路由、分段和可达性时，选 **G3**。
  - 变更如何到达这个环境，选 **G4**。
  - 随时间变化的行为，选 **E1**（或 arc42 运行时视图）。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** UML 2.5.1 是正式的；大多数实际图是约定画法。不要在任意方框上加 UML 构造型（stereotype）并暗示符合规范 [1]。
- **必备元素：**
  - 环境名称和范围，以及是现状还是提议。
  - 承载节点，以及嵌套其中的软件实例或制品。
  - 清晰的包含（承载）关系，与依赖或通信区分开。
  - 有实质意义的通信路径，以及图例。
- **UML 方案：** 节点可以特化为设备或执行环境；制品（artifact）是可部署的信息，可以体现（manifest）软件元素。节点之间的通信路径不是方法调用，也不是带时序的消息 [1]。
- **C4 方案：** 区分部署节点、基础设施节点（负载均衡器、DNS、防火墙）和软件或容器实例；用嵌套表示承载；实例命名与逻辑模型保持一致 [2]。
- **相关时可选：** 副本数或自动扩缩容范围、可用区或区域边界、协议、资源限制、镜像版本或摘要（digest）、健康检查、复制和故障切换箭头。
- **注意：** 托管或无服务器平台不一定要有固定副本数；没有部署位置证据时，"两个副本"不能暗示分布在两个可用区。
- **文字预算：** 节点名加技术（约 2–4 个词）；实例用简短的角色名；只在运维上重要时才标端口。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **从逻辑模型出发**，把其中的单元明确映射到基础设施上 [2][3]；一组没有软件分配的云图标不是部署视图。
2. **说明数字的含义：** 是声明的定义、期望数量、观察到的实例，还是示意性容量。附上引用版本和日期，不要把声明称为"线上实况"。
3. **对复杂环境使用层次结构**，并把理由写在相邻的文字中，而不是在节点里写成段落 [3]。
4. **约束实例间的连线。** 同一服务有多个实例时，只连接真正通信的那几对；避免全连接 [4][5]。
5. **根据部署位置证据展示故障域**（可用区、主机、共享存储），而不是靠重复的方框。

### 反模式
1. **云图标上没有任何软件。**
2. **把重复的方框当作高可用**，而存储、控制平面或调度其实是单点。
3. **在某服务的所有实例之间凭空画连接** [4]。
4. **在一张图中混合多个环境**（开发、预发布和生产），却没有清晰的图例。
5. **总是画灾难恢复。** 只有评审需要时才纳入；否则链接到单独的视图并说明范围。

## 范例 {#exemplars}
<!-- skill: omit -->
- [C4 model: Deployment diagram](https://c4model.com/diagrams/deployment) — 嵌套节点、基础设施节点和图例，附若干完整示例。网站内容；复用图稿前请查看其许可。
- [Structurizr DSL cookbook: Deployment view](https://docs.structurizr.com/dsl/cookbook/deployment-view/) — 由文本模型生成的小型环境，因此图可以重现。
- [Structurizr DSL cookbook: Deployment groups](https://docs.structurizr.com/dsl/cookbook/deployment-groups/) — 对比错误的跨实例连线与受约束的连线。
- [arc42 section 7: Deployment view](https://docs.arc42.org/section-7/) — 将一张图与理由说明和映射表配套，而不是一张过载的图。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 选定一个环境和一个证据引用（提交或日期）；两者都写进标题，例如"网上商城：生产环境，依据 ref X 的声明"。
2. 列出可运行单元（店面、订单服务、聊天机器人、数据库、队列）和承载声明；区分基础设施与软件。
3. 布局：嵌套容器，最外层是区域或站点，然后是可用区或集群，再是主机或平台，最后是实例。对等主机并排放置；通信路径保持短而局部。
4. 承载关系只用嵌套表示。通信画成箭头，在重要处标注协议；复制或故障切换使用不同线型。
5. 只有在有证据时才添加数量、范围和可用区；否则标为"示意"或省略。
6. 文字：每个节点和实例 2–4 个词；为线型以及"声明与观察"提供图例。
7. 颜色：中性填充，软件层用一种强调色，外部或托管节点使用不同样式。不要只用颜色来区分。

**自检清单**
- [ ] 标题中写明了环境以及是现状还是提议。
- [ ] 每个软件单元都位于某个承载节点内；未映射或外部的单元已说明。
- [ ] 承载（嵌套）与通信（箭头）在视觉上有区别。
- [ ] 数量有证据支撑、以范围表示，或标为示意。
- [ ] 可用区和故障域以部署位置证据为依据。
- [ ] 重复的实例之间没有凭空画出的全连接。
- [ ] 端口和协议只在重要处出现。
- [ ] 声明的基础设施没有被当作观察到的部署来展示。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **可运行单元：** Dockerfile、Compose 文件、Kubernetes Deployment、StatefulSet 和 Service、Helm 或 Kustomize 值文件、进程管理器单元、启动脚本。
- **基础设施：** Terraform、CloudFormation 或 CDK 资源，自动扩缩容和部署位置规则，以及各环境的变量文件。
- **规则：** 一个目录不是可部署单元，导入的 SDK 也不是已部署的服务。
- **必须由人或平台提供：** 实际的云配置、外部管理的资源、真实的副本数和可用区分布。
- 绝不要为了画图而执行基础设施 apply 或读取含密钥的状态；将结果标为"声明"。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 应展示哪个环境或变体？（生产环境）
2. 哪些软件单元和归属边界重要？（商城自有服务；托管服务作为外部节点）
3. 数量和部署位置是当前观察、声明还是目标？（声明，并标出 ref）
4. 关注点是部署、容量、故障切换还是运维交接？（部署和故障切换）
5. 灾难恢复放在这里还是单独的视图？（单独的视图，并加链接）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/G1.json` · 布局模板：`nested` · 承载节点成为嵌套的 `boundary` 分组（区域、集群、主机），软件实例成为其中的 `primary` 节点，托管或外部节点使用 `external` 样式，通信成为带协议标签的 `call` 或 `data` 边；`evidence` 记录是声明还是观察。

## 来源 {#sources}
<!-- skill: omit -->
1. OMG, *Unified Modeling Language (UML) 2.5.1* (December 2017), Deployments — https://www.omg.org/spec/UML/2.5.1/ (PDF: https://www.omg.org/spec/UML/2.5.1/PDF) — 访问于 2026-10-14
2. C4 model, "Deployment diagram"（以及图类总览，其中将它列为辅助图之一） — https://c4model.com/diagrams/deployment — 访问于 2026-10-14
3. arc42, "Section 7: Deployment view" and "Section 6: Runtime view" — https://docs.arc42.org/section-7/ ; https://docs.arc42.org/section-6/ — 访问于 2026-10-14
4. Structurizr, "Deployment groups" — https://docs.structurizr.com/dsl/cookbook/deployment-groups/ — 访问于 2026-10-14
5. Structurizr, "Deployment view" — https://docs.structurizr.com/dsl/cookbook/deployment-view/ — 访问于 2026-10-14
6. ISO/IEC/IEEE 42010:2022，仅公开范围部分；页面返回 HTTP 403，未审阅全文 — https://www.iso.org/standard/74393.html — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![G1 示例：网上商城生产环境部署，包含负载均衡器、承载店面、订单服务和聊天机器人实例的容器平台，以及带副本的托管数据库](/samples/G1-deployment-diagram.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
