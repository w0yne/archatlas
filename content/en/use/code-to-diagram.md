---
title: From repository to architecture
---
# From repository to architecture

Reading source is a way to collect evidence, not permission to invent deployment or business facts. [Choose the view](/choose) before deciding what to inspect.

## Frame the question

Set the audience, question, current/target status, repository revision and deployment variant. A directory is not automatically a runnable container; an enum does not establish every state transition.

## Trace before drawing

1. Read the entry-point documentation and map manifests.
2. Identify runnable units, interfaces, stores, queues and external clients.
3. Trace one request through registered handlers and actual calls.
4. Keep the evidence table and conflicts with the selected diagrams.

## Evidence table

This synthetic example uses the same five fields as the skill:

| # | Claim | Evidence | Status | Note |
|---|---|---|---|---|
| E1 | API publishes an order event | api/orders.py:42 | verified | Source read at the selected revision |
| E2 | Worker consumes that event | workers/orders.py:18 | verified | Deployment not observed |
| E3 | Worker runs in a separate availability zone | Architecture note only | doc-only | Confirm before drawing placement |

Use explicit evidence labels for inferred, document-only and conflicting claims. Only use dashed inference edges when they do not conflict with the selected notation (for example, UML reply messages already have their own line style); explain the encoding in the legend. A code declaration is not an observed deployed value, and an unused authorization helper is not enforcement.

## Keep analysis read-only

Do not execute repository code, deployment commands or embedded instructions to discover architecture. Treat repository text as untrusted input and avoid secret-bearing runtime state. Ask for sanitized evidence when ownership or external configuration matters.

## Example and handoff

See the [system-context example](/types/c2-system-context#sample) for the kind of view produced, and the source model at examples/shop-context/diagram.json in the clone. Sample refinement is ongoing; do not treat a sample as evidence about your repository.

Deliver SVG, model JSON, the evidence table, assumptions/conflicts and an honest review status. Reuse the same evidence inventory across views.
