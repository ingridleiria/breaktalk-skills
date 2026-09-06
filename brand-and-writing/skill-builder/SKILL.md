---
name: skill-builder
description: Guides the creation, testing, and improvement of Claude skills: choosing what deserves a skill, writing a description that triggers reliably, structuring instructions that enforce a standard rather than describe a topic, adding references and scripts, testing against real tasks, and packaging for sharing. Use this skill whenever the user wants to write a new skill, improve an existing one, asks why a skill did not trigger, wants to turn a repeated workflow or a set of instructions into a skill, asks how skills work, or wants to publish a skill library. Trigger for any request to create or edit a SKILL.md file.
---

# Skill Builder

A skill is a method written down in a form that executes. It does not make the model know more; it makes the model work to a standard, repeatably. The best skills encode a discipline the author already practices, with the tests they already apply, in the order they already apply them. This skill builds that kind and rejects the other kind.

## Step 1: Decide whether it should be a skill

A task deserves a skill when all three hold:

- It recurs, or will recur for other people.
- Its quality depends on discipline (a checkable method, a standard, an order of operations), not on taste or judgment that cannot be written down.
- The author can describe what a bad output looks like, specifically, because the skill's job is mostly to prevent that.

Skills for taste ("write beautifully"), for relationships, or for knowledge the model already has ("explain economics") do not work; say so and propose the workflow that would.

## Step 2: Extract the method

Interview the author (or examine their past outputs) for:

- The sequence they actually follow, including the steps they do before starting (the inputs they gather, the questions they ask).
- The standards they check against at the end, phrased as pass/fail tests.
- The failures they have seen and how each is prevented.
- The formats they produce and when each applies.
- The vocabulary they use and the vocabulary they ban.
- The tools or connectors involved, and the fallback when a tool is absent.

Write this down as a plain outline before touching the skill format.

## Step 3: Write the SKILL.md

**Frontmatter**

- `name`: the folder name, lowercase, hyphenated, specific (market-research, not research).
- `description`: the single most important field, because it decides whether the skill loads. Write it as: what the skill does (one sentence, the standard it enforces), then "Use this skill whenever the user..." followed by the concrete phrasings, task types, and situations that should trigger it, including casual phrasings and the cases where the user does not name the task explicitly. Aim for 80 to 150 words. A description that only names the topic under-triggers; one that lists the situations triggers correctly.

**Body**

- Open with two or three sentences stating the purpose and the standard, in the author's voice. This sets the register for the whole skill.
- Sequence: the steps in the order performed, with the inputs to gather before starting and what to do when they are missing.
- Standards: the rules as imperatives, specific enough to check ("every number carries a source and a year in the same sentence"), with the banned patterns named.
- Formats: the outputs and when each applies.
- Edge cases: the situations that break the default method and the handling for each.
- Cross-references: other skills to use for adjacent steps, named.
- A quality bar: four to six pass/fail tests applied before returning anything.

Length: 400 to 1,200 words of body for most skills. Longer skills put reference material (templates, long checklists, style tables, scripts) in a `references/` or `scripts/` folder and point to it from the body, so the always-loaded part stays focused.

**Writing rules for skills**

- Imperatives and short paragraphs; the model follows instructions better than descriptions.
- Concrete over abstract: an example of the required output beats a paragraph about quality.
- Name what to refuse to do as clearly as what to do.
- No dependence on a specific tool without a fallback; connectors come and go.
- No proprietary or confidential content in a skill that will be shared.
- Match the author's voice; a skill in generic prose produces generic output.

## Step 4: Test

Run the skill on three to five real tasks of the kind it targets, including one at the edge of scope and one phrased casually. Check: did it trigger; did the output follow the sequence; did the quality bar catch the failures it should; is anything in the skill ignored (delete it) or missing (add it). Compare with the same task run without the skill; if the difference is not visible, the skill is describing rather than enforcing.

## Step 5: Improve an existing skill

Read the skill and the outputs it has produced. Common repairs: a description that names a topic rather than situations (rewrite with triggers); instructions that explain the domain rather than the method (cut the explanation, keep the steps); standards without tests (rewrite as pass/fail); missing failure modes (add from the outputs that went wrong); length that buries the sequence (move reference material out). Keep a change log at the bottom of the skill.

## Step 6: Package and share

One folder per skill with SKILL.md at its root and optional `references/`, `scripts/`, and `assets/` subfolders. Zip each folder individually for Claude.ai upload; keep the source tree in a repository with a README listing every skill and its one-line purpose, a license, and installation instructions. Version releases; write release notes in the author's voice.

## Quality bar

- The description lists trigger situations, not just the topic.
- The body is a sequence with tests, not a description of a domain.
- The skill was run on real tasks and changed the output visibly.
- Nothing proprietary is in a shared skill.
- Reference material is separated from the always-loaded body.
