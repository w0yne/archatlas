---
code: C6
slug: integration-interface
family: C
names:
  en: Integration and interface diagram
  zh: 集成与接口图
  aliases:
    en: [integration diagram, interface map, integration architecture, interface catalog, API landscape, integration landscape, application interaction matrix, event topology]
    zh: [集成架构图, 接口关系图, 系统集成图, 接口清单, 应用通信图, 应用交互矩阵, 事件拓扑图, API 全景图]
question: Which interfaces exist between systems, who initiates each, what is exchanged in which integration style, and under which contract, security, service level and ownership?
audiences: [architects, developers, operations]
levels: [logical, physical]
phases: [design, build]
scope: The interfaces between a set of systems (or one hub or partner in close-up), drawn as a map plus a mandatory interface table.
formal: {kind: convention, ref: none for the diagram; vocabulary from Enterprise Integration Patterns (2003) and TOGAF 9.x Phase C artefacts; contracts in OpenAPI 3.2.x / AsyncAPI 3.1.0}
neighbours: [C1, C2, C3, C5, C7, E1, F2]
status: draft
---

# Integration / Interface Diagram (集成 / 接口图)

> A map of the interfaces between systems, paired with a table that records each interface's style, contract, security, service level and owners.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
<!-- skill-text
- **Question:** which interfaces connect these systems, who calls or publishes, what is exchanged, in which style, and who owns each side? Purpose: make coupling visible and negotiable; the table is the skeleton of the contract.
- **Sources:** no single standard. Enterprise Integration Patterns (four styles: file transfer, shared database, remote call, messaging), TOGAF Interface Catalog and Application Communication diagram, the Interface Control Document, OpenAPI and AsyncAPI contracts.
- **Definition used here:** C6 is *between* systems, partners included; C3 is *inside* one system. Offer a logical variant (no protocol column) and a technical one (with protocol).
- **Variants:** (a) interface map + table (default); (b) event topology with channels as nodes; (c) API landscape table by owner, lifecycle, consumers.
- **Leaves out:** field-level payloads (link the spec), system internals (C3–C5), call order (E1), hosts (G1), lineage (D3).
-->

An integration diagram answers: *which interfaces connect these systems, who calls or publishes, what is exchanged, in which style, and who owns each side?* Its real purpose is to make **coupling visible and negotiable**: it is the artefact two teams, or a company and a partner, agree on before writing code, and its table is the skeleton of the contract. In ISO/IEC/IEEE 42010 terms its concerns are interoperability, coupling, security of exchanges, ownership and change impact [10]. In SEI Views and Beyond it is a component-and-connector view with connectors as first-class elements [11].

No single standard defines the diagram. It draws on four traditions:
- **Enterprise Integration Patterns** (Hohpe & Woolf, 2003): 65 patterns and four **integration styles** — File Transfer, Shared Database, Remote Procedure Invocation, Messaging [1][2]. The book defines pattern icons but states that no widely used, comprehensive notation exists [3].
- **TOGAF 9.x Phase C** artefacts: Interface Catalog, Application Communication diagram and Application Interaction matrix [4]. The 10th Edition text was not verified.
- **Systems engineering:** the Interface Control Document (ICD) records format, frequency and timing for every interface [5].
- **Machine-readable contracts:** OpenAPI (current: 3.2.1) for HTTP APIs [6] and AsyncAPI (current: 3.1.0) for event-driven APIs [7], both checked on 2026-10-14.

**Definition used here:** C6 is *between* systems, including partners. C3 is *inside* one system. TOGAF keeps the Application Communication diagram logical and moves protocol to the technology view [4]. This page therefore offers a **logical variant** (no protocol column) and a **technical variant** (with protocol).

**Three variants under one type:** (a) **interface map + table** (default): systems as nodes, numbered interface lines and a table; (b) **event / asynchronous topology**: channels and topics as first-class nodes between producers and consumers [8]; (c) **API landscape / catalogue**: a portfolio table of many APIs by owner, lifecycle and consumers.

**Deliberately left out:** field-level payloads (link the OpenAPI/AsyncAPI/schema file instead), system internals (C3–C5), call order in one scenario (E1), hosts and networks (G1), data lineage (D3).

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->

