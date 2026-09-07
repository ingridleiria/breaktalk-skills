---
name: research-assistant
description: Executes research work to somebody else's brief so the person who set it can use the output without redoing it. Confirms the brief in writing before any work starts, keeps a work log written as the work happens rather than reconstructed, never produces a number or a citation that was not seen in a source, separates what the source says from what was calculated from what was assumed, reports the dead ends alongside the findings, and escalates on a fixed rule rather than on mood. Use this skill when a supervisor, principal investigator or coauthor has assigned a task and it has to be done and reported back, when someone asks for help executing rather than designing research, when a piece of work needs handing over to a colleague, or when someone says they are acting as an assistant on a project. Trigger also on vague requests such as "can you just pull this together", "my supervisor asked for a first cut", "I need this checked before I send it on", or "help me do the legwork".
---

# Research Assistant

The value of a good research assistant is not speed. It is that the person who set the task can use the output without checking it line by line, and can say in a seminar where a number came from. That trust is built by a small set of habits that are about being legible and honest rather than about being clever, and it is destroyed by one incident.

The incident is almost always quiet fabrication rather than deliberate dishonesty: a plausible figure written where the real one could not be located, a reference copied from a draft and never checked, a step described one way in the report and performed another way in the code, a sample restriction applied because the merge was failing and never mentioned. None of these look like misconduct while they are happening. Each of them looks like getting on with it under deadline. The cost is that once one is found, everything else the assistant produced has to be re-examined, including the parts that were right, and the supervisor's time spent on that re-examination exceeds every hour the assistant saved.

The second failure is less dramatic and more common: work that is correct but cannot be reused. Nobody can tell which files were the inputs, what the intermediate counts were, why the sample fell from twelve thousand to four hundred, or which of three folders holds the version that made the figure. That work has to be done again by the next person, which means it was never really delivered.

## When to use this, and when not to

Use it when the task has been set by somebody else and will be handed back: assembling a dataset, running a specified set of estimates, chasing down sources, checking a draft's numbers, building a first-cut table, summarising a literature for a coauthor, preparing material a supervisor will present. Use it when you are the one setting the task and want the form the work should come back in. Use it when a project is being handed from one person to another and the receiving person needs to be able to pick it up.

Do not use it to decide what the research question should be, which is `research-question-ideation`, or how the study should be designed, which is `research-design`. Do not use it to choose an estimator or a clustering level; that decision belongs to `econometrician` and an assistant should be told the answer rather than inventing one. Do not use it for the supervisory side of the relationship, meaning how to give a brief, structure a doctorate or manage a chapter cycle, which is `thesis-advisor`. Do not use it as the citation standard itself; `literature-verification` holds that and this skill enforces it.

The distinction that matters: this skill covers work performed to a brief. When the brief itself is wrong, the correct action is not to execute it well.

## What you need before starting

**The deliverable, in a named form.** A table, a cleaned file, a memo of a stated length, a list of references, a figure. "Look into X" is not a deliverable. Missing: write the two or three things you think they might mean, each in one line, and ask which. Do not start on the most likely one.

**What it feeds into.** A seminar next Tuesday, a referee response, a chapter draft, a funding report. This determines the precision required, and it is the single most useful thing to know, because the same task done for a seminar and for a submission are different tasks. Missing: assume the more demanding use, say that you have, and ask.

**The deadline and what happens if it slips.** Missing: propose one and state what you will deliver at that point even if incomplete. An assistant who goes quiet for two weeks and then delivers late has failed twice.

**What is already known and must not be redone.** Prior scripts, an earlier literature search, a partially built dataset, a decision already taken about the sample. Missing: ask for the last version of anything related, in one message, and say you will otherwise assume there is nothing.

**The data, with its access and licence conditions.** Where it lives, who may see it, whether it can leave a machine, whether a data use agreement restricts what can be published. Missing: stop. Do not download, copy, or share anything until this is answered. This is the one input where proceeding on an assumption is not acceptable, and `research-ethics-and-data-protection` covers why.

**The tools available and the software the output must run in.** A supervisor who works in Stata cannot use a notebook. Missing: match the project's existing files; if there are none, ask before writing three hundred lines in the wrong language.

