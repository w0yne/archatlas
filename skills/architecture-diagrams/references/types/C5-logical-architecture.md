# Logical Architecture Diagram (逻辑架构图)
<!-- Generated from content/en/types/C5-logical-architecture.md by tools/build_skill_refs.py. Do not edit. -->
> Which technology-neutral building blocks must the system have, what is each responsible for, and through which named interfaces do they depend on each other and on external capabilities?
Scope: One system or one solution, decomposed into responsibility blocks (one level, one page). Neighbours: A7, C1, C2, C3, C4, C6, C7, C8, G1, I1.

## Meaning
A logical architecture diagram answers: *which blocks must exist, what does each own, and how do they depend on each other — whatever products or hosts will later realise them?* Its concerns are allocation of responsibility, traceability from requirements to blocks, change impact, make/buy/reuse decisions and splitting work between teams. Systems-engineering guidance warns that jumping straight from requirements to a physical design is a common mistake, because stakeholders revert to familiar solutions. In ISO/IEC/IEEE 42010 terms it is a view under a structural/functional viewpoint; in C4 model terms it sits beside the container level, but without the technology labels the C4 model requires.

"Logical" has at least five published meanings: Kruchten's 4+1 logical view (a class-level object model); TOGAF's *Logical Application Component*, "independent of a particular implementation"; the systems-engineering logical architecture that is later allocated to a physical one; the "Logical" viewpoint of IEEE 1016 (not verified against the current standard text); and the informal "software, not hardware".

**Definition used here:** a technology-neutral decomposition of one system or solution into responsibility-bearing building blocks, with their named interfaces and dependencies, drawn so that more than one physical or deployment design could realise it. This is closest to the Rozanski & Woods Functional viewpoint and the arc42 level-1 building block view. The 4+1 logical view (catalogue I1) is the same intent at a finer, class-level grain.

**Related but different:** "functional architecture" in systems engineering is a *tree of functions* that feeds the logical blocks, not a block diagram; the SEI "module view" shows *code units*. Neither is this type.

**Deliberately left out:** products, frameworks and versions; hosts, networks, replicas and zones; runtime processes and concurrency; data schemas; call order of scenarios; class-level detail. Infrastructure appears only when it is functionally significant, such as a message bus that transforms data.

## When to use and how to choose
- **Audience:** solution architects, developers and tech leads, product owners (requirement coverage), reviewers comparing build/buy options. Not for executives (use A7 or C1) or operators (use G1).
- **Classic scenarios:** (1) compare technology or vendor options by mapping each onto one logical view; (2) turn requirements into blocks so each lands on exactly one owner; (3) split work and ownership between teams along block boundaries; (4) answer "what does the system consist of?" after a context diagram has been shown; (5) review a partner proposal for gaps and overlaps.
- **When not to use:** the audience needs hosts, scaling or zones (G1/G2); technology is already fixed and readers are developers (C3/C4); you need call order or error paths (E1); the system is one small process (a short module list is enough); the boxes would only list features (that is a capability map, A1).
- **vs neighbours:**
  - Choose **A7 Conceptual architecture** when the reader wants coarse, business-level blocks without interfaces.
  - Choose **C3 Container diagram** when runnable units, their technology and protocols matter; the C4 model requires a technology per container.
  - Choose **C4 Component diagram** when you are inside *one* container and the components carry technology labels; C4 model components are not separately deployable. Decision rule: technology-neutral and system-wide → C5; technology-labelled and per container → C4.
  - Choose **C6 Integration/interface** when protocol, authentication and SLA of each interface matter.
  - Choose **C8 Layered architecture** when the point is an allowed-dependency *rule* inside code; a C5 may be grouped in bands, but states no such rule.
  - Choose **G1 Deployment** when the question is where things run.

## Notation and elements
- **No standard notation.** Plain boxes are the default. UML component diagrams (suggested for the functional view), ArchiMate Application Components and Interfaces, or Capella logical architecture diagrams are optional formal choices. ArchiMate 3.2 (2022) is current; ArchiMate 4 was announced in April 2026 and renames layers to domains.
- **ArchiMate caveat:** its Application Component is "aligned to implementation structure", so to stay logical name *types*, not instances, and keep Node and System Software out. TOGAF's *Logical* Application Component is the implementation-independent term.
- **Required:** title naming type and scope ("Logical view: online shop"); one system boundary; building blocks with a noun-phrase name and one short responsibility; external capabilities outside the boundary in a distinct style; a label on every dependency naming the operation or information exchanged; a legend for every shape, colour and line style.
- **Optional:** grouping frames by responsibility cluster; a handful of numbered key interactions; a "planned" marker defined in the legend.
- **Companion table:** block | responsibility | provided interfaces | required interfaces. This is the Rozanski & Woods element template and the arc42 black-box table.
- **Arrow semantics:** one meaning per diagram. Prefer *depends-on/calls* (consumer → provider) and keep data flow for D2. The label must agree with the arrow direction; avoid a bare "uses".
- **Level of detail:** below "whole system", above "class"; one page; always do level 1 and zoom only where risk justifies it.
- **Naming:** blocks are responsibility nouns ("Checkout", "Order Management"), never product names; interfaces are verb–noun ("reserve stock"); externals are role names ("Payment Provider"), not brands.

