---
code: G2
slug: cloud-infrastructure-architecture
family: G
names:
  en: Cloud Infrastructure Architecture
  zh: 云基础设施架构图
  aliases:
    en: [cloud solution architecture, cloud architecture diagram, provider-specific infrastructure view, cloud reference architecture]
    zh: [云解决方案架构图, 云服务架构图, 云架构图, 云参考架构]
question: "Which cloud capabilities realise the workload, and which trade-offs make that arrangement fit its requirements?"
audiences: [cloud and platform architects, operators, security reviewers, implementation partners, technical decision-makers]
level: logical
phases: [planning, design, review]
scope: "One workload on one provider (or a stated multi-provider split), showing selected services, responsibilities, the main request and data path, and real location or failure boundaries"
formal:
  kind: convention
  ref: "No single standard. Provider icon sets and provider architecture-centre guidance are conventions; Well-Architected frameworks are design-review guidance, not drawing notations"
neighbours: [G1, G3, C3, C5, G4]
status: draft
---

# Cloud Infrastructure Architecture (云基础设施架构图)

> A one-workload picture of the cloud services that realise it, why they are arranged this way, and where the real ownership and failure boundaries lie.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** which cloud capabilities realise this workload, and what trade-offs make the arrangement fit its reliability, security, operations, performance and cost goals?
- **Viewpoint:** a technology or infrastructure concern in an architecture description. This is an informal, concern-based family: provider icon libraries identify services, and Well-Architected frameworks guide review rather than drawing [1][2][3][4]. Not every cloud diagram is "physical": a managed-service design may deliberately hide machines.
- **Deeper meaning:** the valuable content is why services and boundaries are arranged as they are, not how many familiar icons appear. Service selection should follow requirements and failure or cost assumptions.
- **Leaves out:** source modules, every API endpoint, detailed route and firewall tables (G3), and software-instance placement (G1) unless they decide the arrangement.
- **Definition used here:** this page covers *the cloud architecture of one workload*. *Reference architecture* is a separate status: a reusable, recommended arrangement with stated assumptions. Record status as `reference | proposed solution | declared implementation | observed deployment` rather than merging these names. As checked on 2026-10-14, AWS describes six pillars, Azure five and Google Cloud six [1][2][3]; counts change and are not a diagram recipe.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** cloud and platform architects, operators, security reviewers, partners, decision-makers who need the main trade-offs.
- **Scenarios:** evaluating a landing pattern for the storefront and API; moving order processing and background jobs to managed services; choosing a production baseline for an availability target; how a chatbot, a vector store and a model endpoint compose; comparing cost and resilience options.
- **When not to use:** as a business overview, or as proof of deployment, compliance, availability or a quantified SLA.
- **vs neighbours:**
  - **G1** for which software instances run on which hosts.
  - **G3** for routing, segmentation, reachability.
  - **C3** or **C5** for provider-neutral structure.
  - **G4** for the delivery machinery.
-->
- **Audience:** cloud and platform architects, operators, security reviewers, partners, and decision-makers who need the main trade-offs.
- **Classic scenarios:**
  1. Evaluating a landing pattern for the online shop's storefront and API.
  2. Moving order processing and background jobs to managed services.
  3. Choosing a production baseline for an availability target.
  4. Explaining how a support chatbot, a vector store and a model endpoint compose.
  5. Comparing cost and resilience options side by side.
- **When not to use:** as a business overview, or as proof of deployment, compliance, service availability or a quantified SLA.
- **vs neighbours:**
  - Choose **G1** for which software instances run on which hosts.
  - Choose **G3** for routing, segmentation and reachability.
  - Choose **C3** or **C5** for provider-neutral software structure.
  - Choose **G4** for the delivery machinery.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** informal. Icons are conventions, and a vendor logo does not certify suitability.
- **Required:**
  - Workload, scope, provider and design status (reference, proposed, declared, observed).
  - Selected services, each with a workload role ("Managed queue: background jobs").
  - The principal request and data path.
  - Material ownership, location and failure boundaries; assumptions; a key.
- **Arrows:** state whether they mean requests, events, replication, configuration or dependency. Separate runtime paths from administration and delivery paths.
- **Grouping:** use real provider semantics. Account, project or subscription, region, zone, VPC or VNet and service boundary are not interchangeable. Some managed or global services sit outside a customer network; show private endpoints and the service itself correctly instead of wrapping everything in a network box.
- **Optional:** service tiers, scaling boundaries, redundancy, backup and recovery, identity and secrets, telemetry, data lifecycle, cost-sensitive dependencies. Include them when they answer the chosen concern.
- **Text budget:** about 3–6 words per service (name plus role); trade-offs and assumptions go beside the figure.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Start from requirements and failure or cost assumptions,** then choose services [1][2][3].
2. **Respect an example's scope.** Azure's basic web app page says it is for learning and proof of concept, not production, so copying the picture does not give a production baseline [5].
3. **Show zone or region separation only when it exists and matters;** repeated icons do not prove replication, backup or recovery.
4. **Keep alternatives apart.** Do not draw an as-built path and a proposed service in the same style.
5. **Link, do not absorb,** detailed security and network views; state the shared-responsibility split in text.

