---
name: data-profiling-and-cleaning
description: Profiles a dataset before anyone estimates anything on it, then cleans it through code that can be rerun, producing a data quality report, a cleaning log, a sample construction table and an analysis-ready file. Enforces that raw files are never edited, that every variable used is checked against its codebook, that missing codes and sentinel values are found before they become numbers, that merge match rates and panel attrition are reported rather than absorbed, and that every transformation between raw and analysis file is a logged step with a reason and a count. Language agnostic: it decides what must be checked and recorded, not which software does it. Use this skill whenever a dataset arrives or is loaded for the first time, before any estimation on data not yet profiled in this project, when merging or appending files, when harmonising variables across years or waves, when a codebook is in another language, when accents or special characters look wrong, or when somebody says the numbers look odd, the sample is smaller than expected, or a mean has moved for no reason. Trigger also on vaguer requests such as "check this file", "is this data any good", "profile this before I start", or "something is weird in my data".
---

# Data Profiling and Cleaning

Almost every serious empirical error is a data error that nobody looked for. The estimator was right, the identification was defensible, the code ran, and the sample quietly contained four thousand rows in which a missing income was coded as 99999 and treated as a number. Nothing in the output says so. The regression returns a coefficient, the standard error is reasonable, and the paper is written.

That is the failure this prevents: a defect that is invisible in every downstream diagnostic and fatal to the conclusion. Data problems do not announce themselves. A merge that dropped twelve percent of observations returns a dataset, not an error. An identifier that lost its leading zeros produces a match rate that looks like ordinary administrative attrition. A variable whose codes changed meaning in the third year of a panel produces a trend. A duplicate row produces a slightly heavier weight on one unit. Each of these has an explanation ready to hand, which is exactly why they survive.

The cost is asymmetric and it grows with time. Found on day one, a sentinel value costs ten minutes. Found in the third year of a thesis, it costs every table, every figure, every paragraph of interpretation, and whatever was said in two conference presentations. Found by a referee or a journal data editor, it costs the submission. Found after publication, it is a corrigendum, and the researcher's next paper is read differently.

The discipline is not sophistication. It is looking on purpose, in a fixed order, at things that are boring to look at, and writing down what was found.

## When to use this, and when not to

Use it on every dataset the first time it enters a project, and again whenever a new wave, a new year or a new source arrives. Use it before the first estimation on any file that has not been profiled in this project, including a file inherited from a coauthor or a predecessor with assurances that it is clean. Use it when a merge or an append is about to happen, when variables are being harmonised across years, and when a result has moved and nobody can say why.

Use it especially on administrative microdata and on published statistical microdata, which are large, well documented and full of conventions that are obvious to the agency that produced them and invisible to everyone else.

Do not use it for the Stata command craft that implements the fixes: the import types, the destring and encode decision, the merge syntax and its match indicator, reshape, labels, date representation, panel declaration and saving are `stata-data-management`. This skill decides what must be checked and what must be recorded; that skill knows how Stata does it and what Stata does silently. The equivalent for a Python project is `python-for-econometrics`.

Do not use it to design the do-file architecture the cleaning code lives in, which is `stata-do-file-craft`, or the folder layout and the numbered stage skeleton, which is `stata-project-scaffold`. Do not use it to build the paper's summary statistics table, which is `descriptive-statistics-tables`, or to write the data section prose, which is `data-section-writer`, although both take their inputs directly from what this skill produces. Do not use it to decide which observations belong in the sample on substantive grounds, which is a design judgement belonging to `econometrician` and `research-design`; profiling reports what dropping them would cost, and does not decide whether to drop them.

Do not use it as the post hoc check that the paper's numbers came from the code. That is `analysis-audit`, and it runs at the other end of the project.

## What you need before starting

**The raw files, with their provenance.** Where each came from, when it was obtained, from whom, and under what version or extract specification. Missing: record file name, size, and modification date at minimum, and state that provenance is unknown, because a file that cannot be re-obtained makes the project irreproducible upstream of itself no matter how good the code is.