- **Audience:** integration and solution architects, developers on both sides, counterpart owners, operations, security reviewers, and project managers scheduling dependencies.
- **Classic scenarios:** (1) connect several systems for a new flow, such as checkout to payment to warehouse; (2) prepare an interface agreement with an external partner, using the table as the agenda; (3) inventory interfaces for migration or consolidation, scoped "as early as possible" [4]; (4) security and resilience review: unauthenticated, unthrottled or synchronous-on-critical-path interfaces; (5) find who produces and consumes which event in an event-driven estate.
- **When not to use:** one system with no external dependencies (C2/C5); the internals of one service (C4); call order or error paths (E1); field-level payload documentation (link the spec); every internal function call (that is a dependency graph).
- **vs neighbours:**
  - Choose **C1 Application landscape** when you need which applications exist, not the contract on each link.
  - Choose **C2 System context** when one line of purpose per neighbour is enough.
  - Choose **C3 Container diagram** for communication between runnable units *inside* one system.
  - Choose **C7 Bounded context map** to explain *why* a contract looks the way it does (ACL, open host service). Its pattern can be a column here.
  - Choose **E1 Sequence** for the time order of one call chain. Choose **D2/D3** when the subject is the data and its stores. Choose **F2 Threat model** for trust-boundary analysis, which takes this table's authentication column as input.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
<!-- skill-text
- **Nodes:** systems; external parties in a distinct style with the owning organisation named; mediating infrastructure that carries meaning (broker, API gateway, integration platform, file share) as nodes, not hidden in lines.
- **Edges:** one per interface or interface group with a stable ID (I-01…) and a verb-phrase label; unidirectional, label agrees with the arrow, no bare "uses", legend explains every line style.
- **Arrows:** one meaning, either *initiator → provider* or *data flow*; asynchronous paths run producer → channel → consumer. Convention: solid = synchronous, dashed = asynchronous message or event, dotted with a file mark = batch/file transfer.
- **Interface table (mandatory), integration style first:** Integration style (file transfer / shared database / RPC-API / messaging; a shared database is hidden coupling) · ID and initiator → provider (matches the line) · Purpose · Interaction pattern (request-reply, command, event notification, event-carried state, publish-subscribe, batch).
- **Table, continued (required):** Protocol/transport (omit in the logical variant) · Format and contract link (OpenAPI/AsyncAPI/schema; do not inline fields) · Authentication/authorisation · Volume and SLA (mark example numbers "illustrative") · Owner on both sides (a named team or role).
- **Table, conditional/optional:** Failure semantics (retry, idempotency, ordering, dead-letter, de-duplication) required if critical · Lifecycle/version · Data classification.
- **Source of truth:** machine-readable contracts in the repository; generate or cross-check the table from them.
- **Size:** about 8–15 nodes at level 1 (heuristic); level 2 shows one hub or partner in full.
-->

- **Nodes:** systems; external parties in a distinct style with the owning organisation named; **mediating infrastructure that carries meaning** (broker, API gateway, integration platform, file share) as nodes, not hidden inside lines [12].
- **Edges:** one per interface or interface group, with a stable **ID** (I-01…) and a verb-phrase label ("authorises payment"). Lines are unidirectional, the label agrees with the arrow, there are no bare "uses" labels, and the legend explains every line style [13][14].
- **Arrows and line style:** one arrow meaning, either *initiator → provider* or *data flow*; asynchronous paths run **producer → channel → consumer** [8]. Line styles are a convention, so put them in the legend: solid = synchronous, dashed = asynchronous message or event, dotted with a file mark = batch/file transfer.
- **Interface table (mandatory).** Integration style is the **first column**; the others follow:

| Column | Req. | Notes |
|---|---|---|
| Integration style | R | File transfer / shared database / RPC-API / messaging [2]. A shared database is an interface with hidden coupling. |
| ID · initiator → provider | R | Matches the line; for events, producer and each consumer. |
| Purpose | R | One line: why the interface exists. |
| Interaction pattern | R | Request-reply, command, event notification, event-carried state transfer, publish-subscribe, batch [15]. |
| Protocol / transport | R* | *Omit in the logical variant [4]. |
| Format + contract link | R | Link to OpenAPI / AsyncAPI / schema file [6][7]; do not inline fields. |
| Authentication / authorisation | R | Mechanism and identity. |
| Volume · SLA / limits | R | Mark example numbers "illustrative". |
| Failure semantics | R if critical | Retry, idempotency, ordering, dead-letter, de-duplication [16]. |
| Owner (provider) · owner (consumer) | R | A named team or role on **both** sides [9]. |
| Lifecycle / version | O | Planned / live / deprecated; contract version [9]. |
| Data classification | O | Feeds the F-family security views. |

