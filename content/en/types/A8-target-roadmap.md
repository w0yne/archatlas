---
code: A8
slug: target-roadmap
family: A
names:
  en: Target architecture and transition roadmap
  zh: 目标架构与演进路线图
  aliases:
    en: [architecture roadmap, transition architecture, migration roadmap, as-is to-be roadmap, plateau diagram, baseline / target / transition architecture, as-is / to-be roadmap, migration view, capability roadmap]
    zh: [演进路线图, 架构路线图, 迁移路线图, 过渡架构, 现状 / 目标 / 过渡架构, 迁移视图, 平台期图, 能力路线图, 稳定态图]
question: Where are we, where are we going, which stable intermediate states lie between, and which bodies of work move us from one state to the next, in what order and why?
audiences: [leaders, architects]
levels: [strategy]
phases: [initiate, design]
scope: 'One solution or domain from baseline to target over a stated horizon: the states, the work packages between them, their dependencies and the value each state delivers.'
formal: {kind: standard, ref: 'TOGAF ADM Architecture Roadmap and Transition Architectures (Phases E–F, TOGAF 9.1 text); ArchiMate 3.2 Implementation & Migration elements'}
neighbours: [A1, A7, C1]
status: draft
---

# Target Architecture & Transition Roadmap (目标架构与演进路线图)

> Baseline, one or more viable transition states and the target, drawn in one visual grammar, with the work packages that move the architecture from each state to the next.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A roadmap answers "where are we, where are we going, what are the stable steps in between, and which work moves us along?" In ISO/IEC/IEEE 42010 terms it is an evolution / migration viewpoint concerned with sequence, dependencies, value and risk per step, and the viability of each interim state. In TOGAF, Phases B–D develop baseline and target architectures and their gap analysis, Phase E consolidates gaps into work packages and identifies **Transition Architectures**, and Phase F finalises the **Architecture Roadmap** [1][2]. In ArchiMate it is the Migration or Implementation and Migration viewpoint [4]. Each transition state is a decision point: a coherent architecture where stakeholders could stop and still keep the value [1][9]. It leaves out detailed design, task-level schedules and rationale prose.

**Definition used here:** the **Architecture Roadmap** shows work packages and transition architectures on a timeline and "highlights individual work packages' business value at each stage" [1]. The **Implementation and Migration Plan** is a different TOGAF deliverable: the schedule, with timing, cost, resources and milestones [1][2]. A Gantt chart of tasks is that plan, not this diagram. TOGAF asks for "one or more" transition architectures, not a fixed number [1].

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** executives and sponsors, architecture boards, portfolio and programme managers, funding committees, delivery leads checking where their project fits.
- **Scenarios:** an online shop moving from a monolith to modular services with old and new running side by side (strangler fig) [11][14]; consolidating two order systems with alternative transition paths [5]; capability-based investment planning [1][10]; an annual roadmap refresh; cloud migration in waves, each ending in a stable hybrid state.
- **When not to use:** only one release with no meaningful interim state (draw A7 labelled "target"); the audience needs task dates and staffing (use a project plan); the target is still undecided (settle it with A7 options first).
- **vs neighbours:**
  - Choose **A7 conceptual architecture** for the picture of *one* state; A8 puts two or more of them, or their deltas, on a time axis.
  - Choose **A1 capability map** (heat-mapped) as the input to capability-based planning; A8 shows the increments over time.
  - Choose **C1 landscape** for the estate at one point in time; baseline and target C1 views can be part of an A8.
  - A **Wardley map** informs what the target should be; it does not show transition states [12].
  - A **product roadmap** is feature- or outcome-oriented and owned by product; borrow its outcome framing for step labels [13].

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required:** baseline and target as compact pictures or block lists in the same shapes and layering as A7 / C1; 1–N transition states, each named by its outcome ("Checkout runs as its own service", not "Phase 2") with a horizon and its key changes; work packages between states, with dependency arrows; the gaps each step closes [1][3].
- **Legend (required):** new / changed / retained / retired, matching TOGAF's new / retain / transition / replace markings [8]; line meanings; committed vs indicative.
- **Optional:** swimlanes per domain or capability; milestones and implementation events; business value or KPI per state; temporary (transitional) components, explicitly marked [14]; alternative paths while a decision is open [5]; risk flags.
- **Tabular companions** [8]: gap analysis matrix (baseline × target building blocks, with "New" and "Eliminated"); consolidated gaps, solutions and dependencies matrix; Transition Architecture State Evolution table (services × transitions, cells marked new / retain / transition / replace).
- **ArchiMate 3.2 elements** [3]: Plateau ("a relatively stable state of the architecture that exists during a limited period of time"), Gap, Work Package, Deliverable, Implementation Event. Plateaus are commonly chained by triggering, a gap is associated with the two plateaus it compares, and work packages realise deliverables; this is the common tool reading, **not verified against the current spec text**.
- **ArchiMate version note:** ArchiMate 4 was announced on 27 April 2026 [6]. A vendor summary reports that Gap is deprecated (modelled as an Assessment of the difference between two Plateaus) and that layers become domains [7]; the announcement does not list these details, so they are **not verified against the current spec text**. This page follows ArchiMate 3.2; say which version a formal diagram uses.
- **Time axis:** honest spacing in quarters or years; items beyond the commitment horizon marked indicative. Work packages are named bodies of work, not tasks.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices

