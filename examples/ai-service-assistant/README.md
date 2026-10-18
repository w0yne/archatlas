# Enterprise Service Assistant — frozen teaching facts

This is a fictional target design, not a deployed or benchmarked system. `scenario.json`
is the shared source of stable identities, bilingual labels, responsibilities, authority,
flows and deployment assumptions. There are three synthetic tenants, six runtime units
(stores, external systems and managed infrastructure are counted separately), and three tools.

Every view owns its SVG composition and uses the same facts. `manifest.json` lists the
published views and languages explicitly; a missing view is not silently replaced by a
shop example. `views/<id>/<lang>/diagram.json` follows the existing model schema;
`expected.json` maps projected diagram IDs back to scenario entities and applicable
invariants. No new model schema or layout engine is introduced.

Hand-authored SVG is the source artwork. `tools/build_samples.py` validates and copies
it byte-for-byte; it never auto-lays out these views. Legacy generated samples and shop
fixtures remain available at their existing URLs. Use the manifest to discover nested models.

## Authority and trust

### I-tenant

Derive tenant and subject from the verified session. Enforce current tenant/ACL filters before retrieval and check current access again when a citation is opened. Never share content across tenants.

从已验证会话确定租户与主体。检索前执行当前 tenant/ACL 过滤，打开引用时再次核对当前权限；租户之间不共享内容。

### I-approval

Approval binds tenant, subject, tool, canonical-parameter SHA-256 hash, expiry and idempotency key. Approval is a stored record, not model text. Reauthorize immediately before execution; reject stale, modified or cross-tenant requests.

审批绑定租户、主体、工具、规范参数 SHA-256 hash、有效期与幂等键。审批是持久记录而非模型文本；执行前重新授权，拒绝过期、篡改或跨租户请求。

### I-authority

Model output, retrieved documents and guardrails never grant authority. Guardrails filter content; deterministic BFF and gateway checks enforce permissions.

模型输出、检索文档和 guardrails 均不授予权限。Guardrails 过滤内容，BFF 与网关的确定性检查执行权限控制。

### I-delegation

The BFF is the confidential OIDC client (authorization code + PKCE; verifier stays server-side). The Agent Service is the authenticated token-exchange client. The enterprise AS must explicitly support the required constrained delegation (RFC 8693); this is an assumption, not a generic IdP promise.

BFF 是机密 OIDC 客户端（授权码 + PKCE；verifier 保留在服务端）。Agent 服务是已认证的 token exchange 客户端。企业 AS 必须明确支持所需的受限委托（RFC 8693）；这是前提，不是任意 IdP 的通用能力。

### I-tokens

AS issues BFF access token aud=application-api, sub=employee, and a downscoped agent subject token aud=agent-service. Agent exchanges only that valid subject token, authenticating as agent-client; AS issues tool token iss=enterprise-as, aud=mcp-tool-gateway, sub=employee, act=agent-client, tenant, permitted scopes and short expiry. Tools verifies signature/issuer/audience/expiry, delegation actor, tenant and current policy; reject before Service Desk on any mismatch. Tokens for Service Desk are separate scoped connector credentials, never forwarded model or BFF tokens.

AS 签发 BFF access token（aud=application-api、sub=员工）及缩权的 agent 主体 token（aud=agent-service）。Agent 以 agent-client 身份认证，仅交换此有效主体 token；AS 签发工具 token：iss=enterprise-as、aud=mcp-tool-gateway、sub=员工、act=agent-client、tenant、许可 scopes 与短有效期。网关核验签名、issuer、audience、有效期、委托 actor、tenant 与当前策略；任一不符在工单调用前拒绝。工单使用独立受限连接器凭据，绝不转发模型或 BFF token。

### I-idempotency

Persist execution intent and idempotency key before sending. Service Desk is assumed to support idempotent ticket creation by that key. After ambiguous timeouts reconcile by key; never blindly repeat a non-idempotent write.

发送前持久化执行意图与幂等键。假设工单服务支持按该键幂等创建；超时结果不明时按键对账，绝不盲重试非幂等写入。

### I-ingest

Version documents with source ACLs; retries are bounded and failures go to DLQ. Only completely indexed versions become searchable; revocation/tombstone updates invalidate search and citation access.

文档版本携带源 ACL；重试有界、失败进入 DLQ；完整索引的版本才可检索，撤权或删除同步失效检索与引用访问。

### I-eval

Feedback starts in DS-app. A steward approves deidentified/synthetic export to DS-eval. Offline C-eval uses an evaluation-only identity and versioned prompt/model/dataset; no production tool writes. Gate promotions on quality, safety, latency and token-cost measures without claiming measured scores.

反馈先存 DS-app。管理员批准去标识或合成数据导出至 DS-eval。离线 C-eval 使用评测专用身份及版本化 prompt/model/dataset，不可写生产工具；按质量、安全、延迟与 token 成本门禁晋级，不声称实测分数。

### I-operator

Operators see service health and redacted telemetry, not tenant content by default. Logs omit raw tokens and document text. Admin changes are audited and do not bypass data-plane checks.

运维默认只见服务健康与脱敏遥测，不获得租户内容权限。日志不含原始 token 与文档正文；管理变更审计且不绕过数据面检查。

### I-bounds

Exactly three tools: catalogue.lookup, ticket.read, ticket.create. Write requests require the initiating employee approval within current permissions. No arbitrary scripts, procurement, autonomous refunds or unbounded agent loops.

仅三种工具：catalogue.lookup、ticket.read、ticket.create。写请求要求发起员工在当前权限内审批；无任意脚本、采购、自主退款或无限循环。

## Implementation assumptions and limits

OIDC sign-in completes in the BFF: browser redirects carry the authorization code;
PKCE verifier, client authentication, ID/access/agent tokens remain server-side. The
browser receives only a Secure, HttpOnly, SameSite session cookie. Validate state, nonce,
issuer, intended audience and PKCE. The Agent Service receives an AS-issued agent-scoped
subject token over an authenticated BFF→Agent channel; it never treats a BFF-audience
token as its own authority. If the AS cannot issue the constrained delegated token,
change the identity design before implementation. Do not invent support.

F1 focuses on downstream delegation after login; E1 focuses on approval and execution.
Their linked prerequisites are mandatory even when not repeated on every lifeline.
The Service Desk connector uses a machine credential but enforces delegated user/tenant
policy before invocation and records the user and actor in its audit trail.

All processors that touch content use verified tenant identities. Citation links are
opaque IDs resolved through the BFF, not public S3 links that bypass current ACL checks.
Approval authorizes only the stored draft hash; it does not grant additional permissions.

A single AWS region is chosen only after checking required Bedrock model availability,
quotas and permitted data handling. Application services span two AZs; Aurora storage
uses its service-managed three-AZ design. S3, SQS, Bedrock, KMS, CloudWatch and Secrets
Manager are regional services outside customer subnets; CloudFront is global. ECS job
placement in either AZ is not a promise of two simultaneous job copies. OpenSearch
uses two-AZ zone awareness and replicas, not Multi-AZ with Standby. No RTO/SLO, cost or
benchmark scores have been measured. Historical eval results stay tied to their revisions.
