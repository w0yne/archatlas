---
code: F3
slug: access-control-model
family: F
names:
  en: Access-control model
  zh: 访问控制模型
  aliases:
    en: [authorization model, permission model, RBAC model, role-permission matrix, ABAC policy model, ReBAC graph, relationship-based authorization graph]
    zh: [权限模型, 授权模型, 角色权限矩阵, 基于属性的授权模型, 基于关系的授权模型]
question: 主体在什么规则下，能在给定的范围或上下文中对某个资源执行某个操作？
audiences: [architects, developers, security]
levels: [logical]
phases: [design, build]
scope: 一个应用或领域：其资源类别、一小组操作，以及选定的一种模型类型（RBAC、ABAC 或 ReBAC，可组合使用）
formal: {kind: convention, ref: 'RBAC: ANSI/INCITS 359-2004 and its 2012 revision (NIST history). ABAC: NIST SP 800-162. Policy language and architecture: OASIS XACML 3.0. ReBAC has influential models (Zanzibar, OpenFGA) but no single graphical standard'}
neighbours: [D1, F1, F2, H1]
status: draft
translationOf: en/types/F3-access-control-model.md
sourceRev: 1ed1739
reviewed: false
---

# 访问控制模型（Access-Control Model）

> 一张描述“谁可以对哪个资源做什么”的规则图，按策略的性质画成矩阵、属性表或关系图。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 主体在什么规则下，能在给定的范围或上下文中对某个资源执行某个操作？它描述的是授权及其管理，而不是网络可达性或调用顺序。“可编辑”关系与承载文档内容的箭头含义不同。
- **三种模型类型，回答三个问题：**
  - **RBAC：** 哪些角色拥有哪些权限，谁拥有这些角色？用矩阵或层次结构表示 [1]。
  - **ABAC：** 主体、资源和环境的哪些属性满足哪条规则？用属性表或决策表表示 [2]。
  - **ReBAC：** 对象之间的哪些关系推导出哪些访问？用带推导规则的类型化关系图表示 [4][5]。
- **本站采用的定义：** 一项*授予*（grant）始终具有操作、资源和范围三方面的语义。矩阵、属性表和关系图并不是同一事物的不同画法；应按策略来选，而不是按潮流。
- **不包含：** 真实的用户名单、完整的策略代码、所有例外。RACI 矩阵（H1）中名为“管理员”的角色并不是应用权限。
- **不是执行：** 模型图本身不执行任何控制；只有当执行是主题时才画出执行点（F1）。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 业务负责人、安全与治理人员、开发人员、管理员。
- **典型场景：**
  1. 有范围限制的团队协作：网店客服、仓储和财务团队的员工。
  2. 多租户授权：平台商家只能看到自己的订单。
  3. 带继承的文档共享：把一个发票文件夹共享给会计。
  4. 管理委托与职责分离：谁可以创建退款，谁可以审批退款。
  5. 将提议的角色模型与当前实际执行的情况进行比较。
- **不适用的情况：** 当关系、时间或资源属性会实质性地决定访问时，不要只用角色矩阵。也不要仅仅因为某个授权引擎的文档示例好看就引入它。
- **与相邻图类的区别：**
  - 身份在哪里被校验、决策在哪里被执行，选 **F1 认证与授权流程图**。
  - 可能出什么问题，选 **F2 威胁建模 DFD**。
  - 实际的持久化关系（而非权限关系），选 **D1 实体关系图**。
  - 项目职责（而非应用权限），选 **H1 RACI 矩阵**。
  - 展示策略组件在各组成部分中的位置，选 **C5 逻辑架构**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** RBAC、ABAC 和 XACML 的概念有标准支撑；画法则是约定。需声明图例。
