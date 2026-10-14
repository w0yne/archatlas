# Value Stream (Business Architecture) (价值流（业务架构）)
<!-- Generated from content/en/types/A2-value-stream.md by tools/build_skill_refs.py. Do not edit. -->
> How does value accrue, stage by stage, for a triggering stakeholder, and which capabilities enable each stage?
Scope: One value stream: a triggering stakeholder, a value proposition and about 4–8 stages, optionally with capabilities cross-mapped under each stage Neighbours: A1, A5, A6, A9.

## Meaning
- **Question:** how does the enterprise deliver value to one stakeholder, stage by stage, and which capabilities enable each stage? Value is "always defined from the perspective of the stakeholder".
- **Viewpoint:** ArchiMate *Value Stream viewpoint*: "a structured overview of a value stream, the capabilities supporting the stages in that value stream, the value created, and the stakeholders involved" (business managers and architects; designing and deciding; scope Strategy). TOGAF Phase B; artifacts *Value Stream Map* (diagram), *Value Stream Stages catalog* and *Value Stream/Capability matrix*. No C4 model level.
- **Deeper meaning:** the enterprise "in motion" at business-model level, the partner of the A1 capability map ("at rest"). One stage can map to many processes and one process can realise several stages. After each stage the stakeholder may stop, so exit criteria matter more than arrows.
- **Leaves out:** decisions and gateways, roles per step, systems, durations, wait times and exceptions.
- **Definition used here:** a value stream is "an end-to-end collection of activities that create a result for a customer, who may be the ultimate customer or an internal end-user" (BIZBOK); ArchiMate: "a sequence of activities that create an overall result for a customer, stakeholder, or end user". The term "value stream map" has two other meanings: the **Lean value-stream map** with process and wait times, which has its own page (A9), and SAFe's operational and development value streams. TOGAF and the Business Architecture Guild state that their value streams are not Lean value streams. Never put times on this diagram.
- **Version note:** the TOGAF guide is G178, republished in 2022 as part of TOGAF 10. The Value Stream element exists in ArchiMate since 3.1 (2019); this page follows 3.2. ArchiMate 4 (announced April 2026) is not verified against the current spec text.

## When to use and how to choose
- **Audience:** executives, business and enterprise architects, portfolio and strategy leads.
- **Scenarios:** scoping a replatforming ("Fulfil Customer Order": Discover Product → Place Order → Settle Payment → Fulfil Order → Deliver Goods); finding the weak enabler by heat-mapping the capabilities under each stage; customer support ("Resolve Customer Query") with chatbot and agents as stakeholders; internal streams ("Onboard Supplier"); input to an A8 roadmap.
- **When not to use:** detailed workflow or SLAs (A5, E2); time, waste or waiting (A9); system structure (C family); exceptions and branches (A5, E family).
- **vs neighbours:**
  - **A1 Capability Map** for "what abilities, how good"; combine through the cross-map.
  - **A9 Lean Value-Stream Map** for where time and waste sit in today's flow.
  - **A5 BPMN Process** for task order, decisions, roles, exceptions.
  - **A6 Journey Map** for the customer's experience; A2 is the enterprise's delivery of value.
  - **A8 Roadmap** for when change happens. A Porter value chain is an economic view, not a stakeholder value stream.

## Notation and elements
- **Formal or informal:** ArchiMate notation is formal (chevron-shaped Value Stream element, *flow* between stages, capabilities *serve* stages). BIZBOK and TOGAF renderings are chevrons plus a stage table with capabilities stacked under each stage: standard content, conventional graphics.
- **Required header:** value stream **name** in verb-noun, active tense, as the initiating stakeholder would say it ("Fulfil Customer Order"); short **description**; **triggering stakeholder** ("there must be a clearly defined triggering stakeholder"); **value proposition** in stakeholder terms.
- **Required per stage** (TOGAF's six elements): name of two to three words; description; participating stakeholders; entrance criteria (the condition or state change that triggers the stage); exit criteria (which become the next stage's entrance criteria); value item (the incremental value created).
- **Stage count:** about 4–8; keep it concise and do not go down to operational detail.
- **Arrows:** abutting chevrons left to right, or ArchiMate *flow* between stages. They mean value hand-over, not control flow. No gateways or branches.
- **Optional capability cross-map:** capabilities stacked under each stage; in ArchiMate they *serve* the stage, using grouping for compactness. Heat-map the capabilities, never the stages.
- **Optional outcome:** the value stream *realizes* an Outcome; a flow from the last stage to the outcome is a metamodel error.
- **Optional stage table** under the row (entrance, exit, value item, stakeholders), which keeps the chevrons short.
- **Legend:** needed whenever capabilities carry heat colours (criterion, scale, source).

## Best practices and anti-patterns
### Best practices
1. **Start with external, customer-triggered value streams** before internal ones.
2. **Name the stakeholder and the value first,** then the stages.
3. **Write entrance and exit criteria as observable state changes** ("Order placed", "Payment authorised") and chain each exit to the next entrance.
4. **Cross-map capabilities, then heat-map them** to find where to invest.
5. **Draft value streams and capabilities together;** TOGAF: "one should not exist without the other for very long".

### Anti-patterns
1. **Lean times on business stages** (process time, wait, lead time). That is a different diagram (A9); TOGAF says Lean VSM is unsuited to capability cross-mapping.
2. **Too many or task-level stages** (check, approve, send email), which turn the stream into a process.
3. **Org units as stages** ("Finance step") or no triggering stakeholder.
4. **Branches or gateways inside the value stream;** model the stop opportunity through exit criteria instead.
5. **Flow from the last stage to the outcome** in ArchiMate (use *realizes*); also long return lines, unexplained icons and working notes on the figure.

## Drawing recipe
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

## Evidence in a code repository
- **Limited but useful:** domain state enums and status transitions (`OrderStatus: placed → paid → picked → shipped → delivered`) suggest entrance and exit criteria; analytics funnel events and route sequences (catalogue → cart → checkout) suggest customer-facing stages; README and product docs.
- **Capability cross-map:** domain folders and services can suggest candidate capabilities (see A1).
- **Must come from people:** the triggering stakeholder, the value proposition, the value items, which stages matter and all heat-map scores. Mark code-derived stages as candidates.

## Guided-mode questions
1. Is the question stakeholder value and enabling capabilities, or time and waste in a flow? (value and capabilities; otherwise switch to A9)
2. Who triggers the value stream, and what does "done" mean for them? (the shopper; "receives the right goods, paid securely")
3. Current state, target state, or both? (current)
4. Cross-map capabilities, and against which capability list? (yes, against the A1 map if one exists)
5. Heat-map the capabilities, and by which single criterion? (no heat map unless a decision needs it)

## Template
Model template: `assets/templates/A2.json` · Layout template: `tree` · stages are `task` nodes chained by edges in one left-to-right row; capabilities cross-mapped to a stage are listed in its `tags`.

## Sample
Figure: `samples/A2-value-stream.svg` (published with the site)
