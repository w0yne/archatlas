---
code: C2
slug: system-context
family: C
names:
  en: System context diagram (C4 model level 1)
  zh: 系统上下文图（C4 模型第 1 层）
  aliases:
    en: [system context diagram, system environment diagram, context-level DFD, C4 model Level 1, Structured-analysis Context Diagram]
    zh: [系统上下文图, 系统环境图, 上下文级数据流图, C4 模型第 1 层]
question: What is this system, who uses it, and which other systems does it depend on or exchange with?
audiences: [leaders, business, architects, developers, security]
levels: [concept]
phases: [initiate, requirements, design]
scope: One software system as a black box, with the people and the external systems directly connected to it.
formal: {kind: method, ref: 'C4 model (Simon Brown), Level 1 System Context diagram; notation-independent, no versioned standard'}
neighbours: [A3, A7, B4, C1, C3, C6, D2]
status: draft
---

# System Context Diagram (系统上下文图)

> One system as a single box in the middle, with its users and the systems it talks to around it.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
It answers: *what is this system, who uses it, and which other systems does it depend on or exchange with?* The concern is scope and boundary: an agreement on where the system stops, readable by technical and non-technical people alike [1]. It is Level 1 of the C4 model, created by Simon Brown, which is a notation-independent method, not a versioned standard [2][6][7]; the same idea is the structured-analysis context diagram (the context-level DFD; "level 0" is used for it by some authors and for the next level down by others) [10], the systems-engineering context of a system of interest [11] and arc42 section 3 "Context and Scope" [8]. ISO/IEC/IEEE 42010 prescribes no notation; this is a view under a context viewpoint [19]. It deliberately leaves out everything inside the box, technology choices, protocols and deployment, and every system not directly connected [1][13].
**Definition used here:** a *software system* is what one team builds, owns and can see inside; a database or queue that team owns is inside the box, not a neighbour [4]. Product domains, bounded contexts and capabilities are usually not software systems [4].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** everyone; the C4 model recommends it for all teams [1].
- **Scenarios:** the first picture of any architecture document or README; scope alignment at project start; onboarding; the entry point for security work (find every inbound and outbound party before threat modelling); change impact (which neighbours care about a release).
- **When not to use:** internals (C3/C4/C5), runtime flow (E1), data stores and schemas (D1/D2), hosting (G1), or dozens of peer systems with no single focus (C1). The C4 model notes it adds less for heavily customised packaged products, though Levels 1 and 2 can still help [6].
- **vs neighbours:**
  - Choose **C1** when many systems at enterprise or department scope matter; the C4 model System Landscape diagram is the bridge, "a system context diagram without a specific focus" [5].
  - Choose **C3** as soon as you need applications, data stores or technology inside the box.
  - Choose **B4** (a separate scope diagram with in- and out-of-scope regions) when negotiating what is in and out of scope.
  - Choose **D2** when data flows and stores are the question: DFD lines name data, C2 lines name intent.
  - Choose **C6** for protocol, sync/async, authentication and SLA per interface (arc42 "technical context").
  - Choose **A3** for organisations, roles and stakeholder interest rather than systems.
  - Choose **A7** when leaders need the solution's main blocks in business terms rather than the system's users and neighbours.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required [2][3]:** title with type and scope ("System Context diagram for `<System>`"); exactly **one** system in scope, typed and with a one-line description; **people** as roles, not named individuals; **external systems** directly connected, typed and described; **relationships** with one direction each and an intent label (verb phrase) that agrees with the direction; a **legend** for shapes, colours, borders, line styles and arrowheads; acronyms explained.
