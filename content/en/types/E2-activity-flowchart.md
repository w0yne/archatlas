---
code: E2
slug: activity-flowchart
family: E
names:
  en: Activity diagram or flowchart
  zh: 活动图 / 流程图
  aliases:
    en: [activity diagram, UML activity diagram, program flowchart, control flow diagram, control-flow diagram, process flow diagram (informal), workflow diagram (informal)]
    zh: [活动图, UML 活动图, 程序流程图, 控制流图, 控制流程图, 处理逻辑图]
question: What steps does this one behaviour go through, where does it decide, where does it run in parallel, and where does it end?
audiences: [developers, business]
levels: [logical]
phases: [design, build]
scope: One behaviour (a use case, request handler, job or procedure), about 8–20 nodes, optionally with up to 4–5 partitions
formal: {kind: standard, ref: 'OMG UML 2.5.1 activity diagrams; ISO 5807:1985 flowchart symbols'}
neighbours: [A5, D2, E1, E3, E4]
status: draft
---

# Activity Diagram / Flowchart (活动图 / 流程图)

> The steps, decisions, parallel branches and outcomes of one procedure, drawn as a flow of control from a single start to named ends.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** what steps does this behaviour go through, where does it decide, where does it run in parallel, and where does it end?
- **Viewpoint:** the control-flow (and optionally object-flow) view of one behaviour: the "algorithm or procedure" view of conditions, branching, concurrency and termination [8][9].
- **Two dialects:** the **UML activity diagram** (OMG UML 2.5.1 [3]) and the **classic flowchart**, whose documentation symbols for data, program and system flowcharts are standardised in ISO 5807:1985 [1][2]. Do not mix their shapes in one diagram.
- **Token semantics:** since UML 2, activities follow token-flow semantics inspired by Petri nets: a node executes when tokens arrive on its incoming edges [4][5]. This is why a join must never merge alternatives.
- **Leaves out:** the order of messages between collaborating participants (E1), the states of one object (E3), business events and pools (A5), and data structure (D1).
- **Definition used here:** "activity diagram" means UML notation; "flowchart" means the informal or ISO style. Arrows mean "control passes to" (or, for object flows, "data passes to"), never "calls" or "depends on".

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** developers, testers, analysts; business readers if it stays simple.
- **Scenarios:** request-handling logic (validate, check stock, query quotes in parallel, merge, confirm or fall back); a batch or ETL step with error routes; a rule such as automatic refund approval; deriving test paths (each branch is a test case); a runbook.
- **When not to use:** many actors handing work over (E4, A5); an entity's status (E3); a whole system on one page (split by use case); trivial linear steps (use a numbered list).
- **vs neighbours:**
  - **E3 State Machine** for a long-lived reactive thing; E2 for a procedure that runs to completion.
  - **E4 Swimlane** when hand-offs are the point (E4 is essentially E2 with partitions; a few partitions are fine here).
  - **A5 BPMN** for business audiences, business events or automation.
  - **E1 Sequence** when who talks to whom, in what order, matters more than decision logic.
  - **D2 Data Flow** when the arrows are data, not control.
-->
- **Audience:** developers, testers and analysts; business readers if the diagram stays simple.
- **Classic scenarios:**
  1. Request-handling logic: validate the order, check stock, query pricing and shipping quotes in parallel, merge, confirm or fall back.
  2. A batch job or ETL step: read, transform, validate, write, with error routes.
  3. A rule or eligibility check, such as automatic refund approval.
  4. Deriving test paths: each decision branch becomes a test case.
  5. A runbook: onboarding a new seller or restoring a failed import.
- **When not to use:** many actors handing work to each other as the main point (E4, A5); an entity's status as the point (E3); a whole system's behaviour on one page (split by use case); trivial linear steps, where a numbered list is clearer.
- **vs neighbours:**
  - Choose **E3 State Machine** when the same object reacts to events over its life; choose E2 when a procedure runs to completion.
  - Choose **E4 Swimlane** when responsibility hand-offs are the point. UML activity diagrams support *activity partitions* (swimlanes) natively [9], so E4 is essentially E2 with partitions; a few partitions are fine here.
  - Choose **A5 BPMN** for business audiences, standard business events, or automated business processes. Studies compare BPMN and UML activity diagrams for novice readability [10][11]; only the secondary summaries were read.
  - Choose **E1 Sequence** when who talks to whom, and in what order, matters more than the decision logic.
  - Choose **D2 Data Flow** when the arrows are data, not control.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** UML activity diagrams are formal [3]; the flowchart is ISO-standardised for symbols but used informally everywhere.
