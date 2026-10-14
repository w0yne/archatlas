---
code: H3
slug: stakeholder-map
family: H
names:
  en: Stakeholder map (power-interest grid)
  zh: 干系人地图（权力-利益矩阵）
  aliases:
    en: [power-interest grid, stakeholder matrix, stakeholder grid]
    zh: [干系人图, 利益相关者矩阵, 权力利益矩阵]
question: 谁能影响这项举措，或会受到它的影响？应如何与各干系人沟通并促进其参与？
audiences: [leaders, business]
levels: [strategy]
phases: [initiate]
scope: 在明确时间点，对一项举措的干系人参与进行规划。
formal: {kind: method, ref: '权力-利益矩阵绘制实践；没有统一的图形标准。Nielsen Norman Group，Stakeholder Analysis for UX Projects：https://www.nngroup.com/articles/stakeholder-analysis/'}
neighbours: [A3, H1]
status: draft
sourceRev: a5d2191
translationOf: en/types/H3-stakeholder-map.md
reviewed: false
---

# 干系人地图（Stakeholder map）

> 按对项目的权力与关注度摆放干系人，并为每一组给出沟通方式。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
干系人地图将评估所得的权力与关注程度关联到沟通参与方式的选择。它使关注点和影响力清晰可见，也包括从不使用系统的参与方。它支持治理与沟通，而非描绘软件架构。

**本站采用的定义：** 权力-利益矩阵，不是干系人目录、洋葱图或关系网络。这些都是相关方法，但含义不同。这里的 interest 指对举措的关注或利害关系，并不必然表示支持态度 [1]。

这类图没有统一版本。Mendelow 的 1981 年原始论文讨论的是权力与环境动态性 [2]；不要误记为 1991 年，也不要将其坐标轴等同于本矩阵。干系人地图不表达交换关系、工作流程或活动级的最终责任。

历史论述将常见的权力-利益矩阵形式与 Johnson 和 Scholes 联系起来 [3]。这里没有独立核实所引二手论述中的确切版次与日期，因此不声称它首次出现于某一版。地图是特定时间的评估，不是对个人价值的衡量，也不是忽略受影响群体的理由。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 举措发起人、交付负责人、业务分析师，以及规划干系人参与的架构师。
- **场景：** 规划网店结账流程改版；识别被忽略的受影响群体；选择评审参与方和视图；范围变化后重新审视沟通参与安排。
- **不适用：** 简短干系人清单已能回答问题，或需要的视图关注系统结构、依赖关系或交换关系。
- **A3 业务上下文：** 展示参与方与业务交换；表达的是流，而非影响力排名。
- **H1 RACI：** 为每项活动分配职责；权力大的干系人并不会自动对所有任务承担最终责任。
- **洋葱图/目录/网络：** 分别用于表达接近程度、关注点清单或关系；它们不是矩阵的完全同义名称。
- 根据受众选择详细程度。使用角色可以减少个人身份信息，但仍可能透露敏感评估；不存在普遍适用的“仅限内部”规则。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：** 举措、评估日期、干系人标签、定义明确的权力与关注度坐标轴、量表与阈值，以及对沟通参与方式的解释。
- **本站约定：** 关注度向右递增，权力向上递增。权力定义为影响举措结果的能力，不仅是职位高低。
- **象限：** 高权力/高关注度 = 密切沟通参与；高权力/低关注度 = 保持满意；低权力/高关注度 = 保持知情与参与；低权力/低关注度 = 持续观察 [1]。
- **评分：** 采用已达成一致的定性类别或有记录的标准。数值量表不会自然带来客观精度；应在图中点位之外保留不确定性说明。
- **可选：** 态度标记、评估依据、置信度，以及列出关注点、行动、负责人和复核日期的配套表格。
- **箭头：** 默认不在干系人之间画箭头。坐标轴箭头表示数值递增；可选的移动箭头表示明确标注的已观察变化或拟议变化。
- **图例：** 定义态度与移动标记；当前位置必须与期望位置区分。不能暗中用关注度表示态度。
- **标签与布局：** 使用简短的角色或群体名称，细节放入单独的图例或表格；除颜色外，还应使用形状或文字。权力较小不意味着失去参与权 [4]。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
| 最佳实践 | 反模式 |
| --- | --- |
| 同时识别受影响群体与决策者 [4]。 | 只放入管理人员或系统直接用户。 |
| 对标准达成一致，并记录点位安排的依据 [1][5]。 | 根据职位或提交次数编造影响力评分。 |
| 区分关注度、影响程度和态度 [1][4]。 | 将关注度低的干系人称为反对者。 |
| 将评估关联到具体沟通参与安排，并定期复核 [1][5]。 | 只有静态象限标签，没有行动或复核日期。 |
| 根据受众与目的选择评估细节 [1]。 | 仅因姓名已替换为角色，就公开仍可识别对象的判断。 |

