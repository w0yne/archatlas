# Swimlane / Cross-functional Flowchart (泳道流程图)
<!-- Generated from content/en/types/E4-swimlane-cross-functional.md by tools/build_skill_refs.py. Do not edit. -->
> In this process, which role or system performs each step, and where does work or information pass from one to another?
Scope: One process from trigger to outcome, at most about 6 lanes and 20 steps, happy path Neighbours: A5, A6, A9, E1, E2, H1.
Named variant of E2; apply this reference's own recipe and checks.

## Meaning
- **Question:** in this process, which role or system performs each step, and where does work or information pass from one to another?
- **Viewpoint:** responsibility allocation over a flow. Rummler and Brache's point was the "white space on the organisation chart": most delays, errors and ownership gaps sit at hand-offs between functions, and lanes make each hand-off visible. In software work the lanes are often systems or services; the diagram then shows each system's own steps and the integration points between them. One axis is sequence over time, the other is actors.
- **Origin:** multi-column flow process charts of the 1940s; the term "swim lane" was popularised by Geary Rummler and Alan Brache in *Improving Performance* (1990); iGrafx brought it to computer-based modelling and trademarked the term in 1996; Visio 2007 called lanes "functional bands".
- **Leaves out:** message-level detail and timing (E1), business-grade semantics such as events, gateways and pools for separate organisations (A5), complex logic inside one actor (E2) and structure (C family).
- **Definition used here:** E4 is the *informal* cross-functional flowchart: plain flowchart shapes in lanes. The same idea is formal as BPMN pools and lanes (A5) and as UML activity partitions, "shown using a swimlane notation" (E2 with partitions).
- **Version note:** BPMN 2.0.2 is OMG formal/13-12-09; the ISO/IEC 19510:2013 edition is reported as identical to BPMN 2.0.1, not 2.0.2. This was read from secondary summaries, not the ISO text.

## When to use and how to choose
- **Audience:** process owners, analysts, developers, testers, operations; a bridge between business and IT.
- **Scenarios:** order fulfilment across customer, shop web app, payment provider, warehouse; integration between two applications (two BPMN pools with message flows); refund approval across support, finance and the payment provider; incident procedure across support, engineering, vendor; as-is vs to-be (count and remove hand-offs).
- **When not to use:** more than about 6 lanes or a flow crossing lanes at every step (merge or split); order of calls is the point (E1); the whole flow sits in one actor (E2); a standard is required for automation or compliance (A5).
- **E4 or A5:** choose **A5 BPMN** when the actors are business roles and the notation must carry BPMN semantics for owners or tooling; choose **E4** for a lightweight hand-off picture, especially with systems as lanes. A5 is the formal sibling, not the same drawing.
- **Other neighbours:** **E1** for call order and sync vs async; **E2** when lanes are incidental; **A6** for customer emotions; **C3** for static structure.
- Choose **A9 Lean value-stream map** when the question is where time is lost between steps (process and waiting time), not who performs each step.
- Choose **H1 RACI matrix** when the question is who is responsible, accountable, consulted or informed for each activity, regardless of order.

## Notation and elements
- **Formal or informal:** informal convention, aligned with flowchart and BPMN usage.
- **Required:**
  - **Lanes:** parallel bands, each labelled with one role, team or system at a consistent level.
  - **Start and end** (terminators).
  - **Steps:** rectangles named verb + noun, placed in the lane of whoever performs them.
  - **Flow arrows,** and **decisions** as diamonds with labelled exits.
- **Hand-off semantics:** an arrow that crosses a lane boundary is a hand-off of work or information. In BPMN, sequence flow stays inside one pool and message flow (dashed) connects different pools; never draw a sequence flow between pools. In an informal E4, mark cross-system interactions consistently, for example a dashed arrow labelled with the data passed.
- **Optional:** pools (lane groups per organisation or system), phase columns across the top, document or data symbols, wait/timer markers, small "example" cards (input, evidence, output) for business readers.
- **Orientation:** horizontal lanes with time left to right is most common and suits screens; vertical lanes suit tall pages. Choose one and keep it.
- **Naming:** lanes are roles or systems, not people; step labels have one verb and one noun.

## Best practices and anti-patterns
### Best practices
1. **Show the flow of work and keep it simple.** Few colours, consistent box sizes, time along one axis and actors along the other.
2. **Connect arrows to the sides of boxes, in the flow direction;** avoid top and bottom attachment that complicates the flow.
3. **Order lanes to minimise crossings:** initiator first, then actors in the order they engage; put heavily interacting systems next to each other.
4. **Label every hand-off with what passes** (document, request, event). Hand-offs are where problems live.
5. **Do not force it onto one page.** If a one-pager is required, draw a higher-level scope model first. Show the happy path and put errors in a separate figure.

### Anti-patterns
1. **Mixed lane levels:** a role, a team and a system in one diagram.
2. **A step placed in the wrong lane,** or a lane with no steps.
3. **Long lines that fold back across the page** instead of rearranging lanes.
4. **Unlabelled cross-lane arrows,** or BPMN symbols used without BPMN rules (a sequence flow between pools).
5. **A calendar or timeline scale mixed with step order,** more than about 6 lanes, or a ping-pong flow that crosses lanes every step. The lane and step counts are practitioner rules of thumb, not standards.

## Drawing recipe
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

## Evidence in a code repository
- **System lanes:** runnable units (services, workers, functions) found via entry points, Dockerfiles and infrastructure-as-code.
- **Steps:** handlers, jobs and workflow-stage definitions (YAML, Step Functions, Airflow).
- **Hand-offs:** queue and topic producers and consumers, outbound HTTP clients, webhooks, file drops.
- **Human lanes:** UI routes, admin pages, approval endpoints, roles in permission checks.
- **Must come from people:** the organisational role behind a UI action, manual steps, waiting times and the business meaning of each hand-off.

## Guided-mode questions
1. Which process, from trigger to outcome? One scenario or several variants? (the single most common scenario)
2. What are the lanes: roles, teams or systems; should two systems be separate pools? (systems, with separate pools for independent ones)
3. Strict BPMN for process owners or automation, or a plain cross-functional flowchart? (plain, with an offer to upgrade to A5)
4. Label hand-offs with the data or document passed; add example cards for business readers? (label hand-offs, no cards)
5. Happy path only, or with exceptions; current or target process? (happy path, current)

## Template
Model template: `assets/templates/E4.json` · Layout template: `lanes` · lanes become `lane` groups (independent systems wrap their lanes in a `pool` group), steps and decisions are nodes with `parent` = their lane, flow arrows are edges (`call`), and cross-system hand-offs use kind `message` with a `label` naming what passes.

## Sample
Figure: `samples/ai-service-assistant/E4/en/diagram.svg` (published with the site)
