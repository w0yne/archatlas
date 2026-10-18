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
question: How does evidence of service behavior reach analysis, detection, and someone who can act?
audiences: [operations, developers, leaders]
levels: [physical]
phases: [operate]
scope: An environment's telemetry paths and relevant operational response.
formal: {kind: convention, ref: 'No diagram standard; OpenTelemetry signal concepts: https://opentelemetry.io/docs/concepts/signals/ and SRE monitoring practice: https://sre.google/sre-book/monitoring-distributed-systems/'}
neighbours: [G1, G4, H1]
status: draft
sourceRev: '2026-10-14'
---

# Observability view (可观测性视图)

> The path from telemetry in the running service to analysis, alerts and the people who respond.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
An observability view explains how evidence of service behaviour becomes useful for diagnosis, detection, or response. Its deeper concern is the credibility of that path: missing context, dropped data, or an unowned alert can break it.

**Definition used here:** an informal operational view, not a formal notation or fixed C4 model level. OpenTelemetry specifies telemetry behaviour, not drawing symbols. A Collector alone is not a storage, visualization, or paging backend [1][2].

Metrics, logs, and traces are common signals, not a closed set of three pillars. Profiles and context propagation also matter; check component-specific support and maturity [1][3][4]. Omit unrelated business logic and exhaustive metric inventories.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** service owners, developers, operators, and responders.
- **Scenarios:** reviewing checkout readiness; diagnosing slow shop requests; designing collection topology; closing monitoring gaps after an incident.
- **Choose scope:** telemetry pipeline, collector deployment, or detection/response. Split views when one figure cannot explain all three.
- **When not:** use a trace/sequence for one request, a dashboard for current measurements, or a component diagram for static dependencies.
- **G1 deployment / G4 delivery pipeline:** those explain hosting or release machinery, not whether operational evidence reaches its use.
- **H1 RACI:** use it for responsibility assignments; link a runbook for response steps.
- SLO and paging details are required for a corresponding reliability/response claim, not for every profiling or collector-only view.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required:** service/environment scope, signal sources, relevant acquisition/processing/destinations, labeled relations, boundaries, and a legend.
- **Conditional:** detection/response views need measurement definition, detection policy, notification route, responder, and action reference or explicit gaps.
- **Data arrows:** producer → receiver → destination. For pull collection, distinguish scrape-request direction from metric-response direction.
- **Other arrows:** label queries, context propagation, notifications, and remediation separately. Context travels with application calls/messages, not a backend export.
- **Collector pipeline:** receivers → optional ordered processors → exporters; connectors can join pipelines. Configuration must enable components in `service.pipelines` [2][5].
- **Optional unless consequential:** replicas, protocols, queues, retry, retention, sampling, and redaction. Show transformations that change the evidence.
- **SLI/SLO:** measurement definition versus target over a window; an alert condition is neither. For good-event ratios, allowed bad-event fraction is `1 − SLO` [6][7].
- **Labels:** short functional names; signal/protocol on edges. Use distinct evidence tags so dashed lines do not mean both “asynchronous” and “unverified.”

Deployment-focused views are common, but logical telemetry pipelines and service-level response views are equally valid. This family has no universal version. OpenTelemetry's Profiles page states Alpha at the access date; baggage carries context rather than requiring another storage pipeline [1][3][4].

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
| Best practice | Anti-pattern |
| --- | --- |
| Start with user-visible behaviour and actionable detection [7][8]. | Host-health dashboards presented as complete service coverage. |
| Correlate evidence across services and message boundaries [1]. | Assuming an imported SDK proves a connected trace. |
| Expose sampling, processor order, and routing assumptions [5][9]. | Arbitrary load balancing before stateful tail sampling. |
| Show consequential telemetry loss and sensitive-data boundaries [10][11]. | A queue portrayed as lossless, or downstream redaction as preventing upstream exposure. |
| Verify routes and response ownership; monitor collection itself [8][10]. | Treating missing data as health or a notification as completed remediation. |

