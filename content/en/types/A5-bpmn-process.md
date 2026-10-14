---
code: A5
slug: bpmn-process
family: A
names:
  en: Business process diagram (BPMN)
  zh: 业务流程图（BPMN）
  aliases:
    en: [BPMN diagram, BPMN collaboration diagram, BPMN process diagram, process map, swimlane process diagram, process flow diagram]
    zh: [BPMN 流程图, 业务流程建模图, BPMN 协作图, 业务流程图, 协作图]
question: 'How does one instance of a piece of business work run from trigger to outcome: who does each step, where does it branch, and how does it talk to outside parties?'
audiences: [business, product, developers]
levels: [concept, logical]
phases: [requirements, design]
scope: One business process (one kind of instance) at one level of decomposition, with its participants as pools and its performers as lanes.
formal: {kind: standard, ref: 'OMG BPMN 2.0.2 (formal/13-12-09, Jan 2014); ISO/IEC 19510:2013 is identical to BPMN 2.0.1 (same notation)'}
neighbours: [A1, A2, A6, A9, E1, E2, E3, E4]
status: draft
---

# Business Process Diagram, BPMN (业务流程图 / BPMN 泳道图)

> One business process drawn in standard BPMN: one instance flows from a trigger, through tasks and gateways, to named end states, with pools for participants and lanes for performers.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A BPMN process diagram answers "how does one order, request or case flow from its trigger to one of its outcomes, and who does each step?" It serves a behavioural (process) viewpoint in ISO/IEC/IEEE 42010 terms. TOGAF calls it a Process Flow diagram, a Phase B Business Architecture artifact [12]. ArchiMate shows the same process as a single Business Process element, and BPMN details it [13]. The C4 model has no process level. BPMN itself excludes organisation models, functional breakdowns, data models, strategy and business rules, and "is not a data flow language" [2 §7.2].

**Definition used here:** the current version is **BPMN 2.0.2** (OMG, January 2014) [1]. ISO/IEC 19510:2013 is identical to **BPMN 2.0.1**, not 2.0.2; the notation is the same, and 2.0.2 adds clarifications only [3]. A **pool** is a participant (an independent party or process). A **lane** is a partition inside one pool (a role, department or system) [2 §10].

**Deeper meaning:** a BPMN process is defined by its **instance**: one order, request or claim flows from a start event to one of several **end states**. Make the end states explicit, because they are the business outcomes [4][7]. The specification places organisational models and resources, functional breakdowns, data and information models, strategy and business rules **out of scope**, and BPMN is not a data-flow language [2]; use A1, B3, D1, D2 or a rules table for those.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** process owners, analysts, operations, auditors; developers and testers who automate or verify the process. Executives need only a one-page top level of collapsed sub-processes.
- **Scenarios:** as-is / to-be process redesign; online-shop order-to-shipment with the customer and payment provider as external pools; automation scoping (user task vs service task); deriving acceptance tests (one path from start to an end state = one test).
- **When not to use:** the reader needs *what* the business does (A1, A2); the question is the customer's experience (A6); the flow is mostly system-to-system calls (E4, E1); the work is unstructured case work with no fixed order (a state view, E3, usually communicates it better); or the process is trivial and the readers have never seen BPMN.
- **vs neighbours:**
  - Choose **A2 value stream** when the question is which value stages exist, without control flow or roles.
  - Choose **A6 journey map** for the customer's experience; A5 is the organisation's logic behind it.
  - Choose **E4 swimlane flow** when lanes are systems and readers are engineers. A5 has formal semantics (pools, message flows); E4 is an informal convention.
  - Choose **E1 sequence** for exact message order between software parts, **E3 state machine** for the lifecycle of one object.
  - Choose **E2 activity diagram / flowchart** (ISO 5807 symbols [14]) for one performer and 5–8 steps, or readers new to BPMN.
  - Choose **A9** when the question is where waiting time builds up in a delivery process (Lean value-stream map), not who does which step.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Diagram kinds:** a *Process* diagram (one pool with lanes) or a *Collaboration* diagram (several pools linked by message flows); *Choreography* is rarely used for business readers [2 §7.4].
