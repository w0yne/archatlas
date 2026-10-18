# Stakeholder map (干系人地图（权力-利益矩阵）)
<!-- Generated from content/en/types/H3-stakeholder-map.md by tools/build_skill_refs.py. Do not edit. -->
> Who can influence or is affected by the initiative, and how should each stakeholder be engaged?
Scope: Stakeholder engagement for one initiative at a stated time. Neighbours: A3, H1.
Method reference: honour explicit requests; outside the default core catalogue.

## Meaning
A stakeholder map connects assessed power and interest to engagement choices. It makes concerns and influence visible, including parties who never use the system. It supports governance and communication, rather than depicting software architecture.

**Definition used here:** a power–interest grid, not a stakeholder catalog, onion diagram, or relationship network. Those are related methods with different meanings. Interest is attention or stake in the initiative, not necessarily support for it.

There is no universal diagram version. Mendelow's primary 1981 paper concerns power and environmental dynamism; do not misdate it as 1991 or equate its axes with this grid. The map omits exchanges, workflow, and activity-level accountability.

The familiar power–interest form is associated with Johnson and Scholes in historical accounts. The cited secondary account's exact edition/date was not independently established here, so no first-edition claim is made. Maps are time-bound assessments, not measurements of a person's worth or permission to ignore affected groups.

## When to use and how to choose
- **Audience:** initiative sponsors, delivery leads, business analysts, and architects planning engagement.
- **Scenarios:** planning an online-shop checkout redesign; identifying overlooked affected groups; choosing review participants and views; revisiting engagement after scope changes.
- **When not:** a short stakeholder list already answers the question, or the required view is system structure, dependencies, or exchanges.
- **A3 business context:** shows parties and business exchanges; it has flows rather than influence rankings.
- **H1 RACI:** assigns responsibility per activity; a powerful stakeholder is not automatically accountable for every task.
- **Onion/catalog/network:** choose these for proximity, an inventory of concerns, or relationships respectively; they are not exact grid aliases.
- Choose audience-appropriate detail. Roles reduce personal identification but may still reveal sensitive assessments; there is no universal “internal only” rule.

## Notation and elements
- **Required:** initiative, assessment date, stakeholder labels, defined power and interest axes, scale/thresholds, and engagement interpretation.
- **Convention here:** interest increases rightward; power increases upward. Define power as ability to affect the initiative's outcome, not merely job seniority.
- **Quadrants:** high/high = engage closely; high power/low interest = keep satisfied; low power/high interest = keep informed/involved; low/low = monitor.
- **Scores:** use agreed qualitative categories or documented criteria. Numeric scales do not create objective precision; retain uncertainty outside the plotted point.
- **Optional:** attitude markers, assessment rationale, confidence, and a companion table of concerns, actions, owners, and review dates.
- **Arrows:** none between stakeholders by default. Axis arrows mean increasing values; optional movement arrows mean an explicitly labeled observed or proposed change.
- **Legend:** define attitude and movement markers; current position must differ from desired position. Interest must not silently encode attitude.
- **Labels/layout:** short roles or groups, with a separate legend or table for detail; use shape/text as well as colour. Low power does not remove a right to participate.

## Best practices and anti-patterns
| Best practice | Anti-pattern |
| --- | --- |
| Identify affected groups as well as decision-makers. | Plotting only managers or direct system users. |
| Agree criteria and record the basis for placements. | Inventing influence scores from job titles or commit counts. |
| Distinguish interest, impact, and attitude. | Calling low-interest stakeholders opponents. |
| Link assessments to concrete engagement and revisit them. | A static quadrant label with no action or review date. |
| Match assessment detail to the audience and purpose. | Publishing identifiable judgments simply because names were replaced by roles. |

Quadrant labels vary across methods. A source that assesses interest *in a reform succeeding* may use different labels from a grid of interest *in the initiative*. State that distinction rather than importing labels such as “blocker” into every map.

## Drawing recipe
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
- [ ] Labels and markers work without colour.
- [ ] Detail is appropriate for the intended audience.

## Evidence in a code repository
- Governance documents, ADRs, runbooks, and issue discussions identify candidate groups and stated concerns.
- `CODEOWNERS` and approval rules show review authority within their technical scope only.
- Record paths, revisions, and evidence status; distinguish a documented role from an assessed influence level.
- Power, interest, attitude, and external affected groups need contextual evidence and participant validation; code alone cannot establish them.

## Guided-mode questions
1. Which initiative and engagement decision should this map support?
2. Who will see it, and what assessment detail is appropriate?
3. How will power and interest be defined, and who can validate placements?
4. Which affected groups, engagement actions, and review dates must be included?

## Template
Model template: `assets/templates/H3.json` · Layout template: `grid_table` · two `tables[]` entries: a 2×2 influence-by-interest grid and a companion engagement table.
Approximate: the quadrants are plain table cells, not a drawn plane.

## Sample
Figure: `samples/H3-stakeholder-map.svg` (published with the site)