- **通用必备元素：** 主体类别、操作、资源类别、范围或归属、决策规则、默认行为、约束。明确标注“授予”“属于”“继承”和“拥有”。
- **图例：** 区分允许、拒绝、有条件和不适用。空白单元格含义不明。
- **RBAC：** 用户、角色、权限（对对象的操作）及分配关系；相关时还包括会话与激活角色、角色层次，以及静态或动态职责分离 [1]。矩阵的行是角色；列写明对资源的操作，而不是模糊的功能。
- **ABAC：** 权威来源的主体、资源和环境属性，附一个示例谓词或决策表；说明每个属性来自哪里、何时求值 [2]。
- **ReBAC：** 类型化对象、带标签的关系，以及并集、交集或继承规则 [4]。关系链需要有策略语义；仅有一张 ER 风格的图是不够的。
- **可选：** 管理条带（谁授予、谁撤销）、策略和数据的归属、撤销或缓存假设、应用身份与用户身份、执行位置。PEP、PDP、PIP 和 PAP 是面向技术受众的功能职责，并不要求做成四个独立服务 [3]。XACML 的 PAP（策略管理点）不同于 NIST 零信任架构中的策略管理器（policy administrator）。
- **文字预算：** 每个单元格或边标签 1–3 个词；策略说明文字放在注释中。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **默认拒绝，** 并对每个相关请求，针对所请求的操作和资源检查授权 [6]。
2. **将操作能力与资源范围分开。** “客服专员”并不等于有权编辑每个商家的订单；应画出有条件的授予或一个小的范围示例 [4][7]。
3. **说明合并规则**（授予取并集、拒绝优先、约束取交集）。没有一条公式适用于所有系统。
4. **将管理权限与内容权限分开。** 如果管理员可以读取内容，就把这项授予明确画出；紧急访问和委托另行说明。
5. **派生内容保留来源的限制。** 基于受限订单生成的共享报表，必须重新检查来源访问权限或限制其受众。

### 反模式
1. **无人管理、无从解释的直接授予。** 直接授予本身没有错：归属、显式共享和 ACL 都是合理的；问题在于无人负责的例外 [2][4]。
2. **角色爆炸，** 以及另一个极端：把所有上下文相关的策略都硬塞进角色。
3. **用功能代替操作和资源**作为矩阵的列。
4. **省略限定条件的简写**（写“团队成员可以看到”，而实际上还有来源限制）。
5. **未检查执行路径就把设计当作已实现的覆盖范围来展示。**

