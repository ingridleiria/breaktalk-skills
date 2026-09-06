---
name: stata-project-scaffold
description: Generates a complete, runnable Stata project skeleton for a new empirical paper: folder structure, a master do-file, and numbered do-files from setup through cleaning, variable construction, descriptives, identification checks, and first regressions, with logging, versioning, and reproducibility built in. Use this skill whenever a researcher starts a new Stata project, asks for a do-file structure, wants "the base do-files for this project", needs a master do-file, asks how to organize a Stata pipeline, or describes a dataset and a design and is about to start coding. Trigger at the start of any Stata-based empirical project and when an existing project has become a single 3,000-line do-file.
---

# Stata Project Scaffold

A reproducible empirical project can be rerun from raw data to final tables by one command, by someone who is not its author, a year later. This skill produces the skeleton that makes that true from day one, so that reproducibility is not a cleanup task before submission.

## Folder structure

```
project-name/
  data/
    raw/          untouched source files, read-only
    interim/      intermediate files produced by cleaning
    clean/        analysis-ready .dta files
  code/
    00_master.do
    01_setup.do
    02_import.do
    03_clean.do
    04_construct.do
    05_sample.do
    06_descriptives.do
    07_identification.do
    08_main_results.do
    09_robustness.do
    10_figures.do
    _globals.do
    _graphprefs.do
  output/
    tables/
    figures/
    logs/
  docs/
    codebook.md
    cleaning_log.md
    README.md
```

Ask for the project name, the data sources, the unit of observation, the design (panel FE, DiD, IV, RDD, cross-section), and the main treatment and outcome variables. Generate the scaffold with those names filled in, not as placeholders.

## The master do-file

`00_master.do` sets the project root as a global, creates missing folders, opens a dated log, runs each numbered do-file in order with a toggle per stage (so a single stage can be rerun), and closes the log. It also records the Stata version and the packages required, and installs missing packages from SSC with a check rather than an unconditional install.

## What each do-file does

- **01_setup**: version, globals for paths, `_graphprefs.do` and `_globals.do` sourced, package checks (reghdfe, ftools, estout, coefplot, and any design-specific estimators the project needs, such as csdid, did_multiplegt, or rdrobust), and a scheme for figures.
- **02_import**: reads each raw file with encoding handled, saves to interim with the original variable names, and asserts row counts against the documented totals.
- **03_clean**: applies the cleaning steps from the data-profiling-and-cleaning skill, with a count logged after every drop and every recode, writing to `docs/cleaning_log.md`.
- **04_construct**: builds analysis variables with labels stating the formula, treatment indicators, event-time variables, cohort variables for staggered designs, and log or standardized outcomes as needed.
- **05_sample**: applies sample restrictions in fixed order, saves the analysis file, and writes the sample construction table with counts at each step.
- **06_descriptives**: summary statistics by treatment status, balance table, and the descriptive figures, exported with estout or equivalent to `output/tables` using the academic-tables-booktabs conventions.
- **07_identification**: the diagnostics the design requires: pre-trend event study for DiD, first stage and weak-instrument statistics for IV, density and covariate continuity for RDD, common support for matching. Outputs saved, never only displayed.
- **08_main_results**: the estimating equation from the design document, the build-up across specifications, clustered standard errors at the stated level, exported to a single main table.
- **09_robustness**: alternative specifications, samples, and estimators, each labeled, exported to an appendix table.
- **10_figures**: event-study plots, coefficient plots, and any descriptive figures, following the academic-figures-monochrome conventions and the project's graph preferences file.

## Coding conventions embedded in the scaffold

- Every do-file starts with a header: purpose, inputs, outputs, author, date, and last change.
- No absolute paths; everything relative to the project root global.
- `assert` statements after merges and drops, so silent data loss stops the run.
- Variables labeled at creation; value labels for categoricals.
- One estimation command per model, results stored with `estimates store`, tables built from stored estimates rather than copied by hand.
- Seeds set for anything random.
- Comments explain why, not what; the code already says what.

## Deliverables

The full folder structure with every do-file written and runnable against the described data, `docs/README.md` explaining how to run the project, and a short note listing the decisions the researcher still has to make (clustering level, fixed effects set, sample restrictions) marked in the code with a searchable tag.

When the environment has a Stata-specific skill, use it for syntax details; this skill governs structure and reproducibility.

## Quality bar

- `do 00_master.do` runs end to end on the described data without manual steps.
- Every table and figure in the paper can be traced to one do-file and one exported file.
- Every drop in sample size is logged with a count.
- A second researcher can read `docs/README.md` and reproduce the results.
