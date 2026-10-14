# Feature tree and functional decomposition
<!-- Generated from content/en/types/B3-feature-tree.md by tools/build_skill_refs.py. Do not edit. -->
> What must the product do, and how is that functionality decomposed?
Scope: system Neighbours: B2, B1, C5, E2.

## Meaning
A functional hierarchy answers **what the system must do and how that overall function decomposes**. Its concern is capability coverage, not execution order or source-code structure.
**Definition used here:** B3 defaults to an informal functional/capability breakdown. Requirements decomposition is a related traceability mode; a software-product-line *feature model* is a separate variability mode defining valid feature selections.
For an online shop, “Fulfil order” can decompose into functions. A configurable product's delivery options instead need selection rules and constraints. A plain tree does not make these meanings interchangeable.
A static hierarchy leaves out input/output behavior, runtime sequence, physical allocation, and proof of quality requirements. NASA and SEBoK describe iterative analysis with complementary behavior/interface views.
MoSCoW is an optional priority annotation, not tree syntax; “Won't Have” means *this time*. No universal depth or estimable-leaf rule applies.

## When to use and how to choose
- **Audience:** product analysts, systems engineers, architects, testers, and product-line engineers.
- **Scenarios:** decompose an online shop's overall function; review capability coverage; trace needs to lower-level requirements; define supported shop editions; check whether configurable delivery options conflict.
- **When not:** proving workflow correctness, capacity, or interface completeness; listing folders without functional analysis.
- Choose **B2 User story map** for narrative/release slices and **E2 Activity/flowchart** for behavior.
- Choose **C5 Logical architecture** for collaborating responsibilities rather than a function inventory.
- A **WBS** decomposes work/deliverables; a **module tree** decomposes implementation; neither is automatically a function tree.
- Use a requirement graph/matrix when shared or crosscutting requirements make a strict tree misleading.
- Select **variability mode** only when valid combinations, rather than capability coverage or priority, are the question.

## Notation and elements
- **Functional mode:** named root/scope, function nodes, and declared “decomposes into” links; prefer verb–object labels.
- **Requirements mode:** stable IDs and linked testable statements; explain whether a link means refinement, derivation, or coverage. A position below a parent does not prove logical derivation.
- **Tree connectors:** usually undirected lines; if directed parent → child, they mean decomposition, not execution or data transfer.
- **Optional:** priorities, releases, ownership, verification references, and evidence tags; separate these from structural meaning.
- **Variability mode:** declare its language/tool. In FeatureIDE's Boolean conventions, selecting a child requires its parent.
- **Mandatory/optional children:** under AND groups, filled/empty circle markers express whether selecting the parent requires the child; neither marker is a priority.
- **OR/XOR groups:** when the parent is selected, choose at least one/exactly one grouped child; use the documented filled/unfilled group arcs.
- **Cross-tree constraints:** write rules such as `A ⇒ B` or `¬(A ∧ B)` explicitly; they are not decomposition arrows.
- **Validation:** analyze satisfiability, dead features, and false-optional features; other constraints can force a nominally optional feature.
- **Legend and detail:** explain the selected mode, group markers, annotations, and any directed lines; align sibling granularity. Quality constraints may cross branches.

## Best practices and anti-patterns
- Choose a modeling mode first; avoid calling every feature list a formal feature model.
- Keep sibling kinds and decomposition rationale consistent; avoid mixing functions, modules, and project tasks in one group.
- Iterate with behavior and interface analysis; avoid treating static decomposition as proof that exchanges work.
- Preserve requirement provenance and crosscutting constraints; avoid duplicate requirements that drift or quality needs hidden in an unrelated branch.
- Analyze the full variability model and keep priority separate; avoid declaring a configuration valid merely because its tree looks plausible.

## Drawing recipe
1. Select functional, requirements, capability, or variability mode and name it.
2. Establish the root, boundary, audience, baseline, and source evidence.
3. Normalize node kinds/names; justify each parent–child relation.
4. Keep shared requirements and quality constraints as explicit cross-links or a table.
5. For variability, declare the notation and validate group/cross-tree constraints.
6. Lay out top-down or left-to-right with aligned siblings, short labels, sparse color, and a legend.
7. Stop at decision-useful detail; use a focused subview rather than omit significant constraints.

**Self-check**
- [ ] Mode, root, and boundary are explicit.
- [ ] Sibling kinds and granularity are consistent.
- [ ] Decomposition, traceability, and selection constraints remain distinct.
- [ ] Quality constraints and requirement provenance are preserved.
- [ ] Priority does not masquerade as mandatory/optional selection.
- [ ] Variability constraints and feature anomalies were checked when applicable.
- [ ] Labels, markers, cross-links, and evidence are readable.

## Evidence in a code repository
- Requirements, acceptance tests, and product docs support functional coverage.
- Handlers and interfaces support implemented responsibilities; directories do not define functions.
- Feature-model files, build profiles, validators, and configuration tests support variability claims.
- A Boolean flag alone does not define a complete product-line feature model.
- Record `element/relation | path:line/model ID | revision | verified/inferred/doc-only/conflict`.
- Approved scope, derivation rationale, and priority need requirements/decision evidence beyond code.

## Guided-mode questions
1. Are we organizing functions, tracing requirements, or defining valid configurations?
2. What is the root scope and current or proposed baseline?
3. Which requirements or model files are authoritative?
4. Which dependencies or quality constraints cross the hierarchy?
5. What decision should the leaf detail support, and is priority relevant?

## Template
Model template: `assets/templates/B3.json` · Layout template: `tree` · the root is a `system` node and features are `component` and `task` nodes linked by `edges` from parent to child, laid out top to bottom.
Functional decomposition only: variability mode (group markers, constraints, semantic validation) is not supported.

## Sample
Figure: `samples/B3-feature-tree.svg` (published with the site)
