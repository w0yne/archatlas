---
code: H1
slug: raci-matrix
family: H
names:
  en: RACI matrix
  zh: RACI 责任矩阵
  aliases:
    en: [RACI chart, responsibility assignment matrix]
    zh: [RACI 职责分配矩阵, 责任分配矩阵]
question: "For each activity, who performs the work, owns the outcome, provides input, and receives updates?"
audiences: [leaders, business, operations]
level: concept
phases: [initiate, operate]
scope: "Responsibilities for activities within one initiative or service."
formal:
  kind: convention
  ref: "Responsibility-assignment practice; no versioned graphical standard. Atlassian, Understanding and using RACI charts: https://www.atlassian.com/work-management/project-management/raci-chart"
neighbours: [H3, E4, D3, F3]
status: draft
sourceRev: "2026-10-14"
---

# RACI matrix

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A RACI matrix connects activities to execution, accountability, consultation, and communication. Reading across reveals unowned work; reading down reveals concentrated workload or approval authority. It supports a governance concern, not a fixed architecture level.

**Definition used here:** roles, teams, or named individuals may be participants. One A per row is the default convention, not a universal standard: UK Government Security explicitly permits shared accountability [1][2]. Multiple R assignments and combined A/R are possible.

RACI has no universal notation version. A responsibility assignment matrix is the broader family; RASCI adds Support. DACI is a decision framework, not an alias [3]. RACI omits workflow order, scheduling, reporting hierarchy, and enforced software permissions.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** delivery leads, service owners, contributors, and operators.
- **Scenarios:** preparing an online-shop release; handing checkout support to operations; assigning security-control work; tracking incident follow-up responsibilities.
- **When not:** a simple task list already establishes ownership, or the real question is timing, dependencies, or technical access [1][4].
- **H3 stakeholder map:** choose it for engagement priorities; RACI assigns responsibility per activity.
- **E4 swimlane:** choose it for sequence and handoffs; link its activities to matrix rows.
- **F3 access-control model:** choose it for permitted operations. Review permission is not business accountability; **D3** instead addresses data lineage and ownership.
- **DACI:** choose it to organize a particular decision; use RACI for the resulting delivery responsibilities [3].

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required:** scoped activities as rows, identifiable participants as columns, cell assignments, and a legend. Use short verb–object activity names.
- **Codes:** R performs work; A answers for its outcome; C supplies input; I receives updates. Define whether A includes formal approval [1][2].
- **Policy:** normally one A and at least one R per execution row. Shared A needs explicit authority boundaries or a resolution rule; do not silently erase agreed governance.
- **Combined codes:** A/R may name the same participant. Distinguish “no involvement” from “unknown”; blanks must not represent both.
- **Optional:** phase groups, activity IDs, evidence references, effective date, and a role-to-person register. Label an added S as RASCI.
- **Arrows:** none in the matrix. Cells are assignments, not data flow or sequence. Consultation can involve two-way communication without drawn connectors.
- **Companion flow:** label escalation arrows with their trigger and meaning; keep them separate from the matrix.
- **Detail:** use comparable activity granularity and explain mixed participant levels. Letters carry meaning; color is supplementary.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
| Best practice | Anti-pattern |
| --- | --- |
| Agree assignments with the affected participants [1][2]. | Treating an automatically generated draft as granted authority. |
| State local A/R rules and explain shared authority [1][2]. | Claiming one A or one R is universally mandatory. |
| Review row coverage and column workload [1]. | Checking letters while ignoring bottlenecks. |
| Keep meaningful activities and necessary C/I assignments [1][5]. | Filling every cell or listing every implementation microtask. |
| Revisit assignments when scope or staffing changes [2]. | Copying a template's ownership into a different organization. |

