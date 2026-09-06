# Contributing

This library is opinionated on purpose, so the most useful contribution is usually not a new skill. It is a correction, a sharper standard, or a report that a skill did not load when it should have.

## Reporting something

Open an issue. The useful ones say what you asked for, which skill you expected to run, what came back, and what you wanted instead. If a skill produced confident output that was wrong, that is the highest priority thing in this repository and it should be reported even if you are not sure why.

## Improving a skill

Open a pull request against the `SKILL.md`. Small and specific beats large and general.

Every skill follows the structure in [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md): when to use and when not to, the inputs and what to do when one is missing, the method with its decision rules, at least one worked scenario in situation, task, action, result form with real numbers, the output shape, failure modes, edge cases, a checkable quality bar, and the related skills. A pull request that adds a section is more likely to be merged than one that adds a paragraph.

What gets merged:

- A clearer trigger phrase in the `description`, because that field is what decides whether the skill loads at all where loading is automatic.
- A fix for something that behaves differently on another assistant. These are written to be model-agnostic, and a report that a skill works in one and not another is useful even without a proposed fix.
- A tighter quality bar. If a criterion cannot be checked by reading the output, it is decoration and should be replaced by one that can.
- A step that closes a real failure you hit.
- A worked scenario from your own work, with the numbers changed. These are the hardest part to write and the most useful part to read.
- A correction. Wrong is wrong, and I would rather hear it from you than from a reader.

What does not get merged:

- Length for its own sake. Every added sentence has to earn the attention it takes from the ones already there.
- Generic advice a competent person already has. These files exist for the standards people skip under deadline, not for the ones they never knew.
- Anything that makes a skill sound more confident than the method supports.

## Adding a skill

Say in the pull request description what task it enforces a standard for, and why an existing skill does not cover it. New skills follow the house shape:

- Frontmatter with `name` matching the folder, and a `description` that lists the phrases people actually say, not a summary of the contents.
- Plain Markdown that reads as a method, with nothing specific to one assistant, one tool, or one vendor's feature.
- A short opening paragraph stating the failure the skill exists to prevent.
- The method, in the order it is actually done.
- A quality bar at the end, every line checkable by reading the output.

House style: no em dashes, no emoji, no filler. [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) is the empty shape and [skill-builder](brand-and-writing/skill-builder/SKILL.md) is the method.

## Forking

Forking is the expected case and needs no permission. MIT licence, so take it, rewrite it to your standards, and publish it under your own name. If you build something better from it, I would like to see it.
