---
code: H1
slug: raci-matrix
family: H
names:
  en: RACI matrix
  zh: RACI 责任矩阵
  aliases:
    en: [RACI chart, responsibility assignment matrix, RASCI matrix]
    zh: [RACI 职责分配矩阵, 责任分配矩阵]
question: 对于每项活动，谁执行工作、对结果负责、提供意见，以及接收进展通知？
audiences: [leaders, business, operations]
levels: [strategy, concept]
phases: [initiate, operate]
scope: 一项举措或一项服务内各项活动的职责分配。
formal: {kind: convention, ref: '职责分配实践；没有统一版本的图形标准。Atlassian，Understanding and using RACI charts：https://www.atlassian.com/work-management/project-management/raci-chart'}
neighbours: [A4, D3, E4, F3, H2, H3]
status: draft
sourceRev: a5d2191
translationOf: en/types/H1-raci-matrix.md
reviewed: false
---

# RACI 责任矩阵（RACI matrix）

> 活动 × 参与方的网格，逐项说明谁执行、谁最终负责、咨询谁、告知谁。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
RACI 责任矩阵将活动与执行、最终责任、咨询和沟通联系起来。横向阅读可以发现无人负责的工作；纵向阅读可以发现工作量或审批权过度集中的情况。它支持治理方面的关注点，并不对应某个固定的架构层级。

**本站采用的定义：** 角色、团队或具名个人都可以作为参与方。每行一个 A 是默认约定，而非普遍适用的标准：英国政府安全部门明确允许共同承担最终责任 [1][2]。一项活动可以有多个 R，也可以使用 A/R 组合。

RACI 没有统一版本的表示法。职责分配矩阵是更广泛的类别；RASCI 增加了 Support（支持）角色。DACI 是决策框架，不是 RACI 的别名 [3]。RACI 不表达工作流程顺序、时间安排、汇报层级或软件实际执行的权限规则。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 交付负责人、服务负责人、工作参与者和运维人员。
- **场景：** 准备网店发布；将结账功能的支持工作移交运维；分配安全控制工作；跟踪事故后续工作的职责。
- **不适用：** 简单任务清单已能明确责任，或真正需要回答的是时间安排、依赖关系或技术访问权限问题 [1][4]。
- **H3 干系人地图：** 需要确定沟通参与的优先级时使用；RACI 则为每项活动分配职责。
- **E4 泳道：** 需要表达顺序和交接时使用；可将其中的活动关联到矩阵行。
- **F3 访问控制模型：** 需要说明允许执行的操作时使用；评审权限不等于业务上的最终责任。
- **D3 数据血缘与归属图：** 需要说明某个数据集归谁所有、由谁管理时使用；RACI 为活动分配职责。
- **DACI：** 需要组织某项具体决策时使用；决策产生的交付职责可用 RACI 表达 [3]。
- **A4 业务场景矩阵：** 需要说明哪些角色参与哪些业务活动时使用；RACI 为每项活动分配职责，不表达覆盖范围。
- **H2 可观测性视图：** 需要说明事故如何被发现、如何分派时使用；RACI 说明由谁负责响应。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：** 以范围内的活动为行、可识别的参与方为列，填写单元格职责并提供图例。活动名称采用简短的动宾结构。
- **字母含义：** R 执行工作；A 对结果承担最终责任；C 提供意见；I 接收通知。需说明 A 是否包含正式审批 [1][2]。
- **规则：** 每个执行活动行通常有一个 A 和至少一个 R。共同承担 A 时，必须明确权限边界或分歧解决规则；不要擅自抹去已达成一致的治理安排。
- **组合字母：** 同一参与方可以标为 A/R。区分“不参与”和“未知”；空白不能同时表示两者。
- **可选：** 阶段分组、活动 ID、证据引用、生效日期，以及角色与人员的对应表。增加 S 时应将矩阵标为 RASCI。
- **箭头：** 矩阵内不使用箭头。单元格表示职责分配，不表示数据流或执行顺序。咨询可能涉及双向沟通，但无需画出连接线。
- **配套流程：** 升级处理箭头需标明触发条件和含义，并与矩阵分开展示。
- **详细程度：** 活动粒度应具有可比性；参与方层级混用时需解释。含义由字母承载，颜色仅作辅助。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
| 最佳实践 | 反模式 |
| --- | --- |
| 与受影响的参与方共同确认职责分配 [1][2]。 | 将自动生成的草稿视为已授予的权限。 |
| 明确本地 A/R 规则，并解释共同决策权的安排 [1][2]。 | 宣称一个 A 或一个 R 是普遍强制要求。 |
| 检查每行的职责覆盖与每列的工作量 [1]。 | 只检查字母是否齐全，忽略瓶颈。 |
| 保留有实际意义的活动，以及必要的 C/I 分配 [1][5]。 | 填满所有单元格，或列出每个实现细节任务。 |
| 范围或人员发生变化时重新审视分配 [2]。 | 将模板中的责任归属直接套用到另一组织。 |

Asana 正文建议只设一个 R，但其常见问题部分允许多个 R [4]。参考其实践建议时应注意这一不一致；它不是规范性的职责数量规则。

