# Skill template

Every skill in this repository follows the structure below. Copy it into `<track>/<skill-name>/SKILL.md` and replace everything. The folder name and the `name` field must match.

Write it so it works anywhere. The body should read as a method a competent person could follow, with nothing that depends on one assistant, one tool, or one vendor's feature. Where a tool would help, say what it is for and what to do when it is unavailable.

## The structure

```markdown
---
name: skill-name-in-kebab-case
description: What the skill produces and the standard it enforces, then the phrases that should trigger it, written as people actually say them including the vague ones. This field is what decides whether the skill loads where loading is automatic.
---

# Skill Name

One or two paragraphs naming the failure this skill exists to prevent. Not what it does, what goes wrong without it, and what that costs. If you cannot name a specific failure, the skill is probably not worth writing.

## When to use this, and when not to

Two short lists. The cases this handles, and the adjacent cases that belong to a different skill or to no skill at all. Being explicit about what this is not for prevents the most common misuse.

## What you need before starting

Every input, why it matters, and what to do when it is missing. The last part is what separates a usable skill from a wish list: real work starts with three of the six inputs, and the method has to say whether to proceed on assumptions, ask, or stop.

## The method

The steps in the order they are actually performed. For each one: what is done, the judgement call inside it, and the rule for making that call. Number them where order matters.

Include the decision rules explicitly. "Choose the right approach" is not a method; "use A when the data is X, B when it is Y, and if you cannot tell, do the cheap version of A first" is.

## Worked example

At least one, in situation, task, action, result form, with real numbers and real names invented for the purpose. Not a summary of the method restated with placeholders. A reader should be able to see the judgement being exercised, including where it was uncertain.

**Situation.** The context, concretely, with the constraints that shaped it.

**Task.** What had to be produced and by when, and what would count as good.

**Action.** What was actually done, step by step, including the wrong turn and why it was abandoned.

**Result.** What came out, what happened next, and what it cost or saved. Where an outcome is uncertain, say so rather than inventing a clean ending.

Add a second scenario where the skill behaves differently under different conditions, and label what changed.

## Output

The shape of the deliverable, close enough to copy. A table with its columns, a document with its sections, a block of fields. Being concrete here is what makes two runs comparable and what saves the reader the hardest part.

## Failure modes

The specific ways this goes wrong, each with how to recognise it and what to do instead. Write them from experience, not from imagination: the useful ones are the mistakes competent people actually make under deadline.

## Edge cases

The situations where the standard method does not apply, and what to do in each. Small data, no data, a hostile audience, a decision already made, a constraint discovered late.

## Quality bar

- Four to eight lines, each one checkable by reading the output.
- Written as standards, not aspirations. "Every figure traced to a source cell" passes this test. "Thorough analysis" does not.
- The line you would check first if you had thirty seconds goes first.

## Adapting this to your context

One or two sentences saying where this file's defaults came from and that they are defaults, not a standard.

- **The assumption.** What the file currently assumes, then what to change it to and under what condition. Three to six of these, drawn from the file's own numbers, cadences, tools, org shapes, jurisdictions, data shapes or software.
- **What not to change.** The one or two rules that are the method itself and hold in any setting.

## Related skills

Which skill hands work to this one, which one this hands to, and which adjacent skill covers the case this deliberately excludes.
```

## Notes on writing one

The `description` is the load-bearing field wherever the assistant loads skills automatically. A perfect skill that never triggers is worth nothing, and the most common reason a skill does not trigger is that its description describes the contents rather than the request. Where you paste the file in by hand, the description is just a summary and the body does all the work.

The worked example is what makes a skill useful rather than merely correct. Abstract instructions produce abstract output. A scenario with a number in it, a constraint, and a wrong turn shows the judgement that the numbered steps cannot carry, and it is the part readers say they learned from.

The quality bar is the second most important part. It is what turns a document into a standard, and it is the section to write first if you are stuck, because it forces you to decide what finished means before you describe how to get there.

Length follows the work. A skill covering a genuinely complex task will run long, and that is correct. What is not correct is length from restating the same instruction in three registers. Every paragraph should carry something the reader could not have supplied themselves.
