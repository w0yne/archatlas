# Customer / User Journey Map (用户旅程图 / 客户旅程图)
<!-- Generated from content/en/types/A6-journey-map.md by tools/build_skill_refs.py. Do not edit. -->
> What does one persona go through, phase by phase, to reach one goal; what do they do, think and feel; where are the pain points; and who owns each improvement?
Scope: One persona, one scenario and goal, one product or service, 4–7 phases, from the customer's point of view. Neighbours: A2, A4, A5, B2, E4.

## Meaning
A journey map answers "what does this person go through to reach this goal, and where does it hurt?" NN/g defines it as "a visualization of the process that a person goes through in order to accomplish a goal". Its point is the **outside-in** view: the customer's process, not the company's. In ISO/IEC/IEEE 42010 terms it serves an experience viewpoint. It is not a TOGAF artifact (business scenarios are the closest TOGAF technique), ArchiMate has no journey element, and the C4 model does not cover it. It deliberately leaves out internal processes and systems (except as touchpoint names), UI click paths and additional personas.

**Definition used here:** a journey map has three zones: **lens** (one persona, one scenario, expectations), **experience** (phases, actions, thoughts, emotions) and **outputs** (opportunities with owners and metrics). The **experience map** is *not* a synonym: it is product-agnostic and describes a generic human activity. The **service blueprint** is a separate neighbour type with its own notation, not an extension name for this one: it shows the organisation's side (customer actions, frontstage, backstage, support processes, evidence) separated by the lines of interaction, visibility and internal interaction.

## When to use and how to choose
- **Audience:** product, UX and service design, marketing and CX, customer support; executives (who have authority but often know customers least); engineering leads for the backlog hand-off.
- **Scenarios:** online-shop first purchase (current state) to find why customers contact support after paying; a future-state "North Star" journey for a redesigned checkout; a cross-channel journey (web, app, support chatbot, phone); a workshop hypothesis map, labelled as unvalidated, to plan research.
- **When not to use:** you need system internals (C1, C2, E4) or precise process logic (A5); you need a generic, product-independent view (experience map); several personas with different journeys (one map each); nobody will act on it.
- **vs neighbours:**
  - Choose a **service blueprint** (Shostack 1984) after the journey map, when the question is what the organisation must do frontstage and backstage to deliver each touchpoint; both share the customer-actions row.
  - Choose **A5 BPMN** for precise hand-offs and branching behind one blueprint row.
  - Choose **B2 user story map** to turn opportunities into backlog and release slices; it is told from the product's point of view.
  - Choose **A2 value stream** for a strategic, capability-linked view of value delivery without emotions; **A4 scenario matrix** for role × activity scope.
  - Choose an **empathy map** to synthesise interviews early; it has no time order.

## Notation and elements
- **No formal standard**: no ISO, OMG or Open Group notation. The stable part is the component set, not the glyphs.
- **Lens (required):** exactly one persona, from research where possible; one scenario with the persona's goal and expectations.
- **Experience (required):** 4–7 phases as equal columns, left to right; an actions row (narrative per phase, not a click log); a thoughts row (first-person quotes, verbatim where possible); a **single emotion line** across all phases, positive above a neutral midline.
- **Optional:** touchpoints / channels row (web, app, chatbot, e-mail, phone); pain-point markers on the lows of the emotion line.
- **Outputs (required):** opportunities, each with an internal owner and, if known, a metric.
- **Status metadata (state it on the figure):** current-state vs future-state; research-based vs hypothesis.
- **Lines:** the emotion curve is the only continuous line; column order implies sequence, so arrows are rarely needed.
- **Naming:** phases in customer language ("Compare products", not "Lead qualification"); thoughts in the first person ("Will it arrive before Friday?").
- **Legend:** emotion scale, pain-point and opportunity markers, channel icons.

## Best practices and anti-patterns
### Best practices

1. Start from a business goal and the map's users, then choose one actor and one scenario.
2. Base it on qualitative research; quantitative data supports the story but cannot build it alone.
3. Decide current vs future state up front; a common route is current-state hypothesis → research validation → future-state vision.
4. Synthesise before visualising, and build the map collaboratively across marketing, support, sales and product.
5. Close the loop: every opportunity has an owner and a metric, feeds a story map or backlog, and the map is kept up to date.

### Anti-patterns

1. The company's process dressed up as a journey, with phases named after departments; that is a blueprint or a BPMN diagram.
2. Several personas, or an "average user", on one map.
3. A hypothesis map used for important decisions without validation or without a visible "hypothesis" label.
4. No business goal and no owners: a polished poster that changes nothing.
5. Click-by-click steps in the actions row, or current and future state mixed in one unmarked map.

## Drawing recipe
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

## Evidence in a code repository
- **Code can suggest:** touchpoints and phase boundaries from routes, menus, page names and e-mail / push templates; funnels and analytics events (`checkout_started`, `payment_failed`); feature flags and experiments around pain points; support-ticket labels, error-message catalogues and help content; SLAs and timeouts that explain waiting phases; chatbot intents and fallback logs.
- **Ask people:** the real persona, thoughts, emotions and expectations, off-system phases (research before visiting, word of mouth), and the severity of pain points. They come from user research, support agents, survey verbatims and the product team.
- A map drawn from code alone is a **hypothesis map** and must say so.

## Guided-mode questions
1. Whose journey, and which goal or scenario? (the primary customer persona on the most common journey)
2. Current state to find pain points, or future state as a target vision? (current state, unless designing something new)
3. What evidence exists: interviews, support tickets, analytics, or team knowledge only? (team knowledge only → label as hypothesis)
4. Which phases, from first trigger to outcome? (a proposed set of 4–7 for the user to confirm)
5. Customer view only, or also a service blueprint of what happens behind each touchpoint? (journey only)

## Template
Model template: `assets/templates/A6.json` · Layout template: `grid_table` · phases are columns and component rows (actions, thoughts, emotion, pain points, touchpoints, opportunities) are table rows; the emotion row holds one word per phase (the renderer draws no emotion line yet); the first column header must not be empty (use `Row`).

## Sample
Figure: `samples/A6-journey-map.svg` (published with the site)
