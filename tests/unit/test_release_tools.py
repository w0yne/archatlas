"""Core invariants of the release tools (lint_private, pack_skill)."""
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
