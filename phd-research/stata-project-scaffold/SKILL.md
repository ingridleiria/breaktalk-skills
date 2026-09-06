---
name: stata-project-scaffold
description: Lays out an empirical Stata project before the first line of analysis is written: the folder tree with a read-only raw directory, the numbered do-file skeleton from setup through to figures, a master do-file that runs the stages in order with a toggle each, a stage contract saying which file owns which decision and what it reads and writes, output naming that maps every table and figure back to one stage, a project-local package directory, and a register of the decisions still open. Enforces the rule that any given decision lives in exactly one stage, so a sample restriction or a variable definition can never exist in two places and diverge. Use this skill when starting a new empirical project, thesis chapter or replication, when somebody asks for a do-file structure or a master do-file, when a project has grown into one enormous script or into several chapter folders that each clean the same data, when two chapters report different sample sizes for the same population, or when a new team member asks where anything is. Trigger also on vaguer requests such as "how should I organise this project", "give me the base do-files", "set this up properly", or "where should this code go".
---

# Stata Project Scaffold

The failure this prevents is not that code will not run. It is that nobody decided where things go, so the same decision ends up in several places and the copies drift apart. A sample restriction gets written into the cleaning file for the first chapter and again, slightly differently, into the analysis file for the second. A variable definition exists in two forms because a coauthor needed a version with a different denominator and wrote it where they were working. An output called `main_table_v3_FINAL.tex` sits in a folder next to `main_table_new.tex` and neither is dated. Six months later two chapters report different sample sizes for the same population, and finding out which is correct means reading everything.

That is a structural failure, and it is expensive in a specific way: it is discovered late, usually when the pieces are assembled for a thesis or a submission and the numbers are compared for the first time. At that point the fix is a rebuild, and a rebuild under a deadline is where results change and nobody is sure whether the change is a correction or a new mistake. The scaffold is cheap insurance against this because it is an hour of decisions taken on day one, when there is no sunk cost and no wrong answer to defend.

There is a second cost, quieter. A project without a decided structure cannot be handed to anybody. A supervisor cannot check it, a coauthor cannot contribute without asking where everything lives, and a research assistant cannot be given a task without also being given a tour. Structure is what makes a project a thing that other people can work on.

## When to use this, and when not to

Use it at the start of any empirical project that will produce more than one table: a paper, a thesis chapter, a report, a replication of somebody else's work. Use it when an existing project has become a single very long do-file, or a set of chapter folders that each clean the same source data. Use it when a second person joins a project, because the moment of joining is when an undecided structure becomes visible and is still cheap to fix.

Use it when a project is about to be handed over, whether to a successor, to a coauthor, or to a journal data editor, since the tree and the stage contract are most of what the recipient needs.

The three-way boundary with its siblings, because they are easy to confuse and each covers something the other two deliberately leave out:

**This skill decides what files exist and what each one is responsible for.** The folder tree, the numbered stage skeleton, which stage owns which class of decision, what each stage reads from disk and writes to disk, how outputs are named so they trace back to a stage, and the register of decisions not yet taken. It is the map.

**`stata-do-file-craft` decides how the code inside any one of those files is written.** Version statement, the single machine-specific line and relative paths everywhere else, timestamped logging, locals against globals, loops instead of copy-paste, defensive assert and isid checks, where capture is permissible, seeds, and the ban on editing data interactively. It is the standard the contents of every file must meet, and it also governs what the master do-file must contain once this skill has decided which stages the master calls.

**`stata-data-management` decides what happens to the data.** Import types, destring against encode, labels, Stata's date representation, merge and its match indicator, joinby, append, reshape, duplicates, missing value codes, collapse against egen by group, xtset and panel checks, compress and save. It is the operations that stages 02 to 05 perform.

