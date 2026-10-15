# Drawing principles

These are the generic rules distilled from many review rounds; the numbers are for reference inside this skill, quote the text rather than the number. The ten that must always be remembered are also listed in `SKILL.md`. Rules marked **[auto]** are checked mechanically by `scripts/atlas check`; **[planned]** marks checks that are not implemented yet; the others need judgement.

**Priority.** Safety and truth come first, then the selected notation (its line styles, arrowheads, cardinalities and identifiers), then the user's constraints, then the defaults below. The style and density rules are defaults with reasons: adapt them when the question, the notation or the viewing size requires it, and say so. Suggested counts are heuristics, never a reason to omit required information.

## Before drawing

1. **State audience, purpose and as-is or to-be first.** Depth and vocabulary depend on them; a business-plus-technical overview is neither a marketing slide nor a deployment diagram.
2. **Pick the type from a catalogue and name it.** A wrong type or viewpoint costs the most rework (for example a context picture cannot show internals; a list of business abilities is a capability map (A1), a breakdown of product features is a feature tree (B3), and neither is a structure view). Naming the type gives the user a steering vocabulary.
3. **One question per diagram.** A diagram that answers two questions answers neither; split them across figures in one deliverable. Different figures may use different notations.
4. **Agree a text wireframe before rendering.** Layout changes are cheap in text and expensive in SVG.
5. **Trace every element to a requirement or a source.** Mark elements added from best practice as proposed. Keep verified, inferred and target design distinguishable. Mark non-verified claims visibly: dashed lines where line style carries no notation meaning; where it does (UML, BPMN, ArchiMate), keep the formal line and add an evidence tag or legend mark. Require a start or deploy artefact only for runtime and deployment units; business roles and logical concepts need evidence of their own kind (documents, interviews, code names). **[planned: evidence check]**
6. **Verify names and steps against code or documents.** One wrong interface name invalidates the figure for technical readers.

## Structure

7. **A structure view (landscape, context, container, component, logical, layered) shows components, not features.** Business abilities belong in a capability map (A1); product feature breakdowns belong in a feature tree (B3). Inside a structure view, features may appear as small tags on a component.
8. **Siblings are the same kind of thing.** Do not mix containers, actors, process steps and capabilities in one row. **[planned]**
9. **One layering scheme for every system in the figure,** so systems can be compared side by side.
10. **Boundaries are explicit.** Each element sits visibly inside exactly one system boundary or is explicitly external. **[auto]**
11. **Separate the management plane from the runtime plane** in platform views: different users, different risks.
12. **Collapse non-focus subsystems to one box.** At overview level, a subsystem is a box; its internals belong in a dedicated figure.
13. **Visual weight follows importance; peers look alike.** The protagonist is larger, peers share style and size, placeholders are smallest. Name peers with names of the same kind (products with products, not functions). **[planned: peer-size check]**
14. **A shared or reused component is styled identically everywhere.**
15. **Choose contents that convey what is distinctive** about the system; omit generic plumbing that every system has.

## Text and labels

