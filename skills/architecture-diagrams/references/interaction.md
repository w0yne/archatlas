# Interaction: modes, brief, questions, decision log

Read this in Step 0–3 of `SKILL.md`, and whenever you are unsure whether to ask or to decide.

## 1. Two modes, one workflow

| | Autonomous | Guided |
|---|---|---|
| Brief | Infer from the request. Put assumptions at the top of the reply. | Ask the missing fields one question at a time. Each question carries a recommended default ("I suggest X because Y — OK?"). |
| Type choice | Pick the best fit, name one runner-up. | Ask the "First questions" of `selection.md` §1 (audience and purpose → question → scope → current or target), skipping any already answered, then recommend one or two types. |
| Wireframe | Print it in the reply, then render in the same turn. | Print it and stop; render only after explicit approval. |
| Questions | Only when a wrong guess would change the meaning (see §3). | Also confirm inferred items (repository mode) and names. |
| Ambiguous quality words | Restate as a concrete property and carry on as an assumption. | Ask which concrete property is meant. |
| Revisions | Apply feedback, list what changed. | Same, and re-show the decision log. |

Both modes keep the same three gates: a one-paragraph brief, a text wireframe, and a self-review against `principles.md` before anything is shown.

## 2. Asking which mode (once)

If the user has not said, and the session is interactive, ask in plain chat:

> 1) **Autonomous** — I choose sensible defaults and tell you my assumptions.
> 2) **Guided** — we decide audience, diagram type and boundaries together first.

- A host question UI may be used for the same question; do not depend on one existing. Without it, a numbered question in ordinary chat is enough; wait for the reply.
- Clear cues count as the answer ("ask me", "walk me through" → guided; "just draw it", or a request that already fixes type, scope and audience → autonomous); say in one line which mode you took.
- Honour the answer for the whole task. Do not re-ask. Explicit user instructions beat these defaults.
- Non-interactive run (a headless prompt): use the mode in the prompt; if none, autonomous.
- If you must have an answer and cannot get one, end with `needs_input:` and the question. A timeout or silence is not approval, and you must not invent the user's decision.

## 3. When to ask even in autonomous mode

Ask only if a wrong guess would change the diagram's meaning:
- more than one deployment target, environment or product variant could be meant;
- the audience is unknown and the choice is business-level versus technical;
- documents and code conflict in a way that moves a box or a boundary;
- an evidence gap affects ownership or a boundary (for example who owns a data store);
- the user's request could mean two different diagram types with different answers.

Never ask about styling details, colours, exact routing or fonts. Decide, show the result, adjust on feedback.

## 4. The brief (seven fields)

```
audience:     who reads it, what they decide with it
question:     the one thing the diagram must answer
state:        as-is | to-be | both (as separate figures)
scope:        whole system | one subsystem | one scenario; what is explicitly out
language:     labels and text language(s)
format:       svg (default); other formats only through references/formats.md
constraints:  required names, existing diagrams to keep, size, delivery place
revision:     for a fix-up, the label languages found in the source (kept unless the user asks otherwise)
assumptions:  everything inferred rather than stated
```
Keep it to one paragraph in the reply. Update it when the user corrects something.

## 5. Question bank (ask only the relevant ones, in this order)

Each question comes with a recommendation. In guided mode, follow this checklist for every question:
1. Ask exactly one question per message, with its recommended default.
2. Stop and wait for the answer; do not add a second question, a draft or a render to that message.
3. Record the answer in the decision log, then ask the next question or show the wireframe.
**Budget:** skip anything the request, the chosen type or an earlier answer already settles. Ask the type-specific questions first, then the generic ones below; at most five questions before the wireframe. Fold the rest into the wireframe as stated defaults the user can correct.
1. **Audience and purpose** — business, technical, mixed? Review draft or final handout?
2. **Current or target state?** — or both as two figures.
3. **Type** — one or two candidates from the catalogue, with the reason for each.
4. **Depth of secondary elements** — one box for each non-focus subsystem, or expanded? Peers drawn smaller than the protagonist?
5. **External systems** — which to show, kept at the edge.
6. **Inside the main system** — what makes it distinctive (components, not feature lists).
7. **Interface labels** — a generic label, or named endpoints? (Some audiences do not want endpoint names.)
8. **Flows** — happy path only or error branches too? Where does the story start?
Type-specific questions live in `references/types/<code>-<slug>.md` (section "Guided-mode questions").

## 6. Plain-language restatements for vague words

When a quality word appears, restate it and confirm (guided) or assume it (autonomous):
- "intuitive / clearer" → structure is visible: what each system contains, how pieces connect, who can reach what; not simpler wording.
- "simple" → fewer elements at one level of abstraction, not fewer facts.
- "detailed / complete" → which extra layer of detail, for which audience?
- "professional" → standard notation and terms the audience already uses, without obscure acronyms.
- "business view" → no technology names or protocols; capabilities, actors and flows.

## 7. Answer first, then redraw

If the user's message mixes feedback and questions: answer the questions first, summarise the changes you plan, and ask for the go-ahead before redrawing. Keep what was accepted; do not redraw everything.

## 8. Decision log

Keep a compact log in the reply tail and carry accepted decisions into every revision:

```
decisions:
- D1 type: container diagram (runner-up: component)         source: user, round 1
- D2 state: to-be only                                       source: assumption
- D3 payment provider shown as one external box               source: user, round 2
open:
- Q1 which deployment target? (assumed: the production IaC)
```
Record the source of each decision (user, assumption, repository evidence). A later change keeps the old line struck out with the reason.

## 9. Plain-language mode fallback examples

- No question UI available: send the numbered question and stop; continue when the reply arrives.
- Headless and `mode=guided` given: ask the first question and report `needs_input:` so the driver can answer.
- The user answers "whatever you think": treat as autonomous for the remainder, say so in one line.
