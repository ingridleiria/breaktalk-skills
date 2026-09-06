---
name: descriptive-statistics-tables
description: Builds the descriptive exhibits that establish a sample before any estimate is shown: the sample construction table tracing every restriction from raw data to analysis sample with counts, the summary statistics table on exactly the estimation sample, the balance table appropriate to the design, and the three to six sentences of prose that report them. Enforces the rule that the descriptive sample and the regression sample are the same sample or the difference is stated, that every variable carries units and a definition, that imbalance is reported rather than hidden, and that every exhibit is generated from code rather than transcribed. Use this skill when someone asks for summary statistics, Table 1, a balance table, a covariate comparison, sample means by group, a sample construction or attrition table, or says describe my sample. Trigger also on vague requests such as "the referee asked where the sample came from", "my Ns do not add up", "make a Table 1", or when a results section begins with no descriptive exhibit at all.
---

# Descriptive Statistics Tables

Descriptive tables are where a referee decides how much of the rest of the paper to believe. They are read early, they are read quickly, and they are read for inconsistency rather than for content. The number of observations in Table 1 is compared to the number in Table 2. The definition of the treatment variable is compared to the one in the text. The share of treated units is compared to what the institutional section implied. Any mismatch found here is cheap for the referee to spot and expensive for the author to explain, and it colours the reading of every estimate that follows.

The failure this prevents is a descriptive section that describes a different sample from the one the paper estimates on. It happens almost mechanically: Table 1 is built early, from the cleaned file, before the final restrictions are settled; the estimation later drops observations with missing covariates, or restricts to a balanced panel, or excludes a year; and nobody rebuilds Table 1. The paper then reports means for 12,400 units and estimates on 11,260, and the difference is never mentioned. Nothing in the paper is false, and a referee who notices has to ask what else was not updated.

The second failure is a balance table that cannot be read. Twenty covariates, means by group, and a column of p-values that are all below 0.01 because the sample has ninety thousand observations, from which nothing whatever can be concluded about whether the groups are comparable. It looks like diligence and functions as noise.

## When to use this, and when not to

Use it for any exhibit that summarises the data rather than estimating an effect: the summary statistics table, the balance or comparison table, the sample construction or attrition table, subgroup means, a table of variable definitions, and the descriptive figures that accompany them. Use it when a results section opens with an estimate and no description, which is a common structural error in thesis chapters.

Do not use it to build tables of estimates, which is `regression-table-production`; the conventions differ in several places, particularly on what belongs in the bottom block and on how uncertainty is displayed. Do not use it to decide the typography, rules, alignment and note format, which is `academic-tables-booktabs` and which governs the appearance of everything here. Do not use it to clean the data or decide the restrictions, which is `data-profiling-and-cleaning` and, in Stata, `stata-data-management`; this skill reports the restrictions that skill made, and if the restrictions cannot be reconstructed, that is the finding. Do not use it to write the data section of the paper, which is `data-section-writer`; these exhibits are what that section is built around.

## What you need before starting

**The analysis sample, as a file, produced by the code that the estimation uses.** Not the cleaned file, the estimation sample. Missing: this is the most common gap and it must be closed before anything is built. Run the main specification, save the estimation sample flag, and build from that. A Table 1 built before the estimation exists will be wrong by the time the paper is finished.

**The cleaning log or construction script, with the restrictions in order.** Every filter from raw to analysis sample and the count after each. Missing: reconstruct it from the scripts and, where a restriction cannot be located, say so in the table note rather than omitting the row. An unexplained gap between the raw file and the analysis file is a finding, not a formatting problem.

**Variable definitions with units, as constructed in code.** Missing: read the construction script rather than asking. The definition in the table must be the definition in the file, and where the author's memory and the code disagree, the code is right.

**The design and the estimand.** Whether treatment is a group, a timing, a cutoff, or a continuous exposure. This determines what the balance table compares and whether a balance table is the right exhibit at all. Missing: ask, in one line. Building a level balance table for a difference-in-differences design when the relevant check is on trends wastes a day and produces a misleading exhibit.

**The order in which the paper introduces variables.** Missing: use outcomes, treatment, then covariates by block, and say you have assumed it.

**The venue's table conventions and the page budget.** Missing: assume that Table 1 sits in the body and anything beyond roughly twenty-five rows goes to an appendix.

