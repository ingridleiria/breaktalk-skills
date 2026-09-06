#!/usr/bin/env python3
"""Report dash punctuation that should be reviewed in authored content."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATTERNS = (
    ("em dash", re.compile("\u2014")),
    ("en dash", re.compile("\u2013")),
    ("spaced hyphen", re.compile(r"(?<=\S)\s+-\s+(?=\S)")),
)


def inspect(text: str, source: str) -> int:
    issues = 0
    for line_number, line in enumerate(text.splitlines(), start=1):
        labels = [label for label, pattern in PATTERNS if pattern.search(line)]
        if labels:
            issues += len(labels)
            excerpt = line.strip()
            print(f"{source}:{line_number}: {', '.join(labels)}: {excerpt}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find em dashes, en dashes, and spaced hyphens used in text."
    )
    parser.add_argument("files", nargs="*", type=Path, help="UTF-8 text files")
    args = parser.parse_args()

    issues = 0
    if not args.files:
        issues += inspect(sys.stdin.read(), "<stdin>")
    else:
        for path in args.files:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                print(f"{path}: unable to read file: {exc}", file=sys.stderr)
                return 2
            issues += inspect(text, str(path))

    if issues:
        print(f"Found {issues} dash punctuation issue(s).", file=sys.stderr)
        return 1

    print("No prohibited dash punctuation found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
