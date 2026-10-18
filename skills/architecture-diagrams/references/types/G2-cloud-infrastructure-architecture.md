# Cloud Infrastructure Architecture (云基础设施架构图)
<!-- Generated from content/en/types/G2-cloud-infrastructure-architecture.md by tools/build_skill_refs.py. Do not edit. -->
> Which cloud capabilities realise the workload, and which trade-offs make that arrangement fit its requirements?
Scope: One workload on one provider (or a stated multi-provider split), showing selected services, responsibilities, the main request and data path, and real location or failure boundaries Neighbours: C3, C5, G1, G3, G4.
Named variant of G1; apply this reference's own recipe and checks.

## Meaning
- **Question:** which cloud capabilities realise this workload, and what trade-offs make the arrangement fit its reliability, security, operations, performance and cost goals?
- **Viewpoint:** a technology or infrastructure concern in an architecture description. This is an informal, concern-based family: provider icon libraries identify services, and Well-Architected frameworks guide review rather than drawing. Not every cloud diagram is "physical": a managed-service design may deliberately hide machines.
- **Deeper meaning:** the valuable content is why services and boundaries are arranged as they are, not how many familiar icons appear. Service selection should follow requirements and failure or cost assumptions.
- **Leaves out:** source modules, every API endpoint, detailed route and firewall tables (G3), and software-instance placement (G1) unless they decide the arrangement.
- **Definition used here:** this page covers *the cloud architecture of one workload*. *Reference architecture* is a separate status: a reusable, recommended arrangement with stated assumptions. Record status as `reference | proposed solution | declared implementation | observed deployment` rather than merging these names. As checked on 2026-10-14, AWS describes six pillars, Azure five and Google Cloud six; counts change and are not a diagram recipe.

## When to use and how to choose
- **Audience:** cloud and platform architects, operators, security reviewers, partners, decision-makers who need the main trade-offs.
- **Scenarios:** evaluating a landing pattern for the storefront and API; moving order processing and background jobs to managed services; choosing a production baseline for an availability target; how a chatbot, a vector store and a model endpoint compose; comparing cost and resilience options.
- **When not to use:** as a business overview, or as proof of deployment, compliance, availability or a quantified SLA.
- **vs neighbours:**
  - **G1** for which software instances run on which hosts.
  - **G3** for routing, segmentation, reachability.
  - **C3** or **C5** for provider-neutral structure.
  - **G4** for the delivery machinery.

## Notation and elements
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

## Best practices and anti-patterns
### Best practices
1. **Start from requirements and failure or cost assumptions,** then choose services.
2. **Respect an example's scope.** Azure's basic web app page says it is for learning and proof of concept, not production, so copying the picture does not give a production baseline.
3. **Show zone or region separation only when it exists and matters;** repeated icons do not prove replication, backup or recovery.
4. **Keep alternatives apart.** Do not draw an as-built path and a proposed service in the same style.
5. **Link, do not absorb,** detailed security and network views; state the shared-responsibility split in text.

### Anti-patterns
1. **Icon soup:** products with no workload role.
2. **Everything inside one VPC box,** including global or provider-managed services.
3. **Unlabelled arrows** that mix runtime, administration and delivery paths.
4. **Availability claims without mechanism:** two icons, no replication.
5. **A firewall-rule dump** instead of a service arrangement.

## Drawing recipe
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

## Evidence in a code repository
- **Services:** infrastructure-as-code modules and resource types, provider versions, configured service tiers and sizes, resource references.
- **Wiring:** event subscriptions, endpoints, queue and topic names, scaling and backup declarations, per-environment variants.
- **Workload roles:** application code explains roles but does not prove a managed service is provisioned.
- **Must come from people:** foundations managed outside the repository (accounts, landing zones, shared networks), actual sizes and costs, requirements and trade-offs.
- A dependency graph from the IaC tool is not a finished architecture. Label results "declared"; never run deployment operations for discovery.

## Guided-mode questions
1. Is this a reusable reference pattern or the architecture of one actual workload? (one workload)
2. Which provider, region and data-residency constraints apply? (one provider, one region, stated)
3. Which quality goals drive the design and what compromises are acceptable? (availability and cost; accept single-region)
4. Which infrastructure is already managed elsewhere? (shown as external)
5. Should routing, deployment and recovery be separate views? (yes, linked)

## Template
Model template: `assets/templates/G2.json` · Layout template: `statechart` · provider boundaries (region) become `boundary` groups and tiers or zones (edge, network and security, zone 1, zone 2, managed services) become `frame` groups ranked along the request path, so equal-rank zones sit side by side; services are nodes with a role in a chip, and arrows use `call`, `data` or `async` edge kinds; design status is carried in node `style` and `evidence`.

## Sample
Figure: `samples/ai-service-assistant/G1-AWS/en/diagram.svg` (published with the site)
