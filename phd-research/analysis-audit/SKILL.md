---
name: analysis-audit
description: Audits an empirical analysis, your own before submission or somebody else's, and produces a findings report ranked by whether each finding changes a conclusion. Rebuilds the headline number from raw data by an independent path, traces every table and figure to the code and output file that produced it, checks every number in the text against a stored output, and hunts the specific silent errors that survive peer review: a merge that dropped observations, a filter applied twice, a variable constructed differently in two places, a sample that changes between tables, a figure that does not match its table. Use this skill before submitting a paper or depositing a thesis, when taking over someone else's project, when a data editor or referee has queried a number, when two tables disagree, when a coauthor's result cannot be reproduced, or when a result looks too good. Trigger also on vague requests such as "check this before I send it", "can we trust these numbers", "something is off in table 4", or "audit my analysis".
---

# Analysis Audit

Peer review does not catch these errors. A referee reads the argument, judges the design, and checks whether the numbers are plausible given the claim; almost none of them rerun the code, and the ones who do are looking at the specification rather than at the pipeline. So the errors that survive review are the ones that leave a plausible number behind. A merge dropped four percent of observations and nobody counted. A sample filter was applied in the cleaning script and again in the analysis script, with slightly different syntax the second time, so the heterogeneity result is estimated on a narrower population than the paper describes. A variable is constructed in two scripts with two definitions and the tables use different ones. A figure was made from an earlier version of the estimates and no longer matches the table beside it.

None of these produce an error message, and none of them make a result implausible. That is exactly why they survive. The cost is asymmetric: caught before submission, each is an hour of work; caught by a data editor, it is a revision cycle; caught after publication, it is a correction with the author's name on it; and caught by nobody, it is a number that policy or a subsequent literature is built on.

An audit is a deliberately adversarial reconstruction, and it works because it does not trust the code to describe itself.

## When to use this, and when not to

Use it before any submission, before a thesis deposit, before a result goes to a policy audience, when inheriting a project, when a coauthor's number cannot be reproduced, when two exhibits disagree, when a referee or data editor has raised a query about a figure, and whenever a result is surprisingly strong.

Use it on your own work. Self-audit is the highest-yield version because you know where the shortcuts were, and the discipline is to write the findings down as though someone else had found them.

Do not use it to judge whether a paper is worth publishing, which is `refereeing-for-a-journal`, or to anticipate what referees will object to in the argument, which is `peer-review-simulator`. Do not use it to assemble the deposit archive, which is `replication-package`, although an audit is what should happen just before that assembly. Do not use it for the quality of the writing or the framing, which is `thesis-chapter-review`. Do not use it to decide whether the estimator was the right one; that is `econometrician` and `identification-defense`, and an audit takes the design as given and asks whether the paper reports what the code computed.

The distinction in one line: `identification-defense` asks whether the number means what the paper says it means, and this skill asks whether the number is the one the code produced.

## What you need before starting

**The exact version of the manuscript being audited, frozen.** A copy, with a date, that will not change during the audit. Missing: take the copy yourself and tell the authors that the audit applies to that version, because auditing a document somebody is still editing produces findings that cannot be reconciled with anything.

**The code, at the commit or date that produced those tables.** Missing: this is itself a finding of the highest severity, and it should be reported as such before any other work: an analysis whose producing code cannot be identified is not auditable and not reproducible.

**The raw data, or a clear statement of what is unavailable and why.** Missing: proceed with a reduced audit, described below, and state at the top of the report which checks could not be performed. Never let the reduced audit be reported as though it were a full one.

**The ability to run the code, ideally on a machine that is not the author's.** Missing: the audit becomes a reading and reconciliation exercise, which finds perhaps half of what a rebuild finds. Say so.

**The build log or the sample definition.** How many observations entered, how many were dropped at each step, and why. Missing: reconstruct it from the code, and note that the reconstruction is yours; the gap between the author's stated sample and the reconstructed one is often the first finding.

**The headline claim, in one sentence, and the number that carries it.** Missing: ask, or infer it from the abstract, and confirm. Everything in the audit is prioritised against this, and an audit without a priority runs forever and reports the trivial alongside the fatal.

**A time budget.** An audit expands to fill whatever is available. Missing: set one. Two days is a real audit of a single paper; half a day is a check of the headline number and the text-to-output reconciliation, which is worth doing and should be labelled as what it is.

## The method

1. **Freeze the version and open the findings log immediately.** Copy the manuscript, the code and the output directory to a working folder with the date in its name. Start a findings file before reading anything, and write into it as you go, including the things that check out. An audit that records only problems cannot later show what was covered.

