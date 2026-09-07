---
name: process-documentation-sop
description: Turns a process that lives in one person's head into a standard operating procedure someone new can follow without asking: the current-state map built by observation, then the document with purpose, trigger, owner, roles, numbered steps naming the exact system and the expected result, decision rules, exceptions and escalation, quality checks, timings, and a change log. Enforces the standard that the document is not finished until a person who has never done the work completed it from the text while the author watched in silence. Use this skill when someone asks to document a process, write an SOP, a runbook or a checklist, capture what a leaver knows, standardise a task across several people, hand a process to a new hire or an outsourced team, or says only one person knows how to do this and they are on holiday next week.
---

# Process Documentation, SOP

A process that lives in one person's head is a risk with a name on it. The organisation finds out its true cost at the worst possible moment: the week that person resigns, goes on leave, or is off sick during a close, a renewal cycle or an audit. What follows is not a gap in output; it is a scramble in which several people reconstruct the process from partial memory, get it about eighty percent right, and introduce errors that surface weeks later in a report nobody can reconcile.

The second cost is quieter and larger. An undocumented process cannot be improved, because nobody can see it, and cannot be delegated, so the expert stays trapped in it. It also hides the steps that only work because the expert is quietly compensating for a gap somewhere else: the reconciliation done by eye, the person chased every month, the field corrected because a system writes it wrong. Writing it down exposes those, and that exposure is usually worth more than the document.

This skill produces a document that a competent stranger can execute, and it treats an untested document as a draft.

## When to use this, and when not to

Use it when a person with unique knowledge is leaving, changing role or going on extended leave, which is the highest-value case and the most time-pressured. Use it when the same task is done differently by three people and the outputs do not match, or when a process is being handed to a new hire, a junior colleague or an outsourced team. Use it before automating anything, since automating an undocumented process automates whatever it currently does including the errors. Use it when a process has failed twice in the same way, where the map finds the cause faster than an incident review does, and when an auditor or a certification requires evidence that a control is performed consistently.

Do not use it to design a process that does not yet exist. Documentation describes and stabilises; design is a different activity, and writing an SOP for an imagined process produces a document nobody follows because it was never true. Build the process, run it three times, then document it.

Do not use it for genuinely judgement-led work, where each instance differs in kind rather than in detail. Negotiating a contract, diagnosing a novel fault, deciding a pricing exception: numbered steps produce a document that is ignored and a false sense of control. For those, document the inputs, the decision criteria, the escalation path and the record to keep, and leave the judgement to the person.

`operating-cadence-design` covers the meeting and reporting rhythm rather than individual procedures. `program-management` handles work that runs once to a plan rather than repeating. `onboarding-plan` is where a finished SOP does most of its work, and a short overlap with a leaver is best spent producing SOPs rather than conversation.

## What you need before starting

**Access to the person who actually does the work.** Not their manager, who describes the process as designed rather than as performed, and the gap between those two is the entire subject. Missing: work backwards from the last three outputs, confirm with whoever comes closest, and label the document unverified until a practitioner has reviewed it.

**Permission to observe a real run.** Watching beats interviewing by a wide margin, because experts omit the steps they have automated in their heads. Missing: interview against a live example on screen rather than in the abstract, which recovers most of the benefit.

**The systems, with sight of the screens.** The actual buttons, fields, folders and templates. Missing: capture the step in words, mark the system detail to be confirmed, and close those gaps in the test run rather than guessing.

**The trigger and the frequency.** What starts the process, how often it runs, and the deadline it must meet. Missing: ask what happens if it is late, which usually reveals the real deadline and who enforces it.

**The known failure history.** Where it has gone wrong and what happened. Missing: ask the person downstream rather than the performer, since they see the errors and the performer often does not.

**A tester.** Someone who has never done the work and can run it once under observation. Missing: this is the one input worth waiting for. An untested document is a draft, and saying so is better than publishing it as a standard.

**Where the document will live.** Missing: put it where the team already looks rather than where documents are meant to go. A perfect SOP in a repository nobody opens has reduced no risk.

## The method

1. **Establish the boundaries before mapping anything.** Where it starts, where it ends, what is explicitly out of scope. Mapping sessions that run long almost always do so because the boundary was never fixed and the conversation drifted upstream into how the data got there. Write one line: this process begins when X happens and ends when Y exists.

2. **Map the current state as it is actually performed.** Observe a real run if possible, otherwise interview against a live example. For each step record who does it, in which system, with what input, producing what output, and how long it takes. Capture the branches and the rule that decides each. Capture the handoffs, including how the receiver knows the work has arrived, which is where most delay hides. Capture the exceptions, which is the most interesting material: the cases that do not fit, and what actually happens to them rather than what is supposed to.

