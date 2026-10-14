---
code: A6
slug: journey-map
family: A
names:
  en: Customer or user journey map
  zh: 用户旅程图
  aliases:
    en: [customer journey map, user journey map, UX journey map, CJM, journey map]
    zh: [客户旅程图, 顾客旅程地图, 体验旅程图]
question: 一个用户画像为达成一个目标，逐阶段经历了什么：做了什么、想了什么、感受如何；痛点在哪里；每项改进由谁负责？
audiences: [product, business, leaders]
levels: [strategy, concept]
phases: [initiate, requirements]
scope: 一个用户画像、一个场景与目标、一个产品或服务、4–7 个阶段，从客户视角出发。
formal: {kind: convention, ref: 'none (de-facto reference: Nielsen Norman Group journey-mapping guidance)'}
neighbours: [A2, A4, A5, B2, E4]
status: draft
translationOf: en/types/A6-journey-map.md
sourceRev: a5d2191
reviewed: false
---

# 用户旅程图 / 客户旅程图（Customer / User Journey Map）

> 一个用户画像追求一个目标的逐阶段图景：上方是行为、想法和唯一一条情绪曲线，下方是痛点和有负责人的机会点。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
旅程图回答的是：“这个人为达成这个目标经历了什么，哪里让他难受？”NN/g 将其定义为“对一个人为完成某个目标所经历过程的可视化” [1]。它的要义在于**由外而内**（outside-in）的视角：呈现顾客的过程，而不是公司的过程。按 ISO/IEC/IEEE 42010 的说法，它服务于体验视点。它不是 TOGAF 制品（TOGAF 中最接近的技术是业务场景），ArchiMate 没有旅程元素，C4 model 也不涵盖它。它有意排除内部流程和系统（作为触点名称出现的除外）、界面点击路径以及额外的用户画像 [1][7]。

**本站采用的定义：**旅程图有三个区域：**视角设定**（lens：一个用户画像（persona）、一个场景、期望）、**体验**（阶段、行为、想法、情绪）和**产出**（带负责人和指标的机会点）[1][2]。**体验地图**（experience map）*不是*同义词：它与具体产品无关，描述的是一类通用的人类活动 [3]。**服务蓝图**（service blueprint）是一个独立的相邻类型，有自己的表示法，不是本类型的扩展名称：它呈现组织一侧（顾客行为、前台、后台、支持流程、有形证据），以交互线、可视线和内部交互线分隔 [4][9][11]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：**产品、用户体验与服务设计、市场与客户体验、客户支持；高管（握有决策权，却往往最不了解客户）[7]；负责承接待办事项的工程负责人。
- **场景：**网店首次购买（现状），找出顾客付款后联系客服的原因；为重新设计的结账流程描绘未来状态的“北极星”旅程 [6]；跨渠道旅程（网站、App、客服聊天机器人、电话）；工作坊中的假设型旅程图，标注为未经验证，用于规划调研 [6][7]。
- **不适用的情况：**需要系统内部结构（C1、C2、E4）或精确的流程逻辑（A5）；需要与产品无关的通用视图（体验地图）；有多个旅程各不相同的用户画像（每个画像一张图）；没有人会据此采取行动 [2]。
- **与相邻类型的区别：**
  - 在旅程图之后，当问题是组织必须在前台和后台做什么才能交付每个触点时，选**服务蓝图**（Shostack 1984 [9]）；两者共用顾客行为这一行 [4][5]。
  - 要表达某一行蓝图背后的精确交接和分支时，选 **A5 BPMN**。
  - 要把机会点转化为待办事项和发布切片时，选 **B2 用户故事地图**；它是从产品视角讲述的 [8]。
  - 要从战略层面、结合能力来看价值交付且不涉及情绪时，选 **A2 价值流**；要表达角色 × 活动的范围时，选 **A4 场景矩阵**。
  - 要在早期综合访谈结果时，选**同理心地图**（empathy map）；它没有时间顺序 [3]。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **没有正式标准**：ISO、OMG 和 Open Group 都没有相应表示法。稳定的是组成部分，而不是图形符号 [1][2]。