Put concretely: this skill says there is a file called `03_clean.do` and that it is the only place cleaning decisions live; `stata-do-file-craft` says that file must open with a version statement, log its run and assert its key; `stata-data-management` says how to handle the sentinel value inside it. Where two of them appear to speak to the same thing, the rule is that this skill decides which file, craft decides the file's form, and data management decides the command.

Do not use it to choose the estimator or the clustering, which is `econometrician`. Do not use it to build the tables the analysis stages export, which is `regression-table-production` for content and `academic-tables-booktabs` for typography. Do not use it as the deposit checklist for a replication archive, which is `replication-package`; that skill assembles and documents a project that already meets this standard. Do not use it for a Python project, where `python-for-econometrics` covers layout, environment pinning and the equivalent discipline.

## What you need before starting

**The project name and where it will live.** Missing: use a short lowercase name derived from the topic rather than from the funder or the chapter number, since chapter numbers change and folder names outlive them.

**The data sources, one line each: what, from whom, in what format, roughly how large.** This determines whether import is one stage or several. Missing: scaffold for the sources you know and add stages later, but name the unknown source in the register so it is not forgotten.

**The intended unit of observation of the analysis file.** Missing: decide it before generating anything, in one sentence, because it determines what stage 05 does and it is the thing most often left implicit.

**The design: panel fixed effects, difference-in-differences including whether adoption is staggered, instrumental variables, regression discontinuity, matching, or a cross-section.** This decides the contents of the diagnostics stage and which packages the setup stage installs. Missing: scaffold the diagnostics stage as a stub with a comment naming the decision, and put the design choice at the top of the register, because it is the decision everything else waits on.

**The main treatment and outcome variables, by name or by description.** Missing: use descriptive placeholder names that read as English, never `x` and `y`, since placeholders that read as English get replaced and single letters get kept.

**Whether this is one paper or a thesis with several chapters sharing data.** This is the single most consequential layout decision and it is settled in step 2. Missing: assume a thesis, because the shared-pipeline layout costs almost nothing on a single paper and converting a single-paper layout into a thesis layout later is a rebuild.

**Who else will run this code, and on what operating system.** Missing: assume at least one other person on a different system, which costs one conditional in the master file and saves a day later.

**The Stata version and flavour available to everyone involved.** Missing: scaffold to the lowest version anyone has, and record it, since a do-file written under a newer version can fail silently in an older one on syntax that changed meaning.

## The method

1. **Ask the eight questions above and fill the scaffold with real names.** A scaffold delivered with placeholders is a template; a scaffold delivered with the project's own source names, variable names and stage descriptions is a working project. The judgement call is what to do when an answer is not yet known, and the rule is to generate the stage anyway with a header describing its intended contract and a tagged entry in the register, rather than omitting it, because a missing stage is invisible and an empty stage with a header is a prompt.

2. **Decide between the one-paper layout and the shared-pipeline layout.** The rule: if more than one output document will use the same cleaned data, the data pipeline is shared and lives once, and each document gets its own analysis folder that reads the shared analysis file and never reads raw data. If there is exactly one document, use the flat numbered layout. The failure this rule prevents is chapter folders that each clean the same source, which is how two chapters come to report different sample sizes. A chapter may of course apply its own further restriction; it does so in its own analysis stage, from the shared file, with the counts logged.

3. **Create the tree, and make `data/raw` read-only in the file system.** Not by convention, by permission, where the platform allows it. The accident being prevented is a save with the wrong path in it, which is unrecoverable when the source cannot be re-obtained. Record a checksum or the size and date of each raw file in `docs/`.

4. **Write the stage contract before writing any stage.** One row per stage: what class of decision it owns, what it reads, what it writes, and what it must not do. The last column is what makes the contract work. `04_construct.do` must not drop observations; `05_sample.do` must not create variables; `08_main_results.do` must not modify the data. These prohibitions are what keep a decision in exactly one place, and they are worth stating in each file's header so that the person writing the file sees them.

