# archatlas W8b — first full evaluation, rescored (E2)

- Skill revision: `3847acb` (installed from the release zip built by `tools/pack_skill.py`)
- Hosts: claude 2.1.285 (Claude Code), codex codex-cli 0.160.1, pi 1.1.0
- Models: claude=us.anthropic.claude-sonnet-5-5, codex=us.openai.gpt-6.1-sol, pi=us.anthropic.claude-sonnet-5-5
- Cost: runs $20.68 + grading $1.91 = **$22.59** (Claude Code and Pi report cost; Codex is estimated from tokens × list price)
- Live host directories touched by any sandbox: 0

## Headline

| Host / arm | Runs | All gates pass | Mean score (0–3) | median semantic | median structure | median flow | median readability | median compliance | median honesty | Renderer used | Cost $ | Wall s | Tokens in / out / cache read |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude/noskill | 10 | 2 | 1.78 | 2.0 | 2 | 2 | 1 | 1.0 | 2.0 | 0 | 2.41 | 418 | 130 / 44447 / 1655989 |
| claude/skill | 10 | 7 | 2.10 | 2.0 | 3 | 1 | 2 | 2.0 | 3.0 | 9 | 4.58 | 594 | 236 / 67158 / 4566097 |
| codex/noskill | 10 | 2 | 1.60 | 2.0 | 2 | 2 | 2 | 1.0 | 1.5 | 0 | 3.32 | 740 | 3640606 / 80683 / 3218519 |
| codex/skill | 10 | 8 | 1.85 | 2.0 | 2 | 2 | 2 | 2.0 | 2.0 | 9 | 4.29 | 1137 | 6215058 / 47118 / 5567210 |
| pi/noskill | 10 | 1 | 1.64 | 2.0 | 2 | 1 | 1 | 1.0 | 2.5 | 0 | 1.03 | 414 | 202 / 40547 / 1211557 |
| pi/skill | 10 | 6 | 2.15 | 2.0 | 3 | 2 | 2 | 1.0 | 3.0 | 9 | 2.23 | 595 | 306 / 59573 / 3403245 |

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
| S1 | codex | 1.83 | 1.5 | +0.33 | pass / **FAIL** |
| S1 | pi | 2.33 | 1.67 | +0.66 | pass / **FAIL** |
| S2 | claude | 2.0 | 2.33 | -0.33 | **FAIL** / **FAIL** |
| S2 | codex | 2.0 | 2.0 | +0.00 | pass / pass |
| S2 | pi | 2.5 | 1.5 | +1.00 | **FAIL** / **FAIL** |
| S3 | claude | 2.17 | 1.17 | +1.00 | **FAIL** / **FAIL** |
| S3 | codex | 1.5 | 1.5 | +0.00 | **FAIL** / pass |
| S3 | pi | 2.17 | 1.33 | +0.84 | pass / **FAIL** |
| S4 | claude | 2.0 | 1.5 | +0.50 | pass / **FAIL** |
| S4 | codex | 1.67 | 1.33 | +0.34 | pass / **FAIL** |
| S4 | pi | 2.0 | 1.17 | +0.83 | pass / **FAIL** |
| S5 | claude | 2.5 | 2.67 | -0.17 | pass / pass |
| S5 | codex | 1.67 | 1.5 | +0.17 | pass / **FAIL** |
| S5 | pi | 2.67 | 1.67 | +1.00 | pass / **FAIL** |
| S6 | claude | 2.33 | 1.67 | +0.66 | pass / **FAIL** |
| S6 | codex | 2.67 | 2.0 | +0.67 | pass / **FAIL** |
| S6 | pi | 1.67 | 2.0 | -0.33 | pass / **FAIL** |
| S7 | claude | 2.17 | 1.17 | +1.00 | pass / **FAIL** |
| S7 | codex | 1.83 | 1.67 | +0.16 | pass / **FAIL** |
| S7 | pi | 1.83 | 1.5 | +0.33 | **FAIL** / **FAIL** |
| S8 | claude | 1.83 | 1.33 | +0.50 | pass / **FAIL** |
| S8 | codex | 2.17 | 1.17 | +1.00 | pass / **FAIL** |
| S8 | pi | 1.83 | 1.17 | +0.66 | **FAIL** / **FAIL** |
| S9 | claude | 1.83 | 2.0 | -0.17 | **FAIL** / **FAIL** |
| S9 | codex | 1.67 | 1.5 | +0.17 | **FAIL** / **FAIL** |
| S9 | pi | 2.0 | 2.17 | -0.17 | **FAIL** / **FAIL** |
| S10 | claude | 2.0 | 2.5 | -0.50 | pass / pass |
| S10 | codex | 1.5 | 1.83 | -0.33 | pass / **FAIL** |
| S10 | pi | 2.5 | 2.17 | +0.33 | pass / pass |

