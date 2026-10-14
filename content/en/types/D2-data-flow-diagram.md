---
code: D2
slug: data-flow-diagram
family: D
names:
  en: Data Flow Diagram
  zh: 数据流图
  aliases:
    en: [DFD, data flow model, process model (structured analysis), bubble chart, context diagram (top level), threat-model DFD]
    zh: [数据流程图, 数据流向图, 上下文图, 0 层图]
question: "Where does data come from, which processing transforms it, where is it kept, and where does it go?"
audiences: [architects, systems and business analysts, security reviewers, privacy and audit staff]
level: logical
phases: [discovery, design, review]
scope: "One system, one level per diagram: a context diagram, or one decomposition of a single process (3-9 processes)"
formal:
  kind: method
  ref: "Structured Analysis: DeMarco 1978 (Yourdon/DeMarco symbols) and Gane & Sarson 1979; no ISO or OMG standard. Threat-model dialect adds trust boundaries"
neighbours: [C2, D1, D3, E2, F2]
status: draft
---

# Data Flow Diagram (数据流图)

> A picture of what data enters a system, which processes transform it, where it rests and where it leaves, with no control flow and no technology.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** where does data come from, what transforms it, where is it stored, where does it go?
- **Viewpoint:** a functional, information-flow view. It models the system as transformations of data and ignores order, timing, conditions and technology. That is why it is the usual base for threat modelling: attacks follow data and cross trust boundaries [6][7]. ArchiMate expresses the same idea with the *flow* relationship between behaviour elements and *access* to data objects [9].
- **Origin:** Structured Analysis, late 1970s: Tom DeMarco (1978) [1][2], Yourdon and Constantine, and Chris Gane and Trish Sarson (1979) [3]. There is no international standard; DFD is a method convention with well-known rules.
- **Definition used here:** a *context diagram* shows the system as one process. Many texts call it "level 0" [5][10]; others call the first decomposition "diagram 0". State the convention you use.
- **Leaves out:** control flow and decisions (E1, E2), responsibility (E4, A5), data structure (D1), deployment (G1), lineage over time and ownership (D3).

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** architects, analysts, security reviewers, privacy and audit staff.
- **Scenarios:** how the order service takes an order, checks stock and payment and stores the result (logical, technology-free); threat-modelling workshop with trust boundaries (internet, edge, internal, payment provider); privacy mapping of personal data; integration analysis of what crosses between orders, payment and shipping.
- **When not to use:** order of calls or retries (E1); branching logic (E2); hand-offs between teams (E4, A5); runtime infrastructure (G1).
- **vs neighbours:**
  - **C2 System Context** when people and systems matter; a level-0 DFD when the data items matter.
  - **D3 Lineage** for concrete datasets across jobs and runs; a DFD is a design-time model.
  - **F2 Threat Model** for the security workflow; it uses this dialect plus threat annotations.
  - **E2 Activity Flowchart** for control flow; a DFD arrow is data, never "then".
-->
- **Audience:** architects, analysts, security reviewers, privacy and audit staff.
- **Classic scenarios:**
  1. Analysing how the shop's order service takes an order, checks stock and payment, and stores the result (logical, technology-free).
  2. A threat-modelling workshop: a level 1 DFD with trust boundaries between internet, edge, internal network and a payment provider [6][7].
  3. Privacy mapping: where customer personal data enters, where it is stored and who receives it.
  4. Integration analysis: which data items cross between orders, payment and warehouse shipping.
- **When not to use:** order of calls or retries (E1); branching logic (E2); hand-offs between teams (E4, A5); runtime infrastructure (G1).
- **vs neighbours:**
  - Choose **C2 System Context** when the people and systems matter; choose a level-0 DFD when the data items matter.
  - Choose **D3 Lineage** to trace concrete datasets across jobs and runs; a DFD is a design-time logical model.
  - Choose **F2 Threat Model** for the security workflow; it uses this page's dialect (DFD plus trust boundaries) and adds threat annotations.
  - Choose **E2 Activity Flowchart** for control flow. A DFD arrow is data, never "then".

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
<!-- skill-text
- **Convention, not standard:** choose one symbol set and keep it. Yourdon/DeMarco: circle = process, two parallel lines = store, rectangle = external entity. Gane & Sarson: rounded rectangle with id = process, open-ended rectangle with id (D1) = store, square = external entity.
- **Required elements:** *external entity* (source or sink outside scope); *process* (verb plus object, "Validate order", numbered 1, 2, 2.1); *data store* (plural noun with id, "Orders", D1); *data flow* (arrow labelled with the data item, a noun such as "order form", never an action).
- **Threat-model additions:** a trust boundary (dashed line or box) wherever privilege or ownership changes; optionally protocol and authentication on boundary-crossing flows.
- **Validity rules:**
  - Balancing: a child diagram's external inputs and outputs equal its parent process's flows.
  - Every process has at least one input and one output (no black hole, no miracle).
  - No flow store-to-store, entity-to-entity or entity-to-store; a process sits between them.
  - Flows are one-way; draw two arrows for request data and response data.
