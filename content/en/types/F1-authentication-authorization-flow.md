---
code: F1
slug: authentication-authorization-flow
family: F
names:
  en: Authentication and authorization flow
  zh: 认证与授权流程图
  aliases:
    en: [identity flow, sign-in flow, SSO flow, OAuth flow, OIDC flow, delegated access flow, delegated API access flow]
    zh: [身份认证流程图, 统一登录流程图, 委托访问流程图]
question: Who proves which identity to whom, what authority is conveyed, and where is access actually permitted or refused?
audiences: [security, architects, developers]
levels: [logical]
phases: [design, build]
scope: One scenario (browser sign-in, service acting for a user, or machine-only call) and one protected operation
formal: {kind: convention, ref: 'A concern-based diagram family, not a notation. Drawn as a UML 2.5.1 sequence diagram when UML is claimed; protocol semantics come from OAuth 2.0 (RFC 6749), PKCE (RFC 7636), the OAuth security BCP (RFC 9700) and OpenID Connect Core 1.0'}
neighbours: [E1, F2, F3]
status: draft
---

# Authentication and Authorization Flow (认证与授权流程图)

**Named variant of E1.** [Open Sequence diagram → F1](/types/e1-sequence-diagram#variant-f1). This compatibility page retains its recipe, checks, anchors and historical downloads.

> A scenario-specific picture of who proves an identity to whom, which proof is handed to which recipient, and the point where a request is allowed or refused.

## Meaning {#meaning}
<!-- skill: condense (4–6 lines) -->
- **Question:** who proves which identity to whom, what authority is conveyed, and where is access permitted or refused? The view explains a chain of trust, not just HTTP traffic. Sign-in does not grant access to every object.
- **Participants to keep apart:** the human, the client application, the authority that issues a proof, and the service that relies on it.
- **Standing:** a concern-based diagram family, not a formal notation. A sequence diagram is the usual form; a simplified process diagram is the plain-language form. If you claim UML, follow the UML 2.5.1 interaction rules instead of inventing arrow meanings [1].
- **Leaves out:** unrelated business calculations, identity-provider internals, literal secrets, and the full permission model (F3). Renewal and logout get their own scenario when lifecycle is the question.
- **Definition used here:** *authentication* establishes who the caller is; *authorization* decides what that caller may do. OAuth 2.0 is an authorization framework; OpenID Connect adds a user-authentication layer on top of it [2][5]. Showing both in one picture is fine, but the two responsibilities stay visibly separate.

## When to use and how to choose {#choose}
<!-- skill: condense (bullets, ≤12 lines) -->
<!-- skill-text
- **Audience:** architects, identity engineers, developers, security reviewers; a plain-language variant serves business owners.
- **Scenarios:** a shopper signs in, then loads order history through an API; the order API calls the payment API on behalf of the shopper; a nightly job calls the stock API with no end user (machine to machine); step-up sign-in or session renewal.
- **When not to use:** a background job has no end user, so do not draw a human sign-in; F1 is not the permission model or a network design.
- **vs neighbours:**
  - **E1 Sequence** for a general interaction without identity focus.
  - **F3 Access-Control Model** for the permission rules.
  - **F2 Threat-Model DFD** for what can go wrong at trust boundaries.
  - **C2 System Context** to show which identity providers exist, without the exchange.
  - **D2 Data-Flow** for data movement rather than proof movement.
-->
- **Audience:** architects, identity engineers, developers, security reviewers; a plain-language variant serves business owners.
- **Classic scenarios:**
  1. A shopper signs in to the shop web app, then loads their order history through an API.
  2. The order API calls the payment API on behalf of the signed-in shopper.
  3. A nightly inventory-sync job calls the stock API with no end user (machine to machine).
  4. Step-up sign-in before changing a payout account, or session renewal.
- **When not to use:** a background job has no end user, so do not draw a human sign-in; F1 is not the whole permission model or a network design.
- **vs neighbours:**
  - Choose **E1 Sequence Diagram** for a general request interaction without an identity focus.
  - Choose **F3 Access-Control Model** for the permission rules themselves (roles, attributes, relations).
  - Choose **F2 Threat-Model DFD** to reason about what can go wrong at trust boundaries.
  - Choose **C2 System Context** to show which external identity providers exist, without the exchange.
  - Choose **D2 Data-Flow Diagram** for data movement rather than proof movement.

## Notation and elements {#notation}
<!-- skill: condense (bullets, ≤15 lines) -->
- **Formal or informal:** informal. In a UML sequence, lifelines are participants, ordered messages are interactions, dashed arrows are replies, and `alt` fragments show alternatives [1]. In a custom flow, number the arrows and explain them.
- **Required for the chosen scenario:**
  - Distinct participants and who initiates each message.
  - Proof issuer and proof recipient for every credential shown.
  - Where verification happens and where enforcement happens.
  - The protected operation or resource, and the outcome including the refusal point.
  - Authenticated principals kept apart from untrusted, user-supplied identifiers.
- **Technical variant:** name the authorization code, access token, ID token and session cookie distinctly. Show audience, scope and the application-versus-user binding where they affect trust. Draw browser redirects separately from back-channel exchanges. A confidential client secret never travels through a public browser [2]-[5].
- **Plain-language variant:** "sign in", "verified identity", "ask permission", "allow / refuse", with a link to the protocol detail. Simplifying must still show who verifies and who stops access.
- **Not a message:** a trust boundary is a region, not an arrow.
- **Optional:** expiry and refresh, multi-factor, consent, discovery, audit and revocation, only where material to the scenario.
- **Text budget:** 2–6 words per arrow, verb plus proof purpose ("present access token").

## Best practices and anti-patterns {#practice}
<!-- skill: condense (top 5 each, no citations) -->
### Best practices
1. **Separate three things:** identity validation, the permission decision and enforcement. The browser is never the only gate [6].
2. **Respect proof recipients.** A token issued for the order API is not authority at the payment API; an on-behalf-of exchange makes the hand-over explicit [7].
3. **Use current security guidance, not every historical grant.** RFC 9700 updates the baseline: for example public clients must use PKCE, and the implicit and password grants should not be used; requirements depend on client and flow type [4]. Mark any flow you show as current or legacy.
4. **Include a refusal branch** whenever the picture explains enforcement. A login arrow must not imply every operation succeeds.
5. **Match the proof structure to the protocol.** "Application plus user identity" does not necessarily mean two bearer tokens.

### Anti-patterns
1. **One diagram that blends every protocol** (sign-in, delegation, machine calls). Split by scenario.
2. **Treating a code, an ID token, an access token and a session as interchangeable** "tokens".
3. **A token relabelled as authority for a different service** without an exchange step.
4. **Happy path only** in a picture meant to show enforcement.
5. **Secrets or real endpoint values on the figure**, or specialist abbreviations in the plain-language variant.

## Exemplars {#exemplars}
<!-- skill: omit -->
- [RFC 6749, Figures 1 and 3](https://www.rfc-editor.org/rfc/rfc6749.html) — named protocol roles and ordered exchanges; read it with the newer BCP, not as a list of recommended grants. © IETF Trust, text reuse per IETF terms.
- [Microsoft identity platform: authorization code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow) — browser, client and authority separated in a worked flow that includes PKCE.
- [Microsoft identity platform: on-behalf-of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow) — API A and API B with distinct token audiences expose the delegation boundary.
- Link only; no artwork copied. Check each site's illustration terms before reproducing a figure.

## Drawing recipe {#recipe}
<!-- skill: keep (≤25 lines) -->
1. Choose one client type and one protected operation; state audience and current or proposed status in the title ("Shop: signed-in order history, current").
2. From evidence, identify the issuer, caller, receiving API and protected resource.
3. Trace proof issuance and validation first, then permission enforcement as a separate step.
4. Layout: participants left to right (person, client, issuer, API, resource), interactions top to bottom; one scenario per figure. Isolate any downstream exchange (API to API) in its own figure or frame.
5. Draw browser redirects and back-channel calls with different line styles and say so in a one-line key.
6. Add an `alt` frame with an allow and a refuse outcome; the refuse branch ends before the protected operation.
7. Labels: short verb plus proof purpose; number the arrows. Colour marks responsibility (issue, verify, enforce), not product; at most 3 colours plus neutral.

**Self-check**
- [ ] The client type and scenario are explicit.
- [ ] Human and machine identities are distinct.
- [ ] Each proof has an issuer and an intended recipient.
- [ ] Code, ID token, access token and session are not interchangeable in the labels.
- [ ] Verification and enforcement are both visible.
- [ ] The refusal branch does not continue into the protected operation.
- [ ] Browser and back-channel exchanges are drawn consistently; arrows attach to lifelines.
- [ ] Unverified external configuration is disclosed on the figure or its caption.

## Evidence in a code repository {#evidence}
<!-- skill: keep (≤10 lines) -->
- **Inputs:** authentication middleware, callback and session handlers, configured issuer and audience names, client-registration declarations, downstream API clients, permission dependencies, route registration, denial tests, token renewal handling.
- **Read setting names, not secret values.**
- **Declarations are not behaviour:** code shows intent; the deployed identity provider's consent and client configuration stay unverified unless the user confirms them.
- **Must come from people:** which identity choices are decided versus open, and the proposed flow.

## Guided-mode questions {#questions}
<!-- skill: keep (≤8 lines) -->
1. Browser sign-in, a service acting for a user, or a machine-only call? (browser sign-in followed by one API call)
2. Business owners or protocol implementers as audience? (implementers, with a plain-language caption)
3. Which operation and systems, and current or proposed behaviour? (one read operation, current)
4. Which identity choices are confirmed and which are undecided? (mark undecided ones as proposed)
5. Is renewal or revocation the main concern, or a separate scenario? (separate scenario)

## Template {#template}
<!-- skill: keep (≤3 lines) -->
Model template: `assets/templates/F1.json` · Layout template: `sequence` · participants are `lifeline` nodes (person, client, identity provider, API, resource); proofs and requests are numbered `message` edges with `step`; the allow/refuse alternative is an `alt` entry in `frames` with two `operands`, each with its own guard and step range; verification and enforcement are `activations` on the identity provider and the API.

## Sources {#sources}
<!-- skill: omit -->
1. OMG, UML 2.5.1 (December 2017) — https://www.omg.org/spec/UML/2.5.1/ — accessed 2026-10-14
2. IETF, The OAuth 2.0 Authorization Framework, RFC 6749 — https://www.rfc-editor.org/rfc/rfc6749.html — accessed 2026-10-14
3. IETF, Proof Key for Code Exchange by OAuth Public Clients, RFC 7636 — https://www.rfc-editor.org/rfc/rfc7636 — accessed 2026-10-14
4. IETF, Best Current Practice for OAuth 2.0 Security, RFC 9700 (BCP 240, 2025) — https://www.rfc-editor.org/rfc/rfc9700 — accessed 2026-10-14
5. OpenID Foundation, OpenID Connect Core 1.0 incorporating errata set 2 — https://openid.net/specs/openid-connect-core-1_0.html — accessed 2026-10-14
6. OWASP, Authorization Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html — accessed 2026-10-14
7. Microsoft, OAuth 2.0 on-behalf-of flow — https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow — accessed 2026-10-14
8. Microsoft, OAuth 2.0 authorization code flow — https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow — accessed 2026-10-14
9. ISO/IEC/IEEE 42010:2022, public scope only (the direct fetch returned 403; full text not reviewed) — https://www.iso.org/standard/74393.html — accessed 2026-10-14

## Sample {#sample}
<!-- skill: path only -->
![F1 · Enterprise Service Assistant](/samples/ai-service-assistant/F1/en/diagram.svg)
*Downstream delegation after BFF authorization-code sign-in with PKCE, state and nonce validation. The BFF holds ID/access tokens server-side and exposes only a secure session cookie. The AS explicitly issues an agent-scoped subject token; the Agent authenticates as agent-client to exchange it. The tool token is issued by enterprise-as for mcp-tool-gateway, with employee subject, agent actor, verified tenant, allowed scopes and short expiry. Signature, issuer, audience and expiry validation precede policy and approval enforcement. The AS delegation capability and Service Desk connector scopes are unverified teaching assumptions; if unsupported, redesign instead of forwarding a token with the wrong audience. Solid arrows are back-channel requests, dashed arrows replies; browser redirects belong to the prerequisite sign-in, not this figure.*

[SVG](/samples/ai-service-assistant/F1/en/diagram.svg) · [Model JSON](/samples/ai-service-assistant/F1/en/diagram.json) · [Shared facts](/samples/ai-service-assistant/scenario.json)

[Historical shop sample (regression fixture)](/samples/F1-authentication-authorization-flow.svg) · [All seven views and assumptions](/use/ai-service-assistant).
