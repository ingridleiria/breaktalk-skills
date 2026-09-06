---
name: replication-package
description: Closes a project by assembling and testing the package that lets a stranger regenerate every table and figure in the paper from the raw data with one command: a standard folder structure, a README written for both a data editor and a replicator, a manifest mapping every exhibit to the script that produces it, code cleaned of absolute paths and secrets, a pinned environment, an honest data availability statement with an access route, and a from-scratch test run whose log is included. Enforces the rule that the package is not finished until it has been run in a clean location and every number matched against the submitted manuscript. Use this skill when someone asks to make a project reproducible, prepare code and data for submission or deposit, respond to a journal's data editor, tidy a project before handing it to a coauthor, or archive work at the end of a degree. Trigger also on vague requests such as "can someone else run this", "I need a DOI for my code", "the journal is asking for my data", or "I am leaving and someone has to take this over".
---

# Replication Package

Reproducibility is not a virtue added at the end. It is a property a project either has or does not, and the packaging step only makes visible which one is true. That is why the exercise so often produces an unwelcome discovery: the package is assembled, the master script is run in a clean folder, and Table 3 comes out different from Table 3 in the submitted manuscript.

That discrepancy is the failure this skill exists to catch, and it catches it in the one week when it is still cheap. The usual causes are mundane and none of them are misconduct: a number was edited by hand in the manuscript after a specification changed, a filter was applied interactively in a console and never written into a script, a file was overwritten by a later run, a seed was never set, or a variable was constructed one way in the cleaning script and another way in a robustness script written four months later. Found before submission, it is a day's work. Found by a journal's data editor at the acceptance stage, it delays publication and puts the paper on a list nobody wants to be on. Found by a reader after publication, it is a correction, and the reason it is a correction rather than a private embarrassment is that the discrepancy is now public and permanent.

There is a second failure, quieter and just as expensive. A project that only one person can run. When that person leaves, graduates, or simply forgets, the work stops being extendable. Every subsequent paper in that line either starts again or inherits an unverifiable foundation.

## When to use this, and when not to

Use it before every submission to a venue with a data or code policy, which is now most of them, and not after acceptance, because the data availability statement in the manuscript has to be true when it is written. Use it before a thesis deposit where the institution requires code. Use it when handing a project to a coauthor, a successor, or a research assistant. Use it when a data editor has asked for materials. Use it at the end of a degree or a post, when the work has to survive its author's departure. Use it when a coauthor's result cannot be reproduced, because that situation is a packaging problem until proven otherwise.

Do not use it to find out whether the numbers are correct. That is `analysis-audit`, which rebuilds the headline figure by an independent path and hunts the specific silent errors that survive peer review. The two are complementary and the order matters: this skill will tell you that the code produces Table 3 consistently, and it cannot tell you that Table 3 is right. Where a discrepancy appears during the test run, it is handed to `analysis-audit`.

Do not use it to set up a project at the start; that is `stata-project-scaffold` and the equivalent conventions for other languages, and a project built to those conventions makes this skill a two-day job instead of a two-week one.

Do not use it to write the data section of the paper, which is `data-section-writer`, although the data availability statement produced here must agree with it exactly.

## What you need before starting

**The submitted or final manuscript, with its exact tables and figures.** The package is verified against a specific version of the paper, and "the current draft" is not a version. Missing: fix a version, name it, and put its date in the README. Every subsequent claim of a match is against that file.

**All the code, including the parts nobody wants to include.** The interactive session where the sample was defined, the spreadsheet where a number was reformatted, the script that was run once and deleted. Missing: reconstruct what is missing before packaging, because an undocumented manual step is exactly what the test run will fail on, and it is better to find it now deliberately than in three days by accident.

**The raw data, or the exact route to obtain it.** Provider, dataset name, version, access conditions, and any pre-processing applied before the package's first script. Missing: document the route in as much detail as exists and mark the package as untested from raw data, which is a substantive limitation and must be stated rather than glossed.

**The target's requirements.** The journal's data and code policy, the repository's deposit requirements, the institution's deposit rules, any funder mandate. These differ on repository choice, licence, metadata, embargo and file formats. Missing: fetch them; where no live lookup is available, build to the general standard set out here and add a checklist item to verify before deposit.