5. **Set the rule that every stage begins with a load from disk and ends with a save or an export.** No stage depends on what is in memory when it starts. This is what makes a single stage rerunnable, which is what makes the toggles in the master file meaningful, and it is the property that a single long script cannot have. The judgement call is how many intermediate files to keep, and the rule is one per stage that changes the data, since storage is cheap and the ability to reload the file as it stood before a mistaken step is what converts a two-day recovery into ten minutes.

6. **Write the master as an orchestrator and nothing else.** It sets the root, the options, the log and the seed, then calls the stages in order, each behind a local toggle so one can be rerun alone. It contains no data work at all, because anything it computes becomes invisible state the stages silently depend on. Its detailed contents standard belongs to `stata-do-file-craft`; what this skill decides is which stages exist, in what order, and that the master is the only entry point.

7. **Set the output naming convention, and derive it from the stage.** Every exported file carries the stage number that produced it: `tab03_main.tex` from stage 08 is worse than `t08_main.tex`, because a reader tracing a table wants the stage, not the table's position in the paper, which changes. Keep a two-column map in the README from paper exhibit number to file name, since the paper's numbering will change and the file names should not. Never allow a version suffix in a file name: versions live in the version control system or in the log's timestamp, and a file called `_v3_final` is a confession that outputs are being kept by hand.

8. **Clear the output directories at the start of a full master run.** This is what makes a missing table visible instead of being silently satisfied by last week's file, and it is the single cheapest protection in the scaffold. Guard it so that it happens only on a full run, never on a single-stage rerun.

9. **Put shared definitions in exactly one place.** `_globals.do` holds variable lists, control blocks, sample definitions and labels used by more than one stage; `_graphprefs.do` holds the graph scheme applied once. The rule: any list that appears in two stages moves to `_globals.do` immediately, because a control list copied into two regressions is the most common source of two tables that should match and do not.

10. **Install user-written packages into a project-local directory and record their versions.** Set the package directory inside the project so the packages travel with it, and have the setup stage check for each rather than installing unconditionally, so a run does not silently update a package mid-project and change a result. Record the version of each in the README.

11. **Choose the diagnostics stage from the design.** This is the one stage whose contents are not generic, and getting it stubbed correctly on day one is what makes the design real rather than aspirational:

| Design | Stage 07 contains |
| Panel fixed effects | Within variation of the treatment, group and period counts, balance of the panel, sensitivity of the coefficient to the fixed effects set |
| Two-period difference-in-differences | Pre-period balance, a plot of both groups' outcome paths, treatment timing check |
| Staggered adoption | Cohort and timing table, event-study estimates with a stated reference period, a heterogeneity-robust estimator alongside the two-way fixed effects version |
| Instrumental variables | First stage with its diagnostic statistic, reduced form, the instrument's balance against covariates, the exclusion argument written as a comment |
| Regression discontinuity | Running variable density, covariate continuity at the threshold, bandwidth sensitivity, the raw binned plot |
| Matching or reweighting | Common support, balance before and after, the distribution of weights |
| Cross-section | Sensitivity to the control set, and a written statement of what the coefficient does not identify |

12. **Create the register of open decisions, with a searchable tag.** Every decision the researcher still has to make, marked in the code with one distinctive string such as `DECIDE:` so a single search lists them. Clustering level, fixed effects set, sample restrictions, functional form, treatment definition. The judgement call is whether to pick a default, and the rule is to pick a defensible default so the pipeline runs end to end, and to tag it, because a pipeline that runs with a flagged provisional choice is more useful than one that stops.

13. **Write the README to be read by a stranger.** How to run it, what to edit first, what each stage does in one line, the package versions, the expected runtime, and the exhibit map. Test it by giving it to somebody who has not seen the project.

14. **Give exploratory work a sandbox and a promotion rule.** A `scratch/` directory that nothing in the pipeline reads from, and one rule: a result leaves the sandbox only by being rewritten into a numbered stage. Without this, exploratory code becomes a dependency by accident, and the pipeline stops being the source of the paper's numbers.

