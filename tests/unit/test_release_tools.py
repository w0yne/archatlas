"""Core invariants of the release tools (lint_private, pack_skill)."""
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import lint_private  # noqa: E402
import pack_skill  # noqa: E402


def git_repo(test: unittest.TestCase, files: dict) -> Path:
    d = Path(tempfile.mkdtemp(prefix="lint-"))
    test.addCleanup(shutil.rmtree, d, True)
    for name, text in files.items():
        (d / name).write_text(text, encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=d, check=True)
    subprocess.run(["git", "add", "-A"], cwd=d, check=True)
    return d


class LintPrivateTest(unittest.TestCase):
    def test_detects_generic_leaks_and_allows_the_author(self):
        home = "/" + "home/alice/notes"
        key = "AKIA" + "ABCDEFGHIJKLMNOP"
        at = "@"
        lines = [home, key, "bob" + at + "corp-mail.test", "cnstwayne" + at + "gmail.com x" + at + "example.com"]
        repo = git_repo(self, {"a.md": "\n".join(lines) + "\n"})
        rules = {f.rule for f in lint_private.scan(repo, lint_private.load_config(lint_private.CONFIG), [], False)}
        self.assertEqual(rules, {"home-path", "aws-access-key", "email"})

    def test_private_names_come_from_outside_and_are_never_printed(self):
        repo = git_repo(self, {"a.md": "We built this for Acmecorp.\n"})
        names = repo.parent / (repo.name + ".names")
        names.write_text("Acmecorp\n")
        self.addCleanup(names.unlink)
        out = io.StringIO()
        with redirect_stdout(out):
            code = lint_private.main(["--root", str(repo), "--names-file", str(names)])
        self.assertEqual(code, 1)
        self.assertIn("names file line 1", out.getvalue())
        self.assertNotIn("Acmecorp", out.getvalue())
        inside = repo / "names.txt"
        inside.write_text("Acmecorp\n")
        self.assertEqual(lint_private.main(["--root", str(repo), "--names-file", str(inside)]), 2)

    def test_external_prefix_terms_detect_suffixes_without_disclosing_names(self):
        repo = git_repo(self, {"a.md": "EXAMPLE_PRIVATE_SESSION=value\npublic-maintainer/repo\n"})
        names = repo.parent / (repo.name + ".names")
        names.write_text("prefix:EXAMPLE_PRIVATE_\npublic-maintainer\n")
        self.addCleanup(names.unlink)
        out = io.StringIO()
        with redirect_stdout(out):
            code = lint_private.main(["--root", str(repo), "--names-file", str(names)])
        self.assertEqual(code, 1)
        self.assertIn("names file line 1", out.getvalue())
        self.assertIn("names file line 2", out.getvalue())
        self.assertNotIn("EXAMPLE_PRIVATE_", out.getvalue())
        self.assertNotIn("public-maintainer", out.getvalue())
        findings = lint_private.scan_text("a.md", "NOTEXAMPLE_PRIVATE_SESSION", {
            "rules": [], "allow": []}, lint_private.load_names(names))
        self.assertEqual(findings, [])

    def test_history_scans_metadata_after_a_previous_commit_diff(self):
        repo = git_repo(self, {"a.md": "ordinary text\n"})
        names = repo.parent / (repo.name + ".names")
        names.write_text("PublicOwner\n")
        self.addCleanup(names.unlink)
        log = (
            "commit aaaaaaaaaaaa\nPublicOwner <owner@example.com>\nfirst\n"
            "diff --git a/a.md b/a.md\n+++ b/a.md\n+ordinary text\n"
            "commit bbbbbbbbbbbb\nPublicOwner <owner@example.com>\nsecond\n"
            "diff --git a/a.md b/a.md\n+++ b/a.md\n+more text\n"
        )
        with mock.patch.object(lint_private.subprocess, "run", return_value=mock.Mock(stdout=log.encode())):
            findings = lint_private.scan_history(repo, lint_private.load_config(lint_private.CONFIG),
                                                 lint_private.load_names(names))
        self.assertEqual({f.path for f in findings if f.rule == "private-name"},
                         {"aaaaaaaaaaaa:<message>", "bbbbbbbbbbbb:<message>"})


class PackSkillTest(unittest.TestCase):
    def test_zip_is_deterministic_and_installs_for_every_host(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            with redirect_stdout(io.StringIO()):
                self.assertEqual(pack_skill.main(["--out", a]), 0)
                self.assertEqual(pack_skill.main(["--out", b]), 0)
            za, zb = sorted(Path(a).glob("*.zip")), sorted(Path(b).glob("*.zip"))
            self.assertEqual(len(za), 1)
            self.assertEqual(za[0].read_bytes(), zb[0].read_bytes())
            report = pack_skill.verify(za[0])
            self.assertEqual(sum(line.endswith("SKILL.md ok") for line in report), len(pack_skill.HOST_SKILL_DIRS))

    def test_local_state_in_the_skill_folder_is_not_packed(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "src" / pack_skill.SKILL.name
            shutil.copytree(pack_skill.SKILL, skill)
            for state in (".atlas-venv/pyvenv.cfg", "out/diagram.svg", "scripts/__pycache__/x.pyc"):
                (skill / state).parent.mkdir(parents=True, exist_ok=True)
                (skill / state).write_text("local\n")
            original = pack_skill.SKILL
            pack_skill.SKILL = skill
            self.addCleanup(setattr, pack_skill, "SKILL", original)
            staged = pack_skill.stage(Path(tmp) / "stage")
            packed = {p.relative_to(staged).as_posix() for p in staged.rglob("*")}
            self.assertIn("SKILL.md", packed)
            self.assertFalse({p for p in packed if p.startswith((".atlas-venv", "out"))})
            self.assertFalse({p for p in packed if "__pycache__" in p})


if __name__ == "__main__":
    unittest.main()