**The codebook or data dictionary for every source.** This is what tells you that minus eight means "not applicable" and that a variable is asked only of a subgroup. Missing: reconstruct what you can from value distributions, mark every reconstructed meaning as inferred, and do not recode anything you had to guess without flagging it in the file and in the report.

**The intended unit of observation of the final analysis file.** Person-year, firm-year, household, school-cohort, municipality-quarter. Almost every serious merge and aggregation error is a unit-of-observation error. Missing: write it in one sentence before any code is run, because a key cannot be checked before it is named.

**The variables the analysis will actually use.** Profiling everything in a 400-variable extract wastes days. Missing: profile the identifiers, the outcome, the treatment and every variable named in the design document, and profile the rest at the level of structure and missingness only.

**Expected counts, from a published source or from the provider.** How many units should be in this year, how many rows the extract should contain. Missing: state your expectation anyway, even roughly, because the value of an expectation is that it turns a surprise into a signal instead of into a number you accept.

**The expected match rate for every merge, before running it.** Missing: state a guess and then explain the difference, since an unexpected 89 percent match is only detectable as a problem if somebody expected 97.

**Whether identifiers are stable over time.** Firms merge, municipalities split, schools are renumbered, people change identifiers between waves. Missing: check whether the count of distinct identifiers is stable across periods and whether any unit appears under two, and use the publisher's crosswalk where one exists rather than building your own.

**The data licence and any disclosure rules.** They constrain what can be shown in the quality report and what can be shared. Missing: assume the strictest reading, suppress small cells in any output that will leave the project, and route the question through `research-ethics-and-data-protection`.

## The method

Steps 2 to 11 are the profiling sequence, run in order on every new file, with the findings written into the data quality report as you go. Order matters within it: structure before content, and identifiers before anything else, because an identifier problem invalidates everything found after it.

1. **Never edit a raw file, and make that structural rather than a convention.** Raw files are read-only, kept in a directory that nothing writes to, ideally set read-only at the file system level. Every cleaning decision is expressed as code that reads raw and writes elsewhere. There is no acceptable exception, including the tiny obvious fix in a spreadsheet, which is where the majority of unreproducible datasets begin: a spreadsheet application will silently reformat dates, truncate long numeric codes and drop leading zeros on save, and it leaves no record that it did. Record a checksum or the size and date of each raw file, so a later change is detectable. If a file must be converted before it can be read at all, script the conversion and treat its output as a new raw file with its own provenance record.

2. **Structure.** Format, encoding, delimiter, header rows, row and column counts, and file size. Check encoding explicitly by looking at accented and non-Latin characters: mojibake is common in administrative data from countries whose agencies export in a legacy code page, and once it has been read wrongly and saved, the original characters are not recoverable. Then confirm the unit of observation empirically by testing whether the presumed identifier combination is unique, rather than assuming it because the documentation says so.

3. **Identifiers.** Uniqueness, missingness, format consistency across files and across years, and type. The judgement call is whether an identifier is a code or a quantity, and the rule is absolute: an identifier is a string, always, because reading it as a number strips leading zeros and the damage appears later as a merge failure that looks like missing data. Check the length distribution of the identifier: a code that is nine characters in most rows and eight in some is the signature of exactly that loss.

4. **Codebook conformance.** For every variable that will be used, compare the observed values with the documented codes. Three findings matter: values outside the codebook, codes present in the codebook but absent in the data, and codes whose meaning changed between years. Where the codebook is in another language, keep the original variable names and add labels in your working language rather than renaming, so the code stays traceable to the source documentation and a reader can check it against the original.

5. **Missingness and sentinel values.** Rate per variable, and the pattern across variables and across time. Distinguish three kinds: structurally missing, meaning the question did not apply; item missing, meaning it applied and was not answered; and coded missing, meaning a sentinel such as 99, minus one, 9999 or a string like "NA" is standing in for a missing value. The rule for finding sentinels: look at the maximum and minimum of every numeric variable and at the ten most frequent values, because a sentinel is almost always an extreme value or a suspiciously frequent one. Sentinels treated as numbers are the single most damaging silent defect in this list.

