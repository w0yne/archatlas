# archatlas W8c — re-evaluation, rescored (E2)

- Skill revision: `e7caaf8` (installed from the release zip built by `tools/pack_skill.py`)
- Hosts: claude 2.1.285 (Claude Code), codex codex-cli 0.160.1, pi 1.1.0
- Models: claude=us.anthropic.claude-sonnet-5-5, codex=us.openai.gpt-6.1-sol, pi=us.anthropic.claude-sonnet-5-5
- Cost: runs $12.62 + grading $1.83 = **$14.45** (Claude Code and Pi report cost; Codex is estimated from tokens × list price)
- Live host directories touched by any sandbox: 0

## Headline

| Host / arm | Runs | All gates pass | Mean score (0–3) | median semantic | median structure | median flow | median readability | median compliance | median honesty | Renderer used | Cost $ | Wall s | Tokens in / out / cache read |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude/skill | 10 | 5 | 2.27 | 2.0 | 3 | 2 | 2 | 2.0 | 2.0 | 9 | 3.7 | 615 | 240 / 59121 / 4294864 |
| codex/skill | 10 | 8 | 1.85 | 2.0 | 2 | 2 | 2 | 2.0 | 2.0 | 9 | 4.11 | 823 | 5953450 / 40403 / 5321160 |
| pi/skill | 10 | 6 | 2.28 | 2.0 | 3 | 2 | 3 | 2.0 | 2.0 | 9 | 2.09 | 619 | 308 / 56910 / 2851706 |

Skill beats no-skill (higher mean score) per host: claude 8/10, codex 7/10, pi 9/10 (release target: ≥ 8/10, DESIGN §8.5).

## Trigger set

| Host | Precision | Recall | TP | FP | Gate (≥5/6 TP, ≤1/6 FP) | Per item |
|---|---|---|---|---|---|---|
| claude | 1.00 | 1.00 | 6/6 | 0/6 | pass | T1:Y T2:Y T3:Y T4:Y T5:Y T6:Y T7:n T8:n T9:n T10:n T11:n T12:n |
| codex | 1.00 | 1.00 | 6/6 | 0/6 | pass | T1:Y T2:Y T3:Y T4:Y T5:Y T6:Y T7:n T8:n T9:n T10:n T11:n T12:n |
| pi | 1.00 | 0.83 | 5/6 | 0/6 | pass | T1:Y T2:Y T3:Y T4:Y T5:n T6:Y T7:n T8:n T9:n T10:n T11:n T12:n |

## Before / after (baseline: archatlas W8b — first full evaluation, rescored (E2), skill `3847acb`)

All cells read before → after.

| Host / arm | Gates pass | Mean score | median semantic | median structure | median flow | median readability | median compliance | median honesty |
|---|---|---|---|---|---|---|---|---|
| claude/skill | 7/10 → 5/10 | 2.10 → 2.27 | 2.0 → 2.0 | 3 → 3 | 1 → 2 | 2 → 2 | 2.0 → 2.0 | 3.0 → 2.0 |
| codex/skill | 8/10 → 8/10 | 1.85 → 1.85 | 2.0 → 2.0 | 2 → 2 | 2 → 2 | 2 → 2 | 2.0 → 2.0 | 2.0 → 2.0 |
| pi/skill | 6/10 → 6/10 | 2.15 → 2.28 | 2.0 → 2.0 | 3 → 3 | 2 → 2 | 2 → 3 | 1.0 → 2.0 | 3.0 → 2.0 |

| Host | Trigger TP before → after | FP before → after |
|---|---|---|
| claude | 6/6 → 6/6 | 0/6 → 0/6 |
| codex | 6/6 → 6/6 | 1/6 → 0/6 |
| pi | 6/6 → 5/6 | 1/6 → 0/6 |

