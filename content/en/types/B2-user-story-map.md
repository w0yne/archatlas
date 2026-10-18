---
code: B2
slug: user-story-map
family: B
names:
  en: User story map
  zh: 用户故事地图
  aliases:
    en: [story map, story mapping]
    zh: [故事地图, 用户故事映射]
question: What does the user do to reach a goal, and which coherent increments can support or test that experience?
audiences: [product, developers, business]
levels: [concept]
phases: [requirements]
scope: system
formal: {kind: method, ref: 'Jeff Patton, story mapping — https://www.jpattonassociates.com/the-new-backlog/'}
neighbours: [A4, A6, B1, B3]
status: draft
sourceRev: '2026-10-14'
---

# User story map (用户故事地图)

> One user's end-to-end activities as a backbone, with stories hanging below and release slices cut across them.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A story map answers **what a user does to reach a goal, and which coherent increments can support or test that experience**. It preserves the narrative context that a flat backlog can lose [1][3].
**Definition used here:** the collaborative product-discovery and planning method associated with Jeff Patton, not a versioned graphical standard [1][2].
The horizontal backbone follows the order in which the user's story is told; the vertical body organises detail, alternatives, or priority. Neither axis is automatically a precise timeline.
Release or experiment slices cross the activity to support a meaningful outcome. A walking skeleton, prototype, or learning experiment can be the next step; “MVP” is not a required first-line label.
The map omits precise workflow semantics, implementation structure, detailed estimates, and commitments unless supplied separately. It is a conversation aid, not a self-contained requirements contract.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** product managers, researchers/designers, domain users, developers, and testers.
- **Scenarios:** discover an online shopping experience; select a checkout prototype; slice a release into useful increments; place a support-chatbot feature within an existing journey; expose missing steps or accessibility needs.
- **When not:** specifying exact branches/concurrency, committing a schedule, or inventorying internal modules.
- Choose **A6 Journey map** for touchpoints, thoughts, and feelings across an experience [5].
- Choose **B3 Feature tree** for a feature hierarchy without narrative/release semantics.
- Choose **B1 Use case diagram** for actor–goal relationships, or **E2 Activity/flowchart** for precise behaviour.
- A roadmap communicates strategic outcomes/timing; a sprint board tracks work state. Neither is a synonym for a story map.
- Choose **A4 Business scenario matrix** for coverage across several roles at business-activity level; a story map tells one user's end-to-end story.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Core:** target user and goal; high-level activities/tasks forming the backbone; smaller detail cards grouped underneath [1–4].
- **Horizontal position:** approximate narrative order, not mandatory execution order.
- **Vertical position:** state whether it means necessity, priority, detail, or sophistication; do not mix interpretations silently.
- **Slice:** required when planning increments, optional during discovery; label target user, outcome/learning goal, and success evidence.
- **Names:** short verb phrases such as “Compare items” or “Confirm delivery”; keep full acceptance criteria in linked records.
- **Arrows:** normally unnecessary. A dependency arrow, if added, needs a separate legend and does not turn the map into a workflow.
- **Optional:** story IDs, research references, release bands, estimates, and linked technical enablers.
- **Multiple users:** use explicit lanes or linked maps rather than mixing incompatible narratives.
- **Colour:** reinforce card/group/slice meaning with labels; no mandatory palette, row count, or number of releases exists.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
- Establish the broad narrative before detailed decomposition; avoid an exhaustive first column and an empty remainder [2].
- Preserve narrative order in the backbone; prioritize the stories beneath it instead of sorting the whole experience by business value [1].
- Slice toward an end-to-end outcome or experiment; avoid delivering disconnected “highest-priority” fragments [1][3][4].
- Ground activities in research and consider alternatives; avoid presenting team assumptions or only one ideal path as the whole experience [2][4].
- Keep conversations, dependencies, and enabling work attached to cards; avoid treating attractive notes as agreed requirements or banning technical work categorically [2][3].