- **Legend:** symbol set, level convention, how trust boundaries look. Do not mix symbol sets.
- **Size:** 5–9 processes per diagram (practitioner rule of thumb); decompose instead of crowding.
-->
- **Formal or informal:** a method convention; choose one symbol set and keep it [4][5].
  - **Yourdon/DeMarco:** circle (bubble) = process; two parallel lines = data store; rectangle = external entity.
  - **Gane & Sarson:** rounded rectangle = process (with id); open-ended rectangle = data store (with id such as D1); square = external entity.
- **Required, four element kinds [4][5][10]:**
  - **External entity:** a source or sink outside scope.
  - **Process:** transforms data; verb plus object ("Validate order"), numbered 1, 2, 2.1.
  - **Data store:** data at rest; plural noun with id ("Orders", D1).
  - **Data flow:** an arrow labelled with the *data item* (a noun: "order form", "payment confirmation"), never an action.
- **Threat-model additions:** a **trust boundary** (dashed line or box) wherever privilege or ownership changes; optionally protocol and authentication on boundary-crossing flows [6][7][8].
- **Validity rules [10]:**
  - Balancing: a child diagram's external inputs and outputs equal its parent process's flows.
  - Every process has at least one input and one output (no "black hole" with only inputs, no "miracle" with only outputs).
  - No flow store-to-store, entity-to-entity or entity-to-store; a process sits between them.
  - Flows are one-way; draw two arrows for request data and response data.
- **Legend:** symbol set, level convention and how trust boundaries look. Do not mix symbol sets.
- **Size:** 5-9 processes per diagram is a practitioner rule of thumb; decompose instead of crowding.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Start with the context diagram,** agree scope and external entities, then decompose one level at a time.
2. **Name flows with data nouns and processes with verb-object;** number processes for traceability to requirements or threats.
3. **Keep 5-9 processes per diagram;** decompose rather than crowd.
4. **Draw trust boundaries for security reviews** and keep the DFD next to the system so it is updated with it; diagram-as-code tools such as pytm exist for that [7][12].
5. **For privacy reviews** tag flows that carry personal or sensitive data, with the tag explained in the legend.

### Anti-patterns
1. **Control flow as data flow:** arrows labelled "then", "on success", "calls".
2. **Missing processes:** a store wired directly to another store or to an external entity.
3. **Black holes and miracles:** processes with no output or no input.
4. **Unbalanced levels:** a child diagram introduces flows its parent lacks.
5. **Technology names** (a message broker, an object store) on a logical DFD, or one giant diagram with 30 processes instead of levels. Name technology only on a diagram labelled "physical DFD".

