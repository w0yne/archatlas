---
code: A7
slug: conceptual-architecture
family: A
names:
  en: Conceptual architecture (solution overview)
  zh: 概念架构图（方案概览）
  aliases:
    en: [solution overview, solution concept diagram, high-level architecture, architecture on a page, block diagram, functional diagram]
    zh: [方案概览图, 方案总览, 高层架构图, 一页纸架构, 方案构想图, 概念架构图]
question: What big parts make up this solution, what does each part do for the business, and how do they depend on each other and on the outside world?
audiences: [leaders, business, architects]
levels: [concept]
phases: [initiate, design]
scope: 'One solution opened one level below its context: 5–9 technology-neutral building blocks inside an explicit boundary, with users, channels and external systems at the edge.'
formal: {kind: method, ref: 'TOGAF Solution Concept diagram (Phase A artifact, TOGAF 9.1 §35.6.2); informal notation; ArchiMate 3.2 Layered viewpoint as the formal option'}
neighbours: [A1, A8, C1, C2, C3, C5, I2]
status: draft
---

# Conceptual Architecture / Solution Overview (概念架构图 / 方案概览图)

> One page that shows what a solution is made of, in business words and without product names, so sponsors and reviewers agree on the shape before the detailed views.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A conceptual architecture answers "what big parts make up this solution, what does each do, and how do they depend on each other?" In ISO/IEC/IEEE 42010 terms it is an overview viewpoint whose concerns are scope, major building blocks and the solution approach. TOGAF defines it as the **Solution Concept diagram**, a Phase A artifact: "a high-level orientation of the solution", explicitly a "pencil sketch", used "to quickly on-board and align stakeholders" [1][2]. The C4 model has no conceptual level; an A7 sits between the System Context (C2) and Container (C3) views [3]. It leaves out products, versions, protocols and deployment, business capability lists (A1), product feature breakdowns (B3), process steps (A5, E4) and the path from as-is to to-be (A8).

**Definition used here:** the *notation* is informal (boxes, groups, arrows), but the *artifact* is defined (TOGAF Solution Concept). Azure calls this technology-agnostic level a "block or functional diagram" [5]. arc42 pairs it with the Level-1 whitebox of its building-block view [13], and DoDAF OV-1 is a related operational-concept graphic [8]. "Marketecture" is a pejorative name for the bad version of it [17]. ArchiMate references on this page follow **ArchiMate 3.2**; see the version note under Notation.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** executives, sponsors, steering and review boards, customer stakeholders, new joiners; architects use it as the cover page of an architecture pack.
- **Scenarios:** a vision workshop that aligns sponsors on what is being built (an online shop replatforming); a proposal "solution on a page"; the opening slide of an architecture review; onboarding; a reference picture for a recurring solution pattern [14][15][16].
- **When not to use:** engineers need interfaces, deployment or sequencing (C3, C5, G1, E1); the real question is scope only (C2) or the whole estate (C1); the story is a migration (A8); the content is a list of business abilities (A1) or of product features (B3).
- **vs neighbours:**
  - Choose **C2 system context** when the audience only needs scope; A7 opens that black box one level.
  - Choose **C1 application landscape** for many systems across the enterprise; A7 is one solution.
  - Choose **A1 capability map** for what the business must be able to do; A7 shows which parts deliver it [9].
  - Choose **A8 target and roadmap** when the story is change over time; reuse this A7 as the target picture.
  - Choose **C3 / C5** as soon as readers ask which service calls which API.
  - Choose **I2** when business, application and technology elements and their formal ArchiMate relationships must appear in one view.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required:** a title with scope and state; an explicit solution boundary; 5–9 building blocks named as nouns in business language (a working heuristic, not a standard); users / channels at the edge; external systems as single boxes; main dependency arrows; a **key / legend** for every colour, shape, border and line style [4][6].
