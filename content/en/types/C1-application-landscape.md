---
code: C1
slug: application-landscape
family: C
names:
  en: Application landscape
  zh: 应用全景图
  aliases:
    en: [application portfolio view, application communication diagram, system landscape diagram, IT landscape, Application Architecture (portfolio sense), Application Landscape Map, Application Cooperation View, System Landscape Diagram (C4 model), Cluster Map]
    zh: [应用地图, 系统全景图, 应用组合图, 应用协作视图, IT 蓝图]
question: Which applications exist in this scope, how are they grouped, and which depend on or exchange data with which?
audiences: [architects, leaders]
levels: [logical]
phases: [initiate, design]
scope: Many applications within one stated scope (enterprise, department or product line), drawn at application level only.
formal: {kind: method, ref: 'No single notation. Related: TOGAF 9.2 Application Communication diagram and Application Portfolio catalog; ArchiMate 3.2 Application Cooperation viewpoint; C4 model System Landscape diagram'}
neighbours: [A1, A7, A8, C2, C3, C5, C6, I2]
status: draft
---

# Application Landscape (应用架构图)

> A map of the applications in one scope, grouped by a stated criterion and connected by their main dependencies.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
It answers: *which applications do we have here, grouped how, and which depend on or exchange data with which?* It is a portfolio-level viewpoint in the ISO/IEC/IEEE 42010 sense: the concerns are overlap, ownership, change impact and integration hot spots [9]. TOGAF places it in the application architecture domain (Application Portfolio catalog, Application Communication diagram) [2][3]; in ArchiMate it is close to the Application Cooperation viewpoint [5]. It leaves out application internals (C3/C4/C5), hosting (G1), interface attributes such as protocol, authentication or SLA (C6), data schemas (D1) and process flow (A5).
**Definition used here:** "application architecture" has two meanings, the portfolio of many applications (TOGAF, this type) and the internal design of one application [2][10]. Many applications → C1; the parts of one application → C3, C5 or C8.
**Three variants under this id:** (a) *grouped landscape*: applications placed in bands by layer, domain or capability (default); (b) *communication map*: relationship-centred, core applications in the middle (TOGAF Application Communication diagram, ArchiMate Application Cooperation view, the cluster maps of the EAM Pattern Catalog [14]); (c) *capability × application matrix*, a derived view of A1: rows = capabilities, cells = applications, optionally as a heat map (TOGAF Application/Function matrix) [3][11]. The C4 model **System Landscape** diagram is the minimal form of (a)/(b): people and software systems at a stated scope, no containers and no portfolio metadata, "a system context diagram without a specific focus" [1].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** architects, IT leadership, portfolio and integration teams, security (blast radius), new architects joining.
- **Scenarios:** portfolio rationalisation, e.g. with a Tolerate/Invest/Migrate/Eliminate fit grid [21]; impact check before replacing or retiring an application; merger or platform consolidation [20]; overview of a shared platform with business applications on top; baseline for a target-state roadmap (A8).
- **When not to use:** one system with only a few neighbours (C2); internals of one system (C3/C5); field-level data flows (D2/C6); nobody will keep it current, since a stale landscape misleads [10][12].
- **vs neighbours:**
  - Choose **C2** when one system is the focus and you need its users and neighbours.
  - Choose **C3** when you need the running parts of one system and their technology.
  - Choose **C6** when every interface needs protocol, authentication, frequency or SLA.
  - Choose **A1** (with variant c here as an overlay) when the question is business capability coverage.
  - Choose **I2** when business, application and technology layers must appear in one ArchiMate view.
  - Choose **A7** when non-technical readers need the main blocks of one solution, not the inventory of applications.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required:** application boxes named as the organisation names them, all of the same kind [16]; grouping frames with one stated criterion (layer, domain, capability or owner), each application in exactly one group [10]; directed relationship lines with a short label naming what flows or why; title with type, scope and date; legend for every colour, border and badge [15][22]; a scope statement saying what is inside and what is external.
