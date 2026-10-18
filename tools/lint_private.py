#!/usr/bin/env python3
"""Scan the repository for private or customer content before publishing.

Generic patterns (home paths, keys, tokens, internal hosts, account-like ids,
email addresses) come from tools/lint_private.yaml. Words that identify private
organisations, people or products must never be committed, so they are read
from a file outside the repository:

  --names-file PATH            or   ARCHATLAS_PRIVATE_NAMES_FILE=PATH

One term per line, `#` comments allowed, matched as whole words. Use `prefix:NAME_`
to catch a private identifier prefix and all its suffixes. An all-lowercase
term matches any case, a term with capitals matches that exact spelling. Hits on such terms are reported by line number in the names file, never
by the word itself, so CI logs stay clean.

Exit codes: 0 clean, 1 findings (errors, or warnings with --strict), 2 tool error.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = Path(__file__).with_suffix(".yaml")
MAX_BYTES = 2_000_000


@dataclass
class Finding:
    path: str
    line: int
    rule: str
    severity: str
    message: str
    excerpt: str


def load_config(path: Path) -> dict:
    cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    for r in cfg["rules"]:
        r["regex"] = re.compile(r["pattern"])
    return cfg


def load_names(path: Path | None) -> list[tuple[int, re.Pattern]]:
    if not path:
        return []
    names = []
    for no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        term = raw.split("#", 1)[0].strip()
        if term:
            prefix = term.startswith("prefix:")
            if prefix:
                term = term.removeprefix("prefix:").strip()
                if not term or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", term):
                    raise ValueError(f"invalid identifier prefix on names file line {no}")
            # Whole-word for Latin terms; plain substring when the term contains CJK.
            body = re.escape(term)
            pat = (rf"(?<![\w]){body}\w*" if prefix else
                   body if re.search(r"[^\x00-\x7f]", term) else rf"(?<![\w]){body}(?![\w])")
            names.append((no, re.compile(pat, 0 if term != term.lower() else re.I)))
    return names


def tracked_files(root: Path) -> list[Path]:
    out = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=True)
    return [root / p for p in out.stdout.decode().split("\0") if p]


def all_files(root: Path) -> list[Path]:
    skip = {".git", "node_modules", ".venv", "__pycache__", "dist", "cache"}
    return [p for p in root.rglob("*") if p.is_file() and not (set(p.relative_to(root).parts) & skip)]


def matches(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch("/" + rel, "*/" + g.lstrip("*/")) for g in globs)


def email_allowed(addr: str, cfg: dict) -> bool:
    addr = addr.lower()
    domain = addr.rsplit("@", 1)[-1]
    return addr in {a.lower() for a in cfg.get("allow_emails", [])} or any(
        domain == d or domain.endswith("." + d) for d in cfg.get("allow_email_domains", []))


def scan_text(rel: str, text: str, cfg: dict, names, path: str | None = None) -> list[Finding]:
    """Scan text reported as `rel`; allow-list entries match `path` (default: rel)."""
    found = []
    allowed = {(a["rule"], a["path"]) for a in cfg.get("allow", [])}
    path = rel if path is None else path

    def is_allowed(rule: str) -> bool:
        return any(r == rule and fnmatch.fnmatch(path, p) for r, p in allowed)

    for no, line in enumerate(text.splitlines(), 1):
        for r in cfg["rules"]:
            if is_allowed(r["id"]):
                continue
            for m in r["regex"].finditer(line):
                if r["id"] == "email" and email_allowed(m.group(0), cfg):
                    continue
                found.append(Finding(rel, no, r["id"], r["severity"], r["message"], m.group(0)[:80]))
        for name_no, rx in names:
            if rx.search(line):
                found.append(Finding(rel, no, "private-name", "error",
                                     f"term from names file line {name_no}", "<redacted>"))
    return found


def scan(root: Path, cfg: dict, names, every_file: bool) -> list[Finding]:
    findings = []
    for path in (all_files(root) if every_file else tracked_files(root)):
        rel = path.relative_to(root).as_posix()
        if matches(rel, cfg.get("skip_paths", [])) or not path.is_file():
            continue
        data = path.read_bytes()[:MAX_BYTES]
        if b"\0" in data[:8192]:
            continue  # binary
        findings += scan_text(rel, data.decode("utf-8", errors="replace"), cfg, names)
        # The path itself can leak names too.
        findings += [Finding(rel, 0, f.rule, f.severity, f.message + " (in file path)", f.excerpt)
                     for f in scan_text(rel, rel, {**cfg, "rules": []}, names)]
    return findings


def scan_history(root: Path, cfg: dict, names) -> list[Finding]:
    """Added lines and commit metadata in every commit: published history must be clean too."""
    log = subprocess.run(["git", "-C", str(root), "log", "--all", "-p", "--no-color", "--format=commit %H%n%an <%ae>%n%B"],
                         capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
    findings, commit, path = [], "", ""
    keep = []
    for line in log.splitlines():
        if line.startswith("commit "):
            commit = line.split()[1][:12]
            path = ""  # Each commit's metadata is independent of the previous diff.
        elif line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else line[4:]
        elif line.startswith("diff --git"):
            path = ""
        elif line.startswith("+") or not path:
            keep.append((f"{commit}:{path or '<message>'}", line[1:] if path else line))
    for where, text in keep:
        file_path = where.split(":", 1)[1]
        if matches(file_path, cfg.get("skip_paths", [])):
            continue
        findings += scan_text(where, text, cfg, names, path=file_path)
    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--config", type=Path, default=CONFIG)
    ap.add_argument("--names-file", type=Path,
                    default=Path(os.environ["ARCHATLAS_PRIVATE_NAMES_FILE"])
                    if os.environ.get("ARCHATLAS_PRIVATE_NAMES_FILE") else None)
    ap.add_argument("--all-files", action="store_true", help="scan the working tree, not only git-tracked files")
    ap.add_argument("--history", action="store_true", help="also scan every commit (added lines and messages)")
    ap.add_argument("--strict", action="store_true", help="warnings also fail")
    ap.add_argument("--json", action="store_true", help="print findings as JSON")
    args = ap.parse_args(argv)
    try:
        cfg = load_config(args.config)
        if args.names_file and not args.names_file.is_file():
            raise FileNotFoundError(f"names file not found: {args.names_file}")
        names_path = args.names_file.resolve() if args.names_file else None
        if names_path and names_path.is_relative_to(args.root.resolve()):
            raise ValueError("the private names file must live outside the repository")
        names = load_names(names_path)
        findings = scan(args.root.resolve(), cfg, names, args.all_files)
        if args.history:
            findings += scan_history(args.root.resolve(), cfg, names)
    except (OSError, ValueError, re.error, subprocess.CalledProcessError, yaml.YAMLError) as e:
        print(f"lint_private: {e}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps([f.__dict__ for f in findings], ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"{f.path}:{f.line}: {f.severity}: {f.rule}: {f.message}: {f.excerpt}")
        errors = sum(f.severity == "error" for f in findings)
        print(f"lint_private: {errors} error(s), {len(findings) - errors} warning(s); "
              f"names list: {'used' if args.names_file else 'not provided'}", file=sys.stderr)
    failing = [f for f in findings if f.severity == "error" or args.strict]
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