- **Required:** start event (thin circle) labelled with its trigger; tasks (rounded rectangles, verb + object); exclusive (XOR) and parallel (AND) gateways (diamonds); one end event (thick circle) per distinct end state; one process pool with 2–5 lanes.
- **Optional:** collapsed sub-process ([+] marker), call activity, intermediate events (double circle), data object / data store, text annotation, black-box pools for external parties.
- **Conformance level:** stay within the **Descriptive** sub-class for business readers. Loop and multi-instance markers, inclusive and event-based gateways and most intermediate events belong to the **Analytic** class [2 §2, Tables 2.1–2.2][4].
- **Sequence flow** (solid line, solid arrowhead) orders steps inside one pool; it may cross lanes but never a pool boundary [2 §7.2.1].
- **Message flow** (dashed line, open circle at the start, open arrowhead) **only connects two different pools** and must not connect objects in the same pool [2 §9.4].
- **Association** (dotted) links annotations and data to flow objects. Line styles of the three connectors must not be altered [2 §7.5].
- **Size:** at most about 10 activities per process level [5]; decompose models above 50 elements [10]. For slides, 5–9 activities per page is a readability heuristic, not part of BPMN.
- **Naming** [5][6][7]: activities verb + object ("Pick items"); message start "Receive order"; end events as end-state phrases ("Order shipped"); XOR gateway as a question ("Payment authorised?") with Yes/No gates; AND gateways unlabelled; message flows as nouns ("Payment request"); lanes as roles, never people.
- **Legend:** BPMN readers need none; business readers get a 4–6 item legend of the glyphs actually used.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices

1. One interpretation from the printed page alone: explicit start and end events at every level, every node on a continuous path from start to end [4][5][7].
2. Left to right, happy path straight through the middle, splits and joins paired symmetrically, crossings removed by reordering lanes and pools [7].
3. One process pool with internal roles as lanes; external parties as black-box pools reached only by message flows [5][9].
4. A one-page top level of collapsed sub-processes, then one child page per sub-process [4][5].
5. Default shape sizes and minimal colour: at most one faint highlight, for example the happy path or the steps that change in a to-be [7].

### Anti-patterns

