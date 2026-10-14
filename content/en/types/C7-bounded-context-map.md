---
code: C7
slug: bounded-context-map
family: C
names:
  en: Bounded context map (DDD)
  zh: 限界上下文映射（DDD）
  aliases:
    en: [context map, DDD context map, strategic design map, team map (organisational variant)]
    zh: [上下文映射图, DDD 战略设计图, 领域上下文图, DDD 上下文映射, 战略设计图, 团队映射图]
question: Which distinct models, each with its own consistent language, exist in and around this system, and what power, coordination or translation relationship holds across each boundary?
audiences: [architects, developers, business]
levels: [concept, logical]
phases: [design]
scope: The bounded contexts of one system or landscape (or the teams behind them) and the relationship on each boundary; about 5–12 contexts per map.
formal: {kind: method, ref: 'Domain-Driven Design: Evans, DDD (2003) and DDD Reference (2015, CC BY 4.0); no graphical standard'}
neighbours: [C5, C6, C8]
status: draft
---

# Bounded Context Map (限界上下文映射图)

> A map of where one domain model ends and the next begins, and which relationship pattern (who adapts to whom, who translates) holds on each boundary.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->

A context map answers: *which models with their own language exist here, and who must adapt to whom across each boundary?* A bounded context is the boundary within which one model and its terms stay consistent [1][5]. The map is as much **socio-technical** as technical: Evans notes that the relationship constraints show up mainly through non-technical channels [1], and Brandolini deliberately includes team structure and influence that a traditional analysis would leave out [3]. In ISO/IEC/IEEE 42010 terms its concerns are language consistency, integration cost, team coupling and who adapts to whom [12]. It is not a C4 model level: its elements are models or teams, not deployables.

**Provenance (definition used here).** Evans' book (published August 2003) introduced Bounded Context, Context Map, Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Open Host Service, Published Language and Separate Ways. **Partnership** and **Big Ball of Mud** are *not* in the book. Evans' **DDD Reference (2015)** marks both as "new since the 2004 book" [1]. Brandolini used "partnership" in prose in 2009 [3] and Vernon listed it in 2013 [4]. Big Ball of Mud builds on Foote & Yoder (1997) [1]. Earlier public use of "Partnership" by Evans was not found.

**Two variants:** a **system-landscape map** (default; contexts are software models) and an **organisational / team map** (contexts are teams and their relationships) [6].

**Deliberately left out:** internals of each context (aggregates, entities; use a Bounded Context Canvas or D1), database tables, protocol detail (C6), deployment units (G1), call order (E1).

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->

- **Audience:** architects, domain experts and product owners, tech leads, engineering managers deciding team boundaries. It is often the output of a strategic-design workshop such as big-picture EventStorming [8].
- **Classic scenarios:** (1) decompose a monolith, or plan a modular monolith or service split, before cutting code; (2) align several teams: who is upstream, who negotiates, who builds protective layers [8]; (3) integrate a legacy or third-party system and decide between an anticorruption layer and conforming; (4) "map the existing terrain" of a multi-vendor landscape before transforming it [1]; (5) turn language boundaries found in a workshop into a first draft.
- **When not to use:** one small app with one team and one vocabulary (a C3 container view is enough); purely technical integration questions (C6); deployment questions (G1). For readers without DDD vocabulary, use plain labels ("must follow", "translates") and keep the pattern names in the legend.
- **vs neighbours:**
  - Choose **C1/C2** to show *which systems exist and connect*. C7 shows where models end. Two systems can share one context, and one system can host several.
  - Choose **C3/C5** to group by deployable unit or responsibility. C7 groups by *language and model validity*.
  - Choose **C6** for the technical contract. C7 names the pattern (open host service, anticorruption layer…) that explains it, and that pattern can be a column in the C6 table.
  - Choose **C8** for structure *inside* one context. Slicing the whole system into UI/service/database layers is the classic wrong way to find contexts [5].

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->

- **No formal standard.** Common notations: Evans/Vernon-style boxes and labelled lines; DDD Crew pattern glyphs [7]; Context Mapper's CML text with a generated graph [6].
- **Required:** one named box per context, using a business name (it becomes ubiquitous language), never a technology name. Draw one line per relationship, give **every line a pattern label**, and add a legend for the abbreviations used.
- **Direction = influence, not data flow.** An asymmetric line points **upstream → downstream** [6], and data may flow both ways along it.
- **Roles sit on box edges; relationships are lines** [6]:
  - *Upstream-side roles:* **OHS** Open Host Service (one open protocol for many consumers), **PL** Published Language (documented interchange language, often with OHS).
  - *Downstream-side roles:* **CF** Conformist (adopts the upstream model as-is), **ACL** Anticorruption Layer (translates into its own terms).
  - *Symmetric relationships (no U/D):* **P** Partnership (teams succeed or fail together; plan jointly), **SK** Shared Kernel (small, explicitly shared subset of model and code).
  - *Specialised upstream–downstream:* **C/S** Customer/Supplier (downstream priorities enter upstream planning).
  - *No relationship:* **Separate Ways**. *Fenced mess:* **Big Ball of Mud** (draw a boundary, do not model inside it).
- **Consistency rule:** never label a symmetric pair (P, SK) with U/D as well. A line is *either* symmetric *or* upstream–downstream [6].
- **Team relationships** for the organisational variant: mutually dependent, upstream/downstream, free [1][7].
- **Optional:** core/supporting/generic classification, owning team per context, AS-IS/TO-BE tag, a caution mark for an unresolved overlap [3].

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### Best practices

