---
code: E4
slug: swimlane-cross-functional
family: E
names:
  en: Swimlane or cross-functional flowchart
  zh: 泳道流程图（跨职能流程图）
  aliases:
    en: [cross-functional flowchart, swimlane flowchart, Rummler-Brache diagram, swim-lane flowchart, functional flowchart, functional bands (Visio 2007)]
    zh: [跨职能流程图, 泳道流程图, 跨部门流程图, 职责流程图]
question: In this process, which role or system performs each step, and where does work or information pass from one to another?
audiences: [developers, operations, business]
levels: [logical]
phases: [design, operate]
scope: One process from trigger to outcome, at most about 6 lanes and 20 steps, happy path
formal: {kind: convention, ref: Informal cross-functional flowchart (Rummler-Brache tradition); formal equivalents are BPMN 2.0.2 pools and lanes and UML 2.5.1 activity partitions}
neighbours: [A5, A6, A9, E1, E2, H1]
status: draft
---

# Swimlane / Cross-functional Flowchart (泳道流程图)

> A flowchart split into parallel lanes, one per role or system, so every hand-off between them is visible.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** in this process, which role or system performs each step, and where does work or information pass from one to another?
- **Viewpoint:** responsibility allocation over a flow. Rummler and Brache's point was the "white space on the organisation chart": most delays, errors and ownership gaps sit at hand-offs between functions, and lanes make each hand-off visible [1][2]. In software work the lanes are often systems or services; the diagram then shows each system's own steps and the integration points between them. One axis is sequence over time, the other is actors [9].
- **Origin:** multi-column flow process charts of the 1940s; the term "swim lane" was popularised by Geary Rummler and Alan Brache in *Improving Performance* (1990); iGrafx brought it to computer-based modelling and trademarked the term in 1996; Visio 2007 called lanes "functional bands" [1][2][3].
- **Leaves out:** message-level detail and timing (E1), business-grade semantics such as events, gateways and pools for separate organisations (A5), complex logic inside one actor (E2) and structure (C family).
- **Definition used here:** E4 is the *informal* cross-functional flowchart: plain flowchart shapes in lanes [8]. The same idea is formal as BPMN pools and lanes (A5) and as UML activity partitions, "shown using a swimlane notation" (E2 with partitions) [4][7].
- **Version note:** BPMN 2.0.2 is OMG formal/13-12-09; the ISO/IEC 19510:2013 edition is reported as identical to BPMN 2.0.1, not 2.0.2 [4]. This was read from secondary summaries, not the ISO text.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** process owners, analysts, developers, testers, operations; a bridge between business and IT.
- **Scenarios:** order fulfilment across customer, shop web app, payment provider, warehouse; integration between two applications (two BPMN pools with message flows); refund approval across support, finance and the payment provider; incident procedure across support, engineering, vendor; as-is vs to-be (count and remove hand-offs).
- **When not to use:** more than about 6 lanes or a flow crossing lanes at every step (merge or split); order of calls is the point (E1); the whole flow sits in one actor (E2); a standard is required for automation or compliance (A5).
- **E4 or A5:** choose **A5 BPMN** when the actors are business roles and the notation must carry BPMN semantics for owners or tooling; choose **E4** for a lightweight hand-off picture, especially with systems as lanes. A5 is the formal sibling, not the same drawing.
- **Other neighbours:** **E1** for call order and sync vs async; **E2** when lanes are incidental; **A6** for customer emotions; **C3** for static structure.
- Choose **A9 Lean value-stream map** when the question is where time is lost between steps (process and waiting time), not who performs each step.
- Choose **H1 RACI matrix** when the question is who is responsible, accountable, consulted or informed for each activity, regardless of order.
-->
- **Audience:** process owners, analysts, developers, testers and operations. A good bridge between business and IT.
- **Classic scenarios:**
  1. Order fulfilment: customer, shop web app, payment provider and warehouse, from "place order" to "order shipped".
  2. Integration between two applications: each system's own steps plus the exchange points, equivalent to two BPMN pools with message flows.
  3. Refund approval across support, finance and the payment provider.
  4. Incident or on-call procedure across support, engineering and a vendor.
  5. As-is versus to-be improvement: count the hand-offs and remove the unnecessary ones [2].