### Anti-patterns
1. **Icon soup:** products with no workload role.
2. **Everything inside one VPC box,** including global or provider-managed services.
3. **Unlabelled arrows** that mix runtime, administration and delivery paths.
4. **Availability claims without mechanism:** two icons, no replication.
5. **A firewall-rule dump** instead of a service arrangement.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [AWS: Web Application Architecture](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/web-application-architecture/web-application-architecture.html) — multi-zone web and application tiers with managed data services, plus explanation. AWS documentation; AWS permits its icons under its toolkit terms [4].
- [Azure: Basic web application](https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/basic-web-app) — concise runtime, identity and monitoring roles with unusually clear limits on production use.
- [Google Cloud: Three-tier web app template](https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app) — frontend, API, cache and data path as a service composition tied to a configurable deployment.
- Vendor pages remain vendor material: check the specific page or icon package before reproducing artwork.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. State workload, constraints, audience, provider and status in the title, for example "Online shop storefront on a managed platform: proposed".
2. List responsibilities first (serve pages, take orders, run jobs, store data, authenticate); then choose services, one per role.
3. Layout: left to right along the main request path (clients, edge, compute, data). Put supporting services (identity, secrets, monitoring) on a band below or above, not in the main row.
4. Group only real boundaries: provider account or project, region, zone, and the network where a service is truly attached. Place managed or global services outside the network box.
5. Edges: label every arrow with its meaning; use one line style for runtime, another for async events or replication, a third for administration.
6. Text: service name plus role, about 3–6 words; two or three consequential trade-offs as a short note beside the figure.
7. Colour: neutral fills with a distinct tint for the data tier and for external or managed services; use provider icons only if they help recognition and reuse terms allow, otherwise plain labelled shapes.

**Self-check**
- [ ] Status (reference, proposed, declared or observed) is stated near the title.
- [ ] Every service has a workload role, not just a product name.
- [ ] Each arrow type is explained in the key.
- [ ] Region, zone and network boundaries match the provider's semantics.
- [ ] Managed or global services are not placed inside a subnet they do not belong to.
- [ ] Availability or resilience claims name a mechanism, or are left out.
- [ ] Assumptions and two or three trade-offs accompany the image.
- [ ] Icons or artwork have a stated reuse basis.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Services:** infrastructure-as-code modules and resource types, provider versions, configured service tiers and sizes, resource references.
- **Wiring:** event subscriptions, endpoints, queue and topic names, scaling and backup declarations, per-environment variants.
- **Workload roles:** application code explains roles but does not prove a managed service is provisioned.
- **Must come from people:** foundations managed outside the repository (accounts, landing zones, shared networks), actual sizes and costs, requirements and trade-offs.
- A dependency graph from the IaC tool is not a finished architecture. Label results "declared"; never run deployment operations for discovery.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Is this a reusable reference pattern or the architecture of one actual workload? (one workload)
2. Which provider, region and data-residency constraints apply? (one provider, one region, stated)
3. Which quality goals drive the design and what compromises are acceptable? (availability and cost; accept single-region)
4. Which infrastructure is already managed elsewhere? (shown as external)
5. Should routing, deployment and recovery be separate views? (yes, linked)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/G2.json` · Layout template: `layered` · tiers (edge, compute, data, supporting) become `layer` groups, provider boundaries (account, region, zone) become `boundary` groups, services are nodes with a role in `sub`, and arrows use `call`, `data` or `async` edge kinds with explicit labels; design status is carried in node `style` and `evidence`.

## Sources {#sources}
<!-- skill: omit -->
1. AWS, Architecture Center (Well-Architected, six pillars) — https://aws.amazon.com/architecture/ — accessed 2026-10-14
2. Microsoft, "Azure Well-Architected Framework pillars" (five pillars) — https://learn.microsoft.com/en-us/azure/well-architected/pillars — accessed 2026-10-14
3. Google Cloud, "Well-Architected Framework" (six pillars) — https://docs.cloud.google.com/architecture/framework — accessed 2026-10-14
4. AWS, "Architecture Icons" — https://aws.amazon.com/architecture/icons/ — accessed 2026-10-14
5. Microsoft, "Basic web application" (Azure Architecture Center) — https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/basic-web-app — accessed 2026-10-14
6. AWS, "Web Application Architecture" (first published 19 November 2021) — https://docs.aws.amazon.com/reference-architecture-diagrams/latest/web-application-architecture/web-application-architecture.html — accessed 2026-10-14
7. Google Cloud, "Three-tier web app template" — https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app — accessed 2026-10-14
8. ISO/IEC/IEEE 42010:2022, public scope only; the page returned HTTP 403 and the full text was not reviewed — https://www.iso.org/standard/74393.html — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![G2 sample: online shop storefront on a managed cloud platform with CDN, container service, managed database, queue and a support chatbot using a model endpoint](/samples/G2-cloud-infrastructure-architecture.svg)
*Sample pending (generated by the renderer from `examples/`).*
