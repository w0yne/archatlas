---
code: A2
slug: value-stream
family: A
names:
  en: Value stream (business architecture)
  zh: 价值流（业务架构）
  aliases:
    en: [value stream diagram, value stream stages, value stream capability cross-map, value stream, value stream map (TOGAF artifact), value stream / capability cross-map]
    zh: [价值流阶段图, 价值流能力映射, 价值流, 价值流阶段, 价值流—能力映射]
question: How does value accrue, stage by stage, for a triggering stakeholder, and which capabilities enable each stage?
audiences: [leaders, business, architects]
levels: [strategy]
phases: [initiate]
scope: 'One value stream: a triggering stakeholder, a value proposition and about 4–8 stages, optionally with capabilities cross-mapped under each stage'
formal: {kind: standard, ref: 'ArchiMate 3.2 Value Stream element and Value Stream viewpoint; TOGAF Series Guide: Value Streams (G178, republished 2022 for TOGAF 10); BIZBOK Guide'}
neighbours: [A1, A5, A6, A9]
status: draft
---

# Value Stream (Business Architecture) (价值流（业务架构）)

> A left-to-right row of value stages that shows how a triggering stakeholder ends up with the promised value, with the enabling capabilities stacked underneath and no times.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** how does the enterprise deliver value to one stakeholder, stage by stage, and which capabilities enable each stage? Value is "always defined from the perspective of the stakeholder" [1].
- **Viewpoint:** ArchiMate *Value Stream viewpoint*: "a structured overview of a value stream, the capabilities supporting the stages in that value stream, the value created, and the stakeholders involved" (business managers and architects; designing and deciding; scope Strategy) [6]. TOGAF Phase B; artifacts *Value Stream Map* (diagram), *Value Stream Stages catalog* and *Value Stream/Capability matrix* [1][5]. No C4 model level.
- **Deeper meaning:** the enterprise "in motion" at business-model level, the partner of the A1 capability map ("at rest") [2][6]. One stage can map to many processes and one process can realise several stages [1][6]. After each stage the stakeholder may stop, so exit criteria matter more than arrows [1].
- **Leaves out:** decisions and gateways, roles per step, systems, durations, wait times and exceptions.
- **Definition used here:** a value stream is "an end-to-end collection of activities that create a result for a customer, who may be the ultimate customer or an internal end-user" (BIZBOK) [2]; ArchiMate: "a sequence of activities that create an overall result for a customer, stakeholder, or end user" [6]. The term "value stream map" has two other meanings: the **Lean value-stream map** with process and wait times, which has its own page (A9), and SAFe's operational and development value streams [9]. TOGAF and the Business Architecture Guild state that their value streams are not Lean value streams [1][2]. Never put times on this diagram.
- **Version note:** the TOGAF guide is G178, republished in 2022 as part of TOGAF 10 [4]. The Value Stream element exists in ArchiMate since 3.1 (2019) [8]; this page follows 3.2. ArchiMate 4 (announced April 2026) is not verified against the current spec text.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** executives, business and enterprise architects, portfolio and strategy leads.
- **Scenarios:** scoping a replatforming ("Fulfil Customer Order": Discover Product → Place Order → Settle Payment → Fulfil Order → Deliver Goods); finding the weak enabler by heat-mapping the capabilities under each stage; customer support ("Resolve Customer Query") with chatbot and agents as stakeholders; internal streams ("Onboard Supplier"); input to an A8 roadmap.
- **When not to use:** detailed workflow or SLAs (A5, E2); time, waste or waiting (A9); system structure (C family); exceptions and branches (A5, E family).
- **vs neighbours:**
  - **A1 Capability Map** for "what abilities, how good"; combine through the cross-map.
  - **A9 Lean Value-Stream Map** for where time and waste sit in today's flow.
  - **A5 BPMN Process** for task order, decisions, roles, exceptions.
  - **A6 Journey Map** for the customer's experience; A2 is the enterprise's delivery of value.
  - **A8 Roadmap** for when change happens. A Porter value chain is an economic view, not a stakeholder value stream.
