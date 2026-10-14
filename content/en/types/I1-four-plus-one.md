---
code: I1
slug: four-plus-one
family: I
names:
  en: 4+1 view model
  zh: 4+1 视图模型
  aliases:
    en: [4+1 architectural view model, Kruchten 4+1]
    zh: [4+1 架构视图模型, 克鲁岑 4+1 视图模型]
question: How can different stakeholders understand one architecture through views that answer their concerns and stay consistent?
audiences: [architects, developers]
levels: [concept, logical, physical]
phases: [design]
scope: system
formal: {kind: method, ref: 'Kruchten, Architectural Blueprints—The 4+1 View Model of Software Architecture (1995), IEEE Software 12(6), pp. 42–50; https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf'}
neighbours: [C5, E1, G1, I2]
status: draft
sourceRev: '2026-10-14'
---

# 4+1 view model (4+1 视图模型)

> Four coordinated views of one software architecture (logical, process, development, physical), tied together by a few significant scenarios.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
<!-- skill-text
**Definition used here:** Kruchten's 1995 method organises several architectural views; it is neither one standardised diagram nor a formal notation.
Views: **logical** (significant abstractions; domain specialists), **process** (runtime concurrency, not business workflow; integrators), **development** (code organisation; developers), **physical** (execution on nodes; operations).
The **+1** is a few significant scenarios that discover and validate the views, not an exhaustive use-case catalogue.
Correspondences matter: one logical responsibility may span modules, processes and nodes; matching names do not prove one-to-one mappings.
Later texts call development "implementation" and physical "deployment"; say which original view is meant. ISO/IEC/IEEE 42010 and arc42 are not equivalent to 4+1.
-->
**Definition used here:** Kruchten's 1995 method organises several architectural views; it is neither one standardized diagram nor a formal notation [1].
The **logical** view explains significant abstractions; **process** explains runtime concurrency and synchronization; **development** explains static code organisation; **physical** maps execution onto hardware.

| View | Concern and typical reader | Leaves out |
|---|---|---|
| Logical | significant abstractions and functionality; domain specialists, designers | full class inventory, packaging, processor allocation |
| Process | concurrency, synchronisation, communication, availability, performance; integrators | development workflow, business procedures |
| Development | modules, subsystems, dependencies, visibility; developers, maintainers | threads, message timing, placement |
| Physical | software execution mapped to nodes and networks; systems and operations engineers | every source dependency and deployment command |
| +1 scenarios | significant interactions that discover and validate the views; all readers | an exhaustive use-case catalogue |

Later descriptions often rename **development** to "implementation" and **physical** to "deployment"; state which original view is meant. "Process" is runtime concurrency, not a business workflow.
The **+1** comprises architecturally significant scenarios that drive discovery and validate those views. It is not an exhaustive use-case catalog.
Correspondences matter: one logical responsibility may span modules, processes, and nodes. Matching names do not prove one-to-one mappings [1].
The model leaves out implementation minutiae. ISO/IEC/IEEE 42010:2022 defines architecture-description requirements; arc42 supplies a documentation template. Neither is equivalent to 4+1, nor does using 4+1 establish compliance [2][3].
The four abstraction levels of the **C4 model** answer a different question; its diagrams can contribute selected views without replacing this organisation [4].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** architects coordinating domain specialists, developers, integrators, and operations.
- **Review:** explain an online shop's responsibilities, worker concurrency, source modules, and deployment separately.
- **Performance:** trace checkout through competing execution units and resources.
- **Onboarding:** distinguish the shop's package dependencies from runtime communication.
- **Evolution:** compare deployment configurations or validate a support chatbot's recovery scenario.
- **Do not use:** a full view set when one focused diagram answers the question. Omit unhelpful views or combine equivalent logical/development descriptions, explaining the tailoring [1].
- **Also not:** a replacement for detailed business-process models (A5) or for enterprise portfolio views (C1, I2).
- Choose **C5** for logical structure alone, **G1** for deployment, **E1** for one interaction sequence, or **I2** for enterprise service support across layers.
- Use arc42 for the surrounding document; select C4 model diagrams by their abstraction, not by matching the number four [3][4].

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required by this recipe:** scope and baseline, selected views and concerns, significant elements, scenario outcomes, mapping records, and per-view legends.
- **Logical:** abstractions and relationships such as association, containment, or inheritance; do not imply network traffic.
- **Process:** processes/tasks, communication, and synchronization; distinguish synchronous calls, asynchronous messages, and broadcasts.
- **Development:** modules/subsystems and import or compilation dependencies; with “depends on,” point dependent → dependency.
- **Physical:** nodes, communication links, and software allocation; distinguish connectivity from directed requests.
- **Scenarios:** instances and ordered interactions, with triggers and observable outcomes; these are selected for importance, frequency, or technical risk [1].
- **Optional:** replicas, timing, ownership, constraints, alternative configurations, and state diagrams when relevant.
- Use concise structural names, action labels for messages, and stable identities across views. Record mappings between different kinds of unit.
- There is no mandatory 4+1 symbol or colour scheme. The paper uses simplified Booch notation but permits alternatives; declare each chosen notation and obey its semantics [1].
- Preserve formal line styles when using UML or another notation; record uncertainty separately, not by redefining dashed connectors.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- Select risky or significant scenarios; avoid a catalog of routine features [1].
- Maintain cross-view mappings; avoid class = module = process = host assumptions [1].
- Test and measure architectural claims; agreement between drawings does not prove performance [1].
- Tailor the view set; avoid five repetitive sections or a single overloaded picture [1][4].
- Record decisions and constraints; avoid treating historical tools, layer counts, or module sizes as universal requirements [1][3].

