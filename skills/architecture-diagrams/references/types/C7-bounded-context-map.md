# Bounded Context Map (限界上下文映射图)
<!-- Generated from content/en/types/C7-bounded-context-map.md by tools/build_skill_refs.py. Do not edit. -->
> Which distinct models, each with its own consistent language, exist in and around this system, and what power, coordination or translation relationship holds across each boundary?
Scope: The bounded contexts of one system or landscape (or the teams behind them) and the relationship on each boundary; about 5–12 contexts per map. Neighbours: C5, C6, C8.

## Meaning
A context map answers: *which models with their own language exist here, and who must adapt to whom across each boundary?* A bounded context is the boundary within which one model and its terms stay consistent. The map is as much **socio-technical** as technical: Evans notes that the relationship constraints show up mainly through non-technical channels, and Brandolini deliberately includes team structure and influence that a traditional analysis would leave out. In ISO/IEC/IEEE 42010 terms its concerns are language consistency, integration cost, team coupling and who adapts to whom. It is not a C4 model level: its elements are models or teams, not deployables.

**Provenance (definition used here).** Evans' book (published August 2003) introduced Bounded Context, Context Map, Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Open Host Service, Published Language and Separate Ways. **Partnership** and **Big Ball of Mud** are *not* in the book. Evans' **DDD Reference (2015)** marks both as "new since the 2004 book". Brandolini used "partnership" in prose in 2009 and Vernon listed it in 2013. Big Ball of Mud builds on Foote & Yoder (1997). Earlier public use of "Partnership" by Evans was not found.

**Two variants:** a **system-landscape map** (default; contexts are software models) and an **organisational / team map** (contexts are teams and their relationships).

**Deliberately left out:** internals of each context (aggregates, entities; use a Bounded Context Canvas or D1), database tables, protocol detail (C6), deployment units (G1), call order (E1).

## When to use and how to choose
- **Audience:** architects, domain experts and product owners, tech leads, engineering managers deciding team boundaries. It is often the output of a strategic-design workshop such as big-picture EventStorming.
- **Classic scenarios:** (1) decompose a monolith, or plan a modular monolith or service split, before cutting code; (2) align several teams: who is upstream, who negotiates, who builds protective layers; (3) integrate a legacy or third-party system and decide between an anticorruption layer and conforming; (4) "map the existing terrain" of a multi-vendor landscape before transforming it; (5) turn language boundaries found in a workshop into a first draft.
- **When not to use:** one small app with one team and one vocabulary (a C3 container view is enough); purely technical integration questions (C6); deployment questions (G1). For readers without DDD vocabulary, use plain labels ("must follow", "translates") and keep the pattern names in the legend.
- **vs neighbours:**
  - Choose **C1/C2** to show *which systems exist and connect*. C7 shows where models end. Two systems can share one context, and one system can host several.
  - Choose **C3/C5** to group by deployable unit or responsibility. C7 groups by *language and model validity*.
  - Choose **C6** for the technical contract. C7 names the pattern (open host service, anticorruption layer…) that explains it, and that pattern can be a column in the C6 table.
  - Choose **C8** for structure *inside* one context. Slicing the whole system into UI/service/database layers is the classic wrong way to find contexts.

## Notation and elements
- **No formal standard.** Common notations: Evans/Vernon-style boxes and labelled lines; DDD Crew pattern glyphs; Context Mapper's CML text with a generated graph.
- **Required:** one named box per context, using a business name (it becomes ubiquitous language), never a technology name. Draw one line per relationship, give **every line a pattern label**, and add a legend for the abbreviations used.
- **Direction = influence, not data flow.** An asymmetric line points **upstream → downstream**, and data may flow both ways along it.
- **Roles sit on box edges; relationships are lines**:
  - *Upstream-side roles:* **OHS** Open Host Service (one open protocol for many consumers), **PL** Published Language (documented interchange language, often with OHS).
  - *Downstream-side roles:* **CF** Conformist (adopts the upstream model as-is), **ACL** Anticorruption Layer (translates into its own terms).
  - *Symmetric relationships (no U/D):* **P** Partnership (teams succeed or fail together; plan jointly), **SK** Shared Kernel (small, explicitly shared subset of model and code).
  - *Specialised upstream–downstream:* **C/S** Customer/Supplier (downstream priorities enter upstream planning).
  - *No relationship:* **Separate Ways**. *Fenced mess:* **Big Ball of Mud** (draw a boundary, do not model inside it).
