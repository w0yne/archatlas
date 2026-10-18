"""Shared pieces for host adapters: sandbox layout, isolated environment, results."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path

# Exact provider/transport names, never wildcard prefixes. A configured pass_env
# entry is a second opt-in, not permission to inherit arbitrary host state.
PROVIDER_ENV = frozenset({
    "OPENAI_API_KEY", "OPENAI_BASE_URL", "ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL",
    "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "GEMINI_API_KEY", "GOOGLE_API_KEY",
    "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "AWS_PROFILE",
    "AWS_REGION", "AWS_DEFAULT_REGION", "AWS_CONFIG_FILE", "AWS_SHARED_CREDENTIALS_FILE",
    "AWS_EC2_METADATA_DISABLED", "HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY",
    "https_proxy", "http_proxy", "no_proxy", "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE",
    "NODE_EXTRA_CA_CERTS",
})
LITERAL_SETTINGS = frozenset({"CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX"})
SANDBOX_PATHS = frozenset({"CODEX_HOME", "PI_CODING_AGENT_DIR", "PLAYWRIGHT_BROWSERS_PATH"})
ISOLATION_SETTINGS = {
    "DISABLE_AUTOUPDATER": "1", "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "PI_SKIP_VERSION_CHECK": "1", "PI_TELEMETRY": "0",
}
SYSTEM_PATH = ("/usr/local/bin", "/usr/bin", "/bin")


@dataclass
class Sandbox:
    """One isolated run: its own HOME, temp dir and workspace, all under `root`."""
    root: Path

    @property
    def home(self) -> Path:
        return self.root / "home"

    @property
    def tmp(self) -> Path:
        return self.root / "tmp"

    @property
    def workspace(self) -> Path:
        return self.root / "workspace"

    def create(self) -> "Sandbox":
        for d in (self.home, self.tmp, self.workspace):
            d.mkdir(parents=True, exist_ok=True)
        return self


@dataclass
class Turn:
    exit_code: int
    wall_s: float
    final_text: str = ""
    session: str | None = None
    usage: dict = field(default_factory=dict)  # input, output, cache_read, cache_write
    cost_usd: float | None = None
    timed_out: bool = False


def isolated_env(sb: Sandbox, binary: str, host_env: dict, pass_env: list[str]) -> dict:
    """Build the child environment from scratch; nothing is inherited implicitly."""
    path = [str(Path(binary).resolve().parent)]
    node = shutil.which("node")
    if node:
        path.append(str(Path(node).resolve().parent))
    path += [p for p in SYSTEM_PATH if p not in path]
    env = {
        "HOME": str(sb.home),
        "TMPDIR": str(sb.tmp),
        "XDG_CONFIG_HOME": str(sb.home / ".config"),
        "XDG_CACHE_HOME": str(sb.home / ".cache"),
        "XDG_DATA_HOME": str(sb.home / ".local/share"),
        "XDG_STATE_HOME": str(sb.home / ".local/state"),
        "PATH": ":".join(dict.fromkeys(path)),
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "NO_COLOR": "1",
    }
    for name in pass_env:
        if name not in PROVIDER_ENV:
            raise ValueError(f"pass_env may not forward {name}")
        if name in os.environ:
            env[name] = os.environ[name]
    for name, value in host_env.items():
        value = str(value)
        if name in SANDBOX_PATHS:
            # resolve() also rejects a symlink that escapes the isolated root.
            if not Path(value).is_absolute() or not Path(value).resolve().is_relative_to(sb.root.resolve()):
                raise ValueError(f"{name} must remain inside the sandbox")
        elif name in ISOLATION_SETTINGS:
            if value != ISOLATION_SETTINGS[name]:
                raise ValueError(f"protected isolation setting: {name}")
        elif name not in PROVIDER_ENV | LITERAL_SETTINGS:
            raise ValueError(f"host env may not set {name}")
        env[name] = value
    return env


def run_process(argv: list[str], cwd: Path, env: dict, out_dir: Path, tag: str,
                timeout: int) -> tuple[int, float, str, bool]:
    """Run one headless invocation; stdout is saved as the event log."""
    out_dir.mkdir(parents=True, exist_ok=True)
    events = out_dir / f"{tag}.events.jsonl"
    stderr = out_dir / f"{tag}.stderr.txt"
    start = time.monotonic()
    timed_out = False
    with events.open("wb") as so, stderr.open("wb") as se:
        try:
            proc = subprocess.run(argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                                  stdout=so, stderr=se, timeout=timeout)
            code = proc.returncode
        except subprocess.TimeoutExpired:
            code, timed_out = 124, True
    wall = time.monotonic() - start
    (out_dir / f"{tag}.argv.json").write_text(json.dumps(argv, indent=2) + "\n")
    return code, wall, events.read_text(encoding="utf-8", errors="replace"), timed_out


def jsonl(text: str) -> list[dict]:
    rows = []
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("{"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def copy_state_files(copy: dict, state_dir: Path) -> None:
    """Copy named files (minimal auth/model config) into the host's sandbox state dir."""
    for dest, src in (copy or {}).items():
        target = state_dir / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(Path(src).expanduser(), target)
        target.chmod(0o600)


