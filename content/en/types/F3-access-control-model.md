---
code: F3
slug: access-control-model
family: F
names:
  en: Access-Control Model
  zh: 访问控制模型
  aliases:
    en: [authorization model, permission model, role-permission matrix, RBAC model, ABAC policy model, relationship-based authorization graph]
    zh: [授权模型, 权限模型, 角色权限矩阵, 基于属性的授权模型, 基于关系的授权模型]
question: "Under what rules can a subject perform an action on a resource, in a given scope or context?"
audiences: [business owners, security and governance staff, application developers, administrators]
level: logical
phases: [design, review]
scope: "One application or domain: its resource classes, a small set of actions, and one chosen model kind (RBAC, ABAC or ReBAC, possibly combined)"
formal:
  kind: standard
  ref: "RBAC: ANSI/INCITS 359-2004 and its 2012 revision (NIST history). ABAC: NIST SP 800-162. Policy language and architecture: OASIS XACML 3.0. ReBAC has influential models (Zanzibar, OpenFGA) but no single graphical standard"
neighbours: [F1, F2, D1, H1, C5]
status: draft
---

# Access-Control Model (访问控制模型)

> A picture of the rules that decide who may do what to which resource, drawn as a matrix, an attribute table or a relationship graph, whichever matches the policy.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** under what rules can a subject perform an action on a resource in a given scope or context? It describes authority and its administration, not network reachability or the order of calls. A "can edit" relation and an arrow carrying document content have different meanings.
- **Three model kinds, three questions:**
  - **RBAC:** which roles hold which permissions, and who holds the roles? A matrix or hierarchy [1].
  - **ABAC:** which attributes of subject, resource and environment satisfy which rule? An attribute or decision table [2].
  - **ReBAC:** which relationships between objects imply which access? A typed relation graph with derivation rules [4][5].
- **Definition used here:** a *grant* always has action, resource and scope semantics. Matrix, attribute table and graph are not graphical variants of one thing; choose by policy, not fashion.
- **Leaves out:** real user rosters, full policy code, every exception. A role called "administrator" in a RACI chart (H1) is not an application permission.
- **Not enforcement:** a model diagram enforces nothing; show enforcement points only if that is the topic (F1).

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
- **Audience:** business owners, security and governance staff, developers, administrators.
- **Classic scenarios:**
  1. Scoped team collaboration: shop staff in support, warehouse and finance teams.
  2. Multi-tenant authorisation: marketplace merchants who see only their own orders.
  3. Document sharing with inheritance: a folder of invoices shared to an accountant.
  4. Administrative delegation and separation of duties: who may create a refund and who may approve it.
  5. Comparing a proposed role model with what is enforced today.
- **When not to use:** a role matrix alone, when relationships, time or resource attributes materially decide access. Do not introduce an authorisation engine just because its documentation has good examples.
- **vs neighbours:**
  - Choose **F1 Authentication Flow** for where identity is verified and decisions are enforced.
  - Choose **F2 Threat-Model DFD** for what can go wrong.
  - Choose **D1 Entity-Relationship** for actual persistence relationships, not permission relations.
  - Choose **H1 RACI Matrix** for project responsibility, not application permissions.
  - Choose **C5 Logical Architecture** to show where a policy component sits among the parts.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** RBAC, ABAC and XACML have standards behind their concepts; the drawing is a convention. Declare the legend.
- **Common required elements:** subject classes, actions, resource classes, scope or ownership, decision rule, default behaviour, constraints. Label "grant", "member of", "inherits" and "owns" explicitly.
- **Legend:** distinguish allow, deny, conditional and not applicable. A blank cell is ambiguous.
- **RBAC:** users, roles, permissions (operations on objects) and assignment relations; sessions and active roles, hierarchy, and static or dynamic separation of duties where relevant [1]. Matrix rows are roles; columns name operations on resources, not vague features.
- **ABAC:** authoritative subject, resource and environment attributes, with a sample predicate or decision table; show where each attribute comes from and when it is evaluated [2].
- **ReBAC:** typed objects, labelled relations, and union, intersection or inheritance rules [4]. A relation chain needs policy semantics; an ER-style picture alone is not enough.
- **Optional:** an administration strip (who grants and revokes), policy and data ownership, revocation or caching assumptions, application versus user identity, enforcement locations. PEP, PDP, PIP and PAP are functional responsibilities for technical audiences, not four required services [3]. XACML's PAP (policy administration point) is not the policy administrator of NIST's zero-trust architecture.
- **Text budget:** 1–3 words per cell or edge label; policy prose goes in a note.

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Default deny,** and check authorisation for the requested action and resource on every relevant request [6].
2. **Keep action capability separate from resource scope.** "Support agent" is not permission to edit every merchant's orders; show a conditional grant or a small scoped example [4][7].
3. **State the combining rule** (grants union, denies win, constraints intersect). No single formula fits every system.
4. **Separate management authority from content authority.** If administrators can read content, make that grant explicit; explain emergency access and delegation separately.
5. **Keep source restrictions on derived content.** A shared report built from restricted orders must recheck source access or limit its audience.

