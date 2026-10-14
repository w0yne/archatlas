# Conceptual Architecture / Solution Overview (概念架构图 / 方案概览图)
<!-- Generated from content/en/types/A7-conceptual-architecture.md by tools/build_skill_refs.py. Do not edit. -->
> What big parts make up this solution, what does each part do for the business, and how do they depend on each other and on the outside world?
Scope: One solution opened one level below its context: 5–9 technology-neutral building blocks inside an explicit boundary, with users, channels and external systems at the edge. Neighbours: C1, C2, C3, C5, A1, A8.

## Meaning
A conceptual architecture answers "what big parts make up this solution, what does each do, and how do they depend on each other?" In ISO/IEC/IEEE 42010 terms it is an overview viewpoint whose concerns are scope, major building blocks and the solution approach. TOGAF defines it as the **Solution Concept diagram**, a Phase A artifact: "a high-level orientation of the solution", explicitly a "pencil sketch", used "to quickly on-board and align stakeholders". The C4 model has no conceptual level; an A7 sits between the System Context (C2) and Container (C3) views. It leaves out products, versions, protocols and deployment, feature lists (A1), process steps (A5, E4) and the path from as-is to to-be (A8).

**Definition used here:** the *notation* is informal (boxes, groups, arrows), but the *artifact* is defined (TOGAF Solution Concept). Azure calls this technology-agnostic level a "block or functional diagram". arc42 pairs it with the Level-1 whitebox of its building-block view, and DoDAF OV-1 is a related operational-concept graphic. "Marketecture" is a pejorative name for the bad version of it. ArchiMate references on this page follow **ArchiMate 3.2**; see the version note under Notation.

## When to use and how to choose
- **Audience:** executives, sponsors, steering and review boards, customer stakeholders, new joiners; architects use it as the cover page of an architecture pack.
- **Scenarios:** a vision workshop that aligns sponsors on what is being built (an online shop replatforming); a proposal "solution on a page"; the opening slide of an architecture review; onboarding; a reference picture for a recurring solution pattern.
- **When not to use:** engineers need interfaces, deployment or sequencing (C3, C5, G1, E1); the real question is scope only (C2) or the whole estate (C1); the story is a migration (A8); the content is a feature inventory (A1).
- **vs neighbours:**
  - Choose **C2 system context** when the audience only needs scope; A7 opens that black box one level.
  - Choose **C1 application landscape** for many systems across the enterprise; A7 is one solution.
  - Choose **A1 capability map** for what the business must be able to do; A7 shows which parts deliver it.
  - Choose **A8 target and roadmap** when the story is change over time; reuse this A7 as the target picture.
  - Choose **C3 / C5** as soon as readers ask which service calls which API.

## Notation and elements
- **Required:** a title with scope and state; an explicit solution boundary; 5–9 building blocks named as nouns in business language (a working heuristic, not a standard); users / channels at the edge; external systems as single boxes; main dependency arrows; a **key / legend** for every colour, shape, border and line style.
- **Optional:** one layering scheme (channels / applications / platform / data / infrastructure, or ArchiMate business / application / technology) applied to every system; up to 3 tags per block; one numbered headline flow; new vs existing highlighting; cross-cutting bands (identity, security, observability).
- **Lines:** directed arrows from requester to provider; no double-headed arrows (draw two flows if both directions matter); verb-phrase labels where meaning is not obvious; distinct line styles only if the legend explains them.
- **Level of detail:** one level below context; technology at most as a generic category ("search index", "message queue"), never a product name.
- **Naming:** peer blocks of the same kind (all components or all applications, never mixed with features or steps); full name plus abbreviation once.
- **Formal option:** the ArchiMate 3.2 **Layered viewpoint** spans business, application and technology; ArchiMate 2.x had an *Introductory* viewpoint with simplified notation for non-architects.
- **ArchiMate version note:** ArchiMate 4 was announced on 27 April 2026. A vendor summary reports that "layers" become "domains" and the concept set shrinks; the announcement itself does not list these details, and they are **not verified against the current spec text**.

## Best practices and anti-patterns
### Best practices