6. **Distributions.** For numeric variables, minimum, maximum, mean, median, the percentiles at the tails, and the count of zeros. For categoricals, full frequencies. Flag impossible values against the real world, not against the data: negative ages, scores above the instrument maximum, dates before the programme existed, shares above one, and durations longer than a lifetime. Flag suspicious spikes, meaning a value far more frequent than its neighbours, which is usually a default, a rounding, an imputation, or a top-code. And check units, since a variable recorded in thousands in one year and in units in the next produces a trend nobody questions.

7. **Panel coherence, for longitudinal data.** How many units appear in every period, how many enter, how many exit, whether identifiers persist, whether time-invariant variables actually stay invariant, and whether gaps exist inside a unit's series. Attrition is not a nuisance to be cleaned away: its pattern is a result the paper will have to report, and whether it is related to the outcome determines how much of the analysis survives.

8. **Cross-file consistency, before every merge.** Compare the key's format, type and length distribution on both sides. Then merge and report the match rate, the count unmatched from each side, and, critically, what the unmatched rows look like on observables. Unmatched rows that are random are an inconvenience; unmatched rows concentrated in small units, one region, or one year are a finding, and they change what the estimates mean.

9. **Duplicates.** Exact duplicate rows, and near-duplicates meaning the same key with different values. The rule: never resolve duplicates by dropping in whatever order the file happens to be in, because which row survives then depends on the sort order and the discarded row may have been the correct one. Examine them, write a rule, apply the rule, and record how many cases the rule was applied to.

10. **Cross-variable logic.** Internal consistency checks that the codebook implies: a person with a start date after their end date, a household with more children than members, a firm with revenue and no employees, a routed question answered by somebody who should have skipped it. These find data entry and processing errors that per-variable profiling never sees.

11. **Comparison against a published benchmark.** Where the source publishes aggregates, reproduce one: a total count, a national mean, a distribution by a major category. This is the highest-value single check in the whole sequence, because it tests the whole chain from file to your reading of it. A mismatch usually means a weight was not applied, a subpopulation filter is implicit in the extract, or the extract is not what you think it is.

## Cleaning rules

Every transformation is a step in code, with a reason and a count of what it affected. The cleaning log is generated from the code rather than written alongside it, so the two cannot diverge.

- **Never impute silently.** Where imputation is used, it is a named method with a flag variable marking imputed values, and the analysis reports results with and without them.
- **Never drop without a count.** Every restriction records the number before and after. Those counts are the sample construction table, and reconstructing them later is far more work than keeping them.
- **Apply restrictions in a fixed, documented order**, since the counts depend on it.
- **Recode into new variables**, leaving the source variable intact in the interim file, so a decision can be inspected and reversed.
- **Label everything at creation**, with the label of a constructed variable stating its formula and its source variables.
- **Handle sentinel values at import**, before any arithmetic touches them, and preserve the reason for missingness where the software allows a distinction.
- **Harmonise across years by writing a crosswalk as a separate, inspectable file**, never as an inline chain of recodes, because a harmonisation is a research decision a referee may want to see.
- **Top-code and winsorise only as a stated decision** with the threshold justified, and report the untreated result somewhere.
- **Keep the intermediate files.** Storage is cheap and the ability to reload the file as it stood before a mistaken step is what turns a two-day recovery into a ten-minute one.

## Worked example

**Situation.** A doctoral researcher received three annual extracts from a national school census covering all public secondary schools, to study how a school funding reform affected pupil-teacher ratios. Each extract was a delimited text file of roughly 780,000 rows and 118 variables, one row per school-class-year, with a separate municipal file holding the funding variables. The codebook was 240 pages, in the language of the issuing agency, and differed slightly between years. The supervisor wanted first descriptives in three weeks.

**Task.** A defensible school-year analysis file with a documented observation count, a merge to the municipal file that could be explained, and a data quality report that could become a thesis appendix.

**Action.** Structure first. The files opened with visibly broken accented characters in school names and municipality names. Reading them with the encoding the agency documented fixed the school names and, more importantly, revealed that two municipality names had been silently truncated at a special character in an earlier colleague's version of the file, which was how those municipalities had been getting lost.

