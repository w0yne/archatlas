# Enterprise Service Assistant — illustrative assumptions

Version 2. Fictional teaching choices; no implementation or measured results.

## AS-ingest

Application API is the ingestion-job producer; workers consume and publish indexed versions.

Application API 是摄取任务生产者；工作进程消费任务并发布索引版本。

```json
{
  "producer": "C-api",
  "queue": "Q-ingest",
  "consumer": "C-ingest",
  "trigger": "steward requests import or source-version rescan through C-api",
  "job": [
    "tenant",
    "sourceRef",
    "sourceVersion",
    "ACL version",
    "idempotencyKey"
  ],
  "workerPublication": "DS-doc and DS-index only, not new Q-ingest jobs",
  "retry": "SQS visibility 300s; maxReceiveCount 3; failed jobs to DLQ, replay only after cause fixed",
  "revocation": "deny at retrieval and citation immediately using current policy; asynchronously tombstone derived index within 60s"
}
```

## AS-request

One persisted request lifecycle; bind short-lived approval and reconcile uncertain writes before closure.

单一持久请求生命周期；绑定短期审批，不确定写入须先对账再关闭。

```json
{
  "store": "DS-app",
  "states": [
    "unapproved",
    "approved",
    "executing",
    "outcome_unknown",
    "outcome_recorded",
    "refused",
    "closed"
  ],
  "approvalTTLSeconds": 300,
  "toolTokenTTLSeconds": 120,
  "idempotencyScope": [
    "tenant",
    "tool",
    "key"
  ],
  "keyReuse": "same key and canonical hash returns prior outcome; a changed hash is rejected",
  "reconciliation": "read-only lookup by key every 30s, at most four automatic attempts; then hold outcome_unknown for operator-coordinated investigation without tenant-content access",
  "closure": "only outcome_recorded or refused may close; never close unknown as success or issue a fresh blind write",
  "recordRetentionDays": 30
}
```

## AS-policy

Explicit role grants are unioned, then intersected with current tenant/resource constraints; policy denial wins.

显式角色授权取并集，再与当前租户/资源约束相交；策略拒绝优先。

```json
{
  "roleAssignment": "server-verified current membership, never client-selected tenant/roles",
  "default": "deny absent grant or on evaluation error",
  "employee": [
    "read own-tenant knowledge only if current ACL allows",
    "create ticket only for own permitted draft with exact bound approval and execution-time reauthorization"
  ],
  "steward": [
    "maintain own-tenant knowledge and ACL",
    "read own-tenant content only with current ACL",
    "approve tenant-authorized deidentified or synthetic feedback export"
  ],
  "operator": [
    "redacted service health and cost",
    "network/release operations using scoped automation identities",
    "no implicit tenant-content or production tool-write grant"
  ],
  "roleCombination": "operator+employee may use separately granted employee rights; operator role contributes no content grant",
  "serviceRule": "AS proof and scopes are necessary, never sufficient; current policy, tenant, subject, actor and bound approval still apply",
  "roleMatrix": {
    "R-employee": [
      "K",
      "D",
      "W",
      "D",
      "D"
    ],
    "R-steward": [
      "K",
      "M",
      "D",
      "E",
      "D"
    ],
    "R-operator": [
      "D",
      "D",
      "D",
      "D",
      "T"
    ]
  }
}
```

## AS-raci

Use the existing three human roles, with one accountable role per scoped activity.

沿用三个既有人员角色，每项明确范围的活动设一个最终负责角色。

```json
{
  "columns": [
    "R-employee",
    "R-steward",
    "R-operator"
  ],
  "rows": [
    [
      "approve-request",
      "A/R",
      "C",
      "I"
    ],
    [
      "maintain-knowledge",
      "C",
      "A/R",
      "I"
    ],
    [
      "approve-export",
      "C",
      "A/R",
      "C"
    ],
    [
      "operate-health",
      "I",
      "C",
      "A/R"
    ],
    [
      "release-recover",
      "I",
      "A",
      "R"
    ]
  ],
  "A": "accountable for outcome and explicit human approval where required; never a data-plane permission grant",
  "C": "consult before a consequential change; not an approval bypass",
  "I": "receive redacted outcome updates",
  "scope": "employee approval is per initiating employee; stewardship is per tenant; release approval covers the evaluated configuration, not arbitrary production data access"
}
```

## AS-network

Single-region, two-AZ network with TLS, explicit return routing and narrowly scoped endpoint/egress rules.

单区域双 AZ 网络；TLS、显式返回路由与受限端点/出站规则。

