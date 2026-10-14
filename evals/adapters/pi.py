"""Pi 1.1: `pi -p --mode json` with its own PI_CODING_AGENT_DIR."""
from __future__ import annotations

from pathlib import Path

from .base import Adapter, Sandbox, Turn, copy_state_files, jsonl


class PiAdapter(Adapter):
    name = "pi"
    default_binary = "pi"
    invoke_prefix = "/skill:architecture-diagrams"

    def __init__(self, cfg):
        super().__init__(cfg)
        self.skill_path: Path | None = None

    def state_dir(self, sb: Sandbox) -> Path:
        return sb.home / ".pi/agent"

    def prepare(self, sb: Sandbox, skill_dir: Path | None) -> None:
        self.state_dir(sb).mkdir(parents=True, exist_ok=True)
        copy_state_files(self.cfg.get("copy", {}), self.state_dir(sb))
        self.skill_path = skill_dir  # passed explicitly with --skill; discovery stays off

    def host_env(self, sb: Sandbox) -> dict:
        env = {"PI_CODING_AGENT_DIR": str(self.state_dir(sb)), "PI_SKIP_VERSION_CHECK": "1",
               "PI_TELEMETRY": "0"}
        env.update(self.cfg.get("env", {}))
        return env

    def argv(self, sb, prompt, session, multi_turn):
        argv = [self.binary, "-p", "--mode", "json", "--no-extensions", "--no-skills",
                "--no-mcp", "--no-prompt-templates", "--no-themes"]
        if self.cfg.get("provider"):
            argv += ["--provider", self.cfg["provider"]]
        if self.cfg.get("model"):
            argv += ["--model", self.cfg["model"]]
        if self.skill_path:
            argv += ["--skill", str(self.skill_path)]
        if multi_turn:
            argv += ["--session-dir", str(sb.root / "pi-sessions")]
            if session:
                argv += ["--session", session]
        else:
            argv.append("--no-session")
        return argv + ["--", prompt]

    def parse(self, events, sb, tag, out_dir) -> Turn:
        t = Turn(exit_code=0, wall_s=0)
        usage = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}
        cost = 0.0
        for ev in jsonl(events):
            if ev.get("type") == "session":
                t.session = ev.get("id")
            msg = ev.get("message") or {}
            if ev.get("type") == "message_end" and msg.get("role") == "assistant":
                u = msg.get("usage") or {}
                for k, src in (("input", "input"), ("output", "output"),
                               ("cache_read", "cacheRead"), ("cache_write", "cacheWrite")):
                    usage[k] += u.get(src) or 0
                cost += (u.get("cost") or {}).get("total") or 0
                text = "".join(c.get("text", "") for c in msg.get("content", [])
                               if isinstance(c, dict) and c.get("type") == "text")
                if text:
                    t.final_text = text
        t.usage, t.cost_usd = usage, round(cost, 6)
        return t
