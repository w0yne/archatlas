---
code: A6
slug: journey-map
family: A
names:
  en: Customer or user journey map
  zh: 用户旅程图
  aliases:
    en: [customer journey map, user journey map, UX journey map, CJM, journey map]
    zh: [客户旅程图, 顾客旅程地图, 体验旅程图]
question: What does one persona go through, phase by phase, to reach one goal; what do they do, think and feel; where are the pain points; and who owns each improvement?
audiences: [product, business, leaders]
levels: [strategy, concept]
phases: [initiate, requirements]
scope: One persona, one scenario and goal, one product or service, 4–7 phases, from the customer's point of view.
formal: {kind: convention, ref: 'none (de-facto reference: Nielsen Norman Group journey-mapping guidance)'}
neighbours: [A2, A4, A5, B2, E4]
status: draft
---

# Customer / User Journey Map (用户旅程图 / 客户旅程图)

> A phase-by-phase picture of one persona pursuing one goal: actions, thoughts and a single emotion line on top, pain points and owned opportunities below.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A journey map answers "what does this person go through to reach this goal, and where does it hurt?" NN/g defines it as "a visualization of the process that a person goes through in order to accomplish a goal" [1]. Its point is the **outside-in** view: the customer's process, not the company's. In ISO/IEC/IEEE 42010 terms it serves an experience viewpoint. It is not a TOGAF artifact (business scenarios are the closest TOGAF technique), ArchiMate has no journey element, and the C4 model does not cover it. It deliberately leaves out internal processes and systems (except as touchpoint names), UI click paths and additional personas [1][7].

**Definition used here:** a journey map has three zones: **lens** (one persona, one scenario, expectations), **experience** (phases, actions, thoughts, emotions) and **outputs** (opportunities with owners and metrics) [1][2]. The **experience map** is *not* a synonym: it is product-agnostic and describes a generic human activity [3]. The **service blueprint** is a separate neighbour type with its own notation, not an extension name for this one: it shows the organisation's side (customer actions, frontstage, backstage, support processes, evidence) separated by the lines of interaction, visibility and internal interaction [4][9][11].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** product, UX and service design, marketing and CX, customer support; executives (who have authority but often know customers least) [7]; engineering leads for the backlog hand-off.
- **Scenarios:** online-shop first purchase (current state) to find why customers contact support after paying; a future-state "North Star" journey for a redesigned checkout [6]; a cross-channel journey (web, app, support chatbot, phone); a workshop hypothesis map, labelled as unvalidated, to plan research [6][7].
- **When not to use:** you need system internals (C1, C2, E4) or precise process logic (A5); you need a generic, product-independent view (experience map); several personas with different journeys (one map each); nobody will act on it [2].
- **vs neighbours:**
  - Choose a **service blueprint** (Shostack 1984 [9]) after the journey map, when the question is what the organisation must do frontstage and backstage to deliver each touchpoint; both share the customer-actions row [4][5].
  - Choose **A5 BPMN** for precise hand-offs and branching behind one blueprint row.
  - Choose **B2 user story map** to turn opportunities into backlog and release slices; it is told from the product's point of view [8].
  - Choose **A2 value stream** for a strategic, capability-linked view of value delivery without emotions; **A4 scenario matrix** for role × activity scope.
  - Choose an **empathy map** to synthesise interviews early; it has no time order [3].

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **No formal standard**: no ISO, OMG or Open Group notation. The stable part is the component set, not the glyphs [1][2].
- **Lens (required):** exactly one persona, from research where possible; one scenario with the persona's goal and expectations [1].
- **Experience (required):** 4–7 phases as equal columns, left to right; an actions row (narrative per phase, not a click log); a thoughts row (first-person quotes, verbatim where possible); a **single emotion line** across all phases, positive above a neutral midline [1].
- **Optional:** touchpoints / channels row (web, app, chatbot, e-mail, phone); pain-point markers on the lows of the emotion line.
- **Outputs (required):** opportunities, each with an internal owner and, if known, a metric [1][2].
- **Status metadata (state it on the figure):** current-state vs future-state; research-based vs hypothesis [3][6].
- **Lines:** the emotion curve is the only continuous line; column order implies sequence, so arrows are rarely needed.
- **Naming:** phases in customer language ("Compare products", not "Lead qualification"); thoughts in the first person ("Will it arrive before Friday?").
- **Legend:** emotion scale, pain-point and opportunity markers, channel icons.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices

