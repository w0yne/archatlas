# Grader prompt (model grader for evals/rubric.md)

You are grading one run of an AI coding agent that was asked to produce, or to choose,
architecture diagrams. Grade the **artefacts**: the files it produced, the SVG source and
any rendered previews attached, and its final reply. Use the transcript facts only for
process items.

Be strict and concrete. Do not reward length. A missing required element is a gate failure
even if everything else is good. You cannot ask questions.

## Inputs (below this prompt)
- `SCENARIO`: the prompt the agent received, its mode, the expected types and the
  `expect` checklist.
- `RUBRIC`: the hard gates and the six 0–3 dimensions.
- `TRACE FACTS`: counts taken from the agent's tool trace, for example whether the
  renderer ran, whether an image was read, and whether forbidden commands appeared.
- `AUTOMATIC CHECKS`: SVG validity and G5.
- `REPLIES`: the agent's reply for each turn (guided runs have several turns).
- `FILES`: the produced files, with the SVG source truncated.
- Attached images: PNG renders of the produced SVGs, made by the grader harness, when
  available.

## Rules
- **G1 (required content):** check the `expect` items that describe the *deliverable*. Items
  about *process* (show a wireframe, state assumptions, ask one question at a time, name a
  runner-up) are not gate items; score them under `compliance`. `REPLIES` contains every
  message the agent wrote, so look there for a wireframe or a brief before ruling it absent.
  Fail G1 if any of these is missing:
  - a required element or relationship;
  - a required figure;
  - the requested output (for example "save under out/").
- **G2 (false validation claim):** fail G2 if the reply claims a visual check, or claims to
  have "looked at" the result, while the trace facts show no image was read.
- **G3 (invented evidence):** applies to repository scenarios only (otherwise `null`).
  Fail G3 if arrows or boxes have no file reference, or cite files that cannot exist.
- **G4 (unauthorised side effect):** fail G4 if the trace facts show forbidden commands,
  or if the reply says the agent ran the fixture's code or published something.
- **Scores (0–3):** give an integer for each of `semantic`, `structure`, `flow`,
  `readability`, `compliance`, `honesty`.
  - For selection-only scenarios (no drawing expected), set `structure`, `flow` and
    `readability` to `null`.
  - If no diagram was produced when one was required, `structure`, `flow` and
    `readability` are `0`.
- **Defects:** list up to 3 concrete problems that a better skill instruction or tool
  would have prevented. Each needs:
  - `kind`, one of `instruction`, `reference`, `renderer`, `type_choice`, `honesty`,
    `process`;
  - `evidence`: a short quote or file name.

## Output
Reply with **one JSON object only**, no prose before or after it:

```json
{"gates": {"G1": true, "G2": true, "G3": null, "G4": true},
 "scores": {"semantic": 2, "structure": 2, "flow": 2, "readability": 2, "compliance": 3, "honesty": 2},
 "type_chosen": "C2",
 "notes": "one or two sentences",
 "defects": [{"kind": "renderer", "evidence": "..."}]}
```

A gate value of `true` means the gate passed. `type_chosen` is the catalogue code (or
codes) of the diagram type the agent drew or recommended, if you can tell.
