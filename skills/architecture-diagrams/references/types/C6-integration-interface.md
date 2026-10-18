# Integration / Interface Diagram (集成 / 接口图)
<!-- Generated from content/en/types/C6-integration-interface.md by tools/build_skill_refs.py. Do not edit. -->
> Which interfaces exist between systems, who initiates each, what is exchanged in which integration style, and under which contract, security, service level and ownership?
Scope: The interfaces between a set of systems (or one hub or partner in close-up), drawn as a map plus a mandatory interface table. Neighbours: C1, C2, C3, C5, C7, E1, F2.

## Meaning
- **Question:** which interfaces connect these systems, who calls or publishes, what is exchanged, in which style, and who owns each side? Purpose: make coupling visible and negotiable; the table is the skeleton of the contract.
- **Sources:** no single standard. Enterprise Integration Patterns (four styles: file transfer, shared database, remote call, messaging), TOGAF Interface Catalog and Application Communication diagram, the Interface Control Document, OpenAPI and AsyncAPI contracts.
- **Definition used here:** C6 is *between* systems, partners included; C3 is *inside* one system. Offer a logical variant (no protocol column) and a technical one (with protocol).
- **Variants:** (a) interface map + table (default); (b) event topology with channels as nodes; (c) API landscape table by owner, lifecycle, consumers.
- **Leaves out:** field-level payloads (link the spec), system internals (C3–C5), call order (E1), hosts (G1), lineage (D3).

## When to use and how to choose
- **Audience:** integration and solution architects, developers on both sides, counterpart owners, operations, security reviewers, and project managers scheduling dependencies.
- **Classic scenarios:** (1) connect several systems for a new flow, such as checkout to payment to warehouse; (2) prepare an interface agreement with an external partner, using the table as the agenda; (3) inventory interfaces for migration or consolidation, scoped "as early as possible"; (4) security and resilience review: unauthenticated, unthrottled or synchronous-on-critical-path interfaces; (5) find who produces and consumes which event in an event-driven estate.
- **When not to use:** one system with no external dependencies (C2/C5); the internals of one service (C4); call order or error paths (E1); field-level payload documentation (link the spec); every internal function call (that is a dependency graph).
- **vs neighbours:**
  - Choose **C1 Application landscape** when you need which applications exist, not the contract on each link.
  - Choose **C2 System context** when one line of purpose per neighbour is enough.
  - Choose **C3 Container diagram** for communication between runnable units *inside* one system.
  - Choose **C7 Bounded context map** to explain *why* a contract looks the way it does (ACL, open host service). Its pattern can be a column here.
  - Choose **E1 Sequence** for the time order of one call chain. Choose **D2/D3** when the subject is the data and its stores. Choose **F2 Threat model** for trust-boundary analysis, which takes this table's authentication column as input.

## Notation and elements
- **Nodes:** systems; external parties in a distinct style with the owning organisation named; mediating infrastructure that carries meaning (broker, API gateway, integration platform, file share) as nodes, not hidden in lines.
- **Edges:** one per interface or interface group with a stable ID (I-01…) and a verb-phrase label; unidirectional, label agrees with the arrow, no bare "uses", legend explains every line style.
- **Arrows:** one meaning, either *initiator → provider* or *data flow*; asynchronous paths run producer → channel → consumer. Convention: solid = synchronous, dashed = asynchronous message or event, dotted with a file mark = batch/file transfer.
- **Interface table (mandatory), integration style first:** Integration style (file transfer / shared database / RPC-API / messaging; a shared database is hidden coupling) · ID and initiator → provider (matches the line) · Purpose · Interaction pattern (request-reply, command, event notification, event-carried state, publish-subscribe, batch).
- **Table, continued (required):** Protocol/transport (omit in the logical variant) · Format and contract link (OpenAPI/AsyncAPI/schema; do not inline fields) · Authentication/authorisation · Volume and SLA (mark example numbers "illustrative") · Owner on both sides (a named team or role).
- **Table, conditional/optional:** Failure semantics (retry, idempotency, ordering, dead-letter, de-duplication) required if critical · Lifecycle/version · Data classification.
- **Source of truth:** machine-readable contracts in the repository; generate or cross-check the table from them.
- **Size:** about 8–15 nodes at level 1 (heuristic); level 2 shows one hub or partner in full.

## Best practices and anti-patterns
### Best practices

1. Name the integration style first (file, shared database, RPC, messaging), before debating products.
2. Show asynchronous channels as nodes and state the delivery semantics (point-to-point or publish-subscribe), ordering and duplicate handling.
3. Distinguish command from event, and for events say which kind: notification, event-carried state transfer or event sourcing. "Event" alone hides very different coupling.
4. Keep contracts machine-readable and contract-first, and derive the table from them. Give every interface an owner on both sides and a lifecycle state.
5. Say where logic lives: smart endpoints and dumb pipes, or a central hub that routes and transforms. Mark the middleware node accordingly.

### Anti-patterns

1. **Lines without a table:** the topology is then silent on everything that matters.
2. **Sync and async not distinguished:** latent coupling and cascading failure surface late.
3. **Hidden integration** through a shared database or file drop with no owner. File transfer needs agreed name, location, format, timing and clean-up.
4. **Mixed arrow meanings** (sometimes "calls", sometimes "sends data") and "event" used for commands and notifications alike.
5. **Forgotten authentication and rate limits, or SLA numbers without a source**; field lists drawn on the figure instead of linked.

## Drawing recipe
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

## Evidence in a code repository
- Strong: OpenAPI files (paths, servers, securitySchemes), AsyncAPI files (channels, operations, bindings), `.proto` and GraphQL schemas, API gateway/ingress routes with auth and rate-limit plugins, broker topic/queue definitions in IaC, Kubernetes `Service`/`Ingress`/`NetworkPolicy`, endpoint URLs in environment variables (`*_URL`, `*_HOST`), HTTP/gRPC clients and generated SDKs, contract tests, `catalog-info.yaml` `providesApis`/`consumesApis`, CODEOWNERS.
- Cross-check the as-is picture with runtime traces (an OpenTelemetry service graph) where available.
- Not in code (ask people): SLAs and volumes, ownership on the other side, contractual authentication arrangements, data classification, planned interfaces. Shared-database and file-drop interfaces often appear only in scripts or cron jobs; mark inferred rows "to confirm".

## Guided-mode questions
1. Which systems and external parties are in scope, and who reads this? (Default: internal architects and developers; externals as named boxes.)
2. As-is or planned, and do interface sources exist (OpenAPI/AsyncAPI, gateway export, spreadsheet)? (Default: as-is, inferred from the repo and confirmed by you.)
3. Which integration styles dominate, and is there a broker, gateway or integration platform in the middle? (Default: APIs plus one broker.)
4. Which variant: interface map, event topology or API landscape; logical or technical? (Default: interface map, technical, with the full table.)
5. Which table columns matter most beyond the required ones, and what ID scheme? (Default: required columns, IDs I-01…)

## Template
Model template: `assets/templates/C6.json` · Layout template: `grid_table` · the `tables[]` interface table (style-first columns) is the primary output; `grid_table` takes tables only, so the companion map is a second model whose edge `step` or `label` carries the interface ID of the matching table row.

## Sample
Figure: `samples/ai-service-assistant/C6/en/diagram.svg` (published with the site)
