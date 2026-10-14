"""Headless host adapters for the evaluation harness."""
from .claude import ClaudeAdapter
from .codex import CodexAdapter
from .pi import PiAdapter

ADAPTERS = {a.name: a for a in (ClaudeAdapter, CodexAdapter, PiAdapter)}