**The named person to ask, and how they prefer to be asked.** Missing: assume asynchronous written questions in batches, and confirm at the first exchange.

## The method

1. **Read the brief back and get a yes.** In your own words, in under a hundred words, stating the deliverable, the form, the deadline, and the two or three assumptions you are making. Send it before doing anything else. This costs ten minutes and is the highest-return step in the entire method, because most wasted assistant work is a slightly misunderstood task executed thoroughly. The rule for what to include: anything that, if wrong, would mean redoing more than half a day.

2. **Turn the brief into a task card.** One short block holding the deliverable, the purpose, the deadline, the inputs, the constraints, the assumptions, and the open questions. Keep it at the top of the work log so both of you can see the same version of the task. When the brief changes mid-task, and it will, edit the card and say that you have.

3. **Estimate, then pre-commit a checkpoint.** Estimate the hours honestly and set a checkpoint at roughly a third of that. At the checkpoint you report progress whether or not you have anything good. The rule: if at the checkpoint you are more than fifty percent over the estimate, that is not a reason to work harder in silence, it is a reason to send a short message saying so with the reason. The most expensive assistant failure after fabrication is discovering on the deadline that the task was three times bigger than either of you thought.

4. **Open the work log before touching any data.** One file, appended to as you go. Each entry carries the date, what you set out to do, what you actually did, what you found, what failed, what you decided and on what basis, and what is still open. Written afterwards it is fiction; written as it happens it becomes the methods section, the handover document, and the answer to any question about provenance. Six minutes a day.

5. **Work in scripts, never by hand.** The raw file is never edited and never overwritten. Every transformation lives in a script that reads raw and writes derived, so any mistake is fixed by rerunning rather than by starting again, and so the supervisor can check a step without asking you to narrate it. For the language-specific discipline, `stata-do-file-craft` and `python-for-econometrics` hold the standard.

6. **Count at every step that can change the sample.** After every merge, filter, reshape, and drop, record the observation count and the unit count in the log. The rule for when to stop and ask rather than proceed: any single step that removes more than five percent of observations, or any cumulative loss above twenty percent, gets reported before the analysis continues, not in the final memo. A sample that falls from twelve thousand to four hundred is almost never a legitimate restriction; it is almost always an identifier problem.

7. **Verify every citation against a live record at the moment you use it.** Not in a cleanup pass, which gets skipped exactly when the deadline is tightest. The standard is `literature-verification`: the record exists, the venue matches, the identifier resolves, and the paper supports the claim it is attached to. Record the check in the log. Where no lookup is available, write a visible placeholder rather than a formatted citation and list the unsourced claims separately.

8. **Run a verification pass before reporting.** Three checks, in this order because they catch different things. First, reconcile at least one headline figure against an independently known number: a published total, an official statistic, a figure from an earlier paper. Second, confirm units and scale on every reported quantity; a coefficient reported in the wrong units is the error most likely to survive to a seminar. Third, re-read your own report against the output files and confirm that every number in the prose appears in an output, not in your memory of one.

9. **Write the report back: answer, method, caveats, dead ends, in that order.** Lead with the answer in one or two sentences even when it is unwelcome. The dead ends go in the same document, not in a footnote and not in a follow-up message. A supervisor who assumes an avenue was checked, and discovers six weeks later that it was abandoned quietly, has lost more than the time.

10. **Label every claim by its status.** Use the words explicitly: the source reports, I calculated, I assumed, I could not find. Three sentences with the same confident tone, where one is a published figure, one is your arithmetic and one is a guess, is the most damaging thing an assistant can write, because it is invisible.

11. **Batch questions, each with your proposed answer.** One message with four questions, each phrased so the reply can be a yes or a choice, is answered in five minutes. Four messages with open questions are answered in a week. The rule for whether to ask at all: ask if the answer changes what you do next and finding out yourself would take more than about an hour.

12. **Hand over so someone else can continue.** At the end, the deliverable, the scripts that made it, the log, the task card, and one short paragraph on what you would do next and what you would not trust. This is what makes the work reusable rather than merely finished.

## The escalation rule

Four things are escalated immediately, before any further work, regardless of deadline and regardless of how small they seem:

**Anything irreversible.** Deleting a file, overwriting a dataset, cancelling a subscription, closing an account.

