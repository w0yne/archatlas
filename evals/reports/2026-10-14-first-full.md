# archatlas W8b — first full evaluation (2026-10-14)

- Skill revision: `3847acb` (installed from the release zip built by `tools/pack_skill.py`)
- Hosts: claude 2.1.285 (Claude Code), codex codex-cli 0.160.1, pi 1.1.0
- Models: claude=us.anthropic.claude-sonnet-5-5, codex=us.openai.gpt-6.1-sol, pi=us.anthropic.claude-sonnet-5-5
- Cost: runs $20.68 + grading $1.9 = **$22.58** (Claude Code and Pi report cost; Codex is estimated from tokens × list price)
- Live host directories touched by any sandbox: 0

## Headline

| Host / arm | Runs | All gates pass | Mean score (0–3) | median semantic | median structure | median flow | median readability | median compliance | median honesty | Renderer used | Cost $ | Wall s | Tokens in / out / cache read |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude/noskill | 10 | 2 | 1.77 | 2.0 | 2 | 2 | 1 | 1.0 | 2.0 | 0 | 2.41 | 418 | 130 / 44447 / 1655989 |
| claude/skill | 10 | 6 | 2.08 | 2.0 | 3 | 1 | 2 | 2.0 | 3.0 | 9 | 4.58 | 594 | 236 / 67158 / 4566097 |
| codex/noskill | 10 | 2 | 1.53 | 2.0 | 2 | 2 | 2 | 1.0 | 1.0 | 0 | 3.32 | 740 | 3640606 / 80683 / 3218519 |
| codex/skill | 10 | 8 | 1.73 | 2.0 | 2 | 2 | 2 | 2.0 | 1.0 | 9 | 4.29 | 1137 | 6215058 / 47118 / 5567210 |
| pi/noskill | 10 | 1 | 1.58 | 2.0 | 2 | 1 | 1 | 1.0 | 2.0 | 0 | 1.03 | 414 | 202 / 40547 / 1211557 |
| pi/skill | 10 | 5 | 2.05 | 2.0 | 3 | 2 | 2 | 1.0 | 2.0 | 9 | 2.23 | 595 | 306 / 59573 / 3403245 |

Skill beats no-skill (higher mean score) per host: claude 6/10, codex 7/10, pi 8/10 (release target: ≥ 8/10, DESIGN §8.5).

## Trigger set

| Host | Precision | Recall | TP | FP | Gate (≥5/6 TP, ≤1/6 FP) | Per item |
|---|---|---|---|---|---|---|
| claude | 1.00 | 1.00 | 6/6 | 0/6 | pass | T1:Y T2:Y T3:Y T4:Y T5:Y T6:Y T7:n T8:n T9:n T10:n T11:n T12:n |
| codex | 0.86 | 1.00 | 6/6 | 1/6 | pass | T1:Y T2:Y T3:Y T4:Y T5:Y T6:Y T7:n T8:n T9:n T10:Y T11:n T12:n |
| pi | 0.86 | 1.00 | 6/6 | 1/6 | pass | T1:Y T2:Y T3:Y T4:Y T5:Y T6:Y T7:n T8:n T9:n T10:Y T11:n T12:n |

## Skill vs no skill, per scenario and host (mean of graded dimensions)

| Scenario | Host | Skill | No skill | Δ | Gates skill / no skill |
|---|---|---|---|---|---|
| S1 | claude | 2.17 | 1.5 | +0.67 | pass / **FAIL** |
| S1 | codex | 1.67 | 1.33 | +0.34 | pass / **FAIL** |
| S1 | pi | 2.33 | 1.67 | +0.66 | pass / **FAIL** |
| S2 | claude | 2.0 | 2.17 | -0.17 | **FAIL** / **FAIL** |
| S2 | codex | 2.0 | 1.67 | +0.33 | pass / **FAIL** |
| S2 | pi | 2.5 | 1.5 | +1.00 | **FAIL** / **FAIL** |
| S3 | claude | 2.17 | 1.17 | +1.00 | **FAIL** / **FAIL** |
| S3 | codex | 1.33 | 1.5 | -0.17 | **FAIL** / pass |
| S3 | pi | 2.17 | 1.33 | +0.84 | pass / **FAIL** |
| S4 | claude | 2.0 | 1.5 | +0.50 | pass / **FAIL** |
| S4 | codex | 1.33 | 1.17 | +0.16 | pass / **FAIL** |
| S4 | pi | 2.0 | 1.17 | +0.83 | pass / **FAIL** |
| S5 | claude | 2.17 | 2.67 | -0.50 | **FAIL** / pass |
| S5 | codex | 1.5 | 1.5 | +0.00 | pass / **FAIL** |
| S5 | pi | 1.83 | 1.33 | +0.50 | **FAIL** / **FAIL** |
| S6 | claude | 2.33 | 1.67 | +0.66 | pass / **FAIL** |
| S6 | codex | 2.67 | 2.33 | +0.34 | **FAIL** / pass |
| S6 | pi | 1.67 | 2.0 | -0.33 | pass / **FAIL** |
| S7 | claude | 2.17 | 1.17 | +1.00 | pass / **FAIL** |
| S7 | codex | 1.67 | 1.5 | +0.17 | pass / **FAIL** |
| S7 | pi | 1.83 | 1.5 | +0.33 | **FAIL** / **FAIL** |
| S8 | claude | 1.83 | 1.33 | +0.50 | pass / **FAIL** |
| S8 | codex | 2.0 | 1.0 | +1.00 | pass / **FAIL** |
| S8 | pi | 1.83 | 1.17 | +0.66 | **FAIL** / **FAIL** |
| S9 | claude | 2.0 | 2.0 | +0.00 | **FAIL** / **FAIL** |
| S9 | codex | 1.83 | 1.5 | +0.33 | pass / **FAIL** |
| S9 | pi | 1.83 | 2.0 | -0.17 | **FAIL** / **FAIL** |
| S10 | claude | 2.0 | 2.5 | -0.50 | pass / pass |
| S10 | codex | 1.33 | 1.83 | -0.50 | pass / **FAIL** |
| S10 | pi | 2.5 | 2.17 | +0.33 | pass / pass |

