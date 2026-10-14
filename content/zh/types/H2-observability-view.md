---
code: H2
slug: observability-view
family: H
names:
  en: Observability view
  zh: 可观测性视图
  aliases:
    en: [observability architecture diagram, monitoring architecture diagram, telemetry pipeline diagram]
    zh: [可观测性架构图, 监控架构图, 遥测流水线图]
question: 服务行为的证据如何进入分析、检测，并传递给能够采取行动的人？
audiences: [operations, developers, leaders]
levels: [physical]
phases: [operate]
scope: 某个环境中的遥测路径及相关运维响应。
formal: {kind: convention, ref: '没有统一的图形标准；参考 OpenTelemetry 信号概念：https://opentelemetry.io/docs/concepts/signals/ 以及 SRE 监控实践：https://sre.google/sre-book/monitoring-distributed-systems/'}
neighbours: [G1, G4, H1]
status: draft
sourceRev: a082cec
translationOf: en/types/H2-observability-view.md
reviewed: false
---

# 可观测性视图

> 从运行中服务的遥测数据，到分析、告警，再到负责响应的人的完整路径。

## 含义 {#meaning}
<!-- skill: condense (4–6 lines) -->
可观测性视图说明服务行为的证据如何用于诊断、检测或响应。更深层的关注点是这条路径是否可信：上下文缺失、数据丢失或告警无人负责，都可能使其失效。

**本站采用的定义：** 一种非正式的运维视图，不是正式表示法，也不对应固定的 C4 model 层级。OpenTelemetry 规定遥测行为，而非绘图符号。仅有 Collector 并不构成存储、可视化或呼叫值班人员的告警后端 [1][2]。

指标、日志和链路追踪是常见信号，并非只有这“三大支柱”。剖析数据与上下文传播也很重要；应检查具体组件的支持情况和成熟度 [1][3][4]。省略无关业务逻辑及穷尽式指标清单。

## 何时使用与如何选择 {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **受众：** 服务负责人、开发人员、运维人员和响应人员。
- **场景：** 评审结账服务的就绪情况；诊断网店请求缓慢的问题；设计采集拓扑；补齐事故后发现的监控缺口。
- **选择范围：** 遥测流水线、采集器部署，或检测与响应。单图无法解释三者时，应拆分视图。
- **不适用：** 单个请求用链路追踪或时序图，当前测量结果用仪表盘，静态依赖用组件图。
- **G1 部署 / G4 交付流水线：** 它们解释承载或发布机制，不说明运维证据是否到达使用环节。
- **H1 RACI：** 用于职责分配；响应步骤可链接到运维手册。
- 视图声称覆盖相应可靠性或响应能力时，才需要 SLO 与值班告警细节；并非每张剖析视图或仅涉及采集器的视图都要包含这些内容。

## 表示法与元素 {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **必需：** 服务与环境范围、信号来源、相关采集/处理/目的端、带标签的关系、边界及图例。
- **按需必备：** 检测与响应视图需要测量定义、检测策略、通知路径、响应人员及行动参考资料；缺失项须明确标出。
- **数据箭头：** 生产方 → 接收方 → 目的端。拉取式采集需区分抓取请求方向与指标响应方向。
- **其他箭头：** 分别标注查询、上下文传播、通知和修复。上下文随应用调用或消息传播，并非导出到后端的数据流。
- **Collector 流水线：** 接收器 → 可选的有序处理器 → 导出器；连接器可以连接流水线。配置必须在 `service.pipelines` 中启用组件 [2][5]。
- **通常可选、影响含义时必需：** 副本、协议、队列、重试、保留策略、采样和敏感信息遮蔽。应展示会改变证据的转换处理。
- **SLI/SLO：** 前者是测量定义，后者是某个时间窗口内的目标；告警条件与二者均不同。对于良好事件占比，允许的不良事件比例为 `1 − SLO` [6][7]。
- **标签：** 采用简短的功能名称；信号与协议标在线上。使用独立的证据标记，避免虚线同时表示“异步”和“未核实”。