**The data licence or agreement, read rather than remembered.** What may be redistributed, what may be derived and shared, what must be destroyed and when. Missing: find the document. A data availability statement that contradicts an agreement is a serious problem and it is usually made in good faith by someone recalling the terms.

**A clean environment to test in.** A fresh container, a different machine, a new user account, or at minimum a new directory with an empty environment. Missing: perform the strictest test the environment allows, state exactly what was and was not tested, and supply the test procedure as a checklist for the user to run where they can. Never describe an untested package as tested.

## The method

1. **Fix the manuscript version and build the manifest first**, before touching any code. One row per exhibit in the paper: table or figure number, the script that produces it, the output file, and the numbers that must match. Building this first is what converts packaging from tidying into verification, and it routinely finds exhibits that no script produces, which is the discovery the whole exercise exists for.

2. **Lay out the standard structure** below and copy the project into it, rather than reorganising in place. Copying preserves a working version while the package is being broken and rebuilt, which it will be.

3. **Order the scripts into a pipeline** with a numbered sequence and a master script that runs them all. Every script has one job and a header stating its purpose, inputs and outputs. Where the original project's structure does not permit this, the reordering is the work, and it is the step that most often reveals that two scripts write to the same intermediate file.

4. **Clean the code** to the rules below: no absolute paths, no credentials, no manual steps, no dead code, seeds set wherever randomness enters, output written only to the output folders.

5. **Pin the environment.** Language version, package versions, and the install commands. A package list without versions is not an environment; code that ran in one version of a statistical package frequently produces different results in another, and the estimator defaults that changed between versions are the ones that bite.

6. **Write the README** to the structure below, for the two readers it actually has: a data editor deciding whether the package meets policy, and a replicator trying to run it.

7. **Write the data availability statement**, honestly, against the licence document. Where data cannot be shared, say why, name the access route, state the expected wait, and supply a synthetic dataset with the same structure so the code can be executed. This statement goes into the manuscript, so it must be settled before submission.

8. **Run the test from a clean location** and record everything, following the procedure below. This is the step that makes the package real and it is the step most often skipped under deadline.

9. **Reconcile every discrepancy** the test run produces. Each one is a finding. Do not adjust the package to match the paper; find out which is right, and where the paper is wrong, correct the paper. Where the discrepancy indicates a substantive error, hand it to `analysis-audit` before doing anything else.

10. **Complete the compliance checklist** for the journal, repository and institution: licence chosen, repository selected, DOI obtained, metadata completed, embargo handled, statement text agreed with the manuscript.

11. **Deposit, then verify the deposit** by downloading it fresh and checking that the file list matches the manifest. Deposits truncate, refuse file types, and silently drop empty folders more often than anyone expects.

## The standard structure

```
paper-short-name-replication/
  README.md
  LICENSE
  data/
    raw/            original files, or instructions to obtain them
    clean/          analysis files, produced by the code, never edited by hand
  code/
    00_master.*     runs everything, in order
    01_import.*
    02_clean.*
    03_construct.*
    04_analysis.*
    05_exhibits.*
    environment.*   package list with versions and install commands
  output/
    tables/
    figures/
    logs/
  docs/
    codebook.md
    data_availability.md
    manifest.csv
    test_run_log.txt
```

The rule that carries most of the weight: everything in `data/clean` and `output` is disposable and regenerable. If deleting those two folders and rerunning the master script does not reproduce them, the package is not finished. Make that deletion part of the test.

## The README

The README is read by a data editor first and a replicator last. Write for both.

1. **Overview.** The paper's citation, what the package reproduces, the manuscript version it was verified against, total run time, and the hardware and memory required. A replicator's first question is whether this will take twenty minutes or two days, and it should be answerable in the first paragraph.
2. **Data availability.** For each dataset: whether it is included, its source, its version, its licence, exactly how to obtain it if not included, and any transformation applied before inclusion. Where data cannot be shared, the reason, the access route, the expected wait, and what is supplied instead.
3. **Software requirements.** Language and version, packages with versions, the operating system tested on, and the install commands. Where a package is no longer available at the pinned version, say so and name the workaround.
4. **Instructions.** The single command that runs everything, and how to run one stage. What appears where when it works.
5. **Mapping.** The manifest, as a table in the README as well as a file, linking every table and figure in the paper to its script and output file. This is the first thing a data editor checks.
6. **Notes.** Random seeds, known sources of non-determinism, run time per stage, and any manual step. There should be none; where one exists, it is documented, justified, and treated as a defect to be removed rather than a feature to be explained.