class Adapter:
    """One host CLI. Subclasses define how to configure, invoke and parse it."""
    name = ""
    default_binary = ""
    invoke_prefix = ""  # explicit skill invocation, prepended in the with-skill arm

    def __init__(self, cfg: dict):
        self.cfg = cfg or {}
        self.binary = shutil.which(self.cfg.get("binary", self.default_binary)) or ""
        if not self.binary:
            raise FileNotFoundError(f"{self.name}: binary {self.cfg.get('binary', self.default_binary)!r} not found")

    def state_dir(self, sb: Sandbox) -> Path:
        raise NotImplementedError

    def prepare(self, sb: Sandbox, skill_dir: Path | None) -> None:
        raise NotImplementedError

    def host_env(self, sb: Sandbox) -> dict:
        return dict(self.cfg.get("env", {}))

    def argv(self, sb: Sandbox, prompt: str, session: str | None, multi_turn: bool) -> list[str]:
        raise NotImplementedError

    def parse(self, events: str, sb: Sandbox, tag: str, out_dir: Path) -> Turn:
        raise NotImplementedError

    def skill_evidence(self, events: list[dict], skill: str) -> list[str]:
        """Host-specific proof in the event log that the skill was loaded."""
        return []

    # False when the host's event stream does not show image views (G2 cannot be judged from it).
    traces_image_views = True

    def tool_calls(self, events: list[dict]) -> list[str]:
        """The serialised inputs of the agent's tool calls (commands, file reads)."""
        return []

    def assistant_texts(self, events: list[dict]) -> list[str]:
        """Every text message the agent wrote, in order (the final reply is only the last one)."""
        return []

    def skill_listed(self, events: list[dict], skill: str) -> bool | None:
        """Whether the host reported the skill as available (None: host does not report)."""
        return None

    def turn(self, sb: Sandbox, prompt: str, session: str | None, multi_turn: bool,
             out_dir: Path, tag: str, timeout: int) -> Turn:
        env = isolated_env(sb, self.binary, self.host_env(sb), self.cfg.get("pass_env", []))
        (out_dir / "env-keys.json").parent.mkdir(parents=True, exist_ok=True)
        (out_dir / "env-keys.json").write_text(json.dumps(sorted(env), indent=2) + "\n")
        argv = self.argv(sb, prompt, session, multi_turn)
        code, wall, events, timed_out = run_process(argv, sb.workspace, env, out_dir, tag, timeout)
        t = self.parse(events, sb, tag, out_dir)
        t.exit_code, t.wall_s, t.timed_out = code, round(wall, 1), timed_out
        return t


def install_skill(skill_dir: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill_dir, dest)