Black-box symptoms and white-box diagnostics complement each other. Golden signals—latency, traffic, errors, saturation—are monitoring concerns, not telemetry format categories [8]. Burn-rate alerts need appropriate traffic and evaluation windows; published thresholds are examples, not universal defaults [7].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [OpenTelemetry — Collector Architecture, pipeline diagram](https://opentelemetry.io/docs/collector/architecture/) — makes ordered processing and exporter fan-out explicit; documentation is CC BY 4.0, requiring attribution and modification notices for adaptations, subject to asset-specific exceptions.
- [OpenTelemetry — Gateway deployment pattern](https://opentelemetry.io/docs/collector/deploy/gateway/) — populated single/two-tier diagrams distinguish forwarding from stateful routing; CC BY 4.0 documentation, with the same attribution and asset checks.
- [OpenTelemetry — Agent-to-gateway deployment pattern](https://opentelemetry.io/docs/collector/deploy/other/agent-to-gateway/) — separates host-local collection from shared processing and explains tail-sampling constraints; CC BY 4.0 documentation, not a guarantee of every distribution's support.
- [Prometheus — Overview, architecture diagram](https://prometheus.io/docs/introduction/overview/) — distinguishes discovery, scraping, rule evaluation, alert handling, and visualization; documentation repository is Apache-2.0, with applicable notices and asset-specific terms to check before copying.

These are linked architecture examples, not copied graphics. SRE workbook figures have CC BY-NC-ND 4.0 terms; use original explanations and link the book rather than adapting its figures for unrestricted redistribution [6][7]. Documentation licenses are listed in [13][14].

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Choose the operational question, environment, and current/proposed state.
2. Trace each relevant signal from enabled instrumentation through actual configuration to its use.
3. Add correlation, processing, sampling, and consequential trust/failure boundaries.
4. For response scope, connect measurement → detection → notification → responder/runbook; distinguish SLO from alert policy.
5. Lay out sources left, processing center, destinations right; put response below. Group by host only for deployment questions.
6. Use short functional labels, labeled arrows, restrained colour, and an evidence legend; compare against configuration.

**Self-check**
- [ ] Scope and environment are explicit.
- [ ] Sources reach their stated use, or gaps are visible.
- [ ] Data, scrape requests, queries, context, and notifications differ.
- [ ] Enabled pipelines and processor order match evidence.
- [ ] Component/signal support is checked.
- [ ] Sampling, loss, and redaction assumptions are visible.
- [ ] Response claims have measurement, policy, owner, and action.
- [ ] Configured intent is not presented as observed runtime success.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- SDK initialization and exporter settings identify configured generation and destinations.
- Collector pipelines, deployment overlays, and scrape discovery identify enabled paths.
- Middleware and message handlers reveal context propagation and correlation gaps.
- Rules, notification routing, and runbooks support detection and response claims.
- Record path, revision, environment, and evidence status; runtime success needs runtime evidence. Never infer an SLO or staffed responder from naming alone.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Is the goal collection, diagnosis, readiness, or telemetry governance?
2. Which environment/state and configuration are authoritative?
3. Which user behaviour and available signals must be explained?
4. What targets, alert routes, response owners, and data constraints are agreed?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/H2.json` · Layout template: `layered` · layers (instrument, collect, analyse, respond) are `layer` groups holding `component`, `store` and `person` nodes, with `data` and `async` edges between layers and proposed policies in style `planned`.
Use `nested` with `boundary` groups for deployment boundaries instead.

## Sources {#sources}
<!-- skill: omit -->
1. OpenTelemetry — Signals — https://opentelemetry.io/docs/concepts/signals/ — accessed 2026-10-14.
2. OpenTelemetry — Collector Architecture — https://opentelemetry.io/docs/collector/architecture/ — accessed 2026-10-14.
3. OpenTelemetry — Profiles — https://opentelemetry.io/docs/concepts/signals/profiles/ — accessed 2026-10-14.
4. OpenTelemetry — Specification Status Summary — https://opentelemetry.io/docs/specs/status/ — accessed 2026-10-14.
5. OpenTelemetry — Collector Configuration — https://opentelemetry.io/docs/collector/configuration/ — accessed 2026-10-14.
6. Google, The Site Reliability Workbook — Implementing SLOs — https://sre.google/workbook/implementing-slos/ — accessed 2026-10-14.
7. Google, The Site Reliability Workbook — Alerting on SLOs — https://sre.google/workbook/alerting-on-slos/ — accessed 2026-10-14.
8. Google, Site Reliability Engineering — Monitoring Distributed Systems — https://sre.google/sre-book/monitoring-distributed-systems/ — accessed 2026-10-14.
9. OpenTelemetry — Agent-to-gateway deployment pattern — https://opentelemetry.io/docs/collector/deploy/other/agent-to-gateway/ — accessed 2026-10-14.
10. OpenTelemetry — Collector Resiliency — https://opentelemetry.io/docs/collector/resiliency/ — accessed 2026-10-14.
11. OpenTelemetry — Handling sensitive data — https://opentelemetry.io/docs/security/handling-sensitive-data/ — accessed 2026-10-14.
12. OpenTelemetry — Gateway deployment pattern — https://opentelemetry.io/docs/collector/deploy/gateway/ — accessed 2026-10-14.
13. OpenTelemetry documentation — LICENSE, CC BY 4.0 — https://github.com/open-telemetry/opentelemetry.io/blob/main/LICENSE — accessed 2026-10-14.
14. Prometheus documentation — LICENSE, Apache-2.0 — https://github.com/prometheus/docs/blob/main/LICENSE — accessed 2026-10-14.
15. Prometheus — Overview — https://prometheus.io/docs/introduction/overview/ — accessed 2026-10-14.

## Sample {#sample}
<!-- skill: path only -->
![H2 · Enterprise Service Assistant](/samples/ai-service-assistant/H2/en/diagram.svg)
*Redact before export. Illustrative SLO, cost targets, bounded delivery, sampling/retention and CloudWatch→SNS→operator response are specified in AS-observe; none are measured guarantees.*

[SVG](/samples/ai-service-assistant/H2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/H2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

[Historical shop regression sample](/samples/H2-observability-view.svg) · [All 29 views](/use/ai-service-assistant) · [Illustrative assumptions](/use/ai-service-assistant-assumptions).