**The weights, if the estimation is weighted.** Missing: report unweighted descriptives and say so explicitly in the note. Reporting unweighted means beside weighted estimates without saying so is a quiet inconsistency that a careful referee will catch.

## The method

1. **Build the sample construction table first, from the code, before anything else.** Every restriction in the order it is applied, with the count remaining and the count dropped at each step, and the unit counts as well as the observation counts where the data is a panel. Doing this first is what surfaces the problems: a step that drops far more than expected, a restriction applied twice, a merge that lost a fifth of the sample silently. The rule for when to stop and investigate rather than proceed: any single step dropping more than five percent, or a cumulative loss above twenty percent, is examined before the descriptives are built, because the descriptive tables will otherwise document a sample nobody intended.

2. **Fix the sample flag and use it everywhere.** One indicator variable in the data marking the estimation sample, produced by the estimation itself. Every descriptive exhibit conditions on it. This single mechanical step eliminates the most common failure in this skill, and it takes one line of code.

3. **Choose the variable list and the order.** Outcomes first, then the treatment variable, then covariates in blocks that match how the paper introduces them, then institutional or contextual variables. Cap the body table at roughly twenty-five rows. The rule for what is cut to an appendix: a variable that never appears in a specification and is not referred to in the text goes to the appendix, however interesting it is.

4. **Choose the statistics per variable type rather than applying one template to all.** Continuous variables get mean, standard deviation, and N. Skewed variables such as revenue, firm size, population, or income get the median as well, and where the model uses logs, report the variable in the form the model uses so the reader can connect the table to the coefficient. Binary variables get the mean as a share and N; minimum and maximum on a binary variable are noise and should be dropped or suppressed. Count variables get mean, standard deviation, and the share of zeros, which is what tells the reader whether a Poisson or a linear model is doing the work. Categorical variables get shares by category, not a mean.

5. **Report N per variable and explain any variation.** Where variables have different Ns, either the table has a column for it or the note explains it. Differing Ns in Table 1 with a single N in the regression table means listwise deletion happened somewhere, and that deserves a sentence.

6. **Build the balance table appropriate to the design, not a generic one.** The section below sets out what that means for each design. The judgement here is about what the comparison is supposed to establish, and getting it wrong produces an exhibit that answers a question nobody asked.

7. **Report normalised differences alongside any test.** In samples of more than a few thousand, p-values on covariate differences carry almost no information because tiny differences are significant. A normalised difference, meaning the difference in means scaled by the pooled standard deviation, is comparable across variables and across papers, and a value above roughly 0.25 is conventionally the point at which linear adjustment is doing more work than it can reliably do. Report both where the venue expects the test, and read the normalised difference.

8. **State imbalance in the text where it exists, with what the design does about it.** Never present a balance table and move on when three covariates differ. One sentence: which covariates differ, by how much in normalised terms, and whether the identifying assumption requires balance in levels at all. For many designs it does not, and saying so is stronger than pretending the imbalance is not there.

9. **Write the prose.** Three to six sentences after each table, covering the sample in plain terms, the two or three descriptive facts that matter for the argument, and the answer to anything a reader would otherwise stop and ask. Numbers in the prose match the table to the same decimals and the table is named. The rule for what to include: a fact goes in the prose if a later section depends on it, and nowhere else. Reciting the table row by row is the most common padding in an empirical paper.

10. **Generate everything from stored results and save the script beside the output.** Never transcribe from a results window and never edit an exported table by hand. A hand edit is lost on the next regeneration or, worse, survives into the submitted file with a number from a previous version. The check: delete the output file, rerun the script, and confirm the table comes back identical.

11. **Run the cross-table consistency check before delivery.** The N in Table 1, the N in the main results table, and the N stated in the text are the same number, or the difference is explained in a sentence. The treated share in Table 1 matches the number of treated units in the design description. The mean of the outcome in Table 1 is consistent with the comparison-group mean reported in the results table. This takes five minutes and catches the errors that referees find first.

## The three standard exhibits

**The sample construction table.** Restrictions in order, with counts. It answers the question referees ask most often about samples, which is where the sample came from, and it prevents the follow-up question about whether a restriction was applied for a reason related to the outcome. In panel data it carries both observations and units, because those fall for different reasons and a table showing only observations hides the difference between dropping years and dropping units. This exhibit belongs in the data section or the appendix and is generated from the cleaning log.