- **Optional:** one layering scheme (channels / applications / platform / data / infrastructure, or ArchiMate business / application / technology) applied to every system; up to 3 tags per block; one numbered headline flow; new vs existing highlighting; cross-cutting bands (identity, security, observability).
- **Lines:** directed arrows from requester to provider; no double-headed arrows (draw two flows if both directions matter); verb-phrase labels where meaning is not obvious; distinct line styles only if the legend explains them [4][5].
- **Level of detail:** one level below context; technology at most as a generic category ("search index", "message queue"), never a product name [5].
- **Naming:** peer blocks of the same kind (all components or all applications, never mixed with features or steps); full name plus abbreviation once [4].
- **Formal option:** the ArchiMate 3.2 **Layered viewpoint** spans business, application and technology [6]; ArchiMate 2.x had an *Introductory* viewpoint with simplified notation for non-architects [7].
- **ArchiMate version note:** ArchiMate 4 was announced on 27 April 2026 [10]. A vendor summary reports that "layers" become "domains" and the concept set shrinks [11]; the announcement itself does not list these details, and they are **not verified against the current spec text**.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices

1. Match depth to the audience and say which audience it is: start with context, then go one layer down; "layer, don't overload" [5].
2. Make the figure self-explanatory: title, legend, typed and named elements, labelled arrows; run the C4 model review checklist [4].
3. Keep notation consistent within and across diagrams: same colours, casing, sizes and line weights for similar things; peers look alike [4][5].
4. Stay accurate while abstract: "don't sacrifice accuracy for unnecessary simplicity"; use generic shapes, not vendor logos, for generic blocks [5].
5. Keep rationale off the figure: decisions go to the solution-strategy text or ADRs [12]; keep block names traceable to the C2 and C3 views.

### Anti-patterns