16. **Fix fit with layout, not by deleting text.** When revising, keep every user-written label in its original language; widen boxes, re-flow or split the view instead of removing or translating words.
17. **Short names and small tags; no bullet lists or sentences in boxes.** Express structure with nesting, layers and connections, not paragraphs. **[auto: warning]**
18. **No working notes, status words, assumptions or reasoning on the figure** ("TBD", "pending", "draft", "to be confirmed", "see earlier document"). They belong in surrounding text. Mark status only through a legend, such as "planned". **[auto: warning for status words]**
19. **Keep widely known terms; drop specialist acronyms** the audience does not use. Balance: every label must earn its place; less but sufficient.
20. **Full name plus abbreviation once in titles and headers; short form elsewhere.** Use the name the audience officially uses.
21. **Titles carry the message.** No subtitle that restates the diagram type; no internal iteration labels in titles ("simplified", "v2", "draft"). A small type caption is allowed only in a documentation page, not in the figure.
22. **Every number, badge, multiplier or glyph needs an obvious meaning or a legend.** Do not use notation glyphs the audience will misread. If an optional decorative marker renders badly, remove it rather than tweak it; if a required notation mark renders badly, replace it with a legible form that keeps its meaning (for example a text cardinality instead of a crow's foot). **[planned: unexplained-marker check]**
23. **Decoration is not clarity.** Icons only when they carry meaning; prefer clear boundaries and flows.
24. **Use a type scale** (title > element name > body > note). Dense figures may use smaller text when the audience will zoom; never shrink labels to fit. **[auto: minimum size]**

## Lines and flows

25. **An arrow ends exactly on what it connects.** A group-level link ends on the group border; it must not run into or across an unrelated region. **[auto: arrow-through-box, boundary-membership]**
26. **Short, local flows.** No long lines that run to the far side and fold back; arrange or pair the systems instead (for example pools with message flows at aligned heights). Reduce crossings where the layout allows; explain an unavoidable one instead of redrawing for it. **[auto: warning]**
27. **Follow the chosen notation strictly.** Sequence: lifelines are real nameable systems; prerequisites come before the steps that need them; activations end at the return; a loop frame encloses the whole round trip. Generalise mechanisms into one named step unless the audience needs the protocol.
28. **Focus on the main scenario, and keep the paths the question needs.** One scenario per flow figure, starting at the trigger the audience cares about. Keep retries, refusals, compensations and abuse paths whenever the question is about them (a retry policy, an access decision, a threat model); move only unrelated branches to their own figure.

## Process and quality assurance

29. **In guided clarification, ask one question at a time with a recommended default; answer the user's questions before redrawing.** Keep a decision log.
30. **For a figure that keeps failing review, sketch two alternative layouts in text, pick or merge, and suggest an independent review** of the rendered result. Alternatives converge faster than serial redraws. Stop refining when the meaning is right, labels are readable, errors are fixed and remaining warnings are explained; cosmetic passes are not required.
31. **Render and inspect every version.** Check label backgrounds for every text anchor (start, middle, end), overlaps, consistent page orientation in documents, and readability at presentation size. **[auto + review]**
32. **Keep related figures in one deliverable** and give the same step numbers and names to the same things across figures.

## Visual hierarchy

"Few words" and "rich visual structure" are compatible: words stay short, and structure carries the meaning. The renderer's one default style is built on these rules; apply them to hand-drawn figures too.

33. **Show boundaries with zones, not sentences.** A system boundary, layer, subnet, lane or trust zone is a tinted group with a header band holding its name. Use one tint per role (business, application, technology, data, security, neutral) and keep that mapping across all figures of one deliverable. A tint is a colour role, not a claim about content: say what it means in the legend.
34. **One focus element when the view has a single subject.** Style it `primary` (solid blue, white text): the system in a context view, the service in a container view, the central entity in a data model, the subject lifeline in a sequence. Every other ordinary element is a calm `peer`; never give several elements `primary`, and never repeat the focus style on peers "because they are important too". Shared services are green, outside parties gray, planned elements purple, and each such colour needs a legend entry. The warm `highlight` is not a second focus: use it for a status marker or a callout that the legend explains (for example "new this year"), sparingly. A view with no single subject (layers, state machines, matrices, process lanes, peer comparisons, assessment maps) has no focus element; do not invent one. If everything is emphasised, nothing is.
35. **Chips instead of bullet text.** A short technology, protocol, status or ownership word belongs in a chip on the element (`Relational`, `HTTPS`, `New`), not in a sentence inside the box. Keep chips to one to three per element and use one chip style per meaning.
36. **Step numbers only where order matters.** Step numbers belong on sequence diagrams and on process or swimlane steps, where the reader follows a sequence; on context, container, deployment, logical, layer or data views readers would take them as time order. Stable reference IDs that the notation or the user's documents use (threat IDs such as `DF-1`, requirement or control IDs) are identifiers, not order: keep them and say so in the legend. Where step numbers are used, start at 1 without gaps and make the order the real one.
37. **Shape says kind.** Databases are cylinders, queues are queue shapes, documents are folded cards, people are stick figures or person cards. Use a shape only where it separates kinds the reader must tell apart; do not add icons for decoration.
38. **One legend, consistent meaning.** Every colour, line style, chip colour and badge used must appear in one legend, with reader-facing words (not style names). The same meaning keeps the same look in every figure.
39. **Density follows the question and the viewing size.** A slide carries fewer elements than a zoomable document; zones and clear emphasis let a view carry more. The checker's node-count warning is a prompt to consider splitting, not a limit: explain it when the question needs the elements. Never shrink text to fit; widen, re-flow or split.
40. **Sequence diagrams: emphasise the subject lifeline and keep fragments narrow.** Style the subject lifeline `primary` and leave the others `peer`. Use few fragments (one `alt` or `loop` per figure is normal), give each `alt` operand a real guard and at least one message, and put the retry or failure path in a single operand rather than several. Keep only the participants the scenario needs so that fragments stay narrow and the figure is not tall.
41. **One file per view.** Deliver each view once, under one stable name (for example `context.svg` beside `context.json`), and link it once in the reply. Keep user files and earlier versions. Remove only temporary files this run created, when cleanup is permitted; otherwise name the final files and leave the rest untouched.

## Where each kind of rule lives
- Always in mind: `SKILL.md` (core rules).
- Family-specific drawing advice and checklists: `references/types/<code>-<slug>.md`.
- Mechanically detectable: `scripts/atlas check` (see `references/rendering.md`).
- Process and review: `references/interaction.md`, `references/review.md`.