- **Optional:** one metadata overlay at a time: lifecycle (planned / live / retiring), sourcing (build / buy / SaaS) or owner, shown as a tag or a single colour scale [10]; a shared-platform band; external services at the edge in a quieter style; a data store shape only when the store is a shared integration point.
- **Interfaces:** TOGAF's Application Communication diagram does show interfaces between applications [3][13]. The line to C6 is drawn by the *level of attributes* (protocol, authentication, SLA, frequency), not by whether an interface appears at all.
- **Arrow semantics:** pick one and print it in the legend: "A → B = A depends on / calls B" (C4 model, Azure guidance [15]) or "A → B = data flows from A to B" (ArchiMate flow). Never mix them; avoid double-headed arrows.
- **Grouping:** the bands "channels / business applications / shared platform / external" are one common pattern, not a standard. Ask which axis fits the question.
- **ArchiMate mapping (if a formal model is wanted):** Application Component per application, `serving` for "uses the service of", `flow` for data movement [8]. Name the version: ArchiMate 3.2 (2022) is what most tools implement; ArchiMate 4 (announced April 2026) renames layers to "domains" and merges layer-specific behaviour elements [6][7]. The ArchiMate 4 details are taken from published summaries and are not verified against the current spec text.
- **TOGAF artefacts nearby:** Interface catalog, Application/Function, Application/Organisation and Application Interaction matrices, Application and User Location diagram [3][4]. These names are from TOGAF 9.x material; they are not verified against the current TOGAF 10 text.
- **Detail and naming:** application level only. If you want to list modules or features in a box, open a C3 or C5 diagram instead. Peers use the same kind of name; never name an application after a capability [11].

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. Fix the scope, the grouping axis and the inventory source before drawing; place groups first, then applications [10][12].
2. Treat metadata as an overlay, not geometry: one status per view, explained by a legend; a second status needs a second view [10].
3. Manage density with focused views: one overview, then one diagram per domain, instead of one crowded poster [12][22].
4. Anchor the layout on the hubs: the most-connected applications in the centre, applications linked to two hubs between them, single-hub applications beside their hub [13].
5. Keep it alive: derive applications and integrations from a catalogue or code, let people own grouping, ownership and lifecycle, and print the update owner and date [10][19].

