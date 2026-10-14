# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

## Scope

Prefer a small change that improves a recurring problem. Explain the audience and
question before proposing a diagram, new rule or renderer feature. Keep customer data,
private paths, secrets and private conversation material out of the repository.

## Sources and licenses

Author new generic examples. Link to industry exemplars instead of copying images.
Check the actual license before importing code, fonts or artwork; preserve attribution.
Contributions to original project material are under Apache-2.0.

## Content and translations

English type pages are canonical; generated skill references must not be hand-edited.
Preserve the section IDs documented in the site. Chinese mirrors keep the same paths
and IDs, with translationOf, sourceRev and reviewed metadata. Flag unreviewed drafts.

## Verify

Run npm run site:install, npm run check and npm run build for site changes.
Inspect affected diagrams/pages at desktop and mobile sizes. Geometry checks do not
prove semantic correctness or visual quality. Include input, expected behavior, evidence,
and remaining limitations. Keep expensive cross-agent evals in trusted manual jobs.

## Developer Certificate of Origin

By signing off, you certify the contribution under the [DCO 1.1](https://developercertificate.org/).
Use git commit -s with your real contribution identity. No CLA is required. Do not add
someone else's sign-off or include private transcripts as evaluation evidence.

## Review

A maintainer reviews meaning, source provenance, licensing, accessibility and tests.
State whether a change affects installation, catalogue semantics, renderer output or
translations. Follow CODE_OF_CONDUCT.md and SECURITY.md.
