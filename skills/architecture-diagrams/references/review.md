# Reviewing a rendered diagram

Two separate reviews: **semantic** (is it the right, truthful diagram?) and **geometric** (can it be read?). A passing automated check proves neither the meaning nor the look.

## 1. Order of work
semantic check → `scripts/atlas check` → fix → fresh render → visual review → fix → final render → report. Review the exact bytes you will deliver.

## 2. Semantic review (always, by text)
- Does the view answer the audience's question, at one level of abstraction?
- Are element kinds consistent within each row or group? Are boundaries explicit? Do labels describe real relationships?
- Are verified, inferred, proposed and target elements distinguishable? Is there any working note or status text on the figure?
- Is every number, badge or marker explained? Do step numbers match the sequence of events?
- Names and steps checked against the code or documents? (Repository mode: every arrow has an evidence row.)

## 3. Geometric review
Use `findings.json` from `scripts/atlas check` (fields: `id, severity, rule, element ids, boxes, message`). Fix errors; fix or justify warnings in the reply. Do not silence a whole rule; allow-list a specific element with a reason in the model.
Typical defects the checks look for: text outside its box, label background offset from its text, text over lines, node overlap, an arrow crossing an unrelated box or ending in the wrong group, a missing arrowhead target, low contrast, tofu or fallback glyphs in CJK text.

## 4. Visual review
First decide whether you can actually read images **on your real API route** (do not infer it from a model name).

**You can read images:**
1. Produce a preview (`scripts/atlas preview`) and, for several figures, a downscaled contact sheet (`scripts/atlas sheet`).
2. Look at the contact sheet first; open a full-size image only for complex or flagged figures.
3. **Open each image once.** Write the observations down immediately (element ids, what is wrong) instead of reopening. Keep a running count of images viewed in the session and stop near the host's limit; fall back to text checks and say so.
4. Look for: clipped or overlapping text, tiny text, lines through boxes, crossings, unreadable markers, blank space, CJK glyphs, light-on-light contrast, uneven spacing, the last page of a multi-figure document.
5. Report "visual review done" with what you looked at.

**You cannot read images (or the host rejects them):**
1. Run every text, geometry and, if available, browser check.
2. Produce the preview and contact sheet files and give their paths.
3. Report **"visual review pending"**, and say who needs to do it. Never write "visual pass" based on DOM or geometry checks alone.

**Large reviews:** split across sub-agents that return text only, each looking at a subset.

## 5. Independent review
For important deliverables, ask a second reviewer (a different model or a person) to look at the rendered result and the model, without the author's reasoning. Batch their findings into one revision rather than patching one by one.

## 6. Report format
```
type: sequence diagram       audience: developers      state: to-be
checks: structure ok, text-fit ok, overlap 0 errors / 1 warning (justified: ...), contrast ok
visual review: done (contact sheet + 2 full-size) | pending (no image input) 
verified: ...   inferred: ...   proposed: ...
open questions: ...
```