Asana's main instructions recommend one R, while its FAQ permits multiple R assignments [4]. Use its practical guidance with that inconsistency in mind; it is not a normative cardinality rule.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [UK Government Security — populated Secure by Design RACI workbook](https://www.security.gov.uk/wp-content/uploads/2025/12/Cyber-security-roles-and-responsibilities-RACI-matrix-EXAMPLE-September-2026.xlsx) — activity-by-role assignments demonstrate the publisher's shared-A convention; confirm workbook reuse terms before adapting, since public availability alone is not an open license.
- [PMI — Project Manager and Business Analyst Collaboration, Exhibit 1](https://www.pmi.org/learning/library/business-analyst-project-manager-collaboration-6512) — an example RACI focuses on overlapping professional responsibilities; a conference-paper illustration, not a normative standard, with no open reuse license established: link rather than copy.
- [University of Essex — Responsibility matrix, populated four-row example](https://www.essex.ac.uk/staff/strategic-project-delivery/responsibility-matrix) — shows changing participant assignments and combined A/R; placeholder task labels teach notation rather than good activity naming, and no open reuse license is established.

The government workbook and Essex cells were checked as text; PMI's example was identified through its caption and surrounding explanation, not a cell-by-cell visual audit. A blank template or an AI prompt is not counted as a populated exemplar.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Set scope, audience, and current/proposed state; gather agreed activities and participants.
2. Choose roles or individuals; define codes, unknowns, combined codes, and the accountability policy.
3. Draft rows against evidence; leave uncertain ownership unresolved.
4. Review rows for gaps and columns for overload; split activities with conflicting outcomes.
5. Lay out activities vertically and participants horizontally; group phases and repeat headers when splitting.
6. Keep labels short, letters visible without color, and the legend adjacent; record effective date and update ownership.

**Self-check**
- [ ] Scope and state are explicit.
- [ ] Every row has execution coverage or a visible gap.
- [ ] A assignments follow the declared policy.
- [ ] Shared A has a resolution rule.
- [ ] Unknown differs from no involvement.
- [ ] Columns and C/I assignments were reviewed.
- [ ] Participants confirmed ownership; evidence supports the claims.
- [ ] Headers, codes, and legend remain readable without color.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Governance documents and approved decisions support documented responsibility assignments.
- Runbooks and release procedures identify activities, duties, and escalation routes.
- `CODEOWNERS` and approval configuration establish review rules, not organizational A.
- Commit frequency, administrator access, and issue assignment do not establish accountability.
- Record each claim's path, revision, and verified/inferred/doc-only/conflict status; confirm ownership gaps with people.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which activities need clearer ownership, and is this current or proposed state?
2. Should participants be roles, teams, or named individuals?
3. What does A mean here, and is shared accountability permitted?
4. Which assignments are agreed, unresolved, or need a separate escalation flow?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/H1.json` · Layout template: `grid_table` · one `tables[]` entry with activity rows × participant columns and R/A/C/I in the cells (exactly one A per row); the legend goes in the table `title`.

## Sources {#sources}
<!-- skill: omit -->
1. Atlassian — Understanding and using RACI charts — https://www.atlassian.com/work-management/project-management/raci-chart — accessed 2026-10-14.
2. UK Government Security — Agreeing roles and responsibilities, with example workbook — https://www.security.gov.uk/policy-and-guidance/secure-by-design/activities/agreeing-roles-and-responsibilities/ — accessed 2026-10-14.
3. Atlassian Team Playbook — DACI Decision-Making Framework — https://www.atlassian.com/team-playbook/plays/daci — accessed 2026-10-14.
4. Asana — Your guide to RACI charts, with examples — https://asana.com/resources/raci-chart — accessed 2026-10-14.
5. University of Essex — Responsibility matrix — https://www.essex.ac.uk/staff/strategic-project-delivery/responsibility-matrix — accessed 2026-10-14.
6. PMI — Partnering: Project Manager and Business Analyst Collaboration — https://www.pmi.org/learning/library/business-analyst-project-manager-collaboration-6512 — accessed 2026-10-14.
7. UK Government Security — Cyber security roles and responsibilities RACI matrix, example workbook — https://www.security.gov.uk/wp-content/uploads/2025/12/Cyber-security-roles-and-responsibilities-RACI-matrix-EXAMPLE-September-2026.xlsx — accessed 2026-10-14.

## Sample {#sample}
<!-- skill: path only -->
![H1 sample: RACI matrix for a checkout release](/samples/H1-raci-matrix.svg)
*An online-shop release matrix assigns preparation, approval, support handoff and rollback readiness to generic roles. The assignments are illustrative, not an inferred organizational policy.*
