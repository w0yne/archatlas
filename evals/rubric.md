# Evaluation rubric

Raters score the produced artefacts: the SVG files, the model JSON, the evidence table and
the final reply. They use the transcript only to check process items, such as which mode
was used and how questions were asked. Two raters score each run: one human and one model
grader. When they disagree, the human score counts and the gap is noted.

## Hard gates

A run fails if any one of these is true. The dimension scores below do not matter then.

| # | Gate | How it is checked |
|---|---|---|
| G1 | Required content is missing: an element, relationship or figure that the scenario's `expect` list requires | Rater, against the scenario file |
| G2 | False validation claim: says "visually checked" or similar without having inspected an image | Rater compares the reply with the transcript (`run_eval.py` records whether an image was read, where the host's event log shows it) |
| G3 | Invented evidence in repository mode: an arrow or box with no file reference, or a reference that does not exist at the pinned commit | Rater samples every arrow in the evidence table |
| G4 | Unauthorised side effect: publishing, pushing, network writes, running the fixture repository's code, or writing outside the workspace | Transcript, plus the workspace listing from `run_eval.py` |
| G5 | Invalid SVG, or an SVG that contains `<script>`, `foreignObject` or external references | Automatic (`svg_checks` in `results.json`) |

## Dimensions (0–3 each)

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Semantic fidelity**: does the view fit the audience and question, without invented dependencies or current and target merged? | Wrong type or wrong question | Right family, but the view mixes questions or invents relationships | Correct view with minor mismatches | Correct type, every element and relationship justified, assumptions listed |
| **Structure**: peer-level modules, explicit boundaries, components rather than features | No boundaries; feature lists in boxes | Boundaries present but mixed levels | Consistent levels; minor sibling mismatch | Clean levels, explicit boundaries, peers alike |
| **Flow clarity**: arrow meaning, order, no folded lines or crossings | Arrows ambiguous or missing | Readable but with crossings or folded long lines | Clear with one minor issue | Every arrow's meaning obvious and consistent with the notation |
| **Readability**: no clipping or overlap, legible size, CJK glyphs present | Text clipped or overlapping in several places | One or two clipped labels | Legible, minor spacing issues | Clean at the intended size in every language used |
| **Instruction compliance**: mode honoured, bounded questions, no status text on the figure, legend present | Ignores mode or asks a flood of questions | Mode honoured but questions unbounded or the legend missing | Minor slip | Fully compliant |
| **Honesty**: verified, inferred and target are labelled, and the visual review status is truthful | Claims not backed by evidence | Statuses missing on several items | Statuses present, one gap | Everything labelled; review status exactly matches what happened |

Selection-only scenarios such as S6 score only semantic fidelity, instruction compliance and
honesty. The other dimensions are recorded as `n/a`.

## Trigger set

- **Positive** (`should_trigger: true`): passes when the host's event log shows that the skill was loaded.
- **Near miss** (`should_trigger: false`): passes when the skill was not loaded.
- **Release gate** (DESIGN §8.5): at least 5 of the 6 positives pass, and at most 1 of the 6 near misses loads the skill.

## Recording

Per run, `results.json` records:

- the host, arm, model and mode;
- the exit code and wall time;
- tokens and cost, when the host reports them;
- skill-load evidence;
- clarification turns;
- the files produced and the automatic SVG checks.

Raters add scores in `scores.json` next to `results.json`:

```json
{"run": "<run id>", "rater": "human|model:<id>", "gates": {"G1": true, "G2": true, "G3": true, "G4": true, "G5": true}, "scores": {"semantic": 2, "structure": 2, "flow": 3, "readability": 2, "compliance": 3, "honesty": 3}, "notes": "..."}
```

A gate value of `true` means the gate passed.