**Summary statistics, conventionally Table 1.** Variables in rows under block headers, statistics in columns, on the estimation sample. Its job is to let a reader judge whether the sample is what the text describes, whether the outcome varies enough to be studied, and whether the magnitudes in the results section are large or small relative to the variable's own dispersion. That last function is why the standard deviation of the outcome is not optional: without it, an estimate of 1.8 percentage points cannot be interpreted by anyone.

**The balance or comparison table.** Means by group, the difference, a normalised difference, and a test where the venue expects one. Its job is to show whether the groups being compared are similar on things that were fixed before treatment, and, where they are not, to make the reader's concern precise enough for the identification section to answer.

## What goes in a balance table, by design

**Difference-in-differences.** Balance in pre-period levels is informative context and is not the identifying assumption. Groups can differ in levels and still have parallel trends; groups can match in levels and diverge. Report pre-period levels for transparency, and say explicitly in the text that the design does not require level balance. The relevant check is on pre-treatment trends and it belongs in the identification exhibit, not here, which `identification-defense` and `econometric-model-writer` govern.

**Staggered adoption.** Compare cohorts, not just treated against never-treated. A table with a column per adoption wave plus the never-treated is more informative and often reveals the selection story: the early adopters differ systematically, which is exactly the fact the identification section has to address.

**Instrumental variables.** Balance is on the instrument, not on the treatment. Compare units by high and low instrument values, or above and below its median, and show that the covariates a referee would worry about do not differ. Balance on treatment status in an instrumental variables paper is a table that answers no question the design raises.

**Regression discontinuity.** Balance is at the cutoff, estimated within the bandwidth actually used, and ideally as a discontinuity estimate for each covariate rather than a comparison of means across the whole sample. Report the bandwidth in the note. A full-sample comparison of units above and below the cutoff will show enormous differences and means nothing, because the running variable differs by construction.

**Matching and reweighting.** Two panels or two column pairs: before and after adjustment, with normalised differences in both. The after panel is the one that matters, and showing only it hides how much work the adjustment did.

**Randomised or as-good-as-random assignment.** A conventional balance table with a joint test of orthogonality, and honesty about multiple testing: with twenty covariates, one significant difference at the five percent level is expected.

## Formatting

The typography is governed entirely by `academic-tables-booktabs` and this skill defers to it: three horizontal rules, no vertical lines, no shading, decimal-aligned numbers, consistent decimals within a column, and a note that makes the table self-contained. What this skill adds are the content requirements specific to descriptives.

Units appear in the variable label or in the note, always, for every variable. A row labelled "Size" with a mean of 340 is uninterpretable and referees will ask.

Block headers group variables into outcomes, treatment, and covariate blocks, set in italics or small capitals rather than as a separate rule, so the table's structure is visible at a glance.

The note states the sample, the period, the source, the unit of observation, the weighting, and the definition of any abbreviation. For a balance table it also states the test, the clustering if any, and what the normalised difference is.

Decimals are chosen once per column and applied consistently. Shares near zero take three decimals; monetary values take zero or use thousands with a stated unit. Never report a mean to four decimals because the software did.

## Generation

The exhibits are produced by a script that reads the analysis file and writes the table file, saved with the project so that a change in the sample regenerates them.

In Stata, summary statistics and balance tables are built from posted estimates rather than by transcription:

```stata
* Table 1: summary statistics on the estimation sample
use "$data/analysis.dta", clear
quietly reghdfe outcome treat $controls, absorb(unit year) cluster(region)
gen byte insample = e(sample)

label var outcome  "New employer firm registrations (count)"
label var treat    "Rollout in place (=1)"
label var pop_k    "Population (thousands)"
label var infra    "Infrastructure readiness score (0 to 100)"

estpost summarize outcome treat pop_k infra if insample, detail
esttab using "$tab/tab1_summary.tex", replace booktabs ///
    cells("mean(fmt(2)) sd(fmt(2)) p50(fmt(2)) min(fmt(2)) max(fmt(2)) count(fmt(%9.0gc))") ///
    label nonumber nomtitle collabels("Mean" "SD" "Median" "Min" "Max" "N") ///
    addnote("Estimation sample. Municipality-year observations, 2012 to 2022.")

* Balance by treatment cohort, with normalised differences
estpost ttest pop_k infra if insample, by(treat_ever)
esttab using "$tab/tab2_balance.tex", replace booktabs ///
    cells("mu_1(fmt(2)) mu_2(fmt(2)) b(fmt(2)) se(fmt(2)) p(fmt(3))") ///
    label collabels("Comparison" "Treated" "Difference" "SE" "p")
```

