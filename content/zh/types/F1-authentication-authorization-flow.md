---
code: F1
slug: authentication-authorization-flow
family: F
names:
  en: Authentication and authorization flow
  zh: 认证与授权流程图
  aliases:
    en: [identity flow, sign-in flow, SSO flow, OAuth flow, OIDC flow, delegated access flow, delegated API access flow]
    zh: [身份认证流程图, 统一登录流程图, 委托访问流程图]
question: 谁向谁证明了哪个身份，传递了什么授权，访问究竟在哪里被允许或拒绝？
audiences: [security, architects, developers]
levels: [logical]
phases: [design, build]
scope: 一个场景（浏览器登录、服务代表用户调用，或纯机器调用）和一个受保护操作
formal: {kind: convention, ref: 'A concern-based diagram family, not a notation. Drawn as a UML 2.5.1 sequence diagram when UML is claimed; protocol semantics come from OAuth 2.0 (RFC 6749), PKCE (RFC 7636), the OAuth security BCP (RFC 9700) and OpenID Connect Core 1.0'}
neighbours: [E1, F2, F3]
status: draft
translationOf: en/types/F1-authentication-authorization-flow.md
sourceRev: 61fe367
reviewed: false
---

# 认证与授权流程图（Authentication and Authorization Flow）

> 针对单一场景的图：谁向谁证明身份，哪份凭证交给了哪个接收方，以及请求在哪一点被允许或拒绝。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 谁向谁证明了哪个身份，传递了什么授权，访问在哪里被允许或拒绝？这个视图解释的是一条信任链，而不只是 HTTP 流量。登录并不意味着可以访问所有对象。
- **必须区分的参与方：** 人、客户端应用、签发凭证的权威方，以及依赖该凭证的服务。
- **定位：** 一种按关注点划分的图类，而不是正式表示法。常见形式是时序图（sequence diagram）；通俗版采用简化的流程图。如果声称使用 UML，就要遵循 UML 2.5.1 的交互规则，而不是自创箭头含义 [1]。
- **不包含：** 无关的业务计算、身份提供方内部细节、明文密钥，以及完整的权限模型（F3）。当关注点是生命周期时，续期和登出单独成一个场景。
- **本站采用的定义：** *认证*（authentication）确认调用方是谁；*授权*（authorization）决定该调用方可以做什么。OAuth 2.0 是一个授权框架；OpenID Connect 在其之上增加了用户认证层 [2][5]。两者画在同一张图里没有问题，但两种职责必须在图上清晰分开。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 架构师、身份工程师、开发人员、安全评审人员；通俗版面向业务负责人。
- **典型场景：**
  1. 顾客登录网店 Web 应用，然后通过 API 加载自己的订单历史。
  2. 订单 API 代表已登录的顾客调用支付 API。
  3. 夜间库存同步作业在没有终端用户的情况下调用库存 API（机器对机器）。
  4. 修改收款账户前的升级认证（step-up），或会话续期。
- **不适用的情况：** 后台作业没有终端用户，因此不要画人的登录；F1 不是完整的权限模型，也不是网络设计。
- **与相邻类型的区别：**
  - 没有身份关注点的一般请求交互，选 **E1 时序图**。
  - 权限规则本身（角色、属性、关系），选 **F3 访问控制模型**。
  - 推演信任边界上可能出什么问题，选 **F2 威胁建模 DFD**。
  - 只展示存在哪些外部身份提供方、不展示交换过程，选 **C2 系统上下文图**。
  - 关注数据流动而非凭证流动，选 **D2 数据流图**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** 非正式。在 UML 时序图中，生命线是参与方，有序消息是交互，虚线箭头是返回，`alt` 片段表示备选分支 [1]。在自定义流程图中，要给箭头编号并加以说明。
