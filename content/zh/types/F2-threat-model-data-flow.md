---
code: F2
slug: threat-model-data-flow
family: F
names:
  en: Threat-model data-flow diagram with trust boundaries
  zh: 威胁建模数据流图（含信任边界）
  aliases:
    en: [threat-model DFD, security data-flow diagram, trust boundary diagram, DFD with trust boundaries, STRIDE diagram, trust-boundary diagram]
    zh: [威胁建模数据流图, 安全数据流图, 信任边界图, 含信任边界的数据流图]
question: 哪些数据跨越了哪些权限变化或信任假设变化，安全属性可能在哪里失效？
audiences: [security, architects]
levels: [logical]
phases: [design]
scope: 一个功能或子系统，包括其资产、入口点和信任边界；关联一份独立的威胁登记表
formal: {kind: method, ref: Classic data-flow-diagram symbols plus security annotations; practice from the OWASP Threat Modeling Cheat Sheet and Microsoft's documented STRIDE approach. Not a universal graphical standard}
neighbours: [C3, C6, D2, F1, F3, G3]
status: draft
translationOf: en/types/F2-threat-model-data-flow.md
sourceRev: 7002b1114ff60c6a028194c8376c71eee2b9d52d
reviewed: false
---

# 威胁建模数据流图（Threat-Model Data-Flow Diagram）

**D2 的具名变体。** [进入数据流图（DFD） → F2](/zh/types/d2-data-flow-diagram#variant-f2)。此兼容页保留独立画法、检查项、原锚点和历史下载。

> 一种标出信任假设变化之处的数据流图，让团队能够针对每条数据流、每个存储和每条边界追问：可能出什么问题。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 哪些数据跨越了哪些权限变化或信任假设变化，安全属性可能在哪里失效？一条边界可以分隔组织、特权级别、租户、进程，或者同一网络中浏览器与服务器的权限。私有子网并不能证明其中的一切都可信 [1][4]。
- **不是完整的威胁模型：** 这张图对应的是系统建模这一步。威胁模型（threat model）还包括威胁识别、应对（缓解措施）和验证 [1][2]。这些内容放在关联的登记表中。
- **本站采用的定义：** *STRIDE*（仿冒、篡改、抵赖、信息泄露、拒绝服务、权限提升）是一种基于 DFD 的威胁识别方法；它既不是这张图的同义词，也不是它的必要条件。*信任边界图*（trust-boundary diagram）是一种更简单的相关视图，不含完整的数据流 [2][3]。
- **不包含：** 不触及所建模资产或安全属性的附带调用。不要仅仅因为某条内部数据流没有跨越已画出的边界就把它删掉；它可能承载敏感数据或特权操作 [1]。
- **定位：** 成熟的 DFD 符号加安全标注；图形本身没有 ISO 或 OMG 标准。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 安全工程师、架构师、开发人员、隐私专家、服务负责人。
- **典型场景：**
  1. 网店面向第三方分销商新开放的公共 API。
  2. 新增支付服务商的 webhook 或外部身份提供方。
  3. 多租户的上传与处理流程，例如商家商品图片导入。
  4. 托管边界或特权边界发生变化，例如把客服聊天机器人的订单查询迁移到独立服务。
- **不适用的情况：** 用作网络资产清单、渗透测试结果，或证明所有 STRIDE 威胁都已消除。
- **与相邻类型的区别：**
  - 不做信任分析的普通数据处理，选 **D2 数据流图**。
  - 逐步展示一次身份交换，选 **F1 认证与授权流程图**。
  - 权限规则，选 **F3 访问控制模型**。
  - 路由和连通性，选 **G3 网络拓扑**。
  - 这张 DFD 通常所依据的结构视图，选 **C3 容器图**。
  - 需要完整的接口清单时，选 **C6 集成与接口图**；其中的认证与数据分级列是这里信任边界分析的输入。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 非正式，但被广泛讲授。使用一套可辨认的 DFD 符号，或一份声明过的自定义图例 [1]-[3]。
- **必备元素：**
  - 范围说明和重要资产。
  - 外部实体（顾客、支付服务商）、加工（结账服务）、数据存储（订单数据库）。
  - 有方向、有名称的数据流（“卡令牌”“订单记录”）。
  - 信任边界（trust boundary），每条附一行含义说明。
  - 可关联到威胁和待解决问题的元素 ID 与数据流 ID。
- **箭头含义：** 表示具名数据的移动，而不是时间顺序、依赖、角色继承或缓解措施。当方向、载荷或特权不同时，把一条数据流拆成两条箭头。编号用于追溯，不一定表示顺序。
- **边界：** 嵌套的边界必须代表真实的嵌套权限。每个存储都要明确位于每条边界之内或之外。
- **可选：** 数据分级、协议、认证上下文、特权级别、威胁 ID、缓解措施状态。
- **关联登记表：** 元素或数据流 ID、威胁、影响、应对、负责人、验证证据。自动生成的威胁是待评审的假设，而不是已核实的结论 [2]。
- **文字预算：** 每个标签 1–4 个词；威胁描述放在登记表中，不写在箭头上。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **走完整个循环：** 对系统建模，识别可能出什么问题，决定应对措施，再验证这些措施。DFD 只完成了第一步 [1][2]。
2. **在安全区分需要的地方进行分解。** 优先采用一张上下文视图加若干聚焦的子系统 DFD，而不是一张巨大的基础设施图 [1]。
3. **按信任假设画边界。** 并非每个区域、命名空间或子网都值得画一条边界。
4. **把 STRIDE 当作逐元素的提问提示，** 而不是在每个形状上贴六个装饰性徽标；相关威胁取决于元素类型和场景 [3]。
5. **区分已观察到的控制、提议的控制和未核实的假设。** 公开展示未知项，而不是用“安全区”标签把它们掩盖起来。

### 反模式
1. **把边界画在整个系统外围**或每个云组件外围，什么也说明不了。
2. **无标签的箭头**（没有数据名称），或把箭头用于表示顺序或依赖。
3. **机械地省略内部数据流**，只因为它们没有跨越边界；或者为了让图面整洁而删掉拒绝路径和滥用路径，而在安全视图里它们往往正是重点。
4. **把威胁描述塞满图面**，使图难以阅读且无人负责。
5. **把这张图当作已完成的评估来展示，** 或把提议的控制画得像已经落实。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Microsoft Threat Modeling Tool: getting started](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started) — 一张带权限边界的小型 DFD，随后是分析和缓解措施。
- [Microsoft: Uncover Security Design Flaws Using the STRIDE Approach](https://learn.microsoft.com/en-us/archive/msdn-magazine/2006/november/uncover-security-design-flaws-using-the-stride-approach) — 分解与逐元素推理的完整图例；这是一篇历史方法文章，不是当前工具的操作指南。
- [OWASP Threat Dragon: getting started](https://www.threatdragon.com/docs/usage/getting-started.html) — 可编辑的示例模型，把图、元素详情和威胁记录关联起来。旧文档路径已迁移，请使用此链接。
- 仅提供链接，未复制任何图稿。改编具体示例模型前请查看其许可；工具本身的许可并不决定示例的使用权。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 说明资产、范围以及纳入范围的攻击者假设；在标题中写明范围和状态（“网店结账：数据流与信任边界，提议”）。
2. 动笔之前，先盘点入口点和出口点、加工、存储以及权限变化。
3. 画出能保留这些区分的最小模型；在每条箭头上写明其载荷名称。
4. 布局：外部实体放在外侧边缘，加工居中，存储在底部；数据流方向从左到右。边界用虚线框表示，并附简短标签说明信任变化。
5. 检查每一处边界穿越和每条重要的内部数据流；逐一保留或说明理由。
6. 分配稳定的 ID（EE-1、P-1、DS-1、DF-1 这类形式，避免与目录编号混淆），并另以表格输出威胁/缓解措施登记表。
7. 颜色：中性填充；边界用一种强调色；仅为“提议 / 未核实”再加一种标记。符号取自同一套 DFD 符号集，并附图例。
8. 与系统专家一起评审；对缺口加以标注，而不是猜测。

**自检清单**
- [ ] 已说明范围、资产和假设。
- [ ] 已画出相关的入口点、出口点和存储。
- [ ] 每条数据流箭头都写明了数据名称，且只有一个方向。
- [ ] 每条边界都说明了它所标示的权限或信任变化。
- [ ] 重要的内部数据流没有被机械地省略。
- [ ] 威胁 ID 都能对应到负责人、应对措施和验证记录。
- [ ] 提议的控制和未知项与已观察到的控制在视觉上有区别。
- [ ] 这张图没有被当作已完成的评估来展示。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **输入：** 路由和中间件、上传和反序列化点、出站调用和 webhook、队列生产者和消费者、存储访问、进程特权、服务账号和权限引用、网络策略、租户过滤条件。
- **测试和配置体现的是预期的控制，而不是部署后的实际效果。**
- **不作为默认输入：** 日志和运行时状态，其中可能包含密钥。
- **必须由人提供：** 组织层面的信任假设、每个组件由谁控制、攻击者范围，以及哪些控制仅处于提议阶段。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 哪些资产和安全属性最重要？（顾客支付数据和订单完整性）
2. 每个组件由谁控制，特权或租户在哪里发生变化？（列出负责人；标出租户边界）
3. 哪些外部参与者和滥用假设纳入范围？（顾客、分销商、支付服务商）
4. 必须使用 STRIDE，还是应作为另一种方法的输入？（逐元素使用 STRIDE）
5. 是现有系统，还是控制尚不完整的提议设计？（提议设计，并标出控制）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/F2.json` · 布局模板：`nested` · 信任边界成为 `boundary` 分组（可嵌套），外部实体是 `external` 节点，加工是 `component` 节点，存储是 `store` 节点，具名数据流是带单向 `dir` 的 `data` 边；元素 ID 和数据流 ID 放在 `tags` 中，用于关联威胁登记表。

## 来源 {#sources}
<!-- skill: omit -->
1. OWASP, Threat Modeling Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html — 访问于 2026-10-14
2. Microsoft, Getting started with the Threat Modeling Tool — https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started — 访问于 2026-10-14
3. Microsoft / MSDN Magazine, Uncover Security Design Flaws Using the STRIDE Approach (November 2006) — https://learn.microsoft.com/en-us/archive/msdn-magazine/2006/november/uncover-security-design-flaws-using-the-stride-approach — 访问于 2026-10-14
4. NIST, SP 800-207 Zero Trust Architecture (2020) — https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf — 访问于 2026-10-14
5. OWASP Threat Dragon, Getting started (current documentation) — https://www.threatdragon.com/docs/usage/getting-started.html — 访问于 2026-10-14
6. Threat Modeling Manifesto, values and principles — https://www.threatmodelingmanifesto.org/ — 访问于 2026-10-14
7. ISO/IEC/IEEE 42010:2022，仅公开范围部分（直接获取返回 403；未审阅全文） — https://www.iso.org/standard/74393.html — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![F2 · 企业服务助手](/samples/ai-service-assistant/F2/zh/diagram.svg)
*DF 标识将数据流对应到威胁假设，不是消息顺序。DF-6 抽象经 Agent 传递证明（F1），DF-4 经 BFF 读取当前审批；拟议控制仍需实施验证。*

[SVG](/samples/ai-service-assistant/F2/zh/diagram.svg) · [模型 JSON](/samples/ai-service-assistant/F2/zh/diagram.json) · [共享事实](/samples/ai-service-assistant/scenario.json)

[历史 shop 回归样例](/samples/F2-threat-model-data-flow.zh.svg) · [全部29幅视图](/zh/use/ai-service-assistant) · [示意假设](/zh/use/ai-service-assistant-assumptions).

| 威胁 / 数据流 | 假设及影响 | 拟议应对 | 责任方 / 尚需验证 |
|---|---|---|---|
| T1 · DF-1 / DF-10 / TB-1 | 提示注入请求未授权工具 | 模型无授权权力；仅允许三种工具 | Agent 负责人 / 恶意文档测试 |
| T2 · DF-2–5 / TB-2 | 审批后篡改草稿或重放 | 绑定租户、主体、规范 hash、有效期和幂等键；再次授权 | API 负责人 / hash、过期及租户拒绝测试 |
| T3 · DF-6 / TB-3 | 混淆代理使用错误 audience 或 actor | 核验 AS 签名、issuer、audience、actor、tenant、scopes；连接器前拒绝 | 身份负责人 / audience 及跨租户测试 |
| T4 · DF-7–8 | 超时导致重复写入 | 持久意图、连接器幂等及按键查询 | 工具负责人 / 超时对账测试 |
| T5 · DF-4 / DS-app | 运维或模型直接访问审批记录 | 受限服务身份、BFF 策略检查、审计与脱敏 | 平台负责人 / IAM 及日志审查 |

以上均为假设及拟议应对，**尚无验证证据**。
