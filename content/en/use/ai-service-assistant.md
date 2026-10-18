---
title: 'Enterprise Service Assistant: seven views'
sidebar: false
aside: false
---

# Enterprise Service Assistant: seven views

A fictional teaching design. Seven hand-authored views per language share one versioned fact source. This is an isolated documentation candidate, not an implementation or benchmark. The AWS variant is G1’s headline; a separate vendor-neutral G1 sample is deferred. [Manifest](/samples/ai-service-assistant/manifest.json).

<section class="sample-view" id="view-c2">

## C2

![C2 · Enterprise Service Assistant](/samples/ai-service-assistant/C2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

One owned system and its direct neighbours. Arrows mean initiator to dependency; no protocols or internal stores appear at this level. People are roles, not real individuals. All three tenants are synthetic.

<section class="sample-view" id="view-c3">

## C3

![C3 · Enterprise Service Assistant](/samples/ai-service-assistant/C3/en/diagram.svg)

[SVG](/samples/ai-service-assistant/C3/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/C3/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Focused internal container view: six runtime units and five stores/queues, plus the external model dependency. The three other external interfaces (IdP, source repository and Service Desk) remain explicit in C2/F1; ingestion reaches the source, and Tools reaches Service Desk. The Agent includes a logical model gateway, not a seventh service. Only key dependencies are drawn: C-api also approves feedback export to DS-eval, C-ingest produces version jobs and consumes Q-ingest, and C-eval writes gated configuration proposals to DS-eval. Retrieval and citation access enforce current tenant/ACL policy. MCP means Model Context Protocol.

<section class="sample-view" id="view-e1">

## E1

![E1 · Enterprise Service Assistant](/samples/ai-service-assistant/E1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/E1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/E1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

The employee approves only their own currently permitted action. The BFF stores tenant, subject, tool, canonical-parameter hash, expiry and idempotency key. Tools fetches that binding and rechecks current policy immediately before the write; rejected, expired or changed drafts do not reach Service Desk. The request intent is persisted before calling the idempotent connector. On ambiguous timeouts, reconcile by key. F1 supplies the delegated-token prerequisites. The UI presents the final result via the BFF; that return hop is omitted here.

<section class="sample-view" id="view-f1">

## F1

![F1 · Enterprise Service Assistant](/samples/ai-service-assistant/F1/en/diagram.svg)

[SVG](/samples/ai-service-assistant/F1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/F1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Downstream delegation after BFF authorization-code sign-in with PKCE, state and nonce validation. The BFF holds ID/access tokens server-side and exposes only a secure session cookie. The AS explicitly issues an agent-scoped subject token; the Agent authenticates as agent-client to exchange it. The tool token is issued by enterprise-as for mcp-tool-gateway, with employee subject, agent actor, verified tenant, allowed scopes and short expiry. Signature, issuer, audience and expiry validation precede policy and approval enforcement. The AS delegation capability and Service Desk connector scopes are unverified teaching assumptions; if unsupported, redesign instead of forwarding a token with the wrong audience. Solid arrows are back-channel requests, dashed arrows replies; browser redirects belong to the prerequisite sign-in, not this figure.

<section class="sample-view" id="view-g1-aws">

## G1-AWS

![G1-AWS · Enterprise Service Assistant](/samples/ai-service-assistant/G1-AWS/en/diagram.svg)

[SVG](/samples/ai-service-assistant/G1-AWS/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/G1-AWS/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

AWS implementation variant G2, used once as the G1 headline sample. The core G1 recipe stays vendor-neutral; a separate neutral sample is scheduled for P2b. ALB and each ECS application service span two AZs; C-ingest and C-eval are separate job identities scheduled in either AZ. Aurora has a cross-AZ reader, while its managed storage spans three AZs. OpenSearch uses two-AZ zone awareness and replicas, not Multi-AZ with Standby. CloudFront is global; S3, SQS, Bedrock, KMS, CloudWatch and Secrets Manager are regional services outside customer subnets. Check model availability, quotas and endpoint routing before implementation. Trade-offs: managed ECS avoids a cluster control plane; the search index adds operational cost; a single region avoids multi-region complexity but supplies no regional disaster-recovery guarantee. Generic original shapes, no vendor artwork.

<section class="sample-view" id="view-d2">

## D2

![D2 · Enterprise Service Assistant](/samples/ai-service-assistant/D2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/D2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/D2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Level 1 decomposition of the knowledge-answer function, using Gane–Sarson symbols: rounded process, open-ended store and external rectangle. Arrow labels name data, not control steps. P-ingest belongs to C-ingest; retrieval/composition to C-agent; citation enforcement to C-api. The authorization filters derive from verified session context, never a user-selected tenant. Source ACLs accompany every version and chunk; current policy is enforced again when citations are opened. This focused function excludes ticket actions and the evaluation loop; it is not a claimed decomposition of the whole C2 system. Inputs are source+ACL and employee query+identity, plus model drafts; outputs are grounded prompts and authorized answers/citations. DS-app receives audit records.

<section class="sample-view" id="view-f2">

## F2

![F2 · Enterprise Service Assistant](/samples/ai-service-assistant/F2/en/diagram.svg)

[SVG](/samples/ai-service-assistant/F2/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/F2/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

</section>

Focused ticket-write threat DFD; DF IDs are references, not message order. TB-1 marks untrusted content, TB-2 verified tenant/approval authority, TB-3 enforced tool authority; Service Desk is external. DF-6 abstracts proof delivery through the Agent; it does not imply a direct AS-to-gateway HTTP call (see F1). DF-4 is the logical current-approval record, obtained through the BFF API. Proposed controls and threat hypotheses are recorded below; none are claimed as implemented or validated. Tenant isolation is also required on retrieval and citation paths (D2).

| Threat / flow | Hypothesis and impact | Proposed response | Owner / validation still required |
|---|---|---|---|
| T1 · DF-1 / TB-1 | Prompt injection requests an unauthorized tool | Model output has no authority; allowlist three tools | Agent owner / malicious-document test |
| T2 · DF-2–5 / TB-2 | Draft changed or replayed after approval | Bind tenant, subject, canonical hash, expiry and idempotency key; reauthorize | API owner / changed hash, expiry and tenant rejection tests |
| T3 · DF-6 / TB-3 | Confused deputy uses wrong audience or actor | Verify AS signature, issuer, audience, actor, tenant and scopes; deny before connector | Identity owner / wrong-audience and cross-tenant tests |
| T4 · DF-7–8 | Timeout duplicates a write | Persist intent, connector idempotency and lookup by key | Tools owner / ambiguous-timeout reconciliation test |
| T5 · DF-4 / DS-app | Operator or model accesses approval records directly | Scoped service identities; BFF policy gate; audit and redact | Platform owner / IAM and log-content review |

All entries are hypotheses with proposed responses; validation evidence **has not been collected**.

## Shared invariants

- **I-tenant**: Derive tenant and subject from the verified session. Enforce current tenant/ACL filters before retrieval and check current access again when a citation is opened. Never share content across tenants.
- **I-approval**: Approval binds tenant, subject, tool, canonical-parameter SHA-256 hash, expiry and idempotency key. Approval is a stored record, not model text. Reauthorize immediately before execution; reject stale, modified or cross-tenant requests.
- **I-authority**: Model output, retrieved documents and guardrails never grant authority. Guardrails filter content; deterministic BFF and gateway checks enforce permissions.
- **I-delegation**: The BFF is the confidential OIDC client (authorization code + PKCE; verifier stays server-side). The Agent Service is the authenticated token-exchange client. The enterprise AS must explicitly support the required constrained delegation (RFC 8693); this is an assumption, not a generic IdP promise.
- **I-tokens**: AS issues BFF access token aud=application-api, sub=employee, and a downscoped agent subject token aud=agent-service. Agent exchanges only that valid subject token, authenticating as agent-client; AS issues tool token iss=enterprise-as, aud=mcp-tool-gateway, sub=employee, act=agent-client, tenant, permitted scopes and short expiry. Tools verifies signature/issuer/audience/expiry, delegation actor, tenant and current policy; reject before Service Desk on any mismatch. Tokens for Service Desk are separate scoped connector credentials, never forwarded model or BFF tokens.
- **I-idempotency**: Persist execution intent and idempotency key before sending. Service Desk is assumed to support idempotent ticket creation by that key. After ambiguous timeouts reconcile by key; never blindly repeat a non-idempotent write.
- **I-ingest**: Version documents with source ACLs; retries are bounded and failures go to DLQ. Only completely indexed versions become searchable; revocation/tombstone updates invalidate search and citation access.
- **I-eval**: Feedback starts in DS-app. A steward approves deidentified/synthetic export to DS-eval. Offline C-eval uses an evaluation-only identity and versioned prompt/model/dataset; no production tool writes. Gate promotions on quality, safety, latency and token-cost measures without claiming measured scores.
- **I-operator**: Operators see service health and redacted telemetry, not tenant content by default. Logs omit raw tokens and document text. Admin changes are audited and do not bypass data-plane checks.
- **I-bounds**: Exactly three tools: catalogue.lookup, ticket.read, ticket.create. Write requests require the initiating employee approval within current permissions. No arbitrary scripts, procurement, autonomous refunds or unbounded agent loops.