## Cleaning the code

- **No absolute paths.** One root variable, set once in the master script, everything else relative to it. This is the most common single reason a package fails on another machine.
- **No credentials, keys, tokens or personal information** in code, logs, or committed history. Check the logs specifically; connection strings end up there.
- **A header on every script**: purpose, inputs, outputs, and the exhibits it produces.
- **Dead code removed.** The package contains what the paper uses. Abandoned experiments belong in a separate archive, not in the replication package, where they confuse a replicator about what matters.
- **Package installation handled by the master script or the environment file**, never assumed to be present.
- **Output written only to the output folders**, never to the working directory or to a path outside the package.
- **Seeds set wherever randomness enters**: bootstrap, simulation, matching, sampling, cross-validation, any stochastic optimiser.
- **No interactive steps.** No prompts, no manual file selection, no "then open this in a spreadsheet".
- **Intermediate files written once**, by one script. Two scripts writing the same intermediate file is a defect that produces order-dependent results and is invisible until someone runs the pipeline in a different order.

## The test run

1. Copy the package to a clean location, or a fresh environment, with only `data/raw` present.
2. Delete `data/clean` and `output` entirely.
3. Install the environment from the environment file, from scratch, and record any failure.
4. Run the master script. Record the wall-clock time and the full log.
5. Compare every output against the manuscript, table by table and figure by figure, using the manifest. Check the numbers, not the shape: a table that looks right and has a coefficient differing in the third decimal is a finding.
6. Record every discrepancy, resolve each one, and note the resolution in `docs/test_run_log.txt`.
7. Where a clean environment is not available in the session, run the strictest available approximation, state precisely what was tested and what was not, and supply the full procedure above as a checklist for the user to execute where they can.

A package that has not been through this has not been tested, and describing it as tested is the one thing in this whole method that cannot be recovered from later.

## Confidential and restricted data

Restricted data is normal in empirical social science and it does not exempt a project from reproducibility; it changes what reproducibility means.

Document the access process in full detail: the holder, the application route, the eligibility conditions, the typical wait, the cost, and the citation for the exact dataset and version. Include all the code that would run on the restricted data, unchanged. Include a synthetic dataset with the same variable names, types, ranges and structure, clearly labelled as synthetic, so that a replicator can execute the pipeline end to end and confirm that the code runs and produces exhibits of the right shape. Where the provider permits, include summary statistics of the real data so the replicator can check that the synthetic data resembles it in the ways that matter.

Then state plainly, in the README, what a replicator can verify without access and what they cannot. That sentence is what makes the package honest, and its absence is what makes a restricted-data package look like an excuse.

## Journal and repository compliance

Fetch the target journal's data and code policy and the repository's requirements. Where no live lookup is available, build to the general standard here and record the verification as an outstanding checklist item.

The items that recur: deposit in a specified repository rather than a personal site or a code-hosting account, a DOI for the deposit, a licence chosen for code and, separately, for data, a data availability statement in the manuscript matching the package, metadata completed, and any embargo set correctly. Many policies also require that the package be deposited before acceptance rather than after, and that the code be able to run without the author's institutional resources.

Choose the licence deliberately. A permissive licence for code and an appropriate open licence for any data you own is the usual answer; data you do not own cannot be licensed by you at all, which is a distinction that is frequently got wrong.

## Worked example

**Situation.** A three-author paper on hospital staffing and patient outcomes had been accepted subject to the journal's data editor clearing the replication package. The analysis had run over four years across two institutions, in about 40 scripts, with three intermediate datasets and a mix of two statistical languages. The lead author, Sam Whitfield, had left academia eight months earlier and was answering emails at weekends. The data editor gave four weeks.

**Task.** A package the data editor would clear, from a project nobody had run end to end since the second revision.

**Action.** The manifest was built first, from the manuscript rather than from the code: 11 tables and 6 figures, 17 rows. Mapping them to scripts took two days and produced the first two findings before any code ran. Figure 4 was produced by no script in the project; it had been built in a spreadsheet from numbers pasted out of a log, in the week of the first submission. And Table 7 and Table A3 both claimed to come from the same script, which turned out to have been edited between the two runs, so only one of them could be current.

