---
name: skill-builder
description: Builds and repairs skills that trigger reliably and enforce a standard rather than describe a topic. Produces a SKILL.md in the required structure of this library: a trigger-shaped description, an opening that names the failure, explicit missing-input rules, a method with decision rules instead of "choose the right approach", a worked example in situation, task, action and result form with a wrong turn in it, failure modes, edge cases, and a checkable quality bar. Use this skill whenever someone wants to write a new skill, improve or deepen an existing one, asks why a skill did not fire or fired on the wrong request, wants to turn a repeated workflow, a checklist, or a page of instructions into a skill, asks how skills are structured or what makes a good description, wants to audit or publish a library of them, or says something vague like "can you make this a skill", "this should be reusable", or "write me a SKILL.md".
---

# Skill Builder

Two things go wrong with skills, and they are almost never the things the author worried about. The first is that the skill never loads. It sits in the folder, correct and unread, because its description names a subject rather than the requests people make, and nobody notices because the work still gets done, slightly worse, by default. The second is that the skill loads and changes nothing. It explains the domain to a reader who already knows the domain, it says "choose the appropriate method", and the output is what would have appeared without it.

Both failures are quiet, and quiet is what makes them expensive. A team writes fourteen skills over a quarter, believes it has captured how it works, and finds at the first handover that the new starter produces the same inconsistent output as before, because eleven of the fourteen never fired and two of the remaining three were essays. The cost is not the writing time. It is the false confidence that the method is now written down.

This skill produces the other kind: a file that fires on the request people actually make, and that visibly changes the output when it does.

## When to use this, and when not to

Use it when a task recurs and its quality depends on discipline you can describe. Use it to write a new skill, to deepen a thin one, to diagnose a skill that did not trigger or triggered on the wrong request, to convert a checklist or a page of standing instructions into a skill, and to audit a library for overlap and gaps before publishing it.

Do not use it for something you will run once, which is a prompt. Do not use it where quality rests on taste that cannot be written as a test: "write beautifully" enforces nothing, whereas "no sentence longer than forty words and no paragraph that restates its first line" does. Do not use it for knowledge the assistant already has, because a skill explaining a well known subject only adds tokens.

Two adjacent cases belong elsewhere. A procedure that humans perform, with owners, handoffs and a revision date, is `process-documentation-sop`. Rules for how one publication or one person's material must look and sound are a brand skill, of which `breaktalk-brand` is the worked example in this library; you build one using this skill but its content is identity, not method.

## What you need before starting

**The recurring task, stated as a request someone makes.** Not a topic. "Turn a call transcript into a follow-up note" is a task; "communications" is a shelf. Missing: ask for the last three times the person did this work and name the task from what they actually produced.

**A specific bad output you can describe.** The skill's job is mostly to prevent a known failure, and if the author cannot describe the failure in one sentence, the skill will describe a topic instead. Missing: ask what a colleague does wrong on this task, or what gets sent back in review. If nothing comes back, the task probably does not need a skill.

**Two or three real past outputs, good ones.** These carry the sequence, the format and the vocabulary far more reliably than an interview does. Missing: work from one output and mark the method as provisional until it has been run against real tasks.

**The tests the author applies before sending.** These become the quality bar and they are the fastest part of the file to write. Missing: derive them by asking what would make the author refuse to send a draft.

**The phrases people say when they want this.** Including the vague and lazy ones. Missing: collect them from message history, a ticket queue, or by asking three colleagues to request the thing in their own words; do not invent them alone, because authors write the phrasing they wish people used.

**The tool situation.** Which connector, database or script the work touches, and what happens when it is absent. Missing: assume it will be absent and write the fallback first. A skill that stops working when a connector is not configured is a skill that fails silently for most of its readers.

**The rest of the library.** What already exists, so the new skill can name its neighbours and refuse their work. Missing: list the folder names before writing; the boundary section cannot be written from memory.

## The method

1. **Apply the three-part test before writing anything.** A task deserves a skill when it recurs, when its quality depends on a describable discipline, and when the author can name a specific bad output. All three, not two. If the quality rests on judgement nobody can write down, write a checklist of inputs and stop. If the task happens once a year, put it in the team's handbook. Saying no here is the highest-value step, because every unnecessary skill makes the real ones harder to find.

2. **Harvest the method from artefacts, not from memory.** Put the past outputs side by side and mark what is common: the order of sections, the figures that always appear, the check that always happens last. Then interview around the gaps: what do you gather before starting, what do you do first, where do you usually get it wrong, what makes you send a draft back. Practitioners under-report the steps they perform automatically, which is why the artefacts come first.

3. **Write the quality bar before the method.** Four to eight lines, each checkable by reading the finished output. Write it first when stuck, because it forces a decision about what finished means before you describe how to get there. Test each line by asking whether two readers would agree on pass or fail. "Every figure traced to a source cell" passes. "Thorough analysis" does not. Put the line you would check with thirty seconds first.