3. **Interrogate each step with four questions.** Why is this here. What happens if it is skipped. Who else can do it. How do you know it worked. The fourth produces the quality checks; the first produces the cuts, since a step nobody can justify, usually a legacy check or a report nobody reads, is a candidate for removal.

   The rule on improving before documenting: fix a step now only if it is a clear defect, cheap to change, and inside the owner's authority. Everything else goes on a separate improvement list, and the document records the process as it is. An aspirational version is wrong on the day it is published.

4. **Confirm the map with the practitioner before writing prose.** Show it back as a numbered list or a swimlane and ask what is missing. Expect two or three additions, always at the exceptions, and expect at least one step they perform without having been aware of it until they saw the list.

5. **Write the document to the structure below**, in the imperative, one action per step, naming the exact system and the expected result. This is a transcription task once the map is right, and if it feels like invention the map is not right.

6. **Write the exceptions and the escalation path.** Every known non-standard case with what to do, and one clear route for the unknown ones: who to contact, in what timeframe, and what to do meanwhile. An SOP without an escalation path fails on its first unusual day and the person guesses.

7. **Write the quality checks as a short block at the end.** What to verify before declaring the work complete, and what a correct output looks like, with a real example. This is the most commonly omitted section and it decides whether errors are caught at the desk or two weeks downstream, where they cost far more.

8. **Test it in silence.** A person who has not done the work follows the document from start to finish while the author watches and answers nothing. Every question asked, every pause, and every place the tester does something different from what was intended is a defect in the document, recorded and fixed. The silence is not a formality: an author who answers one question has repaired the process in the room and left the document broken.

   Where a live run is impossible, because the process is quarterly or touches production data, run it against the previous cycle's inputs in a copy environment, publish as version 0.9, and treat the first real run as the test with the author observing in silence.

9. **Publish with an owner, a version and a review date**, in the place the team already looks, and tell the people who need it that it exists and what it replaces. Test findability by asking a colleague to locate it in under a minute; if they cannot, no risk has been reduced.

10. **Produce the checklist variant where the process is frequent.** For anything run weekly or more often, the SOP becomes the reference and a one-page checklist the working document: steps as tick boxes, quality checks at the end, fields for who ran it and when. Nobody reads prose for the fortieth run, and a checklist people use beats a document they do not.

## The SOP document structure

1. **Title and identifier**: process name, version, owner, date of last review, next review date.
2. **Purpose**: one paragraph, what the process achieves and for whom.
3. **Scope**: what is covered, what is explicitly not, and the related processes named.
4. **Trigger and timing**: what starts it, how often, the deadline or service level, and what happens if it is missed.
5. **Roles**: each role with its responsibilities. Use role names rather than people's names, with a small current-holders table that can be updated without reissuing the document.
6. **Inputs and prerequisites**: data, approvals, access and tools that must exist before starting, each with where to get it.
7. **Procedure**: numbered steps, one action each, imperative, naming the exact system, menu, template or field, with the expected result stated so the person knows they succeeded. Branches written as "If X, go to step 9; otherwise continue". Screenshots only where the interface genuinely cannot be described in words, since they age badly.
8. **Exceptions**: known non-standard cases with the handling for each, plus the escalation route for anything unlisted.
9. **Quality checks**: what to verify before declaring completion, and what a correct output looks like.
10. **Outputs and records**: what is produced, where it is stored, who is notified, and how long it is retained.
11. **Metrics**: cycle time, error rate, volume, where these are measured.
12. **Change log**: date, change, author.

## Writing rules

Write for a competent person who has never done this task and has nobody to ask. That reader is the standard, and every assumption of tribal knowledge is a defect. Abbreviations, first names and implied context turn an SOP into a set of notes that will not survive its author.

One action per step. "Export the report and send it to the finance team" is two steps and will be half-completed by someone interrupted in the middle.

Name things exactly as they appear on screen, including capitalisation. A reader searching for a menu item worded differently concludes they are in the wrong place.

State the expected result after each significant step. Errors caught at step four are cheap; the same error found at the end means redoing everything.

Give a time estimate per phase, so the reader can plan and so an unexpectedly long step signals a problem.

Avoid internal jargon or define it on first use. An SOP is often the first document a new joiner reads closely, and it teaches vocabulary whether or not it intends to.

## Maintenance and ownership

Every SOP has one named owner, usually the person accountable for the outcome rather than the one who performs the steps.

Set the review cadence by volatility: quarterly for anything touching a system that changes often, annually for stable processes. A review that finds no changes takes five minutes and should still be recorded.

