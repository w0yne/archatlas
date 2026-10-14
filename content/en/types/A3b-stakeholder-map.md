---
code: A3b
slug: stakeholder-map
family: A
names:
  en: Stakeholder Map (Power–Interest Grid)
  zh: 干系人地图（权力–利益矩阵）
  aliases:
    en: [power/interest grid, power-interest matrix, influence/interest grid, stakeholder matrix, stakeholder catalog (TOGAF 10), stakeholder onion diagram]
    zh: [利益相关者地图, 权力/利益矩阵, 影响力 × 关注度矩阵, 干系人洋葱图]
question: "Whose support do we need, how much power and interest does each party have, and how do we engage them?"
audiences: [sponsor, programme or project manager, lead architect]
level: strategy
phases: [discovery, planning, review]
scope: "All stakeholder roles or groups of one initiative, plotted on power and interest, with an engagement approach per quadrant."
formal:
  kind: method
  ref: "Power/interest grid (Johnson & Scholes, Exploring Corporate Strategy, 2nd ed. 1993, after Mendelow 1981); TOGAF Stakeholder Management technique"
neighbours: [A3, H1, A1, I2]
status: draft
---

# Stakeholder Map (干系人地图)

> A 2×2 grid of power against interest that tells you whom to manage closely, keep satisfied, keep informed or simply monitor.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** whose support does the initiative need, how much power and interest does each party have, and how should each be engaged?
- **Concern:** this is the ISO/IEC/IEEE 42010 stakeholder → concern link made explicit [7]. It is a **project and governance** artefact: TOGAF's Stakeholder Management technique uses it to plan communication and to choose which views each group gets [1][2].
- **Left out on purpose:** flows and exchanges (A3), architecture content of any kind, and responsibilities per activity (H1 RACI).
- **Definition used here:** the power × interest grid as published by Johnson & Scholes (*Exploring Corporate Strategy*, 2nd ed., 1993) as a development of **Mendelow (1981)**. Mendelow's original grid was **power × dynamism** and set how intensively to scan the environment [3][4]. The citation "Mendelow 1991" is a misdating [3][4].
- **Sensitivity:** TOGAF notes that stakeholder mapping information is potentially sensitive and keeps it informal [5]. Treat the grid as **internal**: it often rates real people and groups.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** sponsor, programme or project manager, lead architect; restricted circulation.
- **Scenarios:** planning engagement for the online shop's checkout redesign (finance, legal, security, support, warehouse operations, payment provider); finding hidden stakeholders (data protection, tax, works council) before requirements freeze; deciding which diagrams each group receives; re-ranking at each phase gate.
- **When not to use:** in any deck that leaves the core team (use roles only, or a plain list); with fewer than about six stakeholders (a list is enough); to show who exchanges what with the system (A3).
- **vs neighbours:**
  - Choose **A3 Business Context Diagram** when the question is who interacts with the system and what flows; it has flows, not axes.
  - Choose **H1 RACI Matrix** when you need responsibility per activity, not engagement per stakeholder.
  - Choose an **ArchiMate Stakeholder / Motivation view** (I2) when you must trace stakeholders → drivers → goals → requirements formally.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required:** two axes, *Interest →* (x) and *Power ↑* (y), each Low/High or 1–5; four labelled quadrants: **Key Players** (manage closely), **Keep Satisfied**, **Keep Informed**, **Minimal Effort** (monitor) [2][6]; stakeholders plotted as short labels.
- **Plot roles or groups**, not personal names, whenever the map may circulate.
- **Optional third dimension:** attitude (supporter / neutral / critic) by marker shape or colour, with a legend [6][8]. Arrows may show a planned move (e.g. Keep Informed → Key Players).
- **Companion table** (TOGAF stakeholder catalog columns): stakeholder | involvement | quadrant | key concerns | views they need [1][5].
- **Onion variant (BABOK):** concentric rings: solution, people who use it, the hosting organisation, external parties such as customers, regulators and suppliers [9].
- **Lines:** none between stakeholders; this is not a network diagram.
- **Formal alternative:** ArchiMate Stakeholder viewpoint with Stakeholder, Driver, Assessment and Goal elements [10].
- TOGAF 10 quadrant names and catalog columns were taken from TOGAF 9.2 text and secondary guides; not verified against the current spec text.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices

1. Gather broadly before scoring: use the 42010 stakeholder classes [7] and the five TOGAF stakeholder groups (corporate functions, end users, project organisation, operations, external) [6].
2. **Score with the sponsor; never invent scores.** Power and interest are judgements, not data.
3. Add **attitude**, and attach an **engagement action** to every quadrant [8].
4. **Revisit at each phase.** Stakeholders and their power change; mapping is not a one-time activity [6][8].
5. Use the grid to **choose views**: TOGAF's final step tailors the catalogs, matrices and diagrams each group receives [1][2].

### Anti-patterns

