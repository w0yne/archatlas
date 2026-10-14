---
code: C4
slug: component-diagram
family: C
names:
  en: Component diagram (C4 model level 3)
  zh: 组件图（C4 模型第 3 层）
  aliases:
    en: [component view, white-box view of a container, internal structure diagram, C4 model Level 3, Building Block View Level 2 (arc42)]
    zh: [组件视图, 容器内部结构图, 内部结构图, C4 模型第 3 层]
question: Inside this one container, which components does it consist of, what is each responsible for and built with, and how do they depend on each other and on other containers?
audiences: [developers, architects]
levels: [logical]
phases: [design, build]
scope: 'Exactly one container: its components inside a container boundary, plus the other containers, people and systems directly connected to them.'
formal: {kind: method, ref: 'C4 model (Simon Brown), Level 3 Component diagram; notation-independent, no versioned standard. Related: UML 2.5.1 component diagram (OMG), a different meaning of ''component'''}
neighbours: [C3, C5, C8, E1]
status: draft
---

# Component Diagram (组件图)

> The zoom into one container: its major building blocks, their responsibilities and technology, and the dependencies between them.

**A note on the code:** in this catalogue, code `C4` is the component diagram. It is Level 3 of the **C4 model**; the code and the method only share a name.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
It answers: *inside this one container, what are the major components, what is each responsible for and built with, and who calls whom, including the other containers they depend on?* It is Level 3 of the C4 model, Simon Brown's notation-independent method (no versioned standard) [1][4][5], and in arc42 the building-block view, level 2, the white box of one level-1 block [3]. It is a developer-facing view of internal structure. It leaves out other containers' internals, classes (C4 model Level 4, the code diagram), deployment and sequences over time [1][13].
**Definition used here: "component" has three meanings.** Say which one you draw.
- **C4 model component (this type):** a grouping of related functionality behind a well-defined interface, running inside one container. It is not separately deployable, and a package, namespace, folder or JAR is typically *not* a component [6].
- **UML component (UML 2.5.1):** a modular, replaceable part with provided and required interfaces, optionally with ports. It can be logical or physical and may be deployed on its own, so a UML component can match a C4 model *container* as well as a component [7][8][9]. Summarised from a secondary reference; not verified against the current spec text.
- **Cloud-vendor usage:** a view that swaps generic blocks for specific products and integration points, "a visual bill of materials" [10]. That is closer to a technology-labelled C3 view or a G2 diagram.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** software architects and developers [1]; not executives or customers.
- **Recommended?** The C4 model says **no**: draw it only where it adds value, and consider generating it for long-lived documentation [1], because component diagrams change often in active code [14]. A secondary summary of a 2026 talk reports advice that most teams only need Levels 1 and 2 [20]; that summary was not verified against the talk itself.
- **Scenarios:** design review of a complex service before a big change; onboarding to a large service ("where does this change go?"); agreeing module boundaries in a modular monolith or hexagonal design, with code checks as the guard; reviewing a component's dependencies on stores, queues and other services; finding seams before splitting a service.
- **When not to use:** a thin or CRUD-style container (C3 is enough); one per container "for completeness"; flows across containers (E1, E4); no stable code structure to map to; class-level detail (an IDE-generated class diagram) [13]; library design [2].
- **vs neighbours:**
  - Choose **C3** for the whole system; draw C4 only after C3 is agreed and one container proves complex [23].
  - Choose **C5** for technology-neutral, system-wide responsibilities; C4 is technology-labelled and per container.
  - Choose **C8** when the point is a layering rule; a component diagram may *show* layers but names real components.
  - Choose **E1** for the path through components in one scenario (the C4 model "dynamic" diagram is a numbered-interaction form [12]).

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **No mandated notation in the C4 model**: plain boxes and labelled arrows are the norm; the general C4 model notation rules and review checklist apply to every level [11][15].
- **Required:** title "Component diagram for `<Container>` in `<System>`"; **components**, each with name, type ("Component"), technology (e.g. "web controller", "TypeScript module") and a short responsibility; a **container boundary** around them; **relationships**; a **legend** [1][11].
- **Supporting elements:** other containers of the same system (data stores, queues, services) outside the boundary, plus people and external systems only if directly connected to a component [1].
- **Relationships:** one direction, a verb label that agrees with it ("calls", "reads from", "publishes to"); add the protocol where a line leaves the container; mark sync vs async in the legend if both appear; no double-headed arrows [10][11].
- **Optional UML interface notation:** provided-interface balls, required-interface sockets and ports are allowed when readers know UML or when interfaces are the point (e.g. hexagonal ports) [8]. They are not part of the C4 model, and they carry the UML meaning of "component".
- **Granularity [16]:** choose the architectural style first (by layer, by feature, hexagonal); ignore data types with little logic, validators, configuration and bootstrap code; define one identification rule per category (annotation, name suffix, package). Typically 5–15 components; split by feature if more.
- **Tools:** Structurizr DSL [17] and C4-PlantUML [18]; one model can feed both the C3 and C4 views [22].
- **Naming:** components are named as in the code (package, module or class names), so readers can find them [3][16].

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. Draw it only for containers that are complex, volatile or unfamiliar [1][3].
2. Make components findable: same names and module boundaries as the code, ideally with links to code locations [16].
3. Generate it when it must outlive a release: rules over annotations, naming patterns or module layout [14][16][24].
4. Show the main flow and the dependencies on other containers; these are what reviewers need.
5. Keep decomposition rationale in text or a decision record, and put a date and source revision on the figure so staleness is visible [3][19].