- **Source of truth:** machine-readable contracts in the repository (OpenAPI 3.2.x, AsyncAPI 3.1.0); generate or cross-check the table from them [6][7][14]. Level 1 shows all systems at about 8–15 nodes (heuristic); level 2 shows one hub or partner in full.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### Best practices

1. Name the integration style first (file, shared database, RPC, messaging), before debating products [1][2].
2. Show asynchronous channels as nodes and state the delivery semantics (point-to-point or publish-subscribe), ordering and duplicate handling [8][16].
3. Distinguish command from event, and for events say which kind: notification, event-carried state transfer or event sourcing. "Event" alone hides very different coupling [15].
4. Keep contracts machine-readable and contract-first, and derive the table from them. Give every interface an owner on both sides and a lifecycle state [6][9][14].
5. Say where logic lives: smart endpoints and dumb pipes, or a central hub that routes and transforms. Mark the middleware node accordingly [12].

### Anti-patterns

1. **Lines without a table:** the topology is then silent on everything that matters.
2. **Sync and async not distinguished:** latent coupling and cascading failure surface late [16].
3. **Hidden integration** through a shared database or file drop with no owner. File transfer needs agreed name, location, format, timing and clean-up [2].
4. **Mixed arrow meanings** (sometimes "calls", sometimes "sends data") and "event" used for commands and notifications alike [15].
5. **Forgotten authentication and rate limits, or SLA numbers without a source**; field lists drawn on the figure instead of linked.

## Exemplars {#exemplars}
<!-- skill: omit -->

