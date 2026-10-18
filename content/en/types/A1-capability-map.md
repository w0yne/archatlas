---
code: A1
slug: capability-map
family: A
names:
  en: Business capability map
  zh: 业务能力图
  aliases:
    en: [capability map, capability heat map, capability landscape, business capability model]
    zh: [能力地图, 能力热力图, 业务能力模型]
question: What must the business be able to do, independent of who does it, how, or with which system, and which of those abilities are strong, weak, missing or strategic?
audiences: [leaders, business, architects]
levels: [strategy]
phases: [initiate]
scope: One enterprise or business unit, 2–3 capability levels on one page, optionally with one assessment overlay
formal: {kind: standard, ref: 'ArchiMate 3.2 Capability element and Capability Map viewpoint; TOGAF Series Guide: Business Capabilities, Version 2 (G211, 2022) and BIZBOK Guide for content rules'}
neighbours: [A2, A5, A7, A8, C1]
status: draft
---

# Business Capability Map (业务能力图)

> A one-page map of everything the business must be able to do, grouped into tiers and levels, with no flow, no org units and no systems.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
<!-- skill-text
- **Question:** what abilities does the business need, regardless of who performs them, how, or with which system? With a heat overlay: which are weak, missing or strategic?
- **Viewpoint:** ArchiMate Capability Map viewpoint; TOGAF Phase B artefact (Business Capability Map). It shows the enterprise "at rest"; value streams (A2) and processes show it "in motion".
- **Value:** a capability model is stable against org structure, processes and applications, so it anchors cross-maps to org units, value-stream stages, applications and initiatives.
- **Leaves out:** sequence, org units, roles, systems, technology, product catalogue.
- **Definition used here:** the *model* is the full set of capabilities (often 3–6 levels); the *map* is its one-page picture (2–3 levels). Follows ArchiMate 3.2.
-->
- **Question:** what abilities does the business need, regardless of who performs them, how, or with which system? With an overlay: which abilities are weak, missing, strategic or over-invested?
- **Viewpoint:** ArchiMate *Capability Map viewpoint* (stakeholders: business managers, enterprise and business architects; purpose: designing and deciding; scope: Strategy) [3]. TOGAF places it in Phase B, with use in Phase A for vision and prioritisation, and names the artifacts *Business Capability Map* (diagram) and *Business Capabilities catalog* [1][2][11]. There is no C4 model level for it: the map sits above any system.
- **Deeper meaning:** the map shows the enterprise "at rest"; value streams and processes show it "in motion" [4][3]. Its value is stability: a capability model is independent of org structure, processes, applications and product portfolio [1], so it can anchor cross-maps to org units, value-stream stages, applications and initiatives. A capability only says that something must exist, not how well; "how well" is added by a heat-map overlay [1].
- **Leaves out:** sequence and flow, organisation units, roles, systems, technology and the product catalogue. Each of these is a separate view or cross-map [1][4].
- **Definition used here:** the *model* is the full, defined set of capabilities (commonly 3–6 levels deep [1]); the *map* is its one-page picture (2–3 levels [3]). ArchiMate defines a Capability as "an ability that an active structure element, such as an organisation, person, or system, possesses" [3].
- **Version note:** this page follows ArchiMate 3.2. ArchiMate 4 (announced April 2026) renames layers to domains; this is not verified against the current spec text.

| Concept | What it says | Naming | Stability |
|---|---|---|---|
| Capability | *What* the business can do | Noun or gerund ("Order Management") | Highest |
| Business function | Behaviour grouped by skills, "closely aligned to an organisation" [3] | Noun | Medium |
| Business process | *How*: time-ordered steps for a case | Verb-noun ("Handle Return") | Low |
| Value stream (A2) | *How value accrues* to a stakeholder, in stages | Verb-noun ("Fulfil Customer Order") | High |
| Organisation unit | *Who* | Department name | Lowest [1] |

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** executives and sponsors (Level 1 only), strategy and portfolio leads, enterprise and business architects (more depth).
- **Scenarios:** annual planning with a heat map; rationalisation after an acquisition (duplicate capabilities); scoping a transformation (new vs existing); application portfolio overlay (a derived view); team design around capabilities.
- **When not to use:** the question is sequence, timing or hand-offs (A2, A5, E4), system structure (C family) or one project's backlog (B family). Without agreed definitions, a one-level map with definitions beats a deep, contested one.
- **vs neighbours:**
  - **A2 Value Stream** for how value reaches a stakeholder; usually cross-mapped with A1.
  - **A5 BPMN Process** for steps, gateways, hand-offs.
  - **A3 Business Context** for "who"; capability × org is a matrix, not a merged picture.
  - **C1 Application Landscape** when the reader needs systems; the overlay is a derived view.
  - **A7 Conceptual Architecture** for "what are the parts"; a list of business abilities is A1, a list of product features is B3.
  - **A8 Roadmap** for when change happens.
