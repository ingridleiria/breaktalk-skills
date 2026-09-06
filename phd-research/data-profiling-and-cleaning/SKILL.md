---
name: data-profiling-and-cleaning
description: Profiles and cleans research datasets before analysis, producing a data quality report, a documented cleaning log, and analysis-ready files, with special care for administrative microdata, panel coherence across years, codebooks in other languages, and encoding problems. Use this skill whenever a researcher receives or loads a new dataset, asks to check data quality, clean data, inspect missing values, find outliers or impossible codes, harmonize variables across years, merge files, validate a panel, or says "something is weird in my data", "profile this file", "check my variables against the codebook", "prepare the data for Stata". Trigger before any estimation on data that has not been profiled in this project.
---

# Data Profiling and Cleaning

Every regression is only as good as the data it runs on, and most data problems are invisible until someone looks for them on purpose. This skill looks on purpose, records what it finds, and leaves a cleaning log so that every transformation from raw file to analysis file can be reproduced and defended.

## Rule one: raw data is never edited

The raw files stay untouched. Cleaning produces new files through code (Stata do-files, Python, or R scripts) that can be rerun from the raw files at any time. The cleaning log records each step with the reason and the count of observations affected.

## Profiling sequence

Run this on every new file and write the results into the data quality report.

1. **Structure**: file format, encoding (check for mojibake in accented characters, common in Portuguese and Spanish administrative data), delimiter, number of rows and columns, and the unit of observation. Confirm the unit matches expectations (one row per student per year, one row per firm, and so on) by checking whether the presumed identifier is unique.
2. **Identifiers**: uniqueness, missingness, format consistency across files and years (leading zeros dropped, numeric versus string, changed coding schemes). Identifier problems are the most common cause of silent merge failures.
3. **Codebook check**: for every variable, compare the observed values to the documented codes. Values outside the codebook, codes that changed meaning across years, and variables that exist in some years but not others are all findings. When the codebook is in another language, keep the original variable names and add English labels rather than renaming, so the code remains traceable to the source documentation.
4. **Missingness**: rate per variable, patterns across variables (is missingness concentrated in certain years, regions, or institution types), and whether missing is coded as blank, a sentinel value (99, -1, 9999), or a string. Distinguish structurally missing (not applicable) from actually missing.
5. **Distributions**: for numeric variables, minimum, maximum, mean, median, and the tails; for categorical, frequencies. Flag impossible values (negative ages, scores above the scale maximum, dates before the program existed), suspicious spikes (a value repeated far more than its neighbors, often a default or imputation), and units that changed across years.
6. **Panel coherence**: for longitudinal data, how many units appear in every period, how many enter and exit, whether identifiers persist, whether time-invariant variables actually stay invariant, and whether the panel is balanced. Report the attrition pattern; it is a result the paper will need.
7. **Cross-file consistency**: when merging, report the match rate, the unmatched observations from each side, and why they did not match. A merge that drops 12% of observations is a finding the reader must see.
8. **Duplicates**: exact duplicates and near-duplicates (same identifier and period with different values). Decide and document how each is resolved.

## Cleaning rules

- Every transformation is a documented step: variable renamed, recoded, or constructed; observations dropped with the reason and the count; missing values recoded to the software's missing convention.
- Never impute silently. If imputation is used, it is a stated method with its own variable flagging imputed values.
- Sample restrictions are applied in a fixed order and each step's count is recorded, producing the sample construction table the data section will need.
- Constructed variables carry a label stating the formula and the source variables.
- The final analysis file has labeled variables, consistent types, a documented unit of observation, and a unique identifier.

## Deliverables

1. **Data quality report** (short document): structure, the findings from each profiling step with counts and percentages, and the decisions taken. Written so it can become a thesis appendix.
2. **Cleaning log**: the ordered list of transformations with counts, generated from the code.
3. **Cleaning script**: do-file or script that goes from raw to analysis file, runnable end to end.
4. **Sample construction table**: raw observations, each restriction, and the resulting count.

When the environment has a data exploration or Stata skill, use it for mechanics; the sequence above governs what must be checked and recorded.

## Quality bar

- Raw files are unmodified and the analysis file can be regenerated from them by one command.
- Every variable used in the analysis has been checked against the codebook and its distribution inspected.
- Merge rates and attrition are reported with counts.
- The report states what could not be verified and what the analysis must therefore assume.
