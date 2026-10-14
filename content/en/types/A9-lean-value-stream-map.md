---
code: A9
slug: lean-value-stream-map
family: A
names:
  en: Lean Value-Stream Map
  zh: 精益价值流图
  aliases:
    en: [value-stream map, VSM, current-state map, future-state map, material and information flow diagram]
    zh: [价值流程图, 精益价值流程图, 现状图, 未来状态图, VSM]
question: "Where do time and waste sit in today's flow of work and information for one product or service family, and what should the future flow be?"
audiences: [process owners, operations and improvement teams, frontline staff, engineering and delivery leads]
level: logical
phases: [discovery, review, operate]
scope: "One product or service family, door to door from trigger to delivery, current state and (separately) future state, with process times, waits and a timeline"
formal:
  kind: method
  ref: "Rother & Shook, Learning to See (Lean Enterprise Institute, 1998); LEI icon set (de-facto, no ISO notation); Martin & Osterling, Value Stream Mapping (2013) for office and service work"
neighbours: [A2, A5, E4, G4, A8]
status: draft
---

# Lean Value-Stream Map (精益价值流图)

> A door-to-door map of one product or service flow that shows process boxes, queues, information flow and a timeline of process time against waiting time, drawn as a current state and a future state.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** where does the time go between trigger and delivery, how much of it is real work, and what should the future flow look like?
- **Viewpoint:** operational flow and performance of one product or service family, observed where the work happens. LEI defines value-stream mapping as "diagraming every step involved in the material and information flows needed to bring a product from order to delivery" [1]; "it shows the linkage between material flow and information flow. No other tool does this" [1]. In 42010 terms it frames the concern "lead time and waste" for process owners. No ArchiMate viewpoint, no TOGAF artifact, no C4 model level.
- **Deeper meaning:** it is a learning-to-see exercise, not a drawing exercise: "Having a perfectly drawn current state map is not the point" [1]. A current-state map is always paired with a future-state map and an implementation plan [1][4].
- **Leaves out:** physical layout (deliberately postponed [5]), detailed task logic and decisions, capabilities and stakeholder value.
- **Definition used here:** this is the Lean sense of "value stream" (Womack and Jones; mapping method by Rother and Shook [2][3]). It is a different diagram from the business-architecture A2 Value Stream, which has no times. TOGAF notes that the Lean value stream exists to analyse and improve the flow of information or materials and is not suited to cross-mapping stages to capabilities [7]; the Business Architecture Guild says its value streams are not Lean value streams [8]. SAFe's "development value stream" is a third, looser sense [9].
- **Metric used here:** activity ratio (flow efficiency) = ΣPT ÷ total lead time; lead time includes process time, so wait = LT − PT [2].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** process owners, operations and improvement teams and the people who do the work, plus suppliers and customers.
- **Scenarios:** order to doorstep (why a 20-minute job takes a day and a half: sum PT and waits, lead time, activity ratio); support query to resolution; returns; software delivery from ticket and pipeline timestamps; a future-state map with kaizen bursts.
- **When not to use:** without real observations or data ("go and see"); strategy-level value and capabilities (A2); system structure (C family); exceptions and branching logic (A5, E family).
- **vs neighbours:**
  - **A2 Value Stream** for how value reaches a stakeholder; never put times there.
  - **A5 BPMN Process** for task order, decisions, exceptions.
  - **E4 Swimlane** for who or which system does each step; A9 shows how long work sits.
  - **G4 Delivery Pipeline** for the build and release stages; A9 measures the waiting around them.
  - **A8 Roadmap** for a multi-step change plan.
-->
- **Audience:** process owners, operations and improvement teams and the people who do the work; LEI advises involving the "value-creators" plus suppliers and customers [4].
- **Classic scenarios:**
  1. Order to doorstep in an online shop: checkout, payment authorisation by the payment provider, fraud review, picking, packing and carrier hand-over, to see why a 20-minute job takes a day and a half (illustrative numbers: PT 3 + 5 + 6 + 4 + 2 = 20 min, waits 0.5 + 6 + 10 + 2 + 14 = 32.5 h, lead time ≈ 32.8 h, activity ratio ≈ 1 %).
  2. Customer support: query to resolution, from the support chatbot through escalation to an agent and back, to find where tickets wait.
  3. Returns: return request to refund, across the warehouse, finance and the payment provider.
  4. Software delivery: idea to production across intake, build, test and release, using ticket and pipeline timestamps [9].
  5. Future-state design: a second map with kaizen bursts as the basis for an improvement plan [1][6].