Trigger reviews off events as well as dates: a system upgrade, a reorganisation, a role change, a failure, an audit finding. The event triggers are what keep a library current, because calendar ones get deferred.

Retire rather than delete. Mark a superseded SOP as retired with the date and what replaced it, and keep it. The question "how did we do this last year" is asked constantly, mostly by auditors and by people investigating an old number.

## Worked example

**Situation.** A market research company of about 200 people had one operations analyst who ran the monthly client billing reconciliation. She had done it for four years, it took a day and a half each month, and she had accepted a job elsewhere with four weeks' notice. The reconciliation matched project delivery records against the finance system before invoices were issued, and in a typical month it caught three to eight billing errors worth roughly 15,000 to 40,000 US dollars. Nobody else had ever run it. The written material was a calendar reminder titled "billing recon" and a spreadsheet tab called "checks (do not delete)".

**Task.** Produce an SOP that someone in the finance team could run in the month after her departure, tested before her last day.

**Action.** The boundary was set first and the first attempt was wrong. The initial scope of "monthly billing" pulled in invoice generation, credit notes and the dunning process, and the first mapping session ran ninety minutes without reaching the end. It was rewritten to begin when delivery records close on the second working day and end when the finance manager signs off the reconciliation report. Everything downstream became a separate, much shorter document.

Observation was arranged for the following month's run rather than relying on interview, which turned out to matter. The interview version produced eleven steps; the observed version had twenty-three. The twelve missing steps were things she did without noticing: a filter applied every time because one project type was miscoded at source, a check against a fourth system nobody had mentioned, a currency rounding correction made by hand, and a monthly email to a delivery lead whose records were reliably late, sent two days before she needed them.

That last one was the most valuable finding in the exercise. The process only worked because she pre-empted a recurring failure elsewhere, and nobody upstream knew they were being managed. It went into the improvement list and became a change to the delivery team's own close deadline rather than a step in the SOP.

Interrogating the steps found two that could not be justified: a reconciliation against a legacy pricing table not updated in two years, and an export to a shared folder that nothing read, feeding a report retired eighteen months earlier. Both were removed with the finance manager's agreement, cutting the run time before anything else changed.

The test was run by a finance associate of five months' standing, following the document while the analyst watched and said nothing. It took him four hours to reach step nine, where he stopped: the document said "apply the standard project type filter" and he had no way to know what standard meant. Fourteen other defects were logged in that session, including three field names that no longer matched the screen after a system update, two branches with no rule stated, and one point where he produced a plausible but wrong output and had no way to tell, because the quality check section did not yet exist.

The wrong turn: the first draft carried eleven screenshots, on the reasoning that the finance system's interface was confusing. The system was upgraded six weeks later and nine became wrong, showing menus that no longer existed, which is worse than no screenshot because readers trust the picture over the text. The revision kept two, both of a report configuration screen that genuinely could not be described in words, and replaced the rest with exact field names.

**Result.** The SOP was tested a second time, by a different person, three days before the analyst's last day. That run completed with two questions, both about the escalation contact, which was then named explicitly. The first live run after her departure took six hours against her day and a half, partly because two steps had been removed and partly because he was following a document rather than remembering.

The reconciliation caught five errors that month, in line with the historical range, which was the real test. One error was missed and found the following month, caused by an ambiguously written branch condition, fixed in version 1.2. The improvement list produced three changes over the next quarter, of which the delivery close deadline removed the most work. The process now takes about four hours and is run by two people who alternate.

### A second scenario, where it goes differently

The same company, documenting how a research director scopes a new study and decides the methodology and sample design.

The method breaks here, and recognising that is the skill. Every study differs in kind: the client's question, the population, the budget, and the trade-off between sample size and depth. Twenty numbered steps would produce a document the directors ignore and a junior person could follow into a badly designed study while believing they had followed the standard.

What is documented instead is the frame rather than the sequence. The inputs to gather before scoping and where each comes from. The decision criteria, written as considerations with the questions to ask rather than as rules: when a quantitative approach is indicated and when it is not, what sample size the confidence requirement implies, what the budget makes impossible. The two mandatory checkpoints where a second director must review before the proposal goes out. The record to keep, so a decision made in March can be explained in September. And three annotated past examples, which teach more than any procedure.

What changed is the nature of the work, not its importance. Judgement-led processes get a frame, a checkpoint and worked examples; repeatable processes get numbered steps. Applying the wrong form to either is the failure.

## Output

The SOP document, following the twelve-section structure above. Alongside it:

**The process map**, a numbered list or a simple swimlane. Where a diagram is used, keep it monochrome, distinguish roles by shape and dash pattern rather than colour so it survives photocopying and colour blindness, and put the legend outside the plot area.

