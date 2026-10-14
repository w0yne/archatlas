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

The first three-host comparison is complete for skill revision 3847acb and did not meet the release gate. It does not certify the current revision: targeted retesting and release certification are pending. [Read the retained first-run report](/evaluation-report.txt).

Its published summary reports skill wins in 6/10, 7/10 and 8/10 scenarios for Claude Code, Codex and Pi. Each host also has a dimension median below 2, and not every hard gate passes. These are historical reported figures, not a certification of subsequent fixes. Some summary/per-run grading entries require reconciliation against retained evidence; this page does not silently regrade them.

Current samples have been regenerated from templates. Synchronization and geometry checks do not certify full notation conformance. Current-revision retests must record the tested commit, host/model versions, retained outputs, hard gates and per-dimension results; a successful build alone cannot close the release gate.
