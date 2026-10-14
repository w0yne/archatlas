---
code: A4
slug: scenario-matrix
family: A
names:
  en: Business Scenario Matrix (Role × Activity)
  zh: 业务场景矩阵（角色 × 业务活动）
  aliases:
    en: [scenario coverage matrix, role–activity scope matrix, actor–goal matrix]
    zh: [业务场景地图, 场景覆盖矩阵, 业务场景清单, 角色-场景矩阵]
question: "For each role, which business activities does the solution support, through which scenarios, in which release, and which combinations are deliberately left out?"
audiences: [business owners, product managers, programme or project managers, business analysts, architects]
level: concept
phases: [discovery, planning, review]
scope: "One solution or business area: 4–8 roles × 4–8 business activities, with scenarios and a release marker per cell."
formal:
  kind: convention
  ref: "none (table convention; cell content follows Cockburn's user-goal level)"
neighbours: [B1, B2, A6, A1, A2, H1]
status: draft
---

# Business Scenario Matrix (业务场景矩阵)

> Roles down the side, business activities across the top, and in each cell the scenarios the solution supports and when.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** for each role, which business activities does the solution support, through which concrete scenarios, and in which release? Equally: which role × activity combinations are **deliberately not covered**?
- **Concern:** functional scope and phasing for business and product stakeholders (ISO/IEC/IEEE 42010 concerns [13]). It is a **scope contract at user-goal level**: gaps, overlaps and phasing show at a glance, which a flat backlog hides [10]. Architects use it to pick the scenarios for the "+1" view of Kruchten's 4+1 model [14].
- **Left out on purpose:** step order (A5, E-family), UI, data, technical design, emotions (A6) and value-stage flow (A2).
- **Definition used here:** "business scenario map" is not an established English diagram term. This page means an informal role × activity coverage matrix. It is **not** a TOGAF *Business Scenario* (a requirements technique that yields a document: problem, environment, objectives, actors, results) [1][2][3], not an IBM *scenario map* (a journey-map variant, see A6) [4], not a foresight 2×2 scenario matrix [5], and not the SAP "business scenario" process level [6].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** business owners, product and project managers, business analysts; architects selecting key scenarios.
- **Scenarios:** release-1 scope workshop for the online shop (customer, support agent, warehouse clerk, finance × browse, order, pay, fulfil, return); release review that exposes a gap in returns (e.g. "Track return via support chatbot" planned only for R2); choosing 5–8 architecturally significant scenarios for a review [14]; acceptance planning, where each covered cell becomes an end-to-end test.
- **When not to use:** one role only (B2 or A6); when the question is *how* a scenario flows (A5, E4); items below user-goal level (clicks, fields); when nobody will decide phasing (the grid becomes a wish list).
- **vs neighbours:**
  - Choose **B1 Use Case Diagram** for a formal, developer-facing list of actor goals with a system boundary and include/extend; it is weak at showing phasing and gaps [9].
  - Choose **B2 User Story Map** for delivery planning along **one user's narrative** at story level with release slices; choose A4 for many roles at business-activity level [10][11].
  - Choose **A6 Journey Map** for one persona's experience over time; A4 has no time axis and no emotion.
  - Choose **A1 Capability Map** for what the business can do regardless of roles or releases.
  - Choose **H1 RACI Matrix** when cells must hold responsibility (R/A/C/I), not supported scenarios.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
No standard exists; these conventions come from use-case and story-mapping practice [7][8][10][11].