- **所选场景的必备元素：**
  - 区分清楚的参与方，以及每条消息的发起方。
  - 图中每份凭证的签发方和接收方。
  - 校验发生在哪里，执行（enforcement）发生在哪里。
  - 受保护的操作或资源，以及包括拒绝点在内的结果。
  - 已认证的主体与不可信的、用户提供的标识符分开。
- **技术版：** 分别命名授权码、访问令牌、ID 令牌和会话 Cookie。在影响信任的地方，标出受众（audience）、作用域（scope）以及应用与用户的绑定关系。浏览器重定向与后端通道（back-channel）交换分开画。机密客户端的密钥绝不经过公开的浏览器 [2]-[5]。
- **通俗版：** 使用“登录”“已验证身份”“请求许可”“允许 / 拒绝”等说法，并链接到协议细节。即使简化，也必须表明谁负责校验、谁负责阻止访问。
- **不是消息：** 信任边界是一个区域，而不是一条箭头。
- **可选：** 过期与刷新、多因素认证、用户同意、发现（discovery）、审计和吊销，仅在对该场景有实质意义时才画。
- **文字预算：** 每条箭头 2–6 个词，动词加凭证用途（“出示访问令牌”）。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **区分三件事：** 身份校验、权限决策和执行。浏览器绝不能是唯一的关卡 [6]。
2. **尊重凭证的接收方。** 为订单 API 签发的令牌在支付 API 上并不构成授权；代表（on-behalf-of）交换让这次移交变得明确 [7]。
3. **采用当前的安全指南，而不是罗列所有历史授权方式。** RFC 9700 更新了基线：例如公开客户端必须使用 PKCE，不应再使用隐式（implicit）和密码（password）授权方式；具体要求取决于客户端和流程类型 [4]。图中展示的任何流程都要标明是现行还是遗留。
4. **只要图意在解释执行，就要包含拒绝分支。** 一条登录箭头不能暗示所有操作都会成功。
5. **凭证结构要与协议一致。** “应用加用户身份”并不一定意味着两个持有者令牌（bearer token）。

### 反模式
1. **一张图混合所有协议**（登录、委托、机器调用）。应按场景拆分。
2. **把授权码、ID 令牌、访问令牌和会话当作可以互换的“令牌”。**
3. **没有交换步骤，就把一个令牌重新标注为另一个服务的授权。**
4. **在意在展示执行的图中只画主成功路径。**
5. **在图上出现密钥或真实端点值**，或在通俗版中使用专业缩写。