以部署为重点的视图很常见，但逻辑遥测流水线与服务级响应视图同样适用。这类视图没有统一版本。访问时，OpenTelemetry 的 Profiles 页面标注为 Alpha；baggage 携带上下文，不意味着需要另建一条存储流水线 [1][3][4]。

## 最佳实践与反模式 {#practice}
<!-- skill: condense (top 5 each, no citations) -->
| 最佳实践 | 反模式 |
| --- | --- |
| 从用户可感知的行为和能够触发行动的检测出发 [7][8]。 | 将主机健康仪表盘当作完整的服务监测覆盖。 |
| 跨服务与消息边界关联证据 [1]。 | 认为导入 SDK 就证明链路已经连通。 |
| 明示采样、处理器顺序及路由假设 [5][9]。 | 在有状态的尾部采样之前任意分配负载。 |
| 展示影响含义的遥测丢失与敏感数据边界 [10][11]。 | 将队列画成无损保障，或声称下游遮蔽能防止上游暴露。 |
| 核实路径与响应责任归属，并监控采集系统本身 [8][10]。 | 将数据缺失视为健康，或将已通知视为已完成修复。 |

黑盒症状与白盒诊断相互补充。黄金信号——延迟、流量、错误和饱和度——是监控关注点，不是遥测格式类别 [8]。错误预算消耗速率告警需要适当的流量和评估窗口；公开阈值是示例，不是普遍适用的默认值 [7]。