```json
{
  "addresses": "RFC5737 documentation-only fixture; replace with an approved RFC1918 deployment plan before provisioning",
  "vpc": "192.0.2.0/24",
  "publicSubnets": [
    "192.0.2.0/27",
    "192.0.2.32/27"
  ],
  "appSubnets": [
    "192.0.2.64/27",
    "192.0.2.96/27"
  ],
  "dataSubnets": [
    "192.0.2.128/27",
    "192.0.2.160/27"
  ],
  "ingress": "browser HTTPS/443 through CloudFront to public ALB; origin accepts CloudFront origin-facing prefix list plus an origin secret header held only by platform automation; ALB targets C-api on TLS/443",
  "eastWest": "C-api→C-agent, C-agent→C-tools and C-tools→C-api on TLS/443 with workload mTLS; SG allowlists by service identity/security group",
  "data": "Aurora TCP/5432 only from API-approved application security groups; OpenSearch TLS/443 only Agent/Ingestion groups",
  "privateEndpoints": "S3 gateway endpoint; interface endpoints for SQS, Bedrock runtime, CloudWatch Logs, KMS and Secrets Manager; endpoint policies restrict roles/resources",
  "externalEgress": "one NAT gateway per AZ; application route uses same-AZ NAT, public route IGW; return path through same NAT with stateful SG and matching ephemeral NACL returns",
  "externalFilters": "HTTPS/443 to configured AS, Service Desk and source-repository address allowlists; placeholder endpoints use reserved .example names; NAT itself is not an authorizer or domain firewall",
  "dns": "VPC resolver + private DNS for interface endpoints; public/enterprise resolution for approved external .example fixtures replaced during deployment",
  "noInbound": "tasks/stores have no public addresses; no unsolicited inbound path; no peering/transit inferred"
}
```

## AS-release

Promote a tested versioned configuration bundle through human approval and scoped release automation.

经人工批准和受限发布自动化，晋级已测试的版本化配置包。

```json
{
  "trigger": "pull request changing prompt/model configuration; repository workflow builds an immutable bundle in DS-eval",
  "platform": "illustrative GitHub Actions workflow with short-lived AWS workload federation, restricted repository/environment trust",
  "artifactIdentity": [
    "S3 versionId",
    "SHA-256 digest",
    "prompt version",
    "model id/version",
    "dataset version"
  ],
  "evaluation": "C-eval evaluates synthetic/deidentified holdout data using evaluation-only IAM identity; never writes production tools",
  "gates": {
    "answerQualityMin": 0.85,
    "citationPrecisionMin": 0.95,
    "criticalSafetyViolations": 0,
    "p95LatencyMaxSeconds": 8,
    "meanAnswerTokenCostMaxUSD": 0.02
  },
  "approval": "R-steward approves the exact evaluated digest; R-operator executes the release workflow",
  "promotion": "same digest to staging smoke, then production 5% traffic for 10min, then 100% if health gates pass; no rebuild between stages",
  "enforcement": "workflow deployment IAM role can update the configuration pointer only; C-eval cannot assume it",
  "recovery": "stop canary and restore previous compatible pointer on health regression; no automatic database rollback; incompatible changes require forward-fix plan and renewed approval",
  "healthGate": "5xx below 2% and p95 <=8s during canary; minimum 100 requests or hold for manual review",
  "scores": "thresholds are illustrative, not measured outcomes or promised performance"
}
```

## AS-observe

Measure scoped health and cost, redact before export, and route actionable alerts to operators.

度量明确范围的健康与成本，在导出前脱敏，将可操作告警发送给运维。

```json
{
  "SLI": "successful authorized answer requests / eligible requests; exclude policy-denied requests from service-failure numerator, but count them separately for security monitoring",
  "SLO": "99.5% successful authorized answers over rolling 30 days; illustrative internal target, not an SLA",
  "latency": "p95 end-to-end authorized answer latency <=8s, measured daily",
  "cost": "mean answer token cost <=USD0.02; warn when daily aggregate token cost exceeds USD20",
  "capture": "100% aggregate metrics, 100% security/audit events; traces sampled at 10%; trace/context IDs join runtime hops without carrying raw content",
  "redaction": "remove raw tokens, prompts and document text before emission; pseudonymize tenant/user identifiers",
  "retentionDays": {
    "logs": 30,
    "metrics": 90,
    "traces": 7,
    "audit": 365
  },
  "alerts": [
    "5xx ratio >2% for 5min with >=100 requests",
    "DLQ depth >0 for 5min",
    "daily token cost >USD20",
    "no telemetry heartbeat for 5min"
  ],
  "route": "CloudWatch alarms → SNS email → R-operator; acknowledge within 15min; dashboard check if email absent; email delivery is not a guaranteed incident response",
  "runbooks": [
    "drain/reconcile ingest DLQ after fixing cause",
    "reconcile ambiguous tool outcome by existing key; no blind write",
    "stop rollout and restore compatible config pointer on regression"
  ],
  "delivery": "bounded exporter retry; alarm on telemetry loss, never equate absent data with health; no lossless guarantee"
}
```

## AS-domains

Treat each named external system as one opaque bounded context with an explicit upstream contract.

将各具名外部系统视为单一不透明限界上下文，并明确上游契约。

