#!/usr/bin/env python3
"""Build the release zip of the skill and check that it installs.

The zip holds one folder, `architecture-diagrams/`, that works when copied into
any host's skills directory:
  - the skill files from skills/architecture-diagrams/
  - scripts/lib/archatlas/  the renderer library (pure Python), used by
    scripts/atlas when archatlas is not pip-installed
  - LICENSE, NOTICE, THIRD_PARTY_NOTICES.md
Third-party Python packages (Pillow, fonttools, jsonschema) are not bundled;
they are installed with `pip install -r scripts/requirements.txt`.

Usage:
  python3 tools/pack_skill.py [--out dist] [--verify]
The zip is deterministic: same inputs, same bytes.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "architecture-diagrams"
LIBRARY = ROOT / "src" / "archatlas"
LEGAL = ("LICENSE", "NOTICE", "THIRD_PARTY_NOTICES.md")
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
ZIP_DATE = (1980, 1, 1, 0, 0, 0)
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# User-level skills directories per host, relative to the user's home.
HOST_SKILL_DIRS = {
    "claude-code": ".claude/skills",
    "codex": ".codex/skills",
    "pi": ".pi/agent/skills",
    "agent-skills": ".agents/skills",
}


class PackError(Exception):
    pass


def frontmatter(skill_md: Path) -> tuple[dict, str]:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise PackError(f"{skill_md}: missing YAML frontmatter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def check_skill(folder: Path) -> list[str]:
    """Spec and layout checks; returns warnings, raises PackError on errors."""
    errors, warnings = [], []
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        raise PackError(f"{folder}: no SKILL.md")
    meta, body = frontmatter(skill_md)
    name = meta.get("name", "")
    if name != folder.name or not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"name {name!r} must be lowercase-hyphen, ≤64 chars and equal the folder {folder.name!r}")
    desc = meta.get("description") or ""
    if not desc or len(desc) > 1024:
        errors.append(f"description must be 1-1024 chars (has {len(desc)})")
    if not meta.get("license"):
        errors.append("license missing from frontmatter")
    lines = skill_md.read_text(encoding="utf-8").count("\n")
    if lines > 250:
        errors.append(f"SKILL.md has {lines} lines (limit 250)")
    for ref in sorted(set(re.findall(r"`((?:references|scripts|assets)/[^`\s<>*]+)`", body))):
        if not (folder / ref.rstrip("/")).exists():
            errors.append(f"SKILL.md references missing {ref}")
    sel = folder / "references" / "selection.md"
    if sel.is_file():
        for ref in sorted(set(re.findall(r"`(types/[^`\s<>]+\.md)`", sel.read_text(encoding="utf-8")))):
            if not (folder / "references" / ref).is_file():
                warnings.append(f"selection.md points to missing references/{ref}")
    atlas = folder / "scripts" / "atlas"
    if atlas.exists() and not os.access(atlas, os.X_OK):
        errors.append("scripts/atlas is not executable")
    if errors:
        raise PackError("\n".join(errors))
    return warnings


def stage(dest: Path) -> Path:
    folder = dest / SKILL.name
    shutil.copytree(SKILL, folder, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "lib"))
    shutil.copytree(LIBRARY, folder / "scripts" / "lib" / LIBRARY.name, ignore=IGNORE)
    for name in LEGAL:
        src = ROOT / name
        if not src.is_file():
            raise PackError(f"{name} missing at repository root")
        shutil.copyfile(src, folder / name)
    return folder


def write_zip(folder: Path, out: Path) -> None:
    files = sorted(p for p in folder.rglob("*") if p.is_file())
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in files:
            info = zipfile.ZipInfo(f"{folder.name}/{p.relative_to(folder).as_posix()}", ZIP_DATE)
            mode = 0o755 if os.access(p, os.X_OK) else 0o644
            info.external_attr = (stat.S_IFREG | mode) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, p.read_bytes())


def extract(zip_path: Path, dest: Path) -> None:
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            target = dest / info.filename
            if not target.resolve().is_relative_to(dest.resolve()):
                raise PackError(f"unsafe path in zip: {info.filename}")
            zf.extract(info, dest)
            mode = (info.external_attr >> 16) & 0o777
            if mode:
                target.chmod(mode)


def verify(zip_path: Path) -> list[str]:
    """Install into each host's user skills dir inside a temp HOME and check the layout."""
    report = []
    with tempfile.TemporaryDirectory(prefix="archatlas-pack-") as tmp:
        for host, rel in HOST_SKILL_DIRS.items():
            skills_dir = Path(tmp) / host / "home" / rel
            skills_dir.mkdir(parents=True)
            extract(zip_path, skills_dir)
            installed = skills_dir / SKILL.name
            check_skill(installed)
            if not (installed / "scripts" / "lib" / "archatlas" / "cli.py").is_file():
                raise PackError(f"{host}: vendored library missing")
            report.append(f"{host}: ~/{rel}/{SKILL.name}/SKILL.md ok")
        # The shim must reach the vendored library with no pip-installed archatlas.
        installed = Path(tmp) / "claude-code" / "home" / HOST_SKILL_DIRS["claude-code"] / SKILL.name
        env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(Path(tmp) / "claude-code" / "home"),
               "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1"}
        proc = subprocess.run([sys.executable, str(installed / "scripts" / "atlas"), "--help"],
                              capture_output=True, text=True, env=env, cwd=tmp, timeout=60)
        if proc.returncode == 0:
            report.append("scripts/atlas --help: ok (vendored library imported)")
        elif "Renderer unavailable" in proc.stderr or "No module named" in proc.stderr:
            report.append("scripts/atlas --help: dependencies missing here; "
                          f"install scripts/requirements.txt ({proc.stderr.strip().splitlines()[-1]})")
        else:
            raise PackError(f"scripts/atlas --help failed: {proc.stderr.strip()[-400:]}")
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=ROOT / "dist")
    ap.add_argument("--verify", action="store_true", help="install into temp host skill dirs and check")
    args = ap.parse_args(argv)
    try:
        warnings = check_skill(SKILL)
        version = str((frontmatter(SKILL / "SKILL.md")[0].get("metadata") or {}).get("version", "0.0.0"))
        args.out.mkdir(parents=True, exist_ok=True)
        zip_path = args.out / f"archatlas-skill-{version}.zip"
        with tempfile.TemporaryDirectory(prefix="archatlas-stage-") as tmp:
            write_zip(stage(Path(tmp)), zip_path)
        digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
        (args.out / f"{zip_path.name}.sha256").write_text(f"{digest}  {zip_path.name}\n")
        for w in warnings:
            print(f"warning: {w}")
        print(f"built {zip_path} ({zip_path.stat().st_size} bytes, sha256 {digest})")
        if args.verify:
            for line in verify(zip_path):
                print(f"verify: {line}")
    except PackError as e:
        print(f"pack_skill: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
