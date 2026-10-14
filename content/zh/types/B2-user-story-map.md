---
code: B2
slug: user-story-map
family: B
names:
  en: User story map
  zh: 用户故事地图
  aliases:
    en: [story map, story mapping]
    zh: [故事地图, 用户故事映射]
question: "用户如何达成目标？哪些完整的增量可以支持或检验这段体验？"
audiences: [product, developers, business]
level: concept
phases: [requirements]
scope: system
formal:
  kind: method
  ref: "Jeff Patton, story mapping — https://www.jpattonassociates.com/the-new-backlog/"
neighbours: [A4, A6, B3, B1]
status: draft
sourceRev: a082cec
translationOf: en/types/B2-user-story-map.md
reviewed: false
---

# 用户故事地图

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
故事地图回答：**用户如何达成目标，哪些完整的增量可以支持或检验这段体验？** 它保留了扁平待办列表容易丢失的叙事上下文 [1][3]。
**本站采用的定义：** 与 Jeff Patton 相关的协作式产品探索和规划方法，而不是有版本号的图形标准 [1][2]。
横向主干按讲述用户故事的顺序排列；纵向主体组织细节、备选方式或优先级。两个方向都不天然代表精确时间线。
发布或实验切片横跨用户活动，以支持有意义的结果。下一步可以是行走骨架、原型或学习实验；第一条切片线不必标为“MVP”。
除非另行提供，故事地图不表达精确工作流语义、实现结构、详细估算或交付承诺。它辅助对话，不是自足的需求契约。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 产品经理、研究／设计人员、领域用户、开发人员和测试人员。
- **场景：** 探索网上购物体验；选择结账原型；把一次发布切分为有用的增量；将客服聊天机器人功能放入既有旅程；暴露缺失步骤或无障碍需求。
- **何时不用：** 规定精确分支／并发、承诺进度，或盘点内部模块。
- 需要表达体验中的触点、想法和感受时，选择 **A6 用户旅程图** [5]。
- 需要表达能力层次，而不需要叙事／发布语义时，选择 **B3 功能树**。
- 需要表达参与者与目标的关系时，选择 **B1 用例图**；需要精确行为时，选择 **E2 活动图／流程图**。
- 路线图传达战略结果或时间安排；迭代看板跟踪工作状态。两者都不是故事地图的同义词。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **核心：** 目标用户与目标；构成主干的高层活动／任务；按所属活动放在下方的细节卡片 [1–4]。
- **横向位置：** 大致的叙事顺序，不是强制执行顺序。
- **纵向位置：** 说明它表示必要性、优先级、细节程度还是完善程度；不要默默混用。
- **切片：** 规划增量时需要，探索阶段可选；标明目标用户、结果／学习目标，以及成功的证据。
- **名称：** 使用“比较商品”“确认配送”等简短动词短语；完整验收条件保留在链接的记录中。
- **箭头：** 通常不需要。若添加依赖箭头，须单独说明图例；它不会把地图变成工作流。
- **可选：** 故事 ID、研究引用、发布分区、估算，以及关联的技术支撑工作。
- **多个用户：** 使用明确的泳道或关联地图，不要混合彼此不兼容的叙事。
- **颜色：** 配合标签强化卡片、分组或切片含义；没有强制配色、行数或发布次数。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- 先建立完整叙事，再详细分解；避免第一列穷尽细节，其余部分却是空白 [2]。
- 主干保留叙事顺序；对下方故事排序，而不是把整段体验按业务价值重排 [1]。
- 围绕端到端结果或实验切片；避免交付互不衔接的“最高优先级”片段 [1][3][4]。
- 用研究支撑活动，并考虑备选方式；不要把团队假设或一条理想路径当作全部体验 [2][4]。
- 将讨论、依赖和支撑工作关联到卡片；不要把好看的便签当作已达成共识的需求，也不要一概排除技术工作 [2][3]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [Patton，Story Mapping 速查资料](https://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf) — 邮件任务示例区分活动层级、叙事顺序和发布切片。**许可：** 未确认开放的图示复用许可；提供链接，并用自己的语言解释。
- [Patton，The New User Story Backlog is a Map](https://www.jpattonassociates.com/the-new-backlog/) — 汽车待办项／切片示例说明，完整的能力覆盖比逐个做完孤立功能更重要。**许可：** 未确认图片改编许可；不要描摹。
- [Nielsen Norman Group，Mapping User Stories in Agile](https://www.nngroup.com/articles/user-story-mapping/) — 手机存入支票的完整地图把活动、详细任务和原型的学习结果联系起来。**许可：** 未确认开放图片许可；仅提供链接。

这些是具体的教学示例，不是三份经过独立核验的生产项目待办列表。已查阅正文和描述，未对图片做视觉复核。

## 绘制方法 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 选定目标用户、目标、范围，以及现状或拟议体验。
2. 阅读研究与场景，用简短叙事讲述用户的故事。
3. 将粒度相近的活动从左到右排列，相关任务和细节放在下方。
4. 展开到足以暴露备选方式、缺口和支撑依赖的程度。
5. 定义纵向排序；若要规划交付，选定结果切片或学习切片。
6. 使用简短卡片、对齐的列、明确的切片标签，以及不作为唯一编码的少量颜色。
7. 从头到尾走通所选切片；区分证据、承诺与假设。

**自检清单**
- [ ] 用户、目标和范围明确。
- [ ] 主干构成可理解的叙事。
- [ ] 细节卡片归属正确的活动。
- [ ] 纵向位置和颜色有明确含义。
- [ ] 每个计划切片都有完整的结果或学习目标。
- [ ] 已考虑备选方式、必要依赖和支撑工作。
- [ ] 证据、候选想法和承诺可区分且清晰可读。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 用户文档、端到端测试、界面流程和验收条件为现有任务提供依据。
- 特性开关和发布说明反映声明的可用性；检查对应版本。
- 代码可揭示实现覆盖与依赖，却不能确定用户价值或已约定的优先级。
- 记录 `卡片/切片 | 来源:行号/章节 | 版本 | verified/inferred/doc-only/conflict`。
- 用研究和干系人证据确定目标与优先级；绝不从提交历史生成已承诺的发布计划。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 地图围绕谁的目标展开？活动从哪里开始、到哪里结束？
2. 我们是在描述现有体验、探索想法，还是选择一个增量？
3. 哪些研究确定了活动及重要备选方式？
4. 下一个切片必须达成什么结果或学到什么？
5. 哪些依赖、支撑工作或其他用户角色可能改变这个切片？

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/B2.json` · 布局模板：`grid_table` · 一个 `tables[]` 条目：活动为列，发布切片为行，故事文字写在单元格中。
近似表示：这是一张表格，不绘制任务卡片和切片带；它表达叙事与范围，而不是执行状态列。

## 来源 {#sources}
<!-- skill: omit -->
1. Jeff Patton — *The New User Story Backlog is a Map*（2008）— https://www.jpattonassociates.com/the-new-backlog/ — 访问于 2026-10-14。
2. Jeff Patton — *Story Mapping quick reference* — https://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf — 访问于 2026-10-14。
3. Agile Alliance — *Story Mapping* — https://www.agilealliance.org/glossary/story-mapping/ — 访问于 2026-10-14。
4. Nielsen Norman Group — *Mapping User Stories in Agile* — https://www.nngroup.com/articles/user-story-mapping/ — 访问于 2026-10-14。
5. Nielsen Norman Group — *Journey Mapping 101* — https://www.nngroup.com/articles/journey-mapping-101/ — 访问于 2026-10-14。

## 示例 {#sample}
<!-- skill: path only -->
![B2 示例：网店购物者的用户故事地图，含一个原型切片](/samples/B2-user-story-map.svg)
*网店购物者发现商品、进行比较、结账并跟踪配送；一个原型切片检验完整的购物目标。*
