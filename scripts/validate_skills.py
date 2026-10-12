#!/usr/bin/env python3
"""Validate this library's flat skill layout, metadata, and local Markdown links.

Uses only the Python standard library. Required frontmatter values use simple
single-line scalars; this is intentionally not a general-purpose YAML parser.
Output-document placeholders in templates are allowed.
"""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
INLINE_LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\n]+)\)")
REFERENCE_LINK = re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", re.MULTILINE)


def scalar(raw):
    """Read the supported single-line frontmatter scalar format."""
    raw = raw.strip()
    if not raw or re.fullmatch(r"[|>][-+0-9]?", raw):
        raise ValueError("use a nonempty single-line value")
    if raw.startswith('"'):
        value = json.loads(raw)
    elif raw.startswith("'"):
        if len(raw) < 2 or not raw.endswith("'"):
            raise ValueError("unterminated quoted value")
        value = raw[1:-1].replace("''", "'")
    else:
        value = raw.split(" #", 1)[0].strip()
        if value in {"null", "~", "true", "false"}:
            raise ValueError("value must be a string")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("value must be a nonempty string")
    return value


def metadata_errors(path, text):
    match = FRONTMATTER.match(text)
    if not match:
        return [f"{path}: missing or malformed YAML frontmatter"]
    errors = []
    fields = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^(name|description):\s*(.*)$", line)
        if not item:
            continue
        key, raw = item.groups()
        if key in fields:
            errors.append(f"{path}: duplicate {key}")
        fields[key] = raw
    values = {}
    for key in ("name", "description"):
        if key not in fields:
            errors.append(f"{path}: missing {key}")
            continue
        try:
            values[key] = scalar(fields[key])
        except ValueError as exc:
            errors.append(f"{path}: invalid {key}: {exc}")
    name = values.get("name")
    if name is not None:
        if len(name) > 64 or not NAME.fullmatch(name):
            errors.append(f"{path}: name must be 1-64 lowercase letters/digits with single hyphens")
        if name != path.parent.name:
            errors.append(f"{path}: name must match folder '{path.parent.name}'")
    description = values.get("description")
    if description is not None and len(description) > 1024:
        errors.append(f"{path}: description exceeds 1024 characters")
    return errors


def without_code(text):
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.sub(r"(`+).*?\1", "", "\n".join(lines))


def link_errors(path, text, allowed_root):
    errors = []
    text = without_code(text)
    targets = INLINE_LINK.findall(text) + REFERENCE_LINK.findall(text)
    for raw in targets:
        raw = raw.strip()
        if raw.startswith("<"):
            target = raw[1:raw.index(">")]
        else:
            target = raw.split()[0] if raw else ""
        if "{{" in target and "}}" in target:
            continue  # Templates refer to destinations created in the user's project.
        parsed = urlsplit(target)
        if parsed.scheme in {"http", "https", "mailto"} or target.startswith("//"):
            continue
        if parsed.scheme:
            errors.append(f"{path}: unsupported link scheme in '{target}'")
            continue
        if not parsed.path:
            continue  # Fragment-only links refer to the current document.
        relative = unquote(parsed.path)
        if Path(relative).is_absolute() or relative.startswith("~/"):
            errors.append(f"{path}: local link must be relative: '{target}'")
            continue
        destination = (path.parent / relative).resolve()
        try:
            destination.relative_to(allowed_root.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes its portable package: '{target}'")
            continue
        if not destination.exists():
            errors.append(f"{path}: missing local link target '{target}'")
    return errors


def validate_library(root):
    root = Path(root).resolve()
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return [f"{root}: missing skills/ directory"]
    skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not skill_dirs:
        return [f"{skills_root}: no skill folders found"]
    errors = []
    documents = []
    for skill_dir in skill_dirs:
        entrypoint = skill_dir / "SKILL.md"
        if not entrypoint.is_file():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        try:
            errors.extend(metadata_errors(entrypoint, entrypoint.read_text(encoding="utf-8")))
        except (OSError, UnicodeError) as exc:
            errors.append(f"{entrypoint}: cannot read: {exc}")
        documents.extend((path, skill_dir) for path in skill_dir.rglob("*.md"))
    if (root / "README.md").is_file():
        documents.append((root / "README.md", root))
    for path, allowed_root in documents:
        try:
            errors.extend(link_errors(path, path.read_text(encoding="utf-8"), allowed_root))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{path}: cannot validate links: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_library(args.root)
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Skill layout, metadata, and local Markdown links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
