## Method notes

### Setup
- **Installation.** The skill was installed from the release zip that `tools/pack_skill.py` builds at main `3847acb`, into each sandboxed host's skill directory. No renderer dependencies were preinstalled; that is the realistic install path (defect 1).
- **Models.**
  - Claude Code and Pi both ran `us.anthropic.claude-sonnet-5-5`, so their difference is the host's.
  - Codex ran `us.openai.gpt-6.1-sol`.
- **Guided scenarios** used the first listed mode and the scripted answers.
- **Grader.** A model grader (`evals/grade.py` with `evals/grader/prompt.md`) ran through Pi with no tools. It never graded its own model's output:
  - GPT-6.1 Sol graded the Claude Code and Pi runs;
  - Sonnet 5.5 graded the Codex runs.
- **What the grader saw:**
  - every agent message;
  - the produced files, with SVG source truncated;
  - up to 3 CairoSVG PNG renders;
  - the trace facts.
- **Automatic gates:**
  - G5 comes from `svg_checks`;
  - G4 is forced to fail when the trace shows an executed forbidden command;
  - G2 is set to n/a on Codex, whose JSON stream does not record image views.

### Trace facts
Trace facts count the agent's own tool calls, with heredoc bodies stripped before the forbidden-command match. The first version matched raw events, which:
- counted the skill text and system-prompt skill listings;
- flagged `spring-boot:run` written inside a README heredoc as an executed command.

Five S8 grades made with the wrong facts were re-graded; the superseded ones are kept beside them as `grade.v1.json`.

### No-skill arms and the trigger set
The no-skill arms stopped before the trigger set. Triggers need the skill installed, and the harness's `all` includes them.

### Codex trigger rerun
Codex's first trigger runs (T1, T2) used up the per-process budget of the scenario run and were rerun as a separate trigger pass; the superseded pair is kept outside the results.

### Cost
The report's cost line covers the runs and grades that count. Superseded runs and grades added about $0.7.

## Top 10 skill defects (input to the next revision)

**Evidence paths** are relative to the raw results root, which is gitignored and kept
outside the repository. Each run directory holds `turnN.events.jsonl`, `final.txt`, `out/`,
`record.json` and `grade.json`.

**Ordering:** by the number of affected with-skill runs and by severity.

### 1. The bundle's renderer always runs in estimate mode; there are no install instructions
- **Kind:** reference / renderer.
- **What happened:**
  - In 27 of 27 with-skill runs that rendered, the findings report `measured_with: estimate`.
  - No run installed `scripts/requirements.txt`.
  - Codex tried `pip install pillow fonttools cairosvg` 3 times (S2, S9, S10). Every attempt failed with `/usr/bin/python3: No module named pip`, and no agent tried `python3 -m venv`, which works on this host.
  - Nothing in the skill tells an agent what to install, how, or that it should.
- **Where the instructions fall short:**
  - The SKILL.md `compatibility` field says `pip install archatlas`, but that package is not published.
  - `references/rendering.md` has no install step at all.
