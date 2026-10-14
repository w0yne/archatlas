---
code: A9
slug: lean-value-stream-map
family: A
names:
  en: Lean Value-Stream Map
  zh: 精益价值流图
  aliases:
    en: [value-stream map, VSM, current-state map, future-state map, material and information flow diagram]
    zh: [价值流程图, 精益价值流程图, 现状图, 未来状态图, VSM]
question: "对于一个产品或服务族，当前的工作流和信息流中，时间和浪费出现在哪里？未来的流程应该是什么样？"
audiences: [流程负责人, 运营与改进团队, 一线员工, 工程与交付负责人]
level: logical
phases: [discovery, review, operate]
scope: "一个产品或服务族，从触发到交付门到门，现状与（单独绘制的）未来状态，含处理时间、等待时间和时间线"
formal:
  kind: method
  ref: "Rother & Shook, Learning to See (Lean Enterprise Institute, 1998); LEI icon set (de-facto, no ISO notation); Martin & Osterling, Value Stream Mapping (2013) for office and service work"
neighbours: [A2, A5, E4, G4, A8]
status: draft
translationOf: en/types/A9-lean-value-stream-map.md
sourceRev: 674f366
reviewed: false
---

# 精益价值流图（Lean Value-Stream Map）

> 一张门到门的图，描绘一个产品或服务的流动：展示处理框、排队、信息流，以及处理时间与等待时间对比的时间线；分别绘制现状图和未来状态图。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
- **问题：** 从触发到交付，时间花在哪里？其中真正的工作占多少？未来的流程应该是什么样？
- **视点：** 一个产品或服务族的运营流程及其绩效，在工作发生的现场观察。LEI 将价值流图析定义为“diagraming every step involved in the material and information flows needed to bring a product from order to delivery”（把产品从订单到交付所需的物料流和信息流中的每一步都画出来）[1]；“it shows the linkage between material flow and information flow. No other tool does this”（它展示物料流与信息流之间的关联，没有其他工具能做到这一点）[1]。按 42010 的说法，它为流程负责人构建“前置时间与浪费”这一关注点。没有对应的 ArchiMate 视点、TOGAF 制品或 C4 model 层级。
- **深层含义：** 这是一种“学会观察”的练习，而不是画图练习：“Having a perfectly drawn current state map is not the point”（画出一张完美的现状图并不是目的）[1]。现状图总是与未来状态图和实施计划配套 [1][4]。
- **不包含：** 物理布局（刻意推后处理 [5]）、详细的任务逻辑和决策、能力以及干系人价值。
- **本站采用的定义：** 这里采用“价值流”的精益含义（Womack 和 Jones 提出；图析方法由 Rother 和 Shook 提出 [2][3]）。它与业务架构中的 A2 价值流 是不同的图，后者不标注时间。TOGAF 指出，精益价值流用于分析和改进信息流或物料流，不适合把阶段与能力做交叉映射 [7]；Business Architecture Guild 也声明其价值流不是精益价值流 [8]。SAFe 的“development value stream”（开发价值流）是第三种、更宽泛的含义 [9]。
- **本站采用的度量：** 活动比（activity ratio，即流动效率（flow efficiency））= ΣPT ÷ 总前置时间；前置时间包含处理时间，因此等待时间 = LT − PT [2]。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 流程负责人、运营与改进团队以及实际干活的人；LEI 建议让“value-creators”（价值创造者）以及供应商和客户都参与进来 [4]。
- **典型场景：**
  1. 网店从下单到送货上门：结账、支付服务商的支付授权、欺诈审核、拣货、打包和移交承运商，用来看清为什么 20 分钟的活要花一天半（示意数字：PT 3 + 5 + 6 + 4 + 2 = 20 min，等待 0.5 + 6 + 10 + 2 + 14 = 32.5 h，前置时间 ≈ 32.8 h，活动比 ≈ 1 %）。
  2. 客户支持：从提问到解决，经客服聊天机器人、升级到客服人员再返回，找出工单在哪里等待。
  3. 退货：从退货申请到退款，跨仓库、财务和支付服务商。
  4. 软件交付：从想法到生产，跨需求受理、构建、测试和发布，使用工单和流水线时间戳 [9]。
  5. 未来状态设计：第二张图，带改善爆炸点（kaizen burst），作为改进计划的基础 [1][6]。
- **何时不用：** 没有真实的观察或数据时（“go and see”现场观察、“count the right things”统计正确的东西 [4]）；战略层面的价值和能力（A2）；系统结构（C 族）；异常和分支逻辑（A5、E 族）。
- **与相邻类型的区别：**
  - 问题是价值如何到达干系人、由哪些能力支撑时，选择 **A2 价值流**；切勿在那里标注时间。
  - 问题是一个案例的任务顺序、决策和异常时，选择 **A5 BPMN 流程**。
  - 问题是每一步由谁或哪个系统完成时，选择 **E4 泳道图**；A9 展示的是工作停留了多久。
  - 问题是构建和发布阶段本身时，选择 **G4 交付流水线**；A9 衡量的是这些阶段周围的等待。
  - 需要多步骤的变革计划时，选择 **A8 目标架构与路线图**；一张未来状态图只是带改善爆炸点的一个目标。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **正式或非正式：** 一种方法，有事实标准的 LEI 图标集（可下载），但没有 ISO 表示法 [1][6]。读者不熟悉精益图标时，使用带标签的方框加图例。
