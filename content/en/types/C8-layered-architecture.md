---
code: C8
slug: layered-architecture
family: C
names:
  en: Layered Architecture Diagram
  zh: 分层架构图
  aliases:
    en: [layer diagram, layered view, N-layer architecture, presentation-domain-data layering, hexagonal architecture (variant), ports and adapters (variant), onion architecture (variant), clean architecture (variant)]
    zh: [层次结构图, 技术分层图, 六边形架构, 端口与适配器, 洋葱架构, 整洁架构]
question: "Into which responsibility layers is one application's code divided, and which dependency directions are allowed and which forbidden?"
audiences: [developers, tech leads, code reviewers, architects, new joiners]
level: logical
phases: [design, build, review]
scope: "One application, service or bounded context: its code layers (or rings) and the dependency rule between them."
formal:
  kind: convention
  ref: "none for the picture; semantics: SEI layered style ('allowed-to-use', CMU/SEI-2000-SR-004), Evans' Layered Architecture pattern, Clean Architecture Dependency Rule"
neighbours: [C3, C4, C5, C7, G1, I2]
status: draft
---

# Layered Architecture Diagram (分层架构图)

> The layers (or rings) of one application's code and the rule that says which layer may depend on which.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
<!-- skill-text
- **Question:** how is this application's code divided into responsibility layers, and which dependencies are allowed? It states a rule ("allowed-to-use"), not just a grouping; exceptions (skipping a layer, upward use) must be shown.
- **Viewpoint:** a module "uses" view inside one container, at about component level; concerns are modifiability, testability, separation of concerns.
- **Definition used here:** *layer* = logical partition of code responsibility (this type); *tier* = deployment location (G1); *ArchiMate layered viewpoint* = enterprise business/application/technology overview (I2). A capability stack with no dependency rule is C5.
- **Leaves out:** servers and networks (G1), call sequences (E1), data model (D1), integration between systems (C6), individual classes.
-->

A layered architecture diagram answers: *how is this application's code divided into responsibility layers, and which dependencies are allowed?* It states a **rule**, not just a grouping; without a stated rule it degenerates into a coloured stack of boxes. The SEI defines the relation between layers as **"allowed-to-use"**. Exceptions such as bridging (skipping a layer) or upward use must be shown, and many of them signal a poorly structured system [1]. In ISO/IEC/IEEE 42010 terms it belongs to a module "uses" viewpoint, with concerns of modifiability, testability and separation of concerns [14]. In C4 model terms it sits *inside one container*, at roughly the component level [12].

**Definition used here.** The word "layer" has three meanings. Only the first is this type.

| Term | Meaning | Where it belongs |
|---|---|---|
| **Layer** | Logical partition of *code responsibility*; all layers may run in one process [2][9] | **C8** (this type) |
| **Tier** | Physical or virtual deployment location; tiers run on separate machines [10] | G1 Deployment |
| **ArchiMate Layered viewpoint** | Enterprise overview of business / application / technology layers [13] | I2 ArchiMate layered view |

Two further look-alikes: a "capability stack" (bands of functional blocks with no dependency rule) is a C5 logical view, and an OSI-style protocol stack belongs with network diagrams.

**Deliberately left out:** servers, replicas and networks (G1); call sequences (E1); data model (D1); integration between systems (C6); individual classes.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->

- **Audience:** developers, tech leads, reviewers, architects recording design intent, and new joiners.
- **Classic scenarios:** (1) agree the internal structure and dependency rule of a new service; (2) onboarding and review: where does this code belong and what may it import?; (3) generate architecture-conformance tests from the picture [7][8]; (4) refactor a tangled codebase by drawing intended layers beside the actual import graph; (5) explain a framework's reference stack to implementers [11].
- **When not to use:** servers, replicas, availability or security zones (G1); who talks to whom across systems (C2/C6); a module list with no dependency discipline (C5); a tiny service with one or two layers; the top-level split of a large system, where domain modules should come first, each layered inside [2].
- **vs neighbours:**
  - Choose **C5 Logical architecture** for technology-neutral responsibility blocks and interfaces with no mandatory dependency rule.
  - Choose **C3/C4** for runnable units or components. One container may contain all the layers.
  - Choose **C7 Bounded context map** for boundaries *between* models. C8 lives inside one context.
  - Choose **G1 Deployment** for tiers and machines. Choose **I2** for ArchiMate's business/application/technology layering.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->

