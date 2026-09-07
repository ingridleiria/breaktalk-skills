---
name: regression-table-production
description: Turns estimation output into a regression table a journal will print, generated from stored estimates rather than retyped. Covers storing and saving estimates, exporting with a table package, one specification per column and one varying dimension per table, indicator rows for fixed effects and control blocks, the sample size row and which R-squared variant belongs where, standard errors in parentheses with the clustering stated in the note, the case for confidence intervals instead of stars, publication coefficient labels, decimal discipline, panel tables for multiple outcomes, and the note that must carry the estimator, the clustering, the sample and the period. Use this skill when someone asks to build or fix a regression table, says their table does not match their code, asks what to report in a table, how many decimals, whether to use stars, what the note should say, or needs Table 2 for a paper, thesis or referee response. Trigger also on vague requests such as "make this look like a real table", "the referee could not tell what column 4 does", or "turn this output into a table".
---

# Regression Table Production

The failure this prevents is a table that no longer matches the code that produced it. It happens the same way every time. The estimates are exported, a label is wrong, the label is fixed by hand in the exported file, and then the specification changes and the table is regenerated, or worse, is not. Either the hand fix is lost or the hand-fixed file is the one that goes to the journal, carrying numbers from a version of the analysis that no longer exists. Nobody notices, because a regression table looks the same whether or not it is current.

The second failure is a table that is current and still unreadable. It has five columns and no indication of what changes between them, standard errors in parentheses with no statement of what they are clustered on, an R-squared of 0.94 that comes from absorbed fixed effects and means nothing, no sample size, and a note that says "robust standard errors in parentheses" under a model estimated with clustering. A referee cannot evaluate that table, so they either ask questions that cost a round of revision or they assume the worst.

The cost of both is measured in review cycles. A data editor who cannot reproduce a printed number returns the package. A referee who cannot tell what column 4 adds writes that the specifications are unclear, which is the sort of comment that is expensive to answer and impossible to argue with.

## When to use this, and when not to

Use it for any table of estimation results going into a paper, thesis chapter, referee response, or presentation: main results, robustness, heterogeneity, first stages, panel tables across several outcomes.

Do not use it for the typography, which is `academic-tables-booktabs`: three horizontal rules, no vertical lines, aligned decimals, notes below the rule, and the Word and LaTeX mechanics. That skill governs how the table looks; this one governs what is in it and how it is generated. In practice they run together, and where they disagree on presentation, `academic-tables-booktabs` wins.

Do not use it for summary statistics, balance tables or correlation matrices, which are `descriptive-statistics-tables`. Do not use it to decide what to estimate or what to cluster on, which is `econometrician`; this skill reports those decisions faithfully and does not make them. Do not use it to write the paragraphs that interpret the table, which is `results-writing`. Do not use it for figures, including coefficient plots, which are `academic-figures-monochrome`.

## What you need before starting

**Stored estimates, produced by code in this run.** Not a screenshot, not the output window, not a spreadsheet somebody transcribed. Missing: re-run the estimation with storage added. Building a table from retyped numbers is the failure this skill exists to prevent, and there is no version of it that is acceptable under deadline.

**The specification map: what each column is and what varies between them.** Missing: reconstruct it from the code and get it confirmed, because a column whose content the author cannot state in one line will not have a comprehensible heading either.

**The clustering level and the number of clusters, for each column.** These go in the note and the second one goes in the table body. Missing: extract them from the stored estimates; most estimation commands leave the cluster count behind, and if a column has a different clustering from the others that fact is a finding, not a formatting detail.

**The estimation sample definition and period.** The note has to state who is in the table. Missing: take it from the build log; if there is none, produce one before the table, because a table whose sample cannot be described cannot be defended.

**Publication names for every reported variable.** `lwage_hat_2` is not a row label. Missing: write them now; it takes ten minutes and it is the difference between a table a reader can use and one they have to decode against the text.

**The target's format and house rules.** LaTeX or Word, whether the journal prints stars, its decimal conventions, its maximum table width, and whether it requires confidence intervals. Missing: default to booktabs LaTeX with standard errors in parentheses and three star levels defined in the note, and say you have assumed it; converting later is mechanical if the table is generated from code.

## The method