The identifier check found the expected problem in an unexpected place. School codes were eight characters and imported as strings correctly. Municipality codes were seven digits and had been read as numeric by the default import, dropping the leading zero on every municipality in one region. The length distribution made it obvious: 5,208 rows at six characters against the rest at seven.

The wrong turn happened next and cost three days. Rather than re-importing, the researcher padded the short codes back to seven characters with a leading zero, which is the obvious repair and is wrong. It appeared to work, and the merge to the municipal file rose from 89.4 percent to 99.1 percent. The remaining 0.9 percent was assumed to be small municipalities missing from the funding file, an explanation that was available and plausible. It was only the benchmark check, three days later, that exposed the error: the reproduced count of schools in one region was 214 against a published figure of 231. The padding rule had been applied to every code of six characters, but a small number of genuine municipality codes in another region also had six digits and had never lost anything, so padding created seventeen codes that pointed at the wrong municipality. The lesson recorded in the report: a lost leading zero cannot be restored by inference, because you cannot tell how many were lost. The file was re-imported with the identifier typed as a string from the start, and the match rate came out at 99.6 percent with the unmatched rows concentrated in four municipalities that had been created by a boundary change in the second year.

Profiling the analysis variables found three further things. The pupil count variable had a spike at 9999 in 1.8 percent of rows, which was the agency's code for "not reported" and would have made the mean pupil-teacher ratio meaningless in a way no diagnostic would have flagged. The teacher contract type variable had four categories in the first two years and six in the third, where one category had been split; the crosswalk collapsed the two new categories back for comparability and kept the finer version in a separate variable. And a class-size variable was recorded per class in two years and per class group in the third, which the codebook explained in a footnote on page 173 and which produced a 12 percent step in the series that would otherwise have been read as an effect of the reform.

Duplicates: 1,341 exact duplicate rows, all in the second year, all from a known re-submission by one state, resolved by keeping one and recording the rule. A further 86 school-class-year keys appeared twice with different pupil counts; those were kept as a flagged set, the larger count used, and a sensitivity check run later with the smaller.

Boundary change identifiers were handled with the agency's own crosswalk file rather than a home-made one.

**Result.** 2,384,110 raw rows became 41,208 school-year observations across 14,092 schools after aggregation and restriction, with every step counted in the sample construction table. The merge to municipal funding matched 99.6 percent. The data quality report ran to nine pages and went into the thesis appendix with light editing. The benchmark check reproduced published school counts to within 0.3 percent in all three years, with the residual explained by a documented difference in how the agency counts schools with multiple campuses.

Profiling and cleaning took four and a half weeks against an estimate of three. Three days of that were the padding error. The 9999 code alone would have changed the headline result, and nothing downstream would have revealed it.

### A second scenario, where it goes differently

The same researcher later exported 480 responses from a survey platform: one row per respondent, 62 columns, all collected in one wave, in one language, with a schema the researcher had designed.

Most of the sequence collapses. There is no codebook conformance problem because the researcher wrote the instrument. There is no cross-year harmonisation, no panel coherence, no merge. Encoding still matters and took five minutes to check. Profiling took about forty minutes in total.

What moves to the front is different. Duplicate submissions from the same respondent, identifiable by a combination of timestamp proximity and identical open-text answers, of which there were four. Straight-lining across grid items, at 2.1 percent. Completion times, where eleven responses under three minutes on a ten-minute instrument were flagged rather than dropped, with the analysis reported both ways. Attention check failures, which the platform recorded. Item nonresponse concentrated in the two questions about pay. And the open-text fields, which needed encoding checks and whitespace normalisation before they could go to `qualitative-coding-and-analysis`.

The rules that survived unchanged: the export was treated as raw and never edited, every exclusion was counted, the exclusions were applied in a fixed order, and the resulting sample construction table went straight into the paper. Those four are not a function of dataset size. What changes with size is which checks pay, not whether the discipline applies.

## Output

**The data quality report**, written as it goes and structured so it can become an appendix:

