---
code: B3
slug: feature-tree
family: B
names:
  en: Feature tree (functional decomposition)
  zh: 功能树（功能分解）
  aliases:
    en: [functional decomposition, requirements breakdown structure, feature breakdown]
    zh: [需求树, 功能分解图, 需求分解结构, 特性树, 功能特性树]
question: What must the product do, and how is that functionality decomposed?
audiences: [product, developers]
levels: [concept]
phases: [requirements]
scope: system
formal: {kind: convention, ref: 'Functional hierarchy — https://sebokwiki.org/wiki/Logical_Architecture; variability mode uses FeatureIDE conventions'}
neighbours: [B2, C5]
status: draft
sourceRev: '2026-10-14'
---

# Feature tree and functional decomposition (功能树（功能分解）)

> The product's functions decomposed top-down to estimable leaves, with priorities; no flow and no code structure.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A functional hierarchy answers **what the system must do and how that overall function decomposes**. Its concern is functional coverage, not execution order or source-code structure [1][2].
**Definition used here:** B3 defaults to an informal functional breakdown of product features (business capabilities belong in A1). Requirements decomposition is a related traceability mode; a software-product-line *feature model* is a separate variability mode defining valid feature selections [3–5].
For an online shop, “Fulfil order” can decompose into functions. A configurable product's delivery options instead need selection rules and constraints. A plain tree does not make these meanings interchangeable.
A static hierarchy leaves out input/output behaviour, runtime sequence, physical allocation, and proof of quality requirements. NASA and SEBoK describe iterative analysis with complementary behaviour/interface views [1][2].
MoSCoW is an optional priority annotation, not tree syntax; “Won't Have” means *this time*. No universal depth or estimable-leaf rule applies [6].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** product analysts, systems engineers, architects, testers, and product-line engineers.
- **Scenarios:** decompose an online shop's overall function; review functional coverage; trace needs to lower-level requirements; define supported shop editions; check whether configurable delivery options conflict.
- **When not:** proving workflow correctness, capacity, or interface completeness; listing folders without functional analysis.
- Choose **B2 User story map** for narrative/release slices and **E2 Activity/flowchart** for behaviour.
- Choose **C5 Logical architecture** for collaborating responsibilities rather than a function inventory.
- A **WBS** decomposes work/deliverables; a **module tree** decomposes implementation; neither is automatically a function tree.
- Use a requirement graph/matrix when shared or crosscutting requirements make a strict tree misleading.
- Select **variability mode** only when valid combinations, rather than functional coverage or priority, are the question.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Functional mode:** named root/scope, function nodes, and declared “decomposes into” links; prefer verb–object labels [1][2].
- **Requirements mode:** stable IDs and linked testable statements; explain whether a link means refinement, derivation, or coverage. A position below a parent does not prove logical derivation.
- **Tree connectors:** usually undirected lines; if directed parent → child, they mean decomposition, not execution or data transfer.
- **Optional:** priorities, releases, ownership, verification references, and evidence tags; separate these from structural meaning.
- **Variability mode:** declare its language/tool. In FeatureIDE's Boolean conventions, selecting a child requires its parent [4][5].
- **Mandatory/optional children:** under AND groups, filled/empty circle markers express whether selecting the parent requires the child; neither marker is a priority.
- **OR/XOR groups:** when the parent is selected, choose at least one/exactly one grouped child; use the documented filled/unfilled group arcs.
- **Cross-tree constraints:** write rules such as `A ⇒ B` or `¬(A ∧ B)` explicitly; they are not decomposition arrows.
- **Validation:** analyse satisfiability, dead features, and false-optional features; other constraints can force a nominally optional feature [7].
- **Legend and detail:** explain the selected mode, group markers, annotations, and any directed lines; align sibling granularity. Quality constraints may cross branches.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- Choose a modeling mode first; avoid calling every feature list a formal feature model [3–5].
- Keep sibling kinds and decomposition rationale consistent; avoid mixing functions, modules, and project tasks in one group [1][2].
- Iterate with behaviour and interface analysis; avoid treating static decomposition as proof that exchanges work [1][2].
- Preserve requirement provenance and crosscutting constraints; avoid duplicate requirements that drift or quality needs hidden in an unrelated branch.
- Analyse the full variability model and keep priority separate; avoid declaring a configuration valid merely because its tree looks plausible [5–7].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [SEBoK, Logical Architecture, Figure 1](https://sebokwiki.org/wiki/Logical_Architecture) — a concrete functional hierarchy demonstrates decomposition and the limits of static structure. **Rights:** the figure credits Faisandier/Sinergy'Com with other rights reserved; link only.
- [FeatureIDE, Hello World tutorial](https://github.com/FeatureIDE/FeatureIDE/wiki/Tutorial) — connects a feature model with configurations and resulting products. **Rights:** no per-figure license established; the software license is not blanket permission for wiki images.
- [FeatureIDE: Background, GraphLibrary model, slide 7](https://featureide.github.io/slides/featureide-0-background.pdf) — group types plus `Cycle ⇒ Directed` show why cross-tree constraints matter. **Rights:** no slide-image reuse license established; do not trace.

These illustrate different modeling modes, not synonyms.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Select functional, requirements or variability mode and name it.
2. Establish the root, boundary, audience, baseline, and source evidence.
3. Normalize node kinds/names; justify each parent–child relation.
4. Keep shared requirements and quality constraints as explicit cross-links or a table.
5. For variability, declare the notation and validate group/cross-tree constraints.
6. Lay out top-down or left-to-right with aligned siblings, short labels, sparse colour, and a legend.
7. Stop at decision-useful detail; use a focused subview rather than omit significant constraints.

**Self-check**
- [ ] Mode, root, and boundary are explicit.
- [ ] Sibling kinds and granularity are consistent.
- [ ] Decomposition, traceability, and selection constraints remain distinct.
- [ ] Quality constraints and requirement provenance are preserved.
- [ ] Priority does not masquerade as mandatory/optional selection.
- [ ] Variability constraints and feature anomalies were checked when applicable.
- [ ] Labels, markers, cross-links, and evidence are readable.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Requirements, acceptance tests, and product docs support functional coverage.
- Handlers and interfaces support implemented responsibilities; directories do not define functions.
- Feature-model files, build profiles, validators, and configuration tests support variability claims.
- A Boolean flag alone does not define a complete product-line feature model.
- Record `element/relation | path:line/model ID | revision | verified/inferred/doc-only/conflict`.
- Approved scope, derivation rationale, and priority need requirements/decision evidence beyond code.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Are we organising functions, tracing requirements, or defining valid configurations?
2. What is the root scope and current or proposed baseline?
3. Which requirements or model files are authoritative?
4. Which dependencies or quality constraints cross the hierarchy?
5. What decision should the leaf detail support, and is priority relevant?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/B3.json` · Layout template: `tree` · the root is a `system` node and features are `component` and `task` nodes linked by `edges` from parent to child, laid out top to bottom.
Functional decomposition only: variability mode (group markers, constraints, semantic validation) is not supported.

## Sources {#sources}
<!-- skill: omit -->
1. NASA — *4.3 Logical Decomposition* — https://www.nasa.gov/reference/4-3-logical-decomposition/ — accessed 2026-10-14.
2. SEBoK — *Logical Architecture* — https://sebokwiki.org/wiki/Logical_Architecture — accessed 2026-10-14.
3. Kang et al., CMU SEI — *Feature-Oriented Domain Analysis (FODA) Feasibility Study*, CMU/SEI-90-TR-021 (1990) — https://www.sei.cmu.edu/library/feature-oriented-domain-analysis-foda-feasibility-study/ — accessed 2026-10-14.
4. FeatureIDE — *Getting Started tutorial* — https://github.com/FeatureIDE/FeatureIDE/wiki/Tutorial — accessed 2026-10-14.
5. FeatureIDE — *FeatureIDE: Background*, slide 7 (2015) — https://featureide.github.io/slides/featureide-0-background.pdf — accessed 2026-10-14.
6. Agile Business Consortium — *What is MoSCoW Prioritization?* — https://www.agilebusiness.org/resource/what-is-moscow-prioritization/ — accessed 2026-10-14.
7. FeatureIDE — *Feature Diagram* — https://github.com/FeatureIDE/FeatureIDE/wiki/Feature-Diagram — accessed 2026-10-14.

## Sample {#sample}
<!-- skill: path only -->
![B3 sample: feature tree of an online shop](/samples/B3-feature-tree.svg)
*An online shop's functions decompose into browsing, ordering, and fulfilment, with detailed functions grouped under each. This is a functional hierarchy, not a variability model.*
