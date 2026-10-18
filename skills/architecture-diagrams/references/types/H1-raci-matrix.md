# RACI matrix (RACI 责任矩阵)
<!-- Generated from content/en/types/H1-raci-matrix.md by tools/build_skill_refs.py. Do not edit. -->
> For each activity, who performs the work, owns the outcome, provides input, and receives updates?
Scope: Responsibilities for activities within one initiative or service. Neighbours: A4, D3, E4, F3, H2, H3.

## Meaning
A RACI matrix connects activities to execution, accountability, consultation, and communication. Reading across reveals unowned work; reading down reveals concentrated workload or approval authority. It supports a governance concern, not a fixed architecture level.

**Definition used here:** roles, teams, or named individuals may be participants. One A per row is the default convention, not a universal standard: UK Government Security explicitly permits shared accountability. Multiple R assignments and combined A/R are possible.

RACI has no universal notation version. A responsibility assignment matrix is the broader family; RASCI adds Support. DACI is a decision framework, not an alias. RACI omits workflow order, scheduling, reporting hierarchy, and enforced software permissions.

## When to use and how to choose
- **Audience:** delivery leads, service owners, contributors, and operators.
- **Scenarios:** preparing an online-shop release; handing checkout support to operations; assigning security-control work; tracking incident follow-up responsibilities.
- **When not:** a simple task list already establishes ownership, or the real question is timing, dependencies, or technical access.
- **H3 stakeholder map:** choose it for engagement priorities; RACI assigns responsibility per activity.
- **E4 swimlane:** choose it for sequence and handoffs; link its activities to matrix rows.
- **F3 access-control model:** choose it for permitted operations; review permission is not business accountability.
- **D3 data lineage and ownership map:** choose it for who owns and stewards a dataset; RACI assigns responsibility for activities.
- **DACI:** choose it to organise a particular decision; use RACI for the resulting delivery responsibilities.
- **A4 business scenario matrix:** choose it for which roles take part in which business activities; RACI assigns responsibility per activity, not coverage.
- **H2 observability view:** choose it for how incidents are detected and routed; RACI names who owns the response.

## Notation and elements
- **Required:** scoped activities as rows, identifiable participants as columns, cell assignments, and a legend. Use short verb–object activity names.
- **Codes:** R performs work; A answers for its outcome; C supplies input; I receives updates. Define whether A includes formal approval.
- **Policy:** normally one A and at least one R per execution row. Shared A needs explicit authority boundaries or a resolution rule; do not silently erase agreed governance.
- **Combined codes:** A/R may name the same participant. Distinguish “no involvement” from “unknown”; blanks must not represent both.
- **Optional:** phase groups, activity IDs, evidence references, effective date, and a role-to-person register. Label an added S as RASCI.
- **Arrows:** none in the matrix. Cells are assignments, not data flow or sequence. Consultation can involve two-way communication without drawn connectors.
- **Companion flow:** label escalation arrows with their trigger and meaning; keep them separate from the matrix.
- **Detail:** use comparable activity granularity and explain mixed participant levels. Letters carry meaning; colour is supplementary.

## Best practices and anti-patterns
| Best practice | Anti-pattern |
| --- | --- |
| Agree assignments with the affected participants. | Treating an automatically generated draft as granted authority. |
| State local A/R rules and explain shared authority. | Claiming one A or one R is universally mandatory. |
| Review row coverage and column workload. | Checking letters while ignoring bottlenecks. |
| Keep meaningful activities and necessary C/I assignments. | Filling every cell or listing every implementation microtask. |
| Revisit assignments when scope or staffing changes. | Copying a template's ownership into a different organisation. |

Asana's main instructions recommend one R, while its FAQ permits multiple R assignments. Use its practical guidance with that inconsistency in mind; it is not a normative cardinality rule.

## Drawing recipe
1. Set scope, audience, and current/proposed state; gather agreed activities and participants.
2. Choose roles or individuals; define codes, unknowns, combined codes, and the accountability policy.
3. Draft rows against evidence; leave uncertain ownership unresolved.
4. Review rows for gaps and columns for overload; split activities with conflicting outcomes.
5. Lay out activities vertically and participants horizontally; group phases and repeat headers when splitting.
6. Keep labels short, letters visible without colour, and the legend adjacent; record effective date and update ownership.

**Self-check**
- [ ] Scope and state are explicit.
- [ ] Every row has execution coverage or a visible gap.
- [ ] A assignments follow the declared policy.
- [ ] Shared A has a resolution rule.
- [ ] Unknown differs from no involvement.
- [ ] Columns and C/I assignments were reviewed.
- [ ] Participants confirmed ownership; evidence supports the claims.
- [ ] Headers, codes, and legend remain readable without colour.

## Evidence in a code repository
- Governance documents and approved decisions support documented responsibility assignments.
- Runbooks and release procedures identify activities, duties, and escalation routes.
- `CODEOWNERS` and approval configuration establish review rules, not organisational A.
- Commit frequency, administrator access, and issue assignment do not establish accountability.
- Record each claim's path, revision, and verified/inferred/doc-only/conflict status; confirm ownership gaps with people.

## Guided-mode questions
1. Which activities need clearer ownership, and is this current or proposed state?
2. Should participants be roles, teams, or named individuals?
3. What does A mean here, and is shared accountability permitted?
4. Which assignments are agreed, unresolved, or need a separate escalation flow?

## Template
Model template: `assets/templates/H1.json` · Layout template: `grid_table` · one `tables[]` entry with activity rows × participant columns and R/A/C/I in the cells (one A per row by default; a shared A needs a resolution note); the legend goes in the table `title`.

## Sample
Figure: `samples/ai-service-assistant/H1/en/diagram.svg` (published with the site)
