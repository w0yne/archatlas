# User story map (用户故事地图)
<!-- Generated from content/en/types/B2-user-story-map.md by tools/build_skill_refs.py. Do not edit. -->
> What does the user do to reach a goal, and which coherent increments can support or test that experience?
Scope: system Neighbours: A4, A6, B1, B3.

## Meaning
A story map answers **what a user does to reach a goal, and which coherent increments can support or test that experience**. It preserves the narrative context that a flat backlog can lose.
**Definition used here:** the collaborative product-discovery and planning method associated with Jeff Patton, not a versioned graphical standard.
The horizontal backbone follows the order in which the user's story is told; the vertical body organises detail, alternatives, or priority. Neither axis is automatically a precise timeline.
Release or experiment slices cross the activity to support a meaningful outcome. A walking skeleton, prototype, or learning experiment can be the next step; “MVP” is not a required first-line label.
The map omits precise workflow semantics, implementation structure, detailed estimates, and commitments unless supplied separately. It is a conversation aid, not a self-contained requirements contract.

## When to use and how to choose
- **Audience:** product managers, researchers/designers, domain users, developers, and testers.
- **Scenarios:** discover an online shopping experience; select a checkout prototype; slice a release into useful increments; place a support-chatbot feature within an existing journey; expose missing steps or accessibility needs.
- **When not:** specifying exact branches/concurrency, committing a schedule, or inventorying internal modules.
- Choose **A6 Journey map** for touchpoints, thoughts, and feelings across an experience.
- Choose **B3 Feature tree** for a feature hierarchy without narrative/release semantics.
- Choose **B1 Use case diagram** for actor–goal relationships, or **E2 Activity/flowchart** for precise behaviour.
- A roadmap communicates strategic outcomes/timing; a sprint board tracks work state. Neither is a synonym for a story map.
- Choose **A4 Business scenario matrix** for coverage across several roles at business-activity level; a story map tells one user's end-to-end story.

## Notation and elements
- **Core:** target user and goal; high-level activities/tasks forming the backbone; smaller detail cards grouped underneath.
- **Horizontal position:** approximate narrative order, not mandatory execution order.
- **Vertical position:** state whether it means necessity, priority, detail, or sophistication; do not mix interpretations silently.
- **Slice:** required when planning increments, optional during discovery; label target user, outcome/learning goal, and success evidence.
- **Names:** short verb phrases such as “Compare items” or “Confirm delivery”; keep full acceptance criteria in linked records.
- **Arrows:** normally unnecessary. A dependency arrow, if added, needs a separate legend and does not turn the map into a workflow.
- **Optional:** story IDs, research references, release bands, estimates, and linked technical enablers.
- **Multiple users:** use explicit lanes or linked maps rather than mixing incompatible narratives.
- **Colour:** reinforce card/group/slice meaning with labels; no mandatory palette, row count, or number of releases exists.

## Best practices and anti-patterns
- Establish the broad narrative before detailed decomposition; avoid an exhaustive first column and an empty remainder.
- Preserve narrative order in the backbone; prioritize the stories beneath it instead of sorting the whole experience by business value.
- Slice toward an end-to-end outcome or experiment; avoid delivering disconnected “highest-priority” fragments.
- Ground activities in research and consider alternatives; avoid presenting team assumptions or only one ideal path as the whole experience.
- Keep conversations, dependencies, and enabling work attached to cards; avoid treating attractive notes as agreed requirements or banning technical work categorically.

## Drawing recipe
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

## Evidence in a code repository
- User docs, end-to-end tests, UI flows, and acceptance criteria support current tasks.
- Feature flags and release notes indicate declared availability; inspect the relevant version.
- Code can reveal implementation coverage/dependencies, but not user value or agreed priority.
- Record `card/slice | source:line/section | revision | verified/inferred/doc-only/conflict`.
- Use research and stakeholder evidence for goals and priority; never generate a committed release plan from commit history.

## Guided-mode questions
1. Whose goal does the map follow, and where does the activity begin and end?
2. Are we describing the current experience, exploring ideas, or selecting an increment?
3. Which research establishes the activities and important alternatives?
4. What outcome or learning result must the next slice achieve?
5. Which dependencies, enabling work, or other user roles could change that slice?

## Template
Model template: `assets/templates/B2.json` · Layout template: `grid_table` · one `tables[]` entry with activity columns, release slices as rows and the story text in the cells.
Approximate: it is a table; task cards and slice bands are not drawn, and it expresses narrative and scope, not execution-state columns.

## Sample
Figure: `samples/B2-user-story-map.svg` (published with the site)