## Exemplars {#exemplars}
<!-- skill: omit -->
- [Patton, Story Mapping quick reference](https://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf) — email-task illustrations distinguish activity levels, narrative flow, and release slices. **Rights:** no open figure-reuse license established; link and explain in original words.
- [Patton, The New User Story Backlog is a Map](https://www.jpattonassociates.com/the-new-backlog/) — the car backlog/slicing illustration explains why coherent capability coverage matters more than finishing isolated features. **Rights:** no image adaptation license established; do not trace.
- [Nielsen Norman Group, Mapping User Stories in Agile](https://www.nngroup.com/articles/user-story-mapping/) — a worked mobile-deposit map connects activities, detailed tasks, and a prototype's learning outcome. **Rights:** no open image license established; link only.

These are worked teaching illustrations, not three independently verified production backlogs.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Select a target user, goal, scope, and current or proposed experience.
2. Read research and scenarios; tell the user's story in a short narrative.
3. Place comparable activities left to right, with related tasks and details beneath.
4. Expand enough to expose alternatives, gaps, and enabling dependencies.
5. Define vertical ordering; select an outcome or learning slice if planning delivery.
6. Use short cards, aligned columns, labeled slices, and sparse redundant colour.
7. Walk the chosen slice end to end; keep evidence, commitments, and assumptions distinct.

**Self-check**
- [ ] User, goal, and scope are explicit.
- [ ] The backbone forms an intelligible narrative.
- [ ] Detail cards belong to the correct activity.
- [ ] Vertical position and colour have declared meanings.
- [ ] Each planned slice has a coherent outcome or learning goal.
- [ ] Alternatives, essential dependencies, and enabling work are considered.
- [ ] Evidence, candidate ideas, and commitments remain distinguishable and readable.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- User docs, end-to-end tests, UI flows, and acceptance criteria support current tasks.
- Feature flags and release notes indicate declared availability; inspect the relevant version.
- Code can reveal implementation coverage/dependencies, but not user value or agreed priority.
- Record `card/slice | source:line/section | revision | verified/inferred/doc-only/conflict`.
- Use research and stakeholder evidence for goals and priority; never generate a committed release plan from commit history.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Whose goal does the map follow, and where does the activity begin and end?
2. Are we describing the current experience, exploring ideas, or selecting an increment?
3. Which research establishes the activities and important alternatives?
4. What outcome or learning result must the next slice achieve?
5. Which dependencies, enabling work, or other user roles could change that slice?

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/B2.json` · Layout template: `grid_table` · one `tables[]` entry with activity columns, release slices as rows and the story text in the cells.
Approximate: it is a table; task cards and slice bands are not drawn, and it expresses narrative and scope, not execution-state columns.

## Sources {#sources}
<!-- skill: omit -->
1. Jeff Patton — *The New User Story Backlog is a Map* (2008) — https://www.jpattonassociates.com/the-new-backlog/ — accessed 2026-10-14.
2. Jeff Patton — *Story Mapping quick reference* — https://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf — accessed 2026-10-14.
3. Agile Alliance — *Story Mapping* — https://www.agilealliance.org/glossary/story-mapping/ — accessed 2026-10-14.
4. Nielsen Norman Group — *Mapping User Stories in Agile* — https://www.nngroup.com/articles/user-story-mapping/ — accessed 2026-10-14.
5. Nielsen Norman Group — *Journey Mapping 101* — https://www.nngroup.com/articles/journey-mapping-101/ — accessed 2026-10-14.

### A4 · Business scenario matrix (role × activity) {#variant-a4}

Editorial grouping preserves the distinct notation; use this recipe and its checks.

1. Fix scope (solution or business area, as-is / to-be) and the release vocabulary.
2. Pick one column source (value-stream stages, capabilities or backbone activities); 4–8 columns in narrative order.
3. List 4–8 roles as rows, grouped external / internal, primary role on top.
4. Write 0–3 scenarios per cell, verb + object at user-goal level; merge or reject summary and subfunction items.
5. Assign each scenario a release; hatch deliberately unsupported cells, leave not-applicable cells blank.
6. Layout: landscape grid, bold header row and header column, optional thin column bands by stage, no arrows.
7. Colour: one sequential scale for releases (darkest = R1) or 3 distinct fills; neutral grey hatch for "not supported"; outline marker for significant scenarios; legend bottom-right.
8. Text budget: ≤ 6 words per scenario, ≤ 3 per cell; optional footer with counts per release.

**Self-check**

- [ ] All rows are roles of one kind: no systems, no named people.
- [ ] All columns are business activities at one level, in narrative order.
- [ ] Every scenario is verb + object at user-goal level; no clicks, no epics.
- [ ] Every scenario has a release marker; the legend explains every fill, hatch and blank.
- [ ] Release 1 covers the primary role end to end.
- [ ] No step sequences, UI or technical terms in cells.
- [ ] The title states scope and as-is / to-be, and does not use the bare term "scenario map".
- [ ] The grid fits about 8 × 8, or is split by business area.

[Full method and historical sample](/types/a4-scenario-matrix#meaning).

## Sample {#sample}
<!-- skill: path only -->
![B2 · Enterprise Service Assistant](/samples/ai-service-assistant/B2/en/diagram.svg)
*What does the user do end to end, what is the smallest useful first release, and how are later releases sliced?*

[SVG](/samples/ai-service-assistant/B2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/B2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

[Historical shop regression sample](/samples/B2-user-story-map.svg) · [All 29 views](/use/ai-service-assistant) · [Illustrative assumptions](/use/ai-service-assistant-assumptions).