1. "Marketecture": logos only, boxes without lines, unlabelled arrows, ambiguous levels of abstraction [17].
2. A feature list drawn as boxes. Business abilities belong in a capability map (A1) and product features in a feature tree (B3); an architecture view shows parts, and features become tags at most [9].
3. Mixed abstraction among siblings, e.g. a container, an actor and a process step in one row [4].
4. Sentences or bullet lists inside boxes, and icons that decorate rather than mean something [5].
5. A non-focus subsystem drawn in full, or working notes ("TBD", "pending") on the figure instead of a legend category such as "planned" [4].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [C4 model, System context diagram](https://c4model.com/diagrams/system-context) and [System landscape diagram](https://c4model.com/diagrams/system-landscape) — the clearest public reference for the levels around A7: title, key, labelled one-way arrows; CC BY 4.0 [18][19].
- [The Open Group, TOGAF 9 and ArchiMate 1.0 white paper](https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf) — layered baseline and target views with one layering logic for every application; Open Group copyright [20].
- [SAP AppHaus, Generate a Solution Concept Diagram](https://apphaus.sap.com/resource/solution-concept-diagram) — a practical method: blocks derived from capabilities, request→response arrows, stakeholder validation [9].
- [Azure Architecture Center, Browse architectures](https://learn.microsoft.com/en-us/azure/architecture/browse/) — overview diagram plus numbered dataflow list; mostly component level, so read for structure and captioning [15].
- [AWS Reference Architecture Diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/) — one page, one numbered flow; physical level, use as a layout model only [14].

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
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

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Useful:** README and `docs/` overviews and existing diagrams; top-level modules and deployable units (build files, compose files, Helm charts, IaC listing services and data stores); client SDKs and config naming external systems (payment provider, warehouse system); route and gateway definitions (channels); ADRs (solution strategy); CODEOWNERS (team-aligned blocks).
- **Ask people:** business-language names for blocks, which parts matter to this audience, target blocks that do not exist yet, and ownership as the business sees it.
- Code gives physical evidence; lift it to the conceptual level and confirm the result with the sponsor or architect.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Who will read this, and what should they understand or decide afterwards? (sponsors and reviewers, business + IT overview depth)
2. Current or target state, and where is the solution boundary? (target state; boundary = the systems this team builds or changes)
3. Which parts are the focus, and which neighbours appear only as single boxes? (focus on the solution's own blocks; everything else one box each)
4. Which layering scheme, and should new vs existing parts be distinguished? (channels / services / platform / data; yes, if anything is reused)
5. Technology categories ("search index") or no technology at all? (generic categories only)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A7.json` · Layout template: `layered` · groups of kind `layer` become horizontal bands inside a `boundary` group; blocks are equal-size columns per band; external systems are placed outside the boundary.

## Sources {#sources}
<!-- skill: omit -->
1. The Open Group, TOGAF Version 9.1 (2011), §35.6.2 Solution Concept Diagram (evaluation copy, third-party hosted) — http://www.crvs-dgb.org/wp-content/uploads/2015/07/I112.pdf — accessed 2026-10-14
2. The Open Group, World-Class Enterprise Architecture: Framework Guidance and TOGAF 9 Example (white paper, 2010) — https://pubs.opengroup.org/onlinepubs/7698999699/toc.pdf — accessed 2026-10-14
3. C4 model, Abstractions — https://c4model.com/abstractions — accessed 2026-10-14
4. C4 model, Notation and Review checklist — https://c4model.com/diagrams/notation ; https://c4model.com/diagrams/checklist — accessed 2026-10-14
5. Microsoft, Create architecture design diagrams, Azure Well-Architected Framework — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams — accessed 2026-10-14
6. Linked.Archi, ArchiMate 3.2 Example Viewpoints (secondary listing of the spec appendix) — https://meta.linked.archi/archimate3/viewpoints — accessed 2026-10-14
7. Archi User Guide, Sketch View (quotes the ArchiMate 2.x Introductory viewpoint) — https://www.archimatetool.com/downloads/archi/Archi%20User%20Guide.pdf — accessed 2026-10-14
8. The Open Group, TOGAF 9 and the US DoDAF 2.0 (white paper; OV-1 High-Level Operational Concept Graphic, a neighbour) — https://pubs.opengroup.org/onlinepubs/7698999499/toc.pdf — accessed 2026-10-14
9. SAP AppHaus, Generate a Solution Concept Diagram — https://apphaus.sap.com/resource/solution-concept-diagram — accessed 2026-10-14
10. The Open Group, The Open Group Announces ArchiMate 4 Specification (press release, 27 April 2026) — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — accessed 2026-10-14
11. Bizzdesign (M. Lankhorst), ArchiMate 4 Specification: What Changed from Version 3.2? — https://bizzdesign.com/blog/archimate-4-changes — accessed 2026-10-14
12. arc42, Section 4: Solution Strategy — https://docs.arc42.org/section-4/ — accessed 2026-10-14
13. arc42, Section 5: Building Block View — https://docs.arc42.org/section-5/ — accessed 2026-10-14
14. AWS Reference Architecture Diagrams — https://docs.aws.amazon.com/reference-architecture-diagrams/ — accessed 2026-10-14
15. Azure Architecture Center, Browse architectures — https://learn.microsoft.com/en-us/azure/architecture/browse/ — accessed 2026-10-14
16. Google Cloud Architecture Center — https://cloud.google.com/architecture — accessed 2026-10-14
17. Simon Brown, Speaking (talk abstracts on "boxes and arrows" and "Marketecture") — https://simonbrown.je/speaking — accessed 2026-10-14
18. C4 model, System context diagram — https://c4model.com/diagrams/system-context — accessed 2026-10-14
19. C4 model, System landscape diagram — https://c4model.com/diagrams/system-landscape — accessed 2026-10-14
20. H. Jonkers, E. Proper, M. Turner, TOGAF 9 and ArchiMate 1.0 (Open Group white paper, 2009) — https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![A7 sample: conceptual architecture of an online shop with channels, applications and data](/samples/A7-conceptual-architecture.svg)
*Conceptual architecture of the online shop: one boundary with three bands (channels, applications, data) and the building blocks Storefront, Ordering, Catalogue and Shop data. Ordering sends payment requests to the external payment provider outside the boundary.*
