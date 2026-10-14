# Access-Control Model (访问控制模型)
<!-- Generated from content/en/types/F3-access-control-model.md by tools/build_skill_refs.py. Do not edit. -->
> Under what rules can a subject perform an action on a resource, in a given scope or context?
Scope: One application or domain: its resource classes, a small set of actions, and one chosen model kind (RBAC, ABAC or ReBAC, possibly combined) Neighbours: D1, F1, F2, H1.

## Meaning
- **Question:** under what rules can a subject perform an action on a resource in a given scope? It describes authority, not network reachability or call order.
- **Three model kinds, three questions:** RBAC — which roles hold which permissions (matrix or hierarchy); ABAC — which attributes satisfy which rule (decision table); ReBAC — which relationships imply access (typed relation graph).
- **Definition used here:** a grant has action, resource and scope. Matrix, table and graph are not variants of one thing; choose by policy, not fashion.
- **Leaves out:** real user rosters, full policy code, every exception, enforcement points (F1).

## When to use and how to choose
- **Audience:** business owners, security and governance staff, developers, administrators.
- **Scenarios:** scoped team collaboration (support, warehouse, finance); multi-tenant authorisation (merchants see only their orders); document sharing with inheritance; delegation and separation of duties (who creates and who approves a refund); comparing a proposed role model with what is enforced.
- **When not to use:** a role matrix alone when relationships, time or resource attributes decide access. Do not introduce an authorisation engine just because its documentation has good examples.
- **vs neighbours:**
  - **F1** for where identity is verified and decisions enforced.
  - **F2** for what can go wrong.
  - **D1** for persistence relationships, not permission relations.
  - **H1 RACI** for project responsibility.
  - **C5** to show where a policy component sits.

## Notation and elements
- **Formal or informal:** RBAC, ABAC and XACML have standards behind their concepts; the drawing is a convention. Declare the legend.
- **Common required elements:** subject classes, actions, resource classes, scope or ownership, decision rule, default behaviour, constraints. Label "grant", "member of", "inherits" and "owns" explicitly.
- **Legend:** distinguish allow, deny, conditional and not applicable. A blank cell is ambiguous.
- **RBAC:** users, roles, permissions (operations on objects) and assignment relations; sessions and active roles, hierarchy, and static or dynamic separation of duties where relevant. Matrix rows are roles; columns name operations on resources, not vague features.
- **ABAC:** authoritative subject, resource and environment attributes, with a sample predicate or decision table; show where each attribute comes from and when it is evaluated.
- **ReBAC:** typed objects, labelled relations, and union, intersection or inheritance rules. A relation chain needs policy semantics; an ER-style picture alone is not enough.
- **Optional:** an administration strip (who grants and revokes), policy and data ownership, revocation or caching assumptions, application versus user identity, enforcement locations. PEP, PDP, PIP and PAP are functional responsibilities for technical audiences, not four required services. XACML's PAP (policy administration point) is not the policy administrator of NIST's zero-trust architecture.
- **Text budget:** 1–3 words per cell or edge label; policy prose goes in a note.

## Best practices and anti-patterns
### Best practices
1. **Default deny,** and check authorisation for the requested action and resource on every relevant request.
2. **Keep action capability separate from resource scope.** "Support agent" is not permission to edit every merchant's orders; show a conditional grant or a small scoped example.
3. **State the combining rule** (grants union, denies win, constraints intersect). No single formula fits every system.
4. **Separate management authority from content authority.** If administrators can read content, make that grant explicit; explain emergency access and delegation separately.
5. **Keep source restrictions on derived content.** A shared report built from restricted orders must recheck source access or limit its audience.

### Anti-patterns
1. **Unmanaged, unexplained direct grants.** Direct grants themselves are not wrong: ownership, explicit sharing and ACLs are legitimate; the problem is exceptions nobody owns.
2. **Role explosion,** and the opposite: forcing all contextual policy into roles.
3. **Features instead of actions and resources** as matrix columns.
4. **Shorthand that drops qualifiers** ("team members can see it" when source restrictions also apply).
5. **Presenting the design as implemented coverage** without checking enforcement paths.

## Drawing recipe
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

## Evidence in a code repository
- **Inputs:** role and permission tables, authorisation decorators or guards, policy files, row-level filters, relation tuples, owner and tenant columns, administration endpoints, superuser overrides, sharing logic, denial and revocation tests.
- **Caution:** a database relation or an unused helper is not proof that every endpoint enforces it.
- **Do not inspect real permission rosters by default.**
- **Must come from people:** intended policy, delegation rules, whether administrators read content, design versus implemented coverage.

## Guided-mode questions
1. Which resources and actions, and which ownership or tenant boundaries, matter? (orders, invoices, refunds; per-merchant tenants)
2. Do roles suffice, or do attributes or sharing relations change decisions? (roles plus tenant scope; add relations only for sharing)
3. Who can grant and revoke access, and within what delegation scope? (tenant admins, within their tenant)
4. Do administrators automatically read content, or need separate access? (separate access)
5. Are we designing rules or documenting verified implementation? (designing, marked proposed)

## Template
Model template: `assets/templates/F3.json` · Layout template: `grid_table` · roles (or subjects) become rows, resource-action pairs become grouped columns, and each cell holds allow, deny, conditional or not-applicable from a fixed legend; for ABAC and ReBAC the same `tables` carry attribute rules or relation definitions (a relation graph needs a second model, because `grid_table` takes tables only).

## Sample
Figure: `samples/F3-access-control-model.svg` (published with the site)