- **Consistency rule:** never label a symmetric pair (P, SK) with U/D as well. A line is *either* symmetric *or* upstream–downstream.
- **Team relationships** for the organisational variant: mutually dependent, upstream/downstream, free.
- **Optional:** core/supporting/generic classification, owning team per context, AS-IS/TO-BE tag, a caution mark for an unresolved overlap.

## Best practices and anti-patterns
### Best practices

1. Start from language, not technology: a boundary shows where the same term means different things.
2. Map the AS-IS terrain honestly before proposing a TO-BE, and keep unresolved overlaps visible.
3. Choose each pattern by the *real* power structure. Make each context's owning team visible.
4. Keep maps small with one question per map, and include only the patterns that answer it.
5. Keep the map as versioned text in the repository (CML or diagram-as-code), and describe each context separately on a Bounded Context Canvas.

### Anti-patterns

1. **Context = microservice** as an identity. Service and context boundaries correlate. A service should not span two contexts, but one context may hold several services.
2. **Lines without a pattern**, or a pattern picked because the glossary has it.
3. **Layers called contexts:** slicing by UI / service / database.
4. **Wrong arrow meaning or wished-for state:** arrows drawn as data flow, or the desired integration drawn as if it existed.
5. **Inconsistent roles:** U/D on a Partnership pair, a large and fast-changing Shared Kernel, or legacy drawn with clean boundaries instead of a fenced Big Ball of Mud.

## Drawing recipe
1. List candidate contexts as language clusters: the same noun ("order", "product") with different meaning or fields signals a boundary.
2. Name each context with a business noun; add the owning team if known; classify core/supporting/generic only with evidence.
3. Choose the variant: system landscape (default) or organisational/team map.
4. For each interacting pair, ask "who must adapt to whom?". Choose symmetric (P, SK), upstream–downstream (with roles) or Separate Ways. Mark unknown pairs "unclear".
5. Layout: upstream above or left of downstream so influence reads top→bottom or left→right. OHS/PL tags sit on the upstream box edge, CF/ACL on the downstream edge. Symmetric pairs sit side by side with an undirected line.
6. External systems and any Big Ball of Mud go on the periphery with a dashed outline.
7. Text: box = name plus an optional small team line; line label = pattern abbreviations only; no technology logos.
8. Colour has one meaning only (classification *or* team); grey for external; amber only for problems.
9. Title with scope and state (AS-IS/TO-BE); legend limited to the abbreviations used; above about 12 contexts, split by question.

**Self-check**
- [ ] Every box is a model/language boundary, not a layer, tool or server.
- [ ] Every line has a pattern or an explicit "unclear".
- [ ] Asymmetric arrows point upstream → downstream, and the legend says so.
- [ ] No symmetric pair (P, SK) also carries U/D roles.
- [ ] Roles (OHS, PL, CF, ACL) sit on the correct side.
- [ ] AS-IS or TO-BE is declared; no future integration drawn as present.
- [ ] Each context has a consistent name and an owner (or "owner unknown").
- [ ] No tables or deployment names; colour has a single meaning.

## Evidence in a code repository
- Hints, not proof: top-level modules or packages (candidate contexts); the same entity name with different fields in two modules (language boundary); OpenAPI/AsyncAPI/protobuf files and topic names that are versioned and multi-consumer (OHS+PL).
- Adapter, translator or `legacy` packages and mapper classes (ACL); shared `common`/`shared-domain` libraries (Shared Kernel candidate, or a smell).
- Deployment manifests list services, which are candidate *implementations*; several may belong to one context.
- CODEOWNERS and team directories (ownership); glossary, ADRs and existing CML files (use those as the source of truth).
- Ask people: power and negotiation between teams, which pattern is real today, and the intended TO-BE.

## Guided-mode questions
1. What question should the map answer (split a monolith, align teams, plan an integration), and what is in scope? (Default: one landscape, integration planning.)
2. AS-IS or TO-BE; system-landscape or team map? (Default: AS-IS system-landscape map.)
3. Which terms mean different things in different parts of the business, and who owns each meaning? (Default: start from "product", "order", "customer".)
4. For each dependency: who adapts to whom, and is there a negotiated contract, a published API or a translation layer today? (Default: mark "unclear" until confirmed.)
5. Does the audience know DDD pattern names? (Default: pattern abbreviations with a plain-language legend.)

## Template
Model template: `assets/templates/C7.json` · Layout template: `nested` · each context is a `boundary` group holding one `component` node per key model (team in the node `sub`, role chips such as OHS/ACL in its `tags`); `edges` carry the pattern label with `dir` `->` for upstream→downstream or `--` for symmetric.

## Sample
Figure: `samples/ai-service-assistant/C7/en/diagram.svg` (published with the site)