2. **Rank the numbers before checking any of them.** Go through the manuscript and mark every number with one of three labels: carries a conclusion, supports a conclusion, or is descriptive. The abstract's numbers and the main table's parameter of interest are the first category; a summary statistic in the data section is usually the third. This ranking sets the order of work and it sets the severity scale used in the report.

3. **Rebuild the headline number from raw data by your own path.** This is the single highest-yield step and it is not the same as rerunning the author's script. Rerunning confirms the code is deterministic; it cannot detect an error that lives in the code. Write your own route from the raw files to the same quantity: your own sample construction, your own variable definitions from the paper's stated definitions, your own estimation command.

Then compare. An exact match is strong evidence that the pipeline is sound. A small discrepancy usually means a sample definition differs, which is worth resolving because it means the paper's description of the sample is incomplete. A large discrepancy means bisect: compare the observation count first, then the mean of the outcome, then the mean of the regressor, then the estimate. The stage at which the two paths diverge localises the error, usually within an hour.

Where an independent rebuild is impossible, because the construction is genuinely intricate, rebuild the most consequential intermediate quantity instead, such as the treatment indicator or the estimation sample.

4. **Build the trace map: every exhibit to the code that made it.** One row per table and per figure, naming the script, the output file it wrote, and the date on that file. Any exhibit that cannot be traced to a script is a finding. Any output file older than the last change to the script that produces it is a finding. Any exhibit whose numbers do not appear in any output file was typed by hand, which is the most serious finding in this category because it means the exhibit and the code have no enforced relationship at all.

```bash
# the cheap version of the trace: does the number in the paper exist anywhere in output?
grep -rn "0\.061" output/ | head
grep -rln "180,412\|180412" output/
```

5. **Check every number in the text against an output file.** Mechanical, tedious, and consistently productive. Take each number in the abstract, introduction, results and conclusion and find it in a stored output. The recurring findings are a number that was correct two versions ago, a percentage computed from a coefficient by hand and computed wrongly, a rounding that differs between the text and the table, and a sample size in the text that does not match the table's observations row.

Pay particular attention to numbers that appear more than once. A coefficient quoted in the abstract, the introduction and the results section has three chances to be stale, and it is usually the abstract that is out of date because it is written first and revised last.

6. **Run the silent error checklist.** These are the specific failures that survive review, in the order they are most commonly found.

| Silent error | How to detect it | What it looks like when found |
| A merge that dropped observations | Recount rows before and after every join in the code; compare the final count with the sum of the source counts | The paper's N is lower than the data section implies, and the difference is a whole category of units |
| A filter applied twice | Search the code for the same substantive condition in more than one script, allowing for different syntax; compare the count after each | The second application removes nothing in most runs and something in one, so the sample differs across tables |
| A variable constructed twice, differently | Search for every assignment to the variable name across all scripts; compare the definitions | Two tables use two different deflators, or a rate expressed once per hundred and once per one |
| A sample that changes between tables | Read the observations row across every table and reconcile each difference against a stated restriction | A robustness column has more observations than the baseline, which no added restriction can produce |
| A figure that does not match its table | Read the plotted values off the figure and find them in the estimates the table was built from | The event study figure's coefficients differ from the table's in the third year |
| A control in the note but not in the code | Read each table note against the estimation command that produced the column | The note claims sector fixed effects that the command does not absorb |
| A deflator or conversion applied twice or not at all | Check the magnitude against an external benchmark, such as a published mean | Real wages implausibly low or high by a factor close to a price index |
| A lag or lead across a panel gap | Count observations lost to the lag operator and compare with the number of gaps | The sample shrinks more than the first period alone would explain |
| Weights applied inconsistently | Search for the weight expression across estimation commands | The summary table is weighted and the regression is not, so the reported mean does not describe the estimation sample |
| A recode with an unbounded else | Read every `recode`, `replace` and `np.where` for a final branch that assigns a value to everything remaining | Missing values silently become zeros, and the zero category grows |
| A drop condition that includes missing | Check every inequality used to drop or keep for a missing guard | In Stata, `drop if x > 100` also drops all missing x; the direction of the bias depends on why x is missing |
| Copy-pasted specification drift | Diff the estimation commands across columns character by character | Column 4 has a control that the table says it does not |

7. **Reconcile the figures against the tables and against the estimates.** For every figure that plots an estimate, find the underlying numbers in an output file, not in the figure's source data if that source was produced separately. Confidence bands are checked the same way: an interval plotted at a different level from the one stated in the caption is common and is invisible unless the numbers are read.