4. **Write the description as a trigger surface, not a summary.** This is the load-bearing field wherever skills load automatically, and the commonest reason a skill never fires is that its description describes the contents. Use the three-part shape: what the skill produces, then the standard it enforces, then the phrasings that should trigger it, written as people say them including the vague ones. Aim for 90 to 160 words, and include at least two casual or oblique phrasings, because the request that most needs the skill is usually the least precise one. Name the file and the folder identically, lowercase and hyphenated and specific enough to be guessed: `revenue-concentration-risk`, not `analysis`. The `name` field must equal the folder name exactly.

5. **Open on the failure, not on the function.** One or two paragraphs naming what goes wrong without the skill and what it costs, in money, rework, credibility, or a decision made badly. An opening that says what the skill does is wasted, because the reader sees that from the title. If you cannot name a failure, return to step one.

6. **Draw the boundary, naming neighbours by their exact folder name.** What this handles, and the adjacent cases that belong elsewhere. Being explicit about what a skill is not for prevents the commonest misuse and stops two skills fighting over one request. Where the boundary is blurred, state the rule that decides, usually a property of the input: whether the data is already clean, whether the decision has already been made.

7. **Write the inputs with a missing rule on every one.** Real work starts with three of the six inputs, and a skill that only lists what it wants is a wish list. For each input, the reason it matters and then the rule: proceed on stated assumptions, ask one specific question, or stop. Choose by consequence. If a wrong assumption produces work that must be thrown away, ask. If it produces work correctable in place, proceed and label the assumption. If it could produce something misleading that someone might act on, stop.

8. **Write the method as steps with the judgement inside each one.** For each step: what is done, the judgement call it contains, and the rule for making that call. Number them where order matters, and say so where it does not, because readers assume numbering means sequence. The test is the substitution test: replace "choose the right approach" with "use A when the data is monthly and complete, B when it is quarterly or has gaps, and if you cannot tell, run the cheap version of A first and look at the residuals". A step that cannot be rewritten that way is not finished.

9. **Write the worked example in situation, task, action and result form.** This is the section readers say they learned from, and it is not decoration. Abstract instructions produce abstract output; a scenario with a number in it, a constraint, and a decision that could have gone the other way carries the judgement the numbered steps cannot. Invent names and organisations, use real-looking figures, and include at least one wrong turn that was abandoned with the reason. The wrong turn is the part that teaches, because it is where the method disagreed with the obvious approach. Where the outcome was uncertain, write it as uncertain rather than inventing a clean ending. Then add a second, shorter scenario under its own heading, showing the method behaving differently under different conditions, and label what changed.

10. **Give the output a shape close enough to copy.** A table with real column headers, a fenced block with the actual field names, or a document with its sections in order. This makes two runs comparable and saves the reader the hardest part. Placeholder columns called "Item" and "Value" fail this test.

11. **Write failure modes from wreckage and edge cases from limits.** Each failure mode needs how to recognise it and what to do instead, and the useful ones are the mistakes competent people make under deadline, which is why they come from reviewed outputs rather than from a list of virtues inverted. The edge cases are where the method does not apply at all: no data, a decision already taken, a hostile reader, a constraint discovered late, a confidentiality limit. Three genuine entries in each beat ten invented ones.

12. **Test on five real tasks and count the triggers.** Include one phrased casually, one at the edge of scope, and one that should not trigger it at all. Record which fired. Then run two of them without the skill and compare. If you cannot see the difference in the output, the skill is describing rather than enforcing, and the repair is in the method and the quality bar, not in the prose.

13. **Ship it with its neighbours named, and keep a change note.** Cross-references turn a folder of files into a library: which skill feeds this one, which one it feeds, which adjacent one covers the excluded case. Record what changed when you revise, in one line.

## The description field, in detail

Most skills that fail, fail here, so it is worth writing this field three times.

Under-triggering looks like this: `description: Guidance on writing customer emails.` Accurate, short, and it will not fire when someone says "can you draft something to send to the account that churned last week", which is the request that most needed it. The repair is to list situations rather than the subject, including the phrasings that do not name the task.

Over-triggering looks like this: `description: Use for anything involving data.` It fires on requests it cannot help with, displaces the skill that should have fired, and produces output shaped by the wrong method. The repair is to name the input condition that separates this skill from its neighbours, and to add an explicit exclusion with the neighbouring folder name in it.

A serviceable pattern, which the descriptions in this library follow:

> [What it produces and to what standard, one or two sentences.] [The specific things it enforces, so the reader can tell it apart from adjacent skills.] Use this skill whenever someone [request phrasing one], [request phrasing two], [an oblique or vague phrasing], or [the case where the user does not name the task at all].

