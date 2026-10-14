---
code: B4
slug: scope-diagram
family: B
names:
  en: Scope diagram
  zh: 范围图
  aliases:
    en: [in-scope out-of-scope diagram, scope boundary map]
    zh: [范围内外图, 范围边界图]
question: "What does this initiative include or exclude, and which external dependencies still require work?"
audiences: [leaders, product, architects]
level: concept
phases: [initiate, requirements]
scope: system
formal:
  kind: convention
  ref: "Scope modeling — https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-41-scope-modelling/"
neighbours: [C2, A3, B1, D2, C6]
status: draft
sourceRev: "2026-10-14"
---

# Scope diagram

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A scope diagram answers **what an initiative includes or excludes and which dependencies affect that agreement**. Its concern is responsibility for change and delivery, not merely where software runs [1][2].
**Definition used here:** an informal inclusion/exclusion map, optionally paired with a context diagram. It is not another name for the C4 model's System Context diagram or a DFD.
A payment provider can be outside an online shop's system boundary while its integration is inside a checkout project's scope. System, delivery, ownership, and trust boundaries are different facts.
Context views instead describe a subject and its environment: C4 model context emphasizes people/systems; arc42 separates domain exchanges from technical channels; DFD context emphasizes data crossing a whole-system process [3–6].
The scope map omits detailed behavior, deployment, and complete interface contracts. Its diagram cannot itself establish stakeholder agreement; link the decision baseline.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** sponsors, product owners, analysts, architects, and delivery/integration teams.
- **Scenarios:** agree checkout-release inclusions; record support-chatbot exclusions; identify integration work before estimation; compare current and proposed scope; expose unresolved boundary decisions.
- **When not:** specifying sequence, implementation units, firewall rules, or an entire enterprise landscape.
- Choose **C2 System context** for one system's direct external users/dependencies.
- Choose **A3 Business context** for domain partners and exchanges, or **C6 Integration/interface** for technical channels/contracts.
- Choose **D2 Data flow diagram** for data sources/sinks and transformation; declare its context/decomposition numbering.
- Choose **B1 Use case diagram** for actor goals and **C1 Application landscape** for several peer systems.
- A scope map and a context diagram can be companion views; do not silently mix their boundary and arrow meanings.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Core scope map:** named initiative/release and baseline; included capabilities/work; explicit exclusions or a statement that exclusions remain undecided; named boundary meaning [1][2].
- **Optional:** assumptions, undecided scope, prerequisites, owners, and links to acceptance/decision records.
- **Arrows:** normally unnecessary for inclusion/exclusion. If used for prerequisites or dependencies, label that relation; it is not automatically data flow.
- **Context companion:** name one subject and relevant neighbors; do not label all external systems “excluded project work.”
- **C4 model context:** directly connected people/software systems with labeled unidirectional relationships and a key; omit internal components [3][4].
- **arc42 context:** distinguish domain inputs/outputs from technical channels; technical details belong where that concern is selected [5].
- **DFD context:** one process represents the whole system; named arrows follow data, not control sequence. Internal functions/stores belong in decomposition; external stores can be represented under the chosen convention [6].
- **Numbering:** Yourdon calls the decomposition beneath context *Figure 0*; other sources call context *level 0*. State the scheme instead of treating “DFD 0” as unambiguous [6].
- **Legend/detail:** identify delivery, system, ownership, and trust boundaries separately where shown. Use short labels and move contracts/assumptions into a companion table.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- Agree the boundary and change baseline; avoid presenting an author's inference as accepted scope [1][2].
- Separate excluded capabilities from external dependencies; avoid omitting integration work because a provider is outside the system.
- Name meaningful exchanges in a context companion; avoid unlabeled “connects to” lines [3][4].
- Separate business and technical concerns; avoid internal components/protocol detail in a C4 model context [3][5].
- Preserve context data interfaces when decomposing a DFD; avoid inconsistent level numbering or arrows meaning “next step” [6].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [PMI, Three proven ways business analysts help prevent scope creep, Exhibit 2](https://www.pmi.org/learning/library/business-analysts-help-prevent-scope-creep-9352) — a populated product-context diagram demonstrates boundary questions that support scope analysis. **Rights:** no open image license established; link only.
- [arc42, HTML Sanity Checker business context](https://docs.arc42.org/examples/business-context-1/) — a diagram plus neighbor table makes external exchanges and constraints explicit. **Rights:** page states CC BY-SA 4.0; verify asset-specific terms and preserve attribution/share-alike if adapting.
- [arc42, HTML Sanity Checker technical context](https://docs.arc42.org/examples/technical-context-1/) — the same public project provides a technical companion, distinguishing channels/artifacts from domain exchanges. **Rights:** page states CC BY-SA 4.0; check individual assets before adaptation.
- [C4 model, System context diagram example](https://c4model.com/diagrams/system-context) — a one-system view and key demonstrate the neighboring context concern. **Rights:** no asset-specific reuse license verified here; link only.

These are **context examples used in scope discussions**, not four identical inclusion/exclusion maps. The paired arc42 views are one project, not independent case studies. Source text and diagram descriptions were inspected; no visual audit is claimed.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Select delivery scope or a named context variant; state the audience and baseline.
2. Identify the initiative/subject and explain what its boundary means.
3. Gather agreed inclusions, exclusions, dependencies, and unresolved decisions.
4. Keep external system ownership separate from integration work in scope.
5. Lay out labeled scope regions; for a context companion, center the subject and group relevant neighbors.
6. Use short labels, restrained color, and explicit edge meanings; keep contracts in a table.
7. Check evidence and companion views; record disagreements without inventing agreement.

**Self-check**
- [ ] Variant, subject/initiative, and baseline are named.
- [ ] Delivery, system, ownership, and trust boundaries are distinct.
- [ ] Inclusions/exclusions have decision evidence or are marked unresolved.
- [ ] External dependencies are not mistaken for excluded integration work.
- [ ] Arrow direction and labels match the selected convention.
- [ ] Context detail and DFD numbering are appropriate and explicit.
- [ ] Relevant exchanges, assumptions, labels, and endpoints remain readable.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Handlers, API contracts, external clients, events, and operator docs identify candidate exchanges.
- Deployment/build evidence helps locate implementation inside the selected system, not project scope.
- Requirements, accepted decisions, and release plans establish inclusions/exclusions.
- Code absence is not proof of an exclusion; a fixture is not a production dependency.
- Record `boundary/element/edge | path:line/section | revision/environment | verified/inferred/doc-only/conflict`.
- Confirm boundary decisions against authoritative requirements and ownership evidence.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Is the decision about delivery commitments or the system's environment?
2. Which initiative/subject, baseline, and boundary should be shown?
3. Which inclusions and exclusions are already agreed?
4. Which external dependencies create integration work or constraints?
5. Does the audience also need domain exchanges or technical channels?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Integration target: `assets/templates/B4.json`; layout `nested`. Scope regions contain work/capabilities; use a separate context view when nodes and arrows describe an operating system boundary.

## Sources {#sources}
<!-- skill: omit -->
1. IIBA — *BABOK Guide, 10.41 Scope Modelling* — https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/10-techniques/10-41-scope-modelling/ — accessed 2026-10-14 through official indexed summary; full chapter not retrieved.
2. PMI — *Three proven ways business analysts help prevent scope creep* — https://www.pmi.org/learning/library/business-analysts-help-prevent-scope-creep-9352 — accessed 2026-10-14; article text and Exhibit 2/3 descriptions inspected.
3. C4 model — *System context diagram* — https://c4model.com/diagrams/system-context — accessed 2026-10-14.
4. C4 model — *Notation* — https://c4model.com/diagrams/notation — accessed 2026-10-14.
5. arc42 — *Section 3: Context and Scope* — https://docs.arc42.org/section-3/ — accessed 2026-10-14.
6. Ed Yourdon — *Just Enough Structured Analysis, Chapter 9*, revision 2006-01-31, public PDF mirror — https://www.businessanalystlearnings.com/s/Yourdon-DFD.pdf — accessed 2026-10-14; targeted text confirms context versus Figure 0 and external-store qualification.
7. arc42 — *Example Business Context: HTML Sanity Checker* — https://docs.arc42.org/examples/business-context-1/ — accessed 2026-10-14.
8. arc42 — *Example Technical Context: HTML Sanity Checker* — https://docs.arc42.org/examples/technical-context-1/ — accessed 2026-10-14.

## Sample {#sample}
<!-- skill: path only -->
Planned asset: `/samples/B4-scope-diagram.svg`.

**Caption:** A checkout release includes payment integration and order confirmation, excludes a loyalty program, and records an external provider as a dependency. The generated sample is not yet available.