- **必需：**
  - **供应商**（左上）和**顾客**（右上，标注需求速率或节拍时间（takt））[1][6]。
  - **处理框**从左到右排列，每个连续流动区域一个；处理框“stops wherever processes are disconnected and the material flow stops”（在流程断开、物料流停止的地方结束）[1]。
  - 每个处理框下方的**数据框**：周期时间或处理时间（C/T、PT）、换型时间（C/O）、正常运行时间（uptime）、%C&A（完整准确率，percent complete and accurate），以及人员数（办公场景）或可用时间（制造场景）[1][2]。
  - 处理框之间的**库存或排队三角形**，标注数量或等待天数。
  - 顶部的**信息流**：由谁排程或下达工作；手工信息用直线箭头，电子信息用折线箭头 [6]。忽略信息流的价值流图“is like a piece of sheet music that just lists notes randomly”（就像一张只随意罗列音符的乐谱）[5]。
  - 底部的**时间线阶梯**：上层台阶为等待时间，下层台阶为 PT；右侧为合计：总前置时间、ΣPT、活动比，办公类工作还有累计 %C&A（rolled %C&A）[2]。
- **可选：** 推动箭头（条纹）以及表示拉动的超市（supermarket）、先进先出（FIFO）或看板（kanban）图标 [6]；未来状态图上的改善爆炸点 [6]。
- **图例：** 所用图标、单位（分钟、小时、天）以及“current state, mapped on `<date>`”（现状，绘制于某日期），并注明数字来源。
- **命名：** 处理框按所做的工作命名（“Pick”“Pack”），而不是按部门命名；每行数字只用一种时间单位。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### 最佳实践
1. **一个产品或服务族、一个负责人、门到门，** 同时记录工作流和信息流 [1]。
2. **沿着流程走一遍并实地测量**，而不是在会议室里估算 [4]。
3. **快速画出现状图，再画未来状态图；** 把 30/60/90 天的行动嵌套在 18–24 个月的未来状态之中 [4]。
4. **既展示工作，也展示等待；** 浪费藏在等待里，时间线必须同时呈现两者 [1][2]。
5. **先在现有布局内寻找流动方案；** 布局分析放到后面 [5]。

### 反模式
1. **只记录处理时间，** 导致占前置时间大部分的等待时间消失不见 [1][2]。
2. **数字是在会议室里猜出来的**，而不是观察得到或取自系统数据 [4]。
3. **省略信息流** [5]。
4. **只有现状图，没有未来状态图或计划** [1][4]。
5. **混入业务架构内容，** 例如在处理框下方放能力；那属于 A2 [7]。另外，避免把部门当作处理框、过长的回流线和未加说明的图标。