### Anti-patterns
1. Components that are really classes (dozens of boxes) or really folders with no responsibility [6].
2. Several containers' internals mixed in one diagram [1].
3. Invented "subcomponent" levels instead of a second diagram [19][21].
4. Shared libraries drawn as containers or components of their own; they are code reused inside components [19].
5. A technology bill of materials presented as a component diagram without saying which meaning is used [10].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [C4 model: Component diagram](https://c4model.com/diagrams/component) — scope, audience and the "not recommended for most teams" answer, with a reference example and key (CC BY 4.0).
- [C4 model: Component abstraction](https://c4model.com/abstractions/component) — what a component is and is not (CC BY 4.0).
- [Structurizr: component finder introduction](https://docs.structurizr.com/java/component/introduction) — deriving components from real code with explicit rules and what to ignore.
- [arc42 section 5: Building block view](https://docs.arc42.org/section-5/) — the equivalent outside the C4 model with black-box templates and advice on which blocks to refine (CC BY-SA 4.0).
- [uml-diagrams.org: component diagram reference](https://www.uml-diagrams.org/component-diagrams-reference.html) — provided and required interfaces, ports and assembly connectors, if UML notation is needed.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Confirm the one container and the reason (review, onboarding, refactor); if there is no C3, confirm it first.
2. Identify the style of the container (layered, feature modules, hexagonal, modular monolith); ask if the code is ambiguous.
3. List candidates: entry points (controllers, handlers, consumers, schedulers), application logic, outbound adapters (repositories, clients). Drop DTOs, utilities, configuration and bootstrap code.
4. Cluster into 5–15 components with code names, e.g. online shop Shop API: Catalogue Handler, Cart Handler, Checkout Handler, Pricing, Checkout Service, Order Repository, Payment Client, Warehouse Client, Event Publisher.
5. Layout: container boundary; entry points top or left, logic in the middle, adapters bottom or right; other containers (Order Database, "order placed" topic) and external systems (Payment Provider, Warehouse System) outside the boundary next to the adapter that reaches them. Top-to-bottom for layered code, left-to-right for request flow.
6. Draw only the main call paths, not every import; verb labels; protocol where a line leaves the container.
7. Text budget: name 1–3 words, technology one line, description up to about 10 words, arrow label up to about 5 words; no class lists.
8. Colour: components, other containers, external systems in three styles plus a shape cue; legend.
9. Add title, legend, date and source revision; offer an editable or regenerable source.

**Self-check**
- [ ] Exactly one container in scope; boundary, title and legend present.
- [ ] Every component is a cohesive part behind an interface, not a class, folder or library.
- [ ] Component names can be found in the repository.
- [ ] Every arrow has one direction and a matching label; lines leaving the container show protocol.
- [ ] Dependencies on other containers, stores and queues are shown; the main flow is obvious.
- [ ] No deployment detail, no classes, no other container's internals.
- [ ] 5–15 boxes; otherwise split by feature.
- [ ] The figure states which meaning of "component" it uses if UML notation appears.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Source tree: top-level packages, modules, namespaces; workspace or module declarations (strong signal in modular monoliths) [24].
- Annotations and naming suffixes (`@Controller`, `@Repository`, routers, `*Handler`, `*Client`): the rules component finders use [16].
- Import or dependency graphs and architecture tests show real edges; treat them as candidates to filter.
- Dependency-injection wiring and message-handler registrations show components and async entry points.
- Outbound clients, repositories and producers show dependencies on other containers.
- Not in code: intended responsibilities, which seams are architecturally significant, planned components. Ask people.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which container should be opened, and why? (the most complex or most-changed one, for a design review)
2. What is its structure style, and should components come from the code or from a target design? (derive from code)
3. How deep: about 5 coarse components or up to about 15? (5–9)
4. Which neighbouring containers and external systems must appear? (those a component calls directly)
5. Is UML interface notation needed, and do you want a regenerable source? (no UML; diagrams-as-code source)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/C4.json` · Layout template: `nested` · one `boundary` group for the container holding `component` nodes; other `container`, `store`, `queue` and `external` nodes outside it; edges between leaves carry labels.

## Sources {#sources}
<!-- skill: omit -->
1. C4 model — Component diagram — https://c4model.com/diagrams/component — accessed 2026-10-14
2. C4 model — FAQ — https://c4model.com/faq — accessed 2026-10-14
3. arc42 — Section 5, Building block view — https://docs.arc42.org/section-5/ — accessed 2026-10-14
4. C4 model — History — https://c4model.com/history — accessed 2026-10-14
5. C4 model — Home — https://c4model.com/ — accessed 2026-10-14
6. C4 model — Component (abstraction) — https://c4model.com/abstractions/component — accessed 2026-10-14
7. uml-diagrams.org — UML component — https://www.uml-diagrams.org/component.html — accessed 2026-10-14
8. uml-diagrams.org — UML component diagram reference — https://www.uml-diagrams.org/component-diagrams-reference.html — accessed 2026-10-14
9. OMG — Unified Modeling Language 2.5.1 — https://www.omg.org/spec/UML/2.5.1/About-UML — accessed 2026-10-14
10. Microsoft Learn — Create architecture design diagrams (Azure Well-Architected) — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — accessed 2026-10-14
11. C4 model — Notation — https://c4model.com/diagrams/notation — accessed 2026-10-14
12. C4 model — Dynamic diagram — https://c4model.com/diagrams/dynamic — accessed 2026-10-14
13. C4 model — Code diagram — https://c4model.com/diagrams/code — accessed 2026-10-14
14. C4 model — Diagrams FAQ — https://c4model.com/diagrams/faq — accessed 2026-10-14
15. C4 model — Review checklist — https://c4model.com/diagrams/checklist — accessed 2026-10-14
16. Structurizr — Component finder introduction — https://docs.structurizr.com/java/component/introduction — accessed 2026-10-14
17. Structurizr — DSL language reference — https://docs.structurizr.com/dsl/language — accessed 2026-10-14
18. C4-PlantUML — https://github.com/plantuml-stdlib/C4-PlantUML — accessed 2026-10-14
19. Working Software — Misuses and mistakes of the C4 model — https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model — accessed 2026-10-14
20. daily.dev — Summary of "The C4 Model" (S. Brown, S. Kaiser, GOTO 2026) — https://daily.dev/posts/the-c4-model-visualizing-software-architecture-simon-brown-susanne-kaiser-goto-2026-xuw6udw2z — accessed 2026-10-14
21. C4 model — Abstractions FAQ — https://c4model.com/abstractions/faq — accessed 2026-10-14
22. godatadriven/c4-model-example — https://github.com/godatadriven/c4-model-example — accessed 2026-10-14
23. C4 model — Container diagram — https://c4model.com/diagrams/container — accessed 2026-10-14
24. S. Brown — Reverse-engineering architecture diagrams (talk) — https://www.youtube.com/watch?v=2Cz9ZDIlBeM — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![C4 sample: component diagram of the online shop's Shop API with handlers, checkout logic, repository and clients for the payment provider and warehouse system](/samples/C4-component-diagram.svg)
*Sample pending (generated by the renderer from `examples/`).*