-->
- **Audience:** executives and sponsors (usually Level 1 only), strategy and portfolio leads, enterprise and business architects (more depth) [1].
- **Classic scenarios:**
  1. Annual planning: an online shop heat-maps capability maturity against strategic importance and funds the weak, important tiles [1].
  2. Rationalisation after the shop acquires a competitor: cross-maps expose two "Customer Management" implementations [1].
  3. Scoping a transformation: which capabilities are new (e.g. a support chatbot needs "Automated Customer Assistance") and which already exist [1].
  4. Application portfolio review: an overlay of applications per capability shows gaps and overlaps (a derived view).
  5. Team design: long-lived teams aligned to business capabilities [7].
- **When not to use:** the question is sequence, timing or hand-offs (A2, A5, E4); the question is system structure (C family); the content is one project's feature backlog (B family). If there are no agreed definitions and a decision is due this week, a one-level map with definitions beats a deep, contested one.
- **vs neighbours:**
  - Choose **A2 Value Stream** when the question is how value reaches a stakeholder, stage by stage; the two are usually cross-mapped [5].
  - Choose **A5 BPMN Process** when the question is steps, gateways or hand-offs.
  - Choose **A3 Business Context** (or a stakeholder map) when the question is "who"; capability × org is a matrix, not a merged picture.
  - Choose **C1 Application Landscape** when the reader needs systems; a capability-to-application overlay is a derived view and must be labelled as such.
  - Choose **A7 Conceptual Architecture** when the question is "what are the parts": an architecture shows components. A list of business abilities is a capability map (A1); a list of product features is a feature tree (B3).
  - Choose **A8 Target Architecture and Roadmap** for when change happens; a current-vs-target maturity heat map feeds it.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** ArchiMate gives a formal Capability element (rounded rectangle with a stepped icon) and a Capability Map viewpoint [3][8]. The common business rendering is a convention: nested tiles, no arrows, optional colour overlay. TOGAF and BIZBOK prescribe content rules, not graphics [1][4].
- **Required:**
  - **Capability tiles,** each with a business-object-based name and a written definition in the catalogue, usually "Ability to …" [4].
  - **Hierarchy by nesting:** Level 1 tiles contain their Level 2 children; 2–3 levels per page [3].
  - **Level 1 stratification** into tiers, usually *Strategic* (direction-setting), *Core / customer-facing* and *Supporting* [1][4]. TOGAF notes that without stratification a large model is hard to read [1].
  - **Title** stating scope (enterprise or unit) and state (current or target).
- **Optional:**
  - **Heat-map overlay** with a legend. TOGAF lenses: maturity (green = at the desired level, yellow = one level away, red = two or more away, purple = desired but not existing), strategic contribution, performance, revenue contribution, cost contribution, coverage, criticality [1]. One lens per map.
  - **Cross-maps as separate views:** capability × org unit (matrix), capability × value-stream stage (A2), capability × application (overlay).
  - **ArchiMate rendering:** capabilities nested by composition or aggregation; Resource and Outcome elements are allowed in the viewpoint [3].
