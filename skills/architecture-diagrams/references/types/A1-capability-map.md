# Business Capability Map (业务能力图)
<!-- Generated from content/en/types/A1-capability-map.md by tools/build_skill_refs.py. Do not edit. -->
> What must the business be able to do, independent of who does it, how, or with which system, and which of those abilities are strong, weak, missing or strategic?
Scope: One enterprise or business unit, 2–3 capability levels on one page, optionally with one assessment overlay Neighbours: A2, A5, A7, A8, C1.

## Meaning
- **Question:** what abilities does the business need, regardless of who performs them, how, or with which system? With a heat overlay: which are weak, missing or strategic?
- **Viewpoint:** ArchiMate Capability Map viewpoint; TOGAF Phase B artefact (Business Capability Map). It shows the enterprise "at rest"; value streams (A2) and processes show it "in motion".
- **Value:** a capability model is stable against org structure, processes and applications, so it anchors cross-maps to org units, value-stream stages, applications and initiatives.
- **Leaves out:** sequence, org units, roles, systems, technology, product catalogue.
- **Definition used here:** the *model* is the full set of capabilities (often 3–6 levels); the *map* is its one-page picture (2–3 levels). Follows ArchiMate 3.2.

## When to use and how to choose
- **Audience:** executives and sponsors (Level 1 only), strategy and portfolio leads, enterprise and business architects (more depth).
- **Scenarios:** annual planning with a heat map; rationalisation after an acquisition (duplicate capabilities); scoping a transformation (new vs existing); application portfolio overlay (a derived view); team design around capabilities.
- **When not to use:** the question is sequence, timing or hand-offs (A2, A5, E4), system structure (C family) or one project's backlog (B family). Without agreed definitions, a one-level map with definitions beats a deep, contested one.
- **vs neighbours:**
  - **A2 Value Stream** for how value reaches a stakeholder; usually cross-mapped with A1.
  - **A5 BPMN Process** for steps, gateways, hand-offs.
  - **A3 Business Context** for "who"; capability × org is a matrix, not a merged picture.
  - **C1 Application Landscape** when the reader needs systems; the overlay is a derived view.
  - **A7 Conceptual Architecture** for "what are the parts"; a list of business abilities is A1, a list of product features is B3.
  - **A8 Roadmap** for when change happens.

## Notation and elements
- **Formal or informal:** ArchiMate gives a formal Capability element (rounded rectangle with a stepped icon) and a Capability Map viewpoint. The common business rendering is a convention: nested tiles, no arrows, optional colour overlay. TOGAF and BIZBOK prescribe content rules, not graphics.
- **Required:**
  - **Capability tiles,** each with a business-object-based name and a written definition in the catalogue, usually "Ability to …".
  - **Hierarchy by nesting:** Level 1 tiles contain their Level 2 children; 2–3 levels per page.
  - **Level 1 stratification** into tiers, usually *Strategic* (direction-setting), *Core / customer-facing* and *Supporting*. TOGAF notes that without stratification a large model is hard to read.
  - **Title** stating scope (enterprise or unit) and state (current or target).
- **Optional:**
  - **Heat-map overlay** with a legend. TOGAF lenses: maturity (green = at the desired level, yellow = one level away, red = two or more away, purple = desired but not existing), strategic contribution, performance, revenue contribution, cost contribution, coverage, criticality. One lens per map.
  - **Cross-maps as separate views:** capability × org unit (matrix), capability × value-stream stage (A2), capability × application (overlay).
  - **ArchiMate rendering:** capabilities nested by composition or aggregation; Resource and Outcome elements are allowed in the viewpoint.
- **Lines:** none in the business rendering; containment means decomposition. ArchiMate allows *serving* between capabilities and *realization* by core elements; keep these off the executive map.
- **Naming:** noun, compound noun or gerund ("Order Management", "Market Development"). BIZBOK pattern: object plus action noun, e.g. Level 1 "Customer Management" → Level 2 "Customer Definition", "Customer Matching", "Customer Information Management". No department names, no system names ("CRM" is an application; "Customer Management" is the capability).
- **Text budget:** about 2–5 words per tile; definitions live in the catalogue. Siblings are the same kind of thing at the same level.

