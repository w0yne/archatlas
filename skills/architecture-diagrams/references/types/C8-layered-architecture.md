# Layered Architecture Diagram (分层架构图)
<!-- Generated from content/en/types/C8-layered-architecture.md by tools/build_skill_refs.py. Do not edit. -->
> Into which responsibility layers is one application's code divided, and which dependency directions are allowed and which forbidden?
Scope: One application, service or bounded context: its code layers (or rings) and the dependency rule between them. Neighbours: C4, C5, C7, G1, I2.

## Meaning
- **Question:** how is this application's code divided into responsibility layers, and which dependencies are allowed? It states a rule ("allowed-to-use"), not just a grouping; exceptions (skipping a layer, upward use) must be shown.
- **Viewpoint:** a module "uses" view inside one container, at about component level; concerns are modifiability, testability, separation of concerns.
- **Definition used here:** *layer* = logical partition of code responsibility (this type); *tier* = deployment location (G1); *ArchiMate layered viewpoint* = enterprise business/application/technology overview (I2). A capability stack with no dependency rule is C5.
- **Leaves out:** servers and networks (G1), call sequences (E1), data model (D1), integration between systems (C6), individual classes.

## When to use and how to choose
- **Audience:** developers, tech leads, reviewers, architects recording design intent, and new joiners.
- **Classic scenarios:** (1) agree the internal structure and dependency rule of a new service; (2) onboarding and review: where does this code belong and what may it import?; (3) generate architecture-conformance tests from the picture; (4) refactor a tangled codebase by drawing intended layers beside the actual import graph; (5) explain a framework's reference stack to implementers.
- **When not to use:** servers, replicas, availability or security zones (G1); who talks to whom across systems (C2/C6); a module list with no dependency discipline (C5); a tiny service with one or two layers; the top-level split of a large system, where domain modules should come first, each layered inside.
- **vs neighbours:**
  - Choose **C5 Logical architecture** for technology-neutral responsibility blocks and interfaces with no mandatory dependency rule.
  - Choose **C3/C4** for runnable units or components. One container may contain all the layers.
  - Choose **C7 Bounded context map** for boundaries *between* models. C8 lives inside one context.
  - Choose **G1 Deployment** for tiers and machines. Choose **I2** for ArchiMate's business/application/technology layering.

## Notation and elements
- **No graphical standard.** UML packages with dependency arrows can express the rule. The semantics come from the SEI, Evans and Martin.
- **Required:** layers as bands (or rings), each with a **name and a one-line responsibility**. State the **dependency rule** once in a sentence and name the **variant**. Draw arrows only for *allowed* dependencies. Add a legend: solid = source-code dependency, dashed = runtime wiring only (dependency injection).
- **Variant selector** (pick exactly one):
  - **Strict (closed):** a layer uses only the layer directly below. Arrows connect only adjacent bands; pass-through layers are the cost.
  - **Relaxed (open):** a layer may use any lower layer, so arrows may skip bands. The cost is more coupling.
  - **Inward-dependency (hexagonal / onion / clean):** source dependencies point *toward the core*. Adapters depend on ports the core owns. Draw the core in the centre with driving adapters on the left and driven adapters on the right; the hexagon shape is arbitrary and the four clean-architecture rings are only an example.
  - *Segmented layers* (side-by-side peers inside one band, per the SEI) can be combined with either stack variant.
- **Arrow-direction caution:** in the inward variant an arrow goes from "Persistence adapter" to "Domain", even though runtime calls flow the other way. Say "arrows = source-code dependency" in the legend.
- **Optional:** a vertical bar for cross-cutting concerns (logging, security, configuration); 1–5 real module names per layer as chips; up to three forbidden shortcuts as red dashed arrows marked "×"; external systems outside the frame.
- **Level of detail:** 3–5 layers, 2–5 elements each. More than about 6 layers suggests pass-through layers.
- **Naming:** by responsibility ("Domain", "Application", "Adapters"), not by framework. Use the same names as the repository packages so the rule can be tested.

## Best practices and anti-patterns
### Best practices

1. Write the rule next to the picture, then make it executable, e.g. ArchUnit `layeredArchitecture()` / `onionArchitecture()` or import-linter layer contracts.
2. Keep the domain free of UI, infrastructure and framework references. Isolating the domain is the point of layering.
3. Pass simple data across boundaries, not framework rows or ORM entities; use dependency inversion where control flows outward.
4. In a larger system, split by domain or component first and layer *inside* each part.
5. Draw the intended layers and the actual import graph side by side, and list the main violations.

### Anti-patterns

1. **Layers drawn as tiers:** servers and replicas in the layer picture, or deployment called "three-tier layering".
2. **Arrows without a stated rule, or a rule everyone breaks:** many pass-through layers, or strict layering that forces proxy methods.
3. **Reverse dependencies:** the data layer importing UI types, or the domain depending on persistence annotations.
4. **Package-by-layer as the top-level structure** of a large system.
5. **A capability stack presented as if it constrained the code**, or the clean-architecture rings treated as a mandatory four-ring template.

## Drawing recipe
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

## Evidence in a code repository
- Build structure: Maven/Gradle modules and their dependencies, `.csproj` ProjectReferences, Go imports, `package.json` workspaces, Python top-level packages, Rust workspace crates.
- Package tree names (`controller/service/repository`, `domain/application/infrastructure`, `adapters/in|out`, `ports`).
- Existing conformance rules (ArchUnit tests, `.importlinter`). The dependency-injection composition root shows where inward dependencies are wired at runtime.
- ADRs and README architecture sections.
- Anti-evidence: `docker-compose` and Kubernetes files describe tiers and deployables (C3/G1), not layers.
- Ask people: the *intended* rule, accepted exceptions, and whether intended or actual structure should be drawn.

## Guided-mode questions
1. Which application or service is this for, and who reads it? (Default: one backend service; developers and reviewers.)
2. Intended design, actual structure from the code, or both side by side? (Default: both, with violations listed.)
3. Which rule applies: adjacent layers only, any lower layer, or everything depends inward on the domain? (Default: derived from the code; strict stack if unclear.)
4. Which layer and package names are already used, and which cross-cutting concerns must appear? (Default: repository names; auth, logging, config.)
5. Shall I also emit a conformance rule file (ArchUnit or import-linter) from the diagram? (Default: offer it as a next step.)

## Template
Model template: `assets/templates/C8.json` · Layout template: `layered` · each `groups[]` entry of kind `layer` becomes a band with `component` nodes as module chips; `edges` of kind `dependency` show allowed (solid) or runtime (`dashed`) dependencies; `meta.description` holds the variant and the rule sentence.

## Sample
Figure: `samples/C8-layered-architecture.svg` (published with the site)
