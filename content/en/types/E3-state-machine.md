---
code: E3
slug: state-machine
family: E
names:
  en: State machine diagram
  zh: 状态机图
  aliases:
    en: [state diagram, statechart, state transition diagram, statechart diagram, state-transition diagram, lifecycle diagram, finite-state machine (FSM) diagram]
    zh: [状态图, 状态迁移图, 状态转换图, 生命周期图]
question: What states can this one thing be in, which events move it between states, what happens on each move, and which moves are impossible?
audiences: [developers, product]
levels: [logical]
phases: [design, build]
scope: One entity, job, connection or component over its whole life, one diagram per entity
formal: {kind: standard, ref: OMG UML 2.5.1 state machines (behavioral and protocol); Harel statecharts (1987); W3C SCXML 1.0 (2015) for the executable form}
neighbours: [A5, D1, E1, E2]
status: draft
---

# State Machine Diagram (状态机图)

> The lifecycle of one entity: its states, the events that move it between them, and, by omission, the moves that are not allowed.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
<!-- skill-text
- **Question:** what states can one thing be in, which events or conditions move it between states, what happens on each move, and which moves are impossible? Everything not drawn is implicitly forbidden, so the diagram finds gaps (no way out of "Failed").
- **Origin:** finite-state machines; Harel statecharts add nested states, parallel regions and broadcast. UML 2.5.1 state machines, W3C SCXML and XState follow them.
- **Definition used here:** *behavioural* state machine = how an entity reacts to events (default); *protocol* state machine = legal order of operations, labels `[pre] operation / [post]`.
- **Leaves out:** steps inside a state (E2), message exchange (E1), other entities' states (one diagram each), data structure (D1).
- **Unverified:** UML 2.5.1 clause numbers; pseudostate rules come from secondary sources.
-->
- **Question:** what states can this one thing be in, which events or conditions move it between states, what happens on each move, and which moves are impossible?
- **Viewpoint:** a behavioural view centred on one entity over its whole life, i.e. its protocol. Everything not drawn is implicitly forbidden, so the diagram finds gaps (no way out of "Failed") and supports idempotent, recoverable workflows [1][3].
- **Origin:** finite-state machines are classic automata theory. David Harel's statecharts (1987) added nested states, parallel regions and broadcast communication, because flat state diagrams explode in size [1][2][3]. UML state machines are based on Harel's statecharts; the current specification is UML 2.5.1 [4]. W3C published SCXML, an executable statechart notation, as a Recommendation on 1 September 2015 [7]; XState is a widely used statecharts-as-code library [8].
- **Leaves out:** the steps inside a state (E2), who exchanges which messages (E1), other entities' states (draw one diagram each) and data structure (D1).
- **Definition used here:** a *behavioural* state machine describes how an entity reacts to events. A *protocol* state machine describes the legal order of operations on a classifier, with labels `[precondition] operation / [postcondition]` [5][6]. This page covers both and uses the behavioural form by default. "State machine diagram" is the UML 2 name; "statechart diagram" is the UML 1.x name [5].
- **Not verified against the primary text:** UML 2.5.1 clause numbers. Pseudostate rules below are taken from uml-diagrams.org [12] and cross-checked against quoted UML 2.5.1 extracts on a reference card.

| Concept | What it says | Typical unit |
|---|---|---|
| State machine (E3) | Which conditions one entity can be in and how it moves | One entity or component |
| Activity / flowchart (E2) | The steps of a run-to-completion procedure | One procedure |
| Sequence (E1) | Messages of one scenario between participants | One scenario |
| BPMN process (A5) | Who does what, in order, across business roles | One business case |

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** developers and testers (transitions, guards), product owners (business lifecycles in plain events), operations (job or connection states).
- **Scenarios:** a business object lifecycle (order `Created → Paid → Shipped → Delivered`, plus `Cancelled`, `Refunded`); asynchronous jobs (`Queued → Running → Succeeded/Failed` with retry, pause, cancel); protocol or connection behaviour; UI component behaviour (idle, typing, sending, error); finding impossible transitions and missing terminal states.
- **When not to use:** a procedure with no persistent state (E2); several unrelated objects on one page (draw several); states that are really workflow steps owned by different people (A5 or E4, plus a small E3 for the case object).
- **vs neighbours:**
  - **E2 Activity** for a run-to-completion procedure.
  - **E1 Sequence** for one scenario's messages.
  - **A5 BPMN** / **E4 Swimlane** for work across actors.
  - Pair with **D1 ER**: every entity with a `status` column deserves a small E3.