1. Sequence flow drawn between pools, or message flow between lanes of the same pool; both violate the specification [2 §9.4].
2. One pool per department inside a single process, which breaks the instance and turns internal hand-offs into message flows [5].
3. Unlabelled end events and gateways: the model validates but tells the reader nothing [6].
4. Specialist glyphs shown to business readers without need; for example a message-start envelope read as "e-mail". Use a plain start circle plus a label unless the type changes the meaning [4].
5. Exceptions drawn into the main path until the happy path disappears; put them on boundary events or in a separate figure. Also avoid flowchart habits such as untyped diamonds and data flows drawn as sequence flows [2 §7.2].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [OMG, BPMN 2.0 by Example (dtc/10-06-02)](https://www.omg.org/spec/BPMN/2.0/About-BPMN) — official non-normative worked examples of Process, Collaboration and Choreography diagrams [15]. OMG copyright.
- [Camunda, BPMN 2.0 Symbols reference](https://camunda.com/en/bpmn/reference) — each symbol in a small realistic model; free to view, check terms before reuse [8].
- [Camunda, Creating readable process models](https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models) — before/after layouts for symmetry, happy path and labels [7].
- [Trisotech / Bruce Silver, BPMN Style Rules](https://www.trisotech.com/bpmn-style-rules) — one model before and after the style rules, with each label rule illustrated [5].
- [BPMN 2.0 Poster (Berliner BPM-Offensive)](https://bpm-conference.org/BPMNPoster) — one-page symbol overview, free download in many languages; a good model for a reader legend [11].

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix the frame: process name, trigger, what one instance is, 2–4 end states, as-is or to-be, business or technical audience.
2. Pick the kind: Process (one pool with lanes) or Collaboration (add black-box pools for external parties). For a single performer and non-BPMN readers, propose a plain flowchart; if the actors are mostly systems, propose E4.
3. List 5–9 top-level activities (verb + object) of the same instance; group anything beyond 10 into collapsed sub-processes with child pages.
4. Lanes: 2–5 roles or departments, never people; the lane with the first activity on top, the rest ordered to minimise crossings.
5. Layout left to right: happy path on one line in the main lane; branches above or below; joins symmetric to splits; external pools above or below, ordered by first contact, so message flows stay short and vertical.
6. Gateways: XOR as a question with Yes/No or end-state gates; AND unlabelled; every split joined unless each branch ends in its own end event.
7. Events and messages: start labelled with its trigger; one end event per end state; message flows only between pools, each a noun.
8. Text: about 5 words per label, no sentences in shapes, at most 2 annotations; the title carries the message and as-is / to-be.
9. Colour: black on white, one faint highlight at most, one neutral tint for black-box pools; the legend lists only glyphs used.

**Self-check**
- [ ] Every sequence flow stays inside one pool; every message flow joins two different pools.
- [ ] Every path runs from a labelled start event to a labelled end event.
- [ ] End states are distinct; XOR gateways are labelled, AND gateways are not.
- [ ] Activities are verb + object at one granularity, about 10 or fewer per page.
- [ ] Lanes are roles, departments or systems of one kind; no person names.
- [ ] No altered line styles and no home-made shapes.
- [ ] Every specialist glyph is needed and in the legend, or replaced by a plain symbol plus label.
- [ ] Flows read left to right with no long fold-back lines.
- [ ] The title states the process and as-is / to-be; no TBD or status notes on the figure.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Strong:** executable BPMN files (`*.bpmn`, `*.bpmn20.xml`); workflow or orchestration definitions (step functions, durable workflows, DAGs, saga orchestrators); state enums with transition tables. Simplify them for business readers.
- **Medium:** status enums (candidate end states), roles and permissions (candidate lanes), queues, topics and webhooks (message flows to external pools), scheduled jobs (timer starts), approval and notification code, BDD feature files (paths).
- **Weak:** README, `docs/`, ADRs.
- **Ask people:** manual work outside systems, who really performs each step, human exception handling, as-is workarounds and the to-be intent. Keep code-derived vs interview-derived steps in notes, not on the figure.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which process, what is one instance, and what are its possible outcomes? (main success outcome plus one rejection)
2. Current process (as-is) or target (to-be)? (to-be when designing a change)
3. Who reads it: business readers new to BPMN, or analysts and developers? (Descriptive BPMN shapes plus a small legend)
4. Which roles do the work, and which outside parties appear as separate pools? (one pool with lanes; external parties as black-box pools)
5. Happy path only, or main exceptions too? (happy path plus at most one key branch; errors in a separate figure)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A5.json` · Layout template: `lanes` · groups of kind `pool` and `lane` become bands; `task`, `event` and `gateway` nodes are placed left to right per lane; `message` edges are routed only between pools.

## Sources {#sources}
<!-- skill: omit -->
1. OMG, About the BPMN Specification Version 2.0.2 — https://www.omg.org/spec/BPMN/2.0.2/About-BPMN — accessed 2026-10-14
2. OMG, Business Process Model and Notation (BPMN) v2.0.2, formal/13-12-09 (§2 Conformance, §7.2, §7.4, §7.5, §9.4, §10) — https://www.omg.org/spec/BPMN/2.0.2/PDF — accessed 2026-10-14
3. ISO, ISO/IEC 19510:2013 Object Management Group Business Process Model and Notation — https://www.iso.org/standard/62652.html — accessed 2026-10-14
4. Bruce Silver, *BPMN Method and Style*, 2nd ed., 2011 — https://www.methodandstyle.com/books/bpmn-method-and-style — accessed 2026-10-14
5. Bruce Silver / Trisotech, BPMN Style Rules — https://www.trisotech.com/bpmn-style-rules — accessed 2026-10-14
6. Bruce Silver, Standardizing BPMN Labels — https://www.methodandstyle.com/blog/standardizing-bpmn-labels — accessed 2026-10-14
7. Camunda Docs, Creating readable process models — https://docs.camunda.io/docs/components/best-practices/modeling/creating-readable-process-models — accessed 2026-10-14
8. Camunda, BPMN 2.0 Symbols reference — https://camunda.com/en/bpmn/reference — accessed 2026-10-14
9. Camunda, BPMN 2.0 Examples — https://camunda.com/bpmn/examples/ — accessed 2026-10-14
10. Mendling, Reijers, van der Aalst, Seven Process Modeling Guidelines (7PMG), *Information and Software Technology* 52(2), 2010 — https://www.semanticscholar.org/paper/Seven-process-modeling-guidelines-(7PMG)-Mendling-Reijers/5c4a08a28b46fec62a0b45a26647330a0e69feb8 — accessed 2026-10-14
11. BPM Conference, BPMN 2.0 Poster (Berliner BPM-Offensive) — https://bpm-conference.org/BPMNPoster — accessed 2026-10-14
12. The Open Group, TOGAF 9.1 Sample Catalogs, Matrices and Diagrams (Process Flow diagram) — http://www.togaf.info/togafSlides91/TOGAF-V91-Sample-Catalogs-Matrics-Diagrams-v3.pdf — accessed 2026-10-14
13. The Open Group, ArchiMate 3.2 Specification Reference Cards — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — accessed 2026-10-14
14. ISO, ISO 5807:1985 Documentation symbols and conventions for data, program and system flowcharts — https://www.iso.org/standard/11955.html — accessed 2026-10-14
15. OMG, About BPMN 2.0 (informative documents, incl. BPMN 2.0 by Example) — https://www.omg.org/spec/BPMN/2.0/About-BPMN — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![A5 sample: BPMN collaboration for handling a return, with the customer as a black-box pool](/samples/A5-bpmn-process.svg)
*Handling a return as a BPMN collaboration: the online shop pool with support and warehouse lanes, and the customer as a black-box pool. Solid arrows are sequence flows inside the shop pool; dashed arrows with an open circle are message flows to and from the customer (return request, return label, parcel). The decision “Eligible?” leads to the end events “Refund issued” and “Return declined”. This renderer draws start and end events with the same circle.*