1. **Store every estimate at the moment it is produced, and save the store to disk.** Storing in memory lets the table be built in the same run; saving to disk lets it be rebuilt without re-running a model that takes an hour. Both matter, and the second one is what makes a late formatting change cheap.

```stata
eststo clear
eststo m1: reghdfe lwage treat,            absorb(firm_id year) cluster(state)
eststo m2: reghdfe lwage treat `basecont', absorb(firm_id year) cluster(state)
eststo m3: reghdfe lwage treat `basecont' `firmcont', absorb(firm_id year) cluster(state)
estimates save "$out/estimates/tab03", replace
```

2. **Attach the indicator rows at estimation time, not at export time.** The rows saying which fixed effects and which control blocks are in a column must come from the estimation itself, because an indicator row typed at export is a claim about the model rather than a fact about it, and it is exactly the thing that goes stale when a specification changes.

```stata
eststo m3: reghdfe lwage treat `basecont' `firmcont', absorb(firm_id year) cluster(state)
estadd local fe_firm   "Yes"
estadd local fe_year   "Yes"
estadd local c_base    "Yes"
estadd local c_firm    "Yes"
estadd scalar n_clust  = e(N_clust)
summarize lwage if e(sample)
estadd scalar dep_mean = r(mean)
```

The dependent variable mean over the estimation sample deserves particular attention: it is what converts a coefficient into a proportional magnitude, it takes two lines, and its absence is the most common reason a reader cannot tell whether an effect is large.

3. **Let each table vary in one dimension, and use panels for a second.** Columns should differ in one thing: progressively added controls, alternative fixed effects, alternative samples, or alternative estimators. A table where column 2 adds controls and column 3 changes the sample and column 4 does both is a table nobody can read, because no comparison between two columns isolates anything.

The rule for choosing the dimension: put in columns whatever the reader must compare to judge the claim, and put in panels whatever they must see but need not compare directly. Multiple outcomes go in panels with one row block each and identical columns, so the specification is held constant down the page.

4. **Export with a table package, into the format the target wants, in the same run that produced the estimates.** The specific package matters less than the rule that no number reaches the document by hand. In Stata, `esttab` and `estout` are the usual choices, and `outreg2` remains common for Word output. In Python the equivalents live in `python-for-econometrics`. Where no package is available, write the table from the stored estimates with a small loop that reads `_b[]` and `_se[]`; that is still generation from code and it still satisfies the standard.

```stata
esttab m1 m2 m3 using "$out/tables/tab03_main.tex", replace booktabs fragment ///
    b(3) se(3) star(* 0.10 ** 0.05 *** 0.01) ///
    keep(treat) coeflabels(treat "Programme") ///
    mtitles("Baseline" "Plus worker controls" "Plus firm controls") ///
    stats(fe_firm fe_year c_base c_firm dep_mean N n_clust r2_within, ///
          labels("Firm FE" "Year FE" "Worker controls" "Firm controls" ///
                 "Mean of dep. var." "Observations" "Clusters" "Within R\$^2\$") ///
          fmt(0 0 0 0 3 %12.0fc %9.0fc 3)) ///
    nonotes addnotes("\footnotesize Notes: ...")
