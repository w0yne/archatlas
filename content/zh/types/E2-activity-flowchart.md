---
code: E2
slug: activity-flowchart
family: E
names:
  en: Activity Diagram / Flowchart
  zh: 活动图 / 流程图
  aliases:
    en: [activity diagram, flowchart, program flowchart, control-flow diagram, process flow diagram (informal), workflow diagram (informal)]
    zh: [活动图, 流程图, 程序流程图, 控制流程图, 处理逻辑图]
question: "这一个行为经过哪些步骤？在哪里做判断、在哪里并行执行、在哪里结束？"
audiences: [开发人员, 测试人员, 业务分析师, 解决方案架构师, 运维工程师]
level: logical
phases: [design, build, review]
scope: "一个行为（一个用例、请求处理器、作业或操作流程），约 8–20 个节点，可选最多 4–5 个分区"
formal:
  kind: standard
  ref: "OMG UML 2.5.1 activity diagrams; ISO 5807:1985 flowchart symbols"
neighbours: [E1, E3, E4, A5, D2]
status: draft
translationOf: en/types/E2-activity-flowchart.md
sourceRev: 72ec5c8
reviewed: false
---

# 活动图 / 流程图（Activity Diagram / Flowchart）

> 一个操作流程的步骤、判断、并行分支和结果，画成从唯一起点到若干具名终点的控制流。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **要回答的问题：** 这个行为经过哪些步骤，在哪里做判断，在哪里并行执行，在哪里结束？
- **视点：** 单个行为的控制流视图（可选加上对象流）：关于条件、分支、并发和终止的“算法或操作流程”视图 [8][9]。
- **两种方言：** **UML 活动图**（OMG UML 2.5.1 [3]）和**经典流程图**；后者用于数据、程序和系统流程图的文档符号由 ISO 5807:1985 标准化 [1][2]。不要在一张图中混用两者的形状。
- **令牌语义：** 从 UML 2 起，活动遵循受 Petri 网启发的令牌流（token flow）语义：当令牌到达某个节点的所有入边时，该节点才执行 [4][5]。这就是汇合（join）绝不能用来合并备选分支的原因。
- **不包含：** 协作参与方之间的消息顺序（E1）、单个对象的状态（E3）、业务事件和池（A5），以及数据结构（D1）。
- **本站采用的定义：** “活动图”指 UML 表示法；“流程图”指非正式风格或 ISO 风格。箭头表示“控制传递到”（对象流则表示“数据传递到”），绝不表示“调用”或“依赖”。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 开发人员、测试人员和分析师；图保持简单时，业务读者也能看懂。
- **典型场景：**
  1. 请求处理逻辑：校验订单、检查库存、并行查询价格和运费报价、合并结果、确认或走降级路径。
  2. 批处理作业或 ETL 步骤：读取、转换、校验、写入，以及错误路径。
  3. 规则或资格校验，例如自动审批退款。
  4. 推导测试路径：每个判断分支对应一个测试用例。
  5. 运维手册（runbook）：新卖家入驻，或恢复一次失败的导入。
- **不适用的情况：** 重点是多个参与者之间相互交接工作（E4、A5）；重点是某个实体的状态（E3）；在一页上画整个系统的行为（应按用例拆分）；简单的线性步骤，此时编号列表更清楚。
- **与相邻图型的区别：**
  - 同一对象在其生命周期内响应事件，选 **E3 状态机图**；一个操作流程从头执行到结束，选 E2。
  - 职责交接是重点时，选 **E4 泳道图**。UML 活动图原生支持*活动分区（activity partition）*（即泳道）[9]，所以 E4 本质上就是带分区的 E2；在这里用少量分区没有问题。
  - 面向业务受众、标准业务事件或自动化业务流程，选 **A5 BPMN**。有研究比较了 BPMN 与 UML 活动图对新手的可读性 [10][11]；这里只读了二手综述。
  - 谁和谁交互、顺序如何比判断逻辑更重要时，选 **E1 时序图**。
  - 箭头表示数据而不是控制时，选 **D2 数据流图**。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式还是非正式：** UML 活动图是正式表示法 [3]；流程图的符号由 ISO 标准化，但实际上普遍以非正式方式使用。
- **必需元素（UML）：**
  - **初始节点**（实心圆），恰好一个。
  - **动作**（圆角矩形），以“动词+对象”命名。
  - **控制流**（箭头）。
  - **终止节点：** 活动终止（靶心）结束整个活动；流终止（带 X 的圆）只结束一条路径。