- **When not to use:** without real observations or data ("go and see", "count the right things" [4]); for strategy-level value and capabilities (A2); for system structure (C family); for exceptions and branching logic (A5, E family).
- **vs neighbours:**
  - Choose **A2 Value Stream** when the question is how value reaches a stakeholder and which capabilities enable it; never put times there.
  - Choose **A5 BPMN Process** when the question is task order, decisions and exceptions for a case.
  - Choose **E4 Swimlane** when the question is who or which system does each step; A9 shows how long work sits.
  - Choose **G4 Delivery Pipeline** when the question is the build and release stages themselves; A9 measures the waiting around them.
  - Choose **A8 Target Architecture and Roadmap** for a multi-step change plan; a future-state map is one target with kaizen bursts.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** a method with a de-facto LEI icon set (downloadable) but no ISO notation [1][6]. With readers who do not know Lean icons, use labelled boxes and a legend.
- **Required:**
  - **Supplier** (top left) and **customer** (top right, with demand rate or takt) [1][6].
  - **Process boxes** left to right, one per area of continuous flow; a box "stops wherever processes are disconnected and the material flow stops" [1].
  - **Data box** under each process: cycle or process time (C/T, PT), changeover (C/O), uptime, %C&A (percent complete and accurate), and people (office) or availability (manufacturing) [1][2].
  - **Inventory or queue triangles** between boxes, with quantity or days waiting.
  - **Information flow** along the top: who schedules or releases work; manual arrows straight, electronic arrows zig-zag [6]. A map that ignores information flow "is like a piece of sheet music that just lists notes randomly" [5].
  - **Timeline ladder** at the bottom: wait on the upper rungs, PT on the lower rungs; totals at the right: total lead time, ΣPT, activity ratio, and rolled %C&A for office work [2].
- **Optional:** push arrows (striped) and supermarket, FIFO or kanban icons for pull [6]; kaizen bursts on the future-state map [6].
- **Legend:** icons used, units (minutes, hours, days) and "current state, mapped on `<date>`", with the source of the numbers.
- **Naming:** process boxes named as work done ("Pick", "Pack"), not by department; one time unit per row of numbers.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **One product or service family, one lead, door to door,** capturing both work flow and information flow [1].
2. **Walk the flow and measure it** where the work happens instead of estimating in a meeting room [4].
3. **Draw the current state quickly, then the future state;** nest 30/60/90-day actions inside an 18–24-month future state [4].
4. **Show waits as well as work;** waste hides in the waiting, and the timeline must show both [1][2].
5. **Look for a flow solution within the existing layout first;** layout analysis comes later [5].

