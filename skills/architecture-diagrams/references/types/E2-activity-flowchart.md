# Activity Diagram / Flowchart (活动图 / 流程图)
<!-- Generated from content/en/types/E2-activity-flowchart.md by tools/build_skill_refs.py. Do not edit. -->
> What steps does this one behaviour go through, where does it decide, where does it run in parallel, and where does it end?
Scope: One behaviour (a use case, request handler, job or procedure), about 8–20 nodes, optionally with up to 4–5 partitions Neighbours: E1, E3, E4, A5, D2.

## Meaning
- **Question:** what steps does this behaviour go through, where does it decide, where does it run in parallel, and where does it end?
- **Viewpoint:** the control-flow (and optionally object-flow) view of one behaviour: the "algorithm or procedure" view of conditions, branching, concurrency and termination.
- **Two dialects:** the **UML activity diagram** (OMG UML 2.5.1) and the **classic flowchart**, whose documentation symbols for data, program and system flowcharts are standardised in ISO 5807:1985. Do not mix their shapes in one diagram.
- **Token semantics:** since UML 2, activities follow token-flow semantics inspired by Petri nets: a node executes when tokens arrive on its incoming edges. This is why a join must never merge alternatives.
- **Leaves out:** the order of messages between collaborating participants (E1), the states of one object (E3), business events and pools (A5), and data structure (D1).
- **Definition used here:** "activity diagram" means UML notation; "flowchart" means the informal or ISO style. Arrows mean "control passes to" (or, for object flows, "data passes to"), never "calls" or "depends on".

## When to use and how to choose
- **Audience:** developers, testers, analysts; business readers if it stays simple.
- **Scenarios:** request-handling logic (validate, check stock, query quotes in parallel, merge, confirm or fall back); a batch or ETL step with error routes; a rule such as automatic refund approval; deriving test paths (each branch is a test case); a runbook.
- **When not to use:** many actors handing work over (E4, A5); an entity's status (E3); a whole system on one page (split by use case); trivial linear steps (use a numbered list).
- **vs neighbours:**
  - **E3 State Machine** for a long-lived reactive thing; E2 for a procedure that runs to completion.
  - **E4 Swimlane** when hand-offs are the point (E4 is essentially E2 with partitions; a few partitions are fine here).
  - **A5 BPMN** for business audiences, business events or automation.
  - **E1 Sequence** when who talks to whom, in what order, matters more than decision logic.
  - **D2 Data Flow** when the arrows are data, not control.

## Notation and elements
- **Formal or informal:** UML activity diagrams are formal; the flowchart is ISO-standardised for symbols but used informally everywhere.
- **Required (UML):**
  - **Initial node** (filled circle), exactly one.
  - **Actions** (rounded rectangles), named verb plus object.
  - **Control flows** (arrows).
  - **Final nodes:** activity final (bullseye) ends the whole activity; flow final (circle with X) ends only one path.
- **Decision and merge:** a diamond. Each outgoing decision edge has a bracketed guard such as `[in stock]` or `[else]`. A merge rejoins alternatives without synchronising.
- **Fork and join:** a heavy bar. A fork starts concurrent flows; a join waits for all incoming flows.
- **Optional:** object nodes and object flows (data passed between actions); activity partitions (swimlanes, vertical or horizontal); interruptible regions; call-behaviour actions (rake symbol) for sub-activities; accept-event and send-signal actions; notes.
- **ISO 5807 shapes** (classic flowchart): terminator, process, decision, input/output (parallelogram), predefined process, connector, document, stored data.
- **Level of detail:** one behaviour, about 8–20 nodes; extract sub-activities beyond that.
- **Naming:** actions are verb plus object; guards are short Boolean conditions; ends are named outcomes ("Order confirmed", "Escalated to support").

## Best practices and anti-patterns
### Best practices
1. **One entry, explicit exits:** name every final outcome.
2. **Guard every decision branch,** with mutually exclusive, complete guards (use `[else]`).
3. **Fork and join only for real concurrency;** use decision and merge for alternatives.
4. **Keep the main path straight** (top to bottom or left to right); push exceptions to the side or into a separate figure.
5. **Use call-behaviour actions** to keep diagrams small, and write the diagram as code (Mermaid, PlantUML) so it can be reviewed and diffed.

### Anti-patterns
1. **Decision branches without conditions,** or with overlapping conditions.
2. **A join used to merge alternatives,** which deadlocks under token semantics.
3. **Mixed symbol systems,** such as ISO parallelograms inside a UML activity.
4. **Spaghetti routing:** long lines folding back, flows that cross repeatedly.
5. **The whole system in one diagram,** or many actors without partitions.

## Drawing recipe
1. Name the behaviour (one use case or handler), its trigger and its outcomes; put them in the title.
2. Write the steps as an indented outline (sequence, `if/else`, `parallel`, `loop`) and validate it against code or rules. Show it to the user before drawing.
3. Choose one dialect: UML activity (default for software) or ISO flowchart (for organisations that expect it). Never mix.
4. Layout: the main path runs top to bottom (left to right on wide slides); decisions branch sideways and rejoin at a merge; parallel branches sit side by side between a fork bar and a join bar.
5. If more than one actor is involved, add at most 4–5 partitions; beyond that switch to E4 or A5.
6. Text: actions at most 5 words; guards at most 5 words in brackets; no paragraphs in shapes. Details go in numbered notes.
7. Colour: neutral fills; at most one accent (the error or exception path), explained in the legend.
8. Extract a sub-activity (rake symbol) when the diagram passes about 20 nodes.

**Self-check**
- [ ] Exactly one initial node; every path ends in a named final.
- [ ] Every decision edge has a guard; the guards are exclusive and complete.
- [ ] Forks pair with joins only where concurrency is real; merges are used for alternatives.
- [ ] One notation dialect, with a legend if readers are not UML-literate.
- [ ] No crossing or folded-back lines on the main path.
- [ ] At most about 20 nodes, or sub-activities are extracted.
- [ ] Partitions, if any, are real actors at a consistent level.
- [ ] Steps match code or rules, or the figure is marked as a design proposal.

## Evidence in a code repository
- **Control flow:** handler and service functions with `if/switch` branches, loops, `try/except` paths, and concurrency (`asyncio.gather`, futures, thread pools, fan-out to queues).
- **Declared flows:** workflow and pipeline definitions (YAML stage lists, Step Functions or Airflow DAGs).
- **Switches:** feature flags that select a path.
- **Branch inventory:** test cases often enumerate the branches.
- **Must come from people:** which branches matter to the audience, and business names for technical conditions.

## Guided-mode questions
1. Which behaviour is this (one use case, request handler or job), and what triggers it? (the checkout handler, triggered by "place order")
2. Which outcomes or end states should be shown? (every named exit, at most 4)
3. Happy path only, or with key alternative and error branches? (main alternatives inline, errors in a separate figure)
4. Is more than one actor or system involved; add swimlanes or switch to E4 or BPMN? (up to 3 partitions here, otherwise E4)
5. UML activity notation or classic flowchart symbols; does the audience expect BPMN? (UML activity)

## Template
Model template: `assets/templates/E2.json` · Layout template: `lanes` · actions are `task` nodes, decisions and merges are `gateway` nodes, forks and joins are `band` nodes, `initial` and `final` mark start and end; partitions are `lane` groups; control flows are edges of kind `call` with the guard as `label`, and object flows use kind `data`.

## Sample
Figure: `samples/E2-activity-flowchart.svg` (published with the site)
