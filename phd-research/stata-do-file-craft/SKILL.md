---
name: stata-do-file-craft
description: Writes Stata do-files that a stranger can run end to end from raw data on a different machine and get the same numbers. Enforces a master do-file calling numbered scripts, one machine-specific line and relative paths everywhere else, a version statement, timestamped logging of every run, locals inside files and globals only for paths, loops over specifications instead of copy-paste, defensive assert and isid checks, capture used only where it cannot hide an error, seeds for anything random, and an absolute ban on editing data interactively. Use this skill when someone asks for help writing or fixing a do-file, says their code will not run on a coauthor's machine, cannot reproduce a number they produced last month, has a single enormous script that has become unmanageable, is preparing code for a journal data editor, or asks how to make a Stata project reproducible. Trigger also on vaguer requests such as "clean up my Stata code", "why did my results change", or "how do I organise this".
---

# Stata Do-File Craft

The failure this prevents is a piece of code that runs only once, only on one machine, and only in the presence of the person who wrote it. It usually looks fine. It opens, it runs, it makes a table. What it hides is that the working directory was set by hand three hours ago, that a variable was recoded in the Data Editor and never written down, that a `capture` silently swallowed a merge error in 2023, and that the file must be run in an order nobody has recorded because parts of it depend on things earlier parts left in memory.

The cost arrives late and always at the worst moment. A referee asks for the same specification with standard errors clustered one level up, the code is rerun, and a coefficient moves in the third decimal place with no explanation. A journal data editor runs the package on a clean machine and it stops at line 40 on a path that does not exist. In the worst version the numbers in the published paper cannot be regenerated at all, and the author has no way to demonstrate that they were ever right.

The discipline is small and mechanical: a run starts from a clean session, touches nothing by hand, writes a log, and ends with output on disk carrying the date it was made.

## When to use this, and when not to

Use it when writing any do-file that will be run more than once, when inheriting code from a coauthor or a predecessor, when a project has grown into a single long script, when preparing code for submission or deposit, when a result has changed and nobody knows why, and when a colleague reports that the code does not run for them. Use it especially at the moment the project stops being exploratory, which is usually the first time a number from the code appears in a document someone else will read.

Do not use it to lay out a new project from nothing; `stata-project-scaffold` produces the folder tree and the numbered file stubs, and this skill is what goes inside them. Do not use it for the data work itself: import, merge, reshape, labels, panel structure and missing value handling belong to `stata-data-management`. Do not use it to decide which estimator to run, which is `econometrician`, or to build the final table, which is `regression-table-production`. Do not use it as the submission checklist for a replication archive; that is `replication-package`, which assumes the code already meets this standard.

## What you need before starting

**The project root and its folder structure.** Everything else is written relative to it. Missing: impose the minimum structure yourself, which is `data/raw`, `data/clean`, `code`, `output/tables`, `output/figures`, `output/logs`, and say you have done so.

**The Stata version the work will be run under, and the version any coauthor has.** A `version` statement pins behaviour that has genuinely changed between releases: defaults have moved, small-sample adjustments in some variance estimators have changed, and some commands have been reimplemented. Without the line, a rerun under a newer Stata can return a different number with no error and no warning, which is the hardest kind of discrepancy to trace. With it, the code declares which release's behaviour it was written against, so the difference surfaces as a version mismatch rather than as an unexplained third decimal. The lowest version in the team is the one that constrains the code. This library pins `version 18` throughout, here and in `stata-project-scaffold`, so a reader is not handed two numbers to reconcile; change it to the oldest release actually in use on your project, in the master file and in every script header at the same time. Missing: write `version` for the oldest release you know is in use, and note the assumption at the top of the master file.

**The list of user-written commands the project depends on, with versions.** These are the most common reason code runs for one person and not another. Missing: search the code for commands that are not official Stata, list them, and install them into a project-local ado directory rather than the user's own.