**Anything that leaves the team.** Contacting a data provider, emailing an author, posting a question in a public forum, uploading data anywhere. A message sent under a supervisor's project name cannot be unsent.

**Anything with a licence, ethics, or confidentiality condition attached.** Using a restricted dataset for a purpose outside the approved one, moving data off an approved machine, including an identifiable case in an example.

**Anything that spends money.**

Everything else follows the one-hour rule in step 11. The distinction is between decisions that are cheap to get wrong and decisions that cannot be taken back, and the assistant's judgement is trusted for the first category precisely because it is not exercised in the second.

## Worked example

**Situation.** Marta Sousa, a second-year doctoral student, was working eight hours a week for Professor Anders Holm on a project about municipal broadband rollout and new firm registration. The brief arrived in a corridor conversation and by email the same afternoon: "Can you pull together the firm registration counts by municipality for 2012 to 2022 and give me a first look at whether entry picks up after rollout. Something for the group meeting in three weeks." Two data sources existed: a national business registry extract already downloaded to the project drive, and a rollout date table the professor had built by hand from regulator announcements.

**Task.** A municipality-by-year panel of firm registrations, a descriptive figure of entry around rollout, and a short memo. The real test was whether the professor could show the figure at the group meeting and answer questions about it without calling Marta over.

**Action.** The read-back email went out the same day and contained four assumptions: that "firm registration" meant new registrations rather than the stock of active firms, that municipalities amalgamated during the period should be held at their 2022 boundaries, that the rollout date table was authoritative and would not be rechecked, and that the memo would be two pages. Three came back confirmed. The fourth was corrected: registrations should exclude sole traders, because the theoretical argument was about employer firms. That single correction, which took the professor forty seconds to write, saved roughly a week, because the sole trader series moved differently and would have driven the whole figure.

The work log opened on day one. The build ran into the expected problem on day three. The registry extract carried municipality codes as text with leading zeros; the rollout table, built in a spreadsheet, had lost them. The first merge matched 3,062 of 4,412 municipality-years, a 30.6 percent failure. Marta recorded the count, fixed the code formatting, and rechecked. The second merge matched 4,388, leaving 24 unmatched rows, all in three municipalities that had been amalgamated in 2016 and appeared under old codes in one source and new codes in the other. That got a line in the log, a hand-built crosswalk of three entries, and a sentence in the memo.

The wrong turn came in the second week. Marta built the descriptive figure as an event-study plot with estimated coefficients and confidence intervals, treating rollout year as the event and using a two-way fixed effects specification she had seen in a paper on a similar topic. It took two and a half days and it looked like a result. She abandoned it before delivering, for two reasons. The first was that she had not been asked for an estimate, she had been asked for a first look, and delivering an estimate would have moved the project's first credible number into existence without the professor having chosen a design or an estimator. The second was that rollout was staggered across municipalities and she had no basis for knowing whether the two-way fixed effects estimator was appropriate under heterogeneous effects; the honest position was that this was not her decision. What went into the memo instead was a raw plot of mean registrations by year relative to rollout, for the treated municipalities only, with the number of municipalities contributing at each event time shown underneath, and one sentence saying that no estimate had been produced and that the design decision belonged to the professor. That sentence turned out to be the part he quoted back.

The verification pass caught one further problem. The national total of employer firm registrations implied by the panel for 2019 was 41,730. The published national figure was 44,180, a shortfall of 5.5 percent. Tracing it took three hours and found that the extract excluded registrations in the two overseas territories, which was documented on page eleven of the registry's technical note. That went in the memo as a stated limitation with the exact figure, rather than being discovered by somebody at the group meeting.

**Result.** The memo ran two pages: the answer in three sentences, the build in half a page, four labelled caveats, and a paragraph headed what did not work that covered the abandoned event study and why. The professor presented the figure at the group meeting and answered two questions from the log without contacting Marta. The 5.5 percent coverage gap became a footnote in the eventual paper. The whole task took thirty-one hours against an estimate of twenty-four, and the overrun was reported at the checkpoint in week one rather than on the deadline.

The part that mattered was not the panel. It was that a decision Marta was not qualified to make was identified as such and handed back, in writing, before it became a number in a draft.

### A second scenario, where it goes differently

