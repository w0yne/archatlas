## Additional task: visual-quality note

Besides the rubric, judge the **visual quality** of the produced figures against the
style guide below (the renderer's default visual language) and the visual-hierarchy rules
of the skill. Look at the attached renders first; use the SVG source only to confirm.

Check:
- **Hierarchy and emphasis**: exactly one emphasised subject; everything else calm.
- **Zones**: boundaries, layers or lanes drawn as tinted groups with header bands, with
  consistent tint meaning.
- **Chips, badges, shapes**: short facts as chips rather than sentences; badges only for
  order and explained; shapes that separate kinds (store, queue, person).
- **Legend**: every colour, line style and badge explained in reader-facing words.
- **Readability**: no overlaps, clipped or tiny text, crossings or long detours; sensible
  density and whitespace.

Add one more key to your JSON object:

```json
"visual": {"score": 2, "hierarchy": 2, "zones": 2, "readability": 2,
           "verdict": "one sentence a reader can act on",
           "issues": ["up to 3 concrete visual problems"]}
```

Scores are integers 0–3 (0 missing or broken, 1 weak, 2 good with flaws, 3 exemplary).
If no figure was produced, set `visual` to `null`.