## Exemplars {#exemplars}
<!-- skill: omit -->
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — explains why DFDs are the most common system model for threat modelling and which elements (including trust boundaries) to show; CC licence on the OWASP site.
- [Microsoft Learn: create a threat model using data-flow diagram elements](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/) — a free module defining each element and the trust-boundary semantics.
- [Lucidchart: data flow diagram symbols](https://www.lucidchart.com/pages/data-flow-diagram/data-flow-diagram-symbols) — shows the symbol sets side by side; good for a legend. Vendor content.
- [University of Cape Town notes, chapter 6](https://www.cs.uct.ac.za/mit_notes/software/pdfs/Chp06.pdf) — rigorous teaching material on context diagrams, levelling and balancing (checked for balancing and "level 0" wording).
- [Visual Paradigm: what is a data flow diagram](https://www.visual-paradigm.com/guide/data-flow-diagram/what-is-data-flow-diagram/) — worked levels from context to level 2 with naming rules. Vendor content.
- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) — an open-source tool that draws threat-model DFDs and lists threats per element.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Decide the purpose: analysis (logical, technology-free), security review (add trust boundaries) or privacy (tag personal-data flows). Declare the symbol set and the level convention.
2. Draw the context diagram first: one process (the system), external entities left and right, flows labelled with nouns.
3. Level 1: 3-9 numbered processes; inputs on the left, outputs on the right, stores in a middle or lower row; stores are reached only through processes.
4. Layout: left to right, external entities at the edges; trust boundaries as dashed rectangles around zones (internet, edge, internal, partner).
5. Text: process = verb + object, 4 words at most; flow = data noun, 3 words at most; store = plural noun plus id.
6. Colour: neutral elements; one accent for boundary-crossing or sensitive flows, explained in the legend.
7. Check balance against the parent before rendering; fix any mismatch first.
8. Keep requirement or threat references as numbered notes outside the diagram.

**Self-check**
- [ ] Only four element kinds, plus trust boundaries on a security DFD.
- [ ] Every arrow carries a data noun; none says "then", "calls" or "next".
- [ ] No store-to-store, entity-to-entity or entity-to-store flows.
- [ ] Every process has both an input and an output.
- [ ] The child diagram balances with its parent process.
- [ ] Levels are numbered and the level convention is stated.
- [ ] One symbol set, with a legend.
- [ ] At most 9 processes per diagram.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **External entities:** inbound routes and handlers, webhook receivers, message consumers; outbound SDK clients and base-URL settings show where data goes.
- **Stores:** database and ORM models, object-store buckets, caches.
- **Data items on flows:** request and response schemas (OpenAPI, DTOs), event payload schemas.
- **Trust boundaries:** network and infrastructure-as-code (subnets, security groups, ingress), authentication middleware, tenancy checks.
- Code shows *calls*: convert them into data movements and drop calls that move nothing meaningful.
- **Must come from people:** which data is sensitive in business terms, and the intended logical decomposition.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. What is this DFD for: analysis, a threat-modelling session or a privacy review? (analysis)
2. What is the system boundary, and who are the external entities? (the order service; customer, payment provider, warehouse)
3. Logical (technology-free) or physical (named stores and services)? (logical)
4. Which level: context only, level 1, or one process in depth? (context plus level 1)
5. Which symbol set, and which data should be flagged as sensitive? (Gane & Sarson; personal data and payment data)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/D2.json` · Layout template: `nested` · external entities are `external` nodes, processes are `component` nodes, stores are `store` nodes (the store id such as D1 in `sub`), trust boundaries are `boundary` groups around zones, data flows are `data` edges whose `label` is the data noun and whose `dir` is `->`.

## Sources {#sources}
<!-- skill: omit -->
1. T. DeMarco, *Structured Analysis and System Specification* (Google Books record) — https://books.google.com/books/about/Structured_Analysis_and_System_Specifica.html?id=7o0-AAAAIAAJ — accessed 2026-10-14
2. Wikipedia, "Structured analysis" (secondary source) — https://en.wikipedia.org/wiki/Structured_analysis — accessed 2026-10-14
3. C. Gane, T. Sarson, *Structured Systems Analysis: Tools and Techniques*, 1979 (ACM DL record) — https://dl.acm.org/doi/10.5555/578524 — accessed 2026-10-14
4. Lucidchart, "Data Flow Diagram Symbols" — https://www.lucidchart.com/pages/data-flow-diagram/data-flow-diagram-symbols — accessed 2026-10-14
5. Visual Paradigm, "What is Data Flow Diagram?" — https://www.visual-paradigm.com/guide/data-flow-diagram/what-is-data-flow-diagram/ — accessed 2026-10-14
6. Microsoft Learn, "Create a Threat Model Using Data-Flow Diagram Elements" (trust boundary element confirmed) — https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/ — accessed 2026-10-14
7. OWASP Cheat Sheet Series, "Threat Modeling" (DFDs, trust boundaries, store models with the system; the page does not name specific tools) — https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html — accessed 2026-10-14
8. OWASP, "Threat Modeling Process" (DFDs highlight privilege or trust boundaries) — https://owasp.org/www-community/Threat_Modeling_Process — accessed 2026-10-14
9. The Open Group, ArchiMate 3.2 Reference Cards (flow, triggering) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — accessed 2026-10-14
10. University of Cape Town, "Chapter 6. Data-Flow Diagrams" (context diagram "sometimes called a level 0" DFD; balancing section; the terms black hole and miracle are common in the wider literature but not found in this text) — https://www.cs.uct.ac.za/mit_notes/software/pdfs/Chp06.pdf — accessed 2026-10-14
11. OWASP Threat Dragon — https://owasp.org/www-project-threat-dragon/ — accessed 2026-10-14
12. OWASP pytm, "A Pythonic framework for threat modeling" — https://github.com/OWASP/pytm — accessed 2026-10-14
13. Microsoft Threat Modeling Tool overview — https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![D2 sample: online shop level 1 data flow diagram with customer, payment provider and warehouse as external entities, numbered order processes, an Orders store and a trust boundary](/samples/D2-data-flow-diagram.svg)
*Sample pending (generated by the renderer from `examples/`).*