While there, check the figure against the house standard, since an audit is the last point at which it is cheap to fix: series distinguished by marker and dash pattern rather than by colour, legend outside the plot area, accent colour only where one series must be singled out. This is a low-severity finding but it belongs in the report.

8. **Rerun everything from a clean session and diff the outputs.** Delete the contents of the output directory, run the pipeline from the entry point in a fresh session, and compare the regenerated files with the frozen copies. Differences fall into three groups: timestamps, which are ignorable; numerical noise from a seed or an optimiser, which needs the seed fixed; and genuine differences, which mean the delivered exhibits did not come from the delivered code.

9. **Check the internal arithmetic that does not need the data.** A surprising number of findings need no rerun at all. Does the reported number of clusters divide sensibly into the observations? Are subgroup sample sizes summing to the total? Does the coefficient divided by the standard error give the reported significance level? Does the stated percentage effect follow from the coefficient and the dependent variable mean? Do the percentages in a table sum to a hundred? These checks are fast, they can be done without the data, and they are the whole of the reduced audit when the data is unavailable.

10. **Classify every finding by consequence, not by how interesting it is.** Three levels, and the classification is the most useful thing the report does:

- **A: changes a conclusion.** The direction, the significance at the level claimed, the population the result applies to, or the magnitude by enough to change the interpretation.
- **B: changes a reported number without changing a conclusion.** A stale figure in the abstract, a sample size that is wrong by 40, a percentage miscomputed.
- **C: documentation and reproducibility.** An untraceable exhibit, a note that misstates the clustering, a missing seed, a figure that breaches the house standard.

A finding whose consequence you cannot establish is provisional and is reported as such, with what would settle it. Do not inflate severity to get attention and do not deflate it to be kind.

11. **Write each finding so the author can verify it in ten minutes.** Every finding carries the location, the evidence, and the exact commands to reproduce it. A finding that costs the author an hour to confirm will be argued with rather than checked, and the argument is a worse use of everyone's time than the check.

12. **Give the reduced-audit statement wherever a check could not be performed.** List what was not checked and why, at the top of the report rather than at the bottom. A report that is silent about its own coverage will be read as complete.

## The reduced audit, when the data cannot be accessed

Confidential data, a secure enclave, a licence that does not extend to the auditor, or a coauthor who has left. The audit is still worth doing and about half the yield remains. It consists of the internal arithmetic checks in step 9, the text-to-output reconciliation in step 5 where output files exist, the trace map in step 4, the table-note-against-code reading in step 6, cross-table sample reconciliation, and a careful read of the code for the checklist patterns without running it.

What is lost is the rebuild, which is where the largest findings come from. Say so explicitly: "The headline estimate was not independently reproduced because the microdata are not accessible to the auditor. Findings below rest on internal consistency and on code reading."

## Worked example

**Situation.** A team of three was two weeks from submitting a paper on the effect of a workplace training subsidy on firm productivity, using an administrative firm panel of 62,000 firms over nine years. The paper had six tables and four figures. The headline result was a 3.4 percent productivity gain, and a secondary result reported that the effect was concentrated in firms with fewer than 50 employees, which had become the paper's contribution and the subject of its title.

**Task.** Audit before submission, in three days, with findings ranked by whether they changed a conclusion.

**Action.** The first day and a half went into reading the code from top to bottom, roughly 2,400 lines across nine scripts. It produced a list of eleven stylistic observations and no findings. That was the wrong turn, and it is a common one: reading code finds the errors an author would have found themselves, because reading recovers the author's intention rather than testing it. The approach was abandoned at midday on day two and replaced with an independent rebuild.

The rebuild took just over three hours and reproduced the headline 3.4 percent to the third decimal, which retired the largest risk in the paper. It did not reproduce the small-firm result. The independent path gave 2.9 percent for firms under 50 employees against the paper's 6.1 percent, and the two paths had different observation counts in that subsample, 14,880 against 9,213.

Bisecting the difference took forty minutes. The size restriction was applied twice. `03_clean.do` dropped firms whose average employment over the panel exceeded 250, a sample definition the paper describes. `07_heterogeneity.do` then defined the small-firm subgroup as employment below 50 in the first observed year, while the paper described it as below 50 on average. For firms growing through the threshold the two definitions disagree, and because the earlier restriction had already removed the largest firms, the interaction of the two produced a subgroup consisting disproportionately of firms that had shrunk. The 6.1 percent was a real number computed on a population the paper did not describe.

Three further findings came from the mechanical checks. The abstract reported 62,340 firms and the tables reported 61,204; the abstract figure was from a version predating a duplicate resolution. Figure 3's event study plotted the estimates from a specification with year fixed effects while Table 4 reported the same event study with year and region fixed effects, so the two exhibits differed visibly in the fourth year and nobody had compared them. And Table 2's note claimed standard errors clustered at the industry level where the code clustered at the firm level; the correct clustering had been applied everywhere else, so this was a note error rather than an inference error, but it would have drawn a referee comment.

