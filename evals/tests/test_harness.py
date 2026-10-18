"""Core invariants of the evaluation harness. Run: python3 -m unittest discover -s evals/tests"""
import json
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
        parent = {"ORCHESTRATOR_STATE": "/x", "PRIVATE_CONTROLLER": "/y", "PI_SESSION_FILE": "/z",
                  "CODEX_HOME": "/live", "AWS_PROFILE": "p", "HOME": "/home/real", "SECRET_TOKEN": "s"}
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(os.environ, parent, clear=True):
            sb = Sandbox(Path(d)).create()
            env = isolated_env(sb, "/usr/bin/git", {"AWS_REGION": "r"}, [])
            self.assertEqual(env["HOME"], str(sb.home))
            self.assertEqual(env["TMPDIR"], str(sb.tmp))
            for k, v in parent.items():
                self.assertNotEqual(env.get(k), v, k)
            with self.assertRaises(ValueError):
                isolated_env(sb, "/usr/bin/git", {}, ["ORCHESTRATOR_STATE"])

    def test_only_approved_explicit_names_are_forwarded(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(
                os.environ, {"OPENAI_API_KEY": "test-only", "AWS_PROFILE": "fixture",
                             "ARBITRARY_SESSION": "parent-state"}, clear=True):
            sb = Sandbox(Path(d)).create()
            env = isolated_env(sb, "/usr/bin/git", {}, ["OPENAI_API_KEY"])
            self.assertEqual(env["OPENAI_API_KEY"], "test-only")
            self.assertNotIn("AWS_PROFILE", env)
            self.assertNotIn("ARBITRARY_SESSION", env)
            for key in ["ARBITRARY_SESSION", "CODEX_HOME", "HOME", "PATH", "LD_PRELOAD"]:
                with self.subTest(key=key), self.assertRaises(ValueError):
                    isolated_env(sb, "/usr/bin/git", {}, [key])
            for override in [{"HOME": "/outside"}, {"PATH": "/outside"},
                             {"ARBITRARY_SESSION": "state"}, {"CODEX_HOME": "/outside"},
                             {"PI_TELEMETRY": "1"}]:
                with self.subTest(override=override), self.assertRaises(ValueError):
                    isolated_env(sb, "/usr/bin/git", override, [])
            outside = Path(d).parent / "outside-state"
            link = sb.home / "linked-state"
            link.symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                isolated_env(sb, "/usr/bin/git", {"CODEX_HOME": str(link)}, [])
            env = isolated_env(sb, "/usr/bin/git", {
                "CODEX_HOME": str(sb.home / ".codex"),
                "PLAYWRIGHT_BROWSERS_PATH": str(sb.root / "no-browsers"),
                "CLAUDE_CODE_USE_BEDROCK": "1",
            }, [])
            self.assertEqual(env["CODEX_HOME"], str(sb.home / ".codex"))

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



class TraceFactsTest(unittest.TestCase):
    def test_forbidden_counts_executed_commands_not_heredoc_text(self):
        written = "cat > README.md <<'EOF'\nRun ./mvnw spring-boot:run to start.\nEOF"
        self.assertEqual(run_eval.trace_facts([written])["trace"]["forbidden"], 0)
        self.assertEqual(run_eval.trace_facts(["cd fixture && ./mvnw spring-boot:run"])["trace"]["forbidden"], 1)
        self.assertEqual(run_eval.trace_facts(["docker compose up -d"])["trace"]["forbidden"], 1)


class RescoreTest(unittest.TestCase):
    def test_rescored_grade_is_preferred_and_the_original_kept(self):
        import report
        with tempfile.TemporaryDirectory() as d:
            run = Path(d) / "results" / "S2-autonomous-codex-skill"
            run.mkdir(parents=True)
            (run / "record.json").write_text('{"run": "S2-autonomous-codex-skill", "host": "codex", "arm": "skill", "scenario": "S2"}')
            (run / "turn1.events.jsonl").write_text("")
            (run / "grade.json").write_text('{"grade": {"notes": "original"}}')
            runs, _ = report.load_runs([run.parent], grade_file="grade.rescored.json")
            self.assertEqual(runs[0]["_grade"]["grade"]["notes"], "original")
            self.assertFalse(runs[0]["_rescored"])
            (run / "grade.rescored.json").write_text('{"grade": {"notes": "rescored"}}')
            runs, _ = report.load_runs([run.parent], grade_file="grade.rescored.json")
            self.assertEqual(runs[0]["_grade"]["grade"]["notes"], "rescored")
            self.assertTrue(runs[0]["_rescored"])
            self.assertEqual(json.loads((run / "grade.json").read_text())["grade"]["notes"], "original")

    def test_single_trigger_item_can_be_selected(self):
        with mock.patch.object(run_eval, "run_one", return_value={"run": "x", "argv": []}) as run_one, \
                tempfile.TemporaryDirectory() as d:
            hosts = Path(d) / "hosts.yaml"
            hosts.write_text("pi: {model: m}\n")
            run_eval.main(["--hosts", str(hosts), "--scenario", "T5", "--host", "pi", "--out", str(Path(d) / "out"),
                           "--dry-run"])
            ids = [c.args[0]["id"] for c in run_one.call_args_list]
            self.assertEqual(ids, ["T5"])


class GalleryTest(unittest.TestCase):
    def test_inline_svg_is_sanitised_and_ids_are_prefixed(self):
        import gallery
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
               'width="10" height="10" onload="x()"><script>alert(1)</script>'
               '<foreignObject><div>x</div></foreignObject>'
               '<defs><marker id="arrow"/></defs><image href="https://example.com/a.png"/>'
               '<use xlink:href="#arrow"/><path marker-end="url(#arrow)" onclick="y()"/>'
               '<rect style="fill:url(https://example.com/x)"/></svg>')
        out = gallery.sanitise_svg(svg, "g1")
        for bad in ("script", "foreignObject", "onload", "onclick", "example.com"):
            self.assertNotIn(bad, out)
        self.assertIn('id="g1-arrow"', out)
        self.assertIn("url(#g1-arrow)", out)
        self.assertIn('href="#g1-arrow"', out)
        self.assertIsNone(gallery.sanitise_svg("<html/>", "g2"))


if __name__ == "__main__":
    unittest.main()
