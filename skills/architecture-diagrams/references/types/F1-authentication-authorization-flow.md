# Authentication and Authorization Flow (认证与授权流程图)
<!-- Generated from content/en/types/F1-authentication-authorization-flow.md by tools/build_skill_refs.py. Do not edit. -->
> Who proves which identity to whom, what authority is conveyed, and where is access actually permitted or refused?
Scope: One scenario (browser sign-in, service acting for a user, or machine-only call) and one protected operation Neighbours: E1, F3, F2, C2, D2.

## Meaning
- **Question:** who proves which identity to whom, what authority is conveyed, and where is access permitted or refused? The view explains a chain of trust, not just HTTP traffic. Sign-in does not grant access to every object.
- **Participants to keep apart:** the human, the client application, the authority that issues a proof, and the service that relies on it.
- **Standing:** a concern-based diagram family, not a formal notation. A sequence diagram is the usual form; a simplified process diagram is the plain-language form. If you claim UML, follow the UML 2.5.1 interaction rules instead of inventing arrow meanings.
- **Leaves out:** unrelated business calculations, identity-provider internals, literal secrets, and the full permission model (F3). Renewal and logout get their own scenario when lifecycle is the question.
- **Definition used here:** *authentication* establishes who the caller is; *authorization* decides what that caller may do. OAuth 2.0 is an authorization framework; OpenID Connect adds a user-authentication layer on top of it. Showing both in one picture is fine, but the two responsibilities stay visibly separate.

## When to use and how to choose
- **Audience:** architects, identity engineers, developers, security reviewers; a plain-language variant serves business owners.
- **Scenarios:** a shopper signs in, then loads order history through an API; the order API calls the payment API on behalf of the shopper; a nightly job calls the stock API with no end user (machine to machine); step-up sign-in or session renewal.
- **When not to use:** a background job has no end user, so do not draw a human sign-in; F1 is not the permission model or a network design.
- **vs neighbours:**
  - **E1 Sequence** for a general interaction without identity focus.
  - **F3 Access-Control Model** for the permission rules.
  - **F2 Threat-Model DFD** for what can go wrong at trust boundaries.
  - **C2 System Context** to show which identity providers exist, without the exchange.
  - **D2 Data-Flow** for data movement rather than proof movement.

## Notation and elements
- **Formal or informal:** informal. In a UML sequence, lifelines are participants, ordered messages are interactions, dashed arrows are replies, and `alt` fragments show alternatives. In a custom flow, number the arrows and explain them.
- **Required for the chosen scenario:**
  - Distinct participants and who initiates each message.
  - Proof issuer and proof recipient for every credential shown.
  - Where verification happens and where enforcement happens.
  - The protected operation or resource, and the outcome including the refusal point.
  - Authenticated principals kept apart from untrusted, user-supplied identifiers.
- **Technical variant:** name the authorization code, access token, ID token and session cookie distinctly. Show audience, scope and the application-versus-user binding where they affect trust. Draw browser redirects separately from back-channel exchanges. A confidential client secret never travels through a public browser-.
- **Plain-language variant:** "sign in", "verified identity", "ask permission", "allow / refuse", with a link to the protocol detail. Simplifying must still show who verifies and who stops access.
- **Not a message:** a trust boundary is a region, not an arrow.
- **Optional:** expiry and refresh, multi-factor, consent, discovery, audit and revocation, only where material to the scenario.
- **Text budget:** 2–6 words per arrow, verb plus proof purpose ("present access token").

## Best practices and anti-patterns
### Best practices
1. **Separate three things:** identity validation, the permission decision and enforcement. The browser is never the only gate.
2. **Respect proof recipients.** A token issued for the order API is not authority at the payment API; an on-behalf-of exchange makes the hand-over explicit.
3. **Use current security guidance, not every historical grant.** RFC 9700 updates the baseline: for example public clients must use PKCE, and the implicit and password grants should not be used; requirements depend on client and flow type. Mark any flow you show as current or legacy.
4. **Include a refusal branch** whenever the picture explains enforcement. A login arrow must not imply every operation succeeds.
5. **Match the proof structure to the protocol.** "Application plus user identity" does not necessarily mean two bearer tokens.

### Anti-patterns
1. **One diagram that blends every protocol** (sign-in, delegation, machine calls). Split by scenario.
2. **Treating a code, an ID token, an access token and a session as interchangeable** "tokens".
3. **A token relabelled as authority for a different service** without an exchange step.
4. **Happy path only** in a picture meant to show enforcement.
5. **Secrets or real endpoint values on the figure**, or specialist abbreviations in the plain-language variant.

## Drawing recipe
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

## Evidence in a code repository
- **Inputs:** authentication middleware, callback and session handlers, configured issuer and audience names, client-registration declarations, downstream API clients, permission dependencies, route registration, denial tests, token renewal handling.
- **Read setting names, not secret values.**
- **Declarations are not behaviour:** code shows intent; the deployed identity provider's consent and client configuration stay unverified unless the user confirms them.
- **Must come from people:** which identity choices are decided versus open, and the proposed flow.

## Guided-mode questions
1. Browser sign-in, a service acting for a user, or a machine-only call? (browser sign-in followed by one API call)
2. Business owners or protocol implementers as audience? (implementers, with a plain-language caption)
3. Which operation and systems, and current or proposed behaviour? (one read operation, current)
4. Which identity choices are confirmed and which are undecided? (mark undecided ones as proposed)
5. Is renewal or revocation the main concern, or a separate scenario? (separate scenario)

## Template
Model template: `assets/templates/F1.json` · Layout template: `sequence` · participants are `lifeline` nodes (person, client, identity provider, API, resource); proofs and requests are numbered `message` edges with `step`; the allow/refuse alternative is a `frames` entry labelled `alt` over its step range; verification and enforcement are `activations` on the identity provider and the API.

## Sample
Figure: `samples/F1-authentication-authorization-flow.svg` (published with the site)
