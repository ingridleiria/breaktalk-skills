---
name: academic-tables-booktabs
description: Formats regression tables, summary statistics, balance tables, and any academic exhibit to journal standard in the booktabs convention (three horizontal rules, no vertical lines, aligned numbers, standard errors beneath estimates, complete notes), in Word, LaTeX, or Markdown, generated from stored estimates rather than typed. Use this skill whenever a researcher asks to make or format a regression table, "clean up this table", "journal-style table", "Table 2 for the paper", convert Stata or R output into a table, or build any table for a thesis, article, or referee response. Trigger for every table that will appear in an academic document.
---

# Academic Tables, Booktabs

A well-formatted table is invisible: the reader sees the numbers and the structure, never the formatting. The booktabs convention exists because it achieves that, and because journals in economics, education, and management expect it. This skill applies it consistently and generates tables from code so they never drift from the results.

## The rules

1. **Three horizontal rules only**: a heavier rule above the header, a lighter rule below the header, a heavier rule at the bottom. Additional thin rules may separate panels or the coefficient block from the statistics block. No vertical lines, ever. No cell borders, no shading, no zebra stripes.
2. **Columns are specifications or groups**, numbered in parentheses in the header, with the dependent variable named above the numbers (once, spanning, if all columns share it).
3. **Rows are variables**, labeled in words the reader understands (not variable names from the code), with units where relevant.
4. **Standard errors in parentheses directly beneath each estimate**, same decimals. Significance stars, if used, on the estimate, with the convention stated in the note. Prefer reporting standard errors and letting the reader judge; if the venue expects stars, use them consistently.
5. **Numbers right-aligned or decimal-aligned**, consistent decimals within a column (three for coefficients near zero, two otherwise), thousands separators for N.
6. **Bottom block**: fixed effects included (Yes/No rows), controls, number of observations, number of clusters, R-squared or an appropriate fit statistic, and the mean of the dependent variable in the comparison group, which makes magnitudes interpretable.
7. **Notes below the table**: sample, years, estimator, clustering level, definitions of any abbreviation, significance convention, and data source. The note makes the table self-contained.
8. **Title above the table** stating what the table shows, not "Results": "Effect of X on Y, panel fixed effects estimates".

## Structure by table type

- **Main results**: build-up across columns from sparse to full specification; the coefficient of interest first among rows; controls collapsed into a Yes/No row unless a control's coefficient is itself of interest.
- **Heterogeneity**: columns by subgroup or an interaction block, with the subgroup means in the bottom block.
- **Robustness**: rows or columns by alternative, each labeled by what changed, with the baseline reproduced in the first column for comparison.
- **Summary statistics and balance**: follow the descriptive-statistics-tables skill; same rule set.
- **Multi-panel tables**: panels labeled A, B, C, with a short subtitle each and a thin rule between them, sharing the column header.

## Generation, by environment

- **Stata**: estimates stored with `estimates store`, tables built with `esttab` (or `estout`) to `.rtf` or `.docx` for Word and `.tex` with `booktabs` for LaTeX, with labels, statistics, and notes specified in the command. Never copy from the results window.
- **R**: `modelsummary` or `stargazer` with booktabs output, labels mapped from a named vector.
- **Python**: `statsmodels` summary converted through a documented function to Markdown or LaTeX.
- **Word documents**: when a table must be built directly in Word (through the environment's document skill), apply the rules above: top and bottom borders on the table, a single border under the header row, no other borders, numbers right-aligned, notes in a smaller font below.

The script that produced each table is saved with the project; a change in the sample regenerates the table.

## Checks before delivery

- Every number in the table matches the stored estimate to the stated decimals.
- Column numbers, dependent variable, and fixed effects rows are present.
- N and clusters reported; the comparison-group mean reported.
- The note defines every abbreviation and states the clustering.
- No vertical lines, no cell shading, no more than three main rules plus panel separators.

## Quality bar

- The table is readable without the surrounding text.
- A referee can identify the specification of each column from the table alone.
- The formatting is identical across every table in the document.
