# Stakeholder Map (干系人地图)
<!-- Generated from content/en/types/H3-stakeholder-map.md by tools/build_skill_refs.py. Do not edit. -->
> Whose support do we need, how much power and interest does each party have, and how do we engage them?
Scope: All stakeholder roles or groups of one initiative, plotted on power and interest, with an engagement approach per quadrant. Neighbours: A3, H1, A1, I2.

## Meaning
- **Question:** whose support does the initiative need, how much power and interest does each party have, and how should each be engaged?
- **Concern:** this is the ISO/IEC/IEEE 42010 stakeholder → concern link made explicit. It is a **project and governance** artefact: TOGAF's Stakeholder Management technique uses it to plan communication and to choose which views each group gets.
- **Left out on purpose:** flows and exchanges (A3), architecture content of any kind, and responsibilities per activity (H1 RACI).
- **Definition used here:** the power × interest grid as published by Johnson & Scholes (*Exploring Corporate Strategy*, 2nd ed., 1993) as a development of **Mendelow (1981)**. Mendelow's original grid was **power × dynamism** and set how intensively to scan the environment. The citation "Mendelow 1991" is a misdating.
- **Sensitivity:** TOGAF notes that stakeholder mapping information is potentially sensitive and keeps it informal. Treat the grid as **internal**: it often rates real people and groups.

## When to use and how to choose
- **Audience:** sponsor, programme or project manager, lead architect; restricted circulation.
- **Scenarios:** planning engagement for the online shop's checkout redesign (finance, legal, security, support, warehouse operations, payment provider); finding hidden stakeholders (data protection, tax, works council) before requirements freeze; deciding which diagrams each group receives; re-ranking at each phase gate.
- **When not to use:** in any deck that leaves the core team (use roles only, or a plain list); with fewer than about six stakeholders (a list is enough); to show who exchanges what with the system (A3).
- **vs neighbours:**
  - Choose **A3 Business Context Diagram** when the question is who interacts with the system and what flows; it has flows, not axes.
  - Choose **H1 RACI Matrix** when you need responsibility per activity, not engagement per stakeholder.
  - Choose an **ArchiMate Stakeholder / Motivation view** (I2) when you must trace stakeholders → drivers → goals → requirements formally.

## Notation and elements
- **Required:** two axes, *Interest →* (x) and *Power ↑* (y), each Low/High or 1–5; four labelled quadrants: **Key Players** (manage closely), **Keep Satisfied**, **Keep Informed**, **Minimal Effort** (monitor); stakeholders plotted as short labels.
- **Plot roles or groups**, not personal names, whenever the map may circulate.
- **Optional third dimension:** attitude (supporter / neutral / critic) by marker shape or colour, with a legend. Arrows may show a planned move (e.g. Keep Informed → Key Players).
- **Companion table** (TOGAF stakeholder catalog columns): stakeholder | involvement | quadrant | key concerns | views they need.
- **Onion variant (BABOK):** concentric rings: solution, people who use it, the hosting organisation, external parties such as customers, regulators and suppliers.
- **Lines:** none between stakeholders; this is not a network diagram.
- **Formal alternative:** ArchiMate Stakeholder viewpoint with Stakeholder, Driver, Assessment and Goal elements.
- TOGAF 10 quadrant names and catalog columns were taken from TOGAF 9.2 text and secondary guides; not verified against the current spec text.

## Best practices and anti-patterns
### Best practices

1. Gather broadly before scoring: use the 42010 stakeholder classes and the five TOGAF stakeholder groups (corporate functions, end users, project organisation, operations, external).
2. **Score with the sponsor; never invent scores.** Power and interest are judgements, not data.
3. Add **attitude**, and attach an **engagement action** to every quadrant.
4. **Revisit at each phase.** Stakeholders and their power change; mapping is not a one-time activity.
5. Use the grid to **choose views**: TOGAF's final step tailors the catalogs, matrices and diagrams each group receives.

### Anti-patterns

1. Power/interest colouring sprayed onto a context diagram: one figure, two questions.
2. Named individuals placed in "Minimal Effort" in a circulated deck.
3. A grid with no action attached; the analysis never turns into engagement.
4. Only end users plotted; regulators, finance, operations and suppliers forgotten.
5. Attributing power × interest to "Mendelow 1991".

## Drawing recipe
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

## Evidence in a code repository
- **From code:** almost nothing. CODEOWNERS, team labels and issue assignees hint at internal groups; ADR deciders hint at who holds decision power.
- **Limit:** power, interest, attitude and external stakeholders come only from interviews and the sponsor. Never infer them; ask.

## Guided-mode questions
1. Who will see this map? (Core team only; roles instead of names otherwise.)
2. Grid, onion or both? (Grid.)
3. Which scale for power and interest? (High/Low.)
4. Should attitude be shown? (Yes, internal copy only.)
5. Here is a candidate list from the standard groups; who is missing? (Add regulators and suppliers.)

## Template
Model template: `assets/templates/H3.json` · Layout template: `grid_table` · A 2×2 `tables[]` entry holds the quadrants; stakeholders are cell items carrying attitude tags, and the companion table is a second table.

## Sample
Figure: `samples/H3-stakeholder-map.svg` (published with the site)