- **When not to use:** more than about 6 lanes, or a flow that crosses lanes at every step (merge lanes or split the process); the order of calls and replies is the point (E1); the whole flow sits inside one actor (E2); a standard is required for automation or compliance (A5).
- **E4 or A5 (the one rule):** choose **A5 BPMN Process** when the protagonists are business roles and the notation must carry BPMN semantics (events, gateways, pools as participants, message flows) for business owners or tooling. Choose **E4** for a lightweight picture of hand-offs, especially with systems as lanes, for engineers. A5 is the formal sibling of the same drawing, not the same drawing.
- **vs other neighbours:**
  - Choose **E1 Sequence** when the order of calls and sync versus async is the point; E4 when steps and decisions inside each participant matter.
  - Choose **E2 Activity** when lanes are incidental and the logic is the point; E2 with partitions is formally the same diagram.
  - Choose **A6 Journey Map** when customer emotions and touchpoints matter (it has its own line of visibility).
  - Choose **C3 Container Diagram** for static structure, not flow.
  - Choose **A9 Lean value-stream map** when the question is where time is lost between steps (process and waiting time), not who performs each step.
  - Choose **H1 RACI matrix** when the question is who is responsible, accountable, consulted or informed for each activity, regardless of order.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** informal convention, aligned with flowchart and BPMN usage [6][8][9].
- **Required:**
  - **Lanes:** parallel bands, each labelled with one role, team or system at a consistent level.
  - **Start and end** (terminators).
  - **Steps:** rectangles named verb + noun, placed in the lane of whoever performs them.
  - **Flow arrows,** and **decisions** as diamonds with labelled exits.
- **Hand-off semantics:** an arrow that crosses a lane boundary is a hand-off of work or information. In BPMN, sequence flow stays inside one pool and message flow (dashed) connects different pools; never draw a sequence flow between pools [4][5][6]. In an informal E4, mark cross-system interactions consistently, for example a dashed arrow labelled with the data passed.
- **Optional:** pools (lane groups per organisation or system), phase columns across the top, document or data symbols, wait/timer markers, small "example" cards (input, evidence, output) for business readers.
- **Orientation:** horizontal lanes with time left to right is most common and suits screens; vertical lanes suit tall pages [1][9]. Choose one and keep it.
- **Naming:** lanes are roles or systems, not people; step labels have one verb and one noun [9].

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Show the flow of work and keep it simple.** Few colours, consistent box sizes, time along one axis and actors along the other [9].
2. **Connect arrows to the sides of boxes, in the flow direction;** avoid top and bottom attachment that complicates the flow [9].
3. **Order lanes to minimise crossings:** initiator first, then actors in the order they engage; put heavily interacting systems next to each other.
4. **Label every hand-off with what passes** (document, request, event). Hand-offs are where problems live [1][2].
5. **Do not force it onto one page.** If a one-pager is required, draw a higher-level scope model first [9]. Show the happy path and put errors in a separate figure.