## Best practices and anti-patterns
### Best practices
1. **Define before you draw.** Name and define each capability, then test it by decomposing it into the roles, processes, information and tools that realise it; this checks that it is a capability, not a process, function or service. Work business objects first, then actions on them, then decomposition.
2. **One map for the enterprise, each capability once,** even if several units perform it. Show the multiplicity in a capability × org cross-map.
3. **Build top-down with senior leaders, refine bottom-up.** Keep Level 1 small enough for senior leaders to ratify.
4. **Treat the heat map as a decision aid:** one stated criterion, a scale and a date or source. Different heat maps come from the same model.
5. **Use the stable map as the anchor** for cross-maps to value streams, org units, applications and initiatives.

### Anti-patterns
1. **The org chart re-labelled as capabilities.** TOGAF names this a common mistake.
2. **A system inventory as capabilities** ("CRM", "Data Lake" as tiles). When IT writes the names alone, the model reads like a system inventory with better labels.
3. **Processes or steps as capabilities** ("Approve refund"); verb-noun steps belong in a value stream or process.
4. **Duplicates or overlapping siblings,** or mixed kinds in one row (a capability next to a team next to a step).
5. **Heat colours without a legend or criterion,** several lenses in one colour scale, or red/green as the only cue. Also avoid more than 3 levels on one page and "TBD" or working notes on tiles.

## Drawing recipe
1. Fix scope, state and lens; put them in the title, e.g. "Online shop: business capabilities, current maturity".
2. Draft the catalogue first (Tier, Level, Name, "Ability to …" definition); remove org, system and step names and duplicates; show it to the user before drawing.
3. Layout: three horizontal bands top to bottom (Strategic, Core, Supporting); Level 1 tiles are containers per band, Level 2 tiles a grid inside. Max 3 levels; above ~60 leaf tiles, one page per Level 1 domain.
4. Equal sizes for siblings, aligned grid; size encodes nothing unless the legend says so.
5. Text: 2–5 words per tile; no bullets, definitions or uncommon abbreviations on the figure.
6. Colour: neutral fills with light tier tints; a heat map uses one scale plus at most one extra category ("desired, not existing"), a legend with criterion and source/date, and a text or pattern cue for colour-blind readers.
7. No arrows. Cross-maps (value stream, org, applications) are separate figures; an app overlay is labelled "derived view".

**Self-check**
- [ ] Every tile is a capability: business object plus action noun, no system, org unit or step.
- [ ] Each capability appears once; siblings do not overlap and are the same kind and level.
- [ ] Level 1 is stratified into tiers; at most 3 levels are visible.
- [ ] The title states scope and current/target; no subtitle restating the type, no version label.
- [ ] Heat colours have a legend with criterion, scale and source; one lens only.
- [ ] No arrows, bullets, "TBD" or reasoning text on tiles.
- [ ] Every capability has a definition in the accompanying catalogue.
- [ ] Any application overlay is labelled as derived; the base map is system-free.

## Evidence in a code repository
- **Candidate capabilities:** domain or bounded-context folders (`catalogue/`, `cart/`, `payment/`), route and menu definitions, feature-flag names, service names in deployment manifests, CODEOWNERS, issue labels and epics, analytics event families, README feature overviews. Map each to a business-object noun; drop technical modules (auth, logging).
- **Application overlay:** which repositories or services implement which capability.
- **Must come from people:** capabilities with no software (Brand Management, Supplier Management), definitions and tiering, which capabilities are strategic, maturity and investment scores, target-state capabilities.
- Mark any code-derived list as "candidate, to validate with the business".

## Guided-mode questions
1. Scope and state: whole enterprise, one unit or one product area; current, target or both? (one unit, current)
2. Which decision should the map support: investment, rationalisation, transformation scope or team design? (investment, which sets the heat lens)
3. Is there an existing capability list or reference model to align with? (draft one from docs and interviews, marked candidate)
4. How many levels, and stratify Level 1 into Strategic / Core / Supporting? (2 levels, stratified)
5. If heat-mapped: which single criterion and scale, scored by whom, as of when? (maturity, 4-colour TOGAF scale, dated)

## Template
Model template: `assets/templates/A1.json` · Layout template: `layered` · tiers become `layer` groups (bands), Level 1 capabilities become `frame` groups inside them, Level 2 capabilities are equal-size `component` nodes in a grid; heat values map to node `style` tokens (`primary`, `peer`, `planned`, `shared`) plus an auto-generated legend.

## Sample
Figure: `samples/A1-capability-map.svg` (published with the site)