| Scenario | Host | Arm | Mean before | Mean after | Δ | Failed gates before | Failed gates after |
|---|---|---|---|---|---|---|---|
| S1 | claude | skill | 2.17 | 2.50 | +0.33 | – | G1 |
| S1 | codex | skill | 1.83 | 1.83 | +0.00 | – | – |
| S1 | pi | skill | 2.33 | 2.33 | +0.00 | – | – |
| S2 | claude | skill | 2.00 | 2.17 | +0.17 | G1 | G1 |
| S2 | codex | skill | 2.00 | 1.83 | -0.17 | – | – |
| S2 | pi | skill | 2.50 | 2.50 | +0.00 | G1 | G1 |
| S3 | claude | skill | 2.17 | 2.00 | -0.17 | G1 | G1 |
| S3 | codex | skill | 1.50 | 1.33 | -0.17 | G1 | G1 |
| S3 | pi | skill | 2.17 | 1.67 | -0.50 | – | G1 |
| S4 | claude | skill | 2.00 | 2.33 | +0.33 | – | – |
| S4 | codex | skill | 1.67 | 1.83 | +0.16 | – | – |
| S4 | pi | skill | 2.00 | 2.33 | +0.33 | – | – |
| S5 | claude | skill | 2.50 | 2.83 | +0.33 | – | – |
| S5 | codex | skill | 1.67 | 2.17 | +0.50 | – | – |
| S5 | pi | skill | 2.67 | 2.67 | +0.00 | – | – |
| S6 | claude | skill | 2.33 | 1.67 | -0.66 | – | G1 |
| S6 | codex | skill | 2.67 | 2.33 | -0.34 | – | – |
| S6 | pi | skill | 1.67 | 2.00 | +0.33 | – | G1 |
| S7 | claude | skill | 2.17 | 2.00 | -0.17 | – | G1 |
| S7 | codex | skill | 1.83 | 1.83 | +0.00 | – | – |
| S7 | pi | skill | 1.83 | 2.17 | +0.34 | G1 | G1 |
| S8 | claude | skill | 1.83 | 1.83 | +0.00 | – | – |
| S8 | codex | skill | 2.17 | 2.00 | -0.17 | – | – |
| S8 | pi | skill | 1.83 | 2.33 | +0.50 | G3 | – |
| S9 | claude | skill | 1.83 | 2.67 | +0.84 | G1 | – |
| S9 | codex | skill | 1.67 | 2.00 | +0.33 | G1 | – |
| S9 | pi | skill | 2.00 | 2.50 | +0.50 | G1 | – |
| S10 | claude | skill | 2.00 | 2.67 | +0.67 | – | – |
| S10 | codex | skill | 1.50 | 1.33 | -0.17 | – | G1 |
| S10 | pi | skill | 2.50 | 2.33 | -0.17 | – | – |

## Skill vs no skill, per scenario and host (mean of graded dimensions)

No-skill rows not repeated in this run come from the baseline report (same models and prompts).

| Scenario | Host | Skill | No skill | Δ | Gates skill / no skill |
|---|---|---|---|---|---|
| S1 | claude | 2.5 | 1.5 | +1.00 | **FAIL** / **FAIL** |
| S1 | codex | 1.83 | 1.5 | +0.33 | pass / **FAIL** |
| S1 | pi | 2.33 | 1.67 | +0.66 | pass / **FAIL** |
| S2 | claude | 2.17 | 2.33 | -0.16 | **FAIL** / **FAIL** |
| S2 | codex | 1.83 | 2.0 | -0.17 | pass / pass |
| S2 | pi | 2.5 | 1.5 | +1.00 | **FAIL** / **FAIL** |
| S3 | claude | 2.0 | 1.17 | +0.83 | **FAIL** / **FAIL** |
| S3 | codex | 1.33 | 1.5 | -0.17 | **FAIL** / pass |
| S3 | pi | 1.67 | 1.33 | +0.34 | **FAIL** / **FAIL** |
| S4 | claude | 2.33 | 1.5 | +0.83 | pass / **FAIL** |
| S4 | codex | 1.83 | 1.33 | +0.50 | pass / **FAIL** |
| S4 | pi | 2.33 | 1.17 | +1.16 | pass / **FAIL** |
| S5 | claude | 2.83 | 2.67 | +0.16 | pass / pass |
| S5 | codex | 2.17 | 1.5 | +0.67 | pass / **FAIL** |
| S5 | pi | 2.67 | 1.67 | +1.00 | pass / **FAIL** |
| S6 | claude | 1.67 | 1.67 | +0.00 | **FAIL** / **FAIL** |
| S6 | codex | 2.33 | 2.0 | +0.33 | pass / **FAIL** |
| S6 | pi | 2.0 | 2.0 | +0.00 | **FAIL** / **FAIL** |
| S7 | claude | 2.0 | 1.17 | +0.83 | **FAIL** / **FAIL** |
| S7 | codex | 1.83 | 1.67 | +0.16 | pass / **FAIL** |
| S7 | pi | 2.17 | 1.5 | +0.67 | **FAIL** / **FAIL** |
| S8 | claude | 1.83 | 1.33 | +0.50 | pass / **FAIL** |
| S8 | codex | 2.0 | 1.17 | +0.83 | pass / **FAIL** |
| S8 | pi | 2.33 | 1.17 | +1.16 | pass / **FAIL** |
| S9 | claude | 2.67 | 2.0 | +0.67 | pass / **FAIL** |
| S9 | codex | 2.0 | 1.5 | +0.50 | pass / **FAIL** |
| S9 | pi | 2.5 | 2.17 | +0.33 | pass / **FAIL** |
| S10 | claude | 2.67 | 2.5 | +0.17 | pass / pass |
| S10 | codex | 1.33 | 1.83 | -0.50 | **FAIL** / **FAIL** |
| S10 | pi | 2.33 | 2.17 | +0.16 | pass / pass |