```

5. **Report the estimate and its uncertainty in a fixed arrangement, and say what the uncertainty is.** Coefficient on one line, standard error in parentheses directly beneath it, in every column, with no exceptions for the column where it would be inconvenient. The note states what the parentheses contain and the level they are clustered at. A table that says only "standard errors in parentheses" is incomplete: robust, clustered on what, or bootstrapped with how many replications are different claims and only one of them is true.

6. **Consider reporting confidence intervals instead of stars, and know the argument.** Stars compress a continuous quantity into three bins, encourage reading a table by looking for asterisks, and make a coefficient with a p-value of 0.049 look categorically different from one at 0.051. An increasing number of journals in economics, epidemiology and psychology either discourage or forbid them. A confidence interval carries the same information as the star plus the magnitude and the precision, which is what a reader actually needs to judge whether an effect is economically meaningful.

The practical rule: if the target journal permits intervals, report them, in brackets beneath the coefficient, and drop the stars. If the target expects stars, use them, define every level in the note, and put the interval in the appendix for the main coefficient. Never report stars without the standard error, which is a table that cannot be re-analysed and which some journals reject outright.

7. **Always report the sample size, and choose the fit statistic deliberately.** The observation count row is not optional and appears in every column. Where the estimation drops observations, the number in the table is the number actually used, which is why it must come from `e(N)` and not from the dataset.

Which fit statistic belongs depends on the estimator:

| Estimator | Report | Do not report |
| OLS, no absorbed effects | R-squared, or adjusted R-squared where the control count varies across columns | Both, which invites comparison of two things that differ |
| Fixed effects, absorbed | Within R-squared, labelled as within | Overall R-squared, which is dominated by the fixed effects and is near one by construction |
| Instrumental variables | First-stage F or a weak-instrument statistic, and the number of instruments | R-squared, which has no useful interpretation after two-stage least squares |
| Logit, probit, Poisson | Pseudo R-squared if anything, or log likelihood | R-squared, which is not defined |
| Logistic reported as odds ratios | The odds ratio with its confidence interval, and a row stating that coefficients are exponentiated | Odds ratios and untransformed coefficients side by side in one table |
| Multilevel, mixed or hierarchical models | The intraclass correlation from the empty model, the variance component at each level, the number of groups at each level, and marginal and conditional R-squared as a pair | A single R-squared, which hides whether the fit comes from the fixed part or the random part |
| Structural equation and confirmatory factor models | Chi-square with degrees of freedom, CFI, TLI, RMSEA with its interval, SRMR, and the estimator | A model-wide R-squared, which is not what these models are judged on |
| Survival and event history models | Number of events as well as observations, and the hazard ratio with its interval where that is the reported quantity | R-squared, and an events count omitted because the observation count looks large |
| Any model with clustering | Number of clusters | Nothing extra, but the cluster count is mandatory |

An R-squared reported without saying which variant it is causes a specific, avoidable referee comment.

Four of those families carry conventions worth stating explicitly, because they are where fields outside economics differ most.

**Logistic and other non-linear models.** Decide once whether the table reports coefficients, odds ratios, risk ratios or average marginal effects, state which in the note, and hold it constant across every column. Odds ratios are standard in epidemiology and much of public health, average marginal effects in economics, log odds in psychology. An odds ratio has a null of one rather than zero, so the significance statement is an interval that excludes one, and a star key defined against zero is simply wrong beneath an exponentiated coefficient.

**Multilevel and mixed models.** Report the intraclass correlation from the unconditional model, since it is the justification for the nesting; report the variance component at each level; and report the number of groups at each level in the row where a single-level table reports the cluster count. For explained variance, report the marginal and the conditional R-squared as a pair: the marginal is the fixed part alone, the conditional includes the random effects, and either number on its own misleads. Stata's `mixed`, `lme4` and `lmerTest` in R, `MixedLM` in statsmodels and Mplus all produce these, and `performance::r2_nakagawa` computes the pair directly.

**Structural equation and measurement models.** Report chi-square with its degrees of freedom, CFI, TLI, RMSEA with its confidence interval and SRMR, together with the estimator (ML, MLR, WLSMV for categorical indicators) and how missing data were handled. The conventional cutoffs are CFI and TLI at or above 0.95, RMSEA at or below 0.06 and SRMR at or below 0.08. Report the values themselves, not a sentence saying fit was acceptable, and report them once for the model rather than repeating them down a column.

**Survival models.** Report the number of events alongside the number of observations, because a Cox model on 40,000 person-years with 61 deaths is a small study wearing a large sample's clothes, and the observation count alone conceals that.

8. **Label coefficients as the paper names them, order them by importance, and be explicit about what is suppressed.** The parameter of interest is the first row. Controls that the reader needs to see follow. Nuisance terms, fixed effects and constants are suppressed, and the note says they were included. Suppressing a coefficient is legitimate; suppressing it silently is not, because a reader cannot distinguish "not reported" from "not included".

9. **Fix the decimals by what the estimate supports, and keep them constant down a column.** Two or three decimals is right for most coefficients. The test is whether the last digit is informative given the standard error: reporting 0.04213 next to a standard error of 0.019 asserts a precision that does not exist. If a coefficient needs five decimals to be non-zero, the variable is scaled wrong; rescale it and say so in the label, for example expressing spending in thousands rather than units. Standard errors carry the same number of decimals as the coefficients above them. Use thousands separators in the observation count and nowhere else.

10. **Build panel tables so the columns mean the same thing in every panel.** For several outcomes under one specification, use Panel A, Panel B and so on, one outcome each, with identical columns and a single set of column headings at the top. The observations row appears in each panel, because samples usually differ across outcomes. The dependent variable mean row is essential here, since the outcomes are in different units and the coefficients are not comparable without it.

11. **Write the note last and treat it as part of the result.** The note is what makes the table self-contained, and a table that cannot be understood without the surrounding text will be misread when it is reproduced in a slide deck or a referee report. What the note must carry is set out below.

12. **Delete the exported table and rebuild it before submission.** The check is mechanical: remove the file, run the code, confirm the file reappears with identical content. This catches hand edits, stale files and tables built from estimates that no longer exist. Do it before every version that leaves the team.

## What the note has to carry

Every regression table's note contains all of these, in about this order, in three or four sentences:

1. **The estimator and the unit of observation.** "Ordinary least squares on worker-year observations."
2. **What is in parentheses, and the clustering level.** "Standard errors clustered at the state level in parentheses."
3. **The sample and the period.** "The sample is full-time private sector workers aged 25 to 60, 2012 to 2022."
4. **What is included but not shown.** "All specifications include firm and year fixed effects and a quadratic in age; coefficients not reported."
5. **The star key or the interval level.** "* p < 0.10, ** p < 0.05, *** p < 0.01." Or "95 percent confidence intervals in brackets."
6. **Anything non-standard.** Weights, a bootstrap and its replication count, a trimmed sample, a winsorised outcome, an inference method that is not the conventional one.
7. **The data source**, where the table might be read on its own.

A worked note, for the table below:

> Notes: Ordinary least squares on worker-year observations. The dependent variable is log real hourly earnings in 2015 prices. Standard errors clustered at the state level in parentheses; there are 38 clusters. All columns include worker and year fixed effects; column 3 adds firm size, sector and a quadratic in tenure, none of which are reported. The sample is full-time private sector workers aged 25 to 60 observed between 2012 and 2022. Stars denote * p < 0.10, ** p < 0.05, *** p < 0.01. Source: national employer-employee register, authors' calculations.

## Worked example

**Situation.** A three-author paper on the earnings effect of a training programme had a main table with five columns that had been assembled over four months. Two columns came from `esttab`, one had been pasted from the results window into Word during a coauthor call, and two had been edited by hand to correct a variable label. The specification had changed twice since. The paper was due to a journal in six days and one author had noticed that the observation count in column 4 was larger than in column 5, which should have been impossible because column 5 added no restriction.

**Task.** Produce a main table generated entirely from code, reconcile the observation counts, and make the table readable by a referee who has not read the methods section. Good meant that deleting the table file and re-running the code reproduced it exactly.

**Action.** The first step was to rebuild all five columns from a single do-file with `eststo`, which immediately explained the observation counts. Column 5 added a firm-level control that was missing for 2,140 worker-years, so the sample fell, and the coefficient in column 5 was therefore not comparable with column 4 at all. The team's first response was to add a footnote saying the samples differed. That was the wrong turn and it was abandoned within a day: a main table exists so that columns can be compared, and a footnote does not restore comparability. The fix was to run every column on the sample with non-missing values of every variable used anywhere in the table, and to report the wider-sample version in the appendix. That is a substantive change and it moved the headline coefficient from 0.058 to 0.061.

Three further problems surfaced during the rebuild. The reported R-squared was 0.87 in every column, which came from the absorbed worker fixed effects; it was replaced by the within R-squared, which ran from 0.031 to 0.044 and is the honest number. The note said "robust standard errors" while the code clustered at state level; the cluster count of 38 was added as a table row, which also made visible a small-cluster issue that the team then addressed in the inference. And the indicator rows had been typed by hand at export, with the result that the "Firm controls" row said Yes in column 4, where the controls had been removed during the second specification change. That row was wrong in the version that had already been shown at two seminars.

The five columns were relabelled so each heading named what it added, the dependent variable mean was added as a row, coefficients went to three decimals throughout, and stars were kept because the target journal uses them, with the 95 percent interval for the main coefficient added to the appendix table.

**Result.** The table was regenerated in eleven seconds from a single script, and the delete-and-rebuild check passed. The headline number changed by 0.003, which was reported without drama because the reason was stated. The hand-typed indicator row was the finding that mattered most: it had been wrong for four months, in a table shown publicly, and no amount of care in the estimation would have caught it, because the error lived entirely in the export step.

### A second scenario, where it goes differently

A second paper from the same team went to a journal in a field that requires Word submissions and does not accept LaTeX, prints no stars as a matter of editorial policy, and imposes a maximum table width of six columns including the row labels.

Three things changed. The export ran to rich text rather than LaTeX, which meant the table was generated into a Word-readable file by code and then never opened for editing, with all formatting decisions expressed as export options. Stars came out and 95 percent confidence intervals went in beneath each coefficient, which made the table taller and forced the specification count down from five columns to four. The fourth column was the one that had added the least, and losing it improved the table.

The discipline that did not change was the delete-and-rebuild check, and it mattered more here than in the LaTeX case, because a Word table invites hand editing in a way that a LaTeX fragment does not. The rule the team adopted was that the generated file is never opened in the word processor for any purpose other than reading, and that any change is made in the export code.

## Output

The deliverable is a generated table file plus the script that produces it. The table's shape:

| | (1) Baseline | (2) Plus worker controls | (3) Plus firm controls | (4) Balanced sample | (5) Excluding 2020 |
| Programme | 0.061*** | 0.058*** | 0.059*** | 0.055*** | 0.063*** |
| | (0.019) | (0.018) | (0.018) | (0.021) | (0.020) |
| Programme x Post 3 years | 0.088*** | 0.084*** | 0.085*** | 0.081** | 0.090*** |
| | (0.027) | (0.026) | (0.026) | (0.031) | (0.028) |
| Worker FE | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes |
| Worker controls | No | Yes | Yes | Yes | Yes |
| Firm controls | No | No | Yes | Yes | Yes |
| Mean of dep. var. | 2.914 | 2.914 | 2.914 | 2.951 | 2.908 |
| Observations | 180,412 | 180,412 | 180,412 | 96,330 | 164,011 |
| Clusters | 38 | 38 | 38 | 38 | 38 |
| Within R-squared | 0.031 | 0.038 | 0.044 | 0.041 | 0.043 |

Followed by the note carrying the seven items listed above.

For several outcomes, the panel form:

```
                          (1)        (2)        (3)
