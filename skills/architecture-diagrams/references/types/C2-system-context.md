# System Context Diagram (系统上下文图)
<!-- Generated from content/en/types/C2-system-context.md by tools/build_skill_refs.py. Do not edit. -->
> What is this system, who uses it, and which other systems does it depend on or exchange with?
Scope: One software system as a black box, with the people and the external systems directly connected to it. Neighbours: C1, C3, B4, A3, A7, D2, C6, F2, G1.

## Meaning
It answers: *what is this system, who uses it, and which other systems does it depend on or exchange with?* The concern is scope and boundary: an agreement on where the system stops, readable by technical and non-technical people alike. It is Level 1 of the C4 model, created by Simon Brown, which is a notation-independent method, not a versioned standard; the same idea is the structured-analysis context diagram (DFD level 0), the systems-engineering context of a system of interest and arc42 section 3 "Context and Scope". ISO/IEC/IEEE 42010 prescribes no notation; this is a view under a context viewpoint. It deliberately leaves out everything inside the box, technology choices, protocols and deployment, and every system not directly connected.
**Definition used here:** a *software system* is what one team builds, owns and can see inside; a database or queue that team owns is inside the box, not a neighbour. Product domains, bounded contexts and capabilities are usually not software systems.

## When to use and how to choose
- **Audience:** everyone; the C4 model recommends it for all teams.
- **Scenarios:** the first picture of any architecture document or README; scope alignment at project start; onboarding; the entry point for security work (find every inbound and outbound party before threat modelling); change impact (which neighbours care about a release).
- **When not to use:** internals (C3/C4/C5), runtime flow (E1), data stores and schemas (D1/D2), hosting (G1), or dozens of peer systems with no single focus (C1). The C4 model notes it adds less for heavily customised packaged products, though Levels 1 and 2 can still help.
- **vs neighbours:**
  - Choose **C1** when many systems at enterprise or department scope matter; the C4 model System Landscape diagram is the bridge, "a system context diagram without a specific focus".
  - Choose **C3** as soon as you need applications, data stores or technology inside the box.
  - Choose **B4** (variant "context with scope exclusions") when negotiating what is in and out of scope.
  - Choose **D2** when data flows and stores are the question: DFD lines name data, C2 lines name intent.
  - Choose **C6** for protocol, sync/async, authentication and SLA per interface (arc42 "technical context").
  - Choose **A3** for organisations, roles and stakeholder interest rather than systems.

## Notation and elements
- **Required:** title with type and scope ("System Context diagram for <System>"); exactly **one** system in scope, typed and with a one-line description; **people** as roles, not named individuals; **external systems** directly connected, typed and described; **relationships** with one direction each and an intent label (verb phrase) that agrees with the direction; a **legend** for shapes, colours, borders, line styles and arrowheads; acronyms explained.
- **No protocols or technologies on Level 1 lines.** The context diagram is about people and systems, not technologies or protocols. Put protocols on C3 lines, or in a separate technical-context table (arc42) or an interface table (C6).
- **Labels:** "Places orders with", "Sends payment requests to", "Reports stock levels to"; avoid the bare word "Uses". Aim for six words or fewer (a heuristic, not a rule).
- **Arrow semantics:** either "initiator → dependency" (C4 model, Azure guidance) or "data flows from → to" (arc42 business-context tip). Pick one, print it in the legend, never mix. No unexplained double-headed arrows; draw two lines or annotate request/response.
- **Optional:** grouping of many similar neighbours by an explicit criterion; a frame around "our organisation" drawn as a plain group (Structurizr marks the old "enterprise boundary" as deprecated in favour of groups); a caption naming the main data exchanged.
- **Shapes and colour:** boxes and lines; one style for the system in scope, one for external systems, one for people; generic shapes rather than vendor logos; must survive greyscale printing.
- **Tools:** C4-PlantUML covers Level 1 with a legend; Mermaid's C4 model syntax is marked experimental.
- **Size:** about 3–7 neighbours reads well; past about 12 external systems, group them or check whether levels are mixed (heuristic).

## Best practices and anti-patterns
### Best practices
1. Make it stand alone: title, typed elements, labelled lines and a legend, with no narrative needed.
2. Keep it readable by non-technical people: plain verbs, generic shapes, no technology names.
3. Show every real external interface, including manual, file-based and batch ones.
4. Cluster many similar neighbours into labelled groups instead of dropping them.
5. Keep the business context (always) separate from the technical context (only when channels matter, as a table or a C3/C6 view).

### Anti-patterns
1. Boundary confusion: an internal database or queue drawn as an external system, or another team's system drawn inside the box.
2. Level 2 content leaking in: containers, databases, ports, load balancers, technology names.
3. Protocols on the lines ("REST", "HTTPS", "Kafka"); they belong on C3 or in an interface table.
4. Vague or missing labels ("Uses"), no direction, no legend.
5. Named individuals instead of roles, transitive systems that are not directly connected, or speculative integrations drawn as live.

## Drawing recipe
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

## Evidence in a code repository
- README, docs, service catalogue entries (system, owner, consumed and provided APIs, `dependsOn`).
- Configuration and environment variables for third-party endpoints (identity issuer, mail host, payment API base URL); SDKs in package manifests.
- API specs: OpenAPI servers, security schemes and callbacks; AsyncAPI channels shared with other teams.
- Outbound call sites, produced and consumed topics, scheduled imports and exports; ingress (who calls in) and egress rules.
- Role and permission definitions, UI route groups and runbooks give candidate person roles.
- Not in code: who the business users are, what counts as "external", and ownership. Confirm every code-derived neighbour with people.

## Guided-mode questions
1. What is the system called, what does it do in one sentence, and what exactly does your team own? (the deployable parts in your repositories)
2. Who will read it? (both business and technical readers, so no technology on the figure)
3. Which user and operator roles interact with it, and are there non-human callers? (end users plus one support or admin role)
4. Which external systems call it, are called by it, or exchange files with it, and who owns each? (all directly connected ones, clustered if more than about 12)
5. Arrows mean "who calls whom" or "which data flows"; as-is or to-be? (who calls whom; as-is, planned links marked in the legend)

## Template
Model template: `assets/templates/C2.json` · Layout template: `nested` · one `system` node with style `primary` at the centre (no children shown), `person` and `external` nodes around it, `edges` with intent labels and no technology field.

## Sample
Figure: `samples/C2-system-context.svg` (published with the site)