## 范例 {#exemplars}
<!-- skill: omit -->
- [UK Government Security — Secure by Design 已填写的 RACI 工作簿](https://www.security.gov.uk/wp-content/uploads/2025/12/Cyber-security-roles-and-responsibilities-RACI-matrix-EXAMPLE-September-2026.xlsx) — 按活动与角色分配职责，展示了发布方采用的共享 A 约定；改编前应确认工作簿的复用条款，公开可访问本身不代表开放许可。
- [PMI — Project Manager and Business Analyst Collaboration，图表 1](https://www.pmi.org/learning/library/business-analyst-project-manager-collaboration-6512) — RACI 范例聚焦不同专业角色之间重叠的职责；它是会议论文中的示例，不是规范性标准，也未确认开放复用许可，因此应提供链接而非复制。
- [University of Essex — Responsibility matrix，已填写的四行示例](https://www.essex.ac.uk/staff/strategic-project-delivery/responsibility-matrix) — 展示参与方职责随活动变化及 A/R 组合；占位任务名适合讲解表示法，不适合示范良好的活动命名，且未确认开放复用许可。

政府工作簿与 Essex 表格中的单元格已通过文本核对；PMI 范例通过图注及周边说明确认，并未逐格进行视觉核查。空白模板或 AI 提示词不计为已填写的范例。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定范围、受众，以及现状或目标态；收集已达成一致的活动与参与方。
2. 选择角色或个人；定义字母、未知标记、组合字母及最终责任规则。
3. 根据证据起草各行；不确定的责任归属保留为待确定。
4. 检查行是否缺项、列是否过载；拆分结果相互冲突的活动。
5. 活动纵向排列，参与方横向排列；按阶段分组，拆表时重复表头。
6. 标签保持简短，字母在无颜色时仍可辨认，图例放在旁边；记录生效日期和维护责任归属。

**自检清单**
- [ ] 范围与状态明确。
- [ ] 每行都有执行职责覆盖，或明确显示缺口。
- [ ] A 的分配符合已声明的规则。
- [ ] 共享 A 有分歧解决规则。
- [ ] 未知与不参与明确区分。
- [ ] 已检查各列及 C/I 分配。
- [ ] 参与方已确认责任归属，证据支持相应描述。
- [ ] 不依赖颜色仍能读清表头、字母和图例。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 治理文档与已批准的决策支持文档中记载的职责分配。
- 运维手册和发布流程可识别活动、职责及升级处理路径。
- `CODEOWNERS` 和审批配置确定评审规则，而非组织层面的 A。
- 提交频率、管理员权限和事项指派不能确立最终责任。
- 记录每项描述的路径、修订版本及已核实/推断/仅文档/冲突状态；责任归属存在缺口时，应向相关人员确认。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 哪些活动需要更明确的责任归属？描述的是现状还是目标态？
2. 参与方应采用角色、团队还是具名个人？
3. 这里的 A 具体表示什么？是否允许共同承担最终责任？
4. 哪些分配已达成一致、尚未确定，或需要单独的升级处理流程？

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/H1.json` · 布局模板：`grid_table` · 一个 `tables[]` 条目：活动为行 × 参与方为列，单元格填 R/A/C/I（默认每行一个 A；共同承担 A 时须注明权限边界或分歧解决规则）；图例写在表格的 `title` 中。

## 来源 {#sources}
<!-- skill: omit -->
1. Atlassian — Understanding and using RACI charts — https://www.atlassian.com/work-management/project-management/raci-chart — 访问于 2026-10-14。
2. UK Government Security — Agreeing roles and responsibilities，附示例工作簿 — https://www.security.gov.uk/policy-and-guidance/secure-by-design/activities/agreeing-roles-and-responsibilities/ — 访问于 2026-10-14。
3. Atlassian Team Playbook — DACI Decision-Making Framework — https://www.atlassian.com/team-playbook/plays/daci — 访问于 2026-10-14。
4. Asana — Your guide to RACI charts, with examples — https://asana.com/resources/raci-chart — 访问于 2026-10-14。
5. University of Essex — Responsibility matrix — https://www.essex.ac.uk/staff/strategic-project-delivery/responsibility-matrix — 访问于 2026-10-14。
6. PMI — Partnering: Project Manager and Business Analyst Collaboration — https://www.pmi.org/learning/library/business-analyst-project-manager-collaboration-6512 — 访问于 2026-10-14。
7. UK Government Security — Cyber security roles and responsibilities RACI matrix，示例工作簿 — https://www.security.gov.uk/wp-content/uploads/2025/12/Cyber-security-roles-and-responsibilities-RACI-matrix-EXAMPLE-September-2026.xlsx — 访问于 2026-10-14。

## 示例 {#sample}
<!-- skill: path only -->
![H1 示例：一次结账发布的 RACI 矩阵](/samples/H1-raci-matrix.svg)
*网店发布矩阵将准备、审批、支持交接和回滚就绪工作分配给通用角色。其中的分配仅作示意，不代表推断出的组织规则。*
