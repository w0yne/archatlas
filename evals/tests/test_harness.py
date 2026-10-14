"""Core invariants of the evaluation harness. Run: python3 -m unittest discover -s evals/tests"""
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import run_eval  # noqa: E402
from adapters import ADAPTERS  # noqa: E402
from adapters.base import Sandbox, isolated_env  # noqa: E402


class ScenarioTest(unittest.TestCase):
    def setUp(self):
        self.scenarios = run_eval.load_scenarios()

    def test_scenario_set_matches_design(self):
        tasks = [s for s in self.scenarios.values() if s.get("kind") != "trigger"]
        self.assertGreaterEqual(len(tasks), 10)
        for s in tasks:
            for key in ("id", "title", "modes", "lang", "prompt", "expect", "expected_types"):
                self.assertTrue(s.get(key), f"{s['_file']}: {key}")
            if "guided" in s["modes"]:
                self.assertTrue(s.get("scripted_answers"), f"{s['_file']}: guided needs scripted answers")
        repos = [s["fixture"] for s in tasks if (s.get("fixture") or {}).get("repo")]
        self.assertGreaterEqual(len(repos), 2)
        for fx in repos:
            self.assertRegex(fx["commit"], r"^[0-9a-f]{40}$", "repositories are pinned by full commit")
            self.assertTrue(fx["repo"].startswith("https://github.com/"))
        for s in tasks:
            for src in ((s.get("fixture") or {}).get("files") or {}).values():
                self.assertTrue((run_eval.FIXTURES / src).is_file(), src)
        self.assertTrue(any((s.get("environment") or {}).get("no_browser") for s in tasks))

    def test_trigger_set_has_six_positives_and_six_near_misses(self):
        items = self.scenarios["T"]["items"]
        self.assertEqual(sum(i["should_trigger"] for i in items), 6)
        self.assertEqual(sum(not i["should_trigger"] for i in items), 6)
        for i in items:  # never invoked by name
            self.assertNotRegex(i["prompt"], r"architecture-diagrams|/skill:|\$architecture")


class IsolationTest(unittest.TestCase):
    def test_child_env_is_built_from_scratch(self):
        parent = {"RCC_CONTROL_DIR": "/x", "CYBERWARE_CONFIG": "/y", "PI_SESSION_FILE": "/z",
                  "CODEX_HOME": "/live", "AWS_PROFILE": "p", "HOME": "/home/real", "SECRET_TOKEN": "s"}
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(os.environ, parent, clear=True):
            sb = Sandbox(Path(d)).create()
            env = isolated_env(sb, "/usr/bin/git", {"AWS_REGION": "r"}, [])
            self.assertEqual(env["HOME"], str(sb.home))
            self.assertEqual(env["TMPDIR"], str(sb.tmp))
            for k, v in parent.items():
                self.assertNotEqual(env.get(k), v, k)
            with self.assertRaises(ValueError):
                isolated_env(sb, "/usr/bin/git", {}, ["RCC_CONTROL_DIR"])

    def test_host_state_stays_inside_the_sandbox(self):
        with tempfile.TemporaryDirectory() as d:
            sb = Sandbox(Path(d)).create()
            for name, cls in ADAPTERS.items():
                try:
                    adapter = cls({})
                except FileNotFoundError:
                    continue  # host not installed here
                self.assertTrue(str(adapter.state_dir(sb)).startswith(str(sb.root)), name)
                env = adapter.host_env(sb)
                for key in ("CODEX_HOME", "PI_CODING_AGENT_DIR"):
                    if key in env:
                        self.assertTrue(env[key].startswith(str(sb.root)), key)
                argv = " ".join(adapter.argv(sb, "p", None, False))
                self.assertNotIn(str(Path.home()), argv.replace(adapter.binary, ""), name)


class ChecksTest(unittest.TestCase):
    def test_skill_activation_needs_trace_evidence(self):
        def adapter(calls):
            return mock.Mock(skill_evidence=lambda rows, s: [], skill_listed=lambda rows, s: None,
                             tool_calls=lambda rows: calls)
        marker = ["You help a person pick the right architecture diagram"]
        # A skill location listed in the host's system prompt is not a load.
        quiet = ('{"type":"text","text":"I used the architecture-diagrams skill"}\n'
                 '{"systemPrompt":"<location>/h/skills/architecture-diagrams/SKILL.md</location>"}')
        self.assertIs(run_eval.skill_status(adapter([]), quiet, marker, "architecture-diagrams", "noskill", False)["skill_loaded"], False)
        self.assertIs(run_eval.skill_status(adapter([]), quiet, marker, "architecture-diagrams", "skill", True)["skill_loaded"], False)
        self.assertEqual(run_eval.skill_status(adapter([]), quiet, marker, "architecture-diagrams", "skill", False)["skill_loaded"], "unknown")
        read = ['read {"path": "/s/architecture-diagrams/SKILL.md"}']
        self.assertIs(run_eval.skill_status(adapter(read), quiet, marker, "architecture-diagrams", "skill", True)["skill_loaded"], True)

    def test_svg_gate_flags_script_and_external_refs(self):
        with tempfile.TemporaryDirectory() as d:
            good, bad = Path(d, "good.svg"), Path(d, "bad.svg")
            good.write_text('<svg xmlns="http://www.w3.org/2000/svg"><title>t</title></svg>')
            bad.write_text('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
                           '<script>x</script><image xlink:href="https://example.com/a.png"/></svg>')
            self.assertTrue(run_eval.svg_checks(good)["gate_G5_pass"])
            res = run_eval.svg_checks(bad)
            self.assertFalse(res["gate_G5_pass"])
            self.assertTrue(res["script"] and res["external_refs"])


if __name__ == "__main__":
    unittest.main()


class TraceFactsTest(unittest.TestCase):
    def test_forbidden_counts_executed_commands_not_heredoc_text(self):
        written = "cat > README.md <<'EOF'\nRun ./mvnw spring-boot:run to start.\nEOF"
        self.assertEqual(run_eval.trace_facts([written])["trace"]["forbidden"], 0)
        self.assertEqual(run_eval.trace_facts(["cd fixture && ./mvnw spring-boot:run"])["trace"]["forbidden"], 1)
        self.assertEqual(run_eval.trace_facts(["docker compose up -d"])["trace"]["forbidden"], 1)