```
DATA QUALITY REPORT: [source, extract date, version]
1  Provenance      Where obtained, when, from whom, extract specification, checksum
2  Structure       Format, encoding, rows, columns, unit of observation as verified
3  Identifiers     Key tested, uniqueness result, type, length distribution, issues found
4  Codebook        Variables checked, values outside the codebook, codes changed across years
5  Missingness     Per-variable rates, sentinel values found, structural versus item missing
6  Distributions   Impossible values, spikes, unit changes, top-coding found
7  Panel           Units per period, entry, exit, gaps, invariance violations, attrition pattern
8  Merges          Expected and actual match rates, unmatched characterised on observables
9  Duplicates      Exact and key duplicates, resolution rule, cases affected
10 Logic checks    Cross-variable inconsistencies found and how resolved
11 Benchmark       Published figure, reproduced figure, difference and explanation
12 Open items      What could not be verified, and what the analysis must therefore assume
```

**The variable profile table**, for every variable the analysis uses:

| Variable | Type | N non-missing | Missing % | Sentinel codes found | Min | p1 | Median | p99 | Max | Distinct values | Codebook conformance | Action taken |

**The cleaning log**, generated from the code:

| Step | Script and line | Operation | Reason | Rows before | Rows after | Units before | Units after |

**The sample construction table**, which goes into the paper almost unchanged:

| Restriction | Rows remaining | Units remaining | Rows dropped | Share dropped |
| Raw file as received | | | | |
| Drop non-eligible school types | | | | |
| Drop years outside study window | | | | |
| Drop observations missing the outcome | | | | |
| Analysis sample | | | | |

**The merge report**, one row per merge:

| Merge | Key | Expected match | Matched | Master only | Using only | How unmatched differ | Disposition |

**The analysis file itself**, with labelled variables, consistent types, a verified unique key, a documented unit of observation, a flag variable for anything imputed or altered, and a note recording the script and date that produced it.

## Failure modes

**Profiling skipped because the data came from a reputable agency.** Recognise it by the absence of a quality report. Reputable agencies have conventions, and conventions are what break outsiders. Fix by running the sequence anyway; on a well-documented source it is fast.

**Identifiers read as numbers.** Recognise it by a length distribution with two modes, or a distinct count lower than expected, or a merge failing on a geographically clustered subset. Fix by re-importing as a string. Never repair by padding, since you cannot know how many characters were lost.

**Sentinel values treated as data.** Recognise it by a maximum that is a run of nines, or a frequency table with a spike at an implausible value. Fix at import, before anything computes a mean.

**A merge rate accepted because a plausible explanation was available.** The most dangerous failure in this list, because the mind supplies the explanation before the check. Fix by stating the expected rate before running the merge and by characterising the unmatched rows on observables every time.

**Duplicates dropped without examination.** Recognise it by a drop command with no preceding count and no stated rule. Fix by examining, writing the rule, and recording how many cases it touched.

**Harmonisation by inline recode.** Recognise it when the mapping between years exists only inside a long chain of replace statements. Fix by writing the crosswalk as a separate file that can be read and checked.

**Cleaning in a spreadsheet.** Recognise it when the analysis file cannot be regenerated from raw by running code. Fix by rebuilding the steps as code, even where that takes a day, because the alternative is a project that cannot be defended.

**The quality report written at the end.** Recognise it because it is short and has no counts. Fix by writing it during profiling; reconstructing counts afterwards means rerunning everything.

**Outliers deleted because they are outliers.** Recognise it by a restriction whose reason is that the value is extreme. Fix by distinguishing impossible values, which are errors, from extreme but possible values, which are data; treat the second with a stated and reported method, not by deletion.

**Attrition cleaned away.** Recognise it when a balanced panel appears out of an unbalanced source with no note. Fix by reporting the attrition pattern and testing whether it relates to the outcome.

**No benchmark check.** Recognise it by the absence of any external number in the report. Fix by reproducing one published aggregate, which is the cheapest strong test available.

## Edge cases

**No codebook at all.** Reconstruct meaning from distributions and from any published aggregate, mark every inference as inferred in the report and in the variable labels, and keep uninterpretable variables in the file unrecoded rather than guessing. Exclude anything guessed from the analysis.

**Data too large to hold in memory.** Profile on a random sample for distributions, but run identifier, duplicate and key checks on the full file, since those cannot be sampled. Where the full file must be processed in chunks, never let the chunking change a computation that spans chunks, such as a within-unit mean or a duplicate check across the whole key.

