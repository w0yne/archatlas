---
code: C5
slug: logical-architecture
family: C
names:
  en: Logical architecture diagram
  zh: 逻辑架构图
  aliases:
    en: [logical view, logical building-block view, technology-neutral component diagram, functional view, building block view (level 1), logical application architecture]
    zh: [逻辑视图, 逻辑构件视图, 功能视图, 逻辑组件图]
question: Which technology-neutral building blocks must the system have, what is each responsible for, and through which named interfaces do they depend on each other and on external capabilities?
audiences: [architects, product, developers]
levels: [logical]
phases: [design]
scope: One system or one solution, decomposed into responsibility blocks (one level, one page).
formal: {kind: convention, ref: 'none (no graphical standard); closest definitions: Rozanski & Woods Functional viewpoint, arc42 §5 building block view, TOGAF 9.x Logical Application Component'}
neighbours: [A7, B3, C1, C3, C4, C6, C7, C8, G2, I1]
status: draft
---

# Logical Architecture Diagram (逻辑架构图)

> A technology-neutral map of the building blocks a system needs, what each one is responsible for, and the named interfaces between them.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->

A logical architecture diagram answers: *which blocks must exist, what does each own, and how do they depend on each other — whatever products or hosts will later realise them?* Its concerns are allocation of responsibility, traceability from requirements to blocks, change impact, make/buy/reuse decisions and splitting work between teams. Systems-engineering guidance warns that jumping straight from requirements to a physical design is a common mistake, because stakeholders revert to familiar solutions [6][7]. In ISO/IEC/IEEE 42010 terms it is a view under a structural/functional viewpoint [5]; in C4 model terms it sits beside the container level, but without the technology labels the C4 model requires [10].

"Logical" has at least five published meanings: Kruchten's 4+1 logical view (a class-level object model) [1]; TOGAF's *Logical Application Component*, "independent of a particular implementation" [2]; the systems-engineering logical architecture that is later allocated to a physical one [6][8]; the "Logical" viewpoint of IEEE 1016 (not verified against the current standard text) [15]; and the informal "software, not hardware".

**Definition used here:** a technology-neutral decomposition of one system or solution into responsibility-bearing building blocks, with their named interfaces and dependencies, drawn so that more than one physical or deployment design could realise it. This is closest to the Rozanski & Woods Functional viewpoint [3] and the arc42 level-1 building block view [4]. The 4+1 logical view (catalogue I1) is the same intent at a finer, class-level grain.

**Related but different:** "functional architecture" in systems engineering is a *tree of functions* that feeds the logical blocks, not a block diagram [6][8]; the SEI "module view" shows *code units* [9]. Neither is this type.