## 范例 {#exemplars}
<!-- skill: omit -->
- [LEI Lexicon: Value-Stream Mapping](https://www.lean.org/lexicon-terms/value-stream-mapping) — 带数据框和时间线的现状与未来状态示例图，并提供图标下载。© Lean Enterprise Institute。
- [Martin & Osterling, Value Stream Mapping, chapter 1 (TKMG PDF)](https://tkmg.com/wp-content/files/VSM-Ch-1.pdf) — 办公场景的现状/未来状态图，含 LT、PT、%C&A、活动比和累计 %C&A；一个清晰的服务业示例。© McGraw-Hill / TKMG。
- [J. Shook, Misunderstandings about value stream mapping (LEI, 2004)](https://www.lean.org/the-lean-post/articles/misunderstandings-about-value-stream-mapping-flow-analysis-and-takt-time/) — 说明为什么信息流必不可少、为什么布局要放到后面。
- [Lucidchart: Value stream mapping symbols and icons](https://lucid.co/diagram/vsm/value-stream-mapping-symbols) — 对标准图标的易读概览。厂商内容。
- [SAFe: Development Value Streams](https://framework.scaledagile.com/development-value-streams) — 该术语在软件交付中的用法。© Scaled Agile。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 范围：一个产品族、门到门的起点和终点、现状或未来状态、日期；标题要传达发现，例如“Order to doorstep: 20 min of work in 33 h”（从下单到送货上门：33 小时里只有 20 分钟在干活）。
2. 顶部带：左边是供应商，右边是顾客并标注需求速率；中间是协调或排程，以及相应的信息流箭头。
3. 中部带：处理框从左到右排列，每个下方有数据框（PT、%C&A、人员数）；处理框之间是标注数量或等待时间的排队三角形。
4. 底部带：时间线阶梯（等待在上，PT 在下），右侧为合计：前置时间、ΣPT、活动比。
5. 未来状态：第二张图，在变更点标注改善爆炸点，顺序和比例保持一致，便于两张图并排对比。
6. 文字：处理框内用简短的工作名称；数字只出现在数据框和时间线中；每行只用一种时间单位。
7. 颜色：处理框用中性色；等待或改善爆炸点用一种强调色；面向不熟悉精益的读者时，用带标签的普通方框代替精益图标，并始终附图例。

**自检清单**
- [ ] 每个处理框都有含 PT 的数据框；处理框之间展示了排队和等待。
- [ ] 合计能对上：ΣPT ≤ 前置时间，且活动比 = ΣPT ÷ 前置时间。
- [ ] 在图旁注明数字来源（观察、抽样、系统数据）和统计期间。
- [ ] 画出了信息流，而不只是工作流。
- [ ] 严格从左到右，没有过长的回流线；处理框是工作步骤，而不是部门。
- [ ] 没有能力或干系人价值阶段（这些属于 A2）。
- [ ] 图上注明现状或未来状态；未来状态图带有与计划挂钩的改善爆炸点。
- [ ] 图标和单位在图例中有说明。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- **对数字化工作有用：** 订单或工单状态历史中的时间戳、CI/CD 流水线日志、PR 从创建 → 合并 → 部署的时间，以及队列或待办事项的停留时长，可以得出每一步的前置时间、PT 和等待时间。
- **处理框：** 看板列、issue 标签和工作流状态枚举（`placed → paid → picked → packed → shipped`）。
- **%C&A 的替代指标：** 返工次数，例如重新打开的工单、失败的构建或被退回到之前状态的订单。
- **必须来自人：** 手工或线下步骤（仓库打包、承运商揽收）、真实的作业时间、等待的原因以及未来状态。注明样本期间。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 问题是流程中的时间和浪费，还是干系人价值和能力？（时间和浪费；否则改用 A2）
2. 哪个产品或服务族？起点和终点是什么？（标准包裹订单，从结账到移交承运商）
3. 数字从哪里来？统计哪个期间？（最近 4 周的系统时间戳，加上实地观察的作业时间）
4. 现状、未来状态，还是两者并排？（两者，先画现状）
5. 受众能看懂精益图标吗？（不能：用带标签的方框加图例）

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/A9.json` · 布局模板：`tree` · 处理步骤是排成一行、从左到右的 `task` 节点，步骤之间放一个 `queue` 节点；流程数据框写在节点的 `sub` 或 `attributes` 中；合计（前置时间、处理时间、活动比）写入 `meta.description`，因为渲染器暂不绘制时间线行。

## 来源 {#sources}
<!-- skill: omit -->
1. Lean Enterprise Institute, Lexicon: "Value-Stream Mapping" — https://www.lean.org/lexicon-terms/value-stream-mapping — 访问于 2026-10-14
2. K. Martin & M. Osterling, *Value Stream Mapping* (McGraw-Hill, 2013), Chapter 1 (TKMG PDF) — https://tkmg.com/wp-content/files/VSM-Ch-1.pdf — 访问于 2026-10-14
3. Lean Enterprise Institute, "6 Guidelines for Moving Toward a Lean Value Stream" (Rother & Shook; *Learning to See*, Shingo Research Prize 1999) — https://www.lean.org/the-lean-post/articles/6-guidelines-for-moving-toward-a-lean-value-stream — 访问于 2026-10-14
4. Lean Enterprise Institute, "10 Tips for Getting the Most Value from Value Stream Mapping" — https://www.lean.org/the-lean-post/articles/10-tips-for-getting-the-most-value-from-value-stream-mapping/ — 访问于 2026-10-14
5. J. Shook, "Misunderstandings About Value Stream Mapping, Flow Analysis, and Takt Time", LEI (4 Mar 2004) — https://www.lean.org/the-lean-post/articles/misunderstandings-about-value-stream-mapping-flow-analysis-and-takt-time/ — 访问于 2026-10-14
6. Lucidchart, "Value Stream Mapping Symbols and Icons" — https://lucid.co/diagram/vsm/value-stream-mapping-symbols — 访问于 2026-10-14
7. TOGAF Series Guide: Value Streams (G178), App. A.3 "Lean Value Stream", The Open Group (mirror PDF) — https://governance.foundation/assets/frameworks/togaf/g178_2%20-%20Value%20Streams.pdf — 访问于 2026-10-14
8. Business Architecture Guild, "Business Architecture Reference Model Workshop" (2019) — https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf — 访问于 2026-10-14
9. Scaled Agile, "Development Value Streams" — https://framework.scaledagile.com/development-value-streams — 访问于 2026-10-14

## 示例 {#sample}
<!-- skill: path only -->
![A9 示例：网店从下单到送货上门的现状图，含处理框、排队以及处理时间与等待时间对比的时间线](/samples/A9-lean-value-stream-map.svg)
*示例待生成（由渲染器根据 `examples/` 生成）。*