- **Required (UML):**
  - **Initial node** (filled circle), exactly one.
  - **Actions** (rounded rectangles), named verb plus object.
  - **Control flows** (arrows).
  - **Final nodes:** activity final (bullseye) ends the whole activity; flow final (circle with X) ends only one path.
- **Decision and merge:** a diamond. Each outgoing decision edge has a bracketed guard such as `[in stock]` or `[else]`. A merge rejoins alternatives without synchronising [8][12].
- **Fork and join:** a heavy bar. A fork starts concurrent flows; a join waits for all incoming flows [8][5].
- **Optional:** object nodes and object flows (data passed between actions); activity partitions (swimlanes, vertical or horizontal) [9]; interruptible regions; call-behaviour actions (rake symbol) for sub-activities; accept-event and send-signal actions; notes.
- **ISO 5807 shapes** (classic flowchart) [1]: terminator, process, decision, input/output (parallelogram), predefined process, connector, document, stored data.
- **Level of detail:** one behaviour, about 8–20 nodes; extract sub-activities beyond that.
- **Naming:** actions are verb plus object; guards are short Boolean conditions; ends are named outcomes ("Order confirmed", "Escalated to support").

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **One entry, explicit exits:** name every final outcome.
2. **Guard every decision branch,** with mutually exclusive, complete guards (use `[else]`) [8].
3. **Fork and join only for real concurrency;** use decision and merge for alternatives.
4. **Keep the main path straight** (top to bottom or left to right); push exceptions to the side or into a separate figure.
5. **Use call-behaviour actions** to keep diagrams small, and write the diagram as code (Mermaid, PlantUML) so it can be reviewed and diffed [6][7].