## Best practices and anti-patterns
### Best practices

1. State the definition of "logical" and the scope in the title or caption before drawing.
2. Give every block one responsibility and justify why the system is cut this way; hide the inner workings of black boxes.
3. Derive interfaces from the responsibilities they serve. Connecting blocks by intuition produces missing or useless interfaces.
4. Keep the logical model as a stable anchor and allocate it to physical units in a separate step.
5. Put inbound and outbound interfaces per block in a table beside the figure, and review against the C4 model checklist (title, legend, every line labelled, direction matches label).

### Anti-patterns

1. **Technology leakage:** product names inside the boundary turn C5 into a weak C3 and defeat option comparison.
2. **Assumed one-to-one deployment:** a logical block may map to one container, part of one or several.
3. **Class-diagram granularity:** classes without architectural significance belong to a lower level.
4. **Feature lists in boxes, or mixed element kinds** (actors, steps and blocks side by side): structure disappears behind text.
5. **Unlabelled or mixed-meaning arrows**, and status notes ("TBD") on the figure instead of a legend entry.

## Drawing recipe
1. Fix definition and scope: "logical = technology-neutral responsibility blocks and interfaces" for one system or solution.
2. List requirements/capabilities; assign each to exactly one block; group by cohesion; name blocks with nouns.
3. Derive each dependency from a responsibility and label it with the operation or information; drop any without a requirement behind it.
4. Put external capabilities (identity, payment provider, warehouse) outside the boundary.
5. Layout: top-to-bottom by dependency (consumer-facing blocks on top, providers below) or left-to-right for a request flow; 2–5 frames of about 3–7 blocks each (heuristic).
6. Text: block = name (≤3 words) + at most one responsibility line; interface label ≤3 words; detail goes into the companion table.
7. Colour encodes role only (internal / external / planned), never technology; add a legend.
8. Arrows: one meaning (depends-on), orthogonal, ending on the box or on the group border.
9. If technology is fixed later, redraw as C3/C4 instead of adding tags to C5.

**Self-check**
- [ ] Title names type and scope; legend explains every shape, colour and line.
- [ ] No product, framework or host names inside the boundary.
- [ ] Each block has one responsibility; no requirement is unowned or owned twice.
- [ ] Every line is labelled and the label matches the arrow direction.
- [ ] Siblings are the same kind of thing; no actors, steps or feature lists mixed in.
- [ ] External capabilities are outside the boundary and visibly different.
- [ ] Two different physical designs could realise this diagram.
- [ ] No status notes on the figure; every badge or number is explained.

## Evidence in a code repository
- Useful: top-level module/package structure; interface and port definitions, `.proto` and OpenAPI files; import/dependency graphs; README and ADRs (intended responsibilities); route or menu definitions (features → blocks); CODEOWNERS; catalog descriptors such as Backstage `catalog-info.yaml`.
- Misleading on their own: `docker-compose.yml`, Kubernetes manifests and IaC describe containers and deployment (C3/G1); use them only to check that each runnable unit maps to a block.
- Ask people: intended responsibilities, the rationale of the cut, planned blocks and acceptable external capabilities. Treat code-derived blocks as a draft to confirm.

## Guided-mode questions
1. What should this diagram help decide (option comparison, work split, requirement coverage, onboarding) and who reads it? (Default: architects and developers; requirement coverage.)
2. One system or several; which part gets detail, which collapses to one box? (Default: whole system at one level; externals collapsed.)
3. Which "logical" do you mean: responsibility blocks, a class-level model, or a function tree? (Default: responsibility blocks; the others route to class/ER or function decomposition.)
4. Are technology choices already fixed? (Default: no; if yes, offer C3/C4 and keep the mapping in a table.)
5. Which external capabilities and which 3–6 key interactions must appear? (Default: identity, payment provider, the main purchase request.)

## Template
Model template: `assets/templates/C5.json` · Layout template: `layered` · Groups of kind `frame` become horizontal bands of responsibility blocks inside one `boundary`; externals sit outside it and `edges` of kind `dependency` carry operation labels.

## Sample
Figure: `samples/C5-logical-architecture.svg` (published with the site)
