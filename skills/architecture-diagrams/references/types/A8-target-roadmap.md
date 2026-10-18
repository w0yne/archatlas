# Target Architecture & Transition Roadmap (目标架构与演进路线图)
<!-- Generated from content/en/types/A8-target-roadmap.md by tools/build_skill_refs.py. Do not edit. -->
> Where are we, where are we going, which stable intermediate states lie between, and which bodies of work move us from one state to the next, in what order and why?
Scope: One solution or domain from baseline to target over a stated horizon: the states, the work packages between them, their dependencies and the value each state delivers. Neighbours: A1, A7, C1.

## Meaning
A roadmap answers "where are we, where are we going, what are the stable steps in between, and which work moves us along?" In ISO/IEC/IEEE 42010 terms it is an evolution / migration viewpoint concerned with sequence, dependencies, value and risk per step, and the viability of each interim state. In TOGAF, Phases B–D develop baseline and target architectures and their gap analysis, Phase E consolidates gaps into work packages and identifies **Transition Architectures**, and Phase F finalises the **Architecture Roadmap**. In ArchiMate it is the Migration or Implementation and Migration viewpoint. Each transition state is a decision point: a coherent architecture where stakeholders could stop and still keep the value. It leaves out detailed design, task-level schedules and rationale prose.

**Definition used here:** the **Architecture Roadmap** shows work packages and transition architectures on a timeline and "highlights individual work packages' business value at each stage". The **Implementation and Migration Plan** is a different TOGAF deliverable: the schedule, with timing, cost, resources and milestones. A Gantt chart of tasks is that plan, not this diagram. TOGAF asks for "one or more" transition architectures, not a fixed number.

## When to use and how to choose
- **Audience:** executives and sponsors, architecture boards, portfolio and programme managers, funding committees, delivery leads checking where their project fits.
- **Scenarios:** an online shop moving from a monolith to modular services with old and new running side by side (strangler fig); consolidating two order systems with alternative transition paths; capability-based investment planning; an annual roadmap refresh; cloud migration in waves, each ending in a stable hybrid state.
- **When not to use:** only one release with no meaningful interim state (draw A7 labelled "target"); the audience needs task dates and staffing (use a project plan); the target is still undecided (settle it with A7 options first).
- **vs neighbours:**
  - Choose **A7 conceptual architecture** for the picture of *one* state; A8 puts two or more of them, or their deltas, on a time axis.
  - Choose **A1 capability map** (heat-mapped) as the input to capability-based planning; A8 shows the increments over time.
  - Choose **C1 landscape** for the estate at one point in time; baseline and target C1 views can be part of an A8.
  - A **Wardley map** informs what the target should be; it does not show transition states.
  - A **product roadmap** is feature- or outcome-oriented and owned by product; borrow its outcome framing for step labels.

## Notation and elements
- **Required:** baseline and target as compact pictures or block lists in the same shapes and layering as A7 / C1; 1–N transition states, each named by its outcome ("Checkout runs as its own service", not "Phase 2") with a horizon and its key changes; work packages between states, with dependency arrows; the gaps each step closes.
- **Legend (required):** new / changed / retained / retired, matching TOGAF's new / retain / transition / replace markings; line meanings; committed vs indicative.
- **Optional:** swimlanes per domain or capability; milestones and implementation events; business value or KPI per state; temporary (transitional) components, explicitly marked; alternative paths while a decision is open; risk flags.
- **Tabular companions**: gap analysis matrix (baseline × target building blocks, with "New" and "Eliminated"); consolidated gaps, solutions and dependencies matrix; Transition Architecture State Evolution table (services × transitions, cells marked new / retain / transition / replace).
- **ArchiMate 3.2 elements**: Plateau ("a relatively stable state of the architecture that exists during a limited period of time"), Gap, Work Package, Deliverable, Implementation Event. Plateaus are commonly chained by triggering, a gap is associated with the two plateaus it compares, and work packages realise deliverables; this is the common tool reading, **not verified against the current spec text**.
- **ArchiMate version note:** ArchiMate 4 was announced on 27 April 2026. A vendor summary reports that Gap is deprecated (modelled as an Assessment of the difference between two Plateaus) and that layers become domains; the announcement does not list these details, so they are **not verified against the current spec text**. This page follows ArchiMate 3.2; say which version a formal diagram uses.
- **Time axis:** honest spacing in quarters or years; items beyond the commitment horizon marked indicative. Work packages are named bodies of work, not tasks.

## Best practices and anti-patterns
### Best practices

1. Every intermediate state stands on its own: operable, valuable, and a possible stopping point.
2. Label steps with outcomes, not "Phase n" or feature lists.
3. Make dependencies explicit; the order of work depends on which transition path is chosen.
4. Plan for transitional architecture and show it; hidden interim integrations make the roadmap look cheaper than it is.
5. Reuse the A7 / C1 shapes, layering and colour for every state so the changes are visible; label baseline, each transition and target explicitly.

### Anti-patterns

1. Target only, no path; or a big-bang leap from baseline to target.
2. Non-viable interim states: a step that cannot run on its own or delivers nothing until a later step.
3. A feature / date list, or a Gantt chart of projects, posing as an architecture roadmap.
4. A different notation per state, so nobody can see what changed.
5. False precision far out on the time axis, or working notes ("TBD", "pending vendor") and internal version labels on the figure.

## Drawing recipe
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

## Evidence in a code repository
- **Baseline:** deployable units, data stores and integrations from IaC, Helm or compose files; dependency manifests; `@deprecated` markers and deprecated modules.
- **Interim states and direction:** feature flags running old and new paths in parallel; migration scripts; strangler routing rules in gateways or proxies; ADRs ("we will replace X"); epics, milestones, release branches and tags.
- **Ask people:** the target state itself, the business value of each step, priorities and funding, the commitment horizon, and dependencies on organisational change.

## Guided-mode questions
1. What is the target horizon and scope, and is the target agreed or still an option set? (agreed target, 2–3 year horizon)
2. How many intermediate states matter, and what makes each worth stopping at? (2 transitions, each with one value tag)
3. Who reads it: executives, portfolio managers, or both? (state strip for executives)
4. Which hard constraints fix the order: contracts, regulatory dates, end of vendor support? (none assumed; dependencies only)
5. Formal ArchiMate (plateau, work package; 3.2 or 4) or a simplified convention with a legend? (simplified convention, ArchiMate 3.2 terms)

## Template
Model template: `assets/templates/A8.json` · Layout template: `tree` · states are `state` nodes in one left-to-right chain (baseline → target), work packages are `task` nodes between adjacent states linked by `dependency` edges; node `style` (`planned`, `shared`, `external`) marks the block state.

## Sample
Figure: `samples/ai-service-assistant/A8/en/diagram.svg` (published with the site)