### Anti-patterns
1. **Mixed lane levels:** a role, a team and a system in one diagram.
2. **A step placed in the wrong lane,** or a lane with no steps.
3. **Long lines that fold back across the page** instead of rearranging lanes.
4. **Unlabelled cross-lane arrows,** or BPMN symbols used without BPMN rules (a sequence flow between pools).
5. **A calendar or timeline scale mixed with step order,** more than about 6 lanes, or a ping-pong flow that crosses lanes every step. The lane and step counts are practitioner rules of thumb, not standards.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Wikipedia, "Swimlane"](https://en.wikipedia.org/wiki/Swimlane) — concise history and the horizontal versus vertical rationale. CC BY-SA.
- [Mindtools, "Swim Lane / Rummler-Brache Diagrams"](https://www.mindtools.com/abxyani/swim-lanerummler-brache-diagrams/) — the management framing of white space between functions.
- [Microsoft Support, "Create a cross-functional flowchart"](https://support.microsoft.com/en-us/visio/create-a-cross-functional-flowchart) — the de facto business-tool convention with phases and lanes.
- [Lucid: swimlane diagram tips with Alec Sharp](https://lucid.co/blog/webisodes-with-alec-sharp-swimlane-diagrams) — practitioner rules on axes, verb-noun labels and arrow attachment.
- [BPM Tips, "BPMN in practice: pools and lanes"](https://bpmtips.com/bpmn-in-practice-pools-and-lanes/) — common pool and lane mistakes; useful when upgrading an E4 to A5.
- [uml-diagrams.org, UML Activity Diagrams](https://www.uml-diagrams.org/activity-diagrams.html) — the same concept as activity partitions, for software-centric teams.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix the process boundary (trigger to outcome) and the lane granularity: roles, teams or systems, never a mix. Prefer at most 6 lanes. Put both in the title, e.g. "Place and ship an order, happy path".
2. List steps as a table (step, performer lane, input, output, next); verify system steps against code or docs; show it to the user before drawing.
3. Orientation: horizontal lanes with time left to right by default; vertical only for tall documents.
4. Order lanes to minimise crossings. If two independent systems interact, draw them as adjacent lane groups (pools) with a visible boundary.
5. Place steps column by column in time order; align parallel steps in one column; put each decision in the lane of the decider.
6. Hand-offs: a short arrow across the lane boundary, labelled with what is passed; a distinct style (dashed) for cross-system messages, explained in a legend.
7. Text: steps at most 5 words, lane labels at most 3 words; example cards, if any, sit outside the main flow and are labelled "example".
8. Colour: neutral alternating lane tints; at most one accent for cross-boundary hand-offs or the focus system.

**Self-check**
- [ ] Every lane is one actor at a consistent level (all roles or all systems).
- [ ] Every step sits in the lane of its performer.
- [ ] Every cross-lane arrow is a real hand-off and says what passes.
- [ ] Time runs along one axis; no backward folds or long detours.
- [ ] Decisions have labelled exits; start and end are explicit.
- [ ] At most about 6 lanes and 20 steps, or the process is split.
- [ ] If BPMN symbols are used, BPMN rules hold (message flows only between pools); otherwise consider A5.
- [ ] Happy path only, or error handling clearly separated.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **System lanes:** runnable units (services, workers, functions) found via entry points, Dockerfiles and infrastructure-as-code.
- **Steps:** handlers, jobs and workflow-stage definitions (YAML, Step Functions, Airflow).
- **Hand-offs:** queue and topic producers and consumers, outbound HTTP clients, webhooks, file drops.
- **Human lanes:** UI routes, admin pages, approval endpoints, roles in permission checks.
- **Must come from people:** the organisational role behind a UI action, manual steps, waiting times and the business meaning of each hand-off.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which process, from trigger to outcome? One scenario or several variants? (the single most common scenario)
2. What are the lanes: roles, teams or systems; should two systems be separate pools? (systems, with separate pools for independent ones)
3. Strict BPMN for process owners or automation, or a plain cross-functional flowchart? (plain, with an offer to upgrade to A5)
4. Label hand-offs with the data or document passed; add example cards for business readers? (label hand-offs, no cards)
5. Happy path only, or with exceptions; current or target process? (happy path, current)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/E4.json` · Layout template: `lanes` · lanes become `lane` groups (independent systems wrap their lanes in a `pool` group), steps and decisions are nodes with `parent` = their lane, flow arrows are edges (`call`), and cross-system hand-offs use kind `message` with a `label` naming what passes.

## Sources {#sources}
<!-- skill: omit -->
1. Wikipedia, "Swimlane" — https://en.wikipedia.org/wiki/Swimlane — accessed 2026-10-14
2. Mindtools, "Swim Lane/Rummler-Brache Diagrams" — https://www.mindtools.com/abxyani/swim-lanerummler-brache-diagrams/ — accessed 2026-10-14
3. Lucen Software, "Swimlane diagram – definitions, uses, examples" — https://www.lucensoftware.com/swimlane-diagram — accessed 2026-10-14
4. OMG, "About the Business Process Model and Notation Specification Version 2.0.2" — https://www.omg.org/spec/BPMN/2.0.2/About-BPMN — accessed 2026-10-14
5. BPM Tips, "BPMN in practice — pools and lanes" — https://bpmtips.com/bpmn-in-practice-pools-and-lanes/ — accessed 2026-10-14
6. HEFLO, "BPMN Pools vs Lanes Explained" — https://www.heflo.com/blog/bpmn-pools-and-lanes — accessed 2026-10-14
7. uml-diagrams.org, "UML Activity Diagrams" (activity partitions as swimlanes) — https://www.uml-diagrams.org/activity-diagrams.html — accessed 2026-10-14
8. Microsoft Support, "Create a cross-functional flowchart" — https://support.microsoft.com/en-us/visio/create-a-cross-functional-flowchart — accessed 2026-10-14
9. Lucid, "Webisodes with Alec Sharp: Swimlane Diagrams Tips, Tricks, and Best Practices" — https://lucid.co/blog/webisodes-with-alec-sharp-swimlane-diagrams — accessed 2026-10-14
10. A. Sharp, P. McDermott, *Workflow Modeling* (Google Books; background book behind the practices in [9], not read directly) — https://books.google.com/books/about/Workflow_Modeling.html?id=avcWp_0ZMyoC — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![E4 sample: online shop order fulfilment across customer, shop web app, payment provider and warehouse lanes with labelled hand-offs](/samples/E4-swimlane-cross-functional.svg)
*Sample pending (generated by the renderer from `examples/`).*
