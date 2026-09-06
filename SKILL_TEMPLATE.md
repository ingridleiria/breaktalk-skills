# Skill template

Copy this into `<track>/<skill-name>/SKILL.md` and replace everything. The folder name and the `name` field must match.

Write it so it works anywhere. The body should read as a method a competent person could follow, with nothing that depends on one assistant, one tool, or one vendor's feature. Where a tool would help, say what it is for and what to do when it is unavailable.

```markdown
---
name: skill-name-in-kebab-case
description: One or two sentences on what the skill enforces, then the phrases that should trigger it. Write the triggers as people actually say them, including the vague ones, because this field is the only thing deciding whether the skill loads. "Use this skill whenever the user asks to X, mentions Y, or says Z."
---

# Skill Name

One short paragraph naming the failure this skill exists to prevent. Not what it does, what goes wrong without it. If you cannot name a specific failure, the skill is probably not worth writing.

## The method

The steps in the order they are actually performed, with the judgement calls made explicit. Number them when order matters and use headings when it does not. Say what to do when an input is missing, because that is the case that produces confident nonsense.

Where the skill depends on something specific to an organisation, keep it in a separate local file the user writes once, and say here what that file must contain.

## Output

The shape of the deliverable. A table, a document structure, a block of fields. Being concrete here is what makes two runs comparable.

## Quality bar

- Four to six lines, each one checkable by reading the output.
- Written as standards, not aspirations. "Every figure traced to a source cell" passes this test. "Thorough analysis" does not.
- The line you would check first if you had thirty seconds goes first.
```

## Notes

The `description` is the load-bearing field wherever the assistant loads skills automatically. A perfect skill that never triggers is worth nothing, and the most common reason a skill does not trigger is that its description describes the contents rather than the request. Where you paste the file in by hand, the description is just a summary and the body does all the work.

The quality bar is the second most important part. It is what turns a document into a standard, and it is the section to write first if you are stuck.

Keep the whole file under roughly two hundred lines. Longer than that and the parts stop being read, which defeats the purpose.