## All runs

| Run | Exit | Gates G1–G5 | semantic | structure | flow | readability | compliance | honesty | Type chosen (expected) | Skill loaded | Renderer | Clarify | Cost $ | Wall s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 2 | 1 | 1 | 2 | A7 (C2,A7,C1) | **FAIL** | no | 0 | 0.08 | 18.90 |
| S1-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 2 | 3 | A7 (C2,A7,C1) | pass | yes | 0 | 0.24 | 39.50 |
| S1-autonomous-codex-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 1 | 2 | 2 | 1 | 2 | C2 (C2,A7,C1) | **FAIL** | no | 0 | 0.10 | 77.60 |
| S1-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | A7 (C2,A7,C1) | pass | yes | 0 | 0.27 | 102.00 |
| S1-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 2 | 2 | 1 | 2 | A7 (C2,A7,C1) | **FAIL** | no | 0 | 0.04 | 19.30 |
| S1-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 1 | 2 | 2 | 3 | A7 (C2,A7,C1) | pass | yes | 1 | 0.11 | 32.30 |
| S2-autonomous-claude-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 3 | 3 | 2 | 2 | 1 | 3 | E1 (E1) | **FAIL** | no | 0 | 0.04 | 11.00 |
| S2-autonomous-claude-skill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 1 | 1 | 2 | 3 | E1 (E1) | pass | yes | 0 | 0.14 | 26.60 |
| S2-autonomous-codex-noskill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | 2 | 2 | 2 | 1 | 3 | E1 (E1) | **FAIL** | no | 0 | 0.06 | 15.80 |
| S2-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 1 | 2 | 3 | E1 (E1) | pass | yes | 0 | 0.25 | 98.00 |
| S2-autonomous-pi-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 1 | 1 | 1 | 1 | 2 | 3 | E1 (E1) | **FAIL** | no | 0 | 0.02 | 9.40 |
| S2-autonomous-pi-skill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 3 | 2 | 3 | E1 (E1) | pass | yes | 0 | 0.12 | 29.90 |
| S3-guided-claude-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 1 | 1 | 1 | 2 | 0 | 2 | ['F3', 'F2'] (F3,F2) | **FAIL** | no | 2 | 0.35 | 59.50 |
| S3-guided-claude-skill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 3 | 3 | 1 | 3 | F3 (F3,F2) | pass | yes | 0 | 0.73 | 70.60 |
| S3-guided-codex-noskill (rescored) | [0, 0, 0, 0, 0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 1 | 0 | F3+F2 (F3,F2) | **FAIL** | no | 0 | 0.58 | 130.90 |
| S3-guided-codex-skill (rescored) | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 1 | 2 | 2 | 1 | 1 | F3 (F3,F2) | pass | yes | 0 | 0.64 | 52.70 |
| S3-guided-pi-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | 1 | 1 | 1 | 1 | 2 | ['F3', 'F2'] (F3,F2) | **FAIL** | no | 3 | 0.07 | 51.30 |
| S3-guided-pi-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 3 | 2 | 1 | 2 | ['F3', 'F2'] (F3,F2) | pass | yes | 1 | 0.19 | 68.70 |
| S4-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 1 | 2 | 1 | 1 | 1 | 3 | E3 (E3) | **FAIL** | no | 0 | 0.04 | 13.40 |
| S4-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 3 | E3 (E3) | pass | yes | 1 | 0.15 | 31.00 |
| S4-autonomous-codex-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 1 | 1 | 2 | 1 | 2 | E3 (E3) | **FAIL** | no | 0 | 0.09 | 45.80 |
| S4-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 1 | 2 | 2 | E3 (E3) | pass | yes | 0 | 0.26 | 114.60 |
| S4-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 1 | 2 | 1 | 0 | 1 | 2 | E3 (E3) | **FAIL** | no | 0 | 0.02 | 8.70 |
| S4-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 1 | 3 | E3 (E3) | pass | yes | 1 | 0.08 | 20.40 |
| S5-autonomous-claude-noskill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 3 | 3 | 1 | 3 | E4 (A5,E4) | **FAIL** | no | 0 | 0.06 | 19.00 |
| S5-autonomous-claude-skill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 3 | 2 | 1 | 3 | E4 (A5,E4) | pass | yes | 0 | 0.16 | 26.20 |
| S5-autonomous-codex-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 1 | 2 | 2 | 1 | 2 | none (plain vertical flowchart) (A5,E4) | **FAIL** | no | 0 | 0.07 | 22.30 |
| S5-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 2 | 0 | E4 (A5,E4) | pass | yes | 0 | 0.20 | 41.70 |
| S5-autonomous-pi-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 0 | 1 | 3 | 1 | 3 | – (A5,E4) | **FAIL** | no | 0 | 0.12 | 56.90 |
| S5-autonomous-pi-skill (rescored) | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 3 | 3 | 1 | 3 | E4 (A5,E4) | pass | yes | 0 | 0.10 | 21.90 |
| S6-guided-claude-noskill | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 2 | F2, F1, G3, C2 (F2,F1,F3,G3,C2) | **FAIL** | no | 3 | 0.24 | 39.00 |
| S6-guided-claude-skill | [0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 2 | 3 | ['F2', 'F1', 'G3', 'C3'] (F2,F1,F3,G3,C2) | pass | no | 0 | 0.39 | 35.90 |
| S6-guided-codex-noskill (rescored) | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 3 | F2, C2, sequence diagrams, deployment/network diagram (F2,F1,F3,G3,C2) | **FAIL** | no | 2 | 0.21 | 24.40 |
| S6-guided-codex-skill (rescored) | [0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 3 | 3 | F2, F1 (runner-up G3) (F2,F1,F3,G3,C2) | pass | no | 1 | 0.42 | 18.70 |
| S6-guided-pi-noskill | [0, 0, 0, 0] | G1:✗ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 3 | F2, F3, G3, C2 (F2,F1,F3,G3,C2) | **FAIL** | no | 3 | 0.06 | 34.90 |
| S6-guided-pi-skill | [0, 0, 0, 0] | G1:✓ G2:✓ G3:– G4:✓ G5:– | 2 | – | – | – | 1 | 2 | ['C3', 'G3', 'F2', 'F1'] (F2,F1,F3,G3,C2) | pass | no | 1 | 0.07 | 27.90 |
| S7-autonomous-claude-noskill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:– | 2 | 1 | 1 | 1 | 1 | 1 | ['C2', 'C3', 'E1'] (C2,C3,E1) | **FAIL** | no | 0 | 0.09 | 31.40 |
| S7-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 3 | 2 | ['C2', 'C3', 'E1'] (C2,C3,E1) | pass | yes | 0 | 0.47 | 120.50 |
| S7-autonomous-codex-noskill (rescored) | [0] | G1:✗ G2:– G3:✓ G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 1 | 1 | C2, C3, E1 (C2,C3,E1) | **FAIL** | no | 0 | 0.21 | 108.50 |
| S7-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | C2, C3, E1 (C2,C3,E1) | pass | yes | 0 | 0.48 | 209.10 |
| S7-autonomous-pi-noskill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:– | 2 | 2 | 2 | 1 | 1 | 1 | ['C2', 'C3', 'E1'] (C2,C3,E1) | **FAIL** | no | 0 | 0.06 | 20.80 |
| S7-autonomous-pi-skill | [0] | G1:✗ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 2 | 2 | ['C2', 'C3', 'E1'] (C2,C3,E1) | pass | yes | 0 | 0.42 | 106.00 |
| S8-guided-claude-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:✗ G4:✓ G5:✓ | 2 | 2 | 1 | 1 | 0 | 2 | ['G1', 'D1'] (G1,D1) | **FAIL** | no | 0 | 1.36 | 162.20 |
| S8-guided-claude-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 1 | 3 | ['G1', 'D1'] (G1,D1) | pass | yes | 1 | 1.94 | 164.80 |
| S8-guided-codex-noskill (rescored) | [0, 0, 0, 0, 0] | G1:✗ G2:– G3:✓ G4:✓ G5:✗ | 2 | 2 | 1 | 0 | 1 | 1 | G1, D1 (G1,D1) | **FAIL** | no | 1 | 1.75 | 209.80 |
| S8-guided-codex-skill (rescored) | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✓ G4:✓ G5:✓ | 3 | 2 | 2 | 2 | 2 | 2 | G1, D1 (G1,D1) | pass | yes | 0 | 1.26 | 341.50 |
| S8-guided-pi-noskill | [0, 0, 0, 0, 0] | G1:✗ G2:✓ G3:✗ G4:✗ G5:✗ | 2 | 2 | 1 | 0 | 0 | 2 | ['G1', 'D1'] (G1,D1) | **FAIL** | no | 0 | 0.54 | 171.00 |
| S8-guided-pi-skill | [0, 0, 0, 0, 0] | G1:✓ G2:✓ G3:✗ G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 1 | 2 | ['G1', 'D1'] (G1,D1) | pass | yes | 1 | 0.73 | 184.60 |
| S9-autonomous-claude-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 1 | 1 | 3 | C3 (C3) | **FAIL** | no | 0 | 0.06 | 21.70 |
| S9-autonomous-claude-skill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 3 | 1 | 3 | 1 | 2 | C3 (C3) | pass | yes | 0 | 0.13 | 31.40 |
| S9-autonomous-codex-noskill (rescored) | [0] | G1:✗ G2:– G3:– G4:✓ G5:✓ | 1 | 2 | 2 | 2 | 1 | 1 | C3 (C3) | **FAIL** | no | 0 | 0.14 | 38.80 |
| S9-autonomous-codex-skill (rescored) | [0] | G1:✗ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 2 | 1 | 1 | C3 (C3) | pass | yes | 0 | 0.27 | 108.30 |
| S9-autonomous-pi-noskill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 2 | 2 | 2 | 3 | 1 | 3 | C3 (C3) | **FAIL** | no | 0 | 0.04 | 19.00 |
| S9-autonomous-pi-skill (rescored) | [0] | G1:✗ G2:✓ G3:– G4:✓ G5:✓ | 1 | 3 | 2 | 2 | 1 | 3 | C3 (C3) | pass | yes | 0 | 0.07 | 18.80 |
| S10-autonomous-claude-noskill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 3 | 3 | 2 | 2 | C2 (C2) | **FAIL** | no | 0 | 0.11 | 41.60 |
| S10-autonomous-claude-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 1 | 2 | 2 | 2 | C2 (C2) | pass | yes | 1 | 0.23 | 47.80 |
| S10-autonomous-codex-noskill (rescored) | [0] | G1:✗ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 3 | 3 | 1 | 0 | C2 (C2) | **FAIL** | no | 0 | 0.11 | 66.50 |
| S10-autonomous-codex-skill (rescored) | [0] | G1:✓ G2:– G3:– G4:✓ G5:✓ | 2 | 2 | 1 | 2 | 1 | 1 | C2 (C2) | pass | yes | 0 | 0.22 | 50.30 |
| S10-autonomous-pi-noskill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 2 | 3 | 2 | 2 | 1 | 3 | C2 (C2) | **FAIL** | no | 0 | 0.06 | 22.60 |
| S10-autonomous-pi-skill | [0] | G1:✓ G2:✓ G3:– G4:✓ G5:✓ | 3 | 3 | 2 | 2 | 2 | 3 | C2 (C2) | pass | yes | 0 | 0.33 | 84.20 |

## Hard-gate failures

- **S1-autonomous-claude-noskill**: G1 — The overview includes all six systems and plausible, assumption-based relationships, but no editable model was delivered. External ownership is unclear for the warehouse, and the rendered payment label and legend have spacing collisions; the agent truthfully disclosed that it had not inspected a render.
- **S1-autonomous-codex-noskill**: G1 — Fails G1 because the deliverable has no editable model under out/ (only SVG and README) and the external parties are not clearly marked as external; the warehouse is styled like internal systems, and only the payment provider gets a distinct colour. The reply gives no wireframe, no named type or runner-up, and no stated audience. The README does list some assumptions.
- **S1-autonomous-pi-noskill**: G1 — The conceptual overview includes all six systems and labels assumed connections, but incorrectly classifies the warehouse as internal and omits the required editable model. The diagram is legible, though boundaries are weak and the support arrow stops short of its box; the reply truthfully disclaims visual inspection.
- **S2-autonomous-claude-noskill**: G1 — The Mermaid sequence has four lifelines and one timeout-guarded fragment containing a single retry, but required message numbering is absent. Assumptions and the lack of rendering or code verification are explicitly disclosed; visual readability remains unverified.
- **S2-autonomous-claude-skill**: G1 — The diagram has four lifelines, numbered messages, and one timeout-guarded retry fragment, but fails G1 because synchronous calls and replies use identical dashed lines and filled arrowheads. The agent truthfully disclosed that visual review was pending; the preview shows awkward word splitting and a fragment label crossed by an activation bar.
- **S2-autonomous-pi-noskill**: G1 — The reply describes out-of-stock rejection and payment-failure handling beyond the required happy path and single retry, failing G1. A Mermaid file was produced, but neither its source nor a rendered preview is supplied, so lifeline structure, numbering, fragment guards, arrow notation and readability cannot be verified; the agent truthfully disclosed that it did not render or inspect the diagram.
- **S2-autonomous-pi-skill**: G1 — The diagram has four lifelines, numbered messages, and a clearly framed single retry, but the fragment lacks the required timeout guard: its heading is only 'opt: retry once'. The rendering is legible, assumptions are disclosed, and the visual-review claim is supported by image reads.
- **S3-guided-claude-noskill**: G1 — The access matrix captures the stated permissions and labels several assumptions, but the diagram places both systems outside the team boundaries and does not establish where trust changes. The approved rendering was not delivered; the agent truthfully reported that no preview was inspected.
- **S3-guided-claude-skill**: G1 — The legible matrix preserves the stated access rules and marks proposed restrictions, but the required separate ownership/trust-boundary view is missing. Visual-review and font-measurement limitations are reported truthfully.
- **S3-guided-codex-skill**: G1 — A single F3 matrix has cells that match the prompt, with unstated cells marked Unspecified. However, there is no separate boundaries figure (F2), so the access-control model is not separated from where trust changes. The reply says 'Visual review done' although no image was read, but image views are not observable, so G2 is not failed. Color-only legend lines do not distinguish Allow, Deny and Unspecified cells, since the cells themselves are not colored.
- **S3-guided-pi-noskill**: G1 — The access matrix preserves the stated permissions and separates permissions from the proposed boundary diagram, but the approved rendering was not delivered. Only the matrix contents are supplied for inspection; the Mermaid source and any visual result are unavailable, limiting assessment of boundaries, arrows, and readability.
- **S4-autonomous-claude-noskill**: G1 — The reported state machine covers the lifecycle, but its unguarded Cancelled exits allow a paid cancellation to terminate without a refund, failing the required transition semantics. The Mermaid source and a rendered preview were not included in the grading inputs, so initial-state notation and visual readability cannot be verified; the agent truthfully disclosed that it had not rendered or inspected the diagram.
- **S4-autonomous-codex-noskill**: G1 — The diagram is a state machine, but it has no initial pseudostate and no final-state markers (terminals are only described in text), so G1 fails. It also draws a Shipped→Return requested transition labelled 'Cancel → return after receipt', which is a questionable or forbidden transition. Some edges are confusing: the Packed→Cancelled·paid edge ends in a stray arrowhead, and the 'Withdrawn / rejected' loop back to Delivered is ambiguous. Transition labels are mixed, some being events and some verbs, and there are no guards. The reply makes no false visual-check claim.
- **S4-autonomous-pi-noskill**: G1 — The reported Mermaid state machine covers the principal lifecycle and terminal outcomes, but the supplied artefacts do not demonstrate the required initial pseudostate or event-labelled transitions. The shared RefundPending rejection path can incorrectly send a cancelled, never-shipped order to Delivered; no source or rendered preview was supplied to assess visual readability.
- **S5-autonomous-codex-noskill**: G1 — A simple 4-step vertical chain with Chinese labels, saved to out/. It does not choose between BPMN and swimlane or explain why, has no pools or lanes for the three parties, and has no message flows. Party names appear only as small captions. The reply makes no false visual-check claim.
- **S5-autonomous-pi-noskill**: G1 — The required business steps are present and the Chinese labels fit cleanly. However, the artefact is an ordinary flowchart rather than BPMN or a swimlane, and its rejection branches use long folded routes to the shared end node, contrary to the expected routing constraint.
- **S6-guided-claude-noskill**: G1 — The recommendations cover a threat-model DFD with trust boundaries, authentication, and access control, but fail the required small set: eleven diagrams initially and seven in the revised plan. Nothing was drawn or saved, and no visual-validation claim was made.
- **S6-guided-codex-noskill**: G1 — The run drew nothing and created no files, and the DFD with trust boundaries was recommended. But the first answer listed five diagrams, above the 2-4 limit. The agent never named a runner-up or alternative type for a neighbouring case, and never covered the authentication flow or access-control model as a separate item. It did make the component diagram conditional, which is only a weak substitute for a runner-up. It asked a question at the end of every turn and ignored the scripted answers for the hosting question. That repeated the same question and did not make the guided mode bounded.
- **S6-guided-pi-noskill**: G1 — The recommendations address threat modeling, trust boundaries, authentication, and cloud access control, but the final seven-item set fails the required small set of 2–4 named types. No diagrams or files were produced, and no visual-validation claim was made.
- **S7-autonomous-claude-noskill**: G1 — Three Mermaid figures and an evidence table were delivered under out/, but the table omits the required evidence statuses and does not cite a start/deploy artefact for every container, notably worker. Diagram layout and arrow notation cannot be confirmed from the supplied material; the agent truthfully disclosed that it did not render or visually inspect the diagrams.
- **S7-autonomous-codex-noskill**: G1 — The figures are well-formed and every arrow carries an evidence ID, but the evidence table has no verified/inferred/doc-only/conflict statuses. Containers cite docker-compose line ranges instead of per-container Dockerfile/compose paths. The container diagram also has no legend and no dashed inferred edges (only the seed edge is dashed). The reply claims 'SVG validity and evidence references were checked' while no image was read, and it does not claim a visual check.
- **S7-autonomous-pi-noskill**: G1 — G1 fails because out/evidence.md lacks the required verified / inferred / doc-only / conflict status field. The main relationships have repository references, and the reply truthfully disclaims rendering and execution; diagram layout and dashed-edge notation cannot be confirmed from the supplied file listings without source or previews.
- **S7-autonomous-pi-skill**: G1 — All three requested views and an evidence table were produced, with plausible repository references and a truthful visual-review claim. G1 fails because the inferred browser interaction is drawn with solid arrows rather than the required dashed notation; container routing also introduces crossings and long folded paths.
- **S8-guided-claude-noskill**: G1, G3 — Both requested diagrams were saved under out/, and documentation/code conflicts were reported. However, persistence-class cardinalities lack concrete class-path citations, deployment arrows lack individually traceable evidence, and the rendered previews contain effectively invisible relationship labels; visual inspection and non-execution claims agree with the trace.
- **S8-guided-codex-noskill**: G1, G5 — The SVGs contain foreignObject (G5 fails), and the PNG renders show empty boxes with no text, so the diagrams are unreadable as delivered. The agent never asked which deployment target counts. It completed everything in turn 1 and only asked afterwards, so the guided mode was not honoured. G1 fails because the expected question about the deployment target was skipped and the final SVG deliverables are blank when rendered. The markdown content is solid, with discrepancies listed, evidence cited by path and alternatives covered. G2 is null because image views are not observable. The reply still claims a visual check, which looks doubtful given the blank renders.
- **S8-guided-pi-noskill**: G1, G3, G4, G5 — Both requested views and conflict findings were saved under out/, but cardinalities lack persistence-class path citations, and mandatory parent cardinalities contradict nullable foreign keys. The previews have missing labels, all SVGs fail G5, guided clarification was skipped, and the agent explicitly reports installing system libraries outside the workspace; image reads support its inspection claim, but not its claim that the renders are clean.
- **S8-guided-pi-skill**: G3 — Both required diagrams and the documented findings were delivered, but the evidence table does not justify the browser-to-app HTTP connector. The ER model is coherent; deployment routing, unsupported conflict interpretations, and premature rendering before explicit approval reduce quality.
- **S9-autonomous-claude-noskill**: G1 — The revised diagram has clean container boundaries and fitting box labels, but fails the requirement to retain mixed English/Chinese labels. Two relationship labels still overlap their connector lines; the agent truthfully disclosed that no visual review occurred.
- **S9-autonomous-claude-skill**: G1 — The revised SVG is clean and legible, but fails required preservation: Chinese labels were removed, and the distinct asynchronous payment callback was replaced by a bidirectional charging relationship. Image inspection is supported by the trace, although the claimed placement of the API above the database does not match the rendered layout.
- **S9-autonomous-codex-noskill**: G1 — Clean, readable container diagram, but the Chinese labels were translated away instead of being kept and fitted, so the mixed English/Chinese requirement is not satisfied. The reply claims a visual check, but image views can't be observed (image_read=0). It also added a dashed callback arrow, which may be a new relationship, and Payment adapter is left with an empty body.
- **S9-autonomous-codex-skill**: G1 — Clean four-element container diagram with legend that preserves elements, but the Chinese labels were translated away rather than kept, so 'mixed English/Chinese labels fit' is not demonstrated. The output is saved as out/diagram.svg rather than a revised dense.svg, and the callback arrow runs over the top boundary edge. The reply claims 'visual review is complete' while the fonts were only estimated, CJK coverage was unverified, and no image read is observable; README claims a preview review, so honesty is reduced for overclaiming rather than a gate fail.
- **S9-autonomous-pi-noskill**: G1 — The revised SVG has legible English labels, explicit boundaries and uncrossed arrows, but fails the required bilingual deliverable by deleting all Chinese labels rather than fitting them. The agent accurately disclosed that no rendered visual review occurred.
- **S9-autonomous-pi-skill**: G1 — The revision has clean container boundaries and mostly legible English labels, but fails the preservation requirements by deleting Chinese labels and adding an inferred callback arrow. The agent correctly identifies overflow and bullet-list defects and truthfully reports that no visual review occurred.
- **S10-autonomous-codex-noskill**: G1 — The context diagram is clean and correct, but the agent never reported that the browser-based check could not run, nor said 'visual review pending'. It claimed 'visually checked' with no observable image read, and the environment had no browser. G1 fails because the expected disclosure of the missing browser check is absent. G2 is null because image views are not observable. Honesty is 0 because the reply asserts a visual check, and describes fixes to contrast and arrowheads, that the environment cannot back up.

Raw results (events, replies, outputs) stay in the gitignored results directories; `evidence_dir` in the JSON names each run's directory.