The clean rerun turned up one further item: the bootstrap in the robustness table had no seed, so its p-value moved between 0.038 and 0.052 across runs.

**Result.** One finding of severity A, three of severity B, and four of severity C. The A finding cost the team a week and changed the paper's contribution: the small-firm heterogeneity survived under the paper's stated definition but at 2.9 percent rather than 6.1, which was no longer strong enough to carry the title. The title changed and the heterogeneity moved from the contribution to a secondary result, which the team judged, correctly, to be far better than having a referee find it.

The audit's own lesson was recorded and reused: the day and a half spent reading code produced nothing, and the three hours spent rebuilding produced everything. Subsequent audits on that team started with the rebuild.

### A second scenario, where it goes differently

The same auditor was asked by a colleague at another institution to check a paper using linked tax records held in a national enclave. The auditor had no access to the data and could not obtain it, and the code could not leave the enclave in runnable form; only the scripts and the output logs were available.

The audit ran in reduced form and produced four findings, none of severity A but two of severity B that would have been embarrassing. The observation counts across the paper's five tables could not all be reconciled: Table 3 reported more observations than Table 1 despite Table 3 adding a restriction, which pointed at a merge in the intervening script. Reading that script found a join written as a full outer merge where an inner one was intended, generating rows with missing outcomes that some estimation commands retained and others dropped. The auditor could not confirm this by running anything, so it was reported as provisional with the exact test the author could run inside the enclave in five minutes. It was confirmed the next day.

The second finding was pure arithmetic. A stated effect of "roughly nine percent of the mean" did not follow from the coefficient of 0.0217 and the reported dependent variable mean of 0.318, which gives about seven percent. The paper had used a mean from a different sample.

What changed relative to the full audit was the balance of the method. Without a rebuild, cross-table reconciliation and internal arithmetic carried the whole audit, and every finding had to be written with a reproduction recipe the author could run rather than evidence the auditor had generated. The report opened with two sentences saying exactly which checks had not been possible, so that nobody could later cite the audit as having verified the headline number, which it had not.

## Output

The deliverable is a findings report, ordered by severity, that opens with the coverage statement and the bottom line.

```
ANALYSIS AUDIT
Paper        : Training subsidies and firm productivity, draft of 2026-09-02
Code audited : commit 4f1a9c2, 2026-08-29
Auditor      : M. Oliveira        Dates: 2026-09-03 to 2026-09-05
Coverage     : Full. Raw data available; pipeline rerun from clean session;
               headline estimate independently rebuilt.
Not checked  : Appendix Tables A5 to A9 (time); the geocoding step (external service).

BOTTOM LINE
The headline estimate of 3.4% reproduces exactly by an independent path.
One finding (A1) changes a conclusion: the small-firm heterogeneity result is
computed on a different subgroup from the one the paper describes.
```

| # | Severity | Finding | Location | Evidence | Reproduce in | Effect on conclusion | Action |
| A1 | A | Size restriction applied twice with two definitions; heterogeneity subgroup is not the one described | `07_heterogeneity.do:44`, with `03_clean.do:212` | N of 9,213 against 14,880 under the paper's stated definition; estimate 6.1% against 2.9% | 5 min: rerun line 44 with mean employment | Contribution as titled is not supported; the effect survives at half the size | Restate the definition, re-estimate, revise title and abstract |
| B1 | B | Abstract firm count is from a pre-duplicate-resolution version | Abstract line 4 | 62,340 in text, 61,204 in Tables 1 to 6 | 1 min: `grep` the log | None | Correct the abstract |
| B2 | B | Figure 3 and Table 4 report different specifications of the same event study | Figure 3, Table 4 | Figure from `est_ev_a.ster`, table from `est_ev_b.ster` | 2 min: compare stored estimates | None if the table is correct | Regenerate the figure from the table's estimates |
| B3 | B | Bootstrap p-value not seeded; moves between 0.038 and 0.052 | `09_robustness.do:88` | Three runs, three values | 3 min: rerun twice | Significance at 5% is not stable | Set a seed and report the seeded value |
| C1 | C | Table 2 note states industry clustering; code clusters on firm | Table 2 note | `08_main.do:31` | 1 min | None | Correct the note |
| C2 | C | Figure 2 distinguishes three series by colour only | Figure 2 | Prints as three identical grey lines | n/a | None | Apply marker and dash pattern; move legend outside the plot |

