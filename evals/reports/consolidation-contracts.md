# Consolidation contract regression — scenario version 2

This is a deterministic contract regression record, **not a live-agent quality score**.
No Claude/Codex/Pi comparison, grader run, cost comparison or benchmark improvement is
claimed. Historical reports remain unchanged and bound to their recorded revisions.

Scope: existing S6 security-review routing and new held-out S11/S12 prompts, plus shared
sample contracts. The prompts exercise modified approvals, revoked citations, unsupported
AS delegation, and separation of generic deployment, AWS implementation and networking.

Validation command:

```sh
python -m pytest -q evals/tests/test_ai_contracts.py tests/unit/test_samples.py
```

The targeted run passed all 10 tests. It checks F1→E1/F2→D2/G2→G1 routing, explicit
security choices, manifest coverage (25 core + 4 variants), bilingual identity/topology,
central semantic projections, policy/RACI table agreement, API-produced ingestion,
no unapproved execution or unknown-outcome closure shortcut, and the common token
exchange request before allow/deny alternatives. Authored/public bytes must match.

These assertions check the documented design contract; they do not demonstrate that an
implemented application enforces it, nor that an agent can reproduce the diagrams.
Live S11/S12 runs remain available through the existing isolated evaluation runner when
an authenticated host configuration is supplied. They are needed before making new
agent-quality claims, not to reinterpret or overwrite the historical score reports.
