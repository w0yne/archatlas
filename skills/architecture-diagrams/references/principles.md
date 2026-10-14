# Drawing principles

These are the generic rules distilled from many review rounds; the numbers are for reference inside this skill, quote the text rather than the number. The ten that must always be remembered are also listed in `SKILL.md`. Rules marked **[auto]** are checked mechanically by `scripts/atlas check`; **[planned]** marks checks that are not implemented yet; the others need judgement.

## Before drawing

1. **State audience, purpose and as-is or to-be first.** Depth and vocabulary depend on them; a business-plus-technical overview is neither a marketing slide nor a deployment diagram.
2. **Pick the type from a catalogue and name it.** A wrong type or viewpoint costs the most rework (for example a context picture cannot show internals; a feature list is a capability map, not an architecture view). Naming the type gives the user a steering vocabulary.
3. **One question per diagram.** A diagram that answers two questions answers neither; split them across figures in one deliverable. Different figures may use different notations.
4. **Agree a text wireframe before rendering.** Layout changes are cheap in text and expensive in SVG.
5. **Trace every element to a requirement or a source.** Mark elements added from best practice as proposed. Keep verified, inferred and target design distinguishable. Non-verified edges render dashed. **[planned: evidence check]**
6. **Verify names and steps against code or documents.** One wrong interface name invalidates the figure for technical readers.

## Structure

7. **An architecture view shows components, not features.** Feature lists form a capability map. Features may appear as small tags inside a component.
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
22. **Every number, badge, multiplier or glyph needs an obvious meaning or a legend.** Do not use notation glyphs the audience will misread. If a small marker renders badly, remove it rather than tweak it. **[planned: unexplained-marker check]**
23. **Decoration is not clarity.** Icons only when they carry meaning; prefer clear boundaries and flows.
24. **Use a type scale** (title > element name > body > note). Dense figures may use smaller text when the audience will zoom; never shrink labels to fit. **[auto: minimum size]**

## Lines and flows

25. **An arrow ends exactly on what it connects.** A group-level link ends on the group border; it must not run into or across an unrelated region. **[auto: arrow-through-box, boundary-membership]**
26. **Short, local flows.** No long lines that run to the far side and fold back; arrange or pair the systems instead (for example pools with message flows at aligned heights). Avoid crossings. **[auto: warning]**
27. **Follow the chosen notation strictly.** Sequence: lifelines are real nameable systems; prerequisites come before the steps that need them; activations end at the return; a loop frame encloses the whole round trip. Generalise mechanisms into one named step unless the audience needs the protocol.
28. **Happy path first; errors in their own figure.** One scenario per flow figure. Start at the trigger the audience cares about.

## Process and quality assurance

29. **Ask one question at a time with a recommended default; answer the user's questions before redrawing.** Keep a decision log.
30. **For a figure that keeps failing review, sketch two alternative layouts in text, pick or merge, and suggest an independent review** of the rendered result. Alternatives converge faster than serial redraws.
31. **Render and inspect every version.** Check label backgrounds for every text anchor (start, middle, end), overlaps, consistent page orientation in documents, and readability at presentation size. **[auto + review]**
32. **Keep related figures in one deliverable** and give the same step numbers and names to the same things across figures.

## Where each kind of rule lives
- Always in mind: `SKILL.md` (core rules).
- Family-specific drawing advice and checklists: `references/types/<code>-<slug>.md`.
- Mechanically detectable: `scripts/atlas check` (see `rendering.md`).
- Process and review: `interaction.md`, `review.md`.