- **判断与合并：** 菱形。判断节点的每条出边都带有方括号中的守卫条件，例如 `[in stock]` 或 `[else]`。合并（merge）把备选分支重新汇到一起，但不做同步 [8][12]。
- **分叉与汇合：** 粗横条。分叉（fork）启动并发流；汇合（join）等待所有入流到达 [8][5]。
- **可选元素：** 对象节点和对象流（在动作之间传递的数据）；活动分区（泳道，纵向或横向）[9]；可中断区域；用于子活动的调用行为动作（耙形符号）；接收事件动作和发送信号动作；注释。
- **ISO 5807 形状**（经典流程图）[1]：端点、处理、判断、输入/输出（平行四边形）、预定义处理、连接符、文档、存储数据。
- **细节层级：** 一个行为，约 8–20 个节点；超出时抽取子活动。
- **命名：** 动作用“动词+对象”；守卫条件是简短的布尔条件；终点是具名结果（“订单已确认”、“已升级至客服”）。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **单一入口，明确出口：** 为每个最终结果命名。
2. **为每个判断分支加守卫条件，** 且条件互斥、完备（使用 `[else]`）[8]。
3. **分叉和汇合只用于真正的并发；** 备选分支用判断和合并。
4. **主路径保持笔直**（自上而下或从左到右）；把异常放到侧边或单独的图中。
5. **用调用行为动作**让图保持小巧，并把图写成代码（Mermaid、PlantUML），以便评审和比对差异 [6][7]。

### 反模式
1. **判断分支没有条件，** 或条件相互重叠。
2. **用汇合来合并备选分支，** 在令牌语义下会造成死锁 [5]。
3. **混用符号体系，** 例如在 UML 活动图中使用 ISO 平行四边形 [1][3]。
4. **意大利面式连线：** 长线来回折返，流线反复交叉。
5. **把整个系统画在一张图里，** 或有很多参与者却没有分区。