### Anti-patterns
1. **Recording only process time,** so the waits that make up most of the lead time disappear [1][2].
2. **Numbers guessed in a meeting room** instead of observed or taken from system data [4].
3. **Omitting the information flow** [5].
4. **A current-state map with no future state or plan** [1][4].
5. **Mixing in business-architecture content,** such as capabilities under process boxes; that is A2 [7]. Also avoid departments as boxes, long return lines and unexplained icons.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [LEI Lexicon: Value-Stream Mapping](https://www.lean.org/lexicon-terms/value-stream-mapping) — current- and future-state example maps with data boxes and timeline, plus an icon download. © Lean Enterprise Institute.
- [Martin & Osterling, Value Stream Mapping, chapter 1 (TKMG PDF)](https://tkmg.com/wp-content/files/VSM-Ch-1.pdf) — office current/future maps with LT, PT, %C&A, activity ratio and rolled %C&A; a clear service-sector example. © McGraw-Hill / TKMG.
- [J. Shook, Misunderstandings about value stream mapping (LEI, 2004)](https://www.lean.org/the-lean-post/articles/misunderstandings-about-value-stream-mapping-flow-analysis-and-takt-time/) — why information flow is essential and why layout comes later.
- [Lucidchart: Value stream mapping symbols and icons](https://lucid.co/diagram/vsm/value-stream-mapping-symbols) — a readable overview of the standard icons. Vendor content.
- [SAFe: Development Value Streams](https://framework.scaledagile.com/development-value-streams) — the software-delivery use of the term. © Scaled Agile.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Scope: one family, door-to-door start and end, current or future, date; title carries the finding, e.g. "Order to doorstep: 20 min of work in 33 h".
2. Top band: supplier left, customer right with demand rate; coordination or scheduling in the middle with its information arrows.
3. Middle band: process boxes left to right with a data box beneath each (PT, %C&A, people); queue triangles with counts or wait times between them.
4. Bottom band: timeline ladder (wait above, PT below) with totals at the right: lead time, ΣPT, activity ratio.
5. Future state: a second map with kaizen bursts at the change points, same order and scale so the two compare side by side.
6. Text: short work names in boxes; numbers only in data boxes and the timeline; one time unit per row.
7. Colour: neutral boxes; one accent for waits or kaizen bursts; plain labelled boxes instead of Lean icons for non-Lean readers, always with a legend.

**Self-check**
- [ ] Every process box has a data box with PT; queues and waits are shown between boxes.
- [ ] Totals add up: ΣPT ≤ lead time and activity ratio = ΣPT ÷ lead time.
- [ ] The source of the numbers (observed, sampled, system data) and the period are stated near the figure.
- [ ] Information flow is drawn, not only the work flow.
- [ ] Strictly left to right, no long return lines; boxes are work steps, not departments.
- [ ] No capabilities or stakeholder value stages (those belong in A2).
- [ ] The figure states current or future; a future map has kaizen bursts tied to a plan.
- [ ] Icons and units are explained in a legend.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Useful for digital work:** timestamps in order or ticket status histories, CI/CD pipeline logs, PR open → merge → deploy times, and queue or backlog ages give lead time, PT and wait per step.
- **Process boxes:** board columns, issue labels and workflow state enums (`placed → paid → picked → packed → shipped`).
- **%C&A proxies:** rework counts such as reopened tickets, failed builds or orders returned to an earlier state.
- **Must come from people:** manual or offline steps (packing at the warehouse, carrier collection), true touch time, reasons for waiting, and the future state. State the sample period.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Is the question time and waste in a flow, or stakeholder value and capabilities? (time and waste; otherwise switch to A2)
2. Which product or service family, with which start and end points? (standard parcel orders, checkout to carrier hand-over)
3. Where do the numbers come from, and for which period? (system timestamps for the last 4 weeks, plus observed touch times)
4. Current state, future state, or both side by side? (both, current first)
5. Can the audience read Lean icons? (no: labelled boxes plus a legend)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A9.json` · Layout template: `tree` · process steps are `task` nodes in one left-to-right row with a `queue` node between steps; the process data box goes in the node `sub` or `attributes`; totals (lead time, processing time, activity ratio) go in `meta.description` because the renderer draws no timeline row yet.

## Sources {#sources}
<!-- skill: omit -->
1. Lean Enterprise Institute, Lexicon: "Value-Stream Mapping" — https://www.lean.org/lexicon-terms/value-stream-mapping — accessed 2026-10-14
2. K. Martin & M. Osterling, *Value Stream Mapping* (McGraw-Hill, 2013), Chapter 1 (TKMG PDF) — https://tkmg.com/wp-content/files/VSM-Ch-1.pdf — accessed 2026-10-14
3. Lean Enterprise Institute, "6 Guidelines for Moving Toward a Lean Value Stream" (Rother & Shook; *Learning to See*, Shingo Research Prize 1999) — https://www.lean.org/the-lean-post/articles/6-guidelines-for-moving-toward-a-lean-value-stream — accessed 2026-10-14
4. Lean Enterprise Institute, "10 Tips for Getting the Most Value from Value Stream Mapping" — https://www.lean.org/the-lean-post/articles/10-tips-for-getting-the-most-value-from-value-stream-mapping/ — accessed 2026-10-14
5. J. Shook, "Misunderstandings About Value Stream Mapping, Flow Analysis, and Takt Time", LEI (4 Mar 2004) — https://www.lean.org/the-lean-post/articles/misunderstandings-about-value-stream-mapping-flow-analysis-and-takt-time/ — accessed 2026-10-14
6. Lucidchart, "Value Stream Mapping Symbols and Icons" — https://lucid.co/diagram/vsm/value-stream-mapping-symbols — accessed 2026-10-14
7. TOGAF Series Guide: Value Streams (G178), App. A.3 "Lean Value Stream", The Open Group (mirror PDF) — https://governance.foundation/assets/frameworks/togaf/g178_2%20-%20Value%20Streams.pdf — accessed 2026-10-14
8. Business Architecture Guild, "Business Architecture Reference Model Workshop" (2019) — https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf — accessed 2026-10-14
9. Scaled Agile, "Development Value Streams" — https://framework.scaledagile.com/development-value-streams — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![A9 sample: online shop order-to-doorstep current-state map with process boxes, queues and a timeline of process time against waiting time](/samples/A9-lean-value-stream-map.svg)
*Sample pending (generated by the renderer from `examples/`).*