```json
{
  "S-assistant": {
    "team": "Assistant team",
    "model": "conversation, approval, delegated service request"
  },
  "X-idp": {
    "team": "Identity team",
    "model": "principal, membership, scope",
    "pattern": "OHS/PL upstream; assistant conformist for token semantics"
  },
  "X-doc": {
    "team": "Knowledge team",
    "model": "source document, version, source ACL",
    "pattern": "OHS upstream; assistant anti-corruption adapter"
  },
  "X-desk": {
    "team": "Service operations team",
    "model": "catalogue, ticket, idempotency record",
    "pattern": "OHS upstream; assistant anti-corruption adapter"
  },
  "X-model": {
    "team": "Model platform team",
    "model": "model request and generated output",
    "pattern": "OHS/PL upstream; assistant conformist for protocol only, never for authorization"
  },
  "terminology": "DDD ACL means anti-corruption layer; document ACL means access-control list. These are distinct."
}
```

## AS-data

Confirm the logical entities, tenant-scoped identifiers, data stewardship and classification.

确认逻辑实体、租户范围标识、数据管理责任及分类。

```json
{
  "keys": "tenant_id + local_id for tenant-owned records; composite foreign keys preserve tenant scope; idempotency tuple tenant/tool/key is unique",
  "approval": [
    "tenant",
    "subject",
    "tool",
    "canonicalParameterHash",
    "expiresAt",
    "idempotencyKey"
  ],
  "execution": [
    "tenant",
    "tool",
    "idempotencyKey",
    "approvalId",
    "parameterHash",
    "status",
    "recordedOutcome"
  ],
  "storeOwners": {
    "DS-app": "R-steward accountable; C-api technical custodian; R-operator operates infrastructure without implicit content rights",
    "DS-doc": "R-steward",
    "DS-index": "R-steward",
    "DS-eval": "R-steward"
  },
  "classification": {
    "DS-app": "tenant-confidential",
    "DS-doc": "tenant-confidential",
    "DS-index": "tenant-confidential derived; same source ACL restrictions",
    "DS-eval": "internal deidentified/synthetic; evaluation identity only"
  },
  "logicalModel": "D1 attributes are illustrative, not a complete migration schema; Chat denotes a conversation aggregate and does not eliminate message/citation records",
  "evaluationIsolation": "tenant-scoped deidentified prefixes and synthetic datasets; no cross-tenant content sharing"
}
```

## AS-roadmap

Use a read-only slice, approved writes and finally gated change promotion as the illustrative rollout order.

示意实施顺序为只读切片、经审批写入，最后实施变更晋级门禁。

```json
{
  "plateaus": [
    "ST-baseline",
    "ST-answers",
    "ST-tickets",
    "ST-target"
  ],
  "workPackages": [
    "WP-retrieval",
    "WP-approval",
    "WP-eval"
  ],
  "journeyOwners": "R-steward owns source freshness/access explanation; R-operator owns delivery reliability and status reconciliation UI work without being granted tenant content access",
  "notCommitment": "journey emotions, opportunities, durations and roadmap ordering are teaching assumptions, not customer research or committed dates"
}
```

## AS-components

Give the Agent logical components stable, unnumbered module names without adding deployed services.

为 Agent 逻辑组件定义稳定、无序号的模块名，不增加部署服务。

```json
{
  "P-plan": "request_planner",
  "P-retrieve": "authorized_retriever",
  "P-compose": "answer_composer",
  "modelGateway": "logical component within answer_composer; ingestion uses its own scoped model invocation identity",
  "codeStatus": "illustrative module boundaries, not claims about an existing implementation"
}
```

## AS-interfaces

Assign authenticated internal and external contracts with bounded retries and explicit illustrative capacity targets.

为内部及外部接口指定认证契约、有界重试和明确的示意容量目标。

```json
{
  "I-07": "workload mTLS identity for C-tools; approval.lookup limited to matching tenant/subject/tool/hash; fresh policy lookup",
  "I-08": "AWS SigV4 task role restricted to selected Bedrock model and region",
  "I-09": "mTLS source connector identity plus tenant-aware source ACL export; external contract assumed",
  "I-10": "C-api SigV4 role with sqs:SendMessage on Q-ingest only",
  "I-11": "C-ingest SigV4 role with ReceiveMessage/DeleteMessage/ChangeMessageVisibility on Q-ingest; long-poll, no broker push",
  "owners": "R-operator is internal transport custodian; R-steward accountable for tenant data/approval policy; named external-context teams own their endpoints",
  "capacity": "illustrative 10 interactive requests/s per tenant, burst 20 for 60s; ingest 1 version/s/tenant; tool writes 1/s/tenant",
  "timeouts": "internal control calls 5s, model generation 30s, external connector 10s; read retries at most 2 with jitter; never retry an ambiguous write with a new key",
  "serviceTarget": "internal dependency availability target 99.9% monthly, no contractual SLA or vendor guarantee; failures surface to caller and are measured separately"
}
```

