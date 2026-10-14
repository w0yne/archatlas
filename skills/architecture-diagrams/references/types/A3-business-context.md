# Business Context Diagram (业务上下文图)
<!-- Generated from content/en/types/A3-business-context.md by tools/build_skill_refs.py. Do not edit. -->
> What is inside our system or initiative, and who or what outside it exchanges what with us?
Scope: One system, initiative or business unit drawn as a black box, with every external party it exchanges information, goods, money or obligations with. Neighbours: B4, C2, H3.

## Meaning
- **Question:** what is inside the system or initiative, and who or what outside it exchanges what with it (information, goods, money, decisions, obligations)?
- **Concern:** it fixes the **boundary** and the **business interfaces**. In ISO/IEC/IEEE 42010 terms it frames purpose, scope and external dependencies. In arc42 it is the *business context* of §3. The C4 model's System Context diagram is the same idea once the subject is a software system. TOGAF has no artefact called "context diagram"; its Phase A Value Chain and Solution Concept diagrams are the nearest.
- **Left out on purpose:** anything inside the box (A7, C3), protocols and channels (the arc42 *technical* context; C2/C6), process steps (A5), and stakeholder power or interest (H3).
- **Definition used here:** a business context diagram lists only parties that *exchange something with* the subject. Parties that only have power or interest (sponsor, budget holder, auditor with no exchange) belong in the Stakeholder Map (H3), which is a separate figure.

## When to use and how to choose
- **Audience:** executives, business owners, analysts, architects, and anyone new to the initiative.
- **Scenarios:** project kick-off ("the online shop and the parties it trades with"); business-case review (who pays whom, who supplies what); onboarding new team members; agreeing which partners a target state adds or drops (as-is vs to-be pair).
- **When not to use:** to explain internal structure (A7, C5); to specify integrations (C6); to rank stakeholders (H3).
- **vs neighbours:**
  - Choose **C2 System Context** once the subject is a software system and the readers are technical.
  - Choose **B4 Scope diagram** when the point is what is in or out of scope for a project phase.
  - Choose **H3 Stakeholder Map** when the question is who must be engaged and how; it has axes, not flows.
  - Choose **A2 Value Stream** when you need the stages of delivering value, not just the boundary.
  - Choose **A7 Conceptual Architecture** when you need to open the box into major blocks.

## Notation and elements
- **Required:** one central subject drawn as a black box; external parties (roles, organisations, external systems) at the edge; one connector per exchange, labelled with a business noun ("order", "payment", "stock level"); a title stating scope and as-is / to-be.
- **Context-level DFD rules (Yourdon–DeMarco, Gane–Sarson):** the subject is a single process and externals are terminators; every flow has the process at one end, so externals never connect to each other.
- **arc42 rule:** the business context may be a diagram **or** a table *partner | input | output*; channels and formats go in the technical context.
- **C4 model rule:** people and software systems only; no technologies or protocols.
- **Arrow semantics:** the direction of the business exchange, not of the call or of control. A two-way exchange gets two labelled arrows, or one arrow carrying both labels.
- **Optional:** grouping of externals (customers / partners / authorities / internal-but-out-of-scope); flow kinds (information, money, goods) by line style, explained in a legend; numbered flows keyed to an exchange table.
- **Level of detail:** about 5–15 external parties; labels of 1–3 words; no protocol or file-format names.
- **Formal alternative:** ArchiMate business layer: Business Actor / Role / Collaboration around the subject, Flow or Serving relationships, Business Objects for the exchanged items.
- **Naming terms:** "Level 0 DFD" is ambiguous. Some authors use it for the context diagram, others for the first decomposition below it. Say "context-level DFD" to avoid confusion.

## Best practices and anti-patterns
### Best practices

1. Keep the centre a **black box**. Anything drawn inside belongs to another type.
2. Label every flow with the **thing exchanged**, never "uses" or "integrates". All readers should see what data, goods or money cross the boundary.
3. Keep the **business context separate from the technical context**. Channels and protocols go in a second view or table.
4. Hunt for non-obvious parties: regulators, tax authority, payment and identity providers, operations and support. Use checklists such as the 42010 stakeholder classes (users, operators, acquirers, owners, suppliers, maintainers) and the five TOGAF stakeholder groups.
5. State **as-is or to-be** in the title, and draw a pair when the target state changes the partner set.

### Anti-patterns

1. **One diagram, two questions:** a hub-and-spoke context with power/interest colouring sprayed on top. Split it into A3 and H3.
2. Internal subsystems drawn as external parties, or as boxes inside the centre. Every element is either the subject or explicitly external.
3. External parties connected to each other. Context-level DFDs forbid it; if those hand-offs matter, draw A2 or E4.
4. Only end users shown; regulators, finance, logistics and support forgotten.
5. Mixed kinds among the externals: a role next to a department next to a product next to a process step.

## Drawing recipe
1. Confirm the subject (one system, initiative or business unit) and as-is vs to-be. Write the title as a message ("The online shop and the seven parties it trades with").
2. List external parties, merge duplicates, keep one kind per group (roles, organisations, external systems), 5–15 in total.
3. List exchanges as *party → subject: noun* and *subject → party: noun*. Drop anything that is a protocol.
4. Layout: subject centred and visually dominant; customers and channels left, partners and providers right, authorities top, internal-but-out-of-scope bottom; short straight arrows, no crossings.
5. Text budget: party names ≤ 3 words, flow labels ≤ 3 words, no sentences on the canvas.
6. Colour: one neutral fill for the subject, at most 3 fills for party groups; line style (not colour) for flow kinds, always with a legend.
7. Optional: number the flows and add a *partner | input | output* table in the notes.

**Self-check**

- [ ] The centre is a black box; nothing is drawn inside it.
- [ ] Every external party in a group is the same kind of thing.
- [ ] Every arrow has a business-noun label and a clear direction; no protocol names.
- [ ] Regulators, finance, logistics and support were considered (included or deliberately left out).
- [ ] No external-to-external flows.
- [ ] Title states scope and as-is / to-be; no subtitle restating the type.
- [ ] Stakeholder power or interest is not encoded here (that is H3).
- [ ] A legend explains every line style and fill.

## Evidence in a code repository
- **From code:** README integration sections; outbound client modules and SDK dependencies (payment, e-mail, shipping, identity); webhook handlers; API gateway or route definitions that reveal external consumers; environment-variable names for partner endpoints; OpenAPI/AsyncAPI contract folders; ADRs that name external parties.
- **Limit:** code reveals the *technical* partners, not the business exchange. Money, goods, legal obligations and parties with no IT link (tax authority, a courier booked by phone) must come from people. Mark code-derived parties "observed in code" and anything proposed by the drawer "proposed".

## Guided-mode questions
1. Do you need who exchanges what with the subject (this diagram), who must be engaged and how (H3), or both as two figures? (Context first, stakeholder grid separately.)
2. What is the subject in the centre: one system, a project or a business unit; current or target state? (The system the readers will discuss, as-is.)
3. Here are candidate parties grouped as customers / partners / authorities / internal-out-of-scope; anything missing, such as a regulator? (Include payment, logistics and tax parties.)
4. Should flows show only information, or also money and goods? (All three, by line style.)

## Template
Model template: `assets/templates/A3.json` · Layout template: `nested` · the subject is one `system` node with style `primary`, externals are `external` or `actor` nodes around it, and each exchange is a labelled edge whose `kind` is `data`, `call` or `message` (the flow type goes in the label).

## Sample
Figure: `samples/A3-business-context.svg` (published with the site)