- **Rows = roles** of one kind (business roles; no named people, no systems). External systems are at most a note.
- **Columns = business activities** at one level, in narrative or value order left → right: value-stream stages (A2), level-1/2 capabilities (A1) or story-map backbone activities [10][11].
- **Cells:** 0–3 scenario phrases, each **verb + object at user-goal level**. Cockburn's test: can the primary actor "go away happy" after it? [7][8]
- **Release marker** on every scenario (R1/R2/R3 or MVP/Next/Later) by fill, tag or both, with a legend.
- **Empty cells have two meanings, both in the legend:** blank = not applicable; hatched or "—" = in business scope but deliberately not supported.
- **Lines:** none. A cross-role hand-off is an A5/E4 question.
- **Optional:** row groups (customers / staff / partners), column bands by stage, a marker for architecturally significant scenarios, scenario IDs, a count per release.
- **Size:** about 4–8 × 4–8; ≤ 3 phrases of ≤ 6 words per cell. Larger means split by business area.
- **Naming:** roles as singular nouns ("Support agent"), activities as verb–noun stages ("Pay order"), scenarios as active goals ("Pay with saved card").

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices

1. **Fix the goal level first.** Keep cells at user-goal level; push subfunctions into use cases [7][8].
2. **Breadth before depth.** Settle the goal list before writing detail; the matrix is that breadth-first artefact [7][8].
3. **Order columns as a narrative**, so readers can walk it like a story-map backbone [10][11].
4. **Give every cell a release decision**, including "not planned". Release 1 should cover the primary role end to end, like a walking skeleton [10][12].
5. **Trace upward:** each scenario supports a stated business objective [1][2]; mark drawer-proposed scenarios as proposed.

### Anti-patterns