1. Start from language, not technology: a boundary shows where the same term means different things [5].
2. Map the AS-IS terrain honestly before proposing a TO-BE, and keep unresolved overlaps visible [1][3].
3. Choose each pattern by the *real* power structure. Make each context's owning team visible [3][9].
4. Keep maps small with one question per map, and include only the patterns that answer it [7].
5. Keep the map as versioned text in the repository (CML or diagram-as-code), and describe each context separately on a Bounded Context Canvas [6][7].

### Anti-patterns

1. **Context = microservice** as an identity. Service and context boundaries correlate [10]. A service should not span two contexts, but one context may hold several services [11].
2. **Lines without a pattern**, or a pattern picked because the glossary has it.
3. **Layers called contexts:** slicing by UI / service / database [5].
4. **Wrong arrow meaning or wished-for state:** arrows drawn as data flow, or the desired integration drawn as if it existed.
5. **Inconsistent roles:** U/D on a Partnership pair, a large and fast-changing Shared Kernel, or legacy drawn with clean boundaries instead of a fenced Big Ball of Mud.

## Exemplars {#exemplars}
<!-- skill: omit -->

- [Context Mapper examples](https://github.com/ContextMapper/context-mapper-examples) — text model and generated map side by side, AS-IS/TO-BE, system and team maps (Apache-2.0).
- [DDD Crew, Context Mapping](https://github.com/ddd-crew/context-mapping) — cheat sheet and pattern glyphs, with team relationships (README says CC BY 4.0, repository metadata says CC BY-SA 4.0; check before reusing graphics).
- [Brandolini, "Strategic Domain Driven Design with Context Mapping"](https://www.infoq.com/articles/ddd-contextmapping) — a worked, evolving AS-IS map with caution marks and team context (licence not checked).
- [Microsoft, "Use domain analysis to model microservices"](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) — from domain sketch to contexts, to a relationship list, to service boundaries (Microsoft Learn terms).
- [Evans, DDD Reference (2015)](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) — the canonical pattern definitions in a short PDF (CC BY 4.0).

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->

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

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->

- Hints, not proof: top-level modules or packages (candidate contexts); the same entity name with different fields in two modules (language boundary); OpenAPI/AsyncAPI/protobuf files and topic names that are versioned and multi-consumer (OHS+PL).
- Adapter, translator or `legacy` packages and mapper classes (ACL); shared `common`/`shared-domain` libraries (Shared Kernel candidate, or a smell).
- Deployment manifests list services, which are candidate *implementations*; several may belong to one context.
- CODEOWNERS and team directories (ownership); glossary, ADRs and existing CML files (use those as the source of truth).
- Ask people: power and negotiation between teams, which pattern is real today, and the intended TO-BE.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->

1. What question should the map answer (split a monolith, align teams, plan an integration), and what is in scope? (Default: one landscape, integration planning.)
2. AS-IS or TO-BE; system-landscape or team map? (Default: AS-IS system-landscape map.)
3. Which terms mean different things in different parts of the business, and who owns each meaning? (Default: start from "product", "order", "customer".)
4. For each dependency: who adapts to whom, and is there a negotiated contract, a published API or a translation layer today? (Default: mark "unclear" until confirmed.)
5. Does the audience know DDD pattern names? (Default: pattern abbreviations with a plain-language legend.)

## Template {#template}
<!-- skill: keep (≤3 lines) -->

Model template: `assets/templates/C7.json` · Layout template: `nested` · each context is a `boundary` group holding one `component` node per key model (team in the node `sub`, role chips such as OHS/ACL in its `tags`); `edges` carry the pattern label with `dir` `->` for upstream→downstream or `--` for symmetric.

## Sources {#sources}
<!-- skill: omit -->

1. Evans, *Domain-Driven Design Reference: Definitions and Pattern Summaries* (2015, CC BY 4.0) — https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf — accessed 2026-10-14
2. Wikipedia, "Domain-driven design" (Evans' book, August 2003) — https://en.wikipedia.org/wiki/Domain-driven_design — accessed 2026-10-14 (secondary)
3. Brandolini, "Strategic Domain Driven Design with Context Mapping", InfoQ (2009) — https://www.infoq.com/articles/ddd-contextmapping — accessed 2026-10-14
4. Vernon, *Implementing Domain-Driven Design* (2013), sample pages — https://ptgmedia.pearsoncmg.com/images/9780321834577/samplepages/0321834577.pdf — accessed 2026-10-14
5. Fowler, "BoundedContext" (2014) — https://martinfowler.com/bliki/BoundedContext.html — accessed 2026-10-14
6. Context Mapper, Context Map and language semantics — https://contextmapper.org/docs/context-map/ — accessed 2026-10-14
7. DDD Crew, Context Mapping — https://github.com/ddd-crew/context-mapping — accessed 2026-10-14
8. DDD Crew, DDD Starter Modelling Process — https://github.com/ddd-crew/ddd-starter-modelling-process — accessed 2026-10-14
9. Avanscoperta, "Context Mapping in DDD" — https://www.avanscoperta.it/en/context-mapping/ — accessed 2026-10-14
10. Lewis & Fowler, "Microservices" (2014) — https://martinfowler.com/articles/microservices.html — accessed 2026-10-14
11. Microsoft Learn, "Identify microservice boundaries" — https://learn.microsoft.com/en-us/azure/architecture/microservices/model/microservice-boundaries — accessed 2026-10-14
12. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/ieee-1471/cm — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->

![C7 sample: online-shop context map — Catalogue (OHS, PL) upstream of Ordering (CF); Ordering and Payments in Partnership; Ordering as supplier to Fulfilment; Fulfilment with an ACL against the legacy warehouse system (Big Ball of Mud); Payments with an ACL against the external payment provider (OHS); Customer Support conforming to Ordering](/samples/C7-bounded-context-map.svg)
*Sample pending (generated by the renderer from `examples/`).*
