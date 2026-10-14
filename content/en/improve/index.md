---
title: Improve the skill
---
# Improve the skill

Useful changes explain a recurring problem, not a preference unique to one project.

## Contribute a small, reviewable change

1. Describe the misunderstanding or defect and the intended reader.
2. Supply a fresh generic example or a permissively licensed public source.
3. Change the smallest relevant reference, template or check.
4. Run make check and inspect the resulting image in both languages when affected.
5. Record what improved and what remains uncertain.

## Concrete checks and wrong-guidance reports

From an activated development environment, make check runs the tests, generators, translation check, private-content lint, pack verification and site build. The focused commands are:

    python -m pytest -q
    python tools/build_selection.py --check
    python tools/i18n_check.py
    python tools/lint_private.py --strict --history
    npm run check

Do not disable a failing check to publish. To report wrong or ambiguous type guidance, identify the type code, reader and question, quote the conflicting line, link a primary source, and propose a minimal correction. Use a generic reproduction in the repository issue tracker or send the report to a maintainer; never attach private diagrams.

## Content is a single source

Long-form type guidance lives under content/en/types; short skill references are generated from selected sections. Do not hand-edit generated copies. Each type page keeps stable section IDs: meaning, choose, notation, practice, exemplars, recipe, evidence, questions, template, sources and sample.

## Sources, privacy and licensing

No customer records, private paths, credentials, meeting transcripts or copied proprietary diagrams. Link to industry examples; check the specific asset license before reusing artwork. Code, documentation and original examples use Apache-2.0; third-party material retains its own terms.

## Translations

English is canonical. Chinese pages mirror the path and section IDs and carry translationOf, sourceRev and reviewed metadata. Mark machine drafts as under review. Re-layout localized labels rather than assuming English geometry fits Chinese.

## Contribution agreement

Contributions use the Developer Certificate of Origin, not a CLA. Sign off commits with your real contribution identity using git commit -s. Read the repository CONTRIBUTING documents for the review process.

Next: [evaluate changes](./evals).
