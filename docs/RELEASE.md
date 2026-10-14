# Release checklist

[中文](#发布清单中文) · Applies to every tagged release, starting with v0.1.0. Tick each
item in the release pull request. Release tooling: `tools/lint_private.py` and
`tools/pack_skill.py`. CI job: `release-hygiene` in `.github/workflows/check.yml`.

## 1. Before the first public push (v0.1.0 only)

- [ ] **Names are free.**
  - GitHub organisation or repository `archatlas`, the PyPI project `archatlas` and the npm
    package `archatlas`.
  - Fallback: `archatlas-skill` (DESIGN §1).
  - Check the GitHub user namespace too. Also search GitHub for repositories with the same
    name in the same domain, which could confuse users.
- [ ] **History is clean.** Run `python3 tools/lint_private.py --history --strict
  --names-file <private list outside the repo>`. It should report 0 findings. Every commit is
  published, so a clean working tree is not enough.
- [ ] **Commit authors and messages are generic.** No internal hostnames, ticket ids or
  people other than the author.
- [ ] **The private names list exists only outside the repository.** For CI, it is stored as
  the repository secret `ARCHATLAS_PRIVATE_NAMES`, one term per line.

## 2. Licences

- [ ] `THIRD_PARTY_NOTICES.md` matches the current pins:
  - `skills/architecture-diagrams/scripts/requirements.txt`
  - `pyproject.toml`
  - `content/.vitepress/package-lock.json`
- [ ] No new dependency has a copyleft or unknown licence. If one does, decide how to handle
  it and record the decision in the notices file.
- [ ] No font, icon or image from a third party is in the repository or the zip. Run
  `git ls-files '*.ttf' '*.otf' '*.woff*' '*.png' '*.jpg'` to check.
- [ ] Sample 10 % of type pages. Check that standards are cited, not copied. Text adapted
  from arc42 (CC BY-SA) or the C4 model website (CC BY) needs the matching attribution, or
  must be rewritten.
- [ ] `LICENSE` (Apache-2.0), `NOTICE` and `THIRD_PARTY_NOTICES.md` are present. The pack
  script copies them into the zip.

## 3. Content and quality gates

- [ ] `python3 tools/lint_private.py --strict` → 0 findings. Without a names file, it uses the
  generic patterns only.
- [ ] Generators are up to date:
  - `python3 tools/build_selection.py --check`
  - `tools/build_skill_refs.py` (check mode)
  - `tools/i18n_check.py`
- [ ] Every type reference that `references/selection.md` points to exists.
  `pack_skill.py` prints a warning for each missing one; there must be none.
- [ ] Unit, geometry and golden tests pass, and `atlas check` reports 0 errors on all
  examples.
- [ ] CI is green on the release commit. That covers `site`, `release-hygiene` and the
  Pages build.
- [ ] Evaluation (DESIGN §8.5): the release gate is met, and the report with host versions
  is attached to the release notes.

## 4. Package

- [ ] Bump `metadata.version` in `SKILL.md` and `version` in `pyproject.toml`; they must
  match. Update `CHANGELOG.md`: move items out of *Unreleased*, and add the date and the
  compare link.
- [ ] `python3 tools/pack_skill.py --verify`. It produces
  `dist/archatlas-skill-<version>.zip` and a `.sha256` file. The check installs the zip
  into temporary Claude Code, Codex, Pi and `.agents` skill directories, and runs
  `scripts/atlas --help`.
- [ ] Install smoke test per host from the zip. In a clean HOME, ask for one diagram and
  confirm that the skill loads (see `evals/README.md`).

## 5. Publish

- [ ] Tag `v<version>` (annotated, signed if possible) on the reviewed commit, and push the
  tag.
- [ ] Create a GitHub release with the zip, the `.sha256` file and the changelog section.
- [ ] Deploy Pages from the tag. Then check the deployed URLs:
  - home, choose, three type pages and the use page, in English and Chinese;
  - internal links;
  - search for one English and one Chinese alias.
- [ ] Optional: publish the Python package to PyPI and the plugin wrappers.

---

## 发布清单（中文）

适用于每一个打 tag 的版本，从 v0.1.0 开始。发布 PR 里逐项勾选。

1. **首次公开推送前（仅 v0.1.0）**
   - 确认 GitHub 组织 / 仓库、PyPI、npm 上的 `archatlas` 名称可用，备选名为 `archatlas-skill`。另外在 GitHub 上搜一下有没有同领域的同名项目。
   - 用 `lint_private.py --history --strict` 并提供仓库外的私有词表，扫描**全部历史**，结果必须为 0。
   - commit 的作者和提交信息里不能出现内部信息。
   - 私有词表只能放在仓库外；CI 中通过 secret `ARCHATLAS_PRIVATE_NAMES` 提供。
2. **许可证**
   - `THIRD_PARTY_NOTICES.md` 与当前锁定的依赖版本一致。
   - 新依赖不能是 copyleft 或许可证未知；如果有，必须在该文件中写明处理决定。
   - 仓库和 zip 里不能有第三方字体、图标或图片。
   - 抽查 10% 的类型页：标准只能引用，不能复制。改写自 arc42（CC BY-SA）或 C4 网站（CC BY）的文字要按其许可证署名，否则重写。
3. **内容与质量**
   - lint 结果为 0。
   - 各生成器的 `--check` 都通过，i18n 检查通过。
   - `selection.md` 指向的类型参考文件都存在。
   - 测试通过，`atlas check` 对所有示例报 0 个错误。
   - CI 全绿。
   - 评测达到 DESIGN §8.5 的门槛。
4. **打包**
   - SKILL.md 和 pyproject 中的版本号一致，并更新 CHANGELOG。
   - 运行 `pack_skill.py --verify`，确认能安装到 Claude Code / Codex / Pi / .agents 的 skills 目录，且 `scripts/atlas --help` 正常。
   - 在每个宿主上从 zip 安装并做一次冒烟测试。
5. **发布**
   - 打 tag，创建 GitHub release，附上 zip、sha256 和 changelog。
   - 部署 Pages，部署后检查中英文页面、链接和搜索。
