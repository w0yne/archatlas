"""Claude Code 2.1.x: `claude -p --output-format stream-json`."""
from __future__ import annotations

from pathlib import Path

from .base import Adapter, Sandbox, Turn, copy_state_files, install_skill, jsonl


class ClaudeAdapter(Adapter):
    name = "claude"
    default_binary = "claude"
    invoke_prefix = "/architecture-diagrams"

    def state_dir(self, sb: Sandbox) -> Path:
        return sb.home / ".claude"

    def prepare(self, sb: Sandbox, skill_dir: Path | None) -> None:
        self.state_dir(sb).mkdir(parents=True, exist_ok=True)
        copy_state_files(self.cfg.get("copy", {}), self.state_dir(sb))
        if skill_dir:
            # Project skill: discovered from the workspace, never from the real HOME.
            install_skill(skill_dir, sb.workspace / ".claude/skills" / skill_dir.name)

    def host_env(self, sb: Sandbox) -> dict:
        env = {"DISABLE_AUTOUPDATER": "1", "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"}
        env.update(self.cfg.get("env", {}))
        return env

    def argv(self, sb, prompt, session, multi_turn):
        # Never --bare or --disable-slash-commands: they would hide the skill (DESIGN §8.4).
        argv = [self.binary, "-p", "--output-format", "stream-json", "--verbose",
                "--permission-mode", "acceptEdits",
                "--allowedTools", "Read,Write,Edit,Glob,Grep,Bash,Skill",
                "--setting-sources", "project"]
        if self.cfg.get("model"):
            argv += ["--model", self.cfg["model"]]
        if not multi_turn:
            argv.append("--no-session-persistence")
        if session:
            argv += ["--resume", session]
        return argv + ["--", prompt]

    def skill_evidence(self, events, skill):
        found = []
        for ev in events:
            for c in (ev.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") == "Skill" \
                        and skill in str(c.get("input")):
                    found.append("Skill tool call")
        return found

    def skill_listed(self, events, skill):
        for ev in events:
            if ev.get("type") == "system" and ev.get("subtype") == "init":
                return skill in (ev.get("slash_commands") or []) or skill in (ev.get("skills") or [])
        return None

    def parse(self, events, sb, tag, out_dir) -> Turn:
        t = Turn(exit_code=0, wall_s=0)
        for ev in jsonl(events):
            if ev.get("session_id"):
                t.session = ev["session_id"]
            if ev.get("type") == "result":
                t.final_text = ev.get("result") or ""
                u = ev.get("usage") or {}
                t.usage = {"input": u.get("input_tokens"), "output": u.get("output_tokens"),
                           "cache_read": u.get("cache_read_input_tokens"),
                           "cache_write": u.get("cache_creation_input_tokens")}
                t.cost_usd = ev.get("total_cost_usd")
        return t
