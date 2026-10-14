---
code: H3
slug: stakeholder-map
family: H
names:
  en: Stakeholder map (power-interest grid)
  zh: 干系人地图（权力-利益矩阵）
  aliases:
    en: [power-interest grid, stakeholder matrix, stakeholder grid]
    zh: [干系人图, 利益相关者矩阵, 权力利益矩阵]
question: "Who can influence or is affected by the initiative, and how should each stakeholder be engaged?"
audiences: [leaders, business]
level: strategy
phases: [initiate]
scope: "Stakeholder engagement for one initiative at a stated time."
formal:
  kind: method
  ref: "Power-interest mapping practice; no universal graphical standard. Nielsen Norman Group, Stakeholder Analysis for UX Projects: https://www.nngroup.com/articles/stakeholder-analysis/"
neighbours: [A3, H1]
status: draft
sourceRev: "2026-10-14"
---

# Stakeholder map

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A stakeholder map connects assessed power and interest to engagement choices. It makes concerns and influence visible, including parties who never use the system. It supports governance and communication, rather than depicting software architecture.

**Definition used here:** a power–interest grid, not a stakeholder catalog, onion diagram, or relationship network. Those are related methods with different meanings. Interest is attention or stake in the initiative, not necessarily support for it [1].

There is no universal diagram version. Mendelow's primary 1981 paper concerns power and environmental dynamism [2]; do not misdate it as 1991 or equate its axes with this grid. The map omits exchanges, workflow, and activity-level accountability.

The familiar power–interest form is associated with Johnson and Scholes in historical accounts [3]. The cited secondary account's exact edition/date was not independently established here, so no first-edition claim is made. Maps are time-bound assessments, not measurements of a person's worth or permission to ignore affected groups.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** initiative sponsors, delivery leads, business analysts, and architects planning engagement.
- **Scenarios:** planning an online-shop checkout redesign; identifying overlooked affected groups; choosing review participants and views; revisiting engagement after scope changes.
- **When not:** a short stakeholder list already answers the question, or the required view is system structure, dependencies, or exchanges.
- **A3 business context:** shows parties and business exchanges; it has flows rather than influence rankings.
- **H1 RACI:** assigns responsibility per activity; a powerful stakeholder is not automatically accountable for every task.
- **Onion/catalog/network:** choose these for proximity, an inventory of concerns, or relationships respectively; they are not exact grid aliases.
- Choose audience-appropriate detail. Roles reduce personal identification but may still reveal sensitive assessments; there is no universal “internal only” rule.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Required:** initiative, assessment date, stakeholder labels, defined power and interest axes, scale/thresholds, and engagement interpretation.
- **Convention here:** interest increases rightward; power increases upward. Define power as ability to affect the initiative's outcome, not merely job seniority.
- **Quadrants:** high/high = engage closely; high power/low interest = keep satisfied; low power/high interest = keep informed/involved; low/low = monitor [1].
- **Scores:** use agreed qualitative categories or documented criteria. Numeric scales do not create objective precision; retain uncertainty outside the plotted point.
- **Optional:** attitude markers, assessment rationale, confidence, and a companion table of concerns, actions, owners, and review dates.
- **Arrows:** none between stakeholders by default. Axis arrows mean increasing values; optional movement arrows mean an explicitly labeled observed or proposed change.
- **Legend:** define attitude and movement markers; current position must differ from desired position. Interest must not silently encode attitude.
- **Labels/layout:** short roles or groups, with a separate legend or table for detail; use shape/text as well as color. Low power does not remove a right to participate [4].

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
| Best practice | Anti-pattern |
| --- | --- |
| Identify affected groups as well as decision-makers [4]. | Plotting only managers or direct system users. |
| Agree criteria and record the basis for placements [1][5]. | Inventing influence scores from job titles or commit counts. |
| Distinguish interest, impact, and attitude [1][4]. | Calling low-interest stakeholders opponents. |
| Link assessments to concrete engagement and revisit them [1][5]. | A static quadrant label with no action or review date. |
| Match assessment detail to the audience and purpose [1]. | Publishing identifiable judgments simply because names were replaced by roles. |

