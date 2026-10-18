# Business Process Diagram, BPMN (业务流程图 / BPMN 泳道图)
<!-- Generated from content/en/types/A5-bpmn-process.md by tools/build_skill_refs.py. Do not edit. -->
> How does one instance of a piece of business work run from trigger to outcome: who does each step, where does it branch, and how does it talk to outside parties?
Scope: One business process (one kind of instance) at one level of decomposition, with its participants as pools and its performers as lanes. Neighbours: A1, A2, A6, A9, E1, E2, E3, E4.

## Meaning
A BPMN process diagram answers "how does one order, request or case flow from its trigger to one of its outcomes, and who does each step?" It serves a behavioural (process) viewpoint in ISO/IEC/IEEE 42010 terms. TOGAF calls it a Process Flow diagram, a Phase B Business Architecture artifact. ArchiMate shows the same process as a single Business Process element, and BPMN details it. The C4 model has no process level. BPMN itself excludes organisation models, functional breakdowns, data models, strategy and business rules, and "is not a data flow language".

**Definition used here:** the current version is **BPMN 2.0.2** (OMG, January 2014). ISO/IEC 19510:2013 is identical to **BPMN 2.0.1**, not 2.0.2; the notation is the same, and 2.0.2 adds clarifications only. A **pool** is a participant (an independent party or process). A **lane** is a partition inside one pool (a role, department or system).

**Deeper meaning:** a BPMN process is defined by its **instance**: one order, request or claim flows from a start event to one of several **end states**. Make the end states explicit, because they are the business outcomes. The specification places organisational models and resources, functional breakdowns, data and information models, strategy and business rules **out of scope**, and BPMN is not a data-flow language; use A1, B3, D1, D2 or a rules table for those.

## When to use and how to choose
- **Audience:** process owners, analysts, operations, auditors; developers and testers who automate or verify the process. Executives need only a one-page top level of collapsed sub-processes.
- **Scenarios:** as-is / to-be process redesign; online-shop order-to-shipment with the customer and payment provider as external pools; automation scoping (user task vs service task); deriving acceptance tests (one path from start to an end state = one test).
- **When not to use:** the reader needs *what* the business does (A1, A2); the question is the customer's experience (A6); the flow is mostly system-to-system calls (E4, E1); the work is unstructured case work with no fixed order (a state view, E3, usually communicates it better); or the process is trivial and the readers have never seen BPMN.
- **vs neighbours:**
  - Choose **A2 value stream** when the question is which value stages exist, without control flow or roles.
  - Choose **A6 journey map** for the customer's experience; A5 is the organisation's logic behind it.
  - Choose **E4 swimlane flow** when lanes are systems and readers are engineers. A5 has formal semantics (pools, message flows); E4 is an informal convention.
  - Choose **E1 sequence** for exact message order between software parts, **E3 state machine** for the lifecycle of one object.
  - Choose **E2 activity diagram / flowchart** (ISO 5807 symbols) for one performer and 5–8 steps, or readers new to BPMN.
  - Choose **A9** when the question is where waiting time builds up in a delivery process (Lean value-stream map), not who does which step.

## Notation and elements
- **Diagram kinds:** a *Process* diagram (one pool with lanes) or a *Collaboration* diagram (several pools linked by message flows); *Choreography* is rarely used for business readers.
- **Required:** start event (thin circle) labelled with its trigger; tasks (rounded rectangles, verb + object); exclusive (XOR) and parallel (AND) gateways (diamonds); one end event (thick circle) per distinct end state; one process pool with 2–5 lanes.
- **Optional:** collapsed sub-process ([+] marker), call activity, intermediate events (double circle), data object / data store, text annotation, black-box pools for external parties.
- **Conformance level:** stay within the **Descriptive** sub-class for business readers. Loop and multi-instance markers, inclusive and event-based gateways and most intermediate events belong to the **Analytic** class.
- **Sequence flow** (solid line, solid arrowhead) orders steps inside one pool; it may cross lanes but never a pool boundary.
- **Message flow** (dashed line, open circle at the start, open arrowhead) **only connects two different pools** and must not connect objects in the same pool.
- **Association** (dotted) links annotations and data to flow objects. Line styles of the three connectors must not be altered.
- **Size:** at most about 10 activities per process level; decompose models above 50 elements. For slides, 5–9 activities per page is a readability heuristic, not part of BPMN.
- **Naming**: activities verb + object ("Pick items"); message start "Receive order"; end events as end-state phrases ("Order shipped"); XOR gateway as a question ("Payment authorised?") with Yes/No gates; AND gateways unlabelled; message flows as nouns ("Payment request"); lanes as roles, never people.
- **Legend:** BPMN readers need none; business readers get a 4–6 item legend of the glyphs actually used.