**The step table**, which is the working artefact behind the document:

| # | Step | Role | System | Input | Output | Time | Decision rule | Exception |

**The test log**, kept as evidence that the standard was met:

| Test date | Tester | Step reached | Question or defect | Fix applied | Version |

**The improvement list**, separate from the SOP, so that description and change do not get confused:

| # | Observation | Why it happens | Proposed change | Owner | Agreed? |

**The checklist variant**, one page, for frequent processes: steps as tick boxes, quality checks at the end, fields for run by, date, and exceptions encountered.

## Failure modes

**Documenting the designed process rather than the performed one.** Recognise it when the document is shorter than the real work and contains no exceptions. It comes from interviewing a manager. Fix by observing a run.

**The expert's invisible steps.** Recognise it when the tester's first run produces a different output from the expert's. Experts omit what they have automated in their heads, and no amount of asking recovers it. Only observation and the silent test do.

**Answering questions during the test.** Recognise it when the test log is empty and the tester finished easily. Every answer given in the room is a defect left in the document.

**Screenshots as the primary content.** Recognise it when the document cannot be understood without the images. They break at the next interface change, silently, and readers trust them over the text. Use exact names in words, and reserve images for what genuinely cannot be described.

**Names instead of roles.** Recognise it when the document goes wrong within a quarter because someone changed jobs. Use roles, with a separate holders table.

**Improving and documenting in the same pass.** Recognise it when the document describes a process nobody currently performs. Keep the improvement list separate and document reality.

## Edge cases

**The expert has already left.** Reconstruct from the last three outputs, the system audit trails, and the people upstream and downstream. Publish explicitly as a reconstruction with the gaps marked, and treat the first three live runs as the real mapping exercise, updating after each.

**A hostile or anxious expert.** Documenting a process is often read as a prelude to redundancy, and the fear is not always unfounded. Say plainly what the document is for; the strongest framing is the true one, that this is what lets them take a holiday, get promoted, or stop being called at weekends. Never document someone's process without telling them.

**The process is broken and everyone knows it.** Documenting it faithfully feels absurd. Do it anyway, briefly, then attach the improvement list: a written description of the broken process is the most effective argument for changing it anyone has produced.

**A regulated or audited process.** The document may need a mandated format, approval signatures, formal version control and a record of training completion. Ask what the standard requires before writing, keep the substance identical, and let the compliance function own the format.

**Several people do it differently and all get acceptable results.** Do not average them. Pick the version with the fewest steps and the best error record, document that one, and get the others to agree explicitly. An SOP describing a compromise nobody follows is worse than three openly inconsistent practices.

## Quality bar

- A person who had never done the work completed it from the document while the author watched in silence, and the test log records what they asked.
- Every step names the system, the field or template, and the expected result.
- Exceptions and one escalation route with a named contact are documented.
- The quality checks state what a correct output looks like, with an example.
- The document uses role names, with a separate table of current holders.
- It carries an owner, a version, a last-reviewed date and a next-review date, and lives where the team already looks.
- The improvement list is separate from the SOP, and the SOP describes the process as it is performed today.
- Any step removed or changed during mapping was agreed with the owner and recorded in the change log.

## Adapting this to your context

The twelve-section structure, the review cadence and the silent test come from office and back-office processes in commercial companies of fifty to five hundred people, running in software systems.

- **The twelve-section structure.** Where a quality system prescribes a template, ISO 9001, Good Manufacturing Practice, a clinical procedure format, a laboratory quality manual, use theirs and map these sections onto it.
- **The silent test with a fresh person.** Where the process touches patients, production, money movement or live infrastructure, test against the previous cycle's inputs in a copy environment, publish as version 0.9, and let the first supervised live run be the real test.
- **Quarterly or annual review.** Set the cadence from how fast the underlying system changes. A process built on software that ships weekly needs an event trigger on every release note.
- **Exact on-screen names instead of screenshots.** For physical or laboratory procedures, a photograph of a correct setup is often the only accurate description, and there the picture is the content.
- **What not to change.** The document is a draft until someone who has never done the work completed it from the text while the author watched in silence, and it describes the process as performed, with improvements on a separate list.

## Related skills

`onboarding-plan` is where a finished SOP earns most of its value, and a short handover overlap is best spent producing SOPs rather than conversation. `operating-cadence-design` documents the rhythm of meetings and reporting these procedures sit inside. `program-management` covers work that runs once to a plan rather than repeating. `decision-memo` is the format for taking a change from the improvement list to whoever must approve it. `ai-adoption-program` depends on this, since a process cannot sensibly be automated until it has been mapped. `weekly-status-update` is where a process failure and its fix should appear.