1. Power/interest colouring sprayed onto a context diagram: one figure, two questions [5].
2. Named individuals placed in "Minimal Effort" in a circulated deck [5].
3. A grid with no action attached; the analysis never turns into engagement.
4. Only end users plotted; regulators, finance, operations and suppliers forgotten.
5. Attributing power × interest to "Mendelow 1991" [3][4].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [NN/g — Stakeholder Analysis for UX Projects](https://www.nngroup.com/articles/stakeholder-analysis/) — power/interest grid with attitude and the advice to revisit.
- [Votito — Stakeholder mapping origins](https://www.votito.com/methods/stakeholder-mapping/) — clear public account of Mendelow vs Johnson & Scholes vs Freeman.
- [TOGAF 10 — Stakeholder Management](https://pubs.opengroup.org/togaf-standard/adm-techniques/chap03.html) — example stakeholder table and power grid (login-gated; © The Open Group).
- [BAwiki — Stakeholder Onion Diagram](http://bawiki.com/wiki/Stakeholder-Onion-Diagram.html) — step-by-step onion construction.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Confirm who will see the map. If it may leave the core team, use roles or groups only and drop attitude.
2. Gather stakeholders as roles or groups with the checklists above; aim for 6–20.
3. Score power and interest with the user (High/Low or 1–5). Never guess.
4. Draw a square 2×2 grid; axis labels *Interest →* and *Power ↑*; quadrant names in the corners.
5. Plot short labels (≤ 3 words); attitude by marker shape, with a legend; optional arrows for planned moves.
6. Put concerns and engagement actions in a companion table, not on the grid.
7. Colour: neutral quadrants (one light tint for Key Players at most); attitude markers use shape first, colour second.
8. Footer "Internal — stakeholder analysis" whenever real groups or names appear.

**Self-check**

- [ ] Axes and all four quadrants are labelled.
- [ ] Every point is a role or group, or the figure is marked internal.
- [ ] Scores came from the user, not the drawer.
- [ ] Regulators, finance, operations and suppliers were considered.
- [ ] Each quadrant has an engagement action in the companion table.
- [ ] The grid is a separate figure from the context diagram.
- [ ] Any attribution reads "Johnson & Scholes, after Mendelow 1981".

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **From code:** almost nothing. CODEOWNERS, team labels and issue assignees hint at internal groups; ADR deciders hint at who holds decision power.
- **Limit:** power, interest, attitude and external stakeholders come only from interviews and the sponsor. Never infer them; ask.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Who will see this map? (Core team only; roles instead of names otherwise.)
2. Grid, onion or both? (Grid.)
3. Which scale for power and interest? (High/Low.)
4. Should attitude be shown? (Yes, internal copy only.)
5. Here is a candidate list from the standard groups; who is missing? (Add regulators and suppliers.)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A3b.json` · Layout template: `grid_table` · A 2×2 `tables[]` entry holds the quadrants; stakeholders are cell items carrying attitude tags, and the companion table is a second table.

## Sources {#sources}
<!-- skill: omit -->
1. The Open Group — TOGAF Standard 10, ADM Techniques ch. 3 "Stakeholder Management" — https://pubs.opengroup.org/togaf-standard/adm-techniques/chap03.html — accessed 2026-10-14 (login-gated; not verified against the current spec text)
2. The Open Group — TOGAF 9.2 ch. 21 "Stakeholder Management" — https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap21.html — accessed 2026-10-14
3. Mendelow, A. L. — "Environmental Scanning — The Impact of the Stakeholder Concept", ICIS 1981 Proceedings, paper 20 — https://aisel.aisnet.org/icis1981/20/ — accessed 2026-10-14
4. Votito — "Stakeholder Mapping — Power Interest Matrix origins" — https://www.votito.com/methods/stakeholder-mapping/ — accessed 2026-10-14
5. The Open Group — TOGAF Standard 10, Architecture Content ch. 3 "Architectural Artifacts" (Stakeholder catalog) — https://pubs.opengroup.org/togaf-standard/architecture-content/chap03.html — accessed 2026-10-14 (login-gated); TOGAF 9.2 ch. 31 — https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap31.html — accessed 2026-10-14
6. TOGAF Exam Preparation Guide — "Stakeholder Management" (quadrant names, five stakeholder groups) — https://togafguide.wordpress.com/stakeholder-management/ — accessed 2026-10-14
7. ISO/IEC/IEEE 42010 — conceptual model and stakeholder checklists — http://www.iso-architecture.org/ieee-1471/cm/ and http://www.iso-architecture.org/ieee-1471/ads/ — accessed 2026-10-14
8. NN/g — "Stakeholder Analysis for UX Projects" — https://www.nngroup.com/articles/stakeholder-analysis/ — accessed 2026-10-14
9. IIBA — BABOK Guide v3, 10.43 "Stakeholder List, Map, or Personas" — https://www.iiba.org/my-iiba/search-the-babok-guide/babok-guide/techniques/stakeholder-list-map-or-personas/ — accessed 2026-10-14
10. The Open Group — ArchiMate 3.2 Specification, Appendix C "Example Viewpoints" (Stakeholder viewpoint) — https://pubs.opengroup.org/architecture/archimate3-doc/ch-Example-Viewpoints.html — accessed 2026-10-14 (login-gated; not verified against the current spec text)

## Sample {#sample}
<!-- skill: path only -->
![A3b sample: power–interest grid for the online shop's checkout redesign, with finance, payment provider, support, warehouse operations and data protection as roles](/samples/A3b-stakeholder-map.svg)
*Sample pending (generated by the renderer from `examples/`).*