The structure was laid out and the project copied into it. The scripts were ordered into a five-stage pipeline, which exposed that two separate cleaning scripts both wrote a file called `analysis_sample`, one in each language, and that which version survived depended on the order in which they were run. That was the third finding and it was the serious one.

Cleaning found 31 absolute paths across the 40 scripts, two of them pointing at a network drive at an institution the second author had left, and a database connection string with a username and password in a script header, which had also been written into a log file that had been sitting in the project folder for three years.

**The wrong turn.** The first test run was performed in the project's own working directory, with the existing `data/clean` folder present, because regenerating the intermediate files was estimated at nine hours and the deadline was tight. It passed. Every table matched. That result was worthless and it was recognised as worthless when the second author asked which of the two `analysis_sample` files the run had used, and nobody could answer, because the file was already on disk before the run began and neither cleaning script had needed to write it.

The run was redone properly: clean location, `data/clean` and `output` deleted, environment installed from scratch. It failed in the second stage on a package that had been renamed in a newer release of one of the languages, which took half a day to resolve and pin. It then completed in seven hours and forty minutes.

Against the manuscript, 15 of 17 exhibits matched exactly. Two did not. Table 7's fourth column differed in the second decimal across all six coefficients, which traced to the `analysis_sample` collision: the manuscript's Table 7 had been produced from the version written by the script that no longer ran last. The difference was small and did not change any conclusion, but the manuscript was wrong. Figure 4, having no script, was rebuilt properly in code, and the rebuilt version differed visibly from the published draft in one series, which traced to a transcription error made in the spreadsheet three years earlier.

Both were handed to `analysis-audit` to confirm which version was correct before anything was changed. The audit confirmed the newly generated versions and found nothing further.

**Result.** The manuscript was corrected before publication, with a note to the editor explaining both changes. The package cleared the data editor on the first review, with one comment asking for the run time to be stated more precisely per stage, which took twenty minutes. Total effort: about nineteen days across three people, of which roughly six were spent on the two exhibit discrepancies and their resolution.

The counterfactual was stated by the data editor in the clearance note, and it is the reason the exercise is worth its cost: a discrepancy of that kind found after publication is a correction, and a corrected paper is cited with its correction for as long as it is cited at all.

### A second scenario, where it goes differently

A doctoral thesis deposit, single author, one language, data from a public survey that may be redistributed, and the project built from the start on a project scaffold with numbered scripts, a master file, and relative paths.

Here the package is two days rather than nineteen, and the method shortens to the manifest, the README, the environment pin, the test run, and the deposit. The structure already exists. There is no licence complication, because the survey's terms explicitly permit redistribution with attribution, and that clause was checked rather than assumed.

What must not be shortened is the test run. The single most common failure in this easy case is the assumption that because one person has run the pipeline many times, it runs. It usually does not: the pipeline has been run in pieces, in an order the author knows, with a `data/clean` folder that has been accumulating for two years, and one intermediate file in it was produced by a script that was later edited. Deleting `data/clean` and running from scratch is a twenty-minute test in this case and it is the whole value of the exercise.

The other difference is the audience. A thesis deposit's replicator is most likely to be the author themselves in three years, or a supervisor's next student building on the work. The README should therefore say what the project is for and what its intermediate files mean, which a journal package does not need to do and which is the part that makes the work extendable rather than merely verifiable.

## Output

**The package**, in the structure above.

**The manifest**, as `docs/manifest.csv` and as a table in the README:

| Exhibit | Paper table or figure | Script | Output file | Verified against manuscript | Notes |

**The README**, to the six-part structure above.

**The data availability statement**, in the wording that will appear in the manuscript:

```
DATA AVAILABILITY
Dataset:            [name, version, provider]
Included:           [yes / no, with the reason]
Access route:       [exact route, application form, expected wait, cost]
Licence:            [terms, and what they permit]
Supplied instead:   [synthetic data, summary statistics, or nothing]
What a replicator can verify without access: [...]
What they cannot:   [...]
```

**The test run log**, `docs/test_run_log.txt`: environment, date, wall-clock time per stage, the full console log, the exhibit-by-exhibit comparison, and every discrepancy with its resolution.

**The compliance checklist**

| Requirement | Source | Status |

## Failure modes

**Testing in the project's own folder.** Recognise it when `data/clean` was present before the run. Delete it and run again; a run that does not regenerate its intermediates has tested nothing.