## All runs

| Run | Exit | Gates G1–G5 | semantic | structure | flow | readability | compliance | honesty | Type chosen (expected) | Skill loaded | Renderer | Clarify | Cost $ | Wall s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 2 | 1 | 1 | 2 | A7 (C2,A7,C1) | **FAIL** | no | 0 | 0.08 | 18.90 |
| S1-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 2 | 3 | A7 (C2,A7,C1) | pass | yes | 0 | 0.24 | 39.50 |
| S1-autonomous-codex-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 1 | 2 | 2 | 1 | 1 | C2 (C2,A7,C1) | **FAIL** | no | 0 | 0.10 | 77.60 |
| S1-autonomous-codex-skill | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 1 | A7 (C2,A7,C1) | pass | yes | 0 | 0.27 | 102.00 |
| S1-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 2 | 2 | 1 | 2 | A7 (C2,A7,C1) | **FAIL** | no | 0 | 0.04 | 19.30 |
| S1-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 1 | 2 | 2 | 3 | A7 (C2,A7,C1) | pass | yes | 1 | 0.11 | 32.30 |
| S2-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | 3 | 2 | 2 | 1 | 3 | E1 (E1) | **FAIL** | no | 0 | 0.04 | 11.00 |
| S2-autonomous-claude-skill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 3 | E1 (E1) | pass | yes | 0 | 0.14 | 26.60 |
| S2-autonomous-codex-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | 2 | 2 | 1 | 1 | 2 | E1 (E1) | **FAIL** | no | 0 | 0.06 | 15.80 |
| S2-autonomous-codex-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 1 | 2 | 3 | E1 (E1) | pass | yes | 0 | 0.25 | 98.00 |
| S2-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | 1 | 1 | 1 | 1 | 3 | E1 (E1) | **FAIL** | no | 0 | 0.02 | 9.40 |
| S2-autonomous-pi-skill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 3 | 2 | 3 | E1 (E1) | pass | yes | 0 | 0.12 | 29.90 |
| S3-guided-claude-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 1 | 1 | 1 | 2 | 0 | 2 | ['F3', 'F2'] (F3,F2) | **FAIL** | no | 2 | 0.35 | 59.50 |
| S3-guided-claude-skill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 3 | 3 | 1 | 3 | F3 (F3,F2) | pass | yes | 0 | 0.73 | 70.60 |
| S3-guided-codex-noskill | [0, 0, 0, 0, 0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 1 | 0 | F3+F2 (F3,F2) | **FAIL** | no | 0 | 0.58 | 130.90 |
| S3-guided-codex-skill | [0, 0, 0, 0, 0] | G1:✗ G2:– G3:– G4:✓ G5:✓ | 2 | 1 | 2 | 2 | 1 | 0 | F3 (F3,F2) | pass | yes | 0 | 0.64 | 52.70 |
| S3-guided-pi-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | 1 | 1 | 1 | 1 | 2 | ['F3', 'F2'] (F3,F2) | **FAIL** | no | 3 | 0.07 | 51.30 |
| S3-guided-pi-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 3 | 2 | 1 | 2 | ['F3', 'F2'] (F3,F2) | pass | yes | 1 | 0.19 | 68.70 |
| S4-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 1 | 2 | 1 | 1 | 1 | 3 | E3 (E3) | **FAIL** | no | 0 | 0.04 | 13.40 |
| S4-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 3 | E3 (E3) | pass | yes | 1 | 0.15 | 31.00 |
| S4-autonomous-codex-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 1 | 1 | 1 | 1 | 2 | E3 (E3) | **FAIL** | no | 0 | 0.09 | 45.80 |
| S4-autonomous-codex-skill | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 1 | 1 | 1 | E3 (E3) | pass | yes | 0 | 0.26 | 114.60 |
| S4-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 1 | 2 | 1 | 0 | 1 | 2 | E3 (E3) | **FAIL** | no | 0 | 0.02 | 8.70 |
| S4-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 1 | 3 | E3 (E3) | pass | yes | 1 | 0.08 | 20.40 |
| S5-autonomous-claude-noskill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 3 | 3 | 1 | 3 | E4 (A5,E4) | **FAIL** | no | 0 | 0.06 | 19.00 |
| S5-autonomous-claude-skill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 3 | 0 | 1 | 3 | E4 (A5,E4) | pass | yes | 0 | 0.16 | 26.20 |
| S5-autonomous-codex-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 1 | 1 | 3 | 1 | 2 | none (plain vertical step list; neither A5 nor E4) (A5,E4) | **FAIL** | no | 0 | 0.07 | 22.30 |
| S5-autonomous-codex-skill | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 1 | 2 | 0 | E4 (A5,E4) | pass | yes | 0 | 0.20 | 41.70 |
| S5-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 0 | 1 | 3 | 1 | 2 | – (A5,E4) | **FAIL** | no | 0 | 0.12 | 56.90 |
| S5-autonomous-pi-skill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 3 | 0 | 1 | 1 | E4 (A5,E4) | pass | yes | 0 | 0.10 | 21.90 |
| S6-guided-claude-noskill | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 2 | F2, F1, G3, C2 (F2,F1,F3,G3,C2) | **FAIL** | no | 3 | 0.24 | 39.00 |
| S6-guided-claude-skill | [0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 2 | 3 | ['F2', 'F1', 'G3', 'C3'] (F2,F1,F3,G3,C2) | pass | no | 0 | 0.39 | 35.90 |
| S6-guided-codex-noskill | [0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 2 | 3 | C2, F1, F3 (context, deployment, DFD with trust boundaries, sequences) (F2,F1,F3,G3,C2) | **FAIL** | no | 2 | 0.21 | 24.40 |
| S6-guided-codex-skill | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 3 | 3 | F2, F1 (runner-up G3) (F2,F1,F3,G3,C2) | pass | no | 1 | 0.42 | 18.70 |
| S6-guided-pi-noskill | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 3 | F2, F3, G3, C2 (F2,F1,F3,G3,C2) | **FAIL** | no | 3 | 0.06 | 34.90 |
| S6-guided-pi-skill | [0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 2 | ['C3', 'G3', 'F2', 'F1'] (F2,F1,F3,G3,C2) | pass | no | 1 | 0.07 | 27.90 |
| S7-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:– | 2 | 1 | 1 | 1 | 1 | 1 | ['C2', 'C3', 'E1'] (C2,C3,E1) | **FAIL** | no | 0 | 0.09 | 31.40 |
| S7-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 3 | 2 | ['C2', 'C3', 'E1'] (C2,C3,E1) | pass | yes | 0 | 0.47 | 120.50 |
| S7-autonomous-codex-noskill | [0] | G1:✗ G2:– G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 1 | 1 | C2+C3+E1 (C2,C3,E1) | **FAIL** | no | 0 | 0.21 | 108.50 |
| S7-autonomous-codex-skill | [0] | G1:✓ G2:– G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 1 | C2, C3, E1 (C2,C3,E1) | pass | yes | 0 | 0.48 | 209.10 |
| S7-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:– | 2 | 2 | 2 | 1 | 1 | 1 | ['C2', 'C3', 'E1'] (C2,C3,E1) | **FAIL** | no | 0 | 0.06 | 20.80 |
| S7-autonomous-pi-skill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | ['C2', 'C3', 'E1'] (C2,C3,E1) | pass | yes | 0 | 0.42 | 106.00 |
| S8-guided-claude-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:✗ G4:✓ G5:✓ | 2 | 2 | 1 | 1 | 0 | 2 | ['G1', 'D1'] (G1,D1) | **FAIL** | no | 0 | 1.36 | 162.20 |
| S8-guided-claude-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 1 | 3 | ['G1', 'D1'] (G1,D1) | pass | yes | 1 | 1.94 | 164.80 |
| S8-guided-codex-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:– G3:– G4:✓ G5:✗ | 2 | 1 | 2 | 0 | 1 | 0 | D1, G1 (G1,D1) | **FAIL** | no | 1 | 1.75 | 209.80 |
| S8-guided-codex-skill | [0, 0, 0, 0, 0] | G1:✓ G2:– G3:✓ G4:✓ G5:✓ | 3 | 2 | 2 | 2 | 2 | 1 | G1, D1 (G1,D1) | pass | yes | 0 | 1.26 | 341.50 |
| S8-guided-pi-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:✗ G4:✗ G5:✗ | 2 | 2 | 1 | 0 | 0 | 2 | ['G1', 'D1'] (G1,D1) | **FAIL** | no | 0 | 0.54 | 171.00 |
| S8-guided-pi-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✗ G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 1 | 2 | ['G1', 'D1'] (G1,D1) | pass | yes | 1 | 0.73 | 184.60 |
| S9-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 1 | 1 | 3 | C3 (C3) | **FAIL** | no | 0 | 0.06 | 21.70 |
| S9-autonomous-claude-skill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 3 | 1 | 3 | 1 | 3 | C3 (C3) | pass | yes | 0 | 0.13 | 31.40 |
| S9-autonomous-codex-noskill | [0] | G1:✗ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 1 | 0 | C3 (C3) | **FAIL** | no | 0 | 0.14 | 38.80 |
| S9-autonomous-codex-skill | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 2 | 1 | C3 (C3) | pass | yes | 0 | 0.27 | 108.30 |
| S9-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 1 | 3 | C3 (C3) | **FAIL** | no | 0 | 0.04 | 19.00 |
| S9-autonomous-pi-skill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 3 | 2 | 2 | 1 | 2 | C3 (C3) | pass | yes | 0 | 0.07 | 18.80 |
| S10-autonomous-claude-noskill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 3 | 3 | 2 | 2 | C2 (C2) | **FAIL** | no | 0 | 0.11 | 41.60 |
| S10-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 2 | 2 | C2 (C2) | pass | yes | 1 | 0.23 | 47.80 |
| S10-autonomous-codex-noskill | [0] | G1:✗ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 3 | 3 | 1 | 0 | C2 (C2) | **FAIL** | no | 0 | 0.11 | 66.50 |
| S10-autonomous-codex-skill | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 1 | 0 | C2 (C2) | pass | yes | 0 | 0.22 | 50.30 |
| S10-autonomous-pi-noskill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 2 | 1 | 3 | C2 (C2) | **FAIL** | no | 0 | 0.06 | 22.60 |
| S10-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 2 | 2 | 2 | 3 | C2 (C2) | pass | yes | 0 | 0.33 | 84.20 |

## Hard-gate failures

- **S1-autonomous-claude-noskill**: G1 — The overview includes all six systems and plausible, assumption-based relationships, but no editable model was delivered. External ownership is unclear for the warehouse, and the rendered payment label and legend have spacing collisions; the agent truthfully disclosed that it had not inspected a render.
- **S1-autonomous-codex-noskill**: G1 — Delivers an SVG and README, but there is no editable model under out/, no named type or runner-up, and no wireframe. The warehouse is not marked external (only the payment provider is distinguished by colour, with no legend). The 'Customer support tool' label nearly touches its box edge, and the figure carries status-like caveat text.
- **S1-autonomous-pi-noskill**: G1 — The conceptual overview includes all six systems and labels assumed connections, but incorrectly classifies the warehouse as internal and omits the required editable model. The diagram is legible, though boundaries are weak and the support arrow stops short of its box; the reply truthfully disclaims visual inspection.
- **S2-autonomous-claude-noskill**: G1 — The four-lifeline sequence diagram shows checkout, inventory, payment and a guarded single retry, but lacks required numbered messages and an asynchronous-message distinction. Assumptions and the lack of rendering or code verification are stated truthfully.
- **S2-autonomous-claude-skill**: G1 — The diagram has four lifelines, numbered messages, and the requested checkout interactions, but fails required notation: all messages look identical, and the retry uses an opt frame rather than the specified loop or alt. The agent truthfully disclosed that visual review was pending.
- **S2-autonomous-codex-noskill**: G1 — The deliverable is a Mermaid sequence diagram in markdown, not an SVG under out/, so the requested output is not met. It has 5 lifelines, autonumber, and the retry shown as an opt frame, but it also includes unrelated error branches (items unavailable, declined, retry timeout) that the expect list excludes. It never states that it was not visually checked, and it labels the interaction as proposed.
- **S2-autonomous-pi-noskill**: G1 — The described sequence adds out-of-stock rejection and payment-failure/release branches beyond the required happy path plus one retry. The Mermaid source and rendered preview are not included in the grading inputs, so required lifelines, numbered messages, guarded retry framing, message styles, and visual quality cannot be verified.
- **S2-autonomous-pi-skill**: G1 — The diagram has four lifelines, numbered messages, clear layout, and reported output under out/. G1 fails because the retry uses an unguarded opt frame rather than the required guarded loop or alt frame, and asynchronous-message notation is not distinguished.
- **S3-guided-claude-noskill**: G1 — The access matrix captures the stated permissions and labels several assumptions, but the diagram places both systems outside the team boundaries and does not establish where trust changes. The approved rendering was not delivered; the agent truthfully reported that no preview was inspected.
- **S3-guided-claude-skill**: G1 — The legible matrix preserves the stated access rules and marks proposed restrictions, but the required separate ownership/trust-boundary view is missing. Visual-review and font-measurement limitations are reported truthfully.
- **S3-guided-codex-skill**: G1 — Delivers a matrix whose cells match the prompt and marks unstated cells as Unspecified. It fails G1 because there is no boundaries figure (F2) separating where trust changes from who-may-do-what, and the first turns asked multiple questions that repeated each other. It fails G2 because the reply says 'Visual review done' although no image was read in the trace. The matrix also uses Deny for admin cross-team role management, which was not stated, and the legend uses line swatches that do not match the cell text.
- **S3-guided-pi-noskill**: G1 — The access matrix preserves the stated permissions and separates permissions from the proposed boundary diagram, but the approved rendering was not delivered. Only the matrix contents are supplied for inspection; the Mermaid source and any visual result are unavailable, limiting assessment of boundaries, arrows, and readability.
- **S4-autonomous-claude-noskill**: G1 — The reported state machine covers the lifecycle, but its unguarded Cancelled exits allow a paid cancellation to terminate without a refund, failing the required transition semantics. The Mermaid source and a rendered preview were not included in the grading inputs, so initial-state notation and visual readability cannot be verified; the agent truthfully disclosed that it had not rendered or inspected the diagram.
- **S4-autonomous-codex-noskill**: G1 — The state machine has no initial pseudostate and no final-state markers (terminal states are plain boxes), which fails the G1 requirement. Edge labels are missing or hidden in the render (Pay, Pack, etc. are off-canvas above the boxes or clipped), and the Shipped edge has the wrong label and an overlapping, confusing route. Transitions are not consistently labelled as events or guards, and the Shipped→Return requested path is questionable because it conflicts with the stated rule that returns follow receipt.
- **S4-autonomous-pi-noskill**: G1 — The reported Mermaid state machine covers the principal lifecycle and terminal outcomes, but the supplied artefacts do not demonstrate the required initial pseudostate or event-labelled transitions. The shared RefundPending rejection path can incorrectly send a cancelled, never-shipped order to Delivered; no source or rendered preview was supplied to assess visual readability.
- **S5-autonomous-claude-skill**: G1 — The swimlane model captures the requested parties, steps and notification, with clear forward progression. However, the attached render displays Chinese text as fallback boxes throughout, violating an explicit deliverable requirement; the figure also lacks a legend.
- **S5-autonomous-codex-noskill**: G1 — The SVG is saved to out/ with clean Chinese labels. It is a plain four-box vertical chain with the party as a small caption, not a BPMN or swimlane. There are no pools or lanes and no message flows. The reply does not choose between A5 and E4 or give a reason, so G1 fails. It makes no false visual-check claim.
- **S5-autonomous-pi-noskill**: G1 — The generic flowchart includes the requested steps and legible Chinese labels, but provides neither BPMN pools nor swimlanes. Long folded exception routes violate the routing requirement; the reply transparently identifies added assumptions but omits a type-choice rationale and visual-review status.
- **S5-autonomous-pi-skill**: G1 — The swimlane diagram contains the required participants and ordered steps, with clear, noncrossing handoffs. G1 fails because the attached render displays fallback boxes throughout rather than readable Chinese; the claim that Chinese displays normally is not supported by this artefact.
- **S6-guided-claude-noskill**: G1 — The recommendations cover a threat-model DFD with trust boundaries, authentication, and access control, but fail the required small set: eleven diagrams initially and seven in the revised plan. Nothing was drawn or saved, and no visual-validation claim was made.
- **S6-guided-codex-skill**: G1 — Recommends F2 (threat-model DFD with trust boundaries) and F1 (auth flow) with the question each answers, names G3 as runner-up, and draws nothing. Only 2 types are recommended, which is within the 2-4 range, but access-control model is mentioned only as part of the auth flow rather than as a separate view (F3), so the 'considers access-control model' item is only weakly met. Under strict G1 the final recommendation omits an explicit access-control view, so G1 is marked failed.
- **S6-guided-pi-noskill**: G1 — The recommendations address threat modeling, trust boundaries, authentication, and cloud access control, but the final seven-item set fails the required small set of 2–4 named types. No diagrams or files were produced, and no visual-validation claim was made.
- **S7-autonomous-claude-noskill**: G1 — Three Mermaid figures and an evidence table were delivered under out/, but the table omits the required evidence statuses and does not cite a start/deploy artefact for every container, notably worker. Diagram layout and arrow notation cannot be confirmed from the supplied material; the agent truthfully disclosed that it did not render or visually inspect the diagrams.
- **S7-autonomous-codex-noskill**: G1 — The deliverables exist with evidence IDs and file/line references, but the evidence table has no verified/inferred/doc-only/conflict statuses and the figures do not mark inferred edges. The reply says 'SVG validity ... checked' and mentions 'checking the SVG figures' while no image was read; it only claims validity, but the process note is ambiguous. The container diagram has crossing and overlapping lines, and a label overlaps the boundary. It cites docker-compose.yml but does not cite Dockerfiles per container.
- **S7-autonomous-pi-noskill**: G1 — G1 fails because out/evidence.md lacks the required verified / inferred / doc-only / conflict status field. The main relationships have repository references, and the reply truthfully disclaims rendering and execution; diagram layout and dashed-edge notation cannot be confirmed from the supplied file listings without source or previews.
- **S7-autonomous-pi-skill**: G1 — All three requested views and an evidence table were produced, with plausible repository references and a truthful visual-review claim. G1 fails because the inferred browser interaction is drawn with solid arrows rather than the required dashed notation; container routing also introduces crossings and long folded paths.
- **S8-guided-claude-noskill**: G1, G3 — Both requested diagrams were saved under out/, and documentation/code conflicts were reported. However, persistence-class cardinalities lack concrete class-path citations, deployment arrows lack individually traceable evidence, and the rendered previews contain effectively invisible relationship labels; visual inspection and non-execution claims agree with the trace.
- **S8-guided-codex-noskill**: G1, G5 — The PNG renders show boxes with no text, because the Mermaid SVGs use foreignObject labels, which fail G5. The reply claims 'visually checked' although no image was read (G2). The agent also did not ask the deployment-target question up front; it built everything first and only reacted to the user's answer afterwards. The rendered diagrams are unreadable. The G1 failure comes from the empty labels and the late question.
- **S8-guided-pi-noskill**: G1, G3, G4, G5 — Both requested views and conflict findings were saved under out/, but cardinalities lack persistence-class path citations, and mandatory parent cardinalities contradict nullable foreign keys. The previews have missing labels, all SVGs fail G5, guided clarification was skipped, and the agent explicitly reports installing system libraries outside the workspace; image reads support its inspection claim, but not its claim that the renders are clean.
- **S8-guided-pi-skill**: G3 — Both required diagrams and the documented findings were delivered, but the evidence table does not justify the browser-to-app HTTP connector. The ER model is coherent; deployment routing, unsupported conflict interpretations, and premature rendering before explicit approval reduce quality.
- **S9-autonomous-claude-noskill**: G1 — The revision preserves the four containers and provides a clean boundary, but fails the required bilingual-label preservation by deleting Chinese text. Two horizontal relationship labels still touch or overlap their arrow lines; the agent truthfully states that no visual review occurred.
- **S9-autonomous-claude-skill**: G1 — The revised diagram is legible and has a clear boundary, but fails required preservation: Chinese labels were deleted, and the distinct asynchronous callback was replaced by a bidirectional charging relationship. The visual-review disclosure matches the recorded image reads and distinguishes preview inspection from a full checklist review.
- **S9-autonomous-codex-noskill**: G1 — The diagram is clean and keeps the same four containers and their relationships, but it translated the Chinese labels to English instead of making mixed English/Chinese labels fit, so the CJK requirement is not met. The reply claims 'visually checked the rendered output' while the trace shows no image was read (G2 fail). The reply also does not name overflow or bullet lists as defects beyond brief change notes.
- **S9-autonomous-pi-noskill**: G1 — The revision has legible English labels, explicit boundaries and uncrossed arrows, but fails the required bilingual deliverable by deleting all Chinese labels. The agent truthfully states that no image review occurred.
- **S9-autonomous-pi-skill**: G1 — Fails required preservation: Chinese labels were deleted rather than fitted, and an inferred callback relationship was added as an ordinary current-state arrow. The diagram has clean container boundaries and mostly legible English text; the agent truthfully disclosed that no visual review occurred.
- **S10-autonomous-codex-noskill**: G1 — The context diagram is clean and correct, but the scenario expects the agent to report that the browser-based check could not run and to say 'visual review pending'. The reply instead claims it visually checked the diagram, while the trace shows no image was read (image_read=0). That is a false validation claim (G2), and the missing report on the unrun check fails G1.

## Method notes

### Setup
- **Installation.** The skill was installed from the release zip that `tools/pack_skill.py` builds at main `3847acb`, into each sandboxed host's skill directory. No renderer dependencies were preinstalled; that is the realistic install path (defect 1).
- **Models.**
  - Claude Code and Pi both ran `us.anthropic.claude-sonnet-5-5`, so their difference is the host's.
  - Codex ran `us.openai.gpt-6.1-sol`.
- **Guided scenarios** used the first listed mode and the scripted answers.
- **Grader.** A model grader (`evals/grade.py` with `evals/grader/prompt.md`) ran through Pi with no tools. It never graded its own model's output:
  - GPT-6.1 Sol graded the Claude Code and Pi runs;
  - Sonnet 5.5 graded the Codex runs.
- **What the grader saw:**
  - every agent message;
  - the produced files, with SVG source truncated;
  - up to 3 CairoSVG PNG renders;
  - the trace facts.
- **Automatic gates:**
  - G5 comes from `svg_checks`;
  - G4 is forced to fail when the trace shows an executed forbidden command;
  - G2 is set to n/a on Codex, whose JSON stream does not record image views.

### Trace facts
Trace facts count the agent's own tool calls, with heredoc bodies stripped before the forbidden-command match. The first version matched raw events, which:
- counted the skill text and system-prompt skill listings;
- flagged `spring-boot:run` written inside a README heredoc as an executed command.

Five S8 grades made with the wrong facts were re-graded; the superseded ones are kept beside them as `grade.v1.json`.

### No-skill arms and the trigger set
The no-skill arms stopped before the trigger set. Triggers need the skill installed, and the harness's `all` includes them.

### Codex trigger rerun
Codex's first trigger runs (T1, T2) used up the per-process budget of the scenario run and were rerun as a separate trigger pass; the superseded pair is kept outside the results.

### Cost
The report's cost line covers the runs and grades that count. Superseded runs and grades added about $0.7.

## Top 10 skill defects (input to the next revision)

**Evidence paths** are relative to the raw results root, which is gitignored and kept
outside the repository. Each run directory holds `turnN.events.jsonl`, `final.txt`, `out/`,
`record.json` and `grade.json`.

**Ordering:** by the number of affected with-skill runs and by severity.

### 1. The bundle's renderer always runs in estimate mode; there are no install instructions
- **Kind:** reference / renderer.
- **What happened:**
  - In 27 of 27 with-skill runs that rendered, the findings report `measured_with: estimate`.
  - No run installed `scripts/requirements.txt`.
  - Codex tried `pip install pillow fonttools cairosvg` 3 times (S2, S9, S10). Every attempt failed with `/usr/bin/python3: No module named pip`, and no agent tried `python3 -m venv`, which works on this host.
  - Nothing in the skill tells an agent what to install, how, or that it should.
- **Where the instructions fall short:**
  - The SKILL.md `compatibility` field says `pip install archatlas`, but that package is not published.
  - `references/rendering.md` has no install step at all.
- **Consequences:** wrong text widths, mid-word wraps (#3) and fallback fonts (#2).
- **Evidence:**
  - `results/claude-skill/S1-autonomous-claude-skill/final.txt` ("Pillow and fontTools are missing")
  - the `out/*findings.json` of every skill run
- **Fix:**
  - Add a "Set up the renderer" step to `rendering.md`: `python3 -m venv .atlas-venv && .atlas-venv/bin/pip install -r scripts/requirements.txt`, then `scripts/atlas fonts doctor`.
  - `scripts/atlas` should prefer that venv's interpreter when one exists.
  - Make `render` print the exact install command when it falls back to estimate mode.
  - Drop `pip install archatlas` until the package is published.

### 2. Chinese labels render as fallback boxes; one agent claimed they display correctly
- **Kind:** renderer / honesty.
- **What happened:**
  - S5 failed G1 for Claude and Pi with the skill.
  - Estimate mode writes `font-family="sans-serif"` with no CJK family, so the rendered preview shows tofu boxes.
  - Pi answered "中文显示正常" without inspecting a CJK-capable render.
- **Evidence:** `results/claude-skill/S5-autonomous-claude-skill/out/diagram.svg`, `results/pi-skill/S5-autonomous-pi-skill/grade.json`
- **Fix:**
  - Always emit an explicit CJK-capable font stack when the label language is zh (Noto Sans CJK SC, Source Han Sans SC, PingFang SC, Microsoft YaHei), even in estimate mode.
  - Make `check` raise a warning, not info, when a CJK run has no measured glyph coverage.
  - In `review.md`: never state that CJK displays correctly without a preview rendered with a CJK font.

### 3. Labels and names wrap mid-word
- **Kind:** renderer.
- **Examples:** "Checkou / t", "Shipp / ed", "PaymentRec / eived", "vet_speci / alties", even with plenty of free canvas.
- **Seen in:** S2, S4 and S8 on 4 skill runs.
- **Evidence:** `results/claude-skill/S4-autonomous-claude-skill/grade.json`, `results/pi-skill/S4-autonomous-pi-skill/grade.json`
- **Fix:**
  - Break only at word boundaries for Latin text.
  - Widen the box up to `size_hint` or the column width before breaking.
  - Add a `check` finding for intra-word breaks in Latin runs.

### 4. Routing folds back and shares segments
- **Kind:** renderer.
- **What happened:** 15 of 30 with-skill runs got grader comments about folded, long or shared connector segments. Examples:
  - the C4/E3 transitions share x=1068;
  - the storefront arrow folds around the mobile app;
  - the warehouse route runs back across the figure.
- **Effect:** this is the main reason the skill arm's median **flow** stays at 1–2.
- **Evidence:** `results/claude-skill/S1-autonomous-claude-skill/grade.json`, `results/pi-skill/S4-autonomous-pi-skill/grade.json`, `results/claude-skill/S7-autonomous-claude-skill/grade.json`
- **Fix:**
  - Penalise shared collinear segments between unrelated edges in `route.py`.
  - Prefer the side ports that face the target.
  - Make `check` report a warning for edges whose length exceeds 2× the Manhattan distance.

### 5. Sequence notation is lost: no reply or async messages, and frames have no operator or guard
- **Kind:** reference / template / renderer.
- **What happened:**
  - S2 failed G1 for Claude and Pi with the skill.
  - Every message was modelled as `kind: call`, and replies were not dashed.
  - The retry was drawn as an unguarded `opt` frame instead of `loop`/`alt [timeout]`.
- **Why:** `assets/templates/E1.json` contains only `call` edges. The `frames` field in `rendering.md` has a free `label`, with no `operator` or `guard`.
- **Evidence:** `results/claude-skill/S2-autonomous-claude-skill/out/model.json`, `results/pi-skill/S2-autonomous-pi-skill/grade.json`
- **Fix:**
  - Give the E1 template one `reply` (dashed) and one `async` message.
  - Add `frames[].operator` (`loop|alt|opt|par|break`) and `guard`, and render them as `loop [guard]`.
  - Add a type-reference line: "a retry is `loop [timeout, max 1]` or `alt`".

### 6. Legends show renderer tokens instead of meaning
- **Kind:** renderer / reference.
- **What happened:** 12 of 30 with-skill grades criticise the legend. It either shows "peer", "primary" or "call · dashed", or is missing where it is needed (initial/final symbols, arrow meaning). This is the same finding as R2 S-1.
- **Evidence:** `results/pi-skill/S3-guided-pi-skill/grade.json`, `results/pi-skill/S2-autonomous-pi-skill/grade.json`
- **Fix:**
  - Generate per-template default legend labels ("request", "reply", "transition", "trust boundary").
  - Let `meta.legend` override the automatic entries.
  - Never print a style token.

### 7. Mixed English/Chinese input labels are dropped when revising
- **Kind:** instruction.
- **What happened:** on S9, all three hosts deleted or translated the Chinese labels, with and without the skill.
- **Why:** the skill only has a single "output language" brief field. Nothing says to keep the source's language mix in a fix-up task.
- **Evidence:** `results/claude-skill/S9-autonomous-claude-skill/final.txt`, `results/codex-skill/S9-autonomous-codex-skill/grade.json`
- **Fix:**
  - In the brief, add: "for revisions, keep the existing label languages unless asked".
  - In `principles.md`, add: "fix fit with layout, not by deleting text".
  - Add a review checklist item that compares the label language before and after.

### 8. Autonomous mode does not show a wireframe, and guided mode asks several questions at once or proceeds before approval
- **Kind:** instruction.
- **Wireframe:** missing in S1 for Claude and Pi. Codex showed one.
- **Guided mode:**
  - S3 and S8 asked 2–3 questions in one turn.
  - Pi rendered in S3 before "Approved".
  - Claude continued with defaults in S8 before approval.
- **Effect:** the skill arm's median **compliance** is only 1–2.
- **Evidence:** `results/pi-skill/S1-autonomous-pi-skill/grade.json`, `results/pi-skill/S3-guided-pi-skill/turn4.final.txt`, `results/claude-skill/S8-guided-claude-skill/grade.json`
- **Fix:** move the wireframe into the reply template ("before rendering, print the wireframe block") and make the one-question rule an explicit numbered checklist item in SKILL.md, with a "stop and wait" line after each question.

### 9. Inferred evidence is not reflected on the figure, and paired views are dropped
- **Kind:** instruction / reference.
- **S7 (Pi):** evidence statuses were listed as inferred, but the edges were drawn solid because the agent never set `evidence.status` in the model.
- **S3 (all three hosts):** only the access matrix (F3) was delivered, without the trust or ownership figure (F2) that the request implied.
- **Evidence:** `results/pi-skill/S7-autonomous-pi-skill/grade.json`, `results/claude-skill/S3-guided-claude-skill/turn4.final.txt`
- **Fix:**
  - In `repo-analysis.md`, add a step: "copy each claim's status into `edges[].evidence.status`".
  - In `selection.md`, add a "pairs" rule: "who-may-do-what plus where trust changes → F3 + F2".

### 10. The skill triggers on non-software flowcharts, and visual-review claims cannot be checked on Codex
- **Kind:** instruction / process.
- **Trigger:** T10 ("flowchart of how to bake bread") loaded the skill on Codex and Pi. The description excludes charts, mockups and logos, but not non-software process flowcharts.
- **Codex review claims:** Codex runs said "Visual review done" 7 times. `codex exec --json` emits no image-view events, so G2 could not be judged and was set to n/a. The grader nevertheless lowered Codex's honesty scores.
- **Evidence:** `results/codex-triggers/T10-trigger-codex-skill/record.json`, `results/pi-skill/T10-trigger-pi-skill/record.json`, `results/codex-skill/S4-autonomous-codex-skill/final.txt`
- **Fix:**
  - Add "or flowcharts of non-software everyday processes" to the description's exclusions.
  - In `review.md`: state the evidence for a visual review (the image file opened) in the delivery summary, so it can be audited on any host.

Raw results (events, replies, outputs) stay in the gitignored results directories; `evidence_dir` in the JSON names each run's directory.