**The raw data files and confirmation that they are the raw files.** A file called `data_clean_v3.dta` sitting in `raw` is not raw data and the pipeline built on it is not reproducible. Missing: ask what produced it, and if the answer is unknown, mark the project as reproducible only from that point forward and say so in writing.

**Whether anything in the analysis is random.** Bootstraps, permutation tests, simulation, random sampling, random assignment for a pilot, machine learning splits, and some estimators with numerical optimisation from random starts. Missing: assume yes and set a seed anyway; a seed on deterministic code costs nothing.

**Who will run this, and on what.** A coauthor on a laptop, a data editor on a clean machine, a secure enclave with no internet, or a cluster. Missing: assume a stranger on a clean machine with no internet, which is the strictest case and the one journals actually apply.

## The method

1. **Make the master do-file the only entry point.** One file, `00_master.do`, that sets the environment once and then calls the numbered scripts in order. Nothing else is ever run directly in normal operation. The judgement call is how much the master does itself: the rule is that the master sets paths, options, logging and the seed, and contains no data work at all, because anything it computes becomes invisible state that the individual scripts silently depend on.

2. **Reduce machine-specific information to exactly one line.** One global holding the project root, set once, with everything else derived from it. Below that line, every path in the project is relative. The test is that moving the project folder to another disk requires editing one line. Where several people run the same code, use a short conditional on the username rather than commented-out alternatives, because a commented-out path is a path somebody will eventually uncomment by mistake.

```stata
version 18
clear all
set more off
set varabbrev off
set linesize 120

* ---- the only machine-specific line in the project ----
if "`c(username)'" == "moliveira"  global root "/Users/moliveira/projects/wage-panel"
else if "`c(username)'" == "khan"  global root "C:/research/wage-panel"
else {
    display as error "Unknown user. Set global root in 00_master.do."
    exit 198
}

global data "$root/data"
global code "$root/code"
global out  "$root/output"

* project-local packages, so versions travel with the project
sysdir set PLUS "$root/code/ado"
```

3. **Number the scripts by stage and keep each one runnable in isolation given its inputs.** A script loads what it needs from disk at the top and saves what it produces at the bottom, and never relies on what happened to be in memory. The judgement call is where to cut the boundaries: cut where a stage produces a saved dataset the next stage reads, and split any file that passes roughly three hundred lines or that mixes a slow stage with a fast one, because a slow stage bundled with a fast one gets skipped and then gets skipped in the wrong place.

4. **Log every run with a timestamp and never overwrite the log.** The log is the only durable evidence of what the code actually did on a given day, and a log written with `replace` to a fixed name destroys that evidence the moment something goes wrong. Use `text` rather than SMCL so the file is readable and diffable outside Stata.

```stata
local stamp = string(date(c(current_date), "DMY"), "%tdCCYYNNDD") ///
            + "_" + subinstr(c(current_time), ":", "", .)