- [Enterprise Integration Patterns, integration styles](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html) — the vocabulary behind the first table column and an honest statement about missing notation (licence not checked).
- [Azure Architecture Center, message broker and events for enterprise integration](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/integration/queues-events) — reference architecture with a sync/async split and broker and event-routing nodes (Microsoft Learn terms).
- [Azure Architecture Center, interservice communication](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication) — a clear trade-off discussion of synchronous APIs versus messaging (Microsoft Learn terms).
- [AsyncAPI document concepts](https://www.asyncapi.com/docs/concepts/asyncapi-document) and [spec examples](https://github.com/asyncapi/spec) — channels, operations, messages and bindings as a contract (repository Apache-2.0).
- [EventCatalog](https://www.eventcatalog.dev) — an open-source producer/consumer visualiser with owners; a model for the event-topology variant (licence not checked).
- [Backstage descriptor format](https://backstage.io/docs/features/software-catalog/descriptor-format/) — API entities with owner, lifecycle and provides/consumes relations; a data model for the API-landscape variant (Apache-2.0 project).

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->

1. Fix scope, audience, variant (map, event topology, API landscape), logical or technical, as-is or planned.
2. Build the **interface inventory before drawing**: IDs, integration style, then the other columns. Leave unknowns as "?" for the user; never invent protocols, SLAs or owners.
3. Cluster systems by domain or trust zone; split the figure if it exceeds about 15 nodes.
4. Layout left-to-right by initiation (shop front-ends left, core systems middle, partners right), or as vertical zone bands (internal | middleware | external). Brokers and gateways sit between the parties they mediate.
5. Nodes: name plus an optional owner tag. Externals get a dashed border with the owning organisation named.
6. Edges: ID badge plus a label of 2–4 words; line style by sync/async/batch; arrows initiator → provider or producer → channel → consumer.
7. Colour encodes ownership domain or trust zone (3–4 muted hues) plus one warning colour for flagged risks; never technology.
8. Add title (type + scope), legend, and the table beside or below with the same IDs.

**Self-check**
- [ ] Every line has an ID and label; every ID has exactly one table row and vice versa.
- [ ] Integration style filled for every row; shared databases and file drops are not hidden.
- [ ] One arrow semantics; each label matches its arrow direction.
- [ ] Sync and async visibly differ; asynchronous paths show the channel.
- [ ] Authentication, SLA/limits and both owners filled or marked unknown.
- [ ] Contract column links to OpenAPI/AsyncAPI/schema files; no field lists on the figure.
- [ ] Externals visibly distinct; no working notes or "TBD" on the figure.
- [ ] Illustrative numbers are labelled as such.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->

- Strong: OpenAPI files (paths, servers, securitySchemes), AsyncAPI files (channels, operations, bindings), `.proto` and GraphQL schemas, API gateway/ingress routes with auth and rate-limit plugins, broker topic/queue definitions in IaC, Kubernetes `Service`/`Ingress`/`NetworkPolicy`, endpoint URLs in environment variables (`*_URL`, `*_HOST`), HTTP/gRPC clients and generated SDKs, contract tests, `catalog-info.yaml` `providesApis`/`consumesApis`, CODEOWNERS.
- Cross-check the as-is picture with runtime traces (an OpenTelemetry service graph) where available [14].
- Not in code (ask people): SLAs and volumes, ownership on the other side, contractual authentication arrangements, data classification, planned interfaces. Shared-database and file-drop interfaces often appear only in scripts or cron jobs; mark inferred rows "to confirm".

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->

1. Which systems and external parties are in scope, and who reads this? (Default: internal architects and developers; externals as named boxes.)
2. As-is or planned, and do interface sources exist (OpenAPI/AsyncAPI, gateway export, spreadsheet)? (Default: as-is, inferred from the repo and confirmed by you.)
3. Which integration styles dominate, and is there a broker, gateway or integration platform in the middle? (Default: APIs plus one broker.)
4. Which variant: interface map, event topology or API landscape; logical or technical? (Default: interface map, technical, with the full table.)
5. Which table columns matter most beyond the required ones, and what ID scheme? (Default: required columns, IDs I-01…)

## Template {#template}
<!-- skill: keep (≤3 lines) -->

Model template: `assets/templates/C6.json` · Layout template: `grid_table` · the `tables[]` interface table (style-first columns) is the primary output; `grid_table` takes tables only, so the companion map is a second model whose edge `step` or `label` carries the interface ID of the matching table row.

## Sources {#sources}
<!-- skill: omit -->

1. Enterprise Integration Patterns, Messaging Patterns index — https://www.enterpriseintegrationpatterns.com/patterns/messaging/ — accessed 2026-10-14
2. Enterprise Integration Patterns, Integration Styles — https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html — accessed 2026-10-14
3. Hohpe & Woolf, Enterprise Integration Patterns, sample pages (diagram notation) — https://ptgmedia.pearsoncmg.com/images/9780321200686/samplepages/0321200683.pdf — accessed 2026-10-14
4. The TOGAF Standard 9.2, Architectural Artifacts (Interface Catalog, Application Communication diagram, Application Interaction matrix) — https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap31.html — accessed 2026-10-14 (search excerpts only; TOGAF 10 text not verified)
5. Wikipedia, "Interface control document" (cites NASA Systems Engineering Handbook) — https://en.wikipedia.org/wiki/Interface_control_document — accessed 2026-10-14 (secondary)
6. OpenAPI Initiative, OpenAPI Specification versions (3.2.1 current) — https://spec.openapis.org/oas/ — accessed 2026-10-14
7. AsyncAPI, Specification reference (3.1.0 current) — https://www.asyncapi.com/docs/reference/specification/latest — accessed 2026-10-14
8. Enterprise Integration Patterns, Message Channel / Publish-Subscribe Channel — https://www.enterpriseintegrationpatterns.com/patterns/messaging/ — accessed 2026-10-14
9. Backstage, Descriptor format of catalog entities — https://backstage.io/docs/features/software-catalog/descriptor-format/ — accessed 2026-10-14
10. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/42010/cm/ — accessed 2026-10-14
11. SEI, Views and Beyond Collection — https://www.sei.cmu.edu/library/views-and-beyond-collection — accessed 2026-10-14
12. Lewis & Fowler, "Microservices" (smart endpoints and dumb pipes) — https://martinfowler.com/articles/microservices.html — accessed 2026-10-14
13. C4 model, Review checklist — https://c4model.com/diagrams/checklist — accessed 2026-10-14
14. C4 model, FAQ — https://c4model.com/diagrams/faq — accessed 2026-10-14
15. Fowler, "What do you mean by 'Event-Driven'?" — https://martinfowler.com/articles/201701-event-driven.html — accessed 2026-10-14
16. Azure Architecture Center, "Interservice communication in microservices" — https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![C6 sample: interface table with three interfaces of an online shop](/samples/C6-integration-interface.svg)
*Interface table of the online shop with three interfaces: I1 order API to payment provider (synchronous REST, charge request, at checkout), I2 order API to email service (asynchronous message, receipt, when an order is paid) and I3 order API to carrier (nightly file, shipment list). The table alone; the companion interface map is a separate figure.*