1. Start from a business goal and the map's users, then choose one actor and one scenario [2][7].
2. Base it on qualitative research; quantitative data supports the story but cannot build it alone [2][7].
3. Decide current vs future state up front; a common route is current-state hypothesis → research validation → future-state vision [6].
4. Synthesise before visualising, and build the map collaboratively across marketing, support, sales and product [2][7].
5. Close the loop: every opportunity has an owner and a metric, feeds a story map or backlog, and the map is kept up to date [1][2][8].

### Anti-patterns

1. The company's process dressed up as a journey, with phases named after departments; that is a blueprint or a BPMN diagram [3].
2. Several personas, or an "average user", on one map [3][7].
3. A hypothesis map used for important decisions without validation or without a visible "hypothesis" label [6][7].
4. No business goal and no owners: a polished poster that changes nothing [2].
5. Click-by-click steps in the actions row, or current and future state mixed in one unmarked map [1][6].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [NN/g, Journey Mapping 101](https://www.nngroup.com/articles/journey-mapping-101/) — the canonical annotated map with lens / experience / outputs zones and one emotion line [1].
- [NN/g, Journey Mapping for Remote Teams: A Digital Template](https://www.nngroup.com/articles/journey-map-digital-template/) — a template that enforces the component set; free to use, check NN/g terms before redistributing [12].
- [NN/g, UX Mapping Methods Compared](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/) — empathy map, journey map, experience map and blueprint side by side; useful for choosing [3].
- [Adaptive Path, Guide to Experience Mapping](https://productstrategy.co/content/files/2023/09/Adaptive_Paths_Guide_to_Experience_Mapping.pdf) — Doing / Thinking / Feeling rows and "so what / what now" takeaways; licensed for non-commercial remix with attribution [10].
- [Shostack, Designing Services That Deliver (HBR, 1984)](https://hbr.org/1984/01/designing-services-that-deliver) — the original service blueprint with line of visibility and fail points; shows what sits *below* a journey. Paywalled [9].
- [Digital.gov, Map your users' and system's journeys](https://digital.gov/guides/research-collaboration/user-needs/journeys) — public-domain government guidance with method steps [13].

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix the lens: one persona (name + one-line descriptor), one scenario and goal, expectations, current or future state, research-based or hypothesis.
2. Choose 4–7 phases in customer language as equal-width columns, left to right.
3. Rows top to bottom: actions, thoughts (one quote per phase), emotion line, pain points on its lows, optional touchpoints, opportunities with owners.
4. Text: at most 3 bullets of ≤8 words per cell; only the top 3–6 opportunities overall, not one per cell.
5. Emotion line: one smooth line over a neutral midline; number the 1–3 worst lows and reuse the numbers on the matching opportunities.
6. Colour: neutral grid; one neutral-to-warning ramp on the curve (no rainbow); one accent for opportunities; a visible "hypothesis — to validate" badge where it applies; a distinct header tint for a future-state map.
7. Header strip: a title with the insight and the state, e.g. "First-time buyer, current state: no delivery update after payment drives support chats"; persona and scenario box at top left.
8. Backstage questions: propose a separate service blueprint that reuses the actions row; do not overload the journey map.

**Self-check**
- [ ] Exactly one persona and one scenario; state and evidence basis are stated.
- [ ] 4–7 phases, named from the customer's point of view.
- [ ] Actions are narrative per phase; thoughts are first-person quotes.
- [ ] One emotion line, and its lows match the marked pain points.
- [ ] Every opportunity has an owner (and a metric if known).
- [ ] No department steps or system architecture disguised as phases.
- [ ] The legend explains the emotion scale, markers and icons.
- [ ] The title carries the insight; hypothesis content is visibly labelled; no TBD or working notes.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Code can suggest:** touchpoints and phase boundaries from routes, menus, page names and e-mail / push templates; funnels and analytics events (`checkout_started`, `payment_failed`); feature flags and experiments around pain points; support-ticket labels, error-message catalogues and help content; SLAs and timeouts that explain waiting phases; chatbot intents and fallback logs.
- **Ask people:** the real persona, thoughts, emotions and expectations, off-system phases (research before visiting, word of mouth), and the severity of pain points. They come from user research, support agents, survey verbatims and the product team.
- A map drawn from code alone is a **hypothesis map** and must say so.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Whose journey, and which goal or scenario? (the primary customer persona on the most common journey)
2. Current state to find pain points, or future state as a target vision? (current state, unless designing something new)
3. What evidence exists: interviews, support tickets, analytics, or team knowledge only? (team knowledge only → label as hypothesis)
4. Which phases, from first trigger to outcome? (a proposed set of 4–7 for the user to confirm)
5. Customer view only, or also a service blueprint of what happens behind each touchpoint? (journey only)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A6.json` · Layout template: `grid_table` · phases are columns and component rows (actions, thoughts, emotion, pain points, touchpoints, opportunities) are table rows; the emotion row holds one word per phase (the renderer draws no emotion line yet); the first column header must not be empty (use `Row`).

## Sources {#sources}
<!-- skill: omit -->
1. Sarah Gibbons, NN/g, Journey Mapping 101 (2018) — https://www.nngroup.com/articles/journey-mapping-101/ — accessed 2026-10-14
2. Kate Kaplan, NN/g, When and How to Create Customer Journey Maps (2016) — https://www.nngroup.com/articles/customer-journey-mapping/ — accessed 2026-10-14
3. Sarah Gibbons, NN/g, UX Mapping Methods Compared: A Cheat Sheet (2017) — https://www.nngroup.com/articles/ux-mapping-cheat-sheet/ — accessed 2026-10-14
4. Sarah Gibbons, NN/g, Service Blueprints: Definition (2017) — https://www.nngroup.com/articles/service-blueprints-definition/ — accessed 2026-10-14
5. Gibbons & Kendrick, NN/g, Service Blueprinting FAQ (2019) — https://www.nngroup.com/articles/service-blueprinting-faq/ — accessed 2026-10-14
6. Kate Kaplan, NN/g, Journey-Mapping Approaches: 2 Critical Decisions (2020) — https://www.nngroup.com/articles/journey-mapping-approaches/ — accessed 2026-10-14
7. Kendrick & Kaplan, NN/g, Journey Mapping: 9 Frequently Asked Questions (2019) — https://www.nngroup.com/articles/journey-mapping-faq/ — accessed 2026-10-14
8. Anna Kaley, NN/g, Mapping User Stories in Agile (2021) — https://www.nngroup.com/articles/user-story-mapping/ — accessed 2026-10-14
9. G. Lynn Shostack, Designing Services That Deliver, Harvard Business Review, Jan 1984 — https://hbr.org/1984/01/designing-services-that-deliver — accessed 2026-10-14
10. Adaptive Path, Adaptive Path's Guide to Experience Mapping (2013) — https://productstrategy.co/content/files/2023/09/Adaptive_Paths_Guide_to_Experience_Mapping.pdf — accessed 2026-10-14
11. Service Design Tools, Service Blueprint — https://servicedesigntools.org/tools/service-blueprint — accessed 2026-10-14
12. NN/g, Journey Mapping for Remote Teams: A Digital Template — https://www.nngroup.com/articles/journey-map-digital-template/ — accessed 2026-10-14
13. Digital.gov, Map your users' and system's journeys — https://digital.gov/guides/research-collaboration/user-needs/journeys — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![A6 sample: online shop first-time buyer, current state — phases Discover, Compare, Buy, Wait for delivery, Receive, Get help; emotion dips after payment and at the support chatbot hand-off; opportunities owned by Warehouse and Customer Support](/samples/A6-journey-map.svg)
*Sample pending (generated by the renderer from `examples/`).*