- **No graphical standard.** UML packages with dependency arrows can express the rule. The semantics come from the SEI, Evans and Martin [1][3][6].
- **Required:** layers as bands (or rings), each with a **name and a one-line responsibility**. State the **dependency rule** once in a sentence and name the **variant**. Draw arrows only for *allowed* dependencies. Add a legend: solid = source-code dependency, dashed = runtime wiring only (dependency injection) [9].
- **Variant selector** (pick exactly one):
  - **Strict (closed):** a layer uses only the layer directly below. Arrows connect only adjacent bands; pass-through layers are the cost [10].
  - **Relaxed (open):** a layer may use any lower layer, so arrows may skip bands. The cost is more coupling [10].
  - **Inward-dependency (hexagonal / onion / clean):** source dependencies point *toward the core*. Adapters depend on ports the core owns [4][5][6]. Draw the core in the centre with driving adapters on the left and driven adapters on the right; the hexagon shape is arbitrary [4] and the four clean-architecture rings are only an example [6].
  - *Segmented layers* (side-by-side peers inside one band, per the SEI [1]) can be combined with either stack variant.
- **Arrow-direction caution:** in the inward variant an arrow goes from "Persistence adapter" to "Domain", even though runtime calls flow the other way. Say "arrows = source-code dependency" in the legend.
- **Optional:** a vertical bar for cross-cutting concerns (logging, security, configuration); 1–5 real module names per layer as chips; up to three forbidden shortcuts as red dashed arrows marked "×"; external systems outside the frame.
- **Level of detail:** 3–5 layers, 2–5 elements each. More than about 6 layers suggests pass-through layers [10].
- **Naming:** by responsibility ("Domain", "Application", "Adapters"), not by framework. Use the same names as the repository packages so the rule can be tested.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->

### Best practices

1. Write the rule next to the picture, then make it executable, e.g. ArchUnit `layeredArchitecture()` / `onionArchitecture()` or import-linter layer contracts [7][8].
2. Keep the domain free of UI, infrastructure and framework references. Isolating the domain is the point of layering [3][5].
3. Pass simple data across boundaries, not framework rows or ORM entities; use dependency inversion where control flows outward [6][9].
4. In a larger system, split by domain or component first and layer *inside* each part [2].
5. Draw the intended layers and the actual import graph side by side, and list the main violations [1].

### Anti-patterns

1. **Layers drawn as tiers:** servers and replicas in the layer picture, or deployment called "three-tier layering" [2][10].
2. **Arrows without a stated rule, or a rule everyone breaks:** many pass-through layers, or strict layering that forces proxy methods [1][10].
3. **Reverse dependencies:** the data layer importing UI types, or the domain depending on persistence annotations [6].
4. **Package-by-layer as the top-level structure** of a large system [2].
5. **A capability stack presented as if it constrained the code**, or the clean-architecture rings treated as a mandatory four-ring template [6].

## Exemplars {#exemplars}
<!-- skill: omit -->