## Best practices and anti-patterns
### Best practices

1. One interpretation from the printed page alone: explicit start and end events at every level, every node on a continuous path from start to end.
2. Left to right, happy path straight through the middle, splits and joins paired symmetrically, crossings removed by reordering lanes and pools.
3. One process pool with internal roles as lanes; external parties as black-box pools reached only by message flows.
4. A one-page top level of collapsed sub-processes, then one child page per sub-process.
5. Default shape sizes and minimal colour: at most one faint highlight, for example the happy path or the steps that change in a to-be.

### Anti-patterns

1. Sequence flow drawn between pools, or message flow between lanes of the same pool; both violate the specification.
2. One pool per department inside a single process, which breaks the instance and turns internal hand-offs into message flows.
3. Unlabelled end events and gateways: the model validates but tells the reader nothing.
4. Specialist glyphs shown to business readers without need; for example a message-start envelope read as "e-mail". Use a plain start circle plus a label unless the type changes the meaning.
5. Exceptions drawn into the main path until the happy path disappears; put them on boundary events or in a separate figure. Also avoid flowchart habits such as untyped diamonds and data flows drawn as sequence flows.

## Drawing recipe
1. Fix the frame: process name, trigger, what one instance is, 2–4 end states, as-is or to-be, business or technical audience.
2. Pick the kind: Process (one pool with lanes) or Collaboration (add black-box pools for external parties). For a single performer and non-BPMN readers, propose a plain flowchart; if the actors are mostly systems, propose E4.
3. List 5–9 top-level activities (verb + object) of the same instance; group anything beyond 10 into collapsed sub-processes with child pages.
4. Lanes: 2–5 roles or departments, never people; the lane with the first activity on top, the rest ordered to minimise crossings.
5. Layout left to right: happy path on one line in the main lane; branches above or below; joins symmetric to splits; external pools above or below, ordered by first contact, so message flows stay short and vertical.
6. Gateways: XOR as a question with Yes/No or end-state gates; AND unlabelled; every split joined unless each branch ends in its own end event.
7. Events and messages: start labelled with its trigger; one end event per end state; message flows only between pools, each a noun.
8. Text: about 5 words per label, no sentences in shapes, at most 2 annotations; the title carries the message and as-is / to-be.
9. Colour: black on white, one faint highlight at most, one neutral tint for black-box pools; the legend lists only glyphs used.

**Self-check**
- [ ] Every sequence flow stays inside one pool; every message flow joins two different pools.
- [ ] Every path runs from a labelled start event to a labelled end event.
- [ ] End states are distinct; XOR gateways are labelled, AND gateways are not.
- [ ] Activities are verb + object at one granularity, about 10 or fewer per page.
- [ ] Lanes are roles, departments or systems of one kind; no person names.
- [ ] No altered line styles and no home-made shapes.
- [ ] Every specialist glyph is needed and in the legend, or replaced by a plain symbol plus label.
- [ ] Flows read left to right with no long fold-back lines.
- [ ] The title states the process and as-is / to-be; no TBD or status notes on the figure.

## Evidence in a code repository
- **Strong:** executable BPMN files (`*.bpmn`, `*.bpmn20.xml`); workflow or orchestration definitions (step functions, durable workflows, DAGs, saga orchestrators); state enums with transition tables. Simplify them for business readers.
- **Medium:** status enums (candidate end states), roles and permissions (candidate lanes), queues, topics and webhooks (message flows to external pools), scheduled jobs (timer starts), approval and notification code, BDD feature files (paths).
- **Weak:** README, `docs/`, ADRs.
- **Ask people:** manual work outside systems, who really performs each step, human exception handling, as-is workarounds and the to-be intent. Keep code-derived vs interview-derived steps in notes, not on the figure.

## Guided-mode questions
1. Which process, what is one instance, and what are its possible outcomes? (main success outcome plus one rejection)
2. Current process (as-is) or target (to-be)? (to-be when designing a change)
3. Who reads it: business readers new to BPMN, or analysts and developers? (Descriptive BPMN shapes plus a small legend)
4. Which roles do the work, and which outside parties appear as separate pools? (one pool with lanes; external parties as black-box pools)
5. Happy path only, or main exceptions too? (happy path plus at most one key branch; errors in a separate figure)

## Template
Model template: `assets/templates/A5.json` · Layout template: `lanes` · groups of kind `pool` and `lane` become bands; `task`, `event` and `gateway` nodes are placed left to right per lane; `message` edges are routed only between pools.

## Sample
Figure: `samples/ai-service-assistant/A5/en/diagram.svg` (published with the site)