In Python, the same discipline applies and the table is written to file rather than displayed:

```python
import pandas as pd

df = pd.read_parquet("data/analysis.parquet")
sample = df.loc[df["insample"] == 1]

labels = {
    "outcome": "New employer firm registrations (count)",
    "treat":   "Rollout in place (=1)",
    "pop_k":   "Population (thousands)",
    "infra":   "Infrastructure readiness score (0 to 100)",
}

stats = (sample[list(labels)]
         .agg(["mean", "std", "median", "min", "max", "count"])
         .T
         .rename(index=labels)
         .round({"mean": 2, "std": 2, "median": 2, "min": 2, "max": 2}))
stats["count"] = stats["count"].astype(int)

def normalised_difference(frame, var, group):
    a = frame.loc[frame[group] == 1, var]
    b = frame.loc[frame[group] == 0, var]
    pooled = ((a.var(ddof=1) + b.var(ddof=1)) / 2) ** 0.5
    return (a.mean() - b.mean()) / pooled

stats.to_latex("tables/tab1_summary.tex", escape=False, column_format="lrrrrrr")
```

The rule that matters more than the choice of tool: the script writes the file, the document includes the file, and no human types a number in between.

## Worked example

**Situation.** Dr Aiko Tanabe was assembling the descriptive exhibits for a paper on a regional training voucher scheme, three weeks before a submission deadline. The analysis was finished: a difference-in-differences design across 1,204 firms observed annually from 2015 to 2022, with an estimated effect on retained employment of 3.1 percent and a standard error of 1.2. Table 1 had been built eight months earlier, when the data was first cleaned.

**Task.** Three exhibits, a page of prose, and confidence that a referee comparing them would find nothing to query.

**Action.** Step 1 was run first, out of habit rather than suspicion, and it immediately produced the problem. The construction table showed 9,632 firm-year observations after cleaning. The main regression reported 8,146. The gap of 1,486 observations had never been examined by anyone.

Tracing it took an afternoon. Three causes. The largest, 981 observations, was listwise deletion on a covariate for sector-level capital intensity, which was missing for firms in two sectors entirely. The second, 402 observations, came from the requirement of at least three pre-treatment years, applied inside the estimation script rather than in the cleaning script and therefore absent from the construction table. The third, 103 observations, was firms that entered after 2019 and had no pre-period at all.

None of these were wrong. All three were defensible restrictions. But the first meant that two sectors, together nine percent of the raw sample, were absent from the analysis and the paper described its sample as covering all sectors. That sentence was false, and it would have been false in print.

The wrong turn cost two days. Aiko's first balance table compared treated and comparison firms on fourteen covariates across the full 9,632 observations, with a t-test column. Every covariate but two showed p below 0.01. The table was two-thirds of a page and communicated nothing, because with that many firm-years any difference is significant, and because it was built on the wrong sample anyway. It was abandoned.

The replacement did three things differently. It conditioned on the estimation sample flag from step 2. It reported pre-period means only, for 2015 to 2017, since the design compares changes rather than levels. And it replaced the p-value column with a normalised difference column, keeping the p-values in a final column because the target journal's recent papers showed them. Under normalised differences the picture became readable: eleven of fourteen covariates were under 0.10, which is unremarkable, and three were above 0.25. Those three were firm age, prior training expenditure, and a metropolitan indicator, and all three ran in the same direction: firms taking up vouchers were younger, already trained more, and were disproportionately urban.

That was a finding, not a formatting problem, and it changed the identification section. The text now said, in two sentences, that treated firms differ in levels on three characteristics, that the design does not require level balance, and that the concern is whether those characteristics predict differential employment trends, which is answered by the event study in Figure 2 and by a specification interacting each of the three with year effects in Table 5 column 4.

The construction table was rebuilt with all restrictions in order, including the two that had been living inside the estimation script. Table 1 was regenerated on the estimation sample. Two numbers in the data section moved: the mean firm size fell from 41.2 to 38.7 employees once the two missing-covariate sectors were excluded, and the treated share rose from 0.34 to 0.36.

