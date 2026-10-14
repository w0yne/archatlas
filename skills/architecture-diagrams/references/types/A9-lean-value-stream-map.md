# Lean Value-Stream Map (精益价值流图)
<!-- Generated from content/en/types/A9-lean-value-stream-map.md by tools/build_skill_refs.py. Do not edit. -->
> Where do time and waste sit in today's flow of work and information for one product or service family, and what should the future flow be?
Scope: One product or service family, door to door from trigger to delivery, current state and (separately) future state, with process times, waits and a timeline Neighbours: A2, A5, E4, G4, A8.

## Meaning
- **Question:** where does the time go between trigger and delivery, how much of it is real work, and what should the future flow look like?
- **Viewpoint:** operational flow and performance of one product or service family, observed where the work happens. LEI defines value-stream mapping as "diagraming every step involved in the material and information flows needed to bring a product from order to delivery"; "it shows the linkage between material flow and information flow. No other tool does this". In 42010 terms it frames the concern "lead time and waste" for process owners. No ArchiMate viewpoint, no TOGAF artifact, no C4 model level.
- **Deeper meaning:** it is a learning-to-see exercise, not a drawing exercise: "Having a perfectly drawn current state map is not the point". A current-state map is always paired with a future-state map and an implementation plan.
- **Leaves out:** physical layout (deliberately postponed), detailed task logic and decisions, capabilities and stakeholder value.
- **Definition used here:** this is the Lean sense of "value stream" (Womack and Jones; mapping method by Rother and Shook). It is a different diagram from the business-architecture A2 Value Stream, which has no times. TOGAF notes that the Lean value stream exists to analyse and improve the flow of information or materials and is not suited to cross-mapping stages to capabilities; the Business Architecture Guild says its value streams are not Lean value streams. SAFe's "development value stream" is a third, looser sense.
- **Metric used here:** activity ratio (flow efficiency) = ΣPT ÷ total lead time; lead time includes process time, so wait = LT − PT.

## When to use and how to choose
- **Audience:** process owners, operations and improvement teams and the people who do the work, plus suppliers and customers.
- **Scenarios:** order to doorstep (why a 20-minute job takes a day and a half: sum PT and waits, lead time, activity ratio); support query to resolution; returns; software delivery from ticket and pipeline timestamps; a future-state map with kaizen bursts.
- **When not to use:** without real observations or data ("go and see"); strategy-level value and capabilities (A2); system structure (C family); exceptions and branching logic (A5, E family).
- **vs neighbours:**
  - **A2 Value Stream** for how value reaches a stakeholder; never put times there.
  - **A5 BPMN Process** for task order, decisions, exceptions.
  - **E4 Swimlane** for who or which system does each step; A9 shows how long work sits.
  - **G4 Delivery Pipeline** for the build and release stages; A9 measures the waiting around them.
  - **A8 Roadmap** for a multi-step change plan.

## Notation and elements
- **Formal or informal:** a method with a de-facto LEI icon set (downloadable) but no ISO notation. With readers who do not know Lean icons, use labelled boxes and a legend.
- **Required:**
  - **Supplier** (top left) and **customer** (top right, with demand rate or takt).
  - **Process boxes** left to right, one per area of continuous flow; a box "stops wherever processes are disconnected and the material flow stops".
  - **Data box** under each process: cycle or process time (C/T, PT), changeover (C/O), uptime, %C&A (percent complete and accurate), and people (office) or availability (manufacturing).
  - **Inventory or queue triangles** between boxes, with quantity or days waiting.
  - **Information flow** along the top: who schedules or releases work; manual arrows straight, electronic arrows zig-zag. A map that ignores information flow "is like a piece of sheet music that just lists notes randomly".
  - **Timeline ladder** at the bottom: wait on the upper rungs, PT on the lower rungs; totals at the right: total lead time, ΣPT, activity ratio, and rolled %C&A for office work.
- **Optional:** push arrows (striped) and supermarket, FIFO or kanban icons for pull; kaizen bursts on the future-state map.
- **Legend:** icons used, units (minutes, hours, days) and "current state, mapped on `<date>`", with the source of the numbers.
- **Naming:** process boxes named as work done ("Pick", "Pack"), not by department; one time unit per row of numbers.

## Best practices and anti-patterns
### Best practices
1. **One product or service family, one lead, door to door,** capturing both work flow and information flow.
2. **Walk the flow and measure it** where the work happens instead of estimating in a meeting room.
3. **Draw the current state quickly, then the future state;** nest 30/60/90-day actions inside an 18–24-month future state.
4. **Show waits as well as work;** waste hides in the waiting, and the timeline must show both.
5. **Look for a flow solution within the existing layout first;** layout analysis comes later.

### Anti-patterns
1. **Recording only process time,** so the waits that make up most of the lead time disappear.
2. **Numbers guessed in a meeting room** instead of observed or taken from system data.
3. **Omitting the information flow**.
4. **A current-state map with no future state or plan**.
5. **Mixing in business-architecture content,** such as capabilities under process boxes; that is A2. Also avoid departments as boxes, long return lines and unexplained icons.

## Drawing recipe
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

## Evidence in a code repository
- **Useful for digital work:** timestamps in order or ticket status histories, CI/CD pipeline logs, PR open → merge → deploy times, and queue or backlog ages give lead time, PT and wait per step.
- **Process boxes:** board columns, issue labels and workflow state enums (`placed → paid → picked → packed → shipped`).
- **%C&A proxies:** rework counts such as reopened tickets, failed builds or orders returned to an earlier state.
- **Must come from people:** manual or offline steps (packing at the warehouse, carrier collection), true touch time, reasons for waiting, and the future state. State the sample period.

## Guided-mode questions
1. Is the question time and waste in a flow, or stakeholder value and capabilities? (time and waste; otherwise switch to A2)
2. Which product or service family, with which start and end points? (standard parcel orders, checkout to carrier hand-over)
3. Where do the numbers come from, and for which period? (system timestamps for the last 4 weeks, plus observed touch times)
4. Current state, future state, or both side by side? (both, current first)
5. Can the audience read Lean icons? (no: labelled boxes plus a legend)

## Template
Model template: `assets/templates/A9.json` · Layout template: `tree` · process steps are `task` nodes in one left-to-right row with a `queue` node between steps; the process data box goes in the node `sub` or `attributes`; totals (lead time, processing time, activity ratio) go in `meta.description` because the renderer draws no timeline row yet.

## Sample
Figure: `samples/A9-lean-value-stream-map.svg` (published with the site)