-->
- **Audience:** developers and testers (transitions, guards), product owners (business lifecycles in plain events), operations (job or connection states).
- **Classic scenarios:**
  1. Business object lifecycle: an order `Created → Paid → Shipped → Delivered`, plus `Cancelled` and `Refunded`.
  2. Asynchronous jobs: `Queued → Running → Succeeded/Failed`, with retry, pause/resume and cancel. Kubernetes' Pod phases (`Pending, Running, Succeeded, Failed, Unknown`) are a public example [10].
  3. Protocol or connection behaviour, such as the TCP connection diagram in RFC 793 [11].
  4. UI component behaviour, e.g. a support-chat input: idle, typing, sending, error [8].
  5. Finding defects: impossible transitions seen in production, missing terminal states.
- **When not to use:** a procedure with no persistent state (E2); several unrelated objects on one page (draw several diagrams); states that are really workflow steps owned by different people (A5 or E4, plus a small E3 for the case object).
- **vs neighbours:**
  - Choose **E2 Activity** for a run-to-completion procedure; E3 for a long-lived, reactive thing.
  - Choose **E1 Sequence** for one scenario's messages; one scenario may drive several E3 transitions.
  - Choose **A5 BPMN Process** for a business process across actors; one BPMN task often changes the state of several entities.
  - Choose **E4 Swimlane** when the question is who hands work to whom.
  - Pair with **D1 ER**: every entity with a `status` column deserves a small E3 [9].

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** formal in UML and SCXML; also common as informal "status lifecycle" drawings. Notation follows UML 2.5.1 as presented in [12] with statechart concepts from [1][3].
- **Required:**
  - **States:** rounded rectangles named as conditions ("Awaiting payment", not "Pay").
  - **Initial pseudostate:** filled circle, at most one per region, with one outgoing transition that may have an effect but no trigger or guard [12].
  - **Transitions:** arrows labelled `event [guard] / effect`.
  - **Final state(s):** bullseye, where the lifecycle can end.
- **Optional, powerful:**
  - **Composite (nested) states** so shared exits (cancel) are drawn once from the superstate.
  - **Orthogonal regions** (parallel states, separated by a dashed line).
  - **Entry / exit / do behaviours** inside a state.
  - **Choice and junction pseudostates,** fork/join into or out of regions, **history** (shallow, deep), entry/exit points, terminate.
  - **Timed transitions** such as `after 30 s` [3][12].
- **Arrow semantics:** when the event occurs and the guard holds, move from source to target and perform the effect. It is not data flow and not a call.
- **Legend:** if readers do not know UML, explain `event [guard] / effect` and any colour (terminal-success, terminal-failure).
- **Naming:** states are adjectives or participles ("Pending", "Approved"); events are past-tense facts or commands ("PaymentReceived", "cancel"); guards are Boolean.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **One entity, one diagram.** State its identity and its source of truth (for example `order.status` in the order service).
2. **Name states as conditions and events as occurrences.** Never one verb for both ("Review" vs "In review").
3. **Draw every terminal and error state and a way out of each non-terminal state** (cancel, timeout, retry).
4. **List each state's meaning in one line and name forbidden transitions** in a note when they matter ("Delivered to Cancelled is not allowed; use Refund"). Kubernetes does this well for Pod phases [10].
5. **Use hierarchy and parallel regions instead of combinatorial flat states,** Harel's original motivation [1][3]. Keep the model executable (SCXML, XState) where possible so the diagram stays true [7][8].