**Result.** Three exhibits and five sentences of prose. N was 8,146 in the construction table's final row, in Table 1, in the results table, and in the text. The sample description changed from "firms across all sectors" to "firms in sectors for which capital intensity is reported, covering 91 percent of firms in the raw extract", with the excluded sectors named in the note.

The whole pass took four days, two of them on the abandoned balance table. One referee report commented that the sample construction was unusually clear. Neither referee queried a count.

### A second scenario, where it goes differently

The same author, a regression discontinuity paper using a firm-size threshold that triggers a reporting obligation, with 26,000 firms in the raw data and an optimal bandwidth retaining 3,180.

Here almost every rule above changes its application. Table 1 is reported twice: once for the full sample, so a reader can see what population the study sits in, and once for the bandwidth sample, which is what the estimate actually describes. The two are labelled clearly and the second is the one the results section refers to.

The balance table is not a comparison of means above and below the threshold, which would show enormous and meaningless differences driven by the running variable itself. It is a set of discontinuity estimates, one per covariate, using the same bandwidth, kernel and polynomial as the main specification, reported with their standard errors. The note states the bandwidth. Alongside it sits the density test.

And the sample construction table gains a row it would not otherwise have: the bandwidth restriction, which cut the sample from 26,000 to 3,180, an 88 percent reduction that would look alarming in a difference-in-differences paper and is entirely expected here. That row carries a note saying the bandwidth was selected by a stated data-driven procedure rather than chosen.

What changed is that the estimand is local, so the descriptive exhibits have to describe two populations rather than one, and the balance evidence has to be estimated with the same machinery as the effect rather than compared with a t-test. A generic Table 1 in this paper would have been actively misleading about who the results apply to.

## Output

**Sample construction table:**

| Step | Restriction | Observations | Dropped | Firms | Firms dropped |
| 0 | Raw registry extract, 2015 to 2022 | 12,880 | | 1,610 | |
| 1 | Drop firms with no employment record | 11,204 | 1,676 | 1,401 | 209 |
| 2 | Drop sectors without capital intensity | 10,223 | 981 | 1,278 | 123 |
| 3 | Require three pre-treatment years | 9,821 | 402 | 1,228 | 50 |
| 4 | Drop entrants after 2019 | 9,718 | 103 | 1,215 | 13 |
| 5 | Non-missing outcome and controls | 8,146 | 1,572 | 1,204 | 11 |
| | Analysis sample | 8,146 | | 1,204 | |

**Summary statistics:**

| | Mean | SD | Median | Min | Max | N |
| Outcomes | | | | | | |
| Retained employment (count) | 38.7 | 51.2 | 21.0 | 1 | 604 | 8,146 |
| Log retained employment | 3.09 | 1.02 | 3.04 | 0.00 | 6.40 | 8,146 |
| Treatment | | | | | | |
| Voucher received (=1) | 0.36 | 0.48 | | 0 | 1 | 8,146 |
| Covariates | | | | | | |
| Firm age (years) | 14.2 | 9.8 | 12.0 | 1 | 71 | 8,146 |

**Balance table, pre-period levels:**

| | Comparison | Treated | Difference | Normalised diff. | p |
| Firm age (years) | 15.9 | 11.1 | 4.8 | 0.49 | 0.000 |
| Prior training spend (thousands) | 2.1 | 4.6 | 2.5 | 0.31 | 0.000 |
| Metropolitan location (=1) | 0.41 | 0.58 | 0.17 | 0.35 | 0.000 |
| Capital intensity | 0.62 | 0.65 | 0.03 | 0.06 | 0.041 |

Note states: pre-period means, 2015 to 2017, estimation sample, 1,204 firms. Normalised difference is the difference in means over the pooled standard deviation. The design does not require level balance; pre-treatment trends are shown in Figure 2.

## Failure modes

**Table 1 on a different sample from Table 2.** The defining failure of this skill. Recognisable by comparing the two Ns, which takes four seconds and is the first thing an attentive referee does. Fix with the estimation sample flag in step 2.

**P-values on covariate differences in a large sample.** Everything significant, nothing learned. Recognisable when the p column is all zeros. Fix by reading and reporting normalised differences.