- [Fowler, PresentationDomainDataLayering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) — a minimal three-layer explanation, with layers that are not tiers and the warning about top-level use (licence not checked).
- [Microsoft .NET, Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures) — traditional N-layer next to clean architecture; solid arrows for compile-time and dashed for runtime dependencies (Microsoft Learn terms).
- [Android, Guide to app architecture](https://developer.android.com/topic/architecture) — UI / optional domain / data layers with arrows defined as class dependencies (Android content licence; not checked here).
- [Cockburn, Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — the primary source on why and when to leave the stack metaphor (licence not checked).
- [R. C. Martin, The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) — concentric rings and the Dependency Rule (licence not checked).
- [ArchUnit user guide](https://www.archunit.org/userguide/html/000_Index.html) — layer and onion rules as code: the diagram as a test (Apache-2.0 project).

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->

1. Fix the scope to ONE application or service (e.g. the shop backend). For a whole estate, offer C2/C3/C7 first.
2. List top-level packages and the import graph between them. Propose layers from the *actual* names; do not impose a template.
3. Choose the variant: if infrastructure implements interfaces owned by the domain, use inward-dependency; otherwise use a stack and choose strict or relaxed.
4. Each layer: name + a responsibility of 5–10 words + 2–5 real module chips (≤ ~25 chips in total).
5. Stack layout: vertical, entry (web/API) on top, persistence and external clients at the bottom. Inward layout: core centred, driving adapters left, driven adapters right. Use equal band heights and put externals outside the frame.
6. Arrows: one per allowed dependency, from user to used (or toward the core). At most three forbidden shortcuts, red dashed with "×".
7. Show cross-cutting concerns once, as a sidebar, not as arrows from everything.
8. Caption: the rule in one sentence + the variant name + the arrow legend. Colour: one neutral tint per layer family, domain accented, red only for violations; no technology logos.

**Self-check**
- [ ] One application or service only; no servers, replicas or subnets.
- [ ] Variant named; dependency rule stated; arrow meaning in the legend.
- [ ] Every layer has a responsibility and at least one real module name.
- [ ] Arrows match the actual import graph, or are marked "intended".
- [ ] No pass-through layer; 3–5 layers.
- [ ] "Tier" appears only for physical deployment; not confused with the ArchiMate layered viewpoint.
- [ ] Names equal repository package names, so a conformance rule can be generated.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->

- Build structure: Maven/Gradle modules and their dependencies, `.csproj` ProjectReferences, Go imports, `package.json` workspaces, Python top-level packages, Rust workspace crates.
- Package tree names (`controller/service/repository`, `domain/application/infrastructure`, `adapters/in|out`, `ports`).
- Existing conformance rules (ArchUnit tests, `.importlinter`) [7][8]. The dependency-injection composition root shows where inward dependencies are wired at runtime.
- ADRs and README architecture sections.
- Anti-evidence: `docker-compose` and Kubernetes files describe tiers and deployables (C3/G1), not layers.
- Ask people: the *intended* rule, accepted exceptions, and whether intended or actual structure should be drawn.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->

1. Which application or service is this for, and who reads it? (Default: one backend service; developers and reviewers.)
2. Intended design, actual structure from the code, or both side by side? (Default: both, with violations listed.)
3. Which rule applies: adjacent layers only, any lower layer, or everything depends inward on the domain? (Default: derived from the code; strict stack if unclear.)
4. Which layer and package names are already used, and which cross-cutting concerns must appear? (Default: repository names; auth, logging, config.)
5. Shall I also emit a conformance rule file (ArchUnit or import-linter) from the diagram? (Default: offer it as a next step.)

## Template {#template}
<!-- skill: keep (≤3 lines) -->

Model template: `assets/templates/C8.json` · Layout template: `layered` · each `groups[]` entry of kind `layer` becomes a band with `component` nodes as module chips; `edges` of kind `dependency` show allowed (solid) or runtime (`dashed`) dependencies; `meta.description` holds the variant and the rule sentence.

## Sources {#sources}
<!-- skill: omit -->

1. SEI, "Documenting Architectural Layers", CMU/SEI-2000-SR-004 (mirror) — https://pdfs.semanticscholar.org/a9b3/df89f07b4da137de51ed22b84d58c280f910.pdf — accessed 2026-10-14
2. Fowler, "PresentationDomainDataLayering" (2015) — https://martinfowler.com/bliki/PresentationDomainDataLayering.html — accessed 2026-10-14
3. Evans, DDD Reference (2015), "Layered Architecture" — https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf — accessed 2026-10-14
4. Cockburn, "Hexagonal Architecture" (2005) — https://alistair.cockburn.us/hexagonal-architecture/ — accessed 2026-10-14
5. Palermo, "The Onion Architecture: part 1" (2008) — https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/ — accessed 2026-10-14
6. R. C. Martin, "The Clean Architecture" (2012) — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — accessed 2026-10-14
7. ArchUnit user guide — https://www.archunit.org/userguide/html/000_Index.html — accessed 2026-10-14
8. Import Linter documentation — https://import-linter.readthedocs.io/en/stable/ — accessed 2026-10-14
9. Microsoft Learn, "Common web application architectures" — https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures — accessed 2026-10-14
10. Microsoft Learn, "N-tier architecture style" — https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier — accessed 2026-10-14
11. Android Developers, "Guide to app architecture" — https://developer.android.com/topic/architecture — accessed 2026-10-14
12. C4 model, Component diagram — https://c4model.com/diagrams/component — accessed 2026-10-14
13. Visual Paradigm, "Full ArchiMate Viewpoints Guide" (Layered viewpoint; secondary) — https://www.visual-paradigm.com/guide/archimate/full-archimate-viewpoints-guide — accessed 2026-10-14 (not verified against the ArchiMate 3.2 specification text)
14. ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/ieee-1471/cm — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->

![C8 sample: layers of an online-shop backend — web/API adapter (storefront, checkout endpoints), application (place order, update cart), domain (cart, order, pricing), infrastructure (persistence, payment-provider client, warehouse client), strict-stack rule stated in the caption](/samples/C8-layered-architecture.svg)
*Sample pending (generated by the renderer from `examples/`).*