Quadrant labels vary across methods. A source that assesses interest *in a reform succeeding* may use different labels from a grid of interest *in the initiative*. State that distinction rather than importing labels such as “blocker” into every map [6].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Nielsen Norman Group — Stakeholder Analysis for UX Projects, populated power/interest/attitude table](https://www.nngroup.com/articles/stakeholder-analysis/) — distinguishes current and desired attitude alongside assessed power and interest; the completed table is the exemplar, not the blank grid. No open reuse license established: link rather than copy its names, prose, or graphics.
- [UK government-hosted — Understanding stakeholders and political networks, Diagram 3](https://assets.publishing.service.gov.uk/media/69dfa53e61d2e8e9b9e42dc2/Understanding-stakeholders-and-political-networks.pdf) — a populated interest/influence matrix connects prior stakeholder analysis to engagement planning; its reform-oriented definition of interest differs from a general attention axis. Check the document's copyright and third-party notices before adapting; government hosting alone is not a license grant.
- [Simply Stakeholders — Using a Stakeholder Matrix, Example 1](https://simplystakeholders.com/stakeholder-matrix/) — completed power–interest assignments connect six stakeholder groups to engagement approaches; a vendor-authored worked example, not evidence that those rankings generalize. No open reuse license established: link rather than copy the example or graphics.
- [Local Government Association — How to map stakeholders, completed engagement table](https://www.local.gov.uk/sites/default/files/documents/How%20to%20map%20stakeholders.pdf) — a populated alternative incorporates legitimacy and links assessment to channels and tactics; this is a salience-informed companion method, not an exact power–interest grid. No open reuse license established: use the method as a comparison and author original content.

These external examples are not scenarios reused in this page's authored sample. Diagram identity, tables, and worked assignments were checked through primary text extraction; no graphics are reproduced. TOGAF's current chapter was not retrievable and is not counted as a verified exemplar.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Set initiative, date, audience, and the engagement decision the map should support.
2. Gather decision-makers and affected groups; agree power/interest criteria with informed participants.
3. Record placement evidence and uncertainty; do not infer scores from repository activity.
4. Draw a 2×2 grid with interest increasing rightward and power upward; label thresholds and quadrants.
5. Place short role labels; keep attitude optional and distinct. Use neutral fills, text/shape markers, and a legend.
6. Put concerns, engagement actions, owners, and review dates in a companion table; check audience suitability.

**Self-check**
- [ ] Scope, date, axes, and thresholds are clear.
- [ ] Placements have an agreed basis; unknowns are explicit.
- [ ] Interest is separate from attitude and impact.
- [ ] Affected low-power groups were considered.
- [ ] Engagement actions and review dates are recorded.
- [ ] Movement arrows distinguish proposed from observed changes.
- [ ] Labels and markers work without color.
- [ ] Detail is appropriate for the intended audience.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- Governance documents, ADRs, runbooks, and issue discussions identify candidate groups and stated concerns.
- `CODEOWNERS` and approval rules show review authority within their technical scope only.
- Record paths, revisions, and evidence status; distinguish a documented role from an assessed influence level.
- Power, interest, attitude, and external affected groups need contextual evidence and participant validation; code alone cannot establish them.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which initiative and engagement decision should this map support?
2. Who will see it, and what assessment detail is appropriate?
3. How will power and interest be defined, and who can validate placements?
4. Which affected groups, engagement actions, and review dates must be included?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Integration target: `assets/templates/H3.json`; layout `grid_table`, with four quadrants and a companion engagement table. The model template is not yet provided.

## Sources {#sources}
<!-- skill: omit -->
1. Nielsen Norman Group — Stakeholder Analysis for UX Projects — https://www.nngroup.com/articles/stakeholder-analysis/ — accessed 2026-10-14; practical guidance and populated table, but its Mendelow date conflicts with the primary record.
2. A. L. Mendelow — Environmental Scanning—The Impact of the Stakeholder Concept, ICIS 1981 Proceedings, paper 20 — https://aisel.aisnet.org/icis1981/20/ — accessed 2026-10-14; primary abstract confirms power/dynamism and 1981.
3. Votito — Stakeholder Power Interest Matrix origins and analysis — https://www.votito.com/methods/stakeholder-mapping/ — accessed 2026-10-14; secondary historical discussion, not authority for an independently verified textbook edition.
4. Local Government Association — New Conversations 2.0: How to map stakeholders — https://www.local.gov.uk/sites/default/files/documents/How%20to%20map%20stakeholders.pdf — accessed 2026-10-14.
5. UK Government Analysis Function — Stakeholder mapping — https://analysisfunction.civilservice.gov.uk/policy-store/stakeholder-mapping/ — accessed 2026-10-14; scoring procedures are useful, but figure axis wording differs from the surrounding power/interest description.
6. UK government-hosted — Understanding stakeholders and political networks: Practical Guidance Note — https://assets.publishing.service.gov.uk/media/69dfa53e61d2e8e9b9e42dc2/Understanding-stakeholders-and-political-networks.pdf — accessed 2026-10-14.
7. Simply Stakeholders — Using a Stakeholder Matrix: 3 Practical Examples — https://simplystakeholders.com/stakeholder-matrix/ — accessed 2026-10-14; populated power–interest assignments in Example 1.

## Sample {#sample}
<!-- skill: path only -->
`/samples/H3-stakeholder-map.svg`

Expected sample, not yet provided: an original online-shop checkout engagement grid with generic roles and a companion action table. Placements will be explicitly hypothetical and will not rank real people or organizations.