- **Lines:** none in the business rendering; containment means decomposition. ArchiMate allows *serving* between capabilities and *realization* by core elements [3]; keep these off the executive map.
- **Naming:** noun, compound noun or gerund ("Order Management", "Market Development") [1][3]. BIZBOK pattern: object plus action noun, e.g. Level 1 "Customer Management" → Level 2 "Customer Definition", "Customer Matching", "Customer Information Management" [4]. No department names [1], no system names ("CRM" is an application; "Customer Management" is the capability).
- **Text budget:** about 2–5 words per tile; definitions live in the catalogue. Siblings are the same kind of thing at the same level.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Define before you draw.** Name and define each capability, then test it by decomposing it into the roles, processes, information and tools that realise it; this checks that it is a capability, not a process, function or service [1]. Work business objects first, then actions on them, then decomposition [4].
2. **One map for the enterprise, each capability once,** even if several units perform it. Show the multiplicity in a capability × org cross-map [1][4].
3. **Build top-down with senior leaders, refine bottom-up.** Keep Level 1 small enough for senior leaders to ratify [1].
4. **Treat the heat map as a decision aid:** one stated criterion, a scale and a date or source. Different heat maps come from the same model [1].
5. **Use the stable map as the anchor** for cross-maps to value streams [5], org units, applications and initiatives [1][6].