Two calibration checks. Ask what request the description would refuse; if the answer is nothing, it will over-trigger. Then read the five test phrasings and ask whether a reader with only this description would pick this skill for each; if two are ambiguous against another skill, the boundary belongs in both descriptions.

## Files beside the SKILL.md

The body is the part always in view, so keep it the method and nothing else. Everything consulted rather than read goes beside it.

`references/` holds material read only when needed: a style table, a list of banned constructions, a worked template, a data schema. Name it from the body at the point of use, with one line on what is inside, so nobody opens it speculatively.

`scripts/` holds anything mechanical and deterministic. A script earns its place when a check is tedious, exact and repeatable, and when a person will skip it under deadline. Document three things in the body: the command, what it catches, and what it deliberately does not do. That last part matters more than it sounds. A checker that silently repaired what it found would teach nobody and would introduce its own artefacts, so the useful ones report and exit non-zero.

`assets/` holds binaries: a logo, a template, an image. Keep them small, state the licence, and never put anything confidential in a skill that will be shared.

## Worked example

**Situation.** Nadia Okonjo runs client operations at a sixty-person analytics firm. Her team of five produces a monthly service review pack for each of nineteen accounts: usage, incidents, an action list, and a short commentary. The packs vary badly between team members. Two of the five write commentary that names the account's own numbers; three write commentary that could apply to any account. Twice in the previous quarter a pack went out with an incident count that did not match the ticket system, once to an account three months from renewal. Nadia had written a one-page internal note about building the pack eight months earlier. Nobody used it.

**Task.** Turn the method into a skill applied automatically, before the next monthly cycle, thirteen days away. Good meant two checkable things: that a request phrased the way her team actually phrases it would load the skill, and that a pack produced with it would have every number traceable to a source system.

**Action.** The first attempt was the internal note with a frontmatter block on top. The description read: "Guidance for producing monthly client service review packs." True and useless. Nadia tested it against eight phrasings taken from her team's message history, including "can you pull the monthly for the Halden account" and "put together the deck for Thursday's check-in". It loaded on two of the eight, both of which used the phrase "service review pack", which is Nadia's phrase and almost nobody else's.

The rewritten description ran to 128 words: what the pack contains, the standard that every figure is traced and dated, then the trigger phrasings, including "the monthly for X", "the check-in deck", and "what do we send the account this month". It loaded on seven of eight. The eighth was an annual contract review, which correctly belonged to a different skill, so that miss was the useful result of the test rather than a failure of it.

The wrong turn worth recording was the body. The second draft explained what a service review is, why accounts value them, and what good commentary looks like, in about 700 words of prose. It loaded correctly and the packs came out exactly as before. Nadia produced one pack with the skill and one without, and could not tell them apart. Every instruction in the body was a description of a quality rather than an operation: "commentary should be specific to the account" tells a reader nothing they did not already intend.

The repair replaced the explanation with decision rules. Commentary became explicit: open with the largest month-on-month movement in the usage table, state its size in the account's own units, and give the cause from the incident log or say the cause is unknown. Traceability became a step: every figure carries the system it came from and the date it was pulled, and a figure that cannot be traced is removed rather than estimated. The quality bar, written before either, had five lines, the first being that the incident count in the commentary equals the count in the ticket system for the same date range. The worked example was added last: an invented account with a 34 percent drop in weekly active users that turned out to be a licence reassignment rather than churn, including the first draft's wrong attribution of it to dissatisfaction. That example changed the team's writing more than the method section did, which is the usual pattern.

**Result.** The next cycle produced nineteen packs. Seventeen loaded the skill on the first request; the two that did not arrived as forwarded email with no framing, a case no description solves. Every pack carried source and date on every figure. Two figures were removed in production because they could not be traced, and one of those removals surfaced a reporting gap in the usage export that had been wrong for at least two months.

What did not resolve cleanly: commentary quality still varies. Opening on the largest movement made every commentary specific, but the second and third paragraphs are still noticeably better from two of the five. Nadia's judgement is that this part is taste and will not be fixed by a skill. That is step one applied late, and it is the right answer.

### A second scenario, where it goes differently

A research group had the opposite problem. Their `data-cleaning` skill fired on nearly every request that mentioned a dataset, including requests to simply describe one, and imposed a full cleaning and documentation sequence on work that needed a two-line answer. Members had started avoiding the word "data" in their requests, which is the clearest sign a skill is over-triggering.

The repair was in the same field, in the opposite direction. The description was narrowed to state the input condition: raw extracts not yet checked, where the deliverable is a cleaned file with a log of what changed. An explicit exclusion named the neighbouring folder for describing a file already clean. The body gained one line at the top of the method: if the file is already clean and the request is to describe it, hand back and stop.

