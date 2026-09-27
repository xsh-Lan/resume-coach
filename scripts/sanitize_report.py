#!/usr/bin/env python3
"""Post-write sanitizer for 简历 雷达 outputs.

Removes configured names and contact identifiers from report files while keeping
school names and resume content. Intended for Markdown/text report outputs.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
PRIVACY_FILE = PLUGIN_ROOT / "config" / "privacy.json"

DEFAULT_DIRS = [
    Path(r"D:\project2\codex工作文件夹\Offer雷达体检报告"),
    Path(r"D:\project2\codex工作文件夹\简历雷达输出"),
]

TEXT_SUFFIXES = {".md", ".txt", ".json", ".csv", ".html"}
REPORT_NAME_HINTS = ("体检报告", "改写方案", "面试包", "resume-report", "rewrite", "interview")

EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<!\d)(?:\+?86[-\s]?)?1[3-9]\d{9}(?!\d)")
WECHAT_RE = re.compile(r"(?:微信|WeChat|wechat)\s*[:：]?\s*[A-Za-z0-9_\-]{5,}")
QQ_RE = re.compile(r"(?:QQ|qq)\s*[:：]?\s*\d{5,}")
NAME_MARKER_RE = re.compile(r"(?:\[姓名[：:][^\]]*\]|姓名[：:][^\r\n|；，。]{1,20})")
LINKEDIN_RE = re.compile(r"https?://(?:www\.)?linkedin\.com/[^\s|，。；）\]]+")

def load_names() -> list[str]:
    names: list[str] = []
    if PRIVACY_FILE.exists():
        try:
            data = json.loads(PRIVACY_FILE.read_text(encoding="utf-8"))
            names = [str(x) for x in data.get("redact_names", []) if x]
        except Exception:
            pass
    return names

def sanitize_text(text: str, names: list[str]) -> str:
    text = NAME_MARKER_RE.sub("[姓名已删除]", text)
    text = EMAIL_RE.sub("[联系方式已删除]", text)
    text = PHONE_RE.sub("[联系方式已删除]", text)
    text = WECHAT_RE.sub("[联系方式已删除]", text)
    text = QQ_RE.sub("[联系方式已删除]", text)
    text = LINKEDIN_RE.sub("[联系方式已删除]", text)
    for name in sorted(names, key=len, reverse=True):
        if name:
            text = text.replace(name, "[姓名已删除]")
    return text

def should_process(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return False
    try:
        parent = path.resolve()
    except Exception:
        return False
    if any(parent.is_relative_to(d.resolve()) for d in DEFAULT_DIRS if d.exists()):
        return True
    return any(hint in path.name for hint in REPORT_NAME_HINTS)

def collect_paths(data: object) -> list[Path]:
    paths: list[Path] = []
    if isinstance(data, dict):
        for key in ("file_path", "path", "destination"):
            val = data.get(key)
            if isinstance(val, str):
                paths.append(Path(val))
        tool_input = data.get("tool_input")
        if isinstance(tool_input, dict):
            for key in ("file_path", "path"):
                val = tool_input.get(key)
                if isinstance(val, str):
                    paths.append(Path(val))
        tool_response = data.get("tool_response")
        if isinstance(tool_response, str):
            for m in re.finditer(r"(?<![A-Za-z])([A-Za-z]:\\[^\r\n\"']+|[A-Za-z]:/[^\r\n\"']+)", tool_response):
                paths.append(Path(m.group(1)))
        elif isinstance(tool_response, list):
            for item in tool_response:
                paths.extend(collect_paths(item))
    elif isinstance(data, list):
        for item in data:
            paths.extend(collect_paths(item))
    return paths

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", action="append", default=[])
    args, _ = parser.parse_known_args()
    names = load_names()
    targets: set[Path] = set()
    for arg in args.file:
        candidate = Path(arg)
        if candidate.is_file() and should_process(candidate):
            targets.add(candidate)
    for d in DEFAULT_DIRS:
        if d.exists():
            targets.update(p for p in d.rglob("*") if p.is_file() and should_process(p))

    raw = ""
    if not sys.stdin.isatty():
        try:
            raw = sys.stdin.read()
        except Exception:
            raw = ""
    if raw.strip():
        try:
            data = json.loads(raw)
        except Exception:
            data = None
        if data is not None:
            for p in collect_paths(data):
                if p.is_file() and should_process(p):
                    targets.add(p)

    changed = []
    for path in targets:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            new = sanitize_text(text, names)
            if new != text:
                path.write_text(new, encoding="utf-8")
                changed.append(str(path))
        except Exception:
            continue

    if changed:
        print(f"[resume-radar-sanitizer] sanitized {len(changed)} file(s)")
        for p in changed:
            print(" -", p)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