- **No protocols or technologies on Level 1 lines.** The context diagram is about people and systems, not technologies or protocols [1]. Put protocols on C3 lines, or in a separate technical-context table (arc42 [8]) or an interface table (C6).
- **Labels:** "Places orders with", "Sends payment requests to", "Reports stock levels to"; avoid the bare word "Uses" [2]. Aim for six words or fewer (a heuristic, not a rule [18]).
- **Arrow semantics:** either "initiator → dependency" (C4 model, Azure guidance [9]) or "data flows from → to" (arc42 business-context tip [8]). Pick one, print it in the legend, never mix. No unexplained double-headed arrows; draw two lines or annotate request/response [9].
- **Optional:** grouping of many similar neighbours by an explicit criterion [8]; a frame around "our organisation" drawn as a plain group (Structurizr marks the old "enterprise boundary" as deprecated in favour of groups [12]); a caption naming the main data exchanged.
- **Shapes and colour:** boxes and lines; one style for the system in scope, one for external systems, one for people; generic shapes rather than vendor logos [9]; must survive greyscale printing.
- **Tools:** C4-PlantUML covers Level 1 with a legend [14]; Mermaid's C4 model syntax is marked experimental [15].
- **Size:** about 3–7 neighbours reads well; past about 12 external systems, group them or check whether levels are mixed (heuristic [18]).

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. Make it stand alone: title, typed elements, labelled lines and a legend, with no narrative needed [2].
2. Keep it readable by non-technical people: plain verbs, generic shapes, no technology names [1][9].
3. Show every real external interface, including manual, file-based and batch ones [8].
4. Cluster many similar neighbours into labelled groups instead of dropping them [8].
5. Keep the business context (always) separate from the technical context (only when channels matter, as a table or a C3/C6 view) [8].

