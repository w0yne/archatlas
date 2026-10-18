# Observability view (可观测性视图)
<!-- Generated from content/en/types/H2-observability-view.md by tools/build_skill_refs.py. Do not edit. -->
> How does evidence of service behavior reach analysis, detection, and someone who can act?
Scope: An environment's telemetry paths and relevant operational response. Neighbours: G1, G4, H1.

## Meaning
An observability view explains how evidence of service behaviour becomes useful for diagnosis, detection, or response. Its deeper concern is the credibility of that path: missing context, dropped data, or an unowned alert can break it.

**Definition used here:** an informal operational view, not a formal notation or fixed C4 model level. OpenTelemetry specifies telemetry behaviour, not drawing symbols. A Collector alone is not a storage, visualization, or paging backend.

Metrics, logs, and traces are common signals, not a closed set of three pillars. Profiles and context propagation also matter; check component-specific support and maturity. Omit unrelated business logic and exhaustive metric inventories.

## When to use and how to choose
- **Audience:** service owners, developers, operators, and responders.
- **Scenarios:** reviewing checkout readiness; diagnosing slow shop requests; designing collection topology; closing monitoring gaps after an incident.
- **Choose scope:** telemetry pipeline, collector deployment, or detection/response. Split views when one figure cannot explain all three.
- **When not:** use a trace/sequence for one request, a dashboard for current measurements, or a component diagram for static dependencies.
- **G1 deployment / G4 delivery pipeline:** those explain hosting or release machinery, not whether operational evidence reaches its use.
- **H1 RACI:** use it for responsibility assignments; link a runbook for response steps.
- SLO and paging details are required for a corresponding reliability/response claim, not for every profiling or collector-only view.

## Notation and elements
- **Required:** service/environment scope, signal sources, relevant acquisition/processing/destinations, labeled relations, boundaries, and a legend.
- **Conditional:** detection/response views need measurement definition, detection policy, notification route, responder, and action reference or explicit gaps.
- **Data arrows:** producer → receiver → destination. For pull collection, distinguish scrape-request direction from metric-response direction.
- **Other arrows:** label queries, context propagation, notifications, and remediation separately. Context travels with application calls/messages, not a backend export.
- **Collector pipeline:** receivers → optional ordered processors → exporters; connectors can join pipelines. Configuration must enable components in `service.pipelines`.
- **Optional unless consequential:** replicas, protocols, queues, retry, retention, sampling, and redaction. Show transformations that change the evidence.
- **SLI/SLO:** measurement definition versus target over a window; an alert condition is neither. For good-event ratios, allowed bad-event fraction is `1 − SLO`.
- **Labels:** short functional names; signal/protocol on edges. Use distinct evidence tags so dashed lines do not mean both “asynchronous” and “unverified.”

Deployment-focused views are common, but logical telemetry pipelines and service-level response views are equally valid. This family has no universal version. OpenTelemetry's Profiles page states Alpha at the access date; baggage carries context rather than requiring another storage pipeline.

## Best practices and anti-patterns
| Best practice | Anti-pattern |
| --- | --- |
| Start with user-visible behaviour and actionable detection. | Host-health dashboards presented as complete service coverage. |
| Correlate evidence across services and message boundaries. | Assuming an imported SDK proves a connected trace. |
| Expose sampling, processor order, and routing assumptions. | Arbitrary load balancing before stateful tail sampling. |
| Show consequential telemetry loss and sensitive-data boundaries. | A queue portrayed as lossless, or downstream redaction as preventing upstream exposure. |
| Verify routes and response ownership; monitor collection itself. | Treating missing data as health or a notification as completed remediation. |

Black-box symptoms and white-box diagnostics complement each other. Golden signals—latency, traffic, errors, saturation—are monitoring concerns, not telemetry format categories. Burn-rate alerts need appropriate traffic and evaluation windows; published thresholds are examples, not universal defaults.

## Drawing recipe
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

## Evidence in a code repository
- SDK initialization and exporter settings identify configured generation and destinations.
- Collector pipelines, deployment overlays, and scrape discovery identify enabled paths.
- Middleware and message handlers reveal context propagation and correlation gaps.
- Rules, notification routing, and runbooks support detection and response claims.
- Record path, revision, environment, and evidence status; runtime success needs runtime evidence. Never infer an SLO or staffed responder from naming alone.

## Guided-mode questions
1. Is the goal collection, diagnosis, readiness, or telemetry governance?
2. Which environment/state and configuration are authoritative?
3. Which user behaviour and available signals must be explained?
4. What targets, alert routes, response owners, and data constraints are agreed?

## Template
Model template: `assets/templates/H2.json` · Layout template: `layered` · layers (instrument, collect, analyse, respond) are `layer` groups holding `component`, `store` and `person` nodes, with `data` and `async` edges between layers and proposed policies in style `planned`.
Use `nested` with `boundary` groups for deployment boundaries instead.

## Sample
Figure: `samples/ai-service-assistant/H2/en/diagram.svg` (published with the site)
