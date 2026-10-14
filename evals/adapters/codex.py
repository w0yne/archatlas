"""Codex 0.160: `codex exec --json` with its own CODEX_HOME."""
from __future__ import annotations

from pathlib import Path

from .base import Adapter, Sandbox, Turn, copy_state_files, install_skill, jsonl


class CodexAdapter(Adapter):
    name = "codex"
    default_binary = "codex"
    invoke_prefix = "$architecture-diagrams"
    traces_image_views = False  # `codex exec --json` emits no event for viewing an image

    @property
    def sandbox(self) -> str:
        # workspace-write by default (DESIGN §8.4). Hosts where bubblewrap cannot create
        # namespaces must set `sandbox: danger-full-access` and rely on the temp sandbox.
        return self.cfg.get("sandbox", "workspace-write")

    def state_dir(self, sb: Sandbox) -> Path:
        return sb.home / ".codex"

    def prepare(self, sb: Sandbox, skill_dir: Path | None) -> None:
        state = self.state_dir(sb)
        state.mkdir(parents=True, exist_ok=True)
        copy_state_files(self.cfg.get("copy", {}), state)
        # Minimal config written fresh; `{state}` lets it point at copied files.
        (state / "config.toml").write_text(self.cfg.get("config_toml", "").replace("{state}", str(state)))
        if skill_dir:
            install_skill(skill_dir, state / "skills" / skill_dir.name)

    def host_env(self, sb: Sandbox) -> dict:
        env = {"CODEX_HOME": str(self.state_dir(sb))}
        env.update(self.cfg.get("env", {}))
        return env

    def argv(self, sb, prompt, session, multi_turn):
        last = str(sb.root / "codex-last-message.txt")
        opts = ["--json", "--output-last-message", last, "--ignore-rules",
                "-c", "check_for_update_on_startup=false"]
        if self.cfg.get("model"):
            opts += ["-m", self.cfg["model"]]
        if session:
            # `exec resume` has no --sandbox/-C; cwd is the workspace and the mode is set by config.
            return [self.binary, "exec", "resume", *opts, "-c", f'sandbox_mode="{self.sandbox}"',
                    session, prompt]
        opts += ["--sandbox", self.sandbox, "-C", str(sb.workspace)]
        if not multi_turn:
            opts.append("--ephemeral")
        return [self.binary, "exec", *opts, "--", prompt]

    def tool_calls(self, events):
        return [str((ev.get("item") or {}).get("command")) for ev in events
                if ev.get("type") == "item.started" and (ev.get("item") or {}).get("type") == "command_execution"]

    def assistant_texts(self, events):
        return [(ev.get("item") or {}).get("text") or "" for ev in events
                if ev.get("type") == "item.completed" and (ev.get("item") or {}).get("type") == "agent_message"]

    def parse(self, events, sb, tag, out_dir) -> Turn:
        t = Turn(exit_code=0, wall_s=0)
        usage = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}
        for ev in jsonl(events):
            if ev.get("type") == "thread.started":
                t.session = ev.get("thread_id")
            if ev.get("type") == "turn.completed":
                u = ev.get("usage") or {}
                usage["input"] += u.get("input_tokens") or 0
                usage["output"] += u.get("output_tokens") or 0
                usage["cache_read"] += u.get("cached_input_tokens") or 0
                usage["cache_write"] += u.get("cache_write_input_tokens") or 0
            item = ev.get("item") or {}
            if ev.get("type") == "item.completed" and item.get("type") == "agent_message":
                t.final_text = item.get("text") or t.final_text
        last = sb.root / "codex-last-message.txt"
        if last.exists():
            t.final_text = last.read_text(encoding="utf-8", errors="replace") or t.final_text
            last.replace(out_dir / f"{tag}.last-message.txt")
        t.usage = usage
        return t
