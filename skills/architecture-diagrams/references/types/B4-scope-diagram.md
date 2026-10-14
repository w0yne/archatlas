# Scope diagram (范围图)
<!-- Generated from content/en/types/B4-scope-diagram.md by tools/build_skill_refs.py. Do not edit. -->
> What does this initiative include or exclude, and which external dependencies still require work?
Scope: system Neighbours: A3, B1, C2.

## Meaning
A scope diagram answers **what an initiative includes or excludes and which dependencies affect that agreement**. Its concern is responsibility for change and delivery, not merely where software runs.
**Definition used here:** an informal inclusion/exclusion map, optionally paired with a context diagram. It is not another name for the C4 model's System Context diagram or a DFD.
A payment provider can be outside an online shop's system boundary while its integration is inside a checkout project's scope. System, delivery, ownership, and trust boundaries are different facts.
Context views instead describe a subject and its environment: C4 model context emphasizes people/systems; arc42 separates domain exchanges from technical channels; DFD context emphasizes data crossing a whole-system process.
The scope map omits detailed behaviour, deployment, and complete interface contracts. Its diagram cannot itself establish stakeholder agreement; link the decision baseline.

## When to use and how to choose
- **Audience:** sponsors, product owners, analysts, architects, and delivery/integration teams.
- **Scenarios:** agree checkout-release inclusions; record support-chatbot exclusions; identify integration work before estimation; compare current and proposed scope; expose unresolved boundary decisions.
- **When not:** specifying sequence, implementation units, firewall rules, or an entire enterprise landscape.
- Choose **C2 System context** for one system's direct external users/dependencies.
- Choose **A3 Business context** for domain partners and exchanges, or **C6 Integration/interface** for technical channels/contracts.
- Choose **D2 Data flow diagram** for data sources/sinks and transformation; declare its context/decomposition numbering.
- Choose **B1 Use case diagram** for actor goals and **C1 Application landscape** for several peer systems.
- A scope map and a context diagram can be companion views; do not silently mix their boundary and arrow meanings.

## Notation and elements
- **Core scope map:** named initiative/release and baseline; included capabilities/work; explicit exclusions or a statement that exclusions remain undecided; named boundary meaning.
- **Optional:** assumptions, undecided scope, prerequisites, owners, and links to acceptance/decision records.
- **Arrows:** normally unnecessary for inclusion/exclusion. If used for prerequisites or dependencies, label that relation; it is not automatically data flow.
- **Context companion:** name one subject and relevant neighbors; do not label all external systems “excluded project work.”
- **C4 model context:** directly connected people/software systems with labeled unidirectional relationships and a key; omit internal components.
- **arc42 context:** distinguish domain inputs/outputs from technical channels; technical details belong where that concern is selected.
- **DFD context:** one process represents the whole system; named arrows follow data, not control sequence. Internal functions/stores belong in decomposition; external stores can be represented under the chosen convention.
- **Numbering:** Yourdon calls the decomposition beneath context *Figure 0*; other sources call context *level 0*. State the scheme instead of treating “DFD 0” as unambiguous.
- **Legend/detail:** identify delivery, system, ownership, and trust boundaries separately where shown. Use short labels and move contracts/assumptions into a companion table.

## Best practices and anti-patterns
- Agree the boundary and change baseline; avoid presenting an author's inference as accepted scope.
- Separate excluded capabilities from external dependencies; avoid omitting integration work because a provider is outside the system.
- Name meaningful exchanges in a context companion; avoid unlabeled “connects to” lines.
- Separate business and technical concerns; avoid internal components/protocol detail in a C4 model context.
- Preserve context data interfaces when decomposing a DFD; avoid inconsistent level numbering or arrows meaning “next step”.

## Drawing recipe
1. Select delivery scope or a named context variant; state the audience and baseline.
2. Identify the initiative/subject and explain what its boundary means.
3. Gather agreed inclusions, exclusions, dependencies, and unresolved decisions.
4. Keep external system ownership separate from integration work in scope.
5. Lay out labeled scope regions; for a context companion, center the subject and group relevant neighbors.
6. Use short labels, restrained colour, and explicit edge meanings; keep contracts in a table.
7. Check evidence and companion views; record disagreements without inventing agreement.

**Self-check**
- [ ] Variant, subject/initiative, and baseline are named.
- [ ] Delivery, system, ownership, and trust boundaries are distinct.
- [ ] Inclusions/exclusions have decision evidence or are marked unresolved.
- [ ] External dependencies are not mistaken for excluded integration work.
- [ ] Arrow direction and labels match the selected convention.
- [ ] Context detail and DFD numbering are appropriate and explicit.
- [ ] Relevant exchanges, assumptions, labels, and endpoints remain readable.

## Evidence in a code repository
- Handlers, API contracts, external clients, events, and operator docs identify candidate exchanges.
- Deployment/build evidence helps locate implementation inside the selected system, not project scope.
- Requirements, accepted decisions, and release plans establish inclusions/exclusions.
- Code absence is not proof of an exclusion; a fixture is not a production dependency.
- Record `boundary/element/edge | path:line/section | revision/environment | verified/inferred/doc-only/conflict`.
- Confirm boundary decisions against authoritative requirements and ownership evidence.

## Guided-mode questions
1. Is the decision about delivery commitments or the system's environment?
2. Which initiative/subject, baseline, and boundary should be shown?
3. Which inclusions and exclusions are already agreed?
4. Which external dependencies create integration work or constraints?
5. Does the audience also need domain exchanges or technical channels?

## Template
Model template: `assets/templates/B4.json` · Layout template: `nested` · scope regions are `boundary` groups (in scope, out of scope with `dashed`, dependency in style `external`) that contain `component` nodes.
Use a separate context view when nodes and arrows describe an operating system boundary.

## Sample
Figure: `samples/B4-scope-diagram.svg` (published with the site)