1. Match depth to the audience and say which audience it is: start with context, then go one layer down; "layer, don't overload".
2. Make the figure self-explanatory: title, legend, typed and named elements, labelled arrows; run the C4 model review checklist.
3. Keep notation consistent within and across diagrams: same colours, casing, sizes and line weights for similar things; peers look alike.
4. Stay accurate while abstract: "don't sacrifice accuracy for unnecessary simplicity"; use generic shapes, not vendor logos, for generic blocks.
5. Keep rationale off the figure: decisions go to the solution-strategy text or ADRs; keep block names traceable to the C2 and C3 views.

### Anti-patterns

1. "Marketecture": logos only, boxes without lines, unlabelled arrows, ambiguous levels of abstraction.
2. A feature list drawn as boxes; that is a capability map. An architecture view shows parts; features become tags at most.
3. Mixed abstraction among siblings, e.g. a container, an actor and a process step in one row.
4. Sentences or bullet lists inside boxes, and icons that decorate rather than mean something.
5. A non-focus subsystem drawn in full, or working notes ("TBD", "pending") on the figure instead of a legend category such as "planned".

## Drawing recipe
1. Fix the frame: audience, purpose, state (current or target) and the solution boundary; write the title first.
2. List candidate blocks from requirements and capabilities; merge or split to 5–9 of one kind, each a 1–4 word noun.
3. Choose one layering scheme, top to bottom: users / channels → solution services → shared platform → data. External systems sit right or bottom, outside the boundary. Use left-to-right only for one dominant flow.
4. Place each block in exactly one layer, inside or outside the boundary; collapse non-focus subsystems into one box.
5. Add at most about 10 directed arrows, requester → provider; group-level links end at the group border; label only non-obvious arrows; optionally number one headline flow.
6. Text: block name, an optional one-line role, ≤3 tags; no sentences; type scale title > layer label > block name > tag.
7. Colour: neutral by default; one accent for the solution's own (or new) blocks; one style for shared components, identical everywhere; grey for externals; pair colour with border or pattern.
8. Add the legend (colours, borders, lines, numbering); cross-check names against C2 above and C3 / C5 below.

**Self-check**
- [ ] The title states scope and as-is / to-be; no internal version labels.
- [ ] 5–9 blocks of the same kind, named in the audience's language.
- [ ] No feature lists, bullets or sentences in boxes; no product names, protocols or ports unless asked.
- [ ] The boundary is explicit; every element is inside exactly one group or marked external.
- [ ] Arrows are directed, end on what they mean and are labelled where not obvious.
- [ ] The legend explains every colour, shape, border and line style; peers share one style.
- [ ] Icons only where they carry meaning.
- [ ] Block names match the neighbouring C1 / C2 / C3 views.

## Evidence in a code repository
- **Useful:** README and `docs/` overviews and existing diagrams; top-level modules and deployable units (build files, compose files, Helm charts, IaC listing services and data stores); client SDKs and config naming external systems (payment provider, warehouse system); route and gateway definitions (channels); ADRs (solution strategy); CODEOWNERS (team-aligned blocks).
- **Ask people:** business-language names for blocks, which parts matter to this audience, target blocks that do not exist yet, and ownership as the business sees it.
- Code gives physical evidence; lift it to the conceptual level and confirm the result with the sponsor or architect.

## Guided-mode questions
1. Who will read this, and what should they understand or decide afterwards? (sponsors and reviewers, business + IT overview depth)
2. Current or target state, and where is the solution boundary? (target state; boundary = the systems this team builds or changes)
3. Which parts are the focus, and which neighbours appear only as single boxes? (focus on the solution's own blocks; everything else one box each)
4. Which layering scheme, and should new vs existing parts be distinguished? (channels / services / platform / data; yes, if anything is reused)
5. Technology categories ("search index") or no technology at all? (generic categories only)

## Template
Model template: `assets/templates/A7.json` · Layout template: `layered` · groups of kind `layer` become horizontal bands inside a `boundary` group; blocks are equal-size columns per band; external systems are placed outside the boundary.

## Sample
Figure: `samples/A7-conceptual-architecture.svg` (published with the site)
