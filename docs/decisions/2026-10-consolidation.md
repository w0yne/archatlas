# Consolidate entry points; preserve methods and stable identities

Status: branch candidate, October 2026. This is documentation and examples, not an
implementation of the fictional application. Historical evaluation results stay tied
to their original revisions; no new quality-score improvement is claimed.

## Problem and decision

Forty equally prominent entries make initial selection harder than necessary. Some
share notation or answer adjacent questions; others organize several views rather than
answer a common software-system question. This is editorial judgement supported by
public architecture guidance, not a usage survey or a measured popularity ranking.

| Role | Codes and targets |
|---|---|
| 25 core entries | A1 A2 A5 A6 A8 B2 C1 C2 C3 C4 C5 C6 C7 D1 D2 D3 E1 E2 E3 F3 G1 G3 G4 H1 H2 |
| 10 named variants | A3→C2, A4→B2, A7→C5, A9→A2, B4→C2, C8→C4, E4→E2, F1→E1, F2→D2, G2→G1 |
| 5 method references | B1 B3 H3 I1 I2 |

Start with **C2 → C3 → one key E1 → G1**, then add views for specific security,
operational or business questions. This is not a requirement to draw 25 diagrams.
F1 identity/delegation and F2 threat modelling remain prominent with their own recipes,
mandatory checks and independent samples. E4 swimlanes will also get a separate sample.
A9 Lean value-stream mapping and A4 role/activity coverage are editorially grouped,
not equated with the A2 and B2 methods. BPMN stays distinct from informal swimlanes;
network reachability from deployment; ER from DFD and lineage; RACI from permissions.

G1 becomes **Deployment & cloud architecture**. Its core recipe remains vendor-neutral
hosting and software allocation; the first sample is explicitly the G2 AWS implementation
variant. Do not duplicate an AWS drawing and relabel it vendor-neutral.

## Shared fictional scenario

The Enterprise Service Assistant answers from authorized tenant knowledge and reads
service information. Ticket creation requires human approval. Three synthetic tenants,
six runtime units and three tools give a medium-complexity teaching example. Stores,
queues, external systems and managed infrastructure are counted separately. It excludes
arbitrary scripts, model training, multi-cloud and multi-region active-active operation.

`examples/ai-service-assistant/scenario.json` freezes stable IDs, bilingual labels,
responsibilities, flows, deployment assumptions and security invariants. Every view
maps projected nodes and rules back to that source. The model gateway is a logical
component inside the Agent Service, not a seventh runtime unit.

Enforce tenant/ACL rules before retrieval **and** when opening citations. Approval binds
tenant, subject, tool, canonical-parameter hash, expiry and idempotency key. Reauthorize
immediately before execution. Model output, retrieved content and guardrails grant no
authority. The BFF is the confidential OIDC authorization-code + PKCE client; the Agent
is the authenticated token-exchange client. F1 states issuer, audience, subject, actor,
scopes, verification, enforcement and refusal paths. Constrained AS delegation and
Service Desk idempotency are explicit unverified assumptions. Unsupported delegation
requires redesign, not forwarding a token to a recipient with the wrong audience.

A single supported AWS region and two application AZs are assumed. Aurora storage's
service-managed three-AZ replication is distinct from application placement. OpenSearch
uses two-AZ zone awareness and replicas, not Multi-AZ with Standby. S3, SQS, Bedrock,
KMS, CloudWatch and Secrets Manager are regional services outside customer subnets;
CloudFront is global. Region/model availability, quotas, endpoint routing and permitted
data handling need implementation validation. No measured SLA, recovery time, cost or
benchmark is implied by the drawing.

## Generation, packaging and compatibility

The explicit manifest lists seven hand-authored views per language: C2, C3, E1, F1,
G1-AWS (G2, also G1 headline), D2 and F2. A separate vendor-neutral G1 sample is deferred
to the next sample batch. The existing shop examples remain small regression fixtures.

`catalogRole` and `target` are separate from `status: draft|reviewed`. All 40 stable codes
remain valid. The 15 non-core EN/ZH pages retain their original section anchors and
historical downloads with plain target links. Core variant anchors carry the variant's
own recipe and checks. Compatibility needs no JavaScript or server-side 301. Default
catalogue/sidebar discovery shows 25 entries; explicit codes and aliases remain supported.

`tools/build_samples.py` checks and copies hand-authored SVG byte-for-byte, never sends
it through automatic layout, and does not erase old assets. Model schema and layout
engine are unchanged. Nested sample discovery uses a manifest instead of a one-level
`examples/*/diagram.json` glob. Skill bundles include the same facts, manifest and artwork.
The site candidate is built and reviewed in isolation before any public-site promotion.

Geometry checks do not prove semantic correctness or a completed security assessment.
The F2 threat register records hypotheses, proposed controls, owners and validation still
required. Local sample checks are not a new full multi-host evaluation certification.

## Remaining scope

- Complete remaining core examples, E4 and a separate vendor-neutral G1 from shared facts.
- Update affected evaluation inputs with held-out variants; preserve old revision scores.
- Complete independent review and release-level checks before public-site publication.
- Consolidate review feedback once: fix required corrections, record optional improvements,
  and avoid unbounded cosmetic redraws.

## Public sources and limits

- [C4 diagrams](https://c4model.com/diagrams): context and container suffice for many
  teams; further views should answer specific questions.
- [arc42 overview](https://arc42.org/overview): context, building blocks, runtime and
  deployment are separate perspectives.
- [C4 deployment](https://c4model.com/diagrams/deployment) and
  [arc42 deployment view](https://docs.arc42.org/section-7/): software-to-host allocation.
- [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/) and
  [UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/): preserve selected formal notation.
- [OWASP threat modelling](https://owasp.org/www-community/Threat_Modeling): modelling
  supports identification, response and validation; a diagram does not finish the loop.
- [RFC 8693](https://www.rfc-editor.org/rfc/rfc8693) and
  [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700): explicit delegation and current
  OAuth security guidance; standards do not prove a chosen AS supports the required flow.
- [AWS Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/welcome.html):
  security, evaluation, operations and cost all belong in the design.
- [Aurora storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html)
  and [OpenSearch multiple AZs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html):
  distinguish managed durability and selected zone-aware modes.

All figures are original generic SVG shapes, with no customer facts or proprietary
artwork. These sources support reasoning, not usage-frequency or performance claims.