**An exhibit with no script.** Recognise it while building the manifest, which is why the manifest comes first. Rebuild it in code, and expect the rebuilt version to differ.

**Two scripts writing the same intermediate file.** Recognise it by listing every file written by every script and looking for duplicates. This produces order-dependent results and is invisible in normal use.

**Absolute paths.** Recognise them by searching the code for the drive or home directory prefix. One root variable, set once.

**Credentials in code or logs.** Recognise them by searching for the obvious keywords, and check the log files specifically, which people forget.

**An environment without versions.** Recognise it when the file lists package names only. Pin versions and record the language version.

**A manual step described as a feature.** Recognise it in the phrase "then open". Automate it or the package is not one command.

**Adjusting the package to match the paper.** Recognise it when a discrepancy is resolved by changing code until the old number reappears. Find out which is right first; that is `analysis-audit`.

**A data availability statement written from memory.** Recognise it when nobody has opened the agreement. Read the licence.

**Packaging after acceptance.** Recognise it when the statement in the manuscript was written before the package existed. The statement has to be true when submitted.

**Depositing without verifying the deposit.** Recognise it when nobody downloaded the deposited archive. Download it and check it against the manifest.

## Edge cases

**The data cannot be shared at all.** Follow the restricted-data section: full access documentation, all the code, a labelled synthetic dataset, summary statistics where permitted, and an explicit statement of what can and cannot be verified. This is a complete and respectable package and should not be presented apologetically.

**The analysis is not deterministic.** Set seeds everywhere. Where non-determinism remains, from parallel execution, floating-point ordering, or an external service, document it, state the expected tolerance, and report the variation observed across two runs rather than pretending it does not exist.

**The pipeline takes days to run.** Provide a fast path on a documented subsample that exercises every script and produces exhibits of the right shape, alongside the full path. State the run time of both. Data editors accept this; they do not accept an untested full path.

**Proprietary or licensed software is required.** Name it and its version. Where a free alternative can run part of the pipeline, provide that route and say what it covers. Never make the package depend on a paid tool for something a free one can do.

**The raw data is enormous.** Deposit the code and the construction instructions, host the data where the repository permits, and provide checksums for the raw files so a replicator can confirm they obtained the same version. Version drift in public datasets is a real and under-recognised source of failed replications.

**A coauthor's code cannot be run or understood.** Treat it as a takeover: get it running unmodified first, in isolation, before improving anything. Where it cannot be run at all, say so in the package rather than rewriting it into something that produces different numbers, and route the numbers themselves to `analysis-audit`.

**The project is being handed over rather than published.** Add a short orientation document: what the project is trying to establish, what has been tried and abandoned, what the open questions are, and where the decisions are recorded. That is what a successor needs and no manifest supplies it.

**The paper has already been published and a discrepancy is found.** Establish which version is correct, contact the editor promptly with the specifics, and prepare the corrected exhibits. Delay makes every part of this worse.

## Quality bar

- One command reproduces every table and figure from raw data, with no manual step.
- The manifest maps every exhibit in the paper to a script and an output file, and was built from the manuscript before any code was touched.
- The test run was performed in a clean location with `data/clean` and `output` deleted, and its log is included in the package.
- Every output was compared to the manuscript number by number, and every discrepancy is recorded with its resolution.
- No absolute paths, no credentials in code or logs, seeds set wherever randomness enters.
- The environment is pinned with versions and installs from the environment file.
- The data availability statement was written against the licence document and matches the manuscript exactly.
- The deposit was downloaded fresh and checked against the manifest.

## Related skills

`analysis-audit` rebuilds the numbers and takes over whenever the test run produces a discrepancy; the two are complementary and neither substitutes for the other. `stata-project-scaffold` and the equivalent conventions in other languages make this skill cheap by building the structure at the start rather than reconstructing it at the end. `data-section-writer` writes the paper's data section, which must agree with the data availability statement produced here. `research-ethics-and-data-protection` governs what may be shared and is the authority behind the licence reading. `journal-targeting` surfaces the target's data policy in time for the package to be built before submission rather than after acceptance. `response-to-reviewers` requires the package to be updated whenever a revision changes any analysis. `thesis-advisor` should schedule this as load-bearing work before deposit, since many institutions require it. `full-manuscript-build` produces the exhibits this package must regenerate exactly.
