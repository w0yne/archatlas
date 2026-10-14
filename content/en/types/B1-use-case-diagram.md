---
code: B1
slug: use-case-diagram
family: B
names:
  en: Use case diagram
  zh: 用例图
  aliases:
    en: [UML use case diagram, actor–use-case diagram]
    zh: [UML 用例图, 参与者—用例图]
question: Which valuable outcomes does the subject support, and which external roles participate?
audiences: [product, business, developers]
levels: [concept]
phases: [requirements]
scope: system
formal: {kind: standard, ref: 'OMG UML 2.5.1, Chapter 18 — https://www.omg.org/spec/UML/2.5.1/PDF'}
neighbours: [A4, B2, B4]
status: draft
sourceRev: '2026-10-14'
---

# Use case diagram (用例图)

> Actors outside a system boundary, connected to the user goals the system supports; no order, screens or internals.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A use case diagram answers **which valuable outcomes a subject supports, and which external roles participate**. Its concern is externally visible behaviour and responsibility boundaries, rather than implementation [1].
**Definition used here:** OMG UML 2.5.1, Chapter 18. A use case specifies behaviour of a subject that produces an observable result of value to actors or other stakeholders. An actor is an external role, played by a person or another system [1].
“Place an order” is a useful goal for an online shop; “call a database” is usually an implementation step. A business subject can include manual behaviour, while a software subject has a different boundary.
The diagram omits execution order, detailed exceptions, screen layout, deployment, and access-control enforcement. A *use case model* includes behavioural descriptions beyond the diagram; a story map is a different technique.
UML defines semantics and notation, not a fixed layout, colour palette, or maximum number of ovals. A diagram is an index into behaviour, not a complete requirement specification.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** analysts, product owners, domain specialists, testers, and developers.
- **Scenarios:** agree an online shop's customer goals; compare shopper and support roles; identify an external payment provider's participation; index acceptance scenarios; distinguish a business service from its supporting software.
- **When not:** precise ordering, data schema, screen navigation, or hosting. A textual scenario may suffice for one simple goal.
- Choose **B2 User story map** for narrative context and incremental delivery slices.
- Choose **B4 Scope diagram** for agreed inclusions/exclusions and **C2 System context** for external systems and exchanges.
- Choose **E1 Sequence diagram** or **E2 Activity/flowchart** for ordered behaviour, branching, and timing.
- Use a companion **textual use case** for preconditions, success behaviour, alternatives, and postconditions; the oval does not contain these details.
- Choose **A4 Business scenario matrix** when the question is which roles take part in which business activities, and in which release, rather than which use cases the system offers.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Use case:** normally a named ellipse; UML also permits classifier notation. Prefer a short verb–object goal such as “Track order” [1].
- **Actor:** stick figure or permitted classifier notation; name the external role, not an internal module [1].
- **Subject:** a named rectangle enclosing applicable use cases is optional UML notation, recommended when scope matters. Enclosure identifies applicability, not necessarily model ownership [1][2].
- **Association:** solid actor–use-case line means participation. Usually omit arrowheads; neither line placement nor navigability establishes who acts first.
- **Include:** dashed open-arrow line, `including/base → included`, labeled `«include»`; inserts the included behaviour into the including behaviour [1].
- **Extend:** dashed open-arrow line, `extension → extended/base`, labeled `«extend»`; adds behaviour at extension points, with the base meaningful independently [1].
- **Extension condition:** when absent, extension is unconditional at the relevant points; when present, it governs whether extension occurs. “Extend means optional feature” is therefore misleading [1, §18.2.2].
- **Generalization:** solid line with a hollow triangle, `specific → general`; specialization, not inclusion or temporal order.
- **Optional:** extension points/conditions, package groupings, stable IDs, and links to textual scenarios.
- **Legend/detail:** explain nonstandard annotations and colour; keep peers at comparable goal levels. Formal dashed lines must not be repurposed to mean “inferred.”

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- Start with subject, roles, and useful outcomes; avoid presenting buttons or helper functions as peer goals [1].
- Keep actors as roles: one person may play several, and a role may be played by many people [1][2].
- Add include/extend only after stating the behavioural dependency in words; avoid using them as priority or release markers [1].
- Include supporting external systems where relevant; avoid reducing “actor” to “human user” [3].
- Separate overview and detail views and link scenarios; avoid a dense relationship graph that cannot explain its own behaviour [4].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [OMG UML 2.5.1, Figures 18.3–18.4](https://www.omg.org/spec/UML/2.5.1/PDF) — paired Extend/Include examples distinguish direction and behavioral meaning. **Rights:** no open figure-reuse license established; link only.
- [UML-Diagrams, ticket vending machine example](https://www.uml-diagrams.org/use-case-diagrams-examples.html) — one purchase goal with customer and supporting-system participation shows that a small diagram can be complete. **Rights:** no open image license established; link only.
- [UML-Diagrams, online shopping example](https://www.uml-diagrams.org/examples/online-shopping-use-case-diagram-example.html) — overview and focused checkout/authentication views demonstrate progressive detail. **Rights:** no open image license established; do not trace the figures.

Their specific decompositions are teaching choices, not universal requirements.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix the subject, audience, and current or proposed state.
2. Gather scenario evidence; list external roles and useful outcomes.
3. Name goals with short verb–object phrases; separate detail from overview.
4. Draw actor associations, then justify every include, extend, or generalization.
5. Put actors outside a named subject; group related goals with short, uncrossed links.
6. Keep colour restrained and redundant; place longer explanations in linked scenarios.
7. Walk through success and relevant alternative behaviour; record unknowns separately from formal line styles.

**Self-check**
- [ ] Subject and state are explicit.
- [ ] Actors are external roles at that boundary.
- [ ] Goals have comparable granularity and stakeholder value.
- [ ] Associations are not mistaken for sequence or authorization.
- [ ] Include/extend directions and insertion semantics are correct.
- [ ] Extension conditions and generalizations have supporting evidence.
- [ ] Labels, arrowheads, and scenario references are readable.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Requirements, acceptance tests, and user documentation support candidate goals.
- API handlers, permission checks, and external clients support implemented interactions.
- Endpoints do not establish user value; a shared function does not prove Include; a feature flag does not prove Extend.
- Record `claim | path:line/symbol | revision | verified/inferred/doc-only/conflict`.
- Confirm scope and goals with requirements evidence; distinguish declared permissions from enforced behaviour.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. What is the subject: a business service or a software system?
2. Which external roles and supporting systems participate?
3. Which useful outcomes are in scope?
4. Which scenarios establish normal behaviour and important alternatives?
5. Does the reader need goal coverage, relationship detail, or ordered behaviour?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/B1.json` · Layout template: `nested` · actors are `actor` nodes outside one `boundary` group that holds the use cases as `task` nodes; actor–use-case links are `assoc` edges with `dir` `--`.
Approximate: the renderer draws no UML actor figures, use-case ellipses or include/extend markers, so generic boxes alone do not establish UML conformance.

## Sources {#sources}
<!-- skill: omit -->
1. OMG — *Unified Modeling Language 2.5.1*, Chapter 18, especially §§18.1 and 18.2.2 — https://www.omg.org/spec/UML/2.5.1/PDF — accessed 2026-10-14.
2. UML-Diagrams — *Use Case Diagrams Reference* — https://www.uml-diagrams.org/use-case-reference.html — accessed 2026-10-14.
3. UML-Diagrams — *UML Use Case Diagram Examples* — https://www.uml-diagrams.org/use-case-diagrams-examples.html — accessed 2026-10-14.
4. UML-Diagrams — *Online Shopping Use Case Diagram Example* — https://www.uml-diagrams.org/examples/online-shopping-use-case-diagram-example.html — accessed 2026-10-14.
5. OMG — *About UML 2.5.1* — https://www.omg.org/spec/UML/2.5.1/About-UML — accessed 2026-10-14.

## Sample {#sample}
<!-- skill: path only -->
![B1 sample: use cases of an online shop with shopper and payment provider](/samples/B1-use-case-diagram.svg)
*Use cases of an online shop inside one system boundary: the shopper uses browse catalogue, place order and track order, and the payment provider takes part in pay for order. Actors are stick figures and use cases are ellipses; only associations are drawn, with no include or extend relationships.*
