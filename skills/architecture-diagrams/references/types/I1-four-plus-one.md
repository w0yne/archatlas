# 4+1 view model
<!-- Generated from content/en/types/I1-four-plus-one.md by tools/build_skill_refs.py. Do not edit. -->
> How can different stakeholders understand one architecture through views that answer their concerns and stay consistent?
Scope: system Neighbours: I2, C5, G1, E1.

## Meaning
**Definition used here:** Kruchten's 1995 method organizes several architectural views; it is neither one standardized diagram nor a formal notation.
The **logical** view explains significant abstractions; **process** explains runtime concurrency and synchronization; **development** explains static code organization; **physical** maps execution onto hardware.
The **+1** comprises architecturally significant scenarios that drive discovery and validate those views. It is not an exhaustive use-case catalog.
Correspondences matter: one logical responsibility may span modules, processes, and nodes. Matching names do not prove one-to-one mappings.
The model leaves out implementation minutiae. ISO/IEC/IEEE 42010:2022 defines architecture-description requirements; arc42 supplies a documentation template. Neither is equivalent to 4+1, nor does using 4+1 establish compliance.
The four abstraction levels of the **C4 model** answer a different question; its diagrams can contribute selected views without replacing this organization.

## When to use and how to choose
- **Audience:** architects coordinating domain specialists, developers, integrators, and operations.
- **Review:** explain an online shop's responsibilities, worker concurrency, source modules, and deployment separately.
- **Performance:** trace checkout through competing execution units and resources.
- **Onboarding:** distinguish the shop's package dependencies from runtime communication.
- **Evolution:** compare deployment configurations or validate a support chatbot's recovery scenario.
- **Do not use:** a full view set when one focused diagram answers the question. Omit unhelpful views or combine equivalent logical/development descriptions, explaining the tailoring.
- Choose **C5** for logical structure alone, **G1** for deployment, **E1** for one interaction sequence, or **I2** for enterprise service support across layers.
- Use arc42 for the surrounding document; select C4 model diagrams by their abstraction, not by matching the number four.

## Notation and elements
- **Required by this recipe:** scope and baseline, selected views and concerns, significant elements, scenario outcomes, mapping records, and per-view legends.
- **Logical:** abstractions and relationships such as association, containment, or inheritance; do not imply network traffic.
- **Process:** processes/tasks, communication, and synchronization; distinguish synchronous calls, asynchronous messages, and broadcasts.
- **Development:** modules/subsystems and import or compilation dependencies; with “depends on,” point dependent → dependency.
- **Physical:** nodes, communication links, and software allocation; distinguish connectivity from directed requests.
- **Scenarios:** instances and ordered interactions, with triggers and observable outcomes; these are selected for importance, frequency, or technical risk.
- **Optional:** replicas, timing, ownership, constraints, alternative configurations, and state diagrams when relevant.
- Use concise structural names, action labels for messages, and stable identities across views. Record mappings between different kinds of unit.
- There is no mandatory 4+1 symbol or color scheme. The paper uses simplified Booch notation but permits alternatives; declare each chosen notation and obey its semantics.
- Preserve formal line styles when using UML or another notation; record uncertainty separately, not by redefining dashed connectors.

## Best practices and anti-patterns
- Select risky or significant scenarios; avoid a catalog of routine features.
- Maintain cross-view mappings; avoid class = module = process = host assumptions.
- Test and measure architectural claims; agreement between drawings does not prove performance.
- Tailor the view set; avoid five repetitive sections or a single overloaded picture.
- Record decisions and constraints; avoid treating historical tools, layer counts, or module sizes as universal requirements.

## Drawing recipe
1. Fix the readers, boundary, baseline, and selected concerns.
2. Select significant scenarios, such as checkout and its recovery case.
3. Inventory logical responsibilities, execution units, source units, and nodes separately.
4. Draw focused views; group by responsibility, execution boundary, dependency, or placement as appropriate.
5. Use a consistent reading direction, short labels, restrained color, and a legend per notation.
6. Link views with stable identities and explicit mappings; script each scenario through them.
7. Review the mappings and rendered figures; test quality claims independently.

**Self-check**
- [ ] Every selected view answers a distinct concern.
- [ ] Omitted or combined views have a reason.
- [ ] Process means runtime concurrency; development means static software organization.
- [ ] Scenarios have significant triggers, interactions, and outcomes.
- [ ] Logical, source, runtime, and physical units are not falsely equated.
- [ ] Mappings, arrow meanings, and endpoints are consistent.
- [ ] Evidence gaps and unmeasured claims are explicit.
- [ ] Labels and legends remain readable at the intended size.

## Evidence in a code repository
- Logical: domain types, interfaces, responsibilities, and architectural decisions.
- Development: manifests, build targets, imports, visibility rules, and library boundaries.
- Process: entry points, worker loops, thread/task creation, queues, and synchronization.
- Physical: deployment manifests, infrastructure definitions, and environment overlays; declared configuration is not live-state proof.
- Scenarios: integration tests, handlers, consumers, and traces; requirements establish significance.
- Mappings: trace symbols through build outputs, runtime commands, and deployment references.
- Record commit, path/line or symbol, and verified/inferred/doc-only/conflict status. Logical abstractions need not appear in startup files.

## Guided-mode questions
1. Which decision and readers should the view set support?
2. Which system boundary, baseline, and environment apply?
3. Which scenarios carry the greatest importance or technical risk?
4. Which concerns need separate views, and which can be combined?
5. Which notations and evidence sources can establish the mappings?

## Template
Model template: `assets/templates/I1.json` · Layout template: `layered` · views and scenarios are `layer` groups holding `component` and `task` nodes, joined by a `dependency` edge from the scenarios to the views.
This is an overview index: it must link to the substantive views, not substitute for them.

## Sample
Figure: `samples/I1-four-plus-one.svg` (published with the site)