capture mkdir "$out/logs"
log using "$out/logs/run_`stamp'.log", text
display "Run started `c(current_date)' `c(current_time)' by `c(username)' on Stata `c(stata_version)'"
```

5. **Use locals for everything inside a file and globals only for paths.** A local dies when the do-file ends, which is exactly the behaviour you want: it cannot leak into the next script and cannot survive to be reused stale. A global persists across the whole session, which is why a global holding a variable list is a trap. The point that surprises people is that a local set in `00_master.do` is not visible inside a script the master calls with `do`, because `do` opens a new local scope. That is a feature. Where a script genuinely needs a parameter from the master, pass it as an argument or use a global named so distinctively that nobody will reuse it by accident.

```stata
* inside 08_main_results.do
local baseline   "age agesq i.educ"
local plusfirm   "`baseline' i.industry log_emp"
local plusregion "`plusfirm' i.region_type unemp_rate"
```

6. **Loop over specifications rather than copying blocks.** Copy-paste is how a control set ends up different in column 3 than in column 4 with nobody noticing. The rule: if two estimation commands differ only in a list, a sample condition or an outcome, they belong in a loop. If they differ structurally, keep them separate and make the difference visible.

```stata
local specs "baseline plusfirm plusregion"
local k = 0
foreach s of local specs {
    local ++k
    eststo m`k': reghdfe lwage female ``s'' , ///
        absorb(firm_id year) vce(cluster state)
    estadd local fe_firm "Yes"
    estadd local fe_year "Yes"
}
```

7. **Write a program when the same block appears three times or when a block must return numbers.** An `rclass` program returns scalars, macros and matrices through `return`, which is how a computed quantity reaches a table without being retyped. Below three uses a program is usually not worth the indirection it adds.

```stata
capture program drop gapstat
program define gapstat, rclass
    syntax varname [if], Treat(varname) [Cluster(varname)]
    marksample touse
    local vceopt = cond("`cluster'" != "", "vce(cluster `cluster')", "robust")
    quietly regress `varlist' `treat' if `touse', `vceopt'
    return scalar b  = _b[`treat']
    return scalar se = _se[`treat']
    return scalar n  = e(N)
    return local  vce "`vceopt'"
end

gapstat lwage, treat(female) cluster(state)
display "Gap = " %6.3f r(b) "  (" %6.3f r(se) "), N = " r(n)
```

8. **Assert what must be true, at the point it must be true.** Every merge, every collapse, every reshape and every sample restriction changes something you believe about the data, and an `assert` turns that belief into a line that fails loudly when it stops holding. The rule for choosing checks: assert the key uniqueness after anything that could duplicate rows, assert the range of any constructed share or rate, and assert the row count after any operation whose purpose was to preserve it.

```stata
isid firm_id year
assert inrange(female, 0, 1)
count if missing(lwage) & insample == 1
assert r(N) == 0
```

9. **Use `capture` only where a failure is genuinely acceptable, and pair it with a check.** `capture` suppresses the error and sets `_rc`. That is correct for `capture drop x`, `capture mkdir`, and `capture program drop`. It is dangerous around anything that does real work, because a captured merge, regression or save that fails leaves the code running on the wrong data with no visible sign. The rule: if you cannot say in one sentence what should happen when the captured command fails, do not capture it.

```stata
* acceptable
capture drop lwage
capture mkdir "$out/tables"

* correct pattern when a failure must be handled
capture confirm file "$data/clean/panel.dta"
if _rc {
    display as error "panel.dta missing. Run 03_clean.do first."
    exit 601
}

* wrong: hides a broken merge and continues on unmerged data
capture merge 1:1 firm_id year using "$data/clean/accounts.dta"
```

Where a long run should continue past a failure in one branch so the rest still produces output, use `capture noisily`, which prints the error and records it in the log while allowing the master to continue, and then check `_rc` and report at the end.

10. **Set a seed for anything random, and set it in one place.** Put `set seed` in the master so every run of the pipeline starts from the same state, and set a distinct seed again immediately before any bootstrap or simulation so that reordering the scripts does not change the draws. Record the seed in the log. Use the estimator's own seed option where it has one, because it is the seed the estimator actually uses.

```stata
set seed 20260906
bootstrap, reps(999) seed(31415) cluster(state): regress lwage female age
```

Sort order is the hidden source of non-determinism. Where ties exist, `sort x` does not produce a unique ordering, so any command whose result depends on row order can move between runs and between Stata versions. Use `sort x, stable`, sort on a full key that is unique, or `set sortseed` and record it. `duplicates drop` and `by ... : keep if _n == 1` are the two places this bites most often.

11. **Never touch the data interactively.** No `edit`. No typing a command in the Command window that changes anything in memory. `browse` is acceptable because it cannot change anything; `edit` is not, and the cheapest protection is a team rule that the Data Editor is opened in browse mode only. If you find yourself typing a fix in the console, write it into the do-file and rerun the file. The whole reproducibility argument collapses at the first undocumented interactive change, and the person who made it is never the person who discovers it.

12. **Test from a clean session before you believe any of it.** Close Stata entirely, reopen it, and run `do "00_master.do"` and nothing else. Running a file inside a session that already holds the right data in memory proves nothing.

## Making a run reproducible from a clean session

A run is reproducible when all six hold, and the check takes ten minutes: a fresh Stata instance running only `00_master.do` completes without error; every file in `output/` is newer than the start of that run, so nothing on disk is a leftover from an earlier version of the code; the log records the Stata version, date, username, seed and package versions; no path outside the single root line is absolute; no script depends on anything left in memory by another; and a second run produces identical tables apart from timestamps. The strong version, which is the one journals apply, copies the project to a different machine, edits the single root line, and runs it there.

The second condition is the one people skip and the one that catches the most errors. Enforce it by deleting the contents of `output/tables` and `output/figures` at the start of the master run, so a missing table is visible immediately rather than being silently satisfied by last week's file.

## Worked example

**Situation.** A three-person team had a firm-level panel of 1,240 manufacturing firms observed from 2009 to 2019, and one do-file of 2,900 lines named `analysis_final_v7.do`. A referee at a field journal asked for the main table with standard errors clustered at state rather than firm level, a change of one option. The lead author reran the file and the coefficient in the main column moved from 0.062 to 0.058, which was not the change clustering should have produced, and the sample size fell by 46 observations. Nobody could explain either.

**Task.** Rebuild the project so the referee's request could be answered honestly, within five working days, without changing any result that was correct. Good meant a pipeline that ran from raw data on the second author's laptop, reproduced the published table exactly, and explained the 46 observations.

**Action.** The first attempt left the single file intact, wrapped it in a master, added logging, and marked sections with comment banners. It was abandoned after a day and a half, because the team went on running fragments of it by highlighting and executing selections, which is what a single long file invites, and a fragment run inherits whatever is in memory. The structural problem was not the missing master file; it was that the file was not divisible into stages that could each be run from disk.

The rebuild split the file at every point where a dataset could reasonably be saved, producing eleven scripts, each beginning with a `use` and ending with a `save`, run in order by the master into a timestamped log.

Three things came out of the split. First, a sample filter dropping firms with fewer than five employees appeared twice, at line 610 and again at line 1,880, with the second occurrence written against a variable that had been reconstructed in between; the second application removed nothing in most runs, which is why it had survived. Second, a `capture merge m:1 state year using "unemployment.dta"` at line 1,455 had been failing since a variable rename eight months earlier, so the state unemployment control had been missing for the whole period and the regression had been silently dropping it from the control list. Third, and this was the 46 observations, a `duplicates drop firm_id year, force` ran after a plain `sort firm_id year`, and where a firm-year appeared twice with different reported employment, which row survived depended on an ordering that was not unique.

The wrong turn cost about a day and was worth recording for a second reason: the instinct to preserve the existing file came from a fear that splitting it would change results. Splitting it did change results, and that was the point. The changes were errors being exposed, not introduced.

The fixes were mechanical. Duplicate resolution became an explicit rule in `03_clean.do`, keeping the record with the non-missing employment figure and flagging for the data provider the four cases where both were non-missing and different. The merge lost its `capture` and gained an `assert`. The duplicated filter was removed from the later position and an `isid` check placed after it.

**Result.** The master ran in 22 minutes from raw files to eleven tables and six figures. The published coefficient was 0.062 and stayed 0.062 under both clustering levels, as it must, since the level of clustering changes the variance estimate and not the point estimate. What moved was the standard error: 0.018 clustered on firm and 0.027 clustered on state across 38 clusters. That was reported in the response as a change in inference rather than in the estimate, with a note that 38 clusters sits below the roughly forty at which a conventional cluster-robust standard error stops being safe to quote on its own, so a wild cluster bootstrap p-value was given alongside it. The 46 observations were explained in two sentences. The rebuild took four and a half days against an estimate of two.

### A second scenario, where it goes differently

A first-year doctoral student had a single cross-section of 3,400 survey responses, one merge, and about 400 lines of code producing three tables for a term paper. The same rebuild would have wasted two days.

What changed was the size and the number of stages. With one data source and one output stage, the eleven-file structure costs more than it returns, because the overhead of saving and reloading intermediate files exceeds the benefit of running stages independently. The minimum viable version applied instead: one file, but with `version`, `clear all`, the single root global, a timestamped log, a seed, every path relative, `isid` after the merge, no interactive edits, and a clean-session test. That is seven lines of discipline on top of code the student had already written, and it delivers most of the protection.

The rule for choosing between them: split into numbered scripts when there is more than one input dataset, when any stage takes more than about two minutes, or when more than one person will run the code. Otherwise keep one file and keep the discipline.

## Output

The deliverable is a code directory whose entry point is unambiguous, plus a log that proves the run happened.

```
code/
  00_master.do        sets root, options, log, seed; calls 01 to 10; closes log
  01_setup.do         installs and version-pins user-written commands into code/ado
  02_import.do        raw files to data/interim, no cleaning decisions
  03_clean.do         cleaning decisions, one per commented block
  04_construct.do     constructed variables, each with its definition in a comment
  05_sample.do        sample restrictions, each with a count before and after
  06_descriptives.do  output/tables/tab01_summary.tex
  07_checks.do        balance, panel structure, identification diagnostics
  08_main_results.do  output/tables/tab03_main.tex
  09_robustness.do    output/tables/tab04_robust.tex
  10_figures.do       output/figures/*.pdf
  _globals.do         variable lists and labels used in more than one script
  _graphprefs.do      the house graph scheme, applied once
  ado/                project-local user-written packages
```

Header block at the top of every script, so a reader knows the contract without reading the body:

```stata
*==============================================================
* 08_main_results.do
* Purpose : main wage gap estimates, three specifications
* Inputs  : data/clean/panel.dta
* Outputs : output/tables/tab03_main.tex, estimates in e(), memory unchanged
* Author  : M. Oliveira      Last revised: 2026-09-06
* Requires: reghdfe 6.0.3, estout 3.31
*==============================================================
version 18
```

The run record that accompanies a delivered result:

| Field | Value |
| Script run | `00_master.do` |
| Date and time | 2026-09-06 14:32 |
| Stata version and flavour | 18.5 MP, macOS |
| Seed | 20260906 |
| User-written packages | reghdfe 6.0.3, estout 3.31, ftools 2.49.1 |
| Runtime | 22 minutes |
| Outputs written | 11 tables, 6 figures, listed in the log |
| Warnings or non-zero return codes | none |

## Failure modes

**Absolute paths scattered through the code.** Recognise it with a search for the drive letter or the leading slash across the code directory. Every hit outside the one root line is a defect. Fix by deriving all paths from the root global.

**`capture` around real work.** Recognise it by searching for `capture` and reading what follows; anything that merges, estimates, saves or generates is suspect. Fix by removing the capture, or by pairing it with an explicit `_rc` check that stops the run.

**Globals holding variable lists.** Recognise it when a script produces different results depending on what was run before it in the same session. Fix by demoting them to locals inside the script that uses them.

**Results that depend on sort order.** Recognise it by running the pipeline twice in fresh sessions and diffing the tables, and by the presence of `duplicates drop`, `keep if _n == 1`, or `by` groups without a unique sort key. Fix with a stable sort on a genuinely unique key and an explicit tie-break rule.

**The interactive fix that never made it into the file.** Recognise it when the code produces something different from the saved output and nobody can say what changed. There is no fix after the fact beyond rebuilding; the prevention is the ban on `edit` and the clean-session test.

**Copy-pasted specification blocks.** Recognise it when column 4's control list differs from column 3's by something the paper does not mention. Fix with a loop over named control macros.

**User-written commands installed into the user's own ado directory.** Recognise it when the code runs for the author and fails on a clean machine with an unrecognised command. Fix by installing into a project-local directory that ships with the code.

## Edge cases

**A secure enclave or a data room with no internet and no write access outside a working folder.** Package the user-written commands with the code and install from the local copy in `01_setup.do`. Write logs and outputs to the permitted folder. Expect that you cannot take the data out, so the code must produce every number you will need, including the ones you would normally check by eye.

**A run that takes eight hours.** Split the expensive stage into its own script that saves its result, and have downstream scripts read that saved file. Keep one switch in the master that skips the expensive stage, and make its default the slow, correct setting, so a full run is what happens by accident.

**Code inherited from someone unavailable.** Do not refactor first. Run it as found, keep the log, and save its outputs as a reference set. Only then restructure, checking each stage against the reference. Where the reference cannot be reproduced at all, say so in writing before rebuilding begins, because that fact is itself a finding.

**Confidential data that cannot be shipped.** The code still meets this standard: the pipeline starts from a synthetic or public extract with the same structure, so the scripts can be run and checked, and the real run happens where the data lives. Document which is which.

**A coauthor who works interactively and will not stop.** Give them a sandbox script, `99_scratch.do`, excluded from the master and forbidden from writing to `data/clean` or `output`. Exploration is legitimate; the rule is that nothing from the sandbox reaches a table without being written into a numbered script first.

## Quality bar

- A fresh Stata session running only `00_master.do` completes with no error and rewrites every output file.
- Exactly one line in the project contains a machine-specific path.
- Every run writes a timestamped log containing the Stata version, the seed, the package versions and the runtime, and old logs are kept.
- No `capture` appears in front of a command that merges, estimates, generates or saves without a following `_rc` check.
- Every merge, reshape, collapse and sample restriction is followed by an `assert` or `isid` that states what should now be true.
- Any command that draws random numbers is preceded by an explicit seed, and any command sensitive to row order sorts on a unique key.
- Specifications that differ only by a control list, sample or outcome are generated by a loop, not by copied blocks.
- No data change anywhere in the project was made outside a do-file.

## Adapting this to your context

Two layers again. The method: one entry point, one machine-specific line, scripts that load from disk rather than from memory, a timestamped log kept rather than overwritten, an assertion after anything that changes the data, a seed for anything random, and a clean-session test. The commands are Stata dialect.

- **The entry point.** `00_master.do` becomes a `run_all.R` calling `source()` with `here::here()` for the root, a `main.py` or a Makefile, one SAS driver using `%include`, or an SPSS syntax file using `INSERT FILE`. One machine-specific line either way.
- **Pinning behaviour.** `version 18` is a Stata mechanism with no exact counterpart. Use `renv` in R, a lockfile or pinned `requirements.txt` in Python, and where the language offers nothing, record the release and every package version in the log.
- **Logs and seeds.** `log using` becomes `sink()` or `logr`, Python's `logging`, `PROC PRINTTO` in SAS, OMS in SPSS. `set seed` becomes `set.seed()`, `numpy.random.default_rng(seed)`, or `streaminit()`.
- **The ban on interactive edits.** `edit` is Stata's word for it. The rule is that no data change happens outside a script, which rules out SPSS Data View, a spreadsheet opened to fix one cell, and a console command typed once.
- **What not to change.** The clean-session test from raw data, and nothing changed by hand anywhere. Those are the method; the command names are not.

## Related skills

`stata-project-scaffold` creates the folder tree and the empty numbered files that this skill fills in. `stata-data-management` covers what the import, cleaning and construction scripts actually do to the data. `econometrician` decides what the estimation scripts should estimate, and `regression-table-production` turns their stored estimates into tables. `python-for-econometrics` applies the same discipline in a different language and says when that is the better choice. `analysis-audit` is what someone else runs against this code to check that the numbers in the paper came from it. `replication-package` is the final assembly step for deposit, and it assumes this standard has already been met.
