# State Machine Diagram (状态机图)
<!-- Generated from content/en/types/E3-state-machine.md by tools/build_skill_refs.py. Do not edit. -->
> What states can this one thing be in, which events move it between states, what happens on each move, and which moves are impossible?
Scope: One entity, job, connection or component over its whole life, one diagram per entity Neighbours: A5, D1, E1, E2.

## Meaning
- **Question:** what states can one thing be in, which events or conditions move it between states, what happens on each move, and which moves are impossible? Everything not drawn is implicitly forbidden, so the diagram finds gaps (no way out of "Failed").
- **Origin:** finite-state machines; Harel statecharts add nested states, parallel regions and broadcast. UML 2.5.1 state machines, W3C SCXML and XState follow them.
- **Definition used here:** *behavioural* state machine = how an entity reacts to events (default); *protocol* state machine = legal order of operations, labels `[pre] operation / [post]`.
- **Leaves out:** steps inside a state (E2), message exchange (E1), other entities' states (one diagram each), data structure (D1).
- **Unverified:** UML 2.5.1 clause numbers; pseudostate rules come from secondary sources.

## When to use and how to choose
- **Audience:** developers and testers (transitions, guards), product owners (business lifecycles in plain events), operations (job or connection states).
- **Scenarios:** a business object lifecycle (order `Created → Paid → Shipped → Delivered`, plus `Cancelled`, `Refunded`); asynchronous jobs (`Queued → Running → Succeeded/Failed` with retry, pause, cancel); protocol or connection behaviour; UI component behaviour (idle, typing, sending, error); finding impossible transitions and missing terminal states.
- **When not to use:** a procedure with no persistent state (E2); several unrelated objects on one page (draw several); states that are really workflow steps owned by different people (A5 or E4, plus a small E3 for the case object).
- **vs neighbours:**
  - **E2 Activity** for a run-to-completion procedure.
  - **E1 Sequence** for one scenario's messages.
  - **A5 BPMN** / **E4 Swimlane** for work across actors.
  - Pair with **D1 ER**: every entity with a `status` column deserves a small E3.

## Notation and elements
- **Formal or informal:** formal in UML and SCXML; also common as informal "status lifecycle" drawings. Notation follows UML 2.5.1 as presented in with statechart concepts from.
- **Required:**
  - **States:** rounded rectangles named as conditions ("Awaiting payment", not "Pay").
  - **Initial pseudostate:** filled circle, at most one per region, with one outgoing transition that may have an effect but no trigger or guard.
  - **Transitions:** arrows labelled `event [guard] / effect`.
  - **Final state(s):** bullseye, where the lifecycle can end.
- **Optional, powerful:**
  - **Composite (nested) states** so shared exits (cancel) are drawn once from the superstate.
  - **Orthogonal regions** (parallel states, separated by a dashed line).
  - **Entry / exit / do behaviours** inside a state.
  - **Choice and junction pseudostates,** fork/join into or out of regions, **history** (shallow, deep), entry/exit points, terminate.
  - **Timed transitions** such as `after 30 s`.
- **Arrow semantics:** when the event occurs and the guard holds, move from source to target and perform the effect. It is not data flow and not a call.
- **Legend:** if readers do not know UML, explain `event [guard] / effect` and any colour (terminal-success, terminal-failure).
- **Naming:** states are adjectives or participles ("Pending", "Approved"); events are past-tense facts or commands ("PaymentReceived", "cancel"); guards are Boolean.

## Best practices and anti-patterns
### Best practices
1. **One entity, one diagram.** State its identity and its source of truth (for example `order.status` in the order service).
2. **Name states as conditions and events as occurrences.** Never one verb for both ("Review" vs "In review").
3. **Draw every terminal and error state and a way out of each non-terminal state** (cancel, timeout, retry).
4. **List each state's meaning in one line and name forbidden transitions** in a note when they matter ("Delivered to Cancelled is not allowed; use Refund"). Kubernetes does this well for Pod phases.
5. **Use hierarchy and parallel regions instead of combinatorial flat states,** Harel's original motivation. Keep the model executable (SCXML, XState) where possible so the diagram stays true.

### Anti-patterns
1. **States named as actions** ("Approve") or events named as states.
2. **Missing terminal or failure states;** no recovery from "Failed".
3. **A mega-diagram mixing several objects' states,** or workflow steps owned by different people.
4. **Overlapping or incomplete guards** on transitions with the same trigger.
5. **Boolean-flag soup:** several flags that imply states nobody drew. Also drawing only the enum: a list of statuses is not a state machine without its transitions.

## Drawing recipe
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

## Evidence in a code repository
- **States:** status enums, database check constraints, state-name constants.
- **Transitions:** guard code such as `if status in (...)` before an update, service methods named `pause`, `resume`, `cancel`, `retry`, workflow definitions (XState, SCXML, Step Functions, Temporal, YAML) and tests that assert transitions.
- An enum lists states, not transitions: trace every writer of the status field. Mark a transition found in only one place as *inferred*.
- **Must come from people:** intended but unimplemented transitions and the business meaning of each state.

## Guided-mode questions
1. Which entity's lifecycle, and where is its status stored? (the entity with the most status columns, e.g. the order)
2. Current behaviour from code, or intended target design? (current, with gaps marked)
3. Which exceptional paths must appear: cancel, timeout, retry, pause/resume, manual override? (cancel, timeout, retry)
4. Show forbidden transitions explicitly? (yes, as a short note)
5. Who reads it: business readers (plain states and events) or engineers (`event [guard] / effect`, nested states)? (engineers)

## Template
Model template: `assets/templates/E3.json` · Layout template: `statechart` · states are `state` nodes (`initial` and `final` for the pseudostates), composite states are `frame` groups, each transition is an edge of kind `call` with `label` = `event [guard] / effect`; `evidence.status` marks verified versus inferred transitions.

## Sample
Figure: `samples/E3-state-machine.svg` (published with the site)
