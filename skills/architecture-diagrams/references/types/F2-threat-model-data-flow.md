# Threat-Model Data-Flow Diagram (威胁建模数据流图)
<!-- Generated from content/en/types/F2-threat-model-data-flow.md by tools/build_skill_refs.py. Do not edit. -->
> What data crosses which changes of authority or trust assumptions, and where could security properties fail?
Scope: One feature or subsystem, with its assets, entry points and trust boundaries; linked to a separate threat register Neighbours: D2, F1, F3, G3, C3.

## Meaning
- **Question:** what data crosses which changes of authority or trust assumptions, and where could security properties fail? A boundary can separate organisations, privilege levels, tenants, processes, or browser and server authority on the same network. A private subnet does not prove that everything inside it is trusted.
- **Not the whole threat model:** the diagram is the system-model step. A threat model also contains threat identification, responses (mitigations) and validation. Keep those in a linked register.
- **Definition used here:** *STRIDE* (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) is a threat-identification method that works on a DFD; it is neither a synonym for the diagram nor required by it. A *trust-boundary diagram* is a simpler related view without full flows.
- **Leaves out:** incidental calls that do not touch the modelled assets or properties. Do not drop an internal flow just because it crosses no drawn boundary; it may carry sensitive data or a privileged operation.
- **Standing:** established DFD symbols with security annotation; no ISO or OMG standard for the graphic.

## When to use and how to choose
- **Audience:** security engineers, architects, developers, privacy specialists, service owners.
- **Scenarios:** a new public API for third-party resellers; a payment-provider webhook or external identity provider; a multi-tenant upload and processing flow; a change of hosting or privilege boundary (for example moving the chatbot's order lookup into its own service).
- **When not to use:** as a network inventory, a penetration-test result, or proof that all STRIDE threats are eliminated.
- **vs neighbours:**
  - **D2 Data-Flow** for ordinary processing without trust analysis.
  - **F1** for one identity exchange step by step.
  - **F3** for permission rules.
  - **G3** for routing and connectivity.
  - **C3** for the structure this DFD is usually derived from.

## Notation and elements
- **Formal or informal:** informal but widely taught. Use one recognisable DFD symbol set or a declared custom legend-.
- **Required:**
  - Scope statement and the assets that matter.
  - External entities (shopper, payment provider), processes (checkout service), data stores (orders database).
  - Directed, named data flows ("card token", "order record").
  - Trust boundaries, each with a one-line meaning.
  - Element and flow IDs that link to threats and open questions.
- **Arrow meaning:** movement of named data, not time order, dependency, role inheritance or mitigation. Split a flow into two arrows when direction, payload or privilege differs. Numbers give traceability, not necessarily sequence.
- **Boundaries:** nested boundaries must represent real nested authority. Place every store clearly inside or outside each boundary.
- **Optional:** data classification, protocol, authentication context, privilege level, threat IDs, mitigation state.
- **Linked register:** element or flow ID, threat, impact, response, owner, validation evidence. Generated threats are hypotheses to review, not verified findings.
- **Text budget:** 1–4 words per label; threat text lives in the register, not on arrows.

## Best practices and anti-patterns
### Best practices
1. **Run the whole loop:** model the system, identify what can go wrong, decide responses, validate them. The DFD finishes only the first step.
2. **Decompose where a security distinction needs it.** Prefer a context view plus focused subsystem DFDs over one giant infrastructure picture.
3. **Draw boundaries for trust assumptions.** Not every region, namespace or subnet merits one.
4. **Use STRIDE as prompts per element,** not six decorative badges on every shape; relevant threats depend on the element type and scenario.
5. **Separate observed controls, proposed controls and unverified assumptions.** Show unknowns openly rather than hiding them behind a "secure zone" label.

### Anti-patterns
1. **A boundary drawn around the whole system** or around each cloud component, which explains nothing.
2. **Unlabelled arrows** (no data name) or arrows used for sequence or dependency.
3. **Omitting internal flows mechanically** because they cross no boundary.
4. **Threat text crammed onto the diagram** so that it becomes unreadable and unowned.
5. **Presenting the picture as a completed assessment,** or showing proposed controls as if they were in place.

## Drawing recipe
1. State assets, scope and the adversary assumptions in scope; put scope and status in the title ("Shop checkout: data flows and trust boundaries, proposed").
2. Inventory entry and exit points, processes, stores and authority changes before drawing.
3. Draw the smallest model that keeps those distinctions; name every payload on its arrow.
4. Layout: external entities on the outer edges, processes in the middle, stores at the bottom; flow direction left to right. Boundaries are dashed containers with a short label of the trust change.
5. Inspect every boundary crossing and each important internal flow; keep or justify each one.
6. Assign stable IDs (E1, P1, S1, F1 style) and emit a threat/mitigation register as a separate table.
7. Colour: neutral fills; one accent for boundaries; a second marker only for "proposed / unverified". Keep symbols from one DFD set, with a legend.
8. Review with a system expert; label gaps instead of guessing.

**Self-check**
- [ ] Scope, assets and assumptions are stated.
- [ ] Relevant entry and exit points and stores are shown.
- [ ] Every data-flow arrow names the data and has one direction.
- [ ] Each boundary states the authority or trust change it marks.
- [ ] Important internal flows were not omitted mechanically.
- [ ] Threat IDs resolve to owner, response and validation records.
- [ ] Proposed controls and unknowns are visibly different from observed ones.
- [ ] The figure is not presented as a completed assessment.

## Evidence in a code repository
- **Inputs:** routes and middleware, upload and deserialisation points, outbound calls and webhooks, queue producers and consumers, storage access, process privileges, service-account and permission references, network policies, tenant filters.
- **Tests and configuration show intended controls, not deployed effectiveness.**
- **Not default inputs:** logs and runtime state, which may contain secrets.
- **Must come from people:** organisational trust assumptions, who controls each component, adversary scope, and which controls are only proposed.

## Guided-mode questions
1. Which assets and security properties matter most? (customer payment data and order integrity)
2. Who controls each component, and where do privileges or tenants change? (list owners; mark tenant boundaries)
3. Which external actors and abuse assumptions are in scope? (shoppers, resellers, the payment provider)
4. Is STRIDE required, or should this feed another method? (use STRIDE per element)
5. Existing system or proposed design with incomplete controls? (proposed, with controls marked)

## Template
Model template: `assets/templates/F2.json` · Layout template: `nested` · trust boundaries become `boundary` groups (nestable), external entities are `external` nodes, processes `component` nodes and stores `store` nodes, named data flows are `data` edges with a one-way `dir`; element and flow IDs go in `tags` for linking to the threat register.

## Sample
Figure: `samples/F2-threat-model-data-flow.svg` (published with the site)