### Anti-patterns
1. A list of boxes without relationships: that is a catalogue, not a landscape [10].
2. Technical parts (cache, queue, load balancer) drawn as peers of applications, or capabilities, processes and applications mixed in one row [11].
3. Several statuses encoded at once through colour, border, icon and label [10].
4. Integrations deleted when the picture gets crowded; connect to the group border instead [10].
5. Working notes, decisions or rationale on the figure; put them in the text or a decision record [23].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [C4 model: System landscape diagram](https://c4model.com/diagrams/system-landscape) — the smallest landscape notation with an exact scope rule (site content CC BY 4.0).
- [Structurizr: enterprise usage](https://docs.structurizr.com/workspaces/enterprise) — a landscape generated from team-owned definitions instead of being hand-drawn.
- [TU München EAM Pattern Catalog v1.0](https://www.cs.cit.tum.de/fileadmin/w00cfj/sebis/_my_direct_uploads/EAMPatternCatalogV1.0.pdf) — cluster maps, process-support maps and information-flow views, each tied to stakeholder concerns (© TU München; read, do not copy).
- [ArchiSurance case study](https://github.com/archimate-models/archisurance) — baseline and target application architectures in ArchiMate Application Cooperation views (licence: check the repository).
- [Dragon1: how to create an application landscape diagram](https://www.dragon1.com/tutorials/how-to-create-an-application-landscape-diagram) — the full process from mandate and data collection to layout and maintenance.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Write one sentence of scope and lens (which scope; what counts as one application) and put it in the title or legend.
2. Inventory the applications: name, one-line purpose, owner, lifecycle; mark each internal, shared platform or external.
3. Choose the variant (grouped, communication map, capability matrix) and one grouping axis; one primary group per application.
4. Layout: top-to-bottom bands for (a) (channels → business applications → shared platform; external at the side or bottom); hubs in the centre for (b); grid for (c). Example: an online shop with Web Shop and Mobile App on top, Catalogue, Cart & Checkout, Order Management and Customer Support (with Support Chatbot) in the middle, Identity and Data Platform below, Payment Provider and Warehouse System at the edge.
5. Weight: protagonist larger, peers equal size and style, "other applications" small and quiet; a shared application keeps one style everywhere.
6. Lines: only dependencies the question needs; label with what flows (1–3 words, e.g. "orders", "stock levels"), no protocols; end each arrow on the exact box, or on the group border for group-level links.
7. At most one metadata overlay; colour plus a second cue (tag or pattern); legend for all of it.
8. Text budget: box = name plus at most a 3-word descriptor; no bullet lists, feature lists or notes.

**Self-check**
- [ ] Title states type and scope; legend explains every colour, line and badge.
- [ ] Every box is an application of the same kind; no capabilities, components or steps mixed in.
- [ ] Every application sits in exactly one group, and every group has a clear criterion.
- [ ] Every line has one direction and a label; one arrow convention, stated.
- [ ] No internals, hosting nodes or protocol details (C3, G1, C6).
- [ ] At most one status overlay; peers look alike.
- [ ] No working notes, TBDs or rationale on the figure.
- [ ] Each element traces to an inventory row, manifest or catalogue entry, or is marked as planned.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Service catalogue files (e.g. Backstage `catalog-info.yaml`: system, owner, lifecycle, `dependsOn`, provided and consumed APIs) [17].
- Kubernetes labels such as `app.kubernetes.io/part-of` and `name`, ingress routes, network policies [18]; compose files (roll services up to their application).
- API specs (OpenAPI, AsyncAPI, protobuf) and internal client libraries give provider–consumer pairs; `CODEOWNERS` gives owners.
- Infrastructure-as-code resource tags (`application`, `owner`) give inventory but weak dependencies; CI pipelines show which applications are alive.
- Not in code: bought and SaaS applications without a repository, the grouping axis, business ownership and lifecycle decisions. Ask people, or use an asset or procurement list. Treat everything from code as a candidate to confirm.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which scope, and what counts as one application here? (one product line; one team-owned system = one application)
2. Which decision should the map support: rationalisation, impact analysis, onboarding or integration planning? (impact analysis)
3. Which variant and grouping axis: layer, domain, capability or owner? (grouped landscape by layer)
4. Which single attribute should the overlay show: lifecycle, sourcing, owner or none? Current or target state? (none; current state)
5. Arrows mean "depends on" or "data flows to"; all links or only those crossing groups? (depends on; only links needed for the question)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/C1.json` · Layout template: `layered` · groups of kind `layer` become bands; `system` and `external` nodes are placed in their band; edges route between bands (variant c uses `tables[]` rendered with `grid_table`).

## Sources {#sources}
<!-- skill: omit -->
1. C4 model — System landscape diagram — https://c4model.com/diagrams/system-landscape — accessed 2026-10-14
2. The Open Group — TOGAF Standard, 10th Edition launch — https://www.opengroup.org/open-group-announces-launch-togaf-standard-10th-edition — accessed 2026-10-14
3. TOGAF Standard Courseware V9.1 — Sample catalogs, matrices and diagrams — http://www.togaf.info/togafSlides91/TOGAF-V91-Sample-Catalogs-Matrics-Diagrams-v3.pdf — accessed 2026-10-14
4. QualiWare CoE — TOGAF artifacts — https://coe.qualiware.com/resources/togaf/togaf-artifacts — accessed 2026-10-14
5. The Open Group — ArchiMate 3.2 Specification reference cards — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — accessed 2026-10-14
6. The Open Group — ArchiMate 4 Specification announcement — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — accessed 2026-10-14
7. Bizzdesign — What really changes in ArchiMate 4 — https://bizzdesign.com/blog/archimate-4-changes — accessed 2026-10-14
8. Bizzdesign — Practical ArchiMate viewpoints for the application layer — https://bizzdesign.com/blog/practical-archimate-viewpoints-for-the-application-layer — accessed 2026-10-14
9. IEEE SA — ISO/IEC/IEEE 42010:2022 — https://standards.ieee.org/ieee/42010/6846 — accessed 2026-10-14
10. Catio — Application landscape diagrams — https://www.catio.tech/blog/application-landscape-diagram — accessed 2026-10-14
11. Sparx Systems — Application landscape view guide — https://www.sparxsystems.us/application-portfolio-management/application-landscape-view-guide — accessed 2026-10-14
12. Dragon1 — How to create an application landscape diagram — https://www.dragon1.com/tutorials/how-to-create-an-application-landscape-diagram — accessed 2026-10-14
13. Orbus Software — Landscape diagrams part 6: application communication diagram — https://www.orbussoftware.com/resources/blog/detail/landscape-diagrams-pt6-application-communication-diagram — accessed 2026-10-14
14. TU München sebis — EAM Pattern Catalog v1.0 — https://www.cs.cit.tum.de/fileadmin/w00cfj/sebis/_my_direct_uploads/EAMPatternCatalogV1.0.pdf — accessed 2026-10-14
15. Microsoft Learn — Create architecture design diagrams (Azure Well-Architected) — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — accessed 2026-10-14
16. Martin Fowler — Application Boundary — https://martinfowler.com/bliki/ApplicationBoundary.html — accessed 2026-10-14
17. Backstage — System model — https://backstage.io/docs/features/software-catalog/system-model — accessed 2026-10-14
18. Kubernetes — Recommended labels — https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/ — accessed 2026-10-14
19. Structurizr — Enterprise usage — https://docs.structurizr.com/workspaces/enterprise — accessed 2026-10-14
20. ArchiSurance case study — https://github.com/archimate-models/archisurance — accessed 2026-10-14
21. LeanIX — Gartner TIME model — https://www.leanix.net/en/wiki/apm/gartner-time-model — accessed 2026-10-14
22. C4 model — Notation — https://c4model.com/diagrams/notation — accessed 2026-10-14
23. Working Software — Misuses and mistakes of the C4 model — https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![C1 sample: application landscape of an online shop in four layers](/samples/C1-application-landscape.svg)
*Application landscape of the online shop in four layers, each a tinted zone: channels (web storefront, mobile app, support chat widget), business applications (shop, back office, support chatbot), shared platform (identity, notifications, search) and external services (payment provider, carrier, email service). Chips name the access type or ownership, the dark card is the subject (the shop), and arrows between layers say what flows.*
