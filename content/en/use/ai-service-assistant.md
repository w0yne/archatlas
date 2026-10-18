---
title: 'Enterprise Service Assistant: 29 architecture views'
sidebar: false
aside: false
---

# Enterprise Service Assistant: 29 architecture views

25 core views and four named variants, with 29 original hand-authored SVGs per language. Shared facts and explicit illustrative assumptions define one fictional system; no deployment or measured performance is claimed.

[Assumptions and rules](/use/ai-service-assistant-assumptions) · [Manifest](/samples/ai-service-assistant/manifest.json) · [Glossary](/samples/ai-service-assistant/glossary.json)

<section class="sample-view" id="view-a1">

## A1 · Business capability map

![A1 · Enterprise Service Assistant](/samples/ai-service-assistant/A1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/A1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

What can the organisation do, independent of who or what does it, and where should it invest?

<section class="sample-view" id="view-a2">

## A2 · Value stream (business architecture)

![A2 · Enterprise Service Assistant](/samples/ai-service-assistant/A2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/A2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Which stages does a stakeholder pass through, from trigger to delivered value, and which capabilities enable each stage?

<section class="sample-view" id="view-a5">

## A5 · Business process diagram (BPMN)

![A5 · Enterprise Service Assistant](/samples/ai-service-assistant/A5/en/diagram.svg)

[SVG](/samples/ai-service-assistant/A5/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A5/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

How does a business case run from start to end, who does each step, where does it branch, and what passes between participants?

<section class="sample-view" id="view-a6">

## A6 · Customer or user journey map

![A6 · Enterprise Service Assistant](/samples/ai-service-assistant/A6/en/diagram.svg)

[SVG](/samples/ai-service-assistant/A6/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A6/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

The persona, emotions and improvement opportunities are illustrative, not user research. Existing steward/operator roles own the suggested improvements without receiving new content permissions.

<section class="sample-view" id="view-a8">

## A8 · Target architecture and transition roadmap

![A8 · Enterprise Service Assistant](/samples/ai-service-assistant/A8/en/diagram.svg)

[SVG](/samples/ai-service-assistant/A8/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/A8/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Read-only answers, approved writes and evaluation-gated changes are illustrative transition plateaus, not committed dates. Each work package introduces only the capabilities required for its next plateau.

<section class="sample-view" id="view-b2">

## B2 · User story map

![B2 · Enterprise Service Assistant](/samples/ai-service-assistant/B2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/B2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/B2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

What does the user do end to end, what is the smallest useful first release, and how are later releases sliced?

<section class="sample-view" id="view-c1">

## C1 · Application landscape

![C1 · Enterprise Service Assistant](/samples/ai-service-assistant/C1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Which applications exist in the estate, who owns them, what state are they in, and how do they depend on each other?

<section class="sample-view" id="view-c2">

## C2 · System context diagram (C4 model level 1)

![C2 · Enterprise Service Assistant](/samples/ai-service-assistant/C2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

What is the software system, who uses it, and which other systems does it depend on?

<section class="sample-view" id="view-c3">

## C3 · Container diagram (C4 model level 2)

![C3 · Enterprise Service Assistant](/samples/ai-service-assistant/C3/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C3/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C3/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Six runtime units, five stores/queues and the model dependency. API is the sole job producer; workers poll, fetch authorized source versions and create embeddings. All original node and edge identities are retained, with two added dependencies.

<section class="sample-view" id="view-c4">

## C4 · Component diagram (C4 model level 3)

![C4 · Enterprise Service Assistant](/samples/ai-service-assistant/C4/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C4/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C4/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

P-plan, P-retrieve and P-compose are projected as unnumbered logical modules inside C-agent; no new runtime service is added. Module names and responsibilities are illustrative, not source-code observations.

<section class="sample-view" id="view-c5">

## C5 · Logical architecture diagram

![C5 · Enterprise Service Assistant](/samples/ai-service-assistant/C5/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C5/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C5/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Seen by responsibility and without technology choices, which modules and interfaces must the system have?

<section class="sample-view" id="view-c6">

## C6 · Integration and interface diagram

![C6 · Enterprise Service Assistant](/samples/ai-service-assistant/C6/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C6/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C6/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Interface authentication, producer/consumer direction, bounded retries, ownership and capacity are illustrative contracts in AS-interfaces. Queue delivery is polled by the worker, not broker-initiated push.

<section class="sample-view" id="view-c7">

## C7 · Bounded context map (DDD)

![C7 · Enterprise Service Assistant](/samples/ai-service-assistant/C7/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C7/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C7/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Each named system is treated as an opaque bounded context with an illustrative team/model contract. DDD ACL means anti-corruption layer; document ACL means access-control list. CF covers protocol adoption, never authority from model output.

<section class="sample-view" id="view-d1">

## D1 · Entity-relationship diagram

![D1 · Enterprise Service Assistant](/samples/ai-service-assistant/D1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/D1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/D1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

A logical entity subset, not complete DDL. Tenant-owned PK/FKs include tenant scope; approval binds the idempotency tuple as well as subject, tool, hash and expiry. Messages/citations remain part of the conversation aggregate.

<section class="sample-view" id="view-d2">

## D2 · Data flow diagram (DFD)

![D2 · Enterprise Service Assistant](/samples/ai-service-assistant/D2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/D2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/D2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Tenant/ACL filtering is explicit before retrieval and current access is checked again when a citation is opened. This logical DFD covers knowledge answering; ticket writes and evaluation are separate views.

<section class="sample-view" id="view-d3">

## D3 · Data lineage and ownership map

![D3 · Enterprise Service Assistant](/samples/ai-service-assistant/D3/en/diagram.svg)

[SVG](/samples/ai-service-assistant/D3/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/D3/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Steward accountability, technical custody and tenant-confidential versus deidentified classification are specified in AS-data. Ownership is not a read grant, and derived chunks retain source ACL restrictions.

<section class="sample-view" id="view-e1">

## E1 · Sequence diagram

![E1 · Enterprise Service Assistant](/samples/ai-service-assistant/E1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/E1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/E1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

For one scenario, in what order do the participants exchange which messages?

<section class="sample-view" id="view-e2">

## E2 · Activity diagram or flowchart

![E2 · Enterprise Service Assistant](/samples/ai-service-assistant/E2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/E2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/E2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

UML activity: one start, guarded valid/else decision and named outcomes. Approval, current permission and idempotent execution remain distinct. Ambiguous timeouts use key-based reconciliation under AS-request.

<section class="sample-view" id="view-e3">

## E3 · State machine diagram

![E3 · Enterprise Service Assistant](/samples/ai-service-assistant/E3/en/diagram.svg)

[SVG](/samples/ai-service-assistant/E3/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/E3/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

One request in DS-app: unapproved, approved, executing, unknown, recorded, refused and closed. Unknown outcomes remain held after bounded reconciliation; they do not authorize a fresh write.

<section class="sample-view" id="view-e4">

## E4 · Swimlane or cross-functional flowchart

![E4 · Enterprise Service Assistant](/samples/ai-service-assistant/E4/en/diagram.svg)

[SVG](/samples/ai-service-assistant/E4/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/E4/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

In one process, which role or system performs each step, and where are the hand-offs?

<section class="sample-view" id="view-f1">

## F1 · Authentication and authorization flow

![F1 · Enterprise Service Assistant](/samples/ai-service-assistant/F1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/F1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/F1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

The exchange request is common to both allow and deny paths. Agent is the authenticated exchange client. Tool proof binds issuer, audience, subject, actor, tenant and scopes; verification never replaces current authorization. AS delegation support is an implementation prerequisite.

<section class="sample-view" id="view-f2">

## F2 · Threat-model data-flow diagram with trust boundaries

![F2 · Enterprise Service Assistant](/samples/ai-service-assistant/F2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/F2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/F2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

DF identifiers trace data flows to threat hypotheses; they are not message order. DF-6 abstracts proof delivery through Agent (F1), and DF-4 reads current approval through the BFF. Proposed controls still require implementation validation.

<section class="sample-view" id="view-f3">

## F3 · Access-control model

![F3 · Enterprise Service Assistant](/samples/ai-service-assistant/F3/en/diagram.svg)

[SVG](/samples/ai-service-assistant/F3/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/F3/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Explicit grants are unioned, then intersected with current tenant/resource constraints; policy denial wins. Steward reads require ACL permission. Operator rights never automatically grant tenant content access.

<section class="sample-view" id="view-g1-aws">

## G1-AWS · Cloud infrastructure architecture

![G1-AWS · Enterprise Service Assistant](/samples/ai-service-assistant/G1-AWS/en/diagram.svg)

[SVG](/samples/ai-service-assistant/G1-AWS/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/G1-AWS/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

The AWS implementation variant is the first G1 illustration. Application services span two AZs; Aurora managed storage spans three; OpenSearch uses two-AZ zone awareness, not Standby. Regional managed services are outside customer subnets, CloudFront is global.

<section class="sample-view" id="view-g1-generic">

## G1-generic · Deployment & cloud architecture

![G1-generic · Enterprise Service Assistant](/samples/ai-service-assistant/G1-generic/en/diagram.svg)

[SVG](/samples/ai-service-assistant/G1-generic/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/G1-generic/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Vendor-neutral hosting allocation of the same frozen deployment, not a second architecture or a relabelled AWS drawing. Six runtime units and five stores retain their IDs. It complements the G1 AWS headline.

<section class="sample-view" id="view-g3">

## G3 · Network topology and connectivity view

![G3 · Enterprise Service Assistant](/samples/ai-service-assistant/G3/en/diagram.svg)

[SVG](/samples/ai-service-assistant/G3/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/G3/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

A logical reachability view, with transit, DNS, TLS/443, private endpoints, per-AZ NAT and SG/NACL returns specified in AS-network. The fictional address plan and rules are not an observed deployment.

<section class="sample-view" id="view-g4">

## G4 · CI/CD and deployment pipeline

![G4 · Enterprise Service Assistant](/samples/ai-service-assistant/G4/en/diagram.svg)

[SVG](/samples/ai-service-assistant/G4/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/G4/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Versioned prompt/model bundle, immutable digest, offline gates, steward approval and operator release. Promote the same bundle through staging and a 5% canary; recover by compatible configuration pointer, not automatic database rollback.

<section class="sample-view" id="view-h1">

## H1 · RACI matrix

![H1 · Enterprise Service Assistant](/samples/ai-service-assistant/H1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/H1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/H1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Illustrative governance: one A and at least one R per scoped activity. Steward is accountable for release/recovery approval; operator executes the scoped workflow. Accountability grants no data-plane permission.

<section class="sample-view" id="view-h2">

## H2 · Observability view

![H2 · Enterprise Service Assistant](/samples/ai-service-assistant/H2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/H2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/H2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Redact before export. Illustrative SLO, cost targets, bounded delivery, sampling/retention and CloudWatch→SNS→operator response are specified in AS-observe; none are measured guarantees.