**Data accessible only inside a secure environment.** Profiling still happens; the report is what leaves, and it must respect disclosure rules such as minimum cell sizes. Plan the checks before entering the environment, because time inside is usually limited and expensive.

**Weighted survey data with a complex design.** Declare the design before computing anything, and record strata, primary sampling unit and weight variables in the file. An unweighted mean will not match the published figure, and that mismatch is usually the first sign that the design was never declared rather than that the data is wrong.

**A variable's meaning changes mid-series.** Do not harmonise silently. Keep both versions, build an explicit crosswalk, and consider treating the break as a structural feature of the data that the design has to accommodate.

**The provider issues a corrected extract mid-project.** Treat it as a new raw file with its own provenance, rerun the pipeline, and diff the analysis file against the previous one at the level of counts and key statistics. Report what changed rather than silently adopting the new numbers.

**Data that cannot be shared.** The quality report, the cleaning log and the sample construction table can almost always be shared even where the data cannot, and they are what make the work checkable. Prepare them for that purpose from the start.

**Somebody else's cleaned file with no cleaning code.** Treat it as raw data of unknown provenance. Profile it fully, reconstruct what you can about how it was built, and state in the paper that the pipeline upstream of your work is undocumented, because that is what a data editor will find.

## Quality bar

- Raw files are unmodified, and the analysis file can be regenerated from them by running code end to end.
- Every variable used in the analysis has been checked against its codebook and had its distribution inspected, with the result recorded per variable.
- Every merge reports an expected rate, an actual rate, and a characterisation of the unmatched rows.
- Every dropped observation is counted in a sample construction table that reconciles from raw rows to the analysis sample.
- Sentinel and missing codes were identified and handled before any statistic was computed.
- At least one external benchmark figure was reproduced, or the report states that none was available.
- Nothing is imputed, top-coded or winsorised without a flag variable and a stated method.
- The report states plainly what could not be verified and what the analysis therefore assumes.

## Adapting this to your context

The profiling sequence is written for administrative registers, large panels and linked government files. Every step applies to survey and experimental data too, but the emphasis shifts and two whole categories are missing.

- **What is not profiled here.** Survey and instrument data need checks this list lacks: straightlining, completion time outliers, attention check failures, reverse-coded items never reversed, and scale reliability before the composite is built. Add them as a step 12 and run them before anything is scored.
- **The benchmark check.** Written as reproducing a published national aggregate. For survey data, reproduce the published weighted estimates from the same wave; for a trial, the CONSORT flow counts; for a qualitative corpus, that the transcript count and the interview log agree.
- **Sentinel values.** The 99, minus one and 9999 list is administrative. SPSS files carry user-missing values that read as valid numbers elsewhere, and Likert data often codes "prefer not to say" as 8 or 9 inside a live range. Read the codebook before the file.
- **The tooling.** Stata and pandas are assumed. In R, `skimr`, `janitor` and `pointblank` cover the same ground and `pointblank` writes the report; SPSS `CODEBOOK` and `FREQUENCIES` do the per-variable pass.
- **What not to change.** Raw files are read-only and every cleaning decision is code. Nothing is fixed in a spreadsheet, ever.

## Related skills

`stata-data-management` implements these decisions in Stata and covers the traps specific to how Stata represents types, missing values, dates and panels; `python-for-econometrics` is the equivalent for a Python project. `stata-project-scaffold` provides the folder layout and the numbered stage the cleaning code lives in, and `stata-do-file-craft` governs how that code is written so it reruns cleanly. `research-design` and `econometrician` decide which observations belong in the sample on substantive grounds, and this skill supplies the counts that decision costs. `descriptive-statistics-tables` builds Table 1 from the cleaned file, and `data-section-writer` turns the quality report and sample construction table into the paper's data section. `survey-and-instrument-design` is where to look when the defects trace back to the instrument rather than the processing, and `qualitative-coding-and-analysis` takes the open-text fields this skill normalises. `analysis-audit` runs the independent rebuild at the end of the project, and `replication-package` deposits the pipeline this skill produces.