不同方法的象限标签有所不同。评估*对改革成功的关注或利害关系*的来源，可能采用不同于评估*对举措本身的关注*的矩阵标签。应说明这一区别，而不是将“阻碍者”等标签套用到所有地图 [6]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Nielsen Norman Group — Stakeholder Analysis for UX Projects，已填写的权力/关注度/态度表](https://www.nngroup.com/articles/stakeholder-analysis/) — 在评估权力和关注度的同时，区分当前态度与期望态度；范例是已填写的表格，而非空白矩阵。未确认开放复用许可：应提供链接，不复制其中的姓名、文字或图形。
- [英国政府托管 — Understanding stakeholders and political networks，图 3](https://assets.publishing.service.gov.uk/media/69dfa53e61d2e8e9b9e42dc2/Understanding-stakeholders-and-political-networks.pdf) — 已填写的关注度/影响力矩阵，将前期干系人分析关联到参与规划；其面向改革的 interest 定义与一般关注度轴不同。改编前应检查文档的版权及第三方声明；政府托管本身不构成许可授予。
- [Simply Stakeholders — Using a Stakeholder Matrix，示例 1](https://simplystakeholders.com/stakeholder-matrix/) — 已完成的权力与关注度分配，将六类干系人与沟通参与方式关联起来；这是供应商编写的完整示例，不能证明其中的排名普遍适用。未确认开放复用许可：应提供链接，不复制示例或图形。
- [Local Government Association — How to map stakeholders，已填写的参与规划表](https://www.local.gov.uk/sites/default/files/documents/How%20to%20map%20stakeholders.pdf) — 这一已填写的替代形式纳入了参与正当性，并将评估关联到渠道和具体方法；它是借鉴干系人显著性分析的配套方法，并非严格的权力-利益矩阵。未确认开放复用许可：可用来比较方法，但应自行创作内容。

本页原创示例并未复用这些外部范例的场景。图的身份、表格及已完成的分配通过一手来源文本提取进行核对；未复制任何图形。TOGAF 当前章节无法获取，因此不计为已核实的范例。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定举措、日期、受众，以及地图要支持的沟通参与决策。
2. 收集决策者和受影响群体；与了解情况的参与方共同确认权力与关注度标准。
3. 记录点位安排的证据与不确定性；不要从仓库活动推断评分。
4. 绘制 2×2 矩阵，关注度向右递增、权力向上递增；标注阈值和象限。
5. 放置简短角色标签；态度作为可选且独立的维度。采用中性填充、文字或形状标记，并提供图例。
6. 将关注点、沟通参与行动、负责人和复核日期放在配套表格中；检查是否适合受众。

**自检清单**
- [ ] 范围、日期、坐标轴和阈值清楚。
- [ ] 点位安排有已达成一致的依据；未知项明确标出。
- [ ] 关注度与态度、影响程度分开表达。
- [ ] 已考虑权力较小的受影响群体。
- [ ] 已记录沟通参与行动与复核日期。
- [ ] 移动箭头区分拟议变化与已观察变化。
- [ ] 标签和标记不依赖颜色也可理解。
- [ ] 详细程度适合预期受众。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 治理文档、ADR、运维手册和事项讨论可识别候选群体及其已表达的关注点。
- `CODEOWNERS` 和审批规则只能展示相应技术范围内的评审权限。
- 记录路径、修订版本及证据状态；区分文档记载的角色与评估得出的影响力水平。
- 权力、关注度、态度及外部受影响群体需要结合背景证据并经参与方验证；仅凭代码无法确定。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 这张地图应支持哪项举措及哪项沟通参与决策？
2. 谁会查看地图？适合展示哪些评估细节？
3. 如何定义权力与关注度？谁能验证点位安排？
4. 必须包含哪些受影响群体、沟通参与行动和复核日期？

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/H3.json` · 布局模板：`grid_table` · 两个 `tables[]` 条目：一个 2×2 的影响力 × 关注度网格，以及配套的参与规划表。
近似表示：象限只是普通表格单元格，不绘制坐标平面。

## 来源 {#sources}
<!-- skill: omit -->
1. Nielsen Norman Group — Stakeholder Analysis for UX Projects — https://www.nngroup.com/articles/stakeholder-analysis/ — 访问于 2026-10-14；提供实践指导和已填写表格，但其中的 Mendelow 日期与原始记录冲突。
2. A. L. Mendelow — Environmental Scanning—The Impact of the Stakeholder Concept，ICIS 1981 Proceedings，第 20 篇论文 — https://aisel.aisnet.org/icis1981/20/ — 访问于 2026-10-14；原始摘要确认其讨论权力与动态性，年份为 1981。
3. Votito — Stakeholder Power Interest Matrix origins and analysis — https://www.votito.com/methods/stakeholder-mapping/ — 访问于 2026-10-14；属于二手历史论述，不能据此声称教材版次已经独立核实。
4. Local Government Association — New Conversations 2.0: How to map stakeholders — https://www.local.gov.uk/sites/default/files/documents/How%20to%20map%20stakeholders.pdf — 访问于 2026-10-14。
5. UK Government Analysis Function — Stakeholder mapping — https://analysisfunction.civilservice.gov.uk/policy-store/stakeholder-mapping/ — 访问于 2026-10-14；评分流程值得参考，但图中坐标轴用语与周边关于权力和关注度的描述不同。
6. 英国政府托管 — Understanding stakeholders and political networks: Practical Guidance Note — https://assets.publishing.service.gov.uk/media/69dfa53e61d2e8e9b9e42dc2/Understanding-stakeholders-and-political-networks.pdf — 访问于 2026-10-14。
7. Simply Stakeholders — Using a Stakeholder Matrix: 3 Practical Examples — https://simplystakeholders.com/stakeholder-matrix/ — 访问于 2026-10-14；示例 1 包含已完成的权力与关注度分配。

## 示例 {#sample}
<!-- skill: path only -->
![H3 示例：权力-利益干系人图及配套行动表](/samples/H3-stakeholder-map.svg)
*权力-利益干系人图（假设）：商城管理员重点管理，财务令其满意，顾客保持知情，承运商持续关注；配套表给出态度和下一步。摆放位置仅为示意，不对任何真实的人或组织排序。*