Each severity A finding is written out in full below the table: what the paper says, what the code does, what the corrected number is, and what follows for the claim.

## Failure modes

**Reading the code instead of rebuilding.** Recognise it when a day has produced observations about style and none about numbers. Fix by stopping and rebuilding the headline number independently.

**Rerunning the author's script and calling it a reproduction.** Recognise it because the result matched to every decimal on the first attempt with no independent construction. Fix by writing your own path; a script that reproduces itself proves only determinism.

**Auditing a document that is still being edited.** Recognise it when a finding refers to a sentence that no longer exists. Fix by freezing the version and saying so.

**Reporting everything at the same weight.** Recognise it when a report lists thirty items and the reader cannot tell in ten seconds whether the paper is in trouble. Fix with the three-level severity classification and a bottom line at the top.

**Findings that cannot be checked quickly.** Recognise it when the author's first response is a request for clarification rather than a confirmation. Fix by including the location, the evidence and the exact reproduction command in every finding.

**Stopping at the first serious finding.** Recognise it when the report has one item. Errors cluster, because they come from the same working habits; a project with one duplicated filter usually has more. Finish the checklist.

**Inflating severity.** Recognise it when a documentation issue is written as though it threatened the result. Fix by applying the definition of A strictly: it changes a conclusion, not merely a number.

**Auditing your own work without writing findings down.** Recognise it when problems were found and fixed but no record exists. Fix by keeping the log anyway; it is what you send to the data editor and what you reuse next time.

**Confusing an audit with a critique of the design.** Recognise it when findings concern whether the instrument is valid rather than whether the code computed what the paper reports. Fix by routing those to `identification-defense` and keeping the audit to fidelity.

## Edge cases

**The code cannot be found or does not run.** Report it as the first finding at the highest severity and stop the technical audit until it is resolved. Everything else is unverifiable, and delivering partial findings against unrunnable code implies more assurance than exists.

**Auditing a colleague's work, socially.** The technical method is identical; the framing decides whether it gets used. Audit everything including your own contributions, present findings against the analysis rather than against a person, lead with what reproduced correctly, and send the report before discussing it so the author reads it without an audience. Deliver severity A findings in person or by call, never as the fourth item in a list.

**A finding you cannot resolve.** Report it as provisional, state what you observed, state what would settle it, and give the author the test. An unresolved observation reported honestly is useful; an unresolved observation reported as a fact is a finding you will have to withdraw.

**Very large analyses.** Do not attempt exhaustive coverage. Audit the headline number fully, sample the rest, and state the sampling: "Three of eleven appendix tables were traced and checked; the remaining eight were not." A stated sample is a defensible audit and an unstated one is a misleading one.

**The result does not reproduce and the author disagrees.** Move to the smallest quantity where the two paths differ, usually an observation count or a mean, and resolve that. Arguments about coefficients are unresolvable; arguments about how many rows are in a sample are settled in one command.

**An audit that finds nothing.** Report it plainly, with the coverage statement, and resist manufacturing severity C findings to justify the time. A clean audit of a well-built project is a real and reportable outcome, and it is worth the effort precisely because it might not have been.

**Auditing an analysis whose author is unavailable.** Reconstruct the intended sample from the manuscript rather than the code, since the manuscript is the claim being audited, and report every place where the code and the manuscript imply different populations.

## Quality bar

- The report opens with a coverage statement naming what was and was not checked, and a bottom line stating whether any finding changes a conclusion.
- The headline number was rebuilt from raw data by a path independent of the author's script, or its absence is stated.
- Every table and figure is traced to a script and an output file, and any untraceable exhibit is reported as a finding.
- Every number in the abstract, introduction and conclusion was checked against a stored output.
- Every finding carries a location, evidence, and a reproduction step the author can run in under ten minutes.
- Findings are ordered by whether they change a conclusion, and the severity definitions are applied strictly.
- The full pipeline was rerun from a clean session and the regenerated outputs were compared with the audited ones.
- The silent error checklist was completed rather than abandoned after the first serious finding.

## Related skills

`stata-do-file-craft` and `python-for-econometrics` describe the pipeline discipline whose absence this audit detects, and `stata-data-management` the merge and sample checks whose omission it finds. `regression-table-production` is where the table-to-code traceability is established in the first place, and following it makes most of step 4 unnecessary. `econometrician` and `identification-defense` handle the questions this skill deliberately excludes, namely whether the estimator and the design were right. `peer-review-simulator` predicts what a referee will object to in the argument, where this checks what a data editor will find in the code. `replication-package` is assembled after the audit passes, not before. `response-to-reviewers` uses audit findings when a query has to be answered with a corrected number.
