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

## Development setup

You need Python 3.10+, Node (the version in `.nvmrc`) and GNU Make. From a fresh clone:

```sh
make setup    # python3 -m venv .venv && pip install -e '.[dev]' && npm run site:install
make check    # everything CI runs
```

`make check` runs these steps in order:

1. unit, geometry, golden and evaluation-harness tests (`pytest`);
2. the generator checks (`build_selection`, `build_skill_refs` and `build_samples`, each with `--check`);
3. the translation check (`i18n_check`);
4. the private-content lint over files and history (`lint_private --strict --history`);
5. packing the skill zip and verifying that it installs (`pack_skill --verify`);
6. the site check and build (`npm run check` and `npm run build`).

CI runs the same command.

Run a single step with `make test`, `make generated`, `make i18n`, `make lint`, `make pack`
or `make site`.

**Optional settings:**

- **Private-names lint:** set `ARCHATLAS_PRIVATE_NAMES_FILE` to a terms list kept outside
  the repository.
- **Release builds:** use `make check I18N_FLAGS=--release`, which turns stale translations
  into errors.
- **Fonts:** install Noto Sans and Noto Sans CJK if you want text measured with real fonts.

## Verify

Inspect affected diagrams and pages at desktop and mobile sizes. Geometry checks do not
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
