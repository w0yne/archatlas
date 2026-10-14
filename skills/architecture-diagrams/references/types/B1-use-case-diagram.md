# Use case diagram (用例图)
<!-- Generated from content/en/types/B1-use-case-diagram.md by tools/build_skill_refs.py. Do not edit. -->
> Which valuable outcomes does the subject support, and which external roles participate?
Scope: system Neighbours: A4, B2, B4.

## Meaning
A use case diagram answers **which valuable outcomes a subject supports, and which external roles participate**. Its concern is externally visible behaviour and responsibility boundaries, rather than implementation.
**Definition used here:** OMG UML 2.5.1, Chapter 18. A use case specifies behaviour of a subject that produces an observable result of value to actors or other stakeholders. An actor is an external role, played by a person or another system.
“Place an order” is a useful goal for an online shop; “call a database” is usually an implementation step. A business subject can include manual behaviour, while a software subject has a different boundary.
The diagram omits execution order, detailed exceptions, screen layout, deployment, and access-control enforcement. A *use case model* includes behavioural descriptions beyond the diagram; a story map is a different technique.
UML defines semantics and notation, not a fixed layout, colour palette, or maximum number of ovals. A diagram is an index into behaviour, not a complete requirement specification.

## When to use and how to choose
- **Audience:** analysts, product owners, domain specialists, testers, and developers.
- **Scenarios:** agree an online shop's customer goals; compare shopper and support roles; identify an external payment provider's participation; index acceptance scenarios; distinguish a business service from its supporting software.
- **When not:** precise ordering, data schema, screen navigation, or hosting. A textual scenario may suffice for one simple goal.
- Choose **B2 User story map** for narrative context and incremental delivery slices.
- Choose **B4 Scope diagram** for agreed inclusions/exclusions and **C2 System context** for external systems and exchanges.
- Choose **E1 Sequence diagram** or **E2 Activity/flowchart** for ordered behaviour, branching, and timing.
- Use a companion **textual use case** for preconditions, success behaviour, alternatives, and postconditions; the oval does not contain these details.
- Choose **A4 Business scenario matrix** when the question is which roles take part in which business activities, and in which release, rather than which use cases the system offers.

## Notation and elements
- **Use case:** normally a named ellipse; UML also permits classifier notation. Prefer a short verb–object goal such as “Track order”.
- **Actor:** stick figure or permitted classifier notation; name the external role, not an internal module.
- **Subject:** a named rectangle enclosing applicable use cases is optional UML notation, recommended when scope matters. Enclosure identifies applicability, not necessarily model ownership.
- **Association:** solid actor–use-case line means participation. Usually omit arrowheads; neither line placement nor navigability establishes who acts first.
- **Include:** dashed open-arrow line, `including/base → included`, labeled `«include»`; inserts the included behaviour into the including behaviour.
- **Extend:** dashed open-arrow line, `extension → extended/base`, labeled `«extend»`; adds behaviour at extension points, with the base meaningful independently.
- **Extension condition:** when absent, extension is unconditional at the relevant points; when present, it governs whether extension occurs. “Extend means optional feature” is therefore misleading [1, §18.2.2].
- **Generalization:** solid line with a hollow triangle, `specific → general`; specialization, not inclusion or temporal order.
- **Optional:** extension points/conditions, package groupings, stable IDs, and links to textual scenarios.
- **Legend/detail:** explain nonstandard annotations and colour; keep peers at comparable goal levels. Formal dashed lines must not be repurposed to mean “inferred.”

## Best practices and anti-patterns
- Start with subject, roles, and useful outcomes; avoid presenting buttons or helper functions as peer goals.
- Keep actors as roles: one person may play several, and a role may be played by many people.
- Add include/extend only after stating the behavioural dependency in words; avoid using them as priority or release markers.
- Include supporting external systems where relevant; avoid reducing “actor” to “human user”.
- Separate overview and detail views and link scenarios; avoid a dense relationship graph that cannot explain its own behaviour.

## Drawing recipe
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

## Evidence in a code repository
- Requirements, acceptance tests, and user documentation support candidate goals.
- API handlers, permission checks, and external clients support implemented interactions.
- Endpoints do not establish user value; a shared function does not prove Include; a feature flag does not prove Extend.
- Record `claim | path:line/symbol | revision | verified/inferred/doc-only/conflict`.
- Confirm scope and goals with requirements evidence; distinguish declared permissions from enforced behaviour.

## Guided-mode questions
1. What is the subject: a business service or a software system?
2. Which external roles and supporting systems participate?
3. Which useful outcomes are in scope?
4. Which scenarios establish normal behaviour and important alternatives?
5. Does the reader need goal coverage, relationship detail, or ordered behaviour?

## Template
Model template: `assets/templates/B1.json` · Layout template: `nested` · actors are `actor` nodes outside one `boundary` group that holds the use cases as `task` nodes; actor–use-case links are `assoc` edges with `dir` `--`.
Approximate: the renderer draws no UML actor figures, use-case ellipses or include/extend markers, so generic boxes alone do not establish UML conformance.

## Sample
Figure: `samples/B1-use-case-diagram.svg` (published with the site)
