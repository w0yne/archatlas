"""Copied skill shims select a local interpreter without installing anything."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import venv


SHIM = Path(__file__).resolve().parents[2] / "skills/architecture-diagrams/scripts/atlas"
INSTALL_COMMAND = ("python3 -m venv .atlas-venv && "
                   ".atlas-venv/bin/python -m pip install -r scripts/requirements.txt")


class SkillVenvTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.skill = self.root / "copied skill"
        self.shim = self.skill / "scripts/atlas"
        self.shim.parent.mkdir(parents=True)
        shutil.copy2(SHIM, self.shim)
        self.env = dict(os.environ, PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1")
        self.env.pop("PYTHONHOME", None)
        self.env.pop("PYTHONPATH", None)

    def renderer(self, directory, origin):
        package = directory / "archatlas"
        package.mkdir(parents=True)
        (package / "__init__.py").write_text("")
        (package / "cli.py").write_text(
            "import json, sys\n"
            "def main():\n"
            f"    print(json.dumps(dict(origin={origin!r}, prefix=sys.prefix,\n"
            "                          executable=sys.executable, args=sys.argv[1:])))\n"
            "    return int(sys.argv[1])\n"
        )

    def run_shim(self, *args, interpreter=None, isolated=False):
        return subprocess.run(
            [str(interpreter or sys.executable), *(["-I", "-S"] if isolated else []),
             str(self.shim), *args],
            cwd=self.root, env=self.env, capture_output=True, text=True, timeout=15,
        )

    def test_missing_renderer_has_exact_relative_install_hint_and_exit_two(self):
        result = self.run_shim("--help", isolated=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("Renderer unavailable", result.stderr)
        self.assertIn("release bundle containing scripts/lib", result.stderr)
        self.assertIn("from the skill folder", result.stderr)
        self.assertIn(INSTALL_COMMAND, result.stderr)
        self.assertNotIn(str(self.root), result.stderr)
        self.assertFalse((self.skill / ".atlas-venv").exists())

    def test_without_venv_installed_renderer_and_bundle_precedence(self):
        installed = self.root / "installed"
        self.renderer(installed, "installed")
        self.env["PYTHONPATH"] = str(installed)
        result = self.run_shim("0")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["origin"], "installed")
        self.renderer(self.shim.parent / "lib", "bundled")
        result = self.run_shim("1", "argument with spaces")
        self.assertEqual(result.returncode, 1, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["origin"], "bundled")
        self.assertEqual(payload["args"], ["1", "argument with spaces"])
        self.assertFalse((self.skill / ".atlas-venv").exists())

    def test_local_venv_reexec_preserves_bundle_arguments_and_exit_codes(self):
        local_venv = self.skill / ".atlas-venv"
        venv.EnvBuilder(with_pip=False, symlinks=os.name != "nt").create(local_venv)
        python = local_venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        self.renderer(self.shim.parent / "lib", "bundled")
        installed = self.root / "installed"
        self.renderer(installed, "installed")
        self.env["PYTHONPATH"] = str(installed)
        # Both an unrelated active interpreter and direct venv invocation must
        # terminate, including when both executables resolve to the same binary.
        for interpreter, code in ((sys.executable, 1), (python, 2)):
            with self.subTest(interpreter=str(interpreter)):
                result = self.run_shim(str(code), "model with spaces.json",
                                       interpreter=interpreter)
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertEqual(result.stderr, "")
                payload = json.loads(result.stdout)
                self.assertEqual(Path(payload["prefix"]).resolve(), local_venv.resolve())
                self.assertEqual(Path(payload["executable"]), python)
                self.assertEqual(payload["origin"], "bundled")
                self.assertEqual(payload["args"], [str(code), "model with spaces.json"])