15. **Run the empty scaffold end to end before handing it over.** It should complete on whatever data exists, even if several stages do nothing but load and save. A scaffold that has never run is a proposal.

## Choosing the size of the scaffold

The full structure is not always right, and applying it to a small piece of work wastes days. Three sizes, and a rule for choosing:

**Minimal, three files.** One source, one cleaning step, fewer than about four exhibits, one person, no reuse expected. A master, a build file and an analysis file. Everything else in the standard still applies, particularly the read-only raw directory, the logging and the counted drops.

**Standard, the numbered ten.** More than one source, or more than one person, or any stage taking more than about two minutes, or outputs that will appear in a document somebody else reads. This is the default for a paper or a thesis chapter.

**Shared pipeline.** More than one output document drawing on the same cleaned data. A shared build pipeline writing one or more analysis files, plus one analysis folder per document.

The rule for moving up a size: convert when the second source arrives, when the second person arrives, or when the first exhibit goes into a document, whichever happens first. Converting early is cheap; converting late is a rebuild.

## Worked example

**Situation.** A researcher was beginning a thesis chapter on whether a mandatory water metering programme changed household consumption, using an unbalanced panel of 612 municipal water utilities observed from 2008 to 2022, with staggered adoption of the mandate across states. Three sources: an annual utility operations file from a national regulator, a municipal population and income file from a statistics agency, and a hand-collected table of adoption dates compiled from state legislation. A second chapter, on utility cost structures, would use the same operations file. A research assistant would join in two months.

**Task.** A project layout that would still be intelligible when the second chapter started and when the assistant arrived, set up in under a day, with the pipeline running end to end on the data available even though the identification strategy was not settled.

**Action.** The eight questions took twenty minutes and produced one immediate finding: the adoption dates were hand-collected, which meant they were a raw source with provenance that had to be recorded and a source file that had to be treated as read-only exactly like the regulator's extract, a point the researcher had not considered because the file was theirs.

The wrong turn was the layout. The first version created a folder per chapter, each with its own complete numbered pipeline, on the reasoning that the chapters would diverge and that keeping them separate would prevent one breaking the other. It survived eleven days. What killed it was the operations file: the metering chapter dropped utilities serving fewer than 5,000 connections as unrepresentative, and the cost chapter kept them, which was a legitimate difference. But the exclusion had been written into each chapter's cleaning stage, along with everything else, and when a data correction arrived from the regulator for the 2014 file, it was applied in one chapter and not the other. The two chapters then reported utility counts of 574 and 589 for what was described in both as the same population, and reconciling them took most of a day.

The layout was rebuilt as a shared pipeline. Stages 01 to 05 became a single build producing one analysis file at utility-year level with no substantive restrictions beyond structural ones, and each chapter got its own analysis folder whose first stage applied that chapter's restrictions from the shared file, with counts logged. The connection-size restriction moved into the metering chapter's own sample stage where it belonged, and became visible as a chapter-specific decision rather than being buried in shared cleaning. The rebuild took a day and a half. The rule that came out of it, written into the README: shared cleaning contains only decisions both chapters would make identically, and anything either chapter would do differently belongs in that chapter.

The stage contract was written before the stages. Two prohibitions earned their place immediately. `04_construct.do` must not drop observations, which caught an attempt to remove utilities with missing consumption while constructing the log outcome, a drop that would then have been invisible in the sample construction table. And `08_main_results.do` must not modify the data, which caught a convenient recode of the treatment variable written inside the estimation stage where no count would have recorded it.

Because adoption was staggered, stage 07 was stubbed from the design table with a cohort and timing table, an event study with the reference period tagged as a `DECIDE:` item, and a heterogeneity-robust estimator alongside the two-way fixed effects version. The register held nine open decisions on day one, of which the clustering level and the event-study reference period were the two that mattered.