### Anti-patterns
1. **States named as actions** ("Approve") or events named as states [12].
2. **Missing terminal or failure states;** no recovery from "Failed".
3. **A mega-diagram mixing several objects' states,** or workflow steps owned by different people.
4. **Overlapping or incomplete guards** on transitions with the same trigger.
5. **Boolean-flag soup:** several flags that imply states nobody drew. Also drawing only the enum: a list of statuses is not a state machine without its transitions.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Harel (1987), "Statecharts: a visual formalism for complex systems"](https://www.sciencedirect.com/science/article/pii/0167642387900359) — the primary source, with worked examples of hierarchy and orthogonality. © Elsevier; read only.
- [statecharts.dev, "What is a statechart?"](https://statecharts.dev/what-is-a-statechart.html) — the clearest modern explanation of nesting, parallel regions, guards, delayed transitions and history.
- [Kubernetes, "Pod Lifecycle"](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) — a precisely documented lifecycle that defines each phase in text next to the diagram. Documentation under CC BY 4.0.
- [RFC 793, TCP connection state diagram](https://www.rfc-editor.org/rfc/rfc793.txt) — a canonical protocol state machine with event/action labels, drawn in ASCII.
- [XState](https://github.com/statelyai/xstate) and the [W3C SCXML Recommendation](https://www.w3.org/news/2015/state-chart-xml-scxml-state-machine-notation-for-control-abstraction-is-a-w3c-recommendation/) — executable statecharts where the picture is generated from the model the code runs.
- [uml-diagrams.org, State Machine Diagrams](https://www.uml-diagrams.org/state-machine-diagrams.html) — a complete reference for pseudostates, regions and transition syntax.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Choose one entity and its source of truth (status field, enum, workflow engine); put both in the title, e.g. "Order lifecycle (order service, `order.status`)".
2. List states with a one-line meaning each; merge synonyms; separate states from steps.
3. List transitions as a table (from, event, guard, effect, to), including cancel, timeout, retry and pause/resume where they exist. Show the table to the user before drawing.
4. Group with hierarchy: for example "Active" containing "Running" and "Paused", so a shared exit is drawn once from the superstate.
5. Layout: initial pseudostate top-left; the main lifecycle as a left-to-right (or top-down) spine; terminal and error states along the bottom or right edge; retry and resume as short curved back-edges, not long loops.
6. Text: state names at most 3 words; transition labels at most 6 words (`event [guard]`); long effects go into a footnote table.
7. Colour: neutral fills; one accent for terminal-success and one for terminal-failure, explained in a legend that also explains the label syntax.
8. Add a short "forbidden transitions" note if any exist.

**Self-check**
- [ ] Exactly one entity; its source of truth is named.
- [ ] One initial pseudostate per region; at least one final state, or an explicit "never ends".
- [ ] Every state is a condition and every event an occurrence; no state named as an action.
- [ ] Every non-terminal state has an exit (cancel or timeout where applicable).
- [ ] Guards on same-event transitions are exclusive and complete.
- [ ] Hierarchy replaces repeated transitions where possible.
- [ ] Each transition matches code or a stated rule; inferred ones are marked.
- [ ] Forbidden transitions are stated where they matter.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **States:** status enums, database check constraints, state-name constants.
- **Transitions:** guard code such as `if status in (...)` before an update, service methods named `pause`, `resume`, `cancel`, `retry`, workflow definitions (XState, SCXML, Step Functions, Temporal, YAML) and tests that assert transitions.
- An enum lists states, not transitions: trace every writer of the status field. Mark a transition found in only one place as *inferred*.
- **Must come from people:** intended but unimplemented transitions and the business meaning of each state.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which entity's lifecycle, and where is its status stored? (the entity with the most status columns, e.g. the order)
2. Current behaviour from code, or intended target design? (current, with gaps marked)
3. Which exceptional paths must appear: cancel, timeout, retry, pause/resume, manual override? (cancel, timeout, retry)
4. Show forbidden transitions explicitly? (yes, as a short note)
5. Who reads it: business readers (plain states and events) or engineers (`event [guard] / effect`, nested states)? (engineers)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/E3.json` · Layout template: `statechart` · states are `state` nodes (`initial` and `final` for the pseudostates), composite states are `frame` groups, each transition is an edge of kind `call` with `label` = `event [guard] / effect`; `evidence.status` marks verified versus inferred transitions.

## Sources {#sources}
<!-- skill: omit -->
1. D. Harel, "Statecharts: a visual formalism for complex systems", *Science of Computer Programming* 8(3), 1987 — https://www.sciencedirect.com/science/article/pii/0167642387900359 — accessed 2026-10-14
2. Harel 1987 PDF (state-machine.com) — https://www.state-machine.com/doc/Harel87.pdf — accessed 2026-10-14
3. statecharts.dev, "What is a statechart?" — https://statecharts.dev/what-is-a-statechart.html — accessed 2026-10-14
4. OMG, UML 2.5.1 — https://www.omg.org/spec/UML/2.5.1/About-UML — accessed 2026-10-14
5. Wikipedia, "UML state machine" (behavioral vs protocol) — https://en.wikipedia.org/wiki/UML_state_machine — accessed 2026-10-14
6. uml-diagrams.org, "Protocol state machine diagrams" — https://www.uml-diagrams.org/protocol-state-machine-diagrams.html — accessed 2026-10-14
7. W3C, "State Chart XML (SCXML) … is a W3C Recommendation" (1 September 2015) — https://www.w3.org/news/2015/state-chart-xml-scxml-state-machine-notation-for-control-abstraction-is-a-w3c-recommendation/ — accessed 2026-10-14
8. XState (Stately) — https://github.com/statelyai/xstate — accessed 2026-10-14
9. QualiWare CoE, "TOGAF Artifacts" (Data Lifecycle diagram; TOGAF 10 naming not verified) — https://coe.qualiware.com/resources/togaf/togaf-artifacts/ — accessed 2026-10-14
10. Kubernetes, "Pod Lifecycle" — https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ — accessed 2026-10-14
11. IETF, RFC 793 "Transmission Control Protocol" (connection state diagram) — https://www.rfc-editor.org/rfc/rfc793.txt — accessed 2026-10-14
12. uml-diagrams.org, "UML State Machine Diagrams" — https://www.uml-diagrams.org/state-machine-diagrams.html — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![E3 sample: state machine of an order with initial and final states](/samples/E3-state-machine.svg)
*States of an order: Placed, Paid, Shipped and Cancelled, with one initial and one final state. Transitions are labelled event [guard] / effect, for example pay [amount ok] / reserve stock and cancel [before payment]; both a delivered order and a cancelled order reach the final state.*