**Imbalance presented and not discussed.** The table shows three covariates differing sharply and the text moves on. Referees read this as either not noticing or hoping. Fix with one sentence naming the imbalance and what the design does about it.

**A generic balance table in a design that does not need one.** Level balance in a difference-in-differences paper, treatment balance in an instrumental variables paper, whole-sample balance in a regression discontinuity paper. Recognisable by asking what question the table answers and finding that the design does not raise it. Fix by using the design-specific version.

**Minimums and maximums on binary variables.** Six columns to say a dummy is zero or one. Fix by suppressing them and noting that binary variables report the mean as a share.

**Variables without units.** A mean of 340 with no indication of what it counts. Fix in the label, not in the text.

**Hand-edited exported tables.** A label fixed in the output file, then the analysis changes and either the fix is lost or the stale file is submitted. Recognisable because the table cannot be regenerated identically. Fix by deleting the output and rerunning as a routine check.

**Prose that recites the table.** Twelve sentences repeating numbers the reader can see. Fix by keeping only the facts a later section depends on.

**Different Ns per variable, unexplained.** Fix with a column or a note; where listwise deletion is doing it, that belongs in the construction table as its own step.

**Twenty-five variables in the body because they were all in the data.** Fix by moving anything that never enters a specification to the appendix.

## Edge cases

**Restricted-access data with disclosure rules.** Minimum cell sizes, no minimums or maximums that could identify a unit, and rounding requirements. Build the table to the rules from the start rather than redacting afterwards, and state in the note that the statistics are disclosure-controlled and how. `research-ethics-and-data-protection` covers the obligations.

**Survey data with complex weights.** Report weighted means with the weight named, and report the unweighted N alongside the weighted total, because a reader needs both. Never report a weighted N as though it were a sample size.

**Panel data.** Report both observations and units in every count, and state whether the panel is balanced. Where it is not, report the mean and range of observations per unit, because an unbalanced panel where the average unit is seen twice supports very different inference from one where it is seen eight times.

**Time-varying treatment.** The share treated is not a single number. Report the share ever treated, the share treated in the final year, and the distribution of adoption timing, which is usually clearer as a small figure than as a table.

**Very small samples.** Under roughly fifty units, report the individual units where confidentiality allows, or a full distribution rather than a mean and a standard deviation. Summary statistics on twelve observations conceal more than they show.

**A variable with extreme outliers that are real.** Do not winsorise silently to make the table look tidy. Report the raw statistics, report the model's transformation separately, and say in the note what the maximum is and whether it was verified.

**Multiple analysis samples.** A main sample and a heterogeneity subsample, or several outcomes with different coverage. Report Table 1 for the main sample, and a compact appendix table with the columns per sample. Do not average across them.

**The paper has no natural treatment group.** For a purely descriptive or predictive paper, replace the balance table with a comparison across the dimension the paper actually uses: quantiles of the key regressor, periods, or regions.

## Quality bar

- The Table 1 sample is the estimation sample, produced by the estimation's own sample flag, and the N matches the results table and the text.
- Every restriction from raw data to analysis sample appears in the construction table, in order, with counts of both observations and units.
- Every variable carries units and a definition, and binary variables are reported as shares.
- The balance exhibit is the one the design requires, and its note states the comparison, the sample, and the bandwidth or period where relevant.
- Where covariates are imbalanced, the text says so, by how much in normalised terms, and what the design does about it.
- Every table was written to file by a script, and deleting the file and rerunning reproduces it exactly.
- The prose reports only the facts a later section depends on, at the same precision as the table, naming the table.
- Every table is readable without the surrounding text.

## Related skills

`data-profiling-and-cleaning` decides the restrictions and produces the log this skill turns into the construction table, and `stata-data-management` implements them in Stata. `academic-tables-booktabs` governs the typography, rules and notes of every exhibit here and takes precedence on presentation. `regression-table-production` builds the estimation tables these descriptives must reconcile with, and `econometrician` sets the specification whose sample flag step 2 depends on. `academic-figures-monochrome` takes over when a distribution or an adoption-timing pattern reads better as a figure than as a table. `data-section-writer` writes the section these exhibits sit inside, and `identification-defense` owns the pre-trend and continuity evidence that a balance table deliberately does not carry. `analysis-audit` checks from the outside that the counts in these tables match the code that produced them.