### Anti-patterns
1. Boundary confusion: an internal database or queue drawn as an external system, or another team's system drawn inside the box [4].
2. Level 2 content leaking in: containers, databases, ports, load balancers, technology names [17][18].
3. Protocols on the lines ("REST", "HTTPS", "Kafka"); they belong on C3 or in an interface table [1].
4. Vague or missing labels ("Uses"), no direction, no legend [2][3].
5. Named individuals instead of roles, transitive systems that are not directly connected, or speculative integrations drawn as live [17].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [C4 model: System context diagram](https://c4model.com/diagrams/system-context) — the canonical, deliberately sparse picture with a key (CC BY 4.0).
- [Structurizr examples: Big Bank plc](https://github.com/structurizr/examples) — one model rendered as landscape, context, container and deployment views (licence: check the repository).
- [arc42 section 3: Context and Scope](https://docs.arc42.org/section-3) — business vs technical context, a partner / input / output table form and practical tips (CC BY-SA 4.0).
- [Azure Well-Architected: Create architecture design diagrams](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams) — vendor-neutral advice on context diagrams: black box, personas, explicit boundary, generic shapes.
- [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML) — text macros for a faithful Level 1 with a legend (MIT). Mermaid's C4 model syntax is marked experimental, so treat it as a draft path only.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Write one sentence naming the system and what the owning team builds and owns (e.g. "Online Shop: browse the catalogue, fill a cart, check out").
2. List people as roles (Shopper, Customer Support Agent, Catalogue Manager); group similar roles.
3. List external systems that are directly connected (Payment Provider, Warehouse System, Customer Support System with its support chatbot, Email Service); drop anything not directly connected; cluster look-alikes.
4. For each link choose the direction by your arrow convention and write an intent label of six words or fewer. No protocols.
5. Layout: the system box in the middle and larger; people above; upstream sources on one side, downstream consumers on the other; shared services (identity, email) below. Top-to-bottom by default, left-to-right for wide slides. Straight, short lines; move boxes instead of routing around.
6. Styles: in-scope system saturated, external systems grey, people distinct; three text sizes (title > name > description).
7. Text budget: element = name + type + description of at most about 12 words; no bullet lists, no technology inside boxes.
8. Add the title, date and legend (shapes, colours, arrow meaning); then offer the next step: zoom into C3, add a technical-context table (C6), or widen to C1.

**Self-check**
- [ ] Exactly one system in scope; nothing inside it is visible.
- [ ] Every neighbour is directly connected and typed as person or external system.
- [ ] Every line has one direction and a specific intent label; no bare "Uses".
- [ ] No protocols, ports, databases, queues or product stacks anywhere on the figure.
- [ ] People are roles; similar neighbours are clustered, not dropped.
- [ ] Title (type + scope) and legend present; arrow convention stated; acronyms explained.
- [ ] Ownership check: nothing in the box is secretly external, and vice versa.
- [ ] A non-technical reader can explain the figure in one sentence; about 12 neighbours or fewer.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- README, docs, service catalogue entries (system, owner, consumed and provided APIs, `dependsOn`) [16].
- Configuration and environment variables for third-party endpoints (identity issuer, mail host, payment API base URL); SDKs in package manifests.
- API specs: OpenAPI servers, security schemes and callbacks; AsyncAPI channels shared with other teams.
- Outbound call sites, produced and consumed topics, scheduled imports and exports; ingress (who calls in) and egress rules.
- Role and permission definitions, UI route groups and runbooks give candidate person roles.
- Not in code: who the business users are, what counts as "external", and ownership. Confirm every code-derived neighbour with people.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. What is the system called, what does it do in one sentence, and what exactly does your team own? (the deployable parts in your repositories)
2. Who will read it? (both business and technical readers, so no technology on the figure)
3. Which user and operator roles interact with it, and are there non-human callers? (end users plus one support or admin role)
4. Which external systems call it, are called by it, or exchange files with it, and who owns each? (all directly connected ones, clustered if more than about 12)
5. Arrows mean "who calls whom" or "which data flows"; as-is or to-be? (who calls whom; as-is, planned links marked in the legend)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/C2.json` · Layout template: `statechart` · the system is one `system` node with style `highlight` inside a `boundary` group (with sibling systems of the same platform), `person` nodes on the left and `external` nodes on the right are ranked by their edges; short `sub` descriptions, chips for role, and `edges` with intent labels and no technology field.

## Sources {#sources}
<!-- skill: omit -->
1. C4 model — System context diagram — https://c4model.com/diagrams/system-context — accessed 2026-10-14
2. C4 model — Notation — https://c4model.com/diagrams/notation — accessed 2026-10-14
3. C4 model — Review checklist — https://c4model.com/diagrams/checklist — accessed 2026-10-14
4. C4 model — Software system — https://c4model.com/abstractions/software-system — accessed 2026-10-14
5. C4 model — System landscape diagram — https://c4model.com/diagrams/system-landscape — accessed 2026-10-14
6. C4 model — FAQ — https://c4model.com/faq — accessed 2026-10-14
7. C4 model — History — https://c4model.com/history — accessed 2026-10-14
8. arc42 — Section 3, Context and scope — https://docs.arc42.org/section-3 — accessed 2026-10-14
9. Microsoft Learn — Create architecture design diagrams (Azure Well-Architected) — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — accessed 2026-10-14
10. E. Yourdon — Just Enough Structured Analysis, ch. 9 (online edition) — https://www.businessanalystlearnings.com/s/Yourdon-DFD.pdf — accessed 2026-10-14
11. SEBoK — Introduction to Systems Engineering Fundamentals (system context) — https://sebokwiki.org/wiki/Introduction_to_Systems_Engineering_Fundamentals — accessed 2026-10-14
12. Structurizr — Diagram notation — https://docs.structurizr.com/ui/diagrams/notation — accessed 2026-10-14
13. Structurizr — DSL language reference — https://docs.structurizr.com/dsl/language — accessed 2026-10-14
14. C4-PlantUML — https://github.com/plantuml-stdlib/C4-PlantUML — accessed 2026-10-14
15. Mermaid — C4 diagrams — https://mermaid.js.org/syntax/c4 — accessed 2026-10-14
16. Backstage — System model — https://backstage.io/docs/features/software-catalog/system-model — accessed 2026-10-14
17. Working Software — Misuses and mistakes of the C4 model — https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model — accessed 2026-10-14
18. Visual Paradigm — C4 context diagram guide — https://www.visual-paradigm.com/guide/c4-context-diagram-the-best-way-for-beginners-to-visualize-software-architecture — accessed 2026-10-14
19. IEEE SA — ISO/IEC/IEEE 42010:2022 — https://standards.ieee.org/ieee/42010/6846 — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![C2 sample: system context of an online shop with people and external systems](/samples/C2-system-context.svg)
*System context of the online shop. Inside the dashed platform boundary are the online shop (the subject, highlighted), the support chatbot and the back office; outside are three people (customer, support agent, shop admin) on the left and four external systems on the right (payment provider, carrier, email service, language model service). Each element has a one-line description, and arrows are labelled with the exchange; the email arrow is asynchronous.*