### Anti-patterns
1. **Unmanaged, unexplained direct grants.** Direct grants themselves are not wrong: ownership, explicit sharing and ACLs are legitimate; the problem is exceptions nobody owns [2][4].
2. **Role explosion,** and the opposite: forcing all contextual policy into roles.
3. **Features instead of actions and resources** as matrix columns.
4. **Shorthand that drops qualifiers** ("team members can see it" when source restrictions also apply).
5. **Presenting the design as implemented coverage** without checking enforcement paths.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [NIST SP 800-162, Figures 2 and 5](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf) — attribute-based decision inputs and separated decision, enforcement and administration functions; not a requirement for separate servers. US government work, generally public domain.
- [OpenFGA: User Groups](https://openfga.dev/docs/modeling/user-groups) — concrete user, group and object relations with derived permissions and checks that make the model testable.
- [OpenFGA: Authorization Through Organization Context](https://openfga.dev/docs/modeling/organization-context-authorization) — shows why organisation membership and active context can be separate restrictions.
- [AWS Prescriptive Guidance, Example 3: multi-tenant access control with RBAC](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-mt-abac-examples.html) — makes tenant isolation and in-tenant roles visible. The URL says "abac" but the page is titled RBAC; its per-tenant store is one implementation pattern, not a rule.
- Link only; no artwork copied. A product's code licence does not settle the licence of its documentation diagrams.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. List resource classes (order, invoice, product) and a small set of meaningful actions (view, edit, refund, approve).
2. Separate subjects, application identities, roles or groups, and tenant or ownership scope.
3. Choose the form from the policy: matrix for role grants, attribute table for conditions, relation graph for sharing and inheritance. State the choice in the title ("Shop back office: role-permission matrix, proposed").
4. Matrix layout: roles as rows, resource-action pairs as columns grouped by resource; cells carry the legend symbol. Graph layout: subjects on the left, resources on the right, labelled relations between, no more than about 12 nodes.
5. State default deny and the combining rule in a note beside the figure.
6. Add one allowed and one denied worked example that agree with the rules; add an administration strip only if delegation is in scope.
7. Colour: neutral base; one hue for allow, one for conditional, grey hatch for deny; every symbol also has a text or shape cue.
8. Mark design versus verified enforcement in the caption.

**Self-check**
- [ ] The model kind (RBAC, ABAC or ReBAC) is explicitly chosen.
- [ ] Actions and resources are named, not vague features.
- [ ] Scope or ownership is distinct from role.
- [ ] Cell and edge meanings and the combining rule are unambiguous.
- [ ] Default and error behaviour are stated.
- [ ] Administration and content privileges are not conflated.
- [ ] The allowed and denied examples agree with the rules.
- [ ] Enforcement coverage and unverified assumptions are disclosed.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Inputs:** role and permission tables, authorisation decorators or guards, policy files, row-level filters, relation tuples, owner and tenant columns, administration endpoints, superuser overrides, sharing logic, denial and revocation tests.
- **Caution:** a database relation or an unused helper is not proof that every endpoint enforces it.
- **Do not inspect real permission rosters by default.**
- **Must come from people:** intended policy, delegation rules, whether administrators read content, design versus implemented coverage.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Which resources and actions, and which ownership or tenant boundaries, matter? (orders, invoices, refunds; per-merchant tenants)
2. Do roles suffice, or do attributes or sharing relations change decisions? (roles plus tenant scope; add relations only for sharing)
3. Who can grant and revoke access, and within what delegation scope? (tenant admins, within their tenant)
4. Do administrators automatically read content, or need separate access? (separate access)
5. Are we designing rules or documenting verified implementation? (designing, marked proposed)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/F3.json` · Layout template: `grid_table` · roles (or subjects) become rows, resource-action pairs become grouped columns, and each cell holds allow, deny, conditional or not-applicable from a fixed legend; for ABAC and ReBAC the same `tables` carry attribute rules or relation definitions, with nodes and `assoc` edges only for a small illustrative graph.

## Sources {#sources}
<!-- skill: omit -->
1. NIST, Role Based Access Control (archived project and standard history; latest reaffirmation not asserted) — https://csrc.nist.gov/projects/role-based-access-control — accessed 2026-10-14
2. NIST, SP 800-162, Guide to Attribute Based Access Control (ABAC) Definition and Considerations (January 2014, updated 2 August 2019) — https://csrc.nist.gov/pubs/sp/800/162/upd2/final ; figures: https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf — accessed 2026-10-14
3. OASIS, eXtensible Access Control Markup Language (XACML) Version 3.0 (22 January 2013) — https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html — accessed 2026-10-14
4. OpenFGA, User Groups and Authorization Through Organization Context — https://openfga.dev/docs/modeling/user-groups ; https://openfga.dev/docs/modeling/organization-context-authorization — accessed 2026-10-14
5. Google Research, Zanzibar: Google's Consistent, Global Authorization System (USENIX ATC 2019) — https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/ — accessed 2026-10-14
6. OWASP, Authorization Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html — accessed 2026-10-14
7. AWS Prescriptive Guidance, Example 3: Multi-tenant access control with RBAC — https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-mt-abac-examples.html — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![F3 sample: online shop role-permission matrix for customer, support agent, warehouse and finance roles over orders, refunds and inventory, with a tenant-scope note](/samples/F3-access-control-model.svg)
*Sample pending (generated by the renderer from `examples/`).*