## 范例 {#exemplars}
<!-- skill: omit -->
- [RFC 6749, Figures 1 and 3](https://www.rfc-editor.org/rfc/rfc6749.html) — 命名的协议角色和有序的交换；应结合较新的 BCP 阅读，而不是当作推荐授权方式的清单。© IETF Trust，文本复用遵循 IETF 条款。
- [Microsoft identity platform: authorization code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow) — 在一个包含 PKCE 的完整流程中，将浏览器、客户端和权威方分开。
- [Microsoft identity platform: on-behalf-of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow) — API A 与 API B 的令牌受众不同，揭示了委托边界。
- 仅提供链接，未复制任何图稿。复制图之前请先查看各网站的插图使用条款。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 选定一种客户端类型和一个受保护操作；在标题中写明受众以及是现状还是提议（“网店：已登录用户的订单历史，现状”）。
2. 根据证据，识别签发方、调用方、接收 API 和受保护资源。
3. 先追踪凭证的签发与校验，再把权限执行作为单独一步。
4. 布局：参与方从左到右排列（人、客户端、签发方、API、资源），交互从上到下；每张图一个场景。任何下游交换（API 到 API）放到单独的图或框中。
5. 浏览器重定向与后端通道调用使用不同线型，并用一行图例说明。
6. 添加一个 `alt` 框，包含允许和拒绝两种结果；拒绝分支在受保护操作之前结束。
7. 标签：简短的动词加凭证用途；为箭头编号。颜色标示职责（签发、校验、执行），而非产品；最多 3 种颜色加中性色。

**自检清单**
- [ ] 客户端类型和场景已明确。
- [ ] 人的身份与机器身份已区分。
- [ ] 每份凭证都有签发方和预期接收方。
- [ ] 标签中授权码、ID 令牌、访问令牌和会话没有混用。
- [ ] 校验和执行都可见。
- [ ] 拒绝分支没有继续进入受保护操作。
- [ ] 浏览器交换和后端通道交换画法一致；箭头连接在生命线上。
- [ ] 未经核实的外部配置已在图上或图注中说明。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **输入：** 认证中间件、回调和会话处理程序、已配置的签发方和受众名称、客户端注册声明、下游 API 客户端、权限依赖、路由注册、拒绝测试、令牌续期处理。
- **读取配置项名称，而不是密钥值。**
- **声明不等于行为：** 代码体现的是意图；除非用户确认，否则已部署身份提供方的同意设置和客户端配置仍属未核实。
- **必须由人提供：** 哪些身份方案已定、哪些仍待定，以及提议的流程。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 是浏览器登录、服务代表用户调用，还是纯机器调用？（浏览器登录后调用一个 API）
2. 受众是业务负责人还是协议实现者？（实现者，配一段通俗说明）
3. 涉及哪个操作和哪些系统，是现状还是提议的行为？（一个读取操作，现状）
4. 哪些身份方案已确认，哪些尚未决定？（未决定的标为提议）
5. 续期或吊销是主要关注点，还是另起一个场景？（另起一个场景）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/F1.json` · 布局模板：`sequence` · 参与方是 `lifeline` 节点（人、客户端、身份提供方、API、资源）；凭证和请求是带 `step` 的编号 `message` 边；允许/拒绝的备选分支是 `frames` 中的 `alt` 条目，带两个 `operands`，各有自己的守卫条件和步骤范围；校验和执行是身份提供方和 API 上的 `activations`。

## 来源 {#sources}
<!-- skill: omit -->
1. OMG, UML 2.5.1 (December 2017) — https://www.omg.org/spec/UML/2.5.1/ — 访问于 2026-10-14
2. IETF, The OAuth 2.0 Authorization Framework, RFC 6749 — https://www.rfc-editor.org/rfc/rfc6749.html — 访问于 2026-10-14
3. IETF, Proof Key for Code Exchange by OAuth Public Clients, RFC 7636 — https://www.rfc-editor.org/rfc/rfc7636 — 访问于 2026-10-14
4. IETF, Best Current Practice for OAuth 2.0 Security, RFC 9700 (BCP 240, 2025) — https://www.rfc-editor.org/rfc/rfc9700 — 访问于 2026-10-14
5. OpenID Foundation, OpenID Connect Core 1.0 incorporating errata set 2 — https://openid.net/specs/openid-connect-core-1_0.html — 访问于 2026-10-14
6. OWASP, Authorization Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html — 访问于 2026-10-14
7. Microsoft, OAuth 2.0 on-behalf-of flow — https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow — 访问于 2026-10-14
8. Microsoft, OAuth 2.0 authorization code flow — https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow — 访问于 2026-10-14
9. ISO/IEC/IEEE 42010:2022，仅公开范围部分（直接获取返回 403；未审阅全文） — https://www.iso.org/standard/74393.html — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![F1 示例：已登录购物者的授权码流程，含拒绝分支](/samples/F1-authentication-authorization-flow.zh.svg)
*购物者查看订单历史的授权码流程（示意，未对照真实部署验证）：网页应用通过重定向把购物者带到身份提供方，经后端通道用授权码换取访问令牌，再带令牌调用订单接口。接口取得签名密钥后，在一个备选分支框内校验令牌，框内有两个以虚线分隔的操作数：[令牌有效] 时返回订单列表，网页应用显示订单；[否则：令牌无效或已过期] 时回答 401 未授权，在受保护操作之前停止，网页应用重新发起登录。同一请求只会走其中一个操作数。购物者始终拿不到访问令牌。*