-->
- **Audience:** executives, business and enterprise architects, portfolio and strategy leads.
- **Classic scenarios:**
  1. Scoping a replatforming of an online shop: "Fulfil Customer Order" for the shopper, with Discover Product → Place Order → Settle Payment → Fulfil Order → Deliver Goods (pattern from TOGAF's "Acquire Retail Product" [1]).
  2. Finding the weak enabler: heat-map the capabilities under each stage, e.g. a red "Inventory Management" under Fulfil Order [1][3].
  3. Customer support: "Resolve Customer Query", triggered by the customer, with the support chatbot and agents as participating stakeholders, ending in "Customer issue resolved".
  4. Internal value streams triggered by an employee or partner, such as "Onboard Supplier" for the warehouse (cf. TOGAF "Recruit Employee") [1].
  5. Capability-based planning: stages with heat-mapped capabilities feed an A8 roadmap.
- **When not to use:** for detailed workflow, SLAs or one team's procedure (A5, E2); for time, waste or wait analysis (A9); for system structure (C family); for exceptions and branches (A5, E family).
- **vs neighbours:**
  - Choose **A1 Capability Map** for "what abilities, and how good are they"; combine the two through the cross-map [1][3].
  - Choose **A9 Lean Value-Stream Map** when the question is where time and waste sit in today's operational flow.
  - Choose **A5 BPMN Process** for the order of tasks, decisions, roles or exceptions for a case [6].
  - Choose **A6 Journey Map** for the customer's experience (emotions, touchpoints); A2 is the enterprise's delivery of value, outside-in but not experiential.
  - Choose **A8 Target Architecture and Roadmap** for when change happens; A2 with a capability heat map feeds it.
  - A Porter value chain is an economic view of primary and support activities, not a stakeholder value stream [1][2].

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** ArchiMate notation is formal (chevron-shaped Value Stream element, *flow* between stages, capabilities *serve* stages) [6][7]. BIZBOK and TOGAF renderings are chevrons plus a stage table with capabilities stacked under each stage: standard content, conventional graphics [1][2].
- **Required header:** value stream **name** in verb-noun, active tense, as the initiating stakeholder would say it ("Fulfil Customer Order") [1][6]; short **description**; **triggering stakeholder** ("there must be a clearly defined triggering stakeholder") [1]; **value proposition** in stakeholder terms [1][2].
- **Required per stage** (TOGAF's six elements [1]): name of two to three words; description; participating stakeholders; entrance criteria (the condition or state change that triggers the stage); exit criteria (which become the next stage's entrance criteria); value item (the incremental value created).
- **Stage count:** about 4–8; keep it concise and do not go down to operational detail [1].
- **Arrows:** abutting chevrons left to right, or ArchiMate *flow* between stages [6]. They mean value hand-over, not control flow. No gateways or branches.
- **Optional capability cross-map:** capabilities stacked under each stage; in ArchiMate they *serve* the stage, using grouping for compactness [6][8]. Heat-map the capabilities, never the stages [1][3].
- **Optional outcome:** the value stream *realizes* an Outcome; a flow from the last stage to the outcome is a metamodel error [10].
- **Optional stage table** under the row (entrance, exit, value item, stakeholders), which keeps the chevrons short.
- **Legend:** needed whenever capabilities carry heat colours (criterion, scale, source).

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Start with external, customer-triggered value streams** before internal ones [1].
2. **Name the stakeholder and the value first,** then the stages [1][2].
3. **Write entrance and exit criteria as observable state changes** ("Order placed", "Payment authorised") and chain each exit to the next entrance [1].
4. **Cross-map capabilities, then heat-map them** to find where to invest [1][3].
5. **Draft value streams and capabilities together;** TOGAF: "one should not exist without the other for very long" [1].

### Anti-patterns
1. **Lean times on business stages** (process time, wait, lead time). That is a different diagram (A9); TOGAF says Lean VSM is unsuited to capability cross-mapping [1].
2. **Too many or task-level stages** (check, approve, send email), which turn the stream into a process [1][6].
3. **Org units as stages** ("Finance step") or no triggering stakeholder [1][2].
4. **Branches or gateways inside the value stream;** model the stop opportunity through exit criteria instead [1].
5. **Flow from the last stage to the outcome** in ArchiMate (use *realizes*) [10]; also long return lines, unexplained icons and working notes on the figure.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [TOGAF Series Guide: Value Streams (G178, mirror PDF)](https://governance.foundation/assets/frameworks/togaf/g178_2%20-%20Value%20Streams.pdf) — "Acquire Retail Product" and "Recruit Employee" with full stage tables and capability cross-maps; Appendix A compares value chain, value network and Lean VSM. © The Open Group; read only.
- [Business Architecture Guild reference-model workshop deck](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf) — anatomy of a value stream ("Settle Claim" → "Claimant Made Whole"), external vs internal triggers, a stage template. © Business Architecture Guild.
- [The Open Group blog: ArchiMate 3.1, the new version of the standard](https://blog.opengroup.org/2019/11/05/archimate-3-1-specification-the-new-version-of-the-standard) — an ArchiMate value-stream cross-map with stages, value flows and grouped capabilities realising an outcome. © The Open Group.
- [SAFe: Operational Value Streams](https://framework.scaledagile.com/operational-value-streams) — the agile sense of the term, useful to recognise and disambiguate. © Scaled Agile.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Confirm the type: stakeholders, value or capabilities → this page; time, waste or waiting → A9. If unclear, ask.
2. Header: verb-noun name, triggering stakeholder, value proposition. The title carries the message, e.g. "Fulfil Customer Order: shopper receives paid goods in five stages".
3. Draft 4–8 stages as a table (name, entrance, exit, value item, participants); check each exit equals the next entrance.
4. Layout: one row of equal chevrons left to right; stakeholder at the left end, value proposition at the right end; 2–3 words per chevron, no bullets.
5. Cross-map (optional): one column per stage with 2–6 capability tiles beneath, using A1 names; a capability used by several stages is repeated with identical style.
6. Colour: neutral stages; heat colour only on capability tiles, with a legend (criterion, scale, source).
7. Put entrance/exit/value items in a compact table under the row or in the text, not inside chevrons.

**Self-check**
- [ ] No times, durations or waits anywhere on the figure.
- [ ] Triggering stakeholder and value proposition are shown; the name is verb-noun.
- [ ] 4–8 stages with 2–3-word names; no org units, tasks or gateways.
- [ ] Exit criteria chain into the next stage's entrance criteria.
- [ ] Capability tiles use A1 names; heat colours have a legend.
- [ ] Strictly left to right, no return lines; no working notes on the figure.
- [ ] The title or legend states current or target state.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Limited but useful:** domain state enums and status transitions (`OrderStatus: placed → paid → picked → shipped → delivered`) suggest entrance and exit criteria; analytics funnel events and route sequences (catalogue → cart → checkout) suggest customer-facing stages; README and product docs.
- **Capability cross-map:** domain folders and services can suggest candidate capabilities (see A1).
- **Must come from people:** the triggering stakeholder, the value proposition, the value items, which stages matter and all heat-map scores. Mark code-derived stages as candidates.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Is the question stakeholder value and enabling capabilities, or time and waste in a flow? (value and capabilities; otherwise switch to A9)
2. Who triggers the value stream, and what does "done" mean for them? (the shopper; "receives the right goods, paid securely")
3. Current state, target state, or both? (current)
4. Cross-map capabilities, and against which capability list? (yes, against the A1 map if one exists)
5. Heat-map the capabilities, and by which single criterion? (no heat map unless a decision needs it)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A2.json` · Layout template: `tree` · stages are `task` nodes chained by edges in one left-to-right row; capabilities cross-mapped to a stage are listed in its `tags`.

## Sources {#sources}
<!-- skill: omit -->
1. TOGAF Series Guide: Value Streams (G178, Oct 2017, updated Jun 2018), The Open Group (mirror PDF), incl. §2.1–3.1 and App. A.3 "Lean Value Stream" — https://governance.foundation/assets/frameworks/togaf/g178_2%20-%20Value%20Streams.pdf — accessed 2026-10-14
2. Business Architecture Guild, "Business Architecture Reference Model Workshop" (2019; BIZBOK value stream definitions, anatomy, templates) — https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf — accessed 2026-10-14
3. TOGAF Series Guide: Business Capabilities (G189, 2018), §4.2.2 Capability/Value Stream Mapping (mirror PDF) — https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf — accessed 2026-10-14
4. The Open Group Publications, TOGAF Series Guide: Value Streams (G178; republished 25 Apr 2022; part of TOGAF 10) — https://publications.opengroup.org/g178 — accessed 2026-10-14
5. The Open Group / OMG BASIG, "Advancement of Business Architecture in the TOGAF Standard" (TOGAF 9.2 Phase B catalogs, matrices, diagrams) — https://www.omg.org/cgi-bin/doc?basig%2F18-09-03.pdf= — accessed 2026-10-14
6. ArchiMate 3.1 Specification (C197, 2019), §7.3.2 Value Stream, App. C.3.3 Value Stream Viewpoint (mirror PDF) — https://university.sk/wp-content/uploads/2020/01/ARCHIMATE_v3_1_specifikacia.pdf — accessed 2026-10-14
7. ArchiMate 3.2 Specification Reference Cards (N221, 2022) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — accessed 2026-10-14
8. "ArchiMate 3.1 Specification: The New Version of the Standard", The Open Group Blog (5 Nov 2019) — https://blog.opengroup.org/2019/11/05/archimate-3-1-specification-the-new-version-of-the-standard — accessed 2026-10-14
9. Scaled Agile, "Operational Value Streams" and "Development Value Streams" — https://framework.scaledagile.com/operational-value-streams ; https://framework.scaledagile.com/development-value-streams — accessed 2026-10-14
10. "The Value Management Platform and ArchiMate", CEUR-WS Vol-2574 (value stream realizes outcome) — https://ceur-ws.org/Vol-2574/paper2.pdf — accessed 2026-10-14

### A9 · Lean value-stream map (VSM) {#variant-a9}

Editorial grouping preserves the distinct notation; use this recipe and its checks.

1. Scope: one family, door-to-door start and end, current or future, date; title carries the finding, e.g. "Order to doorstep: 20 min of work in 33 h".
2. Top band: supplier left, customer right with demand rate; coordination or scheduling in the middle with its information arrows.
3. Middle band: process boxes left to right with a data box beneath each (PT, %C&A, people); queue triangles with counts or wait times between them.
4. Bottom band: timeline ladder (wait above, PT below) with totals at the right: lead time, ΣPT, activity ratio.
5. Future state: a second map with kaizen bursts at the change points, same order and scale so the two compare side by side.
6. Text: short work names in boxes; numbers only in data boxes and the timeline; one time unit per row.
7. Colour: neutral boxes; one accent for waits or kaizen bursts; plain labelled boxes instead of Lean icons for non-Lean readers, always with a legend.

**Self-check**
- [ ] Every process box has a data box with PT; queues and waits are shown between boxes.
- [ ] Totals add up: ΣPT ≤ lead time and activity ratio = ΣPT ÷ lead time.
- [ ] The source of the numbers (observed, sampled, system data) and the period are stated near the figure.
- [ ] Information flow is drawn, not only the work flow.
- [ ] Strictly left to right, no long return lines; boxes are work steps, not departments.
- [ ] No capabilities or stakeholder value stages (those belong in A2).
- [ ] The figure states current or future; a future map has kaizen bursts tied to a plan.
- [ ] Icons and units are explained in a legend.

[Full method and historical sample](/types/a9-lean-value-stream-map#meaning).

## Sample {#sample}
<!-- skill: path only -->
![A2 · Enterprise Service Assistant](/samples/ai-service-assistant/A2/en/diagram.svg)
*Which stages does a stakeholder pass through, from trigger to delivered value, and which capabilities enable each stage?*

[SVG](/samples/ai-service-assistant/A2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

[Historical shop regression sample](/samples/A2-value-stream.svg) · [All 29 views](/use/ai-service-assistant) · [Illustrative assumptions](/use/ai-service-assistant-assumptions).