Panel A: Log earnings
  Programme             0.061***   0.058***   0.059***
                       (0.019)    (0.018)    (0.018)
  Mean of dep. var.      2.914      2.914      2.914
  Observations         180,412    180,412    180,412

Panel B: Employment (=1 if employed)
  Programme             0.014**    0.012*     0.012*
                       (0.006)    (0.006)    (0.006)
  Mean of dep. var.      0.812      0.812      0.812
  Observations         214,660    214,660    214,660

Worker FE                 Yes        Yes        Yes
Year FE                   Yes        Yes        Yes
Controls                   No     Worker    Worker + firm
Clusters                   38         38         38
```

## Failure modes

**Numbers typed or pasted into the document.** Recognise it because the table cannot be regenerated by running the code. There is no partial version of this failure; fix it by rebuilding from stored estimates.

**Hand edits to the exported file.** Recognise it by the delete-and-rebuild check, or by a table whose formatting differs subtly between two columns. Fix by moving every correction into the export options and never opening the generated file to edit.

**Indicator rows typed at export.** Recognise it by comparing every Yes and No against the estimation command that produced the column. Fix with `estadd local` at estimation time.

**Overall R-squared reported for an absorbed fixed effects model.** Recognise it by a value above about 0.8 that is nearly identical across columns. Fix by reporting the within variant and labelling it.

**Note that does not match the code.** Recognise it by reading the note against the estimation command, specifically the clustering. This is the single most common mismatch in published tables. Fix by generating the clustering statement from `e(clustvar)` where the package allows it.

**Columns that vary in more than one thing.** Recognise it when the difference between two adjacent columns cannot be stated in four words. Fix by splitting into two tables or by moving a dimension into panels.

**Samples that differ across columns without acknowledgement.** Recognise it from the observations row changing where no restriction was added. Fix by estimating all columns on the common sample and putting the wider-sample results in the appendix.

**Stars without standard errors.** Recognise it immediately; the parentheses are absent or contain t-statistics unlabelled. Fix by reporting the standard error and defining what is in the parentheses.

**Too many decimals, or decimals varying down a column.** Recognise it by reading one column top to bottom. Fix by setting the format once in the export call rather than per row.

**A table too wide for the page.** Recognise it in the compiled document, not in the code. Fix by cutting a column that adds least, moving to a panel structure, or rotating the table, in that order of preference; shrinking the font is the last resort and most journals will undo it.

## Edge cases

**Coefficients of very different magnitudes in the same table.** Rescale the variables so the reported numbers are readable, and say what the scaling is in the row label, for example "Spending (thousands)". Never mix scales silently in one column.

**Estimates that are not coefficients.** Marginal effects, elasticities, treatment effects from a matching estimator, or bounds. Say in the row label and the note what the number is, since a reader will otherwise read it as a coefficient, and state the method used to compute it.

**Two-step or bootstrapped estimates.** Report the number of replications and the bootstrap type in the note, and confirm that the reported standard error is the bootstrapped one rather than the analytic one that the command also leaves behind.

**A specification the journal wants but you consider inferior.** Report it, in the position the journal expects, and use the text to state why the preferred specification differs. Omitting it invites the comment; burying it in an appendix invites a worse one.

**Very many specifications.** Beyond about eight columns a table stops being read. Move to a coefficient plot or a specification curve, following `academic-figures-monochrome`, keeping the plot monochrome with markers and dash patterns distinguishing the series and the legend outside the plot area, and keep the full numbers in an appendix table.

**A table for a presentation rather than a paper.** Cut to the parameter of interest and two columns, increase the font, and drop the fit statistics. The generation rule still applies: it comes from the same stored estimates, so the slide and the paper cannot diverge.

**Estimates produced by a coauthor in another package.** Do not retype them. Ask for the stored estimates or the coefficient and standard error in a machine-readable file, and generate from that. Where only a printed table exists, reproduce the estimation before using the numbers.

## Quality bar

- Deleting the table file and re-running the code reproduces it exactly, with no manual step.
- Every column's observation count, cluster count and indicator rows come from the stored estimates rather than being typed.
- The note states the estimator, the unit of observation, what is in parentheses, the clustering level, the sample and period, what is included but unreported, and the star or interval convention.
- Adjacent columns differ in exactly one stated thing, and the difference is legible from the column heading.
- The reported fit statistic is the right variant for the estimator and is labelled as such.
- Decimals are constant down each column and no more precise than the standard errors support.
- The dependent variable mean over the estimation sample appears wherever magnitude has to be judged.
- No coefficient in the table appears anywhere in the manuscript with a different value.

## Adapting this to your context

The code here is Stata, the default output is booktabs LaTeX, and the conventions are economics ones: stars, clustered standard errors, a within R-squared. The generation rule is the method; the rest is dialect.

- **The export tooling.** `eststo` and `esttab` are Stata names. In R use `modelsummary`, `gtsummary`, `texreg` or `stargazer`; in Python `statsmodels` with `summary_col`. Mplus, SPSS and SAS all write machine-readable output you export rather than retype. Whatever the tool, the table is written by code from stored estimates.
- **The table style.** Booktabs LaTeX assumes an economics or finance target. APA 7 tables are Word, no vertical rules, notes ordered general then specific then probability, and variable names spelled out. Set the style once in the export call.
- **Stars.** Economics still prints them. APA 7, most medical journals and a growing set of psychology journals prefer confidence intervals, and a few refuse p-values entirely. Follow the target and drop the stars rather than carrying both.
- **The fit statistics.** The table above now covers logistic, multilevel, SEM and survival models. Use the row for your estimator rather than reporting an R-squared because the software printed one.
- **What not to change.** No number reaches the document by hand, and deleting the table file and re-running the code must reproduce it exactly.

## Related skills

`econometrician` decides the specifications, the clustering and the inference that this table reports. `academic-tables-booktabs` governs the typography, rules and alignment of the finished exhibit and takes precedence on presentation. `descriptive-statistics-tables` handles summary and balance tables, which follow different conventions. `academic-figures-monochrome` takes over when the number of specifications makes a coefficient plot more readable than a table. `stata-do-file-craft` and `python-for-econometrics` provide the estimation and export code and the reproducibility discipline it sits in. `results-writing` writes the text that reads the table, and `analysis-audit` verifies that every number in that text appears in this table and in the output file behind it.