**Deliberately left out:** products, frameworks and versions; hosts, networks, replicas and zones; runtime processes and concurrency; data schemas; call order of scenarios; class-level detail. Infrastructure appears only when it is functionally significant, such as a message bus that transforms data [3].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** solution architects, developers, tech leads, product owners, reviewers of build/buy options; not executives (A7, C1) or operators (G1).
- **Scenarios:** compare technology options on one logical view; assign each requirement to one block; split team ownership; answer "where does this responsibility live?".
- **When not:** hosts or zones (G1/G2); technology fixed and readers are developers (C3/C4); call order (E1); boxes that only list features (A1 abilities, B3 features).
- **vs neighbours:**
  - **A7** for coarse business blocks; **C3** for runnable units with technology; **C4** inside one container with technology labels.
  - **C6** for protocol, authentication and SLA per interface; **C8** for a dependency rule inside code; **G1** for where things run.
  - **B3** for product features to build and prioritise; **C7** for domain-model boundaries and their relationships.
  - **I1** when the logical view is one of several coordinated views (Kruchten's logical view is class-level).
-->

- **Audience:** solution architects, developers and tech leads, product owners (requirement coverage), reviewers comparing build/buy options. Not for executives (use A7 or C1) or operators (use G1).
- **Classic scenarios:** (1) compare technology or vendor options by mapping each onto one logical view; (2) turn requirements into blocks so each lands on exactly one owner; (3) split work and ownership between teams along block boundaries; (4) answer "what does the system consist of?" after a context diagram has been shown; (5) review a partner proposal for gaps and overlaps.
- **When not to use:** the audience needs hosts, scaling or zones (G1/G2); technology is already fixed and readers are developers (C3/C4); you need call order or error paths (E1); the system is one small process (a short module list is enough [4]); the boxes would only list features (business abilities belong in A1, product features in B3).
- **vs neighbours:**
  - Choose **A7 Conceptual architecture** when the reader wants coarse, business-level blocks without interfaces.
  - Choose **C3 Container diagram** when runnable units, their technology and protocols matter; the C4 model requires a technology per container [10].
  - Choose **C4 Component diagram** when you are inside *one* container and the components carry technology labels; C4 model components are not separately deployable [11]. Decision rule: technology-neutral and system-wide → C5; technology-labelled and per container → C4.
  - Choose **C6 Integration/interface** when protocol, authentication and SLA of each interface matter.
  - Choose **C8 Layered architecture** when the point is an allowed-dependency *rule* inside code; a C5 may be grouped in bands, but states no such rule.
  - Choose **G1 Deployment** when the question is where things run.
  - Choose **B3 Feature tree** when the list is product features to build and prioritise; C5 groups responsibilities and interfaces.
  - Choose **C7 Bounded context map** when the boundaries are domain models with their own language and the relationships between them (upstream/downstream, translation) matter.
  - Choose **I1 4+1 view model** when the logical view is one of several coordinated views; Kruchten's logical view is class-level, finer than C5.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->

- **No standard notation.** Plain boxes are the default. UML component diagrams (suggested for the functional view [3]), ArchiMate Application Components and Interfaces [12], or Capella logical architecture diagrams [8] are optional formal choices. ArchiMate 3.2 (2022) is current; ArchiMate 4 was announced in April 2026 and renames layers to domains [13].
- **ArchiMate caveat:** its Application Component is "aligned to implementation structure" [12], so to stay logical name *types*, not instances, and keep Node and System Software out. TOGAF's *Logical* Application Component is the implementation-independent term [2].
- **Required:** title naming type and scope ("Logical view: online shop") [10]; one system boundary; building blocks with a noun-phrase name and one short responsibility; external capabilities outside the boundary in a distinct style; a label on every dependency naming the operation or information exchanged; a legend for every shape, colour and line style [10][14].
- **Optional:** grouping frames by responsibility cluster; a handful of numbered key interactions; a "planned" marker defined in the legend.
- **Companion table:** block | responsibility | provided interfaces | required interfaces. This is the Rozanski & Woods element template and the arc42 black-box table [3][4].
- **Arrow semantics:** one meaning per diagram. Prefer *depends-on/calls* (consumer → provider) and keep data flow for D2. The label must agree with the arrow direction; avoid a bare "uses" [14].
- **Level of detail:** below "whole system", above "class"; one page; always do level 1 and zoom only where risk justifies it [4].
- **Naming:** blocks are responsibility nouns ("Checkout", "Order Management"), never product names; interfaces are verb–noun ("reserve stock"); externals are role names ("Payment Provider"), not brands.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### Best practices

1. State the definition of "logical" and the scope in the title or caption before drawing [1][6].
2. Give every block one responsibility and justify why the system is cut this way; hide the inner workings of black boxes [4].
3. Derive interfaces from the responsibilities they serve. Connecting blocks by intuition produces missing or useless interfaces [7].
4. Keep the logical model as a stable anchor and allocate it to physical units in a separate step [6][7].
5. Put inbound and outbound interfaces per block in a table beside the figure, and review against the C4 model checklist (title, legend, every line labelled, direction matches label) [3][14].

### Anti-patterns

1. **Technology leakage:** product names inside the boundary turn C5 into a weak C3 and defeat option comparison [6].
2. **Assumed one-to-one deployment:** a logical block may map to one container, part of one or several [11].
3. **Class-diagram granularity:** classes without architectural significance belong to a lower level [11].
4. **Feature lists in boxes, or mixed element kinds** (actors, steps and blocks side by side): structure disappears behind text.
5. **Unlabelled or mixed-meaning arrows**, and status notes ("TBD") on the figure instead of a legend entry [14].

## Exemplars {#exemplars}
<!-- skill: omit -->

- [Kruchten, "Architectural Blueprints – The 4+1 View Model"](https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf) — the canonical logical view; shows the class-level reading that our definition coarsens (licence not checked).
- [arc42 §5 Building block view](https://docs.arc42.org/section-5/) and [arc42 examples](https://examples.arc42.org/) — level-1 white box plus black-box responsibility table; shows when to stop zooming (arc42 template CC BY-SA 4.0; examples' licences not checked).
- [Rozanski & Woods architecture description template](https://www.viewpoints-and-perspectives.info/vpandp/wp-content/themes/secondedition/doc/registered/RozanskiAndWoods-Architecture-Description-Template.pdf) — ready-made element template: responsibilities, inbound and outbound interfaces (licence not checked).
- [SEBoK, Logical Architecture Model Development](https://sebokwiki.org/wiki/Logical_Architecture_Model_Development) — the systems-engineering sense and the logical-to-physical allocation step (licence not checked).
- [Capella / Arcadia method](https://mbse-capella.org/arcadia.html) — a full method with the logical architecture as its own engineering level (open-source tool; licence not checked).
- [C4 model, Component](https://c4model.com/abstractions/component) — not a C5 itself, but the clearest public statement of what a component is and is not; a useful contrast.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->

1. Fix definition and scope: "logical = technology-neutral responsibility blocks and interfaces" for one system or solution.
2. List requirements/capabilities; assign each to exactly one block; group by cohesion; name blocks with nouns.
3. Derive each dependency from a responsibility and label it with the operation or information; drop any without a requirement behind it.
4. Put external capabilities (identity, payment provider, warehouse) outside the boundary.
5. Layout: top-to-bottom by dependency (consumer-facing blocks on top, providers below) or left-to-right for a request flow; 2–5 frames of about 3–7 blocks each (heuristic).
6. Text: block = name (≤3 words) + at most one responsibility line; interface label ≤3 words; detail goes into the companion table.
7. Colour encodes role only (internal / external / planned), never technology; add a legend.
8. Arrows: one meaning (depends-on), orthogonal, ending on the box or on the group border.
9. If technology is fixed later, redraw as C3/C4 instead of adding tags to C5.

**Self-check**
- [ ] Title names type and scope; legend explains every shape, colour and line.
- [ ] No product, framework or host names inside the boundary.
- [ ] Each block has one responsibility; no requirement is unowned or owned twice.
- [ ] Every line is labelled and the label matches the arrow direction.
- [ ] Siblings are the same kind of thing; no actors, steps or feature lists mixed in.
- [ ] External capabilities are outside the boundary and visibly different.
- [ ] Two different physical designs could realise this diagram.
- [ ] No status notes on the figure; every badge or number is explained.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->

- Useful: top-level module/package structure; interface and port definitions, `.proto` and OpenAPI files; import/dependency graphs; README and ADRs (intended responsibilities); route or menu definitions (features → blocks); CODEOWNERS; catalog descriptors such as Backstage `catalog-info.yaml` [16].
- Misleading on their own: `docker-compose.yml`, Kubernetes manifests and IaC describe containers and deployment (C3/G1); use them only to check that each runnable unit maps to a block.
- Ask people: intended responsibilities, the rationale of the cut, planned blocks and acceptable external capabilities. Treat code-derived blocks as a draft to confirm.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->

1. What should this diagram help decide (option comparison, work split, requirement coverage, onboarding) and who reads it? (Default: architects and developers; requirement coverage.)
2. One system or several; which part gets detail, which collapses to one box? (Default: whole system at one level; externals collapsed.)
3. Which "logical" do you mean: responsibility blocks, a class-level model, or a function tree? (Default: responsibility blocks; the others route to class/ER or function decomposition.)
4. Are technology choices already fixed? (Default: no; if yes, offer C3/C4 and keep the mapping in a table.)
5. Which external capabilities and which 3–6 key interactions must appear? (Default: identity, payment provider, the main purchase request.)

## Template {#template}
<!-- skill: keep (≤3 lines) -->

Model template: `assets/templates/C5.json` · Layout template: `statechart` · groups of kind `frame` hold the responsibility blocks inside one `boundary` and are ranked by dependency; externals sit outside it, the subject block has style `primary`, and `edges` of kind `call` carry operation labels.

## Sources {#sources}
<!-- skill: omit -->

1. Kruchten, "Architectural Blueprints – The 4+1 View Model of Software Architecture" (1995) — https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf — accessed 2026-10-14
2. The TOGAF Standard 9.1, Glossary (Logical/Physical Application Component) — https://pubs.opengroup.org/architecture/togaf91-doc/arch/apdxa.html — accessed 2026-10-14 (search excerpt only; TOGAF 10 text not verified)
3. Rozanski & Woods, Architecture Description Template (Functional View) — https://www.viewpoints-and-perspectives.info/vpandp/wp-content/themes/secondedition/doc/registered/RozanskiAndWoods-Architecture-Description-Template.pdf — accessed 2026-10-14
4. arc42 documentation, "5 – Building block view" — https://docs.arc42.org/section-5/ — accessed 2026-10-14
5. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/42010/cm/ — accessed 2026-10-14
6. SEBoK, "Logical Architecture Model Development" — https://sebokwiki.org/wiki/Logical_Architecture_Model_Development — accessed 2026-10-14
7. Samares Engineering, "Consistency between functional and logical architectures" — https://www.samares-engineering.com/en/2020/07/21/part-4-consistency-between-functional-and-logical-architectures — accessed 2026-10-14
8. Capella MBSE Tool, "Arcadia" — https://mbse-capella.org/arcadia.html — accessed 2026-10-14
9. SEI, Views and Beyond Collection — https://www.sei.cmu.edu/library/views-and-beyond-collection — accessed 2026-10-14
10. C4 model, Notation — https://c4model.com/diagrams/notation — accessed 2026-10-14
11. C4 model, Component — https://c4model.com/abstractions/component — accessed 2026-10-14
12. ArchiMate 3.2 Specification, Application Layer — https://pubs.opengroup.org/architecture/archimate32-doc/ch-Application-Layer.html — accessed 2026-10-14 (search excerpt only)
13. The Open Group, "The Open Group Announces ArchiMate 4 Specification" — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — accessed 2026-10-14 (search excerpt only)
14. C4 model, Review checklist — https://c4model.com/diagrams/checklist — accessed 2026-10-14
15. Wikipedia, "Software design description" (IEEE 1016-2009 viewpoints) — https://en.wikipedia.org/wiki/Software_design_description — accessed 2026-10-14 (secondary)
16. Backstage, Descriptor format of catalog entities — https://backstage.io/docs/features/software-catalog/descriptor-format/ — accessed 2026-10-14

### A7 · Conceptual architecture (solution overview) {#variant-a7}

Editorial grouping preserves the distinct notation; use this recipe and its checks.

1. Fix the frame: audience, purpose, state (current or target) and the solution boundary; write the title first.
2. List candidate blocks from requirements and capabilities; merge or split to 5–9 of one kind, each a 1–4 word noun.
3. Choose one layering scheme, top to bottom: users / channels → solution services → shared platform → data. External systems sit right or bottom, outside the boundary. Use left-to-right only for one dominant flow.
4. Place each block in exactly one layer, inside or outside the boundary; collapse non-focus subsystems into one box.
5. Add at most about 10 directed arrows, requester → provider; group-level links end at the group border; label only non-obvious arrows; optionally number one headline flow.
6. Text: block name, an optional one-line role, ≤3 tags; no sentences; type scale title > layer label > block name > tag.
7. Colour: neutral by default; one accent for the solution's own (or new) blocks; one style for shared components, identical everywhere; grey for externals; pair colour with border or pattern.
8. Add the legend (colours, borders, lines, numbering); cross-check names against C2 above and C3 / C5 below.

**Self-check**
- [ ] The title states scope and as-is / to-be; no internal version labels.
- [ ] 5–9 blocks of the same kind, named in the audience's language.
- [ ] No feature lists, bullets or sentences in boxes; no product names, protocols or ports unless asked.
- [ ] The boundary is explicit; every element is inside exactly one group or marked external.
- [ ] Arrows are directed, end on what they mean and are labelled where not obvious.
- [ ] The legend explains every colour, shape, border and line style; peers share one style.
- [ ] Icons only where they carry meaning.
- [ ] Block names match the neighbouring C1 / C2 / C3 views.

[Full method and historical sample](/types/a7-conceptual-architecture#meaning).

## Sample {#sample}
<!-- skill: path only -->
![C5 sample: logical view of an online shop with responsibility blocks](/samples/C5-logical-architecture.svg)
*Logical view of the online shop: building blocks grouped by responsibility in tinted zones (Selling: catalogue, cart, checkout; Fulfilment: order management, stock, shipping; Payments: payment handling, invoicing; Customer support: chat assistant). Order management is the subject (the dark block); each dependency is labelled with what is exchanged, and the payment provider and carrier sit outside the boundary.*
