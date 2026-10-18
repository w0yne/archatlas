# Data Flow Diagram (数据流图)
<!-- Generated from content/en/types/D2-data-flow-diagram.md by tools/build_skill_refs.py. Do not edit. -->
> Where does data come from, which processing transforms it, where is it kept, and where does it go?
Scope: One system, one level per diagram: a context diagram, or one decomposition of a single process (3-9 processes) Neighbours: C2, D1, D3, E2, F2.
Named variants (read their own recipes): F2 — `references/types/F2-threat-model-data-flow.md`.

## Meaning
- **Question:** where does data come from, what transforms it, where is it stored, where does it go?
- **Viewpoint:** a functional, information-flow view. It models the system as transformations of data and ignores order, timing, conditions and technology. That is why it is the usual base for threat modelling: attacks follow data and cross trust boundaries. ArchiMate expresses the same idea with the *flow* relationship between behaviour elements and *access* to data objects.
- **Origin:** Structured Analysis, late 1970s: Tom DeMarco (1978), Yourdon and Constantine, and Chris Gane and Trish Sarson (1979). There is no international standard; DFD is a method convention with well-known rules.
- **Definition used here:** a *context diagram* shows the system as one process. Many texts call it "level 0"; others call the first decomposition "diagram 0". State the convention you use.
- **Leaves out:** control flow and decisions (E1, E2), responsibility (E4, A5), data structure (D1), deployment (G1), lineage over time and ownership (D3).

## When to use and how to choose
- **Audience:** architects, analysts, security reviewers, privacy and audit staff.
- **Scenarios:** how the order service takes an order, checks stock and payment and stores the result (logical, technology-free); threat-modelling workshop with trust boundaries (internet, edge, internal, payment provider); privacy mapping of personal data; integration analysis of what crosses between orders, payment and shipping.
- **When not to use:** order of calls or retries (E1); branching logic (E2); hand-offs between teams (E4, A5); runtime infrastructure (G1).
- **vs neighbours:**
  - **C2 System Context** when people and systems matter; a level-0 DFD when the data items matter.
  - **D3 Lineage** for concrete datasets across jobs and runs; a DFD is a design-time model.
  - **F2 Threat Model** for the security workflow; it uses this dialect plus threat annotations.
  - **E2 Activity Flowchart** for control flow; a DFD arrow is data, never "then".
  - Choose **D1 Entity-relationship diagram** when the question is which business objects exist and how they relate, not how data moves.

## Notation and elements
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

## Best practices and anti-patterns
### Best practices
1. **Start with the context diagram,** agree scope and external entities, then decompose one level at a time.
2. **Name flows with data nouns and processes with verb-object;** number processes for traceability to requirements or threats.
3. **Keep 5-9 processes per diagram;** decompose rather than crowd.
4. **Draw trust boundaries for security reviews** and keep the DFD next to the system so it is updated with it; diagram-as-code tools such as pytm exist for that.
5. **For privacy reviews** tag flows that carry personal or sensitive data, with the tag explained in the legend.

### Anti-patterns
1. **Control flow as data flow:** arrows labelled "then", "on success", "calls".
2. **Missing processes:** a store wired directly to another store or to an external entity.
3. **Black holes and miracles:** processes with no output or no input.
4. **Unbalanced levels:** a child diagram introduces flows its parent lacks.
5. **Technology names** (a message broker, an object store) on a logical DFD, or one giant diagram with 30 processes instead of levels. Name technology only on a diagram labelled "physical DFD".

## Drawing recipe
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

## Evidence in a code repository
- **External entities:** inbound routes and handlers, webhook receivers, message consumers; outbound SDK clients and base-URL settings show where data goes.
- **Stores:** database and ORM models, object-store buckets, caches.
- **Data items on flows:** request and response schemas (OpenAPI, DTOs), event payload schemas.
- **Trust boundaries:** network and infrastructure-as-code (subnets, security groups, ingress), authentication middleware, tenancy checks.
- Code shows *calls*: convert them into data movements and drop calls that move nothing meaningful.
- **Must come from people:** which data is sensitive in business terms, and the intended logical decomposition.

## Guided-mode questions
1. What is this DFD for: analysis, a threat-modelling session or a privacy review? (analysis)
2. What is the system boundary, and who are the external entities? (the order service; customer, payment provider, warehouse)
3. Logical (technology-free) or physical (named stores and services)? (logical)
4. Which level: context only, level 1, or one process in depth? (context plus level 1)
5. Which symbol set, and which data should be flagged as sensitive? (Gane & Sarson; personal data and payment data)

## Template
Model template: `assets/templates/D2.json` · Layout template: `nested` · external entities are `external` nodes, processes are `component` nodes, stores are `store` nodes (the store id such as D1 in `sub`), trust boundaries are `boundary` groups around zones, data flows are `data` edges whose `label` is the data noun and whose `dir` is `->`.

## Sample
Figure: `samples/ai-service-assistant/D2/en/diagram.svg` (published with the site)
