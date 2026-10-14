---
code: F2
slug: threat-model-data-flow
family: F
names:
  en: Threat-Model Data-Flow Diagram
  zh: 威胁建模数据流图
  aliases:
    en: [security data-flow diagram, DFD with trust boundaries, STRIDE diagram, trust-boundary diagram]
    zh: [安全数据流图, 含信任边界的数据流图, 信任边界图]
question: "What data crosses which changes of authority or trust assumptions, and where could security properties fail?"
audiences: [security engineers, solution architects, developers, privacy specialists, service owners]
level: logical
phases: [design, review]
scope: "One feature or subsystem, with its assets, entry points and trust boundaries; linked to a separate threat register"
formal:
  kind: convention
  ref: "Classic data-flow-diagram symbols plus security annotations; practice from the OWASP Threat Modeling Cheat Sheet and Microsoft's documented STRIDE approach. Not a universal graphical standard"
neighbours: [D2, F1, F3, G3, C3]
status: draft
---

# Threat-Model Data-Flow Diagram (威胁建模数据流图)

> A data-flow diagram that marks where trust assumptions change, so that a team can ask what could go wrong at each flow, store and boundary.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** what data crosses which changes of authority or trust assumptions, and where could security properties fail? A boundary can separate organisations, privilege levels, tenants, processes, or browser and server authority on the same network. A private subnet does not prove that everything inside it is trusted [1][4].
- **Not the whole threat model:** the diagram is the system-model step. A threat model also contains threat identification, responses (mitigations) and validation [1][2]. Keep those in a linked register.
- **Definition used here:** *STRIDE* (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) is a threat-identification method that works on a DFD; it is neither a synonym for the diagram nor required by it. A *trust-boundary diagram* is a simpler related view without full flows [2][3].
- **Leaves out:** incidental calls that do not touch the modelled assets or properties. Do not drop an internal flow just because it crosses no drawn boundary; it may carry sensitive data or a privileged operation [1].
- **Standing:** established DFD symbols with security annotation; no ISO or OMG standard for the graphic.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** security engineers, architects, developers, privacy specialists, service owners.
- **Classic scenarios:**
  1. A new public API in the shop for third-party resellers.
  2. Adding a payment-provider webhook or an external identity provider.
  3. A multi-tenant upload and processing flow, such as merchant product-image imports.
  4. A change of hosting or privilege boundary, such as moving the support chatbot's order lookup to a separate service.
- **When not to use:** as a network inventory, as a penetration-test result, or as proof that all STRIDE threats are eliminated.
- **vs neighbours:**
  - Choose **D2 Data-Flow Diagram** for ordinary data processing without a trust analysis.
  - Choose **F1 Authentication Flow** for one identity exchange step by step.
  - Choose **F3 Access-Control Model** for the permission rules.
  - Choose **G3 Network Topology** for routing and connectivity.
  - Choose **C3 Container Diagram** for the structural view this DFD is usually derived from.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** informal but widely taught. Use one recognisable DFD symbol set or a declared custom legend [1]-[3].
- **Required:**
  - Scope statement and the assets that matter.
  - External entities (shopper, payment provider), processes (checkout service), data stores (orders database).
  - Directed, named data flows ("card token", "order record").
  - Trust boundaries, each with a one-line meaning.
  - Element and flow IDs that link to threats and open questions.
- **Arrow meaning:** movement of named data, not time order, dependency, role inheritance or mitigation. Split a flow into two arrows when direction, payload or privilege differs. Numbers give traceability, not necessarily sequence.
- **Boundaries:** nested boundaries must represent real nested authority. Place every store clearly inside or outside each boundary.
- **Optional:** data classification, protocol, authentication context, privilege level, threat IDs, mitigation state.
- **Linked register:** element or flow ID, threat, impact, response, owner, validation evidence. Generated threats are hypotheses to review, not verified findings [2].
- **Text budget:** 1–4 words per label; threat text lives in the register, not on arrows.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Run the whole loop:** model the system, identify what can go wrong, decide responses, validate them. The DFD finishes only the first step [1][2].
2. **Decompose where a security distinction needs it.** Prefer a context view plus focused subsystem DFDs over one giant infrastructure picture [1].
3. **Draw boundaries for trust assumptions.** Not every region, namespace or subnet merits one.
4. **Use STRIDE as prompts per element,** not six decorative badges on every shape; relevant threats depend on the element type and scenario [3].
5. **Separate observed controls, proposed controls and unverified assumptions.** Show unknowns openly rather than hiding them behind a "secure zone" label.