## Exemplars {#exemplars}
<!-- skill: omit -->
These five figures cover the five concerns. Four belong to one simplified telephone-switch case; Figure 6 uses a separate air-traffic-control illustration. They are not five independent case studies. Page links use the UBC PDF's internal pagination.

- [Figure 3a, logical blueprint, p. 4](https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf#page=4) — isolates domain abstractions without equating them with processes. **License:** no open image-reuse permission verified; link only.
- [Figure 5, process blueprint, p. 6](https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf#page=6) — distinguishes execution units and communication. This is not the later, similarly numbered notation figure. **License:** no open image license verified; link only.
- [Figure 6, development layers, p. 7](https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf#page=7) — shows static subsystem organization; its five layers are an example, not a rule. **License:** no open image license verified; link only.
- [Figure 9, physical allocation, p. 8](https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf#page=8) — makes process-to-node mapping explicit. **License:** no open image license verified; link only.
- [Figure 11, scenario fragment, p. 10](https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf#page=10) — numbered interactions connect participants to runtime behavior. **License:** no open image license verified; link only.

Figure descriptions were checked through text extraction; images were not visually reviewed. Public access is not permission to copy or trace a figure. Create original examples and check rights before adapting third-party artwork.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix the readers, boundary, baseline, and selected concerns.
2. Select significant scenarios, such as checkout and its recovery case.
3. Inventory logical responsibilities, execution units, source units, and nodes separately.
4. Draw focused views; group by responsibility, execution boundary, dependency, or placement as appropriate.
5. Use a consistent reading direction, short labels, restrained colour, and a legend per notation.
6. Link views with stable identities and explicit mappings; script each scenario through them.
7. Review the mappings and rendered figures; test quality claims independently.

**Self-check**
- [ ] Every selected view answers a distinct concern.
- [ ] Omitted or combined views have a reason.
- [ ] Process means runtime concurrency; development means static software organisation.
- [ ] Scenarios have significant triggers, interactions, and outcomes.
- [ ] Logical, source, runtime, and physical units are not falsely equated.
- [ ] Mappings, arrow meanings, and endpoints are consistent.
- [ ] Evidence gaps and unmeasured claims are explicit.
- [ ] Labels and legends remain readable at the intended size.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Logical: domain types, interfaces, responsibilities, and architectural decisions.
- Development: manifests, build targets, imports, visibility rules, and library boundaries.
- Process: entry points, worker loops, thread/task creation, queues, and synchronization.
- Physical: deployment manifests, infrastructure definitions, and environment overlays; declared configuration is not live-state proof.
- Scenarios: integration tests, handlers, consumers, and traces; requirements establish significance.
- Mappings: trace symbols through build outputs, runtime commands, and deployment references.
- Record commit, path/line or symbol, and verified/inferred/doc-only/conflict status. Logical abstractions need not appear in startup files.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which decision and readers should the view set support?
2. Which system boundary, baseline, and environment apply?
3. Which scenarios carry the greatest importance or technical risk?
4. Which concerns need separate views, and which can be combined?
5. Which notations and evidence sources can establish the mappings?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/I1.json` · Layout template: `layered` · views and scenarios are `layer` groups holding `component` and `task` nodes, joined by a `dependency` edge from the scenarios to the views.
This is an overview index: it must link to the substantive views, not substitute for them.

## Sources {#sources}
<!-- skill: omit -->
1. Kruchten, *Architectural Blueprints—The “4+1” View Model of Software Architecture* (1995) — https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf — accessed 2026-10-14; complete paper text extracted.
2. ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description* — https://www.iso.org/standard/74393.html — accessed 2026-10-14; official catalog excerpts, not the complete paid standard.
3. arc42, *Template Overview* — https://arc42.org/overview — accessed 2026-10-14; page text extracted.
4. C4 model, *Diagrams* — https://c4model.com/diagrams — accessed 2026-10-14; page text extracted.

## Sample {#sample}
<!-- skill: path only -->
![I1 sample: 4+1 views of an online shop](/samples/I1-four-plus-one.svg)
*4+1 views of the online shop: logical, process, development and physical views, linked by mapping lines (classes run as tasks, tasks live in modules, modules deploy to nodes) and validated by two scenarios, checkout and recovery after failure.*