- **视角设定（必需）：**恰好一个用户画像，尽可能来自调研；一个场景，含用户画像的目标和期望 [1]。
- **体验（必需）：**4–7 个阶段，作为等宽列从左到右排列；行为行（每个阶段一段叙述，不是点击日志）；想法行（第一人称引语，尽可能原话）；贯穿所有阶段的**唯一一条情绪曲线**，以中性中线为界，上方为正面 [1]。
- **可选：**触点 / 渠道行（网站、App、聊天机器人、电子邮件、电话）；在情绪曲线低谷处标注痛点。
- **产出（必需）：**机会点，每个都有一个内部负责人，已知时附上指标 [1][2]。
- **状态元数据（须在图上注明）：**现状还是未来状态；基于调研还是假设 [3][6]。
- **线条：**情绪曲线是唯一的连续线；列的顺序已表示先后，因此很少需要箭头。
- **命名：**阶段用顾客的语言（“比较商品”，而不是“线索资格评估”）；想法用第一人称（“周五前能到吗？”）。
- **图例：**情绪刻度、痛点和机会点标记、渠道图标。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践

1. 从业务目标和旅程图的使用者出发，再选定一个角色和一个场景 [2][7]。
2. 以定性调研为基础；定量数据可以支撑故事，但不能单独构建故事 [2][7]。
3. 事先确定是现状还是未来状态；常见路线是现状假设 → 调研验证 → 未来状态愿景 [6]。
4. 先综合再可视化，并由市场、客服、销售和产品协作完成旅程图 [2][7]。
5. 形成闭环：每个机会点都有负责人和指标，输入故事地图或待办列表，并持续更新旅程图 [1][2][8]。

### 反模式