## 范例 {#exemplars}
<!-- skill: omit -->
- [NIST SP 800-162, Figures 2 and 5](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf) — 基于属性的决策输入，以及相互分离的决策、执行和管理功能；并不要求部署独立服务器。美国政府作品，一般属于公有领域。
- [OpenFGA: User Groups](https://openfga.dev/docs/modeling/user-groups) — 具体的用户、组和对象关系，带有派生权限和使模型可测试的检查。
- [OpenFGA: Authorization Through Organization Context](https://openfga.dev/docs/modeling/organization-context-authorization) — 说明为什么组织成员资格与当前上下文可以是两项独立的限制。
- [AWS Prescriptive Guidance, Example 3: multi-tenant access control with RBAC](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-mt-abac-examples.html) — 让租户隔离和租户内角色一目了然。URL 中写的是 “abac”，但页面标题是 RBAC；其按租户划分存储的做法只是一种实现模式，而非规则。
- 仅提供链接，未复制任何图稿。产品的代码许可并不决定其文档插图的许可。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 列出资源类别（订单、发票、商品）和一小组有意义的操作（查看、编辑、退款、审批）。
2. 区分主体、应用身份、角色或组，以及租户或归属范围。
3. 按策略选择形式：角色授予用矩阵，条件用属性表，共享和继承用关系图。在标题中说明所选形式（“网店后台：角色权限矩阵，提议”）。
4. 矩阵布局：角色作为行，“资源-操作”对作为列并按资源分组；单元格填写图例符号。关系图布局：主体在左，资源在右，中间是带标签的关系，节点不超过约 12 个。
5. 在图旁的注释中说明默认拒绝和合并规则。
6. 加一个允许和一个拒绝的示例，二者须与规则一致；只有当委托在范围内时才添加管理条带。
7. 颜色：中性底色；允许用一种色相，有条件用另一种，拒绝用灰色斜线；每个符号同时有文字或形状提示。
8. 在图注中标明是设计还是已核实的执行情况。

**自检清单**
- [ ] 已明确选定模型类型（RBAC、ABAC 或 ReBAC）。
- [ ] 操作和资源都有名称，而不是模糊的功能。
- [ ] 范围或归属与角色相区分。
- [ ] 单元格和边的含义以及合并规则没有歧义。
- [ ] 已说明默认行为和出错行为。
- [ ] 管理权限与内容权限没有混为一谈。
- [ ] 允许和拒绝示例与规则一致。
- [ ] 已说明执行覆盖范围和未核实的假设。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **输入：** 角色和权限表、授权装饰器或守卫、策略文件、行级过滤条件、关系元组、所有者和租户字段、管理端点、超级用户覆盖、共享逻辑、拒绝和撤销测试。
- **注意：** 一个数据库关系或一个未被使用的辅助函数，并不能证明每个端点都执行了它。
- **默认不查看真实的权限名单。**
- **必须由人提供：** 预期的策略、委托规则、管理员是否读取内容、设计与已实现覆盖范围的差别。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 哪些资源和操作、哪些归属或租户边界最重要？（订单、发票、退款；按商家划分租户）
2. 仅靠角色是否足够，还是属性或共享关系会改变决策？（角色加租户范围；仅为共享添加关系）
3. 谁可以授予和撤销访问，委托范围是什么？（租户管理员，限于本租户）
4. 管理员是自动可读内容，还是需要单独授权？（需要单独授权）
5. 我们是在设计规则，还是在记录已核实的实现？（设计，标为提议）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/F3.json` · 布局模板：`grid_table` · 角色（或主体）成为行，“资源-操作”对成为分组的列，每个单元格按固定图例填写允许、拒绝、有条件或不适用；对于 ABAC 和 ReBAC，同样的 `tables` 承载属性规则或关系定义（关系图需要另做一个模型，因为 `grid_table` 只接受表格）。

## 来源 {#sources}
<!-- skill: omit -->
1. NIST, Role Based Access Control (archived project and standard history; latest reaffirmation not asserted) — https://csrc.nist.gov/projects/role-based-access-control — 访问于 2026-10-14
2. NIST, SP 800-162, Guide to Attribute Based Access Control (ABAC) Definition and Considerations (January 2014, updated 2 August 2019) — https://csrc.nist.gov/pubs/sp/800/162/upd2/final ; figures: https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf — 访问于 2026-10-14
3. OASIS, eXtensible Access Control Markup Language (XACML) Version 3.0 (22 January 2013) — https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html — 访问于 2026-10-14
4. OpenFGA, User Groups and Authorization Through Organization Context — https://openfga.dev/docs/modeling/user-groups ; https://openfga.dev/docs/modeling/organization-context-authorization — 访问于 2026-10-14
5. Google Research, Zanzibar: Google's Consistent, Global Authorization System (USENIX ATC 2019) — https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/ — 访问于 2026-10-14
6. OWASP, Authorization Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html — 访问于 2026-10-14
7. AWS Prescriptive Guidance, Example 3: Multi-tenant access control with RBAC — https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-mt-abac-examples.html — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![F3 示例：商城后台的角色-权限矩阵（拟议）](/samples/F3-access-control-model.svg)
*商城后台的角色-权限矩阵（RBAC，拟议方案）：角色为行，“资源-操作”对为列。单元格写明允许、拒绝，或适用的条件（本人订单、分配给该工单、不超过退款限额）。默认拒绝；执行情况尚未验证。*