## 范例 {#exemplars}
<!-- skill: omit -->
- [uml-diagrams.org: Activity diagram controls](https://www.uml-diagrams.org/activity-diagrams-controls.html) 和 [UML Activity Diagrams](https://www.uml-diagrams.org/activity-diagrams.html) — 初始、终止、判断、合并、分叉、汇合和分区的精确定义，并附完整示例。
- [Sparx Systems: Activity Diagram, UML 2 tutorial](https://sparxsystems.com/resources/tutorials/uml2/activity-diagram.html) — 简明的实践参考，涵盖带守卫条件的判断、分叉、汇合和分区。
- [PlantUML activity diagram (new syntax)](https://plantuml.com/activity-diagram-beta) — 用文本表达开始/结束、条件、循环、分区和注释；很适合作为自动生成图的目标格式。开源工具。
- [Mermaid flowchart syntax](https://mermaid.ai/open-source/syntax/flowchart.html) — 嵌入最广泛的流程图语法；可在众多代码托管平台和文档站点中渲染。
- [ISO 5807:1985 preview](https://cdn.standards.iteh.ai/samples/11955/1b7dd254a2a54fd7a89d616dc0570e18/ISO-5807-1985.pdf) — 权威的经典符号集。仅为预览；标准本身受版权保护。
- [Visual Paradigm: activity diagrams vs BPMN](https://guides.visual-paradigm.com/a-comparative-analysis-of-activity-diagrams-and-bpmn-in-uml/) — 并列对比，帮助做选择。厂商指南。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 为行为（一个用例或处理器）命名，写明其触发点和结果，并放进标题。
2. 把步骤写成缩进大纲（顺序、`if/else`、`parallel`、`loop`），对照代码或规则核实。绘图前先给用户看。
3. 选定一种方言：UML 活动图（软件领域默认）或 ISO 流程图（适用于要求使用它的组织）。绝不混用。
4. 布局：主路径自上而下（宽幅幻灯片上从左到右）；判断向侧面分支，再在合并节点汇回；并行分支并排放在分叉条与汇合条之间。
5. 如果涉及多个参与者，最多添加 4–5 个分区；超出时改用 E4 或 A5。
6. 文字：动作最多 5 个词；守卫条件最多 5 个词并写在方括号中；形状内不写段落。细节放进编号注释。
7. 颜色：中性填充；最多一种强调色（错误或异常路径），并在图例中说明。
8. 图超过约 20 个节点时，抽取子活动（耙形符号）。

**自检清单**
- [ ] 恰好一个初始节点；每条路径都以具名终点结束。
- [ ] 每条判断出边都有守卫条件；条件互斥且完备。
- [ ] 只在真正并发时使用成对的分叉和汇合；备选分支用合并。
- [ ] 只用一种表示法方言；读者不熟悉 UML 时附图例。
- [ ] 主路径上没有交叉或折返的线。
- [ ] 最多约 20 个节点，否则已抽取子活动。
- [ ] 如有分区，分区是同一层级上的真实参与者。
- [ ] 步骤与代码或规则一致，否则将图标注为设计方案。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **控制流：** 处理器和服务函数中的 `if/switch` 分支、循环、`try/except` 路径，以及并发（`asyncio.gather`、future、线程池、扇出到队列）。
- **声明式流程：** 工作流和流水线定义（YAML 阶段列表、Step Functions 或 Airflow DAG）。
- **开关：** 用于选择路径的特性开关（feature flag）。
- **分支清单：** 测试用例往往列举了各个分支。
- **必须来自人：** 哪些分支对受众重要，以及技术条件对应的业务名称。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 这是哪个行为（一个用例、请求处理器或作业），由什么触发？（结账处理器，由“下单”触发）
2. 要展示哪些结果或终止状态？（每个具名出口，最多 4 个）
3. 只画主成功路径，还是包含关键的备选和错误分支？（主要备选分支画在图内，错误放在单独的图中）
4. 是否涉及多个参与者或系统；要加泳道，还是改用 E4 或 BPMN？（这里最多 3 个分区，否则用 E4）
5. 用 UML 活动图表示法还是经典流程图符号；受众是否期望 BPMN？（UML 活动图）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/E2.json` · 布局模板：`lanes` · 动作、判断、分叉和终点是 `nodes`（`kind` 承载 UML 形状），按自上而下的流向布局；分区是 `lane` 分组；控制流是 kind 为 `call` 的 `edges`，守卫条件作为 `label`，对象流使用 kind `data`。

## 参考来源 {#sources}
<!-- skill: omit -->
1. ISO 5807:1985 — https://www.iso.org/standard/11955.html — 访问于 2026-10-14
2. ISO 5807:1985 preview (iTeh) — https://cdn.standards.iteh.ai/samples/11955/1b7dd254a2a54fd7a89d616dc0570e18/ISO-5807-1985.pdf — 访问于 2026-10-14
3. OMG, UML 2.5.1 (formal/17-12-05) — https://www.omg.org/spec/UML/2.5.1/About-UML — 访问于 2026-10-14
4. Sparx Systems Central Europe, "UML activity diagram: activities and connections"（源自 Petri 网的令牌语义）— https://www.sparxsystems.eu/languages/uml/diagrams/activitydiagram/ — 访问于 2026-10-14
5. "An ASM Semantics of Token Flow in UML 2 Activity Diagrams" (ResearchGate) — https://www.researchgate.net/publication/220810272_An_ASM_Semantics_of_Token_Flow_in_UML_2_Activity_Diagrams — 访问于 2026-10-14
6. Mermaid, "Flowcharts Syntax" — https://mermaid.ai/open-source/syntax/flowchart.html — 访问于 2026-10-14
7. PlantUML, "Activity Diagram (new syntax)" — https://plantuml.com/activity-diagram-beta — 访问于 2026-10-14
8. uml-diagrams.org, "UML activity diagram controls" — https://www.uml-diagrams.org/activity-diagrams-controls.html — 访问于 2026-10-14
9. uml-diagrams.org, "UML Activity Diagrams"（分区与泳道）— https://www.uml-diagrams.org/activity-diagrams.html — 访问于 2026-10-14
10. Visual Paradigm Guides, "A Comparative Analysis of Activity Diagrams and BPMN in UML" — https://guides.visual-paradigm.com/a-comparative-analysis-of-activity-diagrams-and-bpmn-in-uml/ — 访问于 2026-10-14
11. "A Comparison of BPMN and UML 2.0 Activity Diagrams" (ResearchGate) — https://www.researchgate.net/publication/228965384_A_Comparison_of_BPMN_and_UML_20_Activity_Diagrams — 访问于 2026-10-14
12. Visual Paradigm Online, "Activity Diagram Tutorial"（分叉与汇合的定义）— https://online.visual-paradigm.com/diagrams/tutorials/activity-diagram-tutorial/ — 访问于 2026-10-14
13. Sparx Systems, "Activity Diagram — UML 2 Tutorial" — https://sparxsystems.com/resources/tutorials/uml2/activity-diagram.html — 访问于 2026-10-14

注：UML 2.5.1 的条款原文未亲自阅读；元素语义取自来源 4、8、9 和 12，未对照原文核实。

## 示例图 {#sample}
<!-- skill: path only -->
![E2 示例：网店结账活动流程，包含库存检查、价格与运费报价并行分支、支付判断和具名结果](/samples/E2-activity-flowchart.svg)
*示例图待生成（由渲染器根据 `examples/` 生成）。*
