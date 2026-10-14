---
code: B3
slug: feature-tree
family: B
names:
  en: Feature tree (functional decomposition)
  zh: 功能树（功能分解）
  aliases:
    en: [functional decomposition, requirements breakdown structure, feature breakdown]
    zh: [需求树, 功能分解图, 需求分解结构, 特性树, 功能特性树]
question: 产品必须做什么？这些功能如何分解？
audiences: [product, developers]
levels: [concept]
phases: [requirements]
scope: system
formal: {kind: convention, ref: 'Functional hierarchy — https://sebokwiki.org/wiki/Logical_Architecture; variability mode uses FeatureIDE conventions'}
neighbours: [B2, C5]
status: draft
sourceRev: 88db750
translationOf: en/types/B3-feature-tree.md
reviewed: false
---

# 功能树与功能分解（Feature tree and functional decomposition）

> 把产品功能自上而下分解到可估算的叶子，并标出优先级；不表达流程，也不表达代码结构。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
功能层次图回答：**系统必须做什么，整体功能如何分解？** 它关注功能覆盖，而不是执行顺序或源代码结构 [1][2]。
**本站采用的定义：** B3 默认指非正式的产品功能分解（业务能力属于 A1）。需求分解是相关的可追溯性模式；软件产品线的*特性模型*则是另一种可变性模式，用于定义合法的特性选择组合 [3–5]。
网店的“履行订单”可以分解为若干功能。可配置产品的配送选项则需要选择规则和约束。普通树形结构不会让这些含义变成同一回事。
静态层次图不表达输入／输出行为、运行顺序、物理分配，也不能证明质量要求已经满足。NASA 和 SEBoK 都描述了结合行为／接口视图开展迭代分析的方法 [1][2]。
MoSCoW 是可选的优先级注释，不是树的语法；“Won't Have”表示*这次不做*。没有通用的深度要求，也没有“叶节点必须可估算”的统一规则 [6]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 产品分析师、系统工程师、架构师、测试人员和产品线工程师。
- **场景：** 分解网店的整体功能；审查功能覆盖；建立上层需要与下层需求之间的追溯关系；定义网店支持的产品版本；检查可配置配送选项是否冲突。
- **何时不用：** 证明工作流正确性、容量或接口完整性；未做功能分析就列出文件夹。
- 需要叙事／发布切片时，选择 **B2 用户故事地图**；需要行为时，选择 **E2 活动图／流程图**。
- 需要表达相互协作的职责，而不是功能清单时，选择 **C5 逻辑架构**。
- **WBS** 分解工作／交付物；**模块树**分解实现；两者都不自动等于功能树。
- 当共享或横切需求使严格树形结构产生误导时，使用需求关系图或矩阵。
- 只有当问题是合法组合，而不是功能覆盖或优先级时，才选择**可变性模式**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **功能模式：** 有名称的根节点／范围、功能节点，以及明确的“分解为”连线；优先使用动宾标签 [1][2]。
- **需求模式：** 稳定 ID 和链接的可测试陈述；说明连线表示细化、派生还是覆盖。位于父节点之下不等于证明存在逻辑推导。
- **树形连线：** 通常无方向；若方向为父节点 → 子节点，表示分解，而不是执行或数据传输。
- **可选：** 优先级、发布版本、所有权、验证引用和证据标签；将它们与结构含义分开。
- **可变性模式：** 声明语言／工具。在 FeatureIDE 的布尔特性约定中，选择子特性就要求选择其父特性 [4][5]。
- **必选／可选子特性：** 在 AND 分组中，实心／空心圆标记表示选中父特性时是否必须选中子特性；两种标记都不表示优先级。
- **OR／XOR 分组：** 选中父特性时，分别要求至少选择一个／恰好选择一个组内子特性；使用文档规定的实心／空心分组弧线。
- **跨树约束：** 显式写出 `A ⇒ B` 或 `¬(A ∧ B)` 等规则；它们不是分解箭头。
- **验证：** 分析可满足性、死特性和伪可选特性；其他约束可能使名义上可选的特性变成必选 [7]。
- **图例与细节：** 解释所选模式、分组标记、注释和任何有向连线；同级元素保持相近粒度。质量约束可以跨越分支。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- 先选建模模式；不要把所有功能列表都叫作正式特性模型 [3–5]。
- 同级元素的类型和分解依据保持一致；不要在同一组中混合功能、模块和项目任务 [1][2]。
- 结合行为和接口分析迭代；不要把静态分解当作交换过程能正常工作的证明 [1][2]。
- 保留需求来源和横切约束；避免重复需求各自变化，或将质量需要藏在无关分支中。
- 分析完整的可变性模型，并将优先级单独处理；不要仅因树形图看起来合理就宣布配置合法 [5–7]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [SEBoK，Logical Architecture，图 1](https://sebokwiki.org/wiki/Logical_Architecture) — 具体的功能层次图展示了分解方式及静态结构的局限。**许可：** 该图署名 Faisandier／Sinergy'Com，并保留其他权利；仅提供链接。
- [FeatureIDE，Hello World 教程](https://github.com/FeatureIDE/FeatureIDE/wiki/Tutorial) — 将特性模型与配置及生成的产品联系起来。**许可：** 未确认逐图许可；软件许可证并不一概授权复用 wiki 图片。
- [FeatureIDE: Background，GraphLibrary 模型，第 7 页幻灯片](https://featureide.github.io/slides/featureide-0-background.pdf) — 分组类型加上 `Cycle ⇒ Directed`，说明跨树约束为何重要。**许可：** 未确认幻灯片图片复用许可；不要描摹。

这些范例展示不同的建模模式，而不是同义概念。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 选择功能、需求或可变性模式，并明确命名。
2. 确定根节点、边界、受众、基线和来源证据。
3. 统一节点类型与名称，为每条父子关系提供理由。
4. 用明确的交叉连线或表格保留共享需求和质量约束。
5. 对可变性模式，声明表示法并验证分组／跨树约束。
6. 从上到下或从左到右排版，同级对齐，标签简短，克制用色，并附图例。
7. 细化到有助于当前决策即可；用聚焦的子视图承载细节，不要省略重要约束。

**自检清单**
- [ ] 模式、根节点和边界明确。
- [ ] 同级元素类型和粒度一致。
- [ ] 分解、可追溯性和选择约束保持区别。
- [ ] 质量约束和需求来源得到保留。
- [ ] 优先级没有伪装成必选／可选规则。
- [ ] 适用时，已检查可变性约束和特性异常。
- [ ] 标签、标记、交叉连线和证据清晰可读。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- 需求、验收测试和产品文档为功能覆盖提供依据。
- 处理程序和接口为已实现的职责提供依据；目录不能定义功能。
- 特性模型文件、构建配置、验证器和配置测试为可变性主张提供依据。
- 单个布尔开关不能定义完整的软件产品线特性模型。
- 记录 `元素/关系 | 路径:行号/模型 ID | 版本 | verified/inferred/doc-only/conflict`。
- 已批准的范围、派生理由和优先级，需要代码之外的需求／决策证据。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 我们是在组织功能、追溯需求，还是定义合法配置？
2. 根节点的范围是什么？采用现状还是拟议基线？
3. 哪些需求或模型文件是权威依据？
4. 哪些依赖或质量约束跨越层次结构？
5. 叶节点的细节应支持什么决策？优先级是否相关？

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/B3.json` · 布局模板：`tree` · 根是 `system` 节点，功能是 `component` 和 `task` 节点，由父指向子的 `edges` 连接，自上而下排布。
仅支持功能分解：不支持可变性模式（分组标记、约束、语义验证）。

## 来源 {#sources}
<!-- skill: omit -->
1. NASA — *4.3 Logical Decomposition* — https://www.nasa.gov/reference/4-3-logical-decomposition/ — 访问于 2026-10-14。
2. SEBoK — *Logical Architecture* — https://sebokwiki.org/wiki/Logical_Architecture — 访问于 2026-10-14。
3. Kang 等，CMU SEI — *Feature-Oriented Domain Analysis (FODA) Feasibility Study*，CMU/SEI-90-TR-021（1990）— https://www.sei.cmu.edu/library/feature-oriented-domain-analysis-foda-feasibility-study/ — 访问于 2026-10-14。
4. FeatureIDE — *Getting Started tutorial* — https://github.com/FeatureIDE/FeatureIDE/wiki/Tutorial — 访问于 2026-10-14。
5. FeatureIDE — *FeatureIDE: Background*，第 7 页幻灯片（2015）— https://featureide.github.io/slides/featureide-0-background.pdf — 访问于 2026-10-14。
6. Agile Business Consortium — *What is MoSCoW Prioritization?* — https://www.agilebusiness.org/resource/what-is-moscow-prioritization/ — 访问于 2026-10-14。
7. FeatureIDE — *Feature Diagram* — https://github.com/FeatureIDE/FeatureIDE/wiki/Feature-Diagram — 访问于 2026-10-14。

## 示例 {#sample}
<!-- skill: path only -->
![B3 示例：网店的特性树](/samples/B3-feature-tree.svg)
*网店的特性树：根节点、三项功能（浏览、下单、履约）和它们下面的六项细分功能。这是功能层次结构，不是可变性模型。*
