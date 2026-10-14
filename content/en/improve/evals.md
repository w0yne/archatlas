---
title: Evaluate changes
---
# Evaluate changes

A valid image is not necessarily a useful architecture view. Evaluate discovery, meaning, interaction and output separately.

## Small comparisons, fixed conditions

Compare no skill, the candidate skill, and the previous revision when available. Keep model, prompt, repository revision and permissions fixed. Use held-out examples; repeat unstable cases rather than every scenario indiscriminately.

## What to inspect

- **Semantic fidelity:** the view answers the question without invented relationships.
- **Structure and flow:** boundaries, peers, direction and step order make sense.
- **Readability:** no clipped labels, missing glyphs or misleading connector overlaps.
- **Interaction:** the chosen mode is respected; missing answers are not approvals.
- **Honesty:** evidence and visual-review status match what actually happened.

## Hard failures

Required content omitted, invented repository evidence, invalid/active-content SVG, unauthorized side effects, or a visual-pass claim without image review are failures regardless of a total score.

## Cross-agent release checks

Run clean installation and representative tasks on Claude Code, Codex and Pi, in autonomous and guided modes. Include EN/Chinese labels and missing-browser behavior. Confirm the skill was loaded using host evidence, not just the final answer.

## Keep CI safe

Pull-request checks need no model credentials. Paid model evaluations belong in trusted, manually approved, budgeted jobs. Do not expose secrets to untrusted contributions or commit private model transcripts.

The first release evaluation is pending; this scaffold does not display invented benchmark scores.