## 范例 {#exemplars}
<!-- skill: omit -->
- [OpenTelemetry — Collector Architecture，流水线图](https://opentelemetry.io/docs/collector/architecture/) — 清楚展示顺序处理与导出器扇出；文档采用 CC BY 4.0，改编时需署名并注明修改，同时留意具体素材的例外条款。
- [OpenTelemetry — Gateway deployment pattern](https://opentelemetry.io/docs/collector/deploy/gateway/) — 包含实际元素的单层与双层图，区分转发和有状态路由；文档采用 CC BY 4.0，同样需检查署名要求和具体素材条款。
- [OpenTelemetry — Agent-to-gateway deployment pattern](https://opentelemetry.io/docs/collector/deploy/other/agent-to-gateway/) — 区分主机本地采集与共享处理，并解释尾部采样的约束；文档采用 CC BY 4.0，但不保证所有发行版均支持图中能力。
- [Prometheus — Overview，架构图](https://prometheus.io/docs/introduction/overview/) — 区分发现、抓取、规则求值、告警处理与可视化；文档仓库采用 Apache-2.0，复制前需检查适用声明及具体素材条款。

这里提供架构范例链接，不复制图形。SRE workbook 的插图采用 CC BY-NC-ND 4.0 条款；应自行撰写说明并链接原书，不应改编其插图后进行不受限制的再分发 [6][7]。文档许可证见 [13][14]。

## 绘制步骤 {#recipe}
<!-- skill: keep (≤25 lines) -->
1. 确定运维问题、环境，以及现状或目标态。
2. 沿实际配置追踪每种相关信号，从已启用的埋点直到使用环节。
3. 加入关联、处理、采样，以及影响含义的信任边界与故障边界。
4. 响应范围内应串起测量 → 检测 → 通知 → 响应人员/运维手册；区分 SLO 和告警策略。
5. 来源放左侧，处理放中间，目的端放右侧；响应放下方。仅在讨论部署时按主机分组。
6. 使用简短功能标签、带标签的箭头、克制的配色及证据图例；与配置逐一核对。

**自检清单**
- [ ] 范围与环境明确。
- [ ] 来源能到达所述使用环节，或明确显示缺口。
- [ ] 数据、抓取请求、查询、上下文与通知清楚区分。
- [ ] 已启用的流水线及处理器顺序符合证据。
- [ ] 已检查组件与信号支持情况。
- [ ] 采样、丢失和敏感信息遮蔽的假设清晰可见。
- [ ] 所声称的响应能力有测量、策略、负责人及行动支撑。
- [ ] 未将配置意图表述为已观察到的运行成功。

## 代码仓库中的证据 {#evidence}
<!-- skill: keep (≤10 lines) -->
- SDK 初始化与导出器设置可识别配置中的信号生成方式和目的端。
- Collector 流水线、部署覆盖配置与抓取发现配置可识别已启用的路径。
- 中间件和消息处理器揭示上下文传播与关联缺口。
- 规则、通知路由和运维手册支持关于检测与响应的描述。
- 记录路径、修订版本、环境及证据状态；运行成功需要运行时证据。绝不能仅凭命名推断存在 SLO 或已安排到岗的响应人员。

## 引导模式问题 {#questions}
<!-- skill: keep (≤8 lines) -->
1. 目标是采集、诊断、就绪评估，还是遥测治理？
2. 哪个环境、状态与配置是权威依据？
3. 必须解释哪些用户行为及可用信号？
4. 哪些目标、告警路径、响应负责人和数据约束已达成一致？

## 模板 {#template}
<!-- skill: keep (≤3 lines) -->
模型模板：`assets/templates/H2.json` · 布局模板：`layered` · 各层（埋点、采集、分析、响应）是 `layer` 分组，内含 `component`、`store` 和 `person` 节点，层间用 `data` 和 `async` 边连接，拟议策略使用样式 `planned`。
部署边界改用 `nested` 布局和 `boundary` 分组。

## 来源 {#sources}
<!-- skill: omit -->
1. OpenTelemetry — Signals — https://opentelemetry.io/docs/concepts/signals/ — 访问于 2026-10-14。
2. OpenTelemetry — Collector Architecture — https://opentelemetry.io/docs/collector/architecture/ — 访问于 2026-10-14。
3. OpenTelemetry — Profiles — https://opentelemetry.io/docs/concepts/signals/profiles/ — 访问于 2026-10-14。
4. OpenTelemetry — Specification Status Summary — https://opentelemetry.io/docs/specs/status/ — 访问于 2026-10-14。
5. OpenTelemetry — Collector Configuration — https://opentelemetry.io/docs/collector/configuration/ — 访问于 2026-10-14。
6. Google, The Site Reliability Workbook — Implementing SLOs — https://sre.google/workbook/implementing-slos/ — 访问于 2026-10-14。
7. Google, The Site Reliability Workbook — Alerting on SLOs — https://sre.google/workbook/alerting-on-slos/ — 访问于 2026-10-14。
8. Google, Site Reliability Engineering — Monitoring Distributed Systems — https://sre.google/sre-book/monitoring-distributed-systems/ — 访问于 2026-10-14。
9. OpenTelemetry — Agent-to-gateway deployment pattern — https://opentelemetry.io/docs/collector/deploy/other/agent-to-gateway/ — 访问于 2026-10-14。
10. OpenTelemetry — Collector Resiliency — https://opentelemetry.io/docs/collector/resiliency/ — 访问于 2026-10-14。
11. OpenTelemetry — Handling sensitive data — https://opentelemetry.io/docs/security/handling-sensitive-data/ — 访问于 2026-10-14。
12. OpenTelemetry — Gateway deployment pattern — https://opentelemetry.io/docs/collector/deploy/gateway/ — 访问于 2026-10-14。
13. OpenTelemetry 文档 — LICENSE，CC BY 4.0 — https://github.com/open-telemetry/opentelemetry.io/blob/main/LICENSE — 访问于 2026-10-14。
14. Prometheus 文档 — LICENSE，Apache-2.0 — https://github.com/prometheus/docs/blob/main/LICENSE — 访问于 2026-10-14。
15. Prometheus — Overview — https://prometheus.io/docs/introduction/overview/ — 访问于 2026-10-14。

## 示例 {#sample}
<!-- skill: path only -->
![H2 示例：网店结账的可观测性](/samples/H2-observability-view.svg)
*从结账埋点到采集、分析，以及有明确负责人的告警路径。告警策略是拟议的，不是实际测得的行为。*
