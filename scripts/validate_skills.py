#!/usr/bin/env python3
"""Check every skill against the house standard before a release.

Run: python3 scripts/validate_skills.py
Exits non-zero if any skill fails, so it can gate a release.
"""
import os, re, sys, json

TRACKS = ["chief-of-staff", "phd-research", "brand-and-writing",
          "commercial-and-data", "web-and-presentation"]

# A skill has to say when to use it, how, and what finished looks like.
REQUIRED_SIGNALS = {
    "when to use": [r"when to use", r"use this when", r"when not to"],
    "worked example": [r"worked example", r"situation", r"^## .*example"],
    "quality bar": [r"quality bar", r"finished when", r"checklist", r"guardrails",
                    r"anti-patterns", r"failure modes", r"mechanical checks", r"conduct"],
    "adaptation": [r"adapting this to your context"],
    "what not to change": [r"what not to change"],
}
MIN_BYTES = 8000          # anything shorter is a stub, not a method
BANNED = ["\u2014", "\u2013"]   # em dash and en dash, house style forbids both

def signals(text, patterns):
    low = text.lower()
    return any(re.search(p, low, re.M) for p in patterns)

def main():
    failures, skills = [], []
    for track in TRACKS:
        if not os.path.isdir(track):
            failures.append(f"missing track folder: {track}")
            continue
        for folder in sorted(os.listdir(track)):
            path = os.path.join(track, folder, "SKILL.md")
            if not os.path.isfile(path):
                continue
            text = open(path, encoding="utf-8").read()
            size = len(text.encode("utf-8"))
            skills.append(path)

            if not text.startswith("---"):
                failures.append(f"{path}: no frontmatter")
                continue
            fm = text.split("---")[1]
            name = re.search(r"^name:\s*(.+)$", fm, re.M)
            desc = re.search(r"^description:\s*(.+)$", fm, re.M | re.S)
            if not name:
                failures.append(f"{path}: frontmatter has no name")
            elif name.group(1).strip() != folder:
                failures.append(f"{path}: name '{name.group(1).strip()}' does not match folder '{folder}'")
            if not desc:
                failures.append(f"{path}: frontmatter has no description")
            if size < MIN_BYTES:
                failures.append(f"{path}: {size} bytes, under the {MIN_BYTES} byte floor")
            for label, patterns in REQUIRED_SIGNALS.items():
                if not signals(text, patterns):
                    failures.append(f"{path}: no {label} section")
            for ch in BANNED:
                if ch in text:
                    failures.append(f"{path}: contains a dash character, house style forbids it")
                    break

    print(f"checked {len(skills)} skills across {len(TRACKS)} tracks")
    if failures:
        print(f"\n{len(failures)} problems:")
        for f in failures:
            print("  " + f)
        sys.exit(1)
    print("all skills pass the house standard")

if __name__ == "__main__":
    main()