1. 把公司的流程包装成旅程，阶段以部门命名；那其实是服务蓝图或 BPMN 图 [3]。
2. 一张图上有多个用户画像，或者一个“平均用户” [3][7]。
3. 假设型旅程图未经验证，或没有醒目的“假设”标签，就被用于重要决策 [6][7]。
4. 没有业务目标、没有负责人：一张精美的海报，什么也没改变 [2]。
5. 行为行里写逐次点击的步骤，或者在一张未加标注的图中混杂现状与未来状态 [1][6]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [NN/g, Journey Mapping 101](https://www.nngroup.com/articles/journey-mapping-101/) — 经典的带注解旅程图，含视角设定 / 体验 / 产出三个区域和一条情绪曲线 [1]。
- [NN/g, Journey Mapping for Remote Teams: A Digital Template](https://www.nngroup.com/articles/journey-map-digital-template/) — 强制包含全部组成部分的模板；可免费使用，再分发前请核对 NN/g 条款 [12]。
- [NN/g, UX Mapping Methods Compared](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/) — 同理心地图、旅程图、体验地图和服务蓝图并列对照；便于选型 [3]。
- [Adaptive Path, Guide to Experience Mapping](https://productstrategy.co/content/files/2023/09/Adaptive_Paths_Guide_to_Experience_Mapping.pdf) — 做 / 想 / 感受三行，以及“所以呢 / 接下来做什么”的结论；许可非商业性改编并须署名 [10]。
- [Shostack, Designing Services That Deliver (HBR, 1984)](https://hbr.org/1984/01/designing-services-that-deliver) — 最早的服务蓝图，含可视线和失败点；展示旅程*之下*的内容。需付费阅读 [9]。
- [Digital.gov, Map your users' and system's journeys](https://digital.gov/guides/research-collaboration/user-needs/journeys) — 属于公有领域的政府指南，含方法步骤 [13]。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定视角设定：一个用户画像（名称 + 一行描述）、一个场景与目标、期望、现状还是未来状态、基于调研还是假设。
2. 用顾客的语言选出 4–7 个阶段，作为等宽列从左到右排列。
3. 各行从上到下：行为、想法（每个阶段一句引语）、情绪曲线、曲线低谷处的痛点、可选的触点、带负责人的机会点。
4. 文字：每个单元格最多 3 条要点，每条不超过 8 个词；整张图只列最重要的 3–6 个机会点，而不是每格一个。
5. 情绪曲线：在中性中线上方画一条平滑曲线；为最差的 1–3 个低谷编号，并在对应的机会点上复用这些编号。
6. 颜色：中性网格；曲线使用一种从中性到警示的渐变（不用彩虹色）；机会点用一种强调色；适用时加上醒目的“假设——待验证”徽标；未来状态的旅程图用不同的表头底色。
7. 表头条：标题写明洞见和状态，例如“首次购买者，现状：付款后没有配送进度更新，导致客服咨询”；用户画像和场景框放在左上角。
8. 后台问题：建议另画一张复用行为行的服务蓝图；不要让旅程图负担过重。

**自检清单**
- [ ] 恰好一个用户画像和一个场景；注明了状态和证据基础。
- [ ] 4–7 个阶段，从顾客视角命名。
- [ ] 行为是每个阶段的叙述；想法是第一人称引语。
- [ ] 只有一条情绪曲线，其低谷与标出的痛点一致。
- [ ] 每个机会点都有负责人（已知时还有指标）。
- [ ] 没有把部门步骤或系统架构伪装成阶段。
- [ ] 图例解释了情绪刻度、标记和图标。
- [ ] 标题承载洞见；假设内容有醒目标签；没有 TBD 或工作备注。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **代码可以提示：**从路由、菜单、页面名称以及电子邮件 / 推送模板推断触点和阶段边界；漏斗和埋点事件（`checkout_started`、`payment_failed`）；围绕痛点的功能开关和实验；客服工单标签、错误信息目录和帮助内容；能解释等待阶段的 SLA 和超时设置；聊天机器人意图和兜底日志。
- **需要问人：**真实的用户画像、想法、情绪和期望，系统之外的阶段（访问前的调研、口碑），以及痛点的严重程度。这些来自用户调研、客服人员、调查问卷原话和产品团队。
- 仅凭代码画出的旅程图是**假设型旅程图**，必须如实标明。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 谁的旅程？哪个目标或场景？（最常见旅程上的主要用户画像）
2. 用现状来找痛点，还是用未来状态作为目标愿景？（现状，除非在设计新东西）
3. 有哪些证据：访谈、客服工单、分析数据，还是只有团队经验？（只有团队经验 → 标注为假设）
4. 从最初触发到结果，有哪些阶段？（提议一组 4–7 个阶段供用户确认）
5. 只要顾客视角，还是同时要一张展示每个触点背后发生什么的服务蓝图？（只要旅程）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A6.json` · 布局模板：`grid_table` · 阶段为列，各组成部分（行为、想法、情绪、痛点、触点、机会点）为表格行；情绪行每个阶段写一个词（渲染器暂不绘制情绪曲线）；首列表头不能为空（用 `Row`）。

## 来源 {#sources}
<!-- skill: omit -->
1. Sarah Gibbons, NN/g, Journey Mapping 101 (2018) — https://www.nngroup.com/articles/journey-mapping-101/ — 访问于 2026-10-14
2. Kate Kaplan, NN/g, When and How to Create Customer Journey Maps (2016) — https://www.nngroup.com/articles/customer-journey-mapping/ — 访问于 2026-10-14
3. Sarah Gibbons, NN/g, UX Mapping Methods Compared: A Cheat Sheet (2017) — https://www.nngroup.com/articles/ux-mapping-cheat-sheet/ — 访问于 2026-10-14
4. Sarah Gibbons, NN/g, Service Blueprints: Definition (2017) — https://www.nngroup.com/articles/service-blueprints-definition/ — 访问于 2026-10-14
5. Gibbons & Kendrick, NN/g, Service Blueprinting FAQ (2019) — https://www.nngroup.com/articles/service-blueprinting-faq/ — 访问于 2026-10-14
6. Kate Kaplan, NN/g, Journey-Mapping Approaches: 2 Critical Decisions (2020) — https://www.nngroup.com/articles/journey-mapping-approaches/ — 访问于 2026-10-14
7. Kendrick & Kaplan, NN/g, Journey Mapping: 9 Frequently Asked Questions (2019) — https://www.nngroup.com/articles/journey-mapping-faq/ — 访问于 2026-10-14
8. Anna Kaley, NN/g, Mapping User Stories in Agile (2021) — https://www.nngroup.com/articles/user-story-mapping/ — 访问于 2026-10-14
9. G. Lynn Shostack, Designing Services That Deliver, Harvard Business Review, Jan 1984 — https://hbr.org/1984/01/designing-services-that-deliver — 访问于 2026-10-14
10. Adaptive Path, Adaptive Path's Guide to Experience Mapping (2013) — https://productstrategy.co/content/files/2023/09/Adaptive_Paths_Guide_to_Experience_Mapping.pdf — 访问于 2026-10-14
11. Service Design Tools, Service Blueprint — https://servicedesigntools.org/tools/service-blueprint — 访问于 2026-10-14
12. NN/g, Journey Mapping for Remote Teams: A Digital Template — https://www.nngroup.com/articles/journey-map-digital-template/ — 访问于 2026-10-14
13. Digital.gov, Map your users' and system's journeys — https://digital.gov/guides/research-collaboration/user-needs/journeys — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A6 示例：首次购物者的旅程图，含行为、想法、情绪、痛点、触点和机会点](/samples/A6-journey-map.svg)
*一个用户画像——首次购物者——经历四个阶段（发现、比较、下单、收货）的旅程，标注为假设和现状。各行依次是行为、想法、情绪（每个阶段一个词，不画情绪曲线）、痛点、触点，以及带负责方的机会点。*