- **Consequences:** wrong text widths, mid-word wraps (#3) and fallback fonts (#2).
- **Evidence:**
  - `results/claude-skill/S1-autonomous-claude-skill/final.txt` ("Pillow and fontTools are missing")
  - the `out/*findings.json` of every skill run
- **Fix:**
  - Add a "Set up the renderer" step to `rendering.md`: `python3 -m venv .atlas-venv && .atlas-venv/bin/pip install -r scripts/requirements.txt`, then `scripts/atlas fonts doctor`.
  - `scripts/atlas` should prefer that venv's interpreter when one exists.
  - Make `render` print the exact install command when it falls back to estimate mode.
  - Drop `pip install archatlas` until the package is published.

### 2. Chinese labels render as fallback boxes; one agent claimed they display correctly
- **Kind:** renderer / honesty.
- **What happened:**
  - S5 failed G1 for Claude and Pi with the skill.
  - Estimate mode writes `font-family="sans-serif"` with no CJK family, so the rendered preview shows tofu boxes.
  - Pi answered "中文显示正常" without inspecting a CJK-capable render.
- **Evidence:** `results/claude-skill/S5-autonomous-claude-skill/out/diagram.svg`, `results/pi-skill/S5-autonomous-pi-skill/grade.json`
- **Fix:**
  - Always emit an explicit CJK-capable font stack when the label language is zh (Noto Sans CJK SC, Source Han Sans SC, PingFang SC, Microsoft YaHei), even in estimate mode.
  - Make `check` raise a warning, not info, when a CJK run has no measured glyph coverage.
  - In `review.md`: never state that CJK displays correctly without a preview rendered with a CJK font.

### 3. Labels and names wrap mid-word
- **Kind:** renderer.
- **Examples:** "Checkou / t", "Shipp / ed", "PaymentRec / eived", "vet_speci / alties", even with plenty of free canvas.
- **Seen in:** S2, S4 and S8 on 4 skill runs.
- **Evidence:** `results/claude-skill/S4-autonomous-claude-skill/grade.json`, `results/pi-skill/S4-autonomous-pi-skill/grade.json`
- **Fix:**
  - Break only at word boundaries for Latin text.
  - Widen the box up to `size_hint` or the column width before breaking.
  - Add a `check` finding for intra-word breaks in Latin runs.

### 4. Routing folds back and shares segments
- **Kind:** renderer.
- **What happened:** 15 of 30 with-skill runs got grader comments about folded, long or shared connector segments. Examples:
  - the C4/E3 transitions share x=1068;
  - the storefront arrow folds around the mobile app;
  - the warehouse route runs back across the figure.
- **Effect:** this is the main reason the skill arm's median **flow** stays at 1–2.
- **Evidence:** `results/claude-skill/S1-autonomous-claude-skill/grade.json`, `results/pi-skill/S4-autonomous-pi-skill/grade.json`, `results/claude-skill/S7-autonomous-claude-skill/grade.json`
- **Fix:**
  - Penalise shared collinear segments between unrelated edges in `route.py`.
  - Prefer the side ports that face the target.
  - Make `check` report a warning for edges whose length exceeds 2× the Manhattan distance.

### 5. Sequence notation is lost: no reply or async messages, and frames have no operator or guard
- **Kind:** reference / template / renderer.
- **What happened:**
  - S2 failed G1 for Claude and Pi with the skill.
  - Every message was modelled as `kind: call`, and replies were not dashed.
  - The retry was drawn as an unguarded `opt` frame instead of `loop`/`alt [timeout]`.
- **Why:** `assets/templates/E1.json` contains only `call` edges. The `frames` field in `rendering.md` has a free `label`, with no `operator` or `guard`.
- **Evidence:** `results/claude-skill/S2-autonomous-claude-skill/out/model.json`, `results/pi-skill/S2-autonomous-pi-skill/grade.json`
- **Fix:**
  - Give the E1 template one `reply` (dashed) and one `async` message.
  - Add `frames[].operator` (`loop|alt|opt|par|break`) and `guard`, and render them as `loop [guard]`.
  - Add a type-reference line: "a retry is `loop [timeout, max 1]` or `alt`".

### 6. Legends show renderer tokens instead of meaning
- **Kind:** renderer / reference.
- **What happened:** 12 of 30 with-skill grades criticise the legend. It either shows "peer", "primary" or "call · dashed", or is missing where it is needed (initial/final symbols, arrow meaning). This is the same finding as R2 S-1.
- **Evidence:** `results/pi-skill/S3-guided-pi-skill/grade.json`, `results/pi-skill/S2-autonomous-pi-skill/grade.json`
- **Fix:**
  - Generate per-template default legend labels ("request", "reply", "transition", "trust boundary").
  - Let `meta.legend` override the automatic entries.
  - Never print a style token.

### 7. Mixed English/Chinese input labels are dropped when revising
- **Kind:** instruction.
- **What happened:** on S9, all three hosts deleted or translated the Chinese labels, with and without the skill.
- **Why:** the skill only has a single "output language" brief field. Nothing says to keep the source's language mix in a fix-up task.
- **Evidence:** `results/claude-skill/S9-autonomous-claude-skill/final.txt`, `results/codex-skill/S9-autonomous-codex-skill/grade.json`
- **Fix:**
  - In the brief, add: "for revisions, keep the existing label languages unless asked".
  - In `principles.md`, add: "fix fit with layout, not by deleting text".
  - Add a review checklist item that compares the label language before and after.

### 8. Autonomous mode does not show a wireframe, and guided mode asks several questions at once or proceeds before approval
- **Kind:** instruction.
- **Wireframe:** missing in S1 for Claude and Pi. Codex showed one.
- **Guided mode:**
  - S3 and S8 asked 2–3 questions in one turn.
  - Pi rendered in S3 before "Approved".
  - Claude continued with defaults in S8 before approval.
- **Effect:** the skill arm's median **compliance** is only 1–2.
- **Evidence:** `results/pi-skill/S1-autonomous-pi-skill/grade.json`, `results/pi-skill/S3-guided-pi-skill/turn4.final.txt`, `results/claude-skill/S8-guided-claude-skill/grade.json`
- **Fix:** move the wireframe into the reply template ("before rendering, print the wireframe block") and make the one-question rule an explicit numbered checklist item in SKILL.md, with a "stop and wait" line after each question.

### 9. Inferred evidence is not reflected on the figure, and paired views are dropped
- **Kind:** instruction / reference.
- **S7 (Pi):** evidence statuses were listed as inferred, but the edges were drawn solid because the agent never set `evidence.status` in the model.
- **S3 (all three hosts):** only the access matrix (F3) was delivered, without the trust or ownership figure (F2) that the request implied.
- **Evidence:** `results/pi-skill/S7-autonomous-pi-skill/grade.json`, `results/claude-skill/S3-guided-claude-skill/turn4.final.txt`
- **Fix:**
  - In `repo-analysis.md`, add a step: "copy each claim's status into `edges[].evidence.status`".
  - In `selection.md`, add a "pairs" rule: "who-may-do-what plus where trust changes → F3 + F2".

### 10. The skill triggers on non-software flowcharts, and visual-review claims cannot be checked on Codex
- **Kind:** instruction / process.
- **Trigger:** T10 ("flowchart of how to bake bread") loaded the skill on Codex and Pi. The description excludes charts, mockups and logos, but not non-software process flowcharts.
- **Codex review claims:** Codex runs said "Visual review done" 7 times. `codex exec --json` emits no image-view events, so G2 could not be judged and was set to n/a. The grader nevertheless lowered Codex's honesty scores.
- **Evidence:** `results/codex-triggers/T10-trigger-codex-skill/record.json`, `results/pi-skill/T10-trigger-pi-skill/record.json`, `results/codex-skill/S4-autonomous-codex-skill/final.txt`
- **Fix:**
  - Add "or flowcharts of non-software everyday processes" to the description's exclusions.
  - In `review.md`: state the evidence for a visual review (the image file opened) in the delivery summary, so it can be audited on any host.