Package versions were pinned into a project-local directory, which mattered three months later when a package update changed a default and the pinned copy meant nothing moved.

**Result.** The scaffold ran end to end in eleven minutes on the first day, producing an empty descriptives table and a placeholder figure, which was the point: the pipeline existed before the analysis did. The research assistant was given the README and the stage contract and produced a usable descriptives stage in their first week with two questions asked, both about the data rather than about where anything lived.

At submission, the exhibit map made the data editor's request straightforward: every table named the stage that produced it, and the full run from raw files took nineteen minutes. Setting up the scaffold cost about six hours, and the chapter-folder wrong turn cost eleven days of mild inconvenience plus the day and a half to rebuild.

### A second scenario, where it goes differently

The same researcher was asked to check a published paper's result for a reading group, working from the authors' deposited data and code, with about two days available.

The standard scaffold is wrong here for a reason worth naming: the code already exists, and imposing a new structure on it destroys the correspondence between the deposited code and the published tables, which is the only thing making the check meaningful. Restructuring somebody else's replication code is a way of introducing your own errors and calling them theirs.

What was used instead was a wrapper. The deposited archive sat untouched in `data/raw/original_archive/`, treated exactly as a raw file. A three-file scaffold sat beside it: a master, a file that ran the original code unmodified and captured its log, and a file holding the researcher's own checks, which read the outputs the original code produced and compared them with the published table. Nothing in the researcher's code wrote into the original archive.

The rules that survived: the read-only raw directory, one entry point, a timestamped log, a stated Stata version, counted drops in the researcher's own code, and outputs named by the stage that made them. The rules that were suspended: the numbered ten stages, the stage contract, and the shared pipeline question, none of which apply to two days of work on somebody else's pipeline.

What changed the decision was ownership and horizon. The scaffold's value comes from decisions being made once and held for a long time by several people. With one person, two days, and no authority over the code, that value is not there, and the parts worth keeping are only the ones that make the work reproducible for the person who did it.

## Output

**The folder tree**, generated with real names:

```
water-metering/
  data/
    raw/                 read-only; source files as received, plus provenance notes
      regulator/
      statistics-agency/
      adoption-dates/
    interim/             one file per build stage, regenerable
    clean/               analysis-ready files
  code/
    00_master.do         sets root, options, log, seed; calls stages; closes log
    01_setup.do          version, globals, package checks into code/ado, graph scheme
    02_import.do         raw to interim, original variable names, row-count asserts
    03_clean.do          cleaning decisions, one per commented block, counts logged
    04_construct.do      analysis variables, each labelled with its formula
    05_sample.do         structural restrictions, counts before and after each
    _globals.do          variable lists, control blocks, labels used in more than one stage
    _graphprefs.do       the house graph scheme, applied once
    ado/                 project-local user-written packages
    ch1-metering/
      06_sample_ch1.do   chapter restrictions from the shared file, counts logged
      07_descriptives.do
      08_identification.do
      09_main_results.do
      10_robustness.do
      11_figures.do
    ch2-costs/
      ...
  output/
    tables/
    figures/
    logs/
  docs/
    README.md
    stage_contract.md
    codebook.md
    cleaning_log.md
    open_decisions.md
    raw_provenance.md
  scratch/               exploratory work; nothing in code/ reads from here
```

**The stage contract**, the document that does the real work:

| Stage | Owns these decisions | Reads | Writes | Must not |
| 02_import | Encoding, types on import, row-count expectations | data/raw | data/interim/*_raw.dta | Recode, rename, or drop anything |
| 03_clean | Missing codes, impossible values, duplicates, harmonisation across years | data/interim/*_raw.dta | data/interim/*_clean.dta | Construct analysis variables |
| 04_construct | Variable definitions, treatment indicators, event time, transformations | data/interim/*_clean.dta | data/interim/built.dta | Drop observations |
| 05_sample | Structural restrictions shared by all chapters, with counts | data/interim/built.dta | data/clean/panel.dta | Apply chapter-specific restrictions |
| 06_sample_ch1 | This chapter's restrictions, with counts | data/clean/panel.dta | data/clean/ch1_analysis.dta | Redefine any variable |
| 08_identification | Which diagnostics the design requires | data/clean/ch1_analysis.dta | output/tables, output/figures | Modify the data |
| 09_main_results | Specification build-up, stored estimates | data/clean/ch1_analysis.dta | output/tables/t09_main.tex | Modify the data or define variables |

**The master do-file skeleton**, whose detailed contents standard is `stata-do-file-craft`:

```stata
* 00_master.do : entry point. Nothing else is run directly.
version 17
clear all

* the only machine-specific line in the project
if "`c(username)'" == "aferreira" global root "/Users/aferreira/projects/water-metering"
else if "`c(username)'" == "tanaka" global root "D:/research/water-metering"
else {
    display as error "Unknown user. Add your root path in 00_master.do."
    exit 198
}

global data "$root/data"
global code "$root/code"
global out  "$root/output"
sysdir set PLUS "$code/ado"

local full_run 1        // 1 clears output/ before running; 0 for single-stage reruns
local do_setup      1
local do_import     1
local do_clean      1
local do_construct  1
local do_sample     1
local do_ch1        1

log using "$out/logs/master_`c(current_date)'.log", replace text
set seed 20260906

if `full_run' {
    * remove stale outputs so a missing table is visible, not silently satisfied
}

if `do_setup'     do "$code/01_setup.do"
if `do_import'    do "$code/02_import.do"
* ... remaining stages in order ...

log close
```

**The open decisions register:**

| Tag | Stage | Decision | Provisional choice in code | Who decides | By when |
| DECIDE:01 | 09_main_results | Clustering level: utility or state | State, 27 clusters | Supervisor | Before first draft |
| DECIDE:02 | 08_identification | Event-study reference period | Period minus one | Researcher | Before descriptives |
| DECIDE:03 | 06_sample_ch1 | Minimum connections threshold | 5,000 | Researcher | Before main results |

**The exhibit map**, in the README, so paper numbering can change without renaming files:

| Paper exhibit | File | Produced by |
| Table 1 | output/tables/t07_summary.tex | ch1-metering/07_descriptives.do |
| Table 2 | output/tables/t09_main.tex | ch1-metering/09_main_results.do |
| Figure 2 | output/figures/f08_eventstudy.pdf | ch1-metering/08_identification.do |

**The README**, containing: what the project is in two sentences, how to run it, the one line to edit, the stage list with one line each, the package list with versions, the expected runtime, the exhibit map, and where the open decisions live.

## Failure modes

**A folder per chapter, each with its own cleaning.** Recognise it by the same source file being imported in two places. Fix by moving to a shared pipeline, with chapter-specific restrictions in chapter stages, before the second chapter has produced a number.

**Stages that depend on what is in memory.** Recognise it when running stage 08 alone fails. Fix by making every stage load from disk and save to disk, which is what makes the master's toggles mean anything.

**A master that does data work.** Recognise it when the master contains a generate or a merge. Fix by moving it into the stage that owns that decision, because computation in the master is invisible state.

**Version suffixes in output file names.** Recognise it by any file ending in a number or the word final. Fix by deleting them, letting the pipeline regenerate outputs, and keeping versions in the log timestamp or in version control.

**Two stages that both drop observations.** Recognise it by comparing the sample construction counts with the number of drop statements in the code. Fix with the stage contract's prohibition column, and by moving every drop into the sample stage.

**A control list copied into two stages.** Recognise it when two tables that should have identical controls do not. Fix by moving the list to `_globals.do` and referring to it everywhere.

**Packages installed by an unconditional install command.** Recognise it by an `ssc install` with no check around it. Fix by checking first and installing into the project-local directory, so a run does not update a package and move a coefficient.

**The scratch folder becoming a dependency.** Recognise it when a numbered stage reads a file from `scratch/`. Fix by promoting that code into a numbered stage, which is the only route out of the sandbox.

**A scaffold that has never been run.** Recognise it by an empty log directory. Fix by running it end to end before it is used, even when most stages do nothing.

**Scaffolding a two-day job.** Recognise it when the setup takes longer than the analysis would have. Fix by using the minimal three-file version and keeping only the logging, the read-only raw rule and the counted drops.

## Edge cases

**Data that cannot leave a secure environment.** The tree exists in two halves: the code and documentation outside, the data and outputs inside. Keep the same stage numbering in both, and have the README state exactly which stages run inside and what may be exported. Plan for the outputs directory inside the environment to be the only place results exist until they are cleared for release.

**A project inheriting a supervisor's fixed structure.** Do not rename anything in a shared or institutional layout. Apply the scaffold as an overlay: add a master that calls the existing files in their existing order, add the stage contract as a document describing what each existing file actually does, and add logging. That gets most of the value without breaking anybody else's paths.

**Very large data where intermediate files are expensive.** Keep the stage boundaries but reduce what is saved: write a compressed extract with only the variables needed downstream rather than the full interim file, and note in the contract which stage must be rerun if an earlier one changes.

**Mixed language projects, where some stages are in Python or R.** Keep one master in one language that calls the others as external processes, so there is still exactly one entry point, and record every language's version and package set. `python-for-econometrics` covers the environment pinning for the Python side.

**A team using version control.** The scaffold and version control are complementary, not alternatives: the tree tells you where a decision lives, the repository tells you when it changed. Add the raw data directory and the outputs directory to the ignore file, since outputs are regenerable and raw data usually cannot be committed, and commit the README, the contract and the register.

**Taking over an abandoned project mid-flight.** Do not restructure first. Run what exists, capture a log, write the stage contract as a description of what the existing files actually do, and only then move decisions into single homes, one at a time, checking that a stored result does not change at each move.

**A one-off analysis that turns out not to be one-off.** This is the common case and it is why the promotion rule matters. When a scratch analysis is asked for a second time, that is the signal to promote it into a numbered stage rather than to run it again from the sandbox.

## Quality bar

- A single command runs the project from raw files to every exhibit, with no manual step and no file opened by hand.
- The stage contract exists, and every stage's header states what it owns, reads, writes and must not do.
- Each decision, in particular each sample restriction and each variable definition, appears in exactly one stage.
- Every exported table and figure carries the stage that produced it in its name, and the README maps paper exhibits to files.
- The raw directory is read-only in the file system, and no code writes into it.
- Every stage loads from disk and saves to disk, so any stage can be rerun alone.
- Packages are installed into a project-local directory with their versions recorded.
- The open decisions register lists every provisional choice, each findable by one search of the code.
- A stranger can read the README and reproduce the results without asking a question.

## Related skills

`stata-do-file-craft` governs how the code inside each stage is written, including the master's contents, the logging and the assertion discipline. `stata-data-management` governs the data operations that stages 02 to 05 perform. `data-profiling-and-cleaning` decides, before any of this, what has to be checked and recorded about the incoming data, and its cleaning log is what stage 03 writes. `research-design` supplies the design that determines the diagnostics stage, and `econometrician` supplies the estimator and clustering decisions that the register is holding open. `regression-table-production` and `descriptive-statistics-tables` govern what the analysis stages export, `academic-tables-booktabs` how those tables look, and `academic-figures-monochrome` the figures stage. `python-for-econometrics` is the equivalent layout and environment discipline for a Python project. `analysis-audit` checks from outside that the paper's numbers came from this pipeline, and `replication-package` assembles it for deposit.
