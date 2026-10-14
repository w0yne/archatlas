---
code: I2
slug: archimate-layered-view
family: I
names:
  en: ArchiMate layered view
  zh: ArchiMate 分层视图
  aliases:
    en: [ArchiMate layered viewpoint, business-application-technology view, cross-layer enterprise view]
    zh: [ArchiMate 分层视点, 业务-应用-技术视图, 跨层企业架构视图]
question: "How do business behaviour, applications and technology support one another, and what is affected by a change?"
audiences: [architects, leaders]
level: logical
phases: [initiate, design]
scope: enterprise
formal:
  kind: standard
  ref: "The Open Group, ArchiMate 3.2 (2022), informative Layered Viewpoint, Appendix C.1.5; https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html"
neighbours: [I1, A7, C8, C1]
status: draft
sourceRev: "2026-10-14"
---

# ArchiMate layered view

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
**Definition used here:** the informative **Layered Viewpoint, Appendix C.1.5 of ArchiMate 3.2**, within a standardized modeling language; it is not the whole language [1].
It explains consistency and change impact across selected enterprise layers: dedicated layers realize services, which serve consumers.
Layer order, number, and nature are flexible. Business/Application/Technology is a common arrangement, not a mandatory three-band template [1].
It leaves out detailed execution timing and code dependencies. It is not TOGAF BDAT: ArchiMate models information through passive elements across layers, not a separate core data layer [2][8].
This page targets **3.2 explicitly**. ArchiMate 4 was released in April 2026; do not assume these version-specific rules describe that edition [9].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** enterprise, business, application, and technology architects; leaders reviewing a bounded support chain.
- **Change impact:** identify shop operations depending on a technology service.
- **Shared services:** show applications supporting checkout and returns.
- **Consolidation:** compare the shop's baseline and target support chains.
- **Service review:** find a support chatbot service without a known consumer or realization.
- **Do not use:** detailed request order, API payloads, exhaustive inventory, or inferred business structure without domain evidence.
- Choose Application Usage or Technology Usage for a narrower dependency slice; Service Realization for implementation behavior; Implementation and Deployment for artifact allocation [1].
- Choose **C8** for code-layer dependencies, **A7** for informal conceptual bands, **C1** for a system portfolio, or **I1** for organizing several software views.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required by this recipe:** scope, typed elements, meaningful cross-layer relations, and a legend. No fixed element inventory is mandatory.
- Select actors/roles, processes/functions, components, services, and nodes as needed; information objects, interfaces, artifacts, and internal detail are optional [3].
- **Serving:** provider → consumer; solid line/open arrowhead. It expresses supplied functionality, not request direction.
- **Realization:** concrete → abstract; dashed line/hollow triangle. A function realizes a service; an artifact realizes a component.
- **Assignment:** performer/host → behavior/artifact; solid line, source dot, filled target arrowhead. Example: Node → Artifact.
- **Deployment:** `Node —Assignment→ Artifact —Realization→ Application Component`; “hosted-on” is not a generic ArchiMate relationship [3][5].
- **Access** represents reading/writing passive structure; **Triggering** represents temporal/causal dependency; **Flow** represents transfer. Use their distinct standard glyphs [3].
- Validate source/relation/target combinations and derived shortcuts against the metamodel and normative Appendix B. Selecting all core relationship types does not legalize every pair [4].
- Name structure with nouns and behavior with actions. Explain nesting; a background band alone establishes no relationship.
- Yellow/blue/green are optional conventions, with no formal color semantics [2].
- Keep uncertainty in evidence annotations or a table. Never repurpose formal dashed lines as “inferred.”

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- Select one bounded concern; avoid an enterprise inventory on one page [1].
- Separate performers, behavior, services, and consumers; avoid unlabeled “supports” lines [3][10].
- Preserve standard direction; avoid reversing Serving to resemble an API request [10].
- Validate exact relation pairs; avoid arbitrary cross-layer realization or generic hosting arrows [4][5].
- Keep comparable groups consistent and color redundant; avoid fixed layer counts or color-only typing [1][2].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Open Group, C.1.5, example associated with Table 27](https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html) — the canonical dedicated-layer/service-layer arrangement, expressly non-prescriptive. **License:** no open image-reuse permission established; link only; official HTML may require sign-in.
- [Open Group, Chapter 11, Example 34](https://pubs.opengroup.org/architecture/archimate3-doc/ch-Relationships-Between-Core-Layers.html) — a concrete cross-layer example using optional letter markers for layers. It is related guidance, not another named Layered Viewpoint. **License:** no image-reuse permission established; link only.
- [Visual Paradigm, “Layered Viewpoint Example” figure](https://circle.visual-paradigm.com/docs/archimate/archimate-viewpoints/archimate-viewpoint-layered-viewpoint/) — connects a specific diagram with its stakeholder concerns; the page cites **3.1**, not 3.2. **License:** no open image license verified; link only.
- [Open Group certification evidence, §2.11 Layered Viewpoint](https://certification.opengroup.org/register/archimate/orbus_archimate3_tool_se2.pdf) — a tool-rendered sample alongside focused views; a **3.1** submission, not proof of 3.2 conformance. **License:** public certification hosting grants no assumed reuse rights; link only.

Examples were identified through text and indexed excerpts; images were not visually reviewed. Tool examples may share the standard's illustrative model and are not claimed as independent case studies. Check rights before adapting artwork; author fresh scenarios instead of copying figures.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix the concern, boundary, baseline/target state, and ArchiMate version.
2. Inventory evidenced business behavior, application services, and technology support.
3. Assign exact types and validate relationships before arranging boxes.
4. Align providers and consumers in useful bands; business above application above technology is optional.
5. Use short names, type icons, sparse color, and service bands where helpful.
6. Preserve arrow direction and glyphs; explain nesting and annotate evidence separately.
7. Trace a checkout concern through the chain; split dense detail into focused views.
8. Review semantic validity and readability; an informal renderer output needs an explicit label.

**Self-check**
- [ ] Scope and version are explicit.
- [ ] Components, behavior, and services are distinct.
- [ ] Every relationship is permitted for its endpoint types.
- [ ] Serving and Realization point in the correct directions.
- [ ] Deployment uses artifact/allocation semantics.
- [ ] Layer count and color are not treated as normative.
- [ ] Evidence status does not alter formal line styles.
- [ ] Labels, glyphs, and endpoints remain readable.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Components/behavior: implementation responsibilities, handlers, entry points, build boundaries.
- Services/consumers: interface contracts, clients, configuration, and integration tests.
- Artifacts/allocation: build outputs, image references, deployment manifests, and infrastructure definitions.
- Information: schemas and read/write code; names alone do not establish business meaning.
- Business roles/processes/services: validated requirements and domain documentation; code is insufficient.
- Record commit, path/symbol, relation types, and confidence. Configuration does not prove live state.
- Use evidence annotations, not automatic inference dashes; metamodel validity and factual evidence are separate checks.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which business service or change should the view explain, and to whom?
2. Which boundary and baseline or target state apply?
3. Which business facts are established rather than inferred?
4. Is the concern service support, realization, deployment, or several focused views?
5. Do readers need formal ArchiMate 3.2 or an explicitly informal overview?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Integration target: `assets/templates/I2.json`, layout `layered`; the model template is not yet provided.
A layered layout does not implement formal ArchiMate glyphs or validate its metamodel; formal output needs those capabilities checked separately.

## Sources {#sources}
<!-- skill: omit -->
1. The Open Group, *ArchiMate 3.2 — Example Viewpoints*, C.1.5/Table 27 — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html — accessed 2026-10-14; indexed official excerpts.
2. The Open Group, *ArchiMate 3.2 — Language Structure* — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Language-Structure.html — accessed 2026-10-14; indexed official excerpts.
3. The Open Group, *ArchiMate 3.2 Specification Reference Cards*, N221 (2022) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — accessed 2026-10-14; complete PDF text extracted.
4. The Open Group, *ArchiMate 3.2 — Relationships (Normative)*, Appendix B — https://pubs.opengroup.org/architecture/archimate3-doc/ch-relationships-Normative.html — accessed 2026-10-14; indexed excerpts, not complete relationship tables.
5. The Open Group, *ArchiMate 3.2 — Relationships between Core Layers*, including Example 34 — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Relationships-Between-Core-Layers.html — accessed 2026-10-14; indexed official excerpts.
6. Visual Paradigm, *ArchiMate Viewpoint: Layered Viewpoint* — https://circle.visual-paradigm.com/docs/archimate/archimate-viewpoints/archimate-viewpoint-layered-viewpoint/ — accessed 2026-10-14; extracted page text cites 3.1.
7. *ArchiMate 3.1 Tool — Orbus Software — Tool Certification Supporting Evidence*, §2.11 — https://certification.opengroup.org/register/archimate/orbus_archimate3_tool_se2.pdf — accessed 2026-10-14; PDF text extracted.
8. The Open Group, *TOGAF Standard — Establishing an Architecture Capability*, §2.1 — https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap02.html — accessed 2026-10-14; indexed official description of BDAT domains.
9. The Open Group, *ArchiMate Licensed Downloads* — https://www.opengroup.org/archimate-licensed-downloads — accessed 2026-10-14; extracted official confirmation of version 4, released April 2026.
10. Bizzdesign, *ArchiMate Relationships Point in the Same Direction as the Enterprise* — https://bizzdesign.com/blog/archimate-relationships-point-same-direction-enterprise — accessed 2026-10-14; extracted explanation of relationship directions.

**Access limits:** direct extraction of the 3.2 viewpoint chapter still failed on recheck. Definitions combine indexed official text with the accessible 3.2 reference cards. Complete Appendix B tables and visual glyphs were not independently audited; validate a concrete formal model against the full 3.2 rules.

## Sample {#sample}
<!-- skill: path only -->
Expected sample: `/samples/I2-archimate-layered-view.svg` — not yet provided. Caption: an online shop's checkout behavior, application services, and technology support, with explicit relationship types.