1. Every intermediate state stands on its own: operable, valuable, and a possible stopping point [1][9][10].
2. Label steps with outcomes, not "Phase n" or feature lists [13].
3. Make dependencies explicit; the order of work depends on which transition path is chosen [5][8].
4. Plan for transitional architecture and show it; hidden interim integrations make the roadmap look cheaper than it is [11][14].
5. Reuse the A7 / C1 shapes, layering and colour for every state so the changes are visible; label baseline, each transition and target explicitly [5].

### Anti-patterns

1. Target only, no path; or a big-bang leap from baseline to target [11].
2. Non-viable interim states: a step that cannot run on its own or delivers nothing until a later step [1].
3. A feature / date list, or a Gantt chart of projects, posing as an architecture roadmap [1][13].
4. A different notation per state, so nobody can see what changed [5].
5. False precision far out on the time axis, or working notes ("TBD", "pending vendor") and internal version labels on the figure.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [The Open Group, TOGAF 9 and ArchiMate 1.0 white paper](https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf) — Fig. 22 shows baseline, target and two alternative transition plateaus drawn with identical shapes; Open Group copyright [5].
- [TOGAF 9.1 Migration Planning Techniques (secondary mirror)](https://coe.qualiware.com/resources/togaf/9-1/part3-admguide/migration-planning-techniques) — the State Evolution table and gap analysis forms with new / retain / transition / replace markings [8].
- [Martin Fowler, Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html) — incremental replacement in which "investment and returns occur gradually and visibly" [11].
- [Cartwright, Horn & Lewis, Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html) — interim states with temporary components that are thrown away later [14].
- [Linked.Archi, ArchiMate 3.2 Example Viewpoints](https://meta.linked.archi/archimate3/viewpoints) — element sets for the Migration and Implementation and Migration viewpoints; a checklist for a formal plateau diagram [4].

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Confirm the states: baseline date and scope, target horizon, and how many transitions the audience cares about (often 2–4; TOGAF only requires one or more).
2. Draw or reuse the A7 / C1 view for baseline and target with the same blocks and layering; list the gaps (new / changed / retained / retired).
3. Group gaps into work packages and note their dependencies.
4. Cut transition states where a coherent, valuable architecture exists; name each by its outcome, with 2–4 key changes and any temporary components.
5. Layout (a) **state strip** for executives: thumbnails left to right, Baseline → T1 → T2 → Target, work packages under each arrow. Layout (b) **swimlane roadmap** for portfolio managers: rows per domain, time on x, work packages as bars, plateaus as milestone lines.
6. Text: plateau titles ≤6 words; work packages 2–5 word noun phrases; at most one value tag per state; no paragraphs.
7. Colour: one encoding, the state of each block: new (accent), changed (lighter accent), retained (neutral), retiring (hatched grey), temporary (dashed border); a dashed "indicative" zone beyond the commitment horizon; pair colour with pattern.
8. Legend bottom right; title with scope and horizon, e.g. "Online shop: 2026–2028 transition roadmap". Offer the gap matrix or State Evolution table as an appendix, not inside the figure.

**Self-check**
- [ ] Baseline, every transition and the target are labelled; the target is not the only state.
- [ ] Each transition is operable and names the value it delivers.
- [ ] All states share one set of shapes, layering and colour key.
- [ ] Every gap is closed by a work package, and every work package closes a gap.
- [ ] Dependencies are drawn and the order respects them.
- [ ] Temporary components are visible and marked.
- [ ] Items beyond the commitment horizon are marked indicative.
- [ ] No tasks, person-days or design internals; no working notes or version labels on the figure.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Baseline:** deployable units, data stores and integrations from IaC, Helm or compose files; dependency manifests; `@deprecated` markers and deprecated modules.
- **Interim states and direction:** feature flags running old and new paths in parallel; migration scripts; strangler routing rules in gateways or proxies; ADRs ("we will replace X"); epics, milestones, release branches and tags.
- **Ask people:** the target state itself, the business value of each step, priorities and funding, the commitment horizon, and dependencies on organisational change.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. What is the target horizon and scope, and is the target agreed or still an option set? (agreed target, 2–3 year horizon)
2. How many intermediate states matter, and what makes each worth stopping at? (2 transitions, each with one value tag)
3. Who reads it: executives, portfolio managers, or both? (state strip for executives)
4. Which hard constraints fix the order: contracts, regulatory dates, end of vendor support? (none assumed; dependencies only)
5. Formal ArchiMate (plateau, work package; 3.2 or 4) or a simplified convention with a legend? (simplified convention, ArchiMate 3.2 terms)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/A8.json` · Layout template: `tree` · states are `state` nodes in one left-to-right chain (baseline → target), work packages are `task` nodes between adjacent states linked by `dependency` edges; node `style` (`planned`, `shared`, `external`) marks the block state.

## Sources {#sources}
<!-- skill: omit -->
1. The Open Group, TOGAF Version 9.1 (2011): Ch. 13 Phase E, Ch. 14 Phase F, §3.74 Transition Architecture, §36.2.7 Architecture Roadmap, Ch. 32 Capability-Based Planning (evaluation copy, third-party hosted) — http://www.crvs-dgb.org/wp-content/uploads/2015/07/I112.pdf — accessed 2026-10-14
2. The Open Group, World-Class Enterprise Architecture: Framework Guidance and TOGAF 9 Example (2010) — https://pubs.opengroup.org/onlinepubs/7698999699/toc.pdf — accessed 2026-10-14
3. The Open Group, ArchiMate 3.2 Specification Reference Cards (N221, 2022) — https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf — accessed 2026-10-14
4. Linked.Archi, ArchiMate 3.2 Example Viewpoints — https://meta.linked.archi/archimate3/viewpoints — accessed 2026-10-14
5. H. Jonkers, E. Proper, M. Turner, TOGAF 9 and ArchiMate 1.0 (Open Group white paper, 2009) — https://pubs.opengroup.org/onlinepubs/7698909899/toc.pdf — accessed 2026-10-14
6. The Open Group, The Open Group Announces ArchiMate 4 Specification (press release, 27 April 2026) — https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification — accessed 2026-10-14
7. Bizzdesign (M. Lankhorst), ArchiMate 4 Specification: What Changed from Version 3.2? — https://bizzdesign.com/blog/archimate-4-changes — accessed 2026-10-14
8. TOGAF 9.1 Part III Ch. 27 Gap Analysis and Ch. 28 Migration Planning Techniques (secondary HTML mirror) — https://coe.qualiware.com/resources/togaf/9-1/part3-admguide/migration-planning-techniques — accessed 2026-10-14
9. Conexiam, TOGAF ADM Phase E – Build the Architecture Roadmap — https://conexiam.com/togaf-adm-phase-e-build-the-architecture-roadmap — accessed 2026-10-14
10. Conexiam, Unlocking the Power of Capability-Based Planning: A Quick Guide — https://conexiam.com/unlocking-the-power-of-capability-based-planning-a-quick-guide — accessed 2026-10-14
11. Martin Fowler, Strangler Fig Application — https://martinfowler.com/bliki/StranglerFigApplication.html — accessed 2026-10-14
12. Learn Wardley Mapping, Introduction — https://learnwardleymapping.com/introduction/ — accessed 2026-10-14
13. Marty Cagan (SVPG), The Alternative to Roadmaps (2015) — https://www.svpg.com/the-alternative-to-roadmaps/ — accessed 2026-10-14
14. I. Cartwright, R. Horn, J. Lewis, Transitional Architecture, Patterns of Legacy Displacement (2022) — https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![A8 · Enterprise Service Assistant](/samples/ai-service-assistant/A8/en/diagram.svg)
*Read-only answers, approved writes and evaluation-gated changes are illustrative transition plateaus, not committed dates. Each work package introduces only the capabilities required for its next plateau.*

[SVG](/samples/ai-service-assistant/A8/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A8/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

[Historical shop regression sample](/samples/A8-target-roadmap.svg) · [All 29 views](/use/ai-service-assistant) · [Illustrative assumptions](/use/ai-service-assistant-assumptions).
