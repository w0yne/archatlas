# ArchiMate layered view (ArchiMate 分层视图)
<!-- Generated from content/en/types/I2-archimate-layered-view.md by tools/build_skill_refs.py. Do not edit. -->
> How do business behaviour, applications and technology support one another, and what is affected by a change?
Scope: enterprise Neighbours: A7, C1, C8, I1.
Method reference: honour explicit requests; outside the default core catalogue.

## Meaning
**Definition used here:** the informative **Layered Viewpoint, Appendix C.1.5 of ArchiMate 3.2**, within a standardized modeling language; it is not the whole language.
It explains consistency and change impact across selected enterprise layers: dedicated layers realize services, which serve consumers.
Layer order, number, and nature are flexible. Business/Application/Technology is a common arrangement, not a mandatory three-band template.
It leaves out detailed execution timing and code dependencies. It is not TOGAF BDAT: ArchiMate models information through passive elements across layers, not a separate core data layer.
This page targets **3.2 explicitly**. ArchiMate 4 was released in April 2026; do not assume these version-specific rules describe that edition.

## When to use and how to choose
- **Audience:** enterprise, business, application, and technology architects; leaders reviewing a bounded support chain.
- **Change impact:** identify shop operations depending on a technology service.
- **Shared services:** show applications supporting checkout and returns.
- **Consolidation:** compare the shop's baseline and target support chains.
- **Service review:** find a support chatbot service without a known consumer or realization.
- **Do not use:** detailed request order, API payloads, exhaustive inventory, or inferred business structure without domain evidence.
- Choose Application Usage or Technology Usage for a narrower dependency slice; Service Realization for implementation behaviour; Implementation and Deployment for artifact allocation.
- Choose **C8** for code-layer dependencies, **A7** for informal conceptual bands, **C1** for a system portfolio, or **I1** for organising several software views.

## Notation and elements
- **Required by this recipe:** scope, typed elements, meaningful cross-layer relations, and a legend. No fixed element inventory is mandatory.
- Select actors/roles, processes/functions, components, services, and nodes as needed; information objects, interfaces, artifacts, and internal detail are optional.
- **Serving:** provider → consumer; solid line/open arrowhead. It expresses supplied functionality, not request direction.
- **Realization:** concrete → abstract; dashed line/hollow triangle. A function realizes a service; an artifact realizes a component.
- **Assignment:** performer/host → behaviour/artifact; solid line, source dot, filled target arrowhead. Example: Node → Artifact.
- **Deployment:** `Node —Assignment→ Artifact —Realization→ Application Component`; “hosted-on” is not a generic ArchiMate relationship.
- **Access** represents reading/writing passive structure; **Triggering** represents temporal/causal dependency; **Flow** represents transfer. Use their distinct standard glyphs.
- Validate source/relation/target combinations and derived shortcuts against the metamodel and normative Appendix B. Selecting all core relationship types does not legalize every pair.
- Name structure with nouns and behaviour with actions. Explain nesting; a background band alone establishes no relationship.
- Yellow/blue/green are optional conventions, with no formal colour semantics.
- Keep uncertainty in evidence annotations or a table. Never repurpose formal dashed lines as “inferred.”

## Best practices and anti-patterns
- Select one bounded concern; avoid an enterprise inventory on one page.
- Separate performers, behaviour, services, and consumers; avoid unlabeled “supports” lines.
- Preserve standard direction; avoid reversing Serving to resemble an API request.
- Validate exact relation pairs; avoid arbitrary cross-layer realization or generic hosting arrows.
- Keep comparable groups consistent and colour redundant; avoid fixed layer counts or colour-only typing.

## Drawing recipe
1. Fix the concern, boundary, baseline/target state, and ArchiMate version.
2. Inventory evidenced business behaviour, application services, and technology support.
3. Assign exact types and validate relationships before arranging boxes.
4. Align providers and consumers in useful bands; business above application above technology is optional.
5. Use short names, type icons, sparse colour, and service bands where helpful.
6. Preserve arrow direction and glyphs; explain nesting and annotate evidence separately.
7. Trace a checkout concern through the chain; split dense detail into focused views.
8. Review semantic validity and readability; an informal renderer output needs an explicit label.

**Self-check**
- [ ] Scope and version are explicit.
- [ ] Components, behaviour, and services are distinct.
- [ ] Every relationship is permitted for its endpoint types.
- [ ] Serving and Realization point in the correct directions.
- [ ] Deployment uses artifact/allocation semantics.
- [ ] Layer count and colour are not treated as normative.
- [ ] Evidence status does not alter formal line styles.
- [ ] Labels, glyphs, and endpoints remain readable.

## Evidence in a code repository
- Components/behaviour: implementation responsibilities, handlers, entry points, build boundaries.
- Services/consumers: interface contracts, clients, configuration, and integration tests.
- Artifacts/allocation: build outputs, image references, deployment manifests, and infrastructure definitions.
- Information: schemas and read/write code; names alone do not establish business meaning.
- Business roles/processes/services: validated requirements and domain documentation; code is insufficient.
- Record commit, path/symbol, relation types, and confidence. Configuration does not prove live state.
- Use evidence annotations, not automatic inference dashes; metamodel validity and factual evidence are separate checks.

## Guided-mode questions
1. Which business service or change should the view explain, and to whom?
2. Which boundary and baseline or target state apply?
3. Which business facts are established rather than inferred?
4. Is the concern service support, realization, deployment, or several focused views?
5. Do readers need formal ArchiMate 3.2 or an explicitly informal overview?

## Template
Model template: `assets/templates/I2.json` · Layout template: `layered` · business, application and technology are `layer` groups; relationship types are edge labels with kind `dependency` or `assoc`.
Approximate: no formal ArchiMate glyphs and no metamodel validation; formal output needs those capabilities checked separately.

## Sample
Figure: `samples/I2-archimate-layered-view.svg` (published with the site)