### Anti-patterns
1. **Decision branches without conditions,** or with overlapping conditions.
2. **A join used to merge alternatives,** which deadlocks under token semantics [5].
3. **Mixed symbol systems,** such as ISO parallelograms inside a UML activity [1][3].
4. **Spaghetti routing:** long lines folding back, flows that cross repeatedly.
5. **The whole system in one diagram,** or many actors without partitions.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [uml-diagrams.org: Activity diagram controls](https://www.uml-diagrams.org/activity-diagrams-controls.html) and [UML Activity Diagrams](https://www.uml-diagrams.org/activity-diagrams.html) — precise definitions of initial, final, decision, merge, fork, join and partitions, with worked examples.
- [Sparx Systems: Activity Diagram, UML 2 tutorial](https://sparxsystems.com/resources/tutorials/uml2/activity-diagram.html) — a concise practitioner reference with guarded decisions, forks, joins and partitions.
- [PlantUML activity diagram (new syntax)](https://plantuml.com/activity-diagram-beta) — start/stop, conditions, loops, partitions and notes as text; a good target for generated diagrams. Open-source tool.
- [Mermaid flowchart syntax](https://mermaid.ai/open-source/syntax/flowchart.html) — the most widely embedded flowchart syntax; renders in many code hosts and doc sites.
- [ISO 5807:1985 preview](https://cdn.standards.iteh.ai/samples/11955/1b7dd254a2a54fd7a89d616dc0570e18/ISO-5807-1985.pdf) — the authoritative classic symbol set. Preview only; the standard is copyrighted.
- [Visual Paradigm: activity diagrams vs BPMN](https://guides.visual-paradigm.com/a-comparative-analysis-of-activity-diagrams-and-bpmn-in-uml/) — a side-by-side guide for choosing. Vendor guide.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
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

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Control flow:** handler and service functions with `if/switch` branches, loops, `try/except` paths, and concurrency (`asyncio.gather`, futures, thread pools, fan-out to queues).
- **Declared flows:** workflow and pipeline definitions (YAML stage lists, Step Functions or Airflow DAGs).
- **Switches:** feature flags that select a path.
- **Branch inventory:** test cases often enumerate the branches.
- **Must come from people:** which branches matter to the audience, and business names for technical conditions.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which behaviour is this (one use case, request handler or job), and what triggers it? (the checkout handler, triggered by "place order")
2. Which outcomes or end states should be shown? (every named exit, at most 4)
3. Happy path only, or with key alternative and error branches? (main alternatives inline, errors in a separate figure)
4. Is more than one actor or system involved; add swimlanes or switch to E4 or BPMN? (up to 3 partitions here, otherwise E4)
5. UML activity notation or classic flowchart symbols; does the audience expect BPMN? (UML activity)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/E2.json` · Layout template: `lanes` · actions are `task` nodes, decisions and merges are `gateway` nodes, forks and joins are `band` nodes, `initial` and `final` mark start and end; partitions are `lane` groups; control flows are edges of kind `call` with the guard as `label`, and object flows use kind `data`.

## Sources {#sources}
<!-- skill: omit -->
1. ISO 5807:1985 — https://www.iso.org/standard/11955.html — accessed 2026-10-14
2. ISO 5807:1985 preview (iTeh) — https://cdn.standards.iteh.ai/samples/11955/1b7dd254a2a54fd7a89d616dc0570e18/ISO-5807-1985.pdf — accessed 2026-10-14
3. OMG, UML 2.5.1 (formal/17-12-05) — https://www.omg.org/spec/UML/2.5.1/About-UML — accessed 2026-10-14
4. Sparx Systems Central Europe, "UML activity diagram: activities and connections" (token semantics from Petri nets) — https://www.sparxsystems.eu/languages/uml/diagrams/activitydiagram/ — accessed 2026-10-14
5. "An ASM Semantics of Token Flow in UML 2 Activity Diagrams" (ResearchGate) — https://www.researchgate.net/publication/220810272_An_ASM_Semantics_of_Token_Flow_in_UML_2_Activity_Diagrams — accessed 2026-10-14
6. Mermaid, "Flowcharts Syntax" — https://mermaid.ai/open-source/syntax/flowchart.html — accessed 2026-10-14
7. PlantUML, "Activity Diagram (new syntax)" — https://plantuml.com/activity-diagram-beta — accessed 2026-10-14
8. uml-diagrams.org, "UML activity diagram controls" — https://www.uml-diagrams.org/activity-diagrams-controls.html — accessed 2026-10-14
9. uml-diagrams.org, "UML Activity Diagrams" (partitions and swimlanes) — https://www.uml-diagrams.org/activity-diagrams.html — accessed 2026-10-14
10. Visual Paradigm Guides, "A Comparative Analysis of Activity Diagrams and BPMN in UML" — https://guides.visual-paradigm.com/a-comparative-analysis-of-activity-diagrams-and-bpmn-in-uml/ — accessed 2026-10-14
11. "A Comparison of BPMN and UML 2.0 Activity Diagrams" (ResearchGate) — https://www.researchgate.net/publication/228965384_A_Comparison_of_BPMN_and_UML_20_Activity_Diagrams — accessed 2026-10-14
12. Visual Paradigm Online, "Activity Diagram Tutorial" (fork and join definitions) — https://online.visual-paradigm.com/diagrams/tutorials/activity-diagram-tutorial/ — accessed 2026-10-14
13. Sparx Systems, "Activity Diagram — UML 2 Tutorial" — https://sparxsystems.com/resources/tutorials/uml2/activity-diagram.html — accessed 2026-10-14

Note: the UML 2.5.1 clause text was not read first-hand; element semantics come from sources 4, 8, 9 and 12 and are not verified against the primary text.

## Sample {#sample}
<!-- skill: path only -->
![E2 sample: online shop checkout activity flow with stock check, parallel price and shipping quote branches, payment decision and named outcomes](/samples/E2-activity-flowchart.svg)
*Sample pending (generated by the renderer from `examples/`).*