What changed was the direction of the error. Nothing in the method changed, and neither did the quality bar. When a skill misfires, the repair is almost always in the description and the boundary, not in the method, and rewriting the method first is the commonest wasted afternoon in this work.

## Output

The deliverable is one folder containing a SKILL.md in the structure below, plus any reference or script files it names.

```
<track>/<skill-name>/
  SKILL.md
  references/    (optional, consulted not read)
  scripts/       (optional, mechanical checks)
  assets/        (optional, binaries)
```

```markdown
---
name: skill-name-matching-the-folder
description: What it produces, the standard it enforces, then the phrasings
             people actually use, including the vague ones. 90 to 160 words.
---

# Skill Name

[The failure this prevents and what it costs. One or two paragraphs.]

## When to use this, and when not to
## What you need before starting          (each input with its missing rule)
## The method                             (each step with its decision rule)
## Worked example                         (situation, task, action, result)
### A second scenario, where it goes differently
## Output                                 (close enough to copy)
## Failure modes                          (recognise it, do this instead)
## Edge cases                             (where the method does not apply)
## Quality bar                            (four to eight checkable lines)
## Related skills                         (exact folder names, in backticks)
```

Alongside the file, deliver the trigger test so the author can rerun it after any edit:

| # | Test phrasing, as a person would say it | Should trigger | Did trigger | Note |
| 1 | | yes | | |
| 2 | | yes | | |
| 3 | | yes, casual phrasing | | |
| 4 | | no, belongs to `other-skill` | | |
| 5 | | no | | |

## Failure modes

**The description that names the topic.** Recognise it because it reads like a table of contents entry and contains no request phrasing. The skill will under-trigger and nobody will report it, because the work still gets done. Fix by rewriting from five collected phrasings.

**The essay in place of a method.** Recognise it by running the same task with and without the skill and seeing no difference in the output. Usually every instruction is a quality rather than an operation. Fix by converting each into something a reader could fail to do.

**Steps with no decision rule.** Recognise them by the words "appropriate", "as needed", "where relevant", and "choose the best". Fix by writing the condition, the branch, and the fallback for when the condition cannot be determined.

**The invented worked example.** Recognise it because everything goes right, no figure is awkward, and there is no abandoned attempt. Readers discount it immediately. Fix by using a real case with names changed, and by writing in the moment where the obvious approach was wrong.

**Two skills competing for the same request.** Recognise it when output quality on a task varies by how the request happened to be phrased. Fix by naming the input condition that separates them and putting the exclusion in both descriptions, not just the newer one.

**Confidential material in a shared skill.** Recognise it by reading every example for client names, internal figures, unreleased plans and personal data. Fix before publication, and prefer invented names to redacted ones, because a redaction still reveals something was there.

## Edge cases

**The task recurs but the quality is pure judgement.** Write the input checklist and the quality bar, skip the method, and say in the file that the method is deliberately absent. A short honest file beats a long one pretending to a discipline that does not exist.

**The method exists only in one person's head and they have two days.** Do not attempt the interview. Sit with them through one real instance, record the sequence and every question they ask themselves, and write from that. Two hours of observation beats a day of recollection.

**The skill depends on a connector or a database.** Write the method so a person could follow it manually, then name the tool as an accelerator with the fallback stated at the point of use. Never make a paid or optional tool a hard requirement, and never let its absence produce silent degradation rather than a stated limitation.

**Rewriting a skill people already rely on.** Keep the name and the folder, keep anything true and useful from the existing file, and record what changed. Silently changing a method a team has learned costs more than the improvement usually returns.

**The subject is one person's identity rather than a method.** A brand, a personal voice, a house style tied to an individual. It can still be written as a skill, but it cannot be used by anyone else as written, and the file should say so plainly and present itself as a worked example whose structure is the reusable part.

## Quality bar

- The description contains request phrasings, including at least two vague ones, and would refuse at least one nearby request.
- The `name` field equals the folder name exactly.
- Every input carries a rule for what to do when it is missing.
- Every method step contains a decision rule, with no instance of "choose the appropriate", "as needed", or "where relevant".
- The worked example has real numbers, an invented but concrete setting, and at least one abandoned attempt with the reason.
- The quality bar lines are each checkable by reading an output, and two readers would agree on pass or fail.
- Adjacent skills are named by their exact folder name in both the boundary section and the related section.
- The skill was run on at least five real tasks, and the difference against running without it is visible in the output.

## Related skills

`process-documentation-sop` covers the procedure written for people to follow, with owners and a revision date, which is the adjacent case this deliberately excludes. `human-voice-editor` is the last pass over the finished SKILL.md, because a skill written in generic prose produces generic output. `breaktalk-brand` is the worked example of the identity case named in the edge cases, and is built with this method. `content-quality-gate` applies a comparable pass or fail standard to published material rather than to method files.