The same assistant, a different brief: a coauthor needs to know, by Thursday, whether anyone has estimated the effect of the specific policy instrument in the paper on firm entry, because the introduction currently claims to be first.

Here the deliverable is a judgement about absence, and absence is the hardest thing to report honestly. Two days of searching found four papers on adjacent instruments and none on this one. The temptation, and it is strong, is to deliver the four adjacent papers and let the framing of the message imply thoroughness. What was delivered instead was the search itself: the databases used, the exact strings, the dates run, the counts at each screening stage, the four adjacent papers with one line each on why they are not the same instrument, and an explicit statement that the search had not covered non-English literature or working papers older than 2018, which were the two places a prior study was most likely to be hiding.

The claim of novelty survived, and it survived in a defensible form, because the coauthor could see exactly what had and had not been looked at. What changed between the two scenarios is that when the finding is a negative, the method becomes the deliverable, and the screening counts stop being bookkeeping and start being the evidence.

## Output

**The task card**, at the top of the work log:

```
TASK CARD
Deliverable:    [what, in what form]
Purpose:        [what it feeds into, and by when it is needed there]
Deadline:       [date]     Checkpoint: [date]
Inputs:         [files, sources, prior work]
Constraints:    [software, licence conditions, what may not be used]
Assumptions:    [numbered; each one confirmed, corrected, or still open]
Open questions: [numbered, each with a proposed answer]
Status:         [not started / in progress / blocked on Q3 / delivered]
```

**The work log**, one entry per session, appended:

```
2026-03-11
Aim:        Merge rollout dates onto registry panel.
Did:        Imported registry extract, built municipality-year counts, merged.
Found:      3,062 of 4,412 matched (69.4%). Cause: leading zeros lost in
            rollout table. Refixed codes as string, rematched: 4,388 (99.5%).
Failed:     First merge. Not a data problem, a formatting problem.
Decided:    Hold municipalities at 2022 boundaries; three-row crosswalk for
            2016 amalgamations, saved as crosswalk_muni_2016.csv.
Open:       24 unmatched rows remain, all pre-2016. Ask AH whether to drop.
Files out:  build/02_merge_rollout.do -> data/derived/panel_v3.dta
```

**The report back**, in this order and no other:

| Section | Content | Length |
| Answer | What was found, stated first, including when it is a negative | 2 to 4 sentences |
| What I did | The method, enough to repeat it | Half a page |
| Numbers and where they came from | Each figure with its source, labelled as reported, calculated, or assumed | Table or list |
| Caveats | Each with its size where quantifiable | Bulleted |
| What did not work | Dead ends, abandoned approaches, and why | One paragraph |
| Open questions | Each with a proposed answer | Numbered |
| Files | Deliverable, scripts, log, with paths | List |

## Failure modes

**Executing a misunderstood brief thoroughly.** Recognisable because the work is good and the reaction to it is polite confusion. Fix by reading the brief back before starting, every time, even when it seems obvious. The briefs that seem obvious are the ones most likely to carry an unstated assumption.

**The plausible placeholder.** A number written because one was needed and the real one could not be found, with the intention of replacing it later. It never gets replaced, because by then it looks like every other number in the document. Fix by writing the gap visibly: a bracketed marker that cannot be mistaken for a figure, plus a line in the report.

**Silent method substitution.** The planned approach did not work, so a different one was used and the report describes the plan. Recognisable when the code and the memo disagree in a detail nobody would check. Fix by treating any deviation from the agreed method as an escalation, not a decision.

**The reconstructed log.** Written on the last day from memory, it contains what the assistant now believes happened, which is a cleaned-up version. Recognisable because it has no failures in it. Fix by writing it as you go; a log with no dead ends in it is evidence that it was written afterwards.

**Confidence flattening.** Reporting a published statistic, an own calculation, and an estimate in the same register. Fix with the explicit vocabulary in step 10, applied to every quantitative sentence.

**Question hoarding.** Sitting on four questions for a week because none felt worth interrupting for. Fix with a fixed weekly batch, sent even when short.

**Presenting model output as a source.** Anything generated by an assistant tool is a draft to be checked against a record, never a citation and never a figure. Recognisable because the source cannot be named when asked.