1. Cells mixing epics ("Manage orders") with clicks ("Upload photo") [8].
2. No release markers, so the grid reads as an unbounded wish list.
3. Rows mixing roles, departments, named people and systems.
4. Columns that are system modules or menus, which turns the matrix into a feature list (use B3 or A1).
5. Calling it a "scenario map" in English without a definition; readers expect a TOGAF Business Scenario, a journey map or a foresight 2×2 [1][4][5].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Jeff Patton — The New User Story Backlog Is a Map](https://jpattonassociates.com/the-new-backlog/) — backbone, walking skeleton and release slices; the model for column order and release lines.
- [NN/g — Mapping User Stories in Agile](https://www.nngroup.com/articles/user-story-mapping/) — clear anatomy of activities, steps and details.
- [The Open Group — TOGAF 7 Business Scenarios (public text)](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/bus_scen/bus_scen.htm) — what a TOGAF business scenario formally is, to avoid the name clash (© The Open Group).
- [TOGAF 9 — Business Use-Case Diagram artifact](https://pubs.opengroup.org/architecture/togaf90-doc/epf/TOGAF9/workproducts/Business%20Use-Case%20Diagram_74D9B44D.html) — the formal graphical neighbour (B1).
- [P. Kruchten — The "4+1" View Model of Software Architecture](https://arxiv.org/pdf/2006.04975) — why a scenario catalogue matters to architecture.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix scope (solution or business area, as-is / to-be) and the release vocabulary.
2. Pick one column source (value-stream stages, capabilities or backbone activities); 4–8 columns in narrative order.
3. List 4–8 roles as rows, grouped external / internal, primary role on top.
4. Write 0–3 scenarios per cell, verb + object at user-goal level; merge or reject summary and subfunction items.
5. Assign each scenario a release; hatch deliberately unsupported cells, leave not-applicable cells blank.
6. Layout: landscape grid, bold header row and header column, optional thin column bands by stage, no arrows.
7. Colour: one sequential scale for releases (darkest = R1) or 3 distinct fills; neutral grey hatch for "not supported"; outline marker for significant scenarios; legend bottom-right.
8. Text budget: ≤ 6 words per scenario, ≤ 3 per cell; optional footer with counts per release.

**Self-check**

- [ ] All rows are roles of one kind: no systems, no named people.
- [ ] All columns are business activities at one level, in narrative order.
- [ ] Every scenario is verb + object at user-goal level; no clicks, no epics.
- [ ] Every scenario has a release marker; the legend explains every fill, hatch and blank.
- [ ] Release 1 covers the primary role end to end.
- [ ] No step sequences, UI or technical terms in cells.
- [ ] The title states scope and as-is / to-be, and does not use the bare term "scenario map".
- [ ] The grid fits about 8 × 8, or is split by business area.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **From code (as-is grid):** roles from RBAC definitions, permission enums and seed data; activities and scenarios from routes, menus, API operation IDs, analytics events, BDD `*.feature` files and acceptance-test names; release hints from feature flags, milestones and epic labels; README feature lists and ADRs for context.
- **Limit:** target scope, release assignment of planned scenarios, the business-activity columns and deliberate exclusions come from people. Mark cells "observed in code" or "proposed".

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Agree scope and phasing across several roles (this matrix), plan one user's flow in story slices (B2), or show formal use cases (B1)? (This matrix.)
2. What are the columns: value-stream stages, capabilities, or main activities in user order? (Main activities in user order.)
3. Which roles are rows; should external parties such as customers and partners be included? (Yes, grouped separately.)
4. Which release labels, and should "not supported" differ from "not applicable"? (R1/R2/R3; yes.)
5. Mark the 5–8 scenarios that drive architecture decisions? (Yes.)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A4.json` · Layout template: `grid_table` · One `tables[]` entry: row headers are roles, column headers are activities, and each cell holds scenario items with a release tag and an optional significance flag.

## Sources {#sources}
<!-- skill: omit -->
1. The Open Group — TOGAF Standard 10, "Business Scenarios" — https://pubs.opengroup.org/togaf-standard/business-architecture/business-scenarios.html — accessed 2026-10-14 (login-gated; not verified against the current spec text)
2. The Open Group — TOGAF 7 "Business Scenarios" (public) — https://www.opengroup.org/architecture/togaf7-doc/arch/p4/bus_scen/bus_scen.htm — accessed 2026-10-14
3. The Open Group — "TOGAF Series Guide: Business Scenarios" (G176) — https://publications.opengroup.org/g176 — accessed 2026-10-14
4. Carrier Management — "Design Thinking Basics" (IBM as-is / to-be scenario maps) — https://www.carriermanagement.com/features/2020/05/08/206437.htm — accessed 2026-10-14
5. Futures Platform — "2x2 Scenario Planning Matrix" — https://www.futuresplatform.com/blog/2x2-scenario-planning-matrix-guideline — accessed 2026-10-14
6. SAP Community — "Business Scenario Design Guidelines" — https://community.sap.com/t5/technology-q-a/business-scenario-design-guidelines/qaq-p/9243459 — accessed 2026-10-14
7. A. Cockburn — use case guidelines from *Writing Effective Use Cases* (2001) — https://pja.mykhi.org/mgr/blokowe/INN/sorcersoft.org/io/uml/UC-guidelines.html — accessed 2026-10-14
8. A. Cockburn — *Writing Effective Use Cases* (draft) — https://people.inf.elte.hu/molnarba/Informaciorendszerek_ELTE/Writing_effective_Use_cases_Cockburn.pdf — accessed 2026-10-14
9. The Open Group — TOGAF 9 "Artifact: Business Use-Case Diagram" — https://pubs.opengroup.org/architecture/togaf90-doc/epf/TOGAF9/workproducts/Business%20Use-Case%20Diagram_74D9B44D.html — accessed 2026-10-14
10. J. Patton — "The New User Story Backlog is a Map" — https://jpattonassociates.com/the-new-backlog/ — accessed 2026-10-14
11. NN/g — "Mapping User Stories in Agile" — https://www.nngroup.com/articles/user-story-mapping/ — accessed 2026-10-14
12. Agile Alliance — glossary "Story Mapping" — https://agilealliance.org/glossary/story-mapping/ — accessed 2026-10-14
13. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/ieee-1471/cm/ — accessed 2026-10-14
14. P. Kruchten — "Architectural Blueprints — The '4+1' View Model of Software Architecture", IEEE Software 12(6), 1995 — https://arxiv.org/pdf/2006.04975 — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![A4 sample: the online shop's release-1 scope, with customer, support agent, warehouse clerk and finance against browse, order, pay, fulfil and return](/samples/A4-scenario-matrix.svg)
*Sample pending (generated by the renderer from `examples/`).*