### Anti-patterns
1. **A boundary drawn around the whole system** or around each cloud component, which explains nothing.
2. **Unlabelled arrows** (no data name) or arrows used for sequence or dependency.
3. **Omitting internal flows mechanically** because they cross no boundary.
4. **Threat text crammed onto the diagram** so that it becomes unreadable and unowned.
5. **Presenting the picture as a completed assessment,** or showing proposed controls as if they were in place.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Microsoft Threat Modeling Tool: getting started](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started) — a small DFD with authority boundaries, then analysis and mitigations.
- [Microsoft: Uncover Security Design Flaws Using the STRIDE Approach](https://learn.microsoft.com/en-us/archive/msdn-magazine/2006/november/uncover-security-design-flaws-using-the-stride-approach) — worked figures for decomposition and per-element reasoning; a historical method article, not a current tool recipe.
- [OWASP Threat Dragon: getting started](https://www.threatdragon.com/docs/usage/getting-started.html) — editable sample models connecting diagram, element details and threat records. The older docs path has moved; use this one.
- Link only; no artwork copied. Check the licence of a specific sample model before adapting it; the tool's licence does not settle sample rights.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
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

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Inputs:** routes and middleware, upload and deserialisation points, outbound calls and webhooks, queue producers and consumers, storage access, process privileges, service-account and permission references, network policies, tenant filters.
- **Tests and configuration show intended controls, not deployed effectiveness.**
- **Not default inputs:** logs and runtime state, which may contain secrets.
- **Must come from people:** organisational trust assumptions, who controls each component, adversary scope, and which controls are only proposed.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which assets and security properties matter most? (customer payment data and order integrity)
2. Who controls each component, and where do privileges or tenants change? (list owners; mark tenant boundaries)
3. Which external actors and abuse assumptions are in scope? (shoppers, resellers, the payment provider)
4. Is STRIDE required, or should this feed another method? (use STRIDE per element)
5. Existing system or proposed design with incomplete controls? (proposed, with controls marked)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/F2.json` · Layout template: `nested` · trust boundaries become `boundary` groups (nestable), external entities, processes and stores are nodes with distinct `kind`, named data flows are `data` edges with a one-way `dir`; element and flow IDs go in `tags` for linking to the threat register.

## Sources {#sources}
<!-- skill: omit -->
1. OWASP, Threat Modeling Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html — accessed 2026-10-14
2. Microsoft, Getting started with the Threat Modeling Tool — https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started — accessed 2026-10-14
3. Microsoft / MSDN Magazine, Uncover Security Design Flaws Using the STRIDE Approach (November 2006) — https://learn.microsoft.com/en-us/archive/msdn-magazine/2006/november/uncover-security-design-flaws-using-the-stride-approach — accessed 2026-10-14
4. NIST, SP 800-207 Zero Trust Architecture (2020) — https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf — accessed 2026-10-14
5. OWASP Threat Dragon, Getting started (current documentation) — https://www.threatdragon.com/docs/usage/getting-started.html — accessed 2026-10-14
6. Threat Modeling Manifesto, values and principles — https://www.threatmodelingmanifesto.org/ — accessed 2026-10-14
7. ISO/IEC/IEEE 42010:2022, public scope only (the direct fetch returned 403; full text not reviewed) — https://www.iso.org/standard/74393.html — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![F2 sample: online shop checkout data-flow diagram with browser, application and payment-provider trust boundaries and numbered flows](/samples/F2-threat-model-data-flow.svg)
*Sample pending (generated by the renderer from `examples/`).*
