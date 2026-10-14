---
code: E1
slug: sequence-diagram
family: E
names:
  en: Sequence diagram
  zh: 时序图
  aliases:
    en: [UML sequence diagram, runtime view, C4 dynamic diagram, message sequence chart, MSC, C4 dynamic diagram (sequence style), runtime-view scenario, call-flow diagram, ladder diagram]
    zh: [序列图, 运行时视图, 交互时序图, 顺序图, 调用链时序图]
question: For one scenario, which participants exchange which messages in what order, and where does the flow branch, loop or wait?
audiences: [developers, architects]
levels: [logical]
phases: [design, build]
scope: One scenario (one trigger to one outcome), about 4–8 lifelines at one abstraction level, up to about 25 messages
formal: {kind: standard, ref: 'OMG UML 2.5.1 (formal/2017-12-05), interaction diagrams; ITU-T Z.120 Message Sequence Chart for the telecom ancestor'}
neighbours: [A5, C3, C4, C6, E2, E3, E4, F1, I1]
status: draft
---

# Sequence Diagram (时序图)

> One scenario drawn as participants across the top and messages down the page in time order, showing who calls whom and where the flow branches, repeats or waits.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** in this one scenario, which participants exchange which messages, in what order, and where does the flow branch, loop or wait?
- **Viewpoint:** the runtime view of a single scenario. It turns a static structure (C2, C3) into a story over time. arc42 section 6 "Runtime View" asks for exactly this, for the important scenarios only [6]. The C4 model says dynamic diagrams "should be used sparingly" for interesting or recurring patterns with complicated interactions [4].
- **Deeper meaning:** a sequence diagram is one of the UML 2.x *interaction diagrams*; the interaction family also holds the communication, timing and interaction-overview diagrams [3]. The C4 dynamic diagram can be drawn in a collaboration style (free layout, numbered links) or a sequence style [4].
- **Leaves out:** the full static structure (only this scenario's participants appear), every alternative path, internal algorithms (E2), object lifecycles (E3), data structure (D1) and organisational responsibility (E4, A5).
- **Definition used here:** "sequence diagram" means the UML 2.5.1 notation [1][2], used as a selective sketch in the sense of "UML as sketch" [5]: lifelines, messages and frames are kept, but not every rule is enforced. "Interaction diagram" is the family name, not a synonym.
- **Telecom ancestor:** ITU-T Z.120 *Message Sequence Chart* (MSC), in force as Z.120 (02/11) [16].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
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
-->
- **Audience:** developers, testers, architects, integration partners and security reviewers. Business readers can follow a simplified version with fewer lifelines and plain-language messages.
- **Classic scenarios:**
  1. Agreeing an API integration: storefront, gateway, order service, external payment provider.
  2. Explaining an authentication or authorisation flow with redirects, tokens and callbacks [7][8].
  3. "How is one question answered?" in a support chatbot: UI, orchestrator, language model, product-search service, model again, UI, with a retrieval loop.
  4. Incident review: reconstructing the order of events across services.
  5. Asynchronous processing: order accepted, work queued, webhook or callback later.
- **When not to use:** all behaviours of a system on one sheet; human workflows with many decisions (A5, E4); the lifecycle of one object (E3); more than about 8–10 lifelines or about 25 messages, where you split with `ref` or raise the abstraction level.
- **vs neighbours:**
  - Choose **E4 Swimlane** or **A5 BPMN** when the point is hand-offs between people or organisations.
  - Choose **E2 Activity** for one participant's internal decision logic.
  - Choose a **communication or C4 collaboration-style** diagram when spatial relationships matter more than strict time order [4].
  - Choose **F1 Authentication and authorisation flow** for OAuth/OIDC-style flows; it is a specialised sequence diagram [7][8].
  - Choose **C3/C4** when the question is structure, not behaviour.
  - Choose **C6** when the question is the list of interfaces with protocol, authentication and failure semantics, not the order of one scenario.
  - Choose **I1** when several scenarios must tie the logical, process, development and physical views together; a sequence diagram is one such scenario.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** formal in UML 2.5.1 [1]. Most architecture sequence diagrams are sketches that keep lifelines, messages and frames [5].
- **Required:**
  - **Lifelines:** a box with a dashed vertical line per participant. Use real, nameable roles or systems at one consistent level (all systems, or all containers). An actor may be a stick figure.
  - **Messages:** horizontal arrows ordered top to bottom, optionally numbered.
- **Arrow semantics:**
  - **Synchronous call:** solid line, filled head; the caller waits [9].
  - **Asynchronous message:** solid line, open head; the caller does not wait [9].
  - **Reply:** dashed line back to the caller; optional when obvious. Its head style varies by UML version and tool, so "dashed" is the safe rule [9].
  - **Create / destroy:** a creation message to a new lifeline's head; an X marks destruction.
- **Optional:**
  - **Activation bars:** thin rectangles while a participant processes a call; they end when the reply returns.
  - **Combined fragments** [10]: `alt` (guarded alternatives), `opt`, `loop`, `par`, `break`, `critical`, `ref` (points to another interaction); rarer: `neg`, `assert`, `strict`, `seq`, `ignore`, `consider`. Guards sit in square brackets; `[else]` negates the others.
  - Notes, time constraints, gates, and a frame `sd <name>` around the whole diagram.
- **Level of detail:** state whether lifelines are systems, containers or components, and whether messages are business actions or API calls. Endpoint names are optional.
- **Naming:** messages are verb plus object ("submit order", "GET /orders/{id}"); replies are nouns ("order confirmation"); lifelines reuse names from C2/C3.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
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

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Microsoft identity platform: OAuth 2.0 authorization code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow) — a numbered sequence across user agent, app, identity platform and API that keeps protocol detail readable. Vendor documentation.
- [IETF RFC 6749 section 4.1](https://datatracker.ietf.org/doc/html/rfc6749) — the canonical lettered ASCII flow (A) to (F); precise, minimal step labels. Public standard.
- [C4 model: Dynamic diagram](https://c4model.com/diagrams/dynamic) — the same scenario in collaboration and sequence styles, with guidance on scope.
- [uml-diagrams.org: combined fragments](https://www.uml-diagrams.org/sequence-diagrams-combined-fragment.html) — worked examples for `alt`, `opt`, `loop`, `par`, `break`.
- [Mermaid sequence diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html) and [PlantUML sequence diagrams](https://plantuml.com/sequence-diagram) — diagrams-as-code references with activations, frames, autonumbering and notes. Open-source tools.
- [RFC 9293 (TCP), three-way handshake figure](https://datatracker.ietf.org/doc/html/rfc9293) — a tiny exchange; two lifelines can be enough.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Fix the scenario, trigger, end point and abstraction level (systems, containers or components). Decide: happy path only, or plus one key alternative.
2. List participants in the order they first act; cap at about 6–8. Collapse non-focus subsystems into one lifeline.
3. Write the message list as numbered text first (sender, receiver, sync / async / reply) and validate it against code or docs. Show it to the user before drawing.
4. Layout: time flows top to bottom; the initiator is leftmost. Group lifelines by owning system with a light background band ("inside the shop" vs "external").
5. Frames: `loop` around repeating round trips, `alt [condition]` for branches, `opt` for optional steps, `ref` to point at a separate diagram. A single retry after a timeout: `alt [reply received] … [else: timeout] retry once` when both outcomes matter; `loop [until confirmed, max 2]` around the whole round trip for a bounded retry; `opt [timeout]` only when the figure shows the retry branch alone, guard written. Mark a message async (open arrowhead, kind `async`) only when the sender does not wait (event, notification, queue publish, webhook, callback); never invent one.
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

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Trace the path:** route handler, service calls, outbound clients (HTTP or SDK), queue `send`, consumer handler, store writes, response or stream. Record file and line for every hop.
- **Sync vs async:** look for retries, timeouts, and streaming responses (SSE, websocket) to choose arrow style and loops.
- **Also useful:** OpenAPI specs, tracing spans, integration tests that exercise the whole scenario.
- **Must come from people:** which scenario matters to the audience, and business names for technical steps.
- Mark traced hops as "from code" and unverified hops as "inferred".

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which single scenario should this show, and where does it start and end? (the most-discussed user journey, e.g. place an order)
2. Who is reading: business (systems and plain actions) or engineers (containers or components with endpoints)? (engineers, container level)
3. Happy path only, or also one important alternative or error path? (happy path, errors in a separate diagram)
4. Should setup steps (login, token acquisition) appear? (no, start after them)
5. Show interface and endpoint names, or generalise? (generalise unless engineers will check them against code)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/E1.json` · Layout template: `sequence` · lifelines are `lifeline` nodes ordered left to right; messages are `edges` with `step` numbers and kind `call`, `async` or `message` (a reply is the same edge reversed with `dashed: true`); `frames` mark `loop` / `alt` / `opt` / `par` regions by `operator` over a step range (`from_step`, `to_step`) with a `guard`; an `alt` or `par` frame lists `operands`, each with its own guard and step range, drawn as regions split by a dashed separator; `activations` are the execution bars.

## Sources {#sources}
<!-- skill: omit -->
1. OMG, UML 2.5.1 specification page (formal/17-12-05, December 2017) — https://www.omg.org/spec/UML/2.5.1/About-UML — accessed 2026-10-14
2. Wikipedia, "Sequence diagram" (cites UML 2.5.1 formal/2017-12-05) — https://en.wikipedia.org/wiki/Sequence_diagram — accessed 2026-10-14
3. Lucidchart, "Interaction Diagram Tutorial" (sequence vs communication; interaction family) — https://www.lucidchart.com/pages/uml-interaction-diagram — accessed 2026-10-14
4. C4 model, "Dynamic diagram" — https://c4model.com/diagrams/dynamic — accessed 2026-10-14
5. M. Fowler, "UmlAsSketch" — https://martinfowler.com/bliki/UmlAsSketch.html — accessed 2026-10-14
6. arc42, "6 – Runtime view" — https://docs.arc42.org/section-6/ — accessed 2026-10-14
7. Microsoft Learn, "Microsoft identity platform and OAuth 2.0 authorization code flow" — https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow — accessed 2026-10-14
8. IETF, RFC 6749 "The OAuth 2.0 Authorization Framework" — https://datatracker.ietf.org/doc/html/rfc6749 — accessed 2026-10-14
9. Sparx Systems, "Sequence Diagram — UML 2 Tutorial" — https://sparxsystems.com/resources/tutorials/uml2/sequence-diagram.html — accessed 2026-10-14
10. uml-diagrams.org, "Sequence diagram combined fragment" — https://www.uml-diagrams.org/sequence-diagrams-combined-fragment.html — accessed 2026-10-14
11. Mermaid, "Sequence diagrams" — https://mermaid.js.org/syntax/sequenceDiagram.html — accessed 2026-10-14
12. PlantUML, "Sequence Diagram" — https://plantuml.com/sequence-diagram — accessed 2026-10-14
13. SequenceDiagram.org — https://sequencediagram.org/ — accessed 2026-10-14
14. Thoughtworks Technology Radar, "Diagrams as code" — https://www.thoughtworks.com/en-us/radar/techniques/diagrams-as-code — accessed 2026-10-14
15. IETF, RFC 9293 "Transmission Control Protocol" — https://datatracker.ietf.org/doc/html/rfc9293 — accessed 2026-10-14
16. ITU-T, Recommendation Z.120 "Message Sequence Chart (MSC)", status page (Z.120 (02/11) in force) — https://www.itu.int/rec/t-rec-z.120 — accessed 2026-10-14

Note: the UML 2.5.1 clause text was not read first-hand; element semantics come from sources 9 and 10 and are not verified against the primary text.

## Sample {#sample}
<!-- skill: path only -->
![E1 sample: sequence of placing an order with a loop and an alt frame](/samples/E1-sequence-diagram.svg)
*Sequence of placing an order: the customer places an order with the order API, which reserves each item with the inventory service (loop) and then charges the card at the payment provider. The alt frame has two operands split by a dashed line, each with its own guard: under [card accepted] the payment is confirmed and the order is confirmed; under [else: card declined] the payment is declined and the order is rejected. Only one operand runs for a given order.*
