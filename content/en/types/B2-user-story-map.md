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
question: "What does the user do to reach a goal, and which coherent increments can support or test that experience?"
audiences: [product, developers, business]
level: concept
phases: [requirements]
scope: system
formal:
  kind: method
  ref: "Jeff Patton, story mapping — https://www.jpattonassociates.com/the-new-backlog/"
neighbours: [A4, A6, B3, B1]
status: draft
sourceRev: "2026-10-14"
---

# User story map

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
A story map answers **what a user does to reach a goal, and which coherent increments can support or test that experience**. It preserves the narrative context that a flat backlog can lose [1][3].
**Definition used here:** the collaborative product-discovery and planning method associated with Jeff Patton, not a versioned graphical standard [1][2].
The horizontal backbone follows the order in which the user's story is told; the vertical body organizes detail, alternatives, or priority. Neither axis is automatically a precise timeline.
Release or experiment slices cross the activity to support a meaningful outcome. A walking skeleton, prototype, or learning experiment can be the next step; “MVP” is not a required first-line label.
The map omits precise workflow semantics, implementation structure, detailed estimates, and commitments unless supplied separately. It is a conversation aid, not a self-contained requirements contract.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** product managers, researchers/designers, domain users, developers, and testers.
- **Scenarios:** discover an online shopping experience; select a checkout prototype; slice a release into useful increments; place a support-chatbot feature within an existing journey; expose missing steps or accessibility needs.
- **When not:** specifying exact branches/concurrency, committing a schedule, or inventorying internal modules.
- Choose **A6 Journey map** for touchpoints, thoughts, and feelings across an experience [5].
- Choose **B3 Feature tree** for capability hierarchy without narrative/release semantics.
- Choose **B1 Use case diagram** for actor–goal relationships, or **E2 Activity/flowchart** for precise behavior.
- A roadmap communicates strategic outcomes/timing; a sprint board tracks work state. Neither is a synonym for a story map.

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
- **Color:** reinforce card/group/slice meaning with labels; no mandatory palette, row count, or number of releases exists.

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

These are worked teaching illustrations, not three independently verified production backlogs. Source text and descriptions were inspected; their images were not visually reviewed.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Select a target user, goal, scope, and current or proposed experience.
2. Read research and scenarios; tell the user's story in a short narrative.
3. Place comparable activities left to right, with related tasks and details beneath.
4. Expand enough to expose alternatives, gaps, and enabling dependencies.
5. Define vertical ordering; select an outcome or learning slice if planning delivery.
6. Use short cards, aligned columns, labeled slices, and sparse redundant color.
7. Walk the chosen slice end to end; keep evidence, commitments, and assumptions distinct.

**Self-check**
- [ ] User, goal, and scope are explicit.
- [ ] The backbone forms an intelligible narrative.
- [ ] Detail cards belong to the correct activity.
- [ ] Vertical position and color have declared meanings.
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
Integration target: `assets/templates/B2.json`; layout `grid_table`. Activity columns, grouped task cards, and labeled slice bands express narrative and scope, not execution-state columns.

## Sources {#sources}
<!-- skill: omit -->
1. Jeff Patton — *The New User Story Backlog is a Map* (2008) — https://www.jpattonassociates.com/the-new-backlog/ — accessed 2026-10-14.
2. Jeff Patton — *Story Mapping quick reference* — https://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf — accessed 2026-10-14.
3. Agile Alliance — *Story Mapping* — https://www.agilealliance.org/glossary/story-mapping/ — accessed 2026-10-14.
4. Nielsen Norman Group — *Mapping User Stories in Agile* — https://www.nngroup.com/articles/user-story-mapping/ — accessed 2026-10-14.
5. Nielsen Norman Group — *Journey Mapping 101* — https://www.nngroup.com/articles/journey-mapping-101/ — accessed 2026-10-14.

## Sample {#sample}
<!-- skill: path only -->
Planned asset: `/samples/B2-user-story-map.svg`.

**Caption:** An online shopper discovers items, compares them, checks out, and tracks delivery; a prototype slice tests one complete shopping goal. The generated sample is not yet available.
