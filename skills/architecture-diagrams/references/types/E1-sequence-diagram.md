# Sequence Diagram (时序图)
<!-- Generated from content/en/types/E1-sequence-diagram.md by tools/build_skill_refs.py. Do not edit. -->
> For one scenario, which participants exchange which messages in what order, and where does the flow branch, loop or wait?
Scope: One scenario (one trigger to one outcome), about 4–8 lifelines at one abstraction level, up to about 25 messages Neighbours: A5, C3, C4, C6, E2, E3, E4, F1, I1.

## Meaning
- **Question:** in this one scenario, which participants exchange which messages, in what order, and where does the flow branch, loop or wait?
- **Viewpoint:** the runtime view of a single scenario. It turns a static structure (C2, C3) into a story over time. arc42 section 6 "Runtime View" asks for exactly this, for the important scenarios only. The C4 model says dynamic diagrams "should be used sparingly" for interesting or recurring patterns with complicated interactions.
- **Deeper meaning:** a sequence diagram is one of the UML 2.x *interaction diagrams*; the interaction family also holds the communication, timing and interaction-overview diagrams. The C4 dynamic diagram can be drawn in a collaboration style (free layout, numbered links) or a sequence style.
- **Leaves out:** the full static structure (only this scenario's participants appear), every alternative path, internal algorithms (E2), object lifecycles (E3), data structure (D1) and organisational responsibility (E4, A5).
- **Definition used here:** "sequence diagram" means the UML 2.5.1 notation, used as a selective sketch in the sense of "UML as sketch": lifelines, messages and frames are kept, but not every rule is enforced. "Interaction diagram" is the family name, not a synonym.
- **Telecom ancestor:** ITU-T Z.120 *Message Sequence Chart* (MSC), in force as Z.120 (02/11).

## When to use and how to choose
- **Audience:** developers, testers, architects, integration partners, security reviewers; a simplified version with fewer lifelines suits business readers.
- **Scenarios:** agreeing an API integration (storefront, gateway, order service, payment provider); authentication or authorisation flows with redirects and tokens; how a chatbot answers one question (UI, orchestrator, model, product search, with a retrieval loop); incident reconstruction; asynchronous processing with a later callback.
- **When not to use:** all behaviours on one sheet; human workflows with many decisions (A5, E4); one object's lifecycle (E3); more than about 8–10 lifelines or 25 messages (split with `ref` or raise the level).
- **vs neighbours:**
  - **E4 Swimlane** or **A5 BPMN** for hand-offs between people or organisations.
  - **E2 Activity** for one participant's decision logic.
  - A communication diagram when spatial relationships matter more than time order.
  - **F1** for OAuth/OIDC-style flows (a specialised sequence diagram).
  - **C3/C4** when the question is structure, not behaviour.
  - Choose **C6** when the question is the list of interfaces with protocol, authentication and failure semantics, not the order of one scenario.
  - Choose **I1** when several scenarios must tie the logical, process, development and physical views together; a sequence diagram is one such scenario.

## Notation and elements
- **Formal or informal:** formal in UML 2.5.1. Most architecture sequence diagrams are sketches that keep lifelines, messages and frames.
- **Required:**
  - **Lifelines:** a box with a dashed vertical line per participant. Use real, nameable roles or systems at one consistent level (all systems, or all containers). An actor may be a stick figure.
  - **Messages:** horizontal arrows ordered top to bottom, optionally numbered.
- **Arrow semantics:**
  - **Synchronous call:** solid line, filled head; the caller waits.
  - **Asynchronous message:** solid line, open head; the caller does not wait.
  - **Reply:** dashed line back to the caller; optional when obvious. Its head style varies by UML version and tool, so "dashed" is the safe rule.
  - **Create / destroy:** a creation message to a new lifeline's head; an X marks destruction.
- **Optional:**
  - **Activation bars:** thin rectangles while a participant processes a call; they end when the reply returns.
  - **Combined fragments**: `alt` (guarded alternatives), `opt`, `loop`, `par`, `break`, `critical`, `ref` (points to another interaction); rarer: `neg`, `assert`, `strict`, `seq`, `ignore`, `consider`. Guards sit in square brackets; `[else]` negates the others.
  - Notes, time constraints, gates, and a frame `sd <name>` around the whole diagram.
- **Level of detail:** state whether lifelines are systems, containers or components, and whether messages are business actions or API calls. Endpoint names are optional.
- **Naming:** messages are verb plus object ("submit order", "GET /orders/{id}"); replies are nouns ("order confirmation"); lifelines reuse names from C2/C3.

## Best practices and anti-patterns
### Best practices
1. **One scenario per diagram, named in the title,** with its variant: "Place order: card payment, happy path".
2. **Start at the trigger the audience cares about;** omit setup they take for granted (login) unless it is the point.
3. **Prerequisites first in time order** (obtain the token, then call the API). Note reuse ("token cached until expiry") instead of repeating steps.
4. **Keep lifelines at one abstraction level,** ordered left to right by first action, so arrows rarely cross.
5. **Show asynchrony honestly:** async arrows plus a later callback, not a fake synchronous reply. Wrap the whole repeating round trip in `loop`; put error and timeout handling in a separate diagram when it would crowd the happy path.

### Anti-patterns
1. **The whole system in one sequence:** too many lifelines or messages.
2. **Mixed abstraction levels:** a browser, a database table and a partner company side by side.
3. **Calls and returns confused:** solid return arrows, activation bars that never close.
4. **Fictional participants** that are not real systems or roles.
5. **Time order that contradicts real dependencies** (using a token before obtaining it), or message names that no longer match the code.

## Drawing recipe
1. Fix the scenario, trigger, end point and abstraction level (systems, containers or components). Decide: happy path only, or plus one key alternative.
2. List participants in the order they first act; cap at about 6–8. Collapse non-focus subsystems into one lifeline.
3. Write the message list as numbered text first (sender, receiver, sync / async / reply) and validate it against code or docs. Show it to the user before drawing.
4. Layout: time flows top to bottom; the initiator is leftmost. Group lifelines by owning system with a light background band ("inside the shop" vs "external").
5. Frames: `loop` around repeating round trips, `alt [condition]` for branches, `opt` for optional steps, `ref` to point at a separate diagram.
6. Text: messages at most 6 words; endpoints, payloads or technology only if the audience needs them, as a small mono-font suffix.
7. Colour: neutral lifelines; at most one accent for messages that cross a system boundary or are asynchronous, explained in the key.
8. Add a key (sync, async, reply, frames) if readers are not UML-literate, and a one-line caption with the scenario and its assumptions.

**Self-check**
- [ ] The title is scenario plus variant (happy path or error path).
- [ ] Every lifeline is a real, nameable participant at one abstraction level.
- [ ] Prerequisites come before dependants; reuse is noted, not repeated.
- [ ] Sync calls have filled heads, async open heads, replies are dashed; activations end at the reply.
- [ ] Frames enclose whole round trips; guards are in brackets.
- [ ] At most about 8 lifelines and about 25 messages, or the diagram is split with `ref`.
- [ ] Boundary-crossing messages are identifiable.
- [ ] Message names match the interfaces in code or docs, or are deliberately generalised.

## Evidence in a code repository
- **Trace the path:** route handler, service calls, outbound clients (HTTP or SDK), queue `send`, consumer handler, store writes, response or stream. Record file and line for every hop.
- **Sync vs async:** look for retries, timeouts, and streaming responses (SSE, websocket) to choose arrow style and loops.
- **Also useful:** OpenAPI specs, tracing spans, integration tests that exercise the whole scenario.
- **Must come from people:** which scenario matters to the audience, and business names for technical steps.
- Mark traced hops as "from code" and unverified hops as "inferred".

## Guided-mode questions
1. Which single scenario should this show, and where does it start and end? (the most-discussed user journey, e.g. place an order)
2. Who is reading: business (systems and plain actions) or engineers (containers or components with endpoints)? (engineers, container level)
3. Happy path only, or also one important alternative or error path? (happy path, errors in a separate diagram)
4. Should setup steps (login, token acquisition) appear? (no, start after them)
5. Show interface and endpoint names, or generalise? (generalise unless engineers will check them against code)

## Template
Model template: `assets/templates/E1.json` · Layout template: `sequence` · lifelines are `lifeline` nodes ordered left to right; messages are `edges` with `step` numbers and kind `call`, `async` or `message` (a reply is the same edge reversed with `dashed: true`); `frames` mark `alt` / `loop` / `opt` / `par` regions as a `label` over a step range (`from_step`, `to_step`) and `activations` the execution bars.

## Sample
Figure: `samples/E1-sequence-diagram.svg` (published with the site)