## All runs

| Run | Exit | Gates G1–G5 | semantic | structure | flow | readability | compliance | honesty | Type chosen (expected) | Skill loaded | Renderer | Clarify | Cost $ | Wall s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1-autonomous-claude-skill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 3 | 2 | 3 | A7 (C2,A7,C1) | pass | yes | 0 | 0.35 | 60.40 |
| S1-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | A7 (C2,A7,C1) | pass | yes | 0 | 0.21 | 50.80 |
| S1-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 3 | 2 | 2 | C3 (C2,A7,C1) | pass | yes | 0 | 0.39 | 89.40 |
| S2-autonomous-claude-skill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 1 | 3 | 3 | E1 (E1) | pass | yes | 0 | 0.13 | 36.90 |
| S2-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 2 | 1 | E1 (E1) | pass | yes | 0 | 0.22 | 86.10 |
| S2-autonomous-pi-skill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 3 | 2 | 3 | E1 (E1) | pass | yes | 0 | 0.12 | 36.60 |
| S3-guided-claude-skill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 2 | 1 | 2 | ['F3', 'F2'] (F3,F2) | pass | yes | 1 | 0.79 | 82.80 |
| S3-guided-codex-skill (rescored) | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 2 | 1 | 1 | 1 | F3 (F3,F2) | pass | yes | 1 | 0.76 | 95.30 |
| S3-guided-pi-skill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 2 | 1 | 3 | 1 | 2 | F3 (F3,F2) | pass | yes | 1 | 0.30 | 107.60 |
| S4-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 2 | 3 | 2 | E3 (E3) | unknown | yes | 0 | 0.21 | 58.30 |
| S4-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | E3 (E3) | pass | yes | 0 | 0.24 | 72.00 |
| S4-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 2 | 3 | 2 | E3 (E3) | pass | yes | 0 | 0.13 | 40.20 |
| S5-autonomous-claude-skill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 3 | 2 | 3 | 3 | E4 (A5,E4) | pass | yes | 0 | 0.16 | 44.00 |
| S5-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 3 | 2 | E4 (A5,E4) | pass | yes | 0 | 0.21 | 67.20 |
| S5-autonomous-pi-skill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 2 | 3 | 2 | 3 | E4 (A5,E4) | pass | yes | 0 | 0.12 | 32.10 |
| S6-guided-claude-skill | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 2 | ['C2', 'C3', 'F2', 'F1', 'F3', 'G2', 'G3'] (F2,F1,F3,G3,C2) | pass | no | 1 | 0.44 | 30.60 |
| S6-guided-codex-skill (rescored) | [0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 2 | 3 | F2, F3, G3 (runner-up) (F2,F1,F3,G3,C2) | pass | no | 0 | 0.46 | 18.90 |
| S6-guided-pi-skill | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 3 | ['F2', 'F1', 'F3', 'C3', 'G2', 'C2'] (F2,F1,F3,G3,C2) | pass | no | 0 | 0.12 | 31.50 |
| S7-autonomous-claude-skill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 2 | 2 | ['C2', 'C3', 'E1'] (C2,C3,E1) | pass | yes | 0 | 0.26 | 76.40 |
| S7-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | C2, C3, E1 (C2,C3,E1) | pass | yes | 0 | 0.37 | 114.50 |
| S7-autonomous-pi-skill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 3 | 1 | 3 | 2 | 2 | ['C2', 'C3', 'E1'] (C2,C3,E1) | pass | yes | 0 | 0.21 | 68.10 |
| S8-guided-claude-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | ['G1', 'D1'] (G1,D1) | pass | yes | 0 | 1.05 | 144.60 |
| S8-guided-codex-skill (rescored) | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 2 | 2 | G1, D1 (G1,D1) | pass | yes | 2 | 1.16 | 184.10 |
| S8-guided-pi-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 3 | 2 | 3 | 2 | 2 | ['G1', 'D1'] (G1,D1) | pass | yes | 1 | 0.45 | 138.90 |
| S9-autonomous-claude-skill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 2 | 3 | 3 | 2 | C3 (C3) | pass | yes | 0 | 0.13 | 35.20 |
| S9-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 2 | 2 | C3 (C3) | pass | yes | 0 | 0.25 | 55.90 |
| S9-autonomous-pi-skill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 2 | 2 | 3 | 2 | C3 (C3) | pass | yes | 0 | 0.10 | 35.80 |
| S10-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 2 | 3 | 2 | 3 | C2 (C2) | unknown | yes | 0 | 0.17 | 45.80 |
| S10-autonomous-codex-skill (rescored) | [0] | G1:✗ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 1 | 0 | C2 (C2) | pass | yes | 0 | 0.24 | 78.60 |
| S10-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 1 | 3 | 2 | 2 | C2 (C2) | pass | yes | 0 | 0.13 | 38.40 |

## Hard-gate failures

- **S1-autonomous-claude-skill**: G1 — All six systems are shown with clear boundaries and external participants, and visual inspection is supported by the trace. G1 fails because the editable model was saved in the workspace root rather than under out/; numbered dependencies also imply an assumed sequence and appear out of order.
- **S2-autonomous-claude-skill**: G1 — The diagram has four lifelines, numbered messages, distinct calls and replies, and one timeout-guarded retry fragment. However, the normal successful authorization reply is missing when the opt fragment is skipped, so it does not fully show the required happy path plus optional retry; visual inspection was truthfully reported.
- **S2-autonomous-pi-skill**: G1 — The diagram has four lifelines, numbered messages, distinct request/reply notation, and a clean layout, with files saved under out/. G1 fails because the combined-fragment guard is [retry], not a guard naming the timeout; assumptions and visual-review claims are transparently reported and supported by the trace.
- **S3-guided-claude-skill**: G1 — The matrix covers the stated grants and restriction, and additional content-access restrictions are disclosed as assumptions in the replies. However, the companion shows ownership groups and repeats permission links rather than identifying where trust changes, so the required separation of access control from trust boundaries is incomplete.
- **S3-guided-codex-skill**: G1 — Only an F3 matrix was drawn; the F2 trust-boundary figure that separates where trust changes from who-may-do-what is missing, so G1 fails. Cells are not color-coded to the legend (Allow, Deny and Unspecified cells all look alike), and the matrix invents Deny cells for admins that the prompt never stated. The reply claims 'visual review completed' while no image was read, but image views are not observable, so G2 is not failed.
- **S3-guided-pi-skill**: G1 — The access matrix and ownership scopes are present, but neither figure separately explains where trust changes, failing the required separation. The matrix also introduces an unmarked default-deny policy and labels Support invoice correction as explicitly denied, although only invoice reading was explicitly prohibited.
- **S6-guided-claude-skill**: G1 — The recommendations cover the relevant security questions, include trust boundaries, authentication and access control, and explain neighbouring types. However, the final six-view set violates the required 2–4-type deliverable; nothing was drawn or saved.
- **S6-guided-pi-skill**: G1 — The recommendations address security concerns and include trust-boundary threat modelling, authentication, access control, and a runner-up. However, the final set contains six diagrams rather than the required 2–4, and the agent continues gathering drawing prerequisites after the user accepts the list; no diagrams or files were produced.
- **S7-autonomous-claude-skill**: G1 — All three requested figures and the evidence table were produced under out/, but the worker lacks a cited start/deploy artefact, failing G1. The views have consistent boundaries and generally legible layouts, but some arrow directions and legend meanings are misleading; the pending visual review is reported truthfully.
- **S7-autonomous-pi-skill**: G1 — All three requested views and the evidence table were produced, but Vote web, Worker and Result web lack the required cited start or deploy artefacts. The diagrams are legible and appropriately scoped; image inspection and the lack of repository execution are supported by the trace.
- **S10-autonomous-codex-skill**: G1 — The C2 context diagram is correct, with all four neighbours and a legend, and the SVG is valid. The reply claims 'Visual review done: opened out/preview.png' although the trace shows no image was read and no browser was available. It also never says the browser-based check could not run or why, and never says visual review is pending. Those omissions fail G1 and G2. The delivery connector crosses the staff arrow and doubles back.

Raw results (events, replies, outputs) stay in the gitignored results directories; `evidence_dir` in the JSON names each run's directory.
