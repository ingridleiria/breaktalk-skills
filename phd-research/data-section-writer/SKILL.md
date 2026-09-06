---
name: data-section-writer
description: Writes the data section of an empirical paper, thesis chapter, or proposal: sources and access route, the sample construction chain with counts at every step, variable definitions and units, how treatment and outcome are measured and by whom, descriptive statistics prose, missingness and attrition, and the data availability statement. Use this skill whenever a researcher asks to write or fix the data section, describe the sample, document variable definitions, explain where the data come from, report attrition or missing data, or write a data availability statement; and whenever a methods section starts estimating before the data have been described. Trigger for the data section of every empirical paper.
---

# Data Section Writer

The data section answers the questions a careful reader asks before believing any estimate: where did these observations come from, who measured the variables and how, what was dropped and why, and could someone else assemble the same sample. It is documentation written as prose, and its standard is reproducibility.

## Structure

Write in prose, with one or two tables, in this order:

1. **Sources.** Each dataset named with its producer, the years covered, the unit of observation, and how it was accessed (public download, restricted access agreement, request to the agency, purchased). For administrative data, name the register and the responsible institution. For surveys, the survey name, sampling design, and response rate where published. Cite the data documentation as a source.
2. **Linkage.** How datasets were merged: the identifier, the match rate, and what happened to unmatched observations. A merge that drops observations is reported with counts.
3. **Sample construction.** The chain from raw observations to the analysis sample, each restriction stated with its rationale and the count after it, mirrored in a table (see descriptive-statistics-tables and data-profiling-and-cleaning). Restrictions driven by data availability are stated as such, without a reassuring clause; "only 15 of 20 countries have the variable in all years" is complete on its own.
4. **Treatment.** Exactly how treatment is defined and measured: the source of the treatment indicator, the timing rule (when is a unit considered treated), and who recorded it. For policy treatments, the legal or administrative definition and any discrepancy between formal adoption and implementation.
5. **Outcome.** How the outcome is measured, by whom, at what frequency, with what scale, and its known limitations (test coverage, self-report, administrative lag). If the outcome is standardized or transformed, the transformation and the reference group.
6. **Covariates.** Definitions and sources, grouped, briefly; the full list with units goes in an appendix table.
7. **Descriptive statistics.** Three to six sentences reporting the sample in plain terms and the two or three descriptive facts the reader needs, with numbers identical to the table.
8. **Missing data and attrition.** Rates, patterns, and treatment (listwise deletion, imputation with method stated, or a missingness indicator). For panels, how many units are observed in every period, entry and exit, and whether attrition correlates with treatment.
9. **Data availability statement.** Where the data can be obtained, under what conditions, and where the code is deposited (see replication-package).

## Writing rules

- Every dataset, register, survey, and agency named specifically and cited.
- Counts and years in every paragraph that describes the sample.
- Units at first use of every variable.
- Impersonal or first person plural per the field; consistent with the rest of the paper.
- Limitations stated without softening; the discussion section will address consequences.
- No results in the data section. Descriptive facts yes; estimates no.

## Special cases

- **Restricted or proprietary data**: describe the access route precisely and what a replicator would need to do; state what cannot be shared.
- **Constructed panels from multiple releases**: document harmonization of variables that changed definition across years, with the years of each definition.
- **Text or scraped data**: collection dates, the scraping procedure, deduplication, and the share of the target population captured.
- **Survey data**: weights used and why, and whether estimates change without them.

## Quality bar

- A reader could request the same data and apply the same restrictions to reach the same N.
- Treatment and outcome measurement are described precisely enough to evaluate measurement error.
- Every count in the prose matches the sample construction table.
- The availability statement says where data and code live.