**Over-delivering into someone else's decision.** Producing an estimate when asked for a description, or a recommendation when asked for options. Recognisable because the deliverable is more impressive than the brief. Fix by delivering what was asked and putting the extra work in a clearly marked appendix, or, when the extra work depends on a decision you are not qualified to make, by not doing it and saying why.

## Edge cases

**The brief is wrong.** The task as set will not answer the question behind it. Do not execute it well and do not silently substitute a better one. Say what you think the underlying question is, what the brief as written will and will not tell them, and what you propose instead, in under a hundred words, and wait.

**The supervisor is unreachable and the deadline is fixed.** Proceed on the most conservative reading of the brief, record every assumption in the task card, mark them in the deliverable where they bind, and deliver on time with the assumptions listed first. Do not delay delivery to wait for an answer that may not come.

**The data cannot be shared with you.** Ask for the codebook, the summary statistics, and a synthetic or shuffled extract with the same structure. You can write and test the entire pipeline against a structural copy, and hand it over to be run by someone with access. Do not ask for a workaround that moves restricted data.

**You find an error in earlier work, including your supervisor's.** Report it the day you find it, with the specific line or number, the consequence, and, where possible, the corrected figure. Report it neutrally and privately. Delay makes it worse in every direction, and an error found by an assistant and reported early is a good outcome for the project.

**Two supervisors give conflicting instructions.** Do not choose. State the conflict in one line to both, with what each implies for the deliverable, and let them resolve it. Choosing silently makes you the author of a decision you cannot defend.

**The task takes three times the estimate and is half done.** Send the checkpoint message with the revised estimate, what is finished, and two options: extend, or deliver the reduced version and name what it will not cover. Never present only the bad option.

**You are the assistant to your own future self.** Solo work is the case where the log is most often skipped and most needed, because there is nobody to notice the gap. Apply the same standard; the person who will not remember is you, in four months, during a revision.

## Quality bar

- The brief was read back in writing and confirmed, with the assumptions listed, before work started.
- Every number in the deliverable can be traced to a source file or a script, and none came from memory.
- Every citation was checked against a live record at the moment it was used, and the check is in the log.
- Source, calculation, and assumption are distinguishable in every quantitative sentence.
- The raw data is untouched and every transformation is in a script that reruns.
- Observation counts are recorded at every step that can change the sample.
- The report says what did not work and what could not be found, in the same document as the findings.
- A colleague could pick up the log, the scripts and the task card and continue without asking a question.

## Adapting this to your context

The example is a doctoral assistant on an economics panel dataset in Stata. The habits are general; the deliverables, thresholds and escalation triggers are not.

- **The deliverable.** A panel, a figure, a memo. In qualitative work the equivalents are a coded extract set, a coding frame and analytic memos, delivered with the NVivo, MAXQDA or ATLAS.ti project file. In survey work, a cleaned response file with the scoring syntax.
- **The sample loss thresholds.** Five percent of a step and twenty percent cumulative come from administrative data with thousands of units. On a clinical or lab sample of 300, five percent is fifteen people. Set the trigger in cases rather than percentages when the sample is small.
- **The escalation rule.** Contacting a participant, changing a consent script or reusing data outside the approved purpose needs the ethics committee or IRB, not only the person who set the brief.
- **The decision handed back.** Here it is the estimator and the clustering. Elsewhere it is the imputation model, the number of factors retained, the level structure of a multilevel model, or a change to the coding scheme.
- **What not to change.** Read the brief back and get a yes before starting; write the log as the work happens; and label every quantity as reported, calculated or assumed.

## Related skills

`thesis-advisor` is the other side of this relationship and sets the brief this skill executes. `research-design` and `research-question-ideation` decide what should be done, where this decides how to do it well and how to report it. `literature-verification` holds the citation standard applied in step 7, and `systematic-review-protocol` is the formal version when a search must be reproducible. `data-profiling-and-cleaning` and `stata-data-management` cover the data work itself, and `stata-do-file-craft` and `python-for-econometrics` the code discipline the scripts must meet. `econometrician` owns the estimator and inference decisions an assistant should escalate rather than take. `research-ethics-and-data-protection` governs the access and licence conditions in the escalation rule. `analysis-audit` is what happens to this work when somebody checks it from the outside, and work done to this standard passes it.