### Anti-patterns
1. **The org chart re-labelled as capabilities.** TOGAF names this a common mistake [1].
2. **A system inventory as capabilities** ("CRM", "Data Lake" as tiles). When IT writes the names alone, the model reads like a system inventory with better labels [9].
3. **Processes or steps as capabilities** ("Approve refund"); verb-noun steps belong in a value stream or process [1][3].
4. **Duplicates or overlapping siblings,** or mixed kinds in one row (a capability next to a team next to a step) [4].
5. **Heat colours without a legend or criterion,** several lenses in one colour scale, or red/green as the only cue [1]. Also avoid more than 3 levels on one page [3] and "TBD" or working notes on tiles.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [TOGAF Series Guide: Business Capabilities (G189, mirror PDF)](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf) — the "ABC Company" Level 1 model with strategic/core/supporting tiers, a maturity heat map with purple for missing capabilities, and a capability × org table. © The Open Group; read only.
- [Business Architecture Guild reference-model workshop deck](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf) — stratification picture, decomposition patterns and the BIZBOK principles in compact form. © Business Architecture Guild.
- [ArchiMate 3.2 Reference Cards](https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf) — the formal Capability notation. © The Open Group.
- [Bizzdesign: Business capabilities vs. business functions](https://bizzdesign.com/blog/capabilities-vs-business-functions-same-difference) — a high-level insurance capability map and a careful capability-vs-function explanation. Vendor blog.
- [SAP LeanIX: Business capability map examples and templates](https://www.leanix.net/en/wiki/ea/business-capability-map-examples-and-templates) — several industry L1/L2 layouts that show typical tile density [10]. Vendor content.
- [Martin Fowler bliki: Business Capability Centric](https://martinfowler.com/bliki/BusinessCapabilityCentric.html) — not a map, but shows the downstream use for team design.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix scope, state and lens; put them in the title, e.g. "Online shop: business capabilities, current maturity".
2. Draft the catalogue first (Tier, Level, Name, "Ability to …" definition); remove org, system and step names and duplicates; show it to the user before drawing.
3. Layout: three horizontal bands top to bottom (Strategic, Core, Supporting); Level 1 tiles are containers per band, Level 2 tiles a grid inside. Max 3 levels; above ~60 leaf tiles, one page per Level 1 domain.
4. Equal sizes for siblings, aligned grid; size encodes nothing unless the legend says so.
5. Text: 2–5 words per tile; no bullets, definitions or uncommon abbreviations on the figure.
6. Colour: neutral fills with light tier tints; a heat map uses one scale plus at most one extra category ("desired, not existing"), a legend with criterion and source/date, and a text or pattern cue for colour-blind readers.
7. No arrows. Cross-maps (value stream, org, applications) are separate figures; an app overlay is labelled "derived view".

**Self-check**
- [ ] Every tile is a capability: business object plus action noun, no system, org unit or step.
- [ ] Each capability appears once; siblings do not overlap and are the same kind and level.
- [ ] Level 1 is stratified into tiers; at most 3 levels are visible.
- [ ] The title states scope and current/target; no subtitle restating the type, no version label.
- [ ] Heat colours have a legend with criterion, scale and source; one lens only.
- [ ] No arrows, bullets, "TBD" or reasoning text on tiles.
- [ ] Every capability has a definition in the accompanying catalogue.
- [ ] Any application overlay is labelled as derived; the base map is system-free.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Candidate capabilities:** domain or bounded-context folders (`catalogue/`, `cart/`, `payment/`), route and menu definitions, feature-flag names, service names in deployment manifests, CODEOWNERS, issue labels and epics, analytics event families, README feature overviews. Map each to a business-object noun; drop technical modules (auth, logging).
- **Application overlay:** which repositories or services implement which capability.
- **Must come from people:** capabilities with no software (Brand Management, Supplier Management), definitions and tiering, which capabilities are strategic, maturity and investment scores, target-state capabilities.
- Mark any code-derived list as "candidate, to validate with the business".

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Scope and state: whole enterprise, one unit or one product area; current, target or both? (one unit, current)
2. Which decision should the map support: investment, rationalisation, transformation scope or team design? (investment, which sets the heat lens)
3. Is there an existing capability list or reference model to align with? (draft one from docs and interviews, marked candidate)
4. How many levels, and stratify Level 1 into Strategic / Core / Supporting? (2 levels, stratified)
5. If heat-mapped: which single criterion and scale, scored by whom, as of when? (maturity, 4-colour TOGAF scale, dated)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A1.json` · Layout template: `layered` · tiers become `layer` groups (bands), Level 1 capabilities become `frame` groups inside them, Level 2 capabilities are equal-size `component` nodes in a grid; heat values map to node `style` tokens (`primary`, `peer`, `planned`, `shared`) plus an auto-generated legend.

## Sources {#sources}
<!-- skill: omit -->
1. TOGAF Series Guide: Business Capabilities (G189, June 2018), The Open Group (mirror PDF) — https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf — accessed 2026-10-14
2. The Open Group, TOGAF Series Guide: Business Capabilities, Version 2 (G211, 2022; supersedes G189; part of TOGAF 10) — https://publications.opengroup.org/g211 — accessed 2026-10-14
3. ArchiMate 3.1 Specification (C197, 2019), §7.3.1 Capability, §8.3.2 Business Function, App. C.3.2 Capability Map Viewpoint (mirror PDF; the elements cited are unchanged in 3.2) — https://university.sk/wp-content/uploads/2020/01/ARCHIMATE_v3_1_specifikacia.pdf — accessed 2026-10-14
4. Business Architecture Guild, "Business Architecture Reference Model Workshop" (2019; BIZBOK Guide principles and patterns) — https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf — accessed 2026-10-14
5. TOGAF Series Guide: Value Streams (G178, republished 2022 for TOGAF 10) — https://publications.opengroup.org/g178 — accessed 2026-10-14
6. Bizzdesign, "Business capabilities vs. business functions: Same difference?" — https://bizzdesign.com/blog/capabilities-vs-business-functions-same-difference — accessed 2026-10-14
7. S. Narayan, "Business Capability Centric", martinfowler.com bliki (2016) — https://martinfowler.com/bliki/BusinessCapabilityCentric.html — accessed 2026-10-14
8. ArchiMate 3.2 Specification Reference Cards (N221, 2022) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — accessed 2026-10-14
9. Capstera, "Common Business Capabilities: A Practitioner's List" — https://capstera.com/knowledge-hub/articles/list-of-common-business-capabilities — accessed 2026-10-14
10. SAP LeanIX, "Business Capability Map Examples & Templates" — https://www.leanix.net/en/wiki/ea/business-capability-map-examples-and-templates — accessed 2026-10-14
11. The Open Group / OMG BASIG, "Advancement of Business Architecture in the TOGAF Standard" (TOGAF 9.2 Phase B artifacts: Business Capability Map, Business Capabilities catalog) — https://www.omg.org/cgi-bin/doc?basig%2F18-09-03.pdf= — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![A1 · Enterprise Service Assistant](/samples/ai-service-assistant/A1/en/diagram.svg)
*What can the organisation do, independent of who or what does it, and where should it invest?*

[SVG](/samples/ai-service-assistant/A1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

[Historical shop regression sample](/samples/A1-capability-map.svg) · [All 29 views](/use/ai-service-assistant) · [Illustrative assumptions](/use/ai-service-assistant-assumptions).
