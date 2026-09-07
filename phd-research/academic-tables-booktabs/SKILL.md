---
name: academic-tables-booktabs
description: Sets the typography and document form of every table in an academic paper, thesis or referee response, in the booktabs convention: three horizontal rules and no vertical lines, decimal-aligned numbers with consistent precision per column, spanning headers with partial rules, panel structure, a caption above the table and a self-contained note beneath it, and floats that behave. Covers the LaTeX implementation with booktabs, siunitx and threeparttable, the equivalent discipline in Word and RTF, Markdown for drafts, and the rule that a table is written to file by a script and never edited by hand. Use this skill whenever a table has to be formatted or fixed for an academic document, when someone asks for a journal-style table, says a table is too wide or will not fit, has tables that look different from each other, needs Stata or R output turned into document form, or asks how to align numbers, where the note goes, or whether to use vertical lines. Trigger also on vague requests such as "clean up this table", "make this look like a real paper", or "my table is broken in LaTeX".
---

# Academic Tables, Booktabs

A well-set table is invisible. The reader sees the numbers and the structure and never notices the formatting, which is exactly the point: attention spent decoding a table is attention not spent on the result. The booktabs convention exists because it achieves that with a small number of rules, and because economics, finance, management and most quantitative social science journals expect it, which means a table set any other way signals inexperience before a single number is read. The main exception is the APA Publication Manual, which governs psychology, much of education and several neighbouring fields and specifies its own table format; the section below sets out exactly where the two standards diverge, and everything else in this file applies to both.

The failure this prevents is a document whose tables were each formatted at the moment they were needed, by whichever tool made them, and never reconciled. Table 1 has vertical lines because it came out of a spreadsheet. Table 3 is in a smaller font because it was too wide and got squeezed. Table 4 has three decimal places in one column and two in the next, and its note is a sentence fragment that does not say what the standard errors are clustered on. None of these are errors of substance. All of them are visible on the first page turn, and together they tell a referee that the author did not read their own document as a document.

The second failure is mechanical and expensive: a table that was exported by a script and then improved by hand. A label corrected, a column width adjusted, a stray row deleted. From that moment the table and the analysis are two separate objects that happen to agree today. When the specification changes, either the hand fix is lost and reappears as a defect, or the hand-fixed file is the one that goes to the journal, carrying numbers from a version of the analysis that no longer exists.

## When to use this, and when not to

Use it for the form of any table in an academic document: summary statistics, balance, main results, robustness, heterogeneity, variable definitions, sample construction, appendix tables, and tables in a referee response letter. Use it when tables from several sources have to be brought to one appearance, when a table will not fit the page, when the document is being converted between LaTeX and Word, and at the start of a project to fix the conventions before twenty tables exist.

The boundary with the adjacent skill is precise and worth stating, because these two are done in sequence and confusing them wastes effort.

`regression-table-production` produces the estimation table itself from stored estimates: which specifications become which columns, what belongs in the bottom block, which R-squared variant is reported, whether stars or confidence intervals are shown, and what the note has to say about the estimator and the clustering. That is a question of content and of pipeline.

This skill, `academic-tables-booktabs`, governs the typography and the document form of the result: the rules, the alignment, the spanning headers, the panel structure, the caption and note placement, the float behaviour, and the LaTeX or Word implementation. It takes precedence on presentation and defers on content.

`descriptive-statistics-tables` is the equivalent content skill for summary and balance exhibits, and follows this skill for their appearance.

Do not use this skill to decide what a table should contain, which of those two skills owns, or to decide between a table and a figure, which `academic-figures-monochrome` covers: a figure when the reader needs a shape, a table when they need exact numbers.

## What you need before starting

**The table's numbers, in a file written by a script.** Not in a screenshot and not in a results window. Missing: go back to the estimation or summary script and have it export. Retyping is how a transposed digit enters a paper, and hand-typed tables cannot pass the regeneration check in the quality bar.

**The document class and the compilation route.** LaTeX with pdflatex, LuaLaTeX or XeLaTeX, a journal class file, a Word template, or Markdown into something else. Missing: assume LaTeX with a standard article class and say so, because the packages available determine what is implementable.

**The journal or institution's table requirements.** Some house styles mandate a caption position, a font size, a note format, or forbid a package. Thesis regulations often specify caption placement and numbering. Missing: use the conventions here, which are the general social-science standard, and check before submission rather than after. `journal-targeting` resolves this properly.

**The page geometry.** Text width, single or double column, portrait or landscape allowed. This determines how many columns can fit before something has to give. Missing: assume a single-column article with about 15 cm of text width.

**The table's content decisions, already made.** Which columns, which rows, what the bottom block holds, whether stars are used. Missing: this skill will format whatever it is given, which is the wrong order. Send it back to `regression-table-production` or `descriptive-statistics-tables` first, because reformatting after a content change is wasted work.

**Whether the table will also appear in slides or a response letter.** Missing: assume the document only, and keep the script parameterised enough that a second output format is one argument rather than a rebuild.

## The method

1. **Inventory before formatting anything, whenever there is more than one table.** List every table with its source, whether a generating script exists, whether its numbers trace to an output file, and its width in columns. This takes an hour for twenty tables and it is what surfaces the tables that cannot be regenerated, which are the ones that matter. The rule: any table whose numbers cannot be traced to an output file is rebuilt from the analysis or removed, never restyled.

2. **Confirm the content is settled before touching the form.** Which columns, which rows, what the bottom block holds, stars or intervals. Formatting a table whose specification is still moving is work done twice. Where the content is not settled, send it back to `regression-table-production` or `descriptive-statistics-tables` and format nothing.

3. **Fix the conventions once, for the whole document, before the individual tables.** One preamble block with the packages and the numeric setup, one wrapper snippet for the float and the note, one note template, one decimal policy. Decisions made per table drift; decisions made once do not. This is the step that separates a document with consistent tables from a document with twenty individually reasonable ones.

4. **Set the column structure and the alignment.** One column specification per table, with numeric columns declared to a fixed number of integer and decimal digits so that alignment is enforced by the typesetter rather than by luck. The judgement here is the precision, and the rule is one precision per column, chosen from the magnitude of the numbers in it: three decimals where coefficients sit near zero, two otherwise, none for counts, with a thousands separator on counts.

5. **Build the header.** Column numbers in parentheses on their own row, the dependent variable named above them by a spanning header with a trimmed partial rule where every column shares it, and separate spanning headers where the columns fall into groups. Where more than two levels of header are needed, the table is doing too much and should be split.

6. **Set the body rows.** Labels in words with units, the coefficient of interest first, uncertainty directly beneath each estimate in parentheses at the same precision, and vertical space added between variable blocks with a proper spacing command rather than empty rows.

7. **Build the bottom block below a thin rule.** Indicator rows for each set of fixed effects and each control block, observations, clusters, the fit statistic appropriate to the estimator, and the comparison-group mean of the dependent variable where magnitudes need anchoring.

8. **Write the caption and the note from the template.** Caption above, in sentence form, with a label for cross-referencing. Note below, covering sample and period, unit of observation, estimator, what is in the parentheses and at what clustering level with the cluster count, every abbreviation, the significance convention if stars are used, and the source. The test to apply before moving on: cover the body text and read the table; anything unanswerable goes in the note.

9. **Resolve width by the escalation list, never by scaling.** Work down the list in the section below in order, because the first four steps cost nothing and the last two cost readability. Scaling the type to fit is not on the list at all, for the reason given there.

10. **Wire the generation so the script owns the numbers and the document owns the presentation.** The estimation script writes a fragment containing only the tabular content; the document supplies the float, the caption, the note and the wrapper. Then run the check: delete the fragment, rerun the script, and confirm the document compiles to the same table. A table that fails this check has a hand edit in it somewhere.

11. **Run a consistency pass across the document at the end.** Read the tables consecutively, ignoring their content, looking only for differences in font size, decimal policy, note structure, caption style and header conventions. This is the pass nobody runs and the examiner always does, and it takes twenty minutes.

## The rules

These are the standard the method applies, stated once in full.

1. **Three horizontal rules and no vertical lines, ever.** A heavier rule above the header, a lighter rule below the header, a heavier rule at the bottom. Partial rules under spanning headers and thin rules between panels are permitted and are part of the convention. Vertical lines, cell borders, box frames, shading and zebra striping are not, in any table, in any document. Whitespace separates columns; that is what the wider column spacing in the convention is for.

2. **Caption above the table, note below it.** The caption is a sentence naming what the table shows, not a label: "Effect of rollout on employment, panel fixed effects estimates" rather than "Results". The note sits under the bottom rule, in a smaller size, at the width of the table.

3. **Columns are specifications or groups**, numbered in parentheses in a header row, with the dependent variable named above them by a spanning header where all columns share it.

4. **Rows are variables in words the reader understands**, never variable names from the code, with units where the unit is not obvious.

5. **Numbers are decimal-aligned within a column, with one precision per column.** Three decimals for coefficients near zero, two otherwise, and thousands separators for counts. A column where some entries have two decimals and some have three is the most visible formatting defect in an otherwise good table.

6. **Uncertainty sits directly beneath its estimate, in parentheses, at the same precision.** What is in the parentheses is stated in the note, and it is stated as what it actually is: cluster-robust standard errors, heteroskedasticity-robust standard errors, or a confidence interval.

7. **The bottom block is separated by a thin rule** and carries the indicator rows for fixed effects and control blocks, the number of observations, the number of clusters, the fit statistic, and, where it aids interpretation, the mean of the dependent variable in the comparison group.

8. **The note makes the table self-contained.** Sample, period, unit of observation, estimator, what is in the parentheses and at what clustering level, the significance convention if stars are used, the definition of every abbreviation appearing in the table, and the data source. The test: cover the body text and read the table; anything you cannot answer belongs in the note.

9. **The table is written to file by a script and included, never pasted and never edited.** In LaTeX this means the document contains an input command and the table file is generated output. In Word it means a documented export step, repeated when the analysis changes.

10. **Every table in the document follows the same conventions.** Same font size, same decimal policy, same note structure, same caption style. Inconsistency across tables is more noticeable than any single table's imperfection.

## LaTeX implementation

The packages that do the work, and what each is for:

```latex
\usepackage{booktabs}        % toprule, midrule, bottomrule, cmidrule
\usepackage{siunitx}         % S columns: decimal alignment, fixed precision
\usepackage{threeparttable}  % note set to the table's own width
\usepackage{caption}         % caption spacing and single-line handling
\usepackage{rotating}        % sidewaystable, for a genuinely wide table
\usepackage{longtable}       % tables that must break across pages
\sisetup{
  detect-all,                       % inherit the surrounding font
  table-align-text-after = false,
  input-symbols          = {()*},   % do not choke on stars and parentheses
  group-digits           = integer,
  group-separator        = {,}
}
```

A results table with the full structure, spanning header, panels, bottom block and a threeparttable note:

```latex
\begin{table}[htbp]
\centering
\caption{Effect of rollout on employer firm registrations}
\label{tab:main}
\begin{threeparttable}
\begin{tabular}{l S[table-format=1.3] S[table-format=1.3] S[table-format=1.3] S[table-format=1.3]}
\toprule
 & \multicolumn{4}{c}{Log employer firm registrations} \\
\cmidrule(lr){2-5}
 & {(1)} & {(2)} & {(3)} & {(4)} \\
\midrule
\addlinespace
Rollout in place            & 0.041 & 0.038 & 0.031 & 0.029 \\
                            & (0.014) & (0.013) & (0.012) & (0.014) \\
\addlinespace
Population (log)            &       & 0.212 & 0.198 & 0.201 \\
                            &       & (0.061) & (0.058) & (0.060) \\
\addlinespace
\midrule
Municipality fixed effects  & {Yes} & {Yes} & {Yes} & {Yes} \\
Year fixed effects          & {Yes} & {Yes} & {Yes} & {Yes} \\
Region-specific trends      & {No}  & {No}  & {Yes} & {Yes} \\
Baseline controls           & {No}  & {Yes} & {Yes} & {Yes} \\
\addlinespace
Observations                & {20{,}262} & {20{,}262} & {20{,}262} & {19{,}104} \\
Municipalities              & {1{,}842}  & {1{,}842}  & {1{,}842}  & {1{,}736} \\
Mean of dep.\ var., control & 2.914 & 2.914 & 2.914 & 2.908 \\
Within \(R^{2}\)            & 0.081 & 0.104 & 0.119 & 0.121 \\
\bottomrule
\end{tabular}
\begin{tablenotes}[flushleft]\footnotesize
\item \textit{Notes:} Municipality-year observations, 2012 to 2022. Estimated by
ordinary least squares with municipality and year fixed effects. Cluster-robust
standard errors, clustered at the region level (17 clusters), in parentheses.
Column (4) excludes municipalities amalgamated in 2016. Baseline controls are
population, the share of the population aged 20 to 34, and the infrastructure
readiness score, each measured in 2012 and interacted with year indicators.
Source: national business registry.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

Three details in that block are the ones people get wrong. Text entries inside an `S` column must be wrapped in braces, which is why every "Yes", every column number and every count is braced; an unbraced word in an `S` column produces a compilation error whose message does not point at the cause. `\addlinespace` rather than an empty row is what creates vertical breathing space, because empty rows leave rule spacing wrong. And `\cmidrule(lr){2-5}` with the `(lr)` trims the rule so it does not run into the neighbouring columns, which is the difference between a partial rule that looks deliberate and one that looks like a mistake.

**Panels**, for several outcomes or samples sharing one column header:

```latex
\midrule
\multicolumn{5}{l}{\textit{Panel A. Employer firms}} \\
\addlinespace
Rollout in place & 0.041 & 0.038 & 0.031 & 0.029 \\
                 & (0.014) & (0.013) & (0.012) & (0.014) \\
\addlinespace
\multicolumn{5}{l}{\textit{Panel B. Sole traders}} \\
\addlinespace
Rollout in place & 0.008 & 0.006 & 0.004 & 0.005 \\
                 & (0.011) & (0.011) & (0.010) & (0.011) \\
\midrule
```

Panels share the header and the bottom block where the specifications are identical across panels; where they are not, each panel needs its own bottom block and the table is probably two tables.

**Generation from Stata**, which is where most of these tables come from:

```stata
eststo clear
eststo m1: reghdfe lnreg treat, absorb(muni year) cluster(region)
eststo m2: reghdfe lnreg treat $controls, absorb(muni year) cluster(region)

esttab m1 m2 using "$tab/tab3_main.tex", replace ///
    booktabs fragment nomtitles nonumbers ///
    b(3) se(3) label ///
    keep(treat lnpop) ///
    varlabels(treat "Rollout in place" lnpop "Population (log)") ///
    stats(N N_clust r2_within, fmt(%9.0gc %9.0gc 3) ///
          labels("Observations" "Regions" "Within \(R^{2}\)")) ///
    nonotes
```

Export with `fragment` and no notes, then wrap the fragment in the `table`, `threeparttable` and `caption` environment in the document. This is the arrangement that survives: the script owns the numbers, the document owns the presentation, and neither is edited to fix the other.

**Cross-referencing.** Every table gets a `\label` and is referred to as `Table~\ref{tab:main}` with a non-breaking space. Never write "the table above", which breaks the moment the float moves.

**Float behaviour.** Use `[htbp]` and let LaTeX place the table. Do not use `[H]` to force position; it produces enormous white gaps and fights the layout for the rest of the document. If tables are drifting far from their discussion, the usual cause is too many floats in a short stretch of text, and the fix is `\clearpage` at a section break rather than forcing each one.

## APA style tables, and where they conflict with this one

Booktabs is not the only standard and outside economics it is often not the expected one. Journals following the APA Publication Manual, which covers psychology, much of education, communication, nursing and a good deal of management, specify table format themselves, and a booktabs table submitted there will be sent back for reformatting. The two standards agree on more than they disagree on, and the disagreements are worth knowing precisely rather than discovering at proof stage.

What they agree on: horizontal rules only, no vertical lines, no shading, no cell borders. A rule above the column headings, a rule below them, a rule at the bottom, and no others except a short spanning rule under a column head that covers several columns. Numbers aligned on the decimal. One note structure serving the whole table. Tables generated rather than hand-formatted.

What differs, and each of these is a real reformatting job:

| Element | This file's booktabs convention | APA 7 |
| --- | --- | --- |
| Caption | One sentence above the table, in the caption style, sentence case | Two lines above the table: the table number in bold on its own line, then the title on the next line in italic title case |
| Note | One block below the rule, smaller size | Up to three blocks in order, each starting on a new line: a general note labelled `Note.` in italics, then specific notes keyed by superscript lowercase letters, then a probability note |
| Significance | Stars permitted, convention stated in the note | Stars deprecated. Report exact p values and confidence intervals; where stars are used they go in the probability note, and asterisk conventions differ from the economics one |
| Uncertainty | Standard error in parentheses under the estimate | Standard error in its own column, and a 95 percent confidence interval in its own column or as `[lower, upper]` |
| Leading zeros | `0.086` | No leading zero on a quantity that cannot exceed one: `p = .03`, `r = .41`, but `0.086` for a coefficient that can |
| Statistical symbols | Roman | Italic: *M*, *SD*, *N*, *n*, *p*, *t*, *F*, *r*, *b*, and Greek left roman |
| Bottom block | Fixed effects and control indicator rows, N, clusters, fit statistic | Usually only *N* and the fit statistic; indicator rows for control blocks are an economics habit and read as clutter |
| Row labels | Variables in words | Same, with the stub column left-aligned and levels of a factor indented under their heading |
| Spacing | Single | Double spacing throughout the table unless the journal says otherwise |
| Placement | Where the layout puts it | Often required after the references, one table per page, in submission manuscripts |

Producing APA tables from code, which matters as much here as it does for booktabs: in R, `apaTables` writes APA-formatted tables directly, `papaja::apa_table` does it inside an R Markdown or Quarto manuscript that renders to a full APA document, and `modelsummary` with a `flextable` or `gt` backend gives fine control over both standards from one set of stored estimates. In Python, `pandas.io.formats.style` plus `python-docx`, or writing to `.docx` through a template. In Stata, `estout` and `esttab` can be configured close to APA but not all the way, so the usual route is `esttab` to `.rtf` and a Word table style named for the journal. SPSS output should be exported and rebuilt, never pasted as a pivot table.

The rule that survives whichever standard applies: one convention chosen for the document, applied to every table in it, generated by a script, with a note that makes the table readable on its own. Choose the standard from the target's author guidelines and from three recent articles in it, and note the choice in the project README so that a coauthor does not reformat half the tables the other way.

## When a table will not fit

In order, and the order matters because the first four cost nothing and the last two cost readability:

1. **Remove columns that do not vary.** A control block that is identical across all columns belongs in the note, not as a row of identical Yes entries, and a specification that is dominated by another is often there out of sentiment.
2. **Move rows to an appendix.** Coefficients on controls that nobody will read take a third of many tables. Collapse them into an indicator row and put the full version in an appendix table.
3. **Reduce precision.** Three decimals where two suffice narrows every numeric column.
4. **Shorten the row labels.** "Share of the population aged 20 to 34" becomes "Population share, 20 to 34", with the full definition in the note.
5. **Rotate the table**, with `sidewaystable`. Acceptable in a thesis and in most journals, and much better than shrinking type.
6. **Scale the type**, using `\footnotesize` or `\scriptsize` for the whole table. Acceptable only if applied consistently to every table of that kind in the document, so that the reader does not meet four different table font sizes.

What is not on the list is `\resizebox`. It scales the type by an arbitrary factor determined by the table's width, which means every table gets a different effective font size, none of which match the document. It is the single most common cause of a thesis whose tables all look slightly wrong and whose author cannot say why. Where a table is so wide that only scaling will work, the table has too many columns and should be split.

## Word, RTF and Markdown

The convention is not a LaTeX feature and translates completely.

**In Word**, the same three rules are achieved with borders: a border above the header row and a border below it, a border at the bottom of the table, and no other borders anywhere. Set this once as a table style named for the project and apply it to every table, rather than formatting each one. Numbers are right-aligned, or decimal-aligned using a decimal tab stop in the cell, which is the part most authors do not know exists and is what makes a Word table look professional. The caption uses the Caption style above the table so that cross-references and the list of tables work. The note is a paragraph below the table in a smaller size, not a merged final row, because a merged row moves oddly when the table breaks across pages.

Export from Stata to `.rtf` with `esttab using "tab3.rtf"` and paste into the template, or use the environment's document tooling to write the table programmatically where that is available. Where the analysis is rerun, the export is rerun; the manual step is pasting, and it is the step to keep as small and as documented as possible.

**In Markdown**, for drafts, working notes and referee responses that will not be typeset, use a plain pipe table with a header row, no alignment decoration beyond what the target renders, units in the header, and the note as an italic line beneath. Markdown cannot do spanning headers or panels; where those are needed, the table has outgrown Markdown and belongs in the typeset document.

**Converting between the two.** Keep the generating script capable of writing both formats from one set of stored estimates rather than converting a finished table. Converting output is where labels drift and where the LaTeX and Word versions of a paper stop agreeing.

## Worked example

**Situation.** Daniel Okonkwo was assembling a thesis with nineteen tables, four weeks from deposit. The tables had accumulated over three years: seven exported from Stata as LaTeX fragments, five built in a spreadsheet and pasted as images, four typed directly into the document, and three inherited from a coauthored paper in that paper's format. The internal examiner's preliminary comment was that the document looked like several documents.

**Task.** Nineteen tables to one standard, all regenerable, within four weeks alongside the remaining writing.

**Action.** The inventory came first: every table listed with its source, whether a script existed, whether the numbers were traceable to an output file, and its width in columns. Nine had scripts. Five were images, which meant the numbers existed only as pixels and, for two of them, the underlying results file could not be found at all.

Those two were the real problem and they consumed the first week. One was a robustness table from an early chapter, and rerunning the specifications from the current data produced numbers that differed in the second decimal place for three of eight entries, because the sample had changed when a cleaning bug was fixed eighteen months earlier and that table had never been regenerated. The old table had been in three drafts and one departmental seminar. It was replaced with the current numbers, and the chapter's text needed two sentences changed because one coefficient had moved from significant at five percent to not significant.

The wrong turn cost three days. Daniel's first pass at the width problem was `\resizebox` on the six widest tables. Each compiled, each fitted, and the document then contained tables at six different effective font sizes ranging from roughly nine point down to about six and a half. Read on screen at 150 percent this was invisible. Printed, it was the most conspicuous thing about the document, and it made the smallest table's notes genuinely hard to read. He reverted all six.

The replacement followed the escalation list. Three tables lost a control block to an appendix, which removed four rows each. Two lost a specification column that was dominated by the neighbouring column and had been kept out of habit. The widest, a heterogeneity table with nine subgroup columns, was rotated with `sidewaystable`, which the thesis regulations permitted. Nothing was scaled, and every table ended at the document's body font size except the appendix tables, which were set at `\footnotesize` as a consistent class.

The mechanical part went faster than expected. One preamble block with the four packages and a `\sisetup`, one snippet for the table wrapper, and every Stata export switched to `fragment` output with the wrapper in the document. Column formats were standardised: `S[table-format=1.3]` for coefficients, `S[table-format=2.2]` for the descriptive tables' means, and braced text for every indicator row. Two compilation errors took an hour to diagnose between them, both the same cause: an unbraced "Yes" inside an `S` column, whose error message mentions nothing about braces or about siunitx.

The notes were rewritten last, from a template, so that all nineteen said the same kinds of things in the same order: sample and period, estimator, what is in parentheses and the clustering with the cluster count, abbreviations, source. Six of the original notes had not stated the clustering at all.

**Result.** Nineteen tables, one appearance, seventeen of them regenerated by scripts and two, the inherited coauthored ones, carried with a documented provenance note in the project record because the coauthor's data could not be rerun locally. Total time was eight working days, three of them the abandoned scaling attempt and five of them the inventory and the two lost tables.

The examiners raised no formatting point. The finding that mattered was the eighteen-month-old table whose numbers were stale, which surfaced only because the standard required regeneration from source and would otherwise have been deposited.

### A second scenario, where it goes differently

The same author, submitting a paper from the same thesis to a journal that accepts Word manuscripts only, with a template that specifies its own caption style and a reviewer-friendly line-numbered layout.

None of the LaTeX machinery is available and the standard is unchanged. The three rules become three borders applied through a single named table style, defined once and applied to all five tables, so that a later edit to the style changes all of them. Decimal alignment becomes a decimal tab stop set in the numeric columns, which takes two minutes per table and is the difference between a Word table that reads properly and one that does not. The threeparttable note becomes a paragraph in eight-point below the table, and, because Word will not keep it with the table automatically, the table and its note are placed in a single-cell borderless container so they cannot be separated by a page break.

Two things genuinely change rather than merely being reimplemented. Panels are harder, because Word has no clean way to set a panel label spanning the header, and the solution is a merged row with the panel title in italics, which is acceptable and slightly less tidy. And the generation pipeline gets one irreducible manual step: Stata writes RTF, and a human pastes it into the template. That step is documented in the project record with the exact export command and the target table number, so that the next revision repeats it identically rather than reinventing it.

What is worth noticing is which parts of the standard were format-specific and which were not. The rules, the alignment, the caption above, the self-contained note and the regeneration discipline all survived the move intact. Only the mechanism changed, and the two versions of the paper agree because both are generated from the same stored estimates.

## Output

The table file, generated, plus the wrapper in the document:

```
tables/tab3_main.tex          fragment written by the estimation script
tables/tab3_main.rtf          same content for the Word version
code/tables/03_main_table.do  the script that writes both
```

```latex
% in the manuscript
\begin{table}[htbp]\centering
\caption{Effect of rollout on employer firm registrations}
\label{tab:main}
\begin{threeparttable}
\input{tables/tab3_main}
\begin{tablenotes}[flushleft]\footnotesize
\item \textit{Notes:} [sample and period] [estimator] [what is in parentheses
and the clustering, with the number of clusters] [abbreviations] [source].
\end{tablenotes}
\end{threeparttable}
\end{table}
```

And a project table index, one row per table, kept beside the figure index:

| Table | Caption | Source script | Output file | Columns | Font | Regenerates |
| 1 | Summary statistics, estimation sample | 01_summary.do | tab1_summary.tex | 6 | body | yes |
| 3 | Effect of rollout on registrations | 03_main_table.do | tab3_main.tex | 5 | body | yes |
| 7 | Heterogeneity by firm size | 07_hetero.do | tab7_hetero.tex | 10 | body, rotated | yes |
| A2 | Full coefficient estimates | 03_main_table.do | tabA2_full.tex | 5 | footnotesize | yes |

The checklist run against every table before delivery:

| Check | Pass |
| Three rules, no vertical lines, no shading | |
| Caption above, sentence form, with a label | |
| Column numbers present; dependent variable named by a spanning header | |
| Row labels in words, with units where needed | |
| One precision per column, decimal aligned | |
| Uncertainty beneath the estimate, at the same precision | |
| Bottom block: indicators, N, clusters, fit statistic, comparison mean | |
| Note states sample, period, estimator, parentheses content, clustering, source | |
| Generated by a script; deleting the file and rerunning reproduces it | |
| Same conventions as every other table in the document | |

## Failure modes

**Vertical lines.** The most immediately recognisable departure from the convention, usually inherited from a spreadsheet export. Fix by removing them and letting column spacing separate the columns.

**The hand-edited export.** A label fixed in the `.tex` file, a row deleted, a number rounded. Recognisable because deleting the file and rerunning the script does not reproduce it. Fix by moving every edit into the script, including the ones that seem too small to bother with, because those are the ones that silently disappear on the next regeneration.

**Mixed precision within a column.** Two decimals in some cells and three in others. Recognisable at a glance once you look for it. Fix in the export command, not in the file.

**`\resizebox` on wide tables.** Every table at a different effective font size. Recognisable in print and invisible on screen. Fix by working down the escalation list: drop columns, move rows to an appendix, shorten labels, rotate.

**The note that does not state the clustering.** Recognisable by reading the note and asking what is in the parentheses. This is the single most common omission and it is the first thing a careful referee looks for. Fix from the estimation command, not from memory.

**A caption that is a label.** "Table 4: Robustness" tells the reader nothing. Fix with a sentence naming the outcome, the estimator and the variation being shown.

**Variable names from the code as row labels.** `lnemp_w1` in a published table. Fix with a label mapping in the export script so it cannot recur.

**`[H]` float placement.** Forces the table where it is written and leaves large white gaps. Fix by reverting to `[htbp]` and using `\clearpage` at section boundaries if floats are backing up.

**Unbraced text in an siunitx `S` column.** Produces a compilation error whose message does not mention the cause. Fix by bracing every non-numeric entry, including column numbers and Yes and No.

**Merged cells and multi-row headers built by hand.** Fragile, and they break when a column is added. Fix with `\multicolumn` and `\cmidrule(lr)`.

**Inconsistency across tables.** Four note formats, three font sizes, two decimal policies. Recognisable only by reading the tables consecutively, which nobody does until the examiner. Fix with one wrapper snippet and one note template applied to all.

## Edge cases

**A table that must break across pages.** Use `longtable`, which is compatible with booktabs rules, and repeat the header on each page with `\endhead`. Do not use it inside a float; a `longtable` is not a float, and its caption is set differently. Long variable-definition tables are the usual case.

**A journal that supplies its own class and forbids packages.** Follow the journal. Implement the three rules with whatever the class provides, keep the caption above and the note below, and keep the alignment discipline manually. The convention is a set of typographic decisions, not a set of packages.

**A thesis regulation that specifies caption placement or numbering.** The regulation wins over the convention, without argument. Where it requires captions below tables, comply, and keep everything else.

**Numbers that are not comparable down a column**, such as a column mixing coefficients and shares. This is usually a sign that two tables have been merged. Split them, or use a panel structure with a separate precision per panel and say so in the note.

**Very large numbers, or numbers spanning many orders of magnitude.** Rescale and state the unit in the row label: "Revenue (millions)" rather than nine-digit entries. Never use scientific notation in a body table.

**Text-heavy tables**, such as variable definitions or a summary of the literature. The convention still applies: three rules, no vertical lines, caption above. Use `tabularx` or `p{}` columns for the text column, set it ragged right rather than justified so that word spacing stays even, and keep it to two or three columns.

**A table in a referee response letter.** Same rules, smaller, and add one column the paper's version does not have: what changed and where it now appears in the manuscript. `response-to-reviewers` sets the letter's structure.

**A table produced by a coauthor whose pipeline you cannot run.** Do not restyle it into agreement and present it as generated. Either obtain the generating script, or record in the project index that its provenance is external and that it was not regenerated, so that the fact is visible to whoever assembles the replication package.

**Colour in a table.** Almost never justified. Where a single cell must be picked out, use bold or a footnote marker rather than a fill, so that the emphasis survives greyscale printing, consistent with the figure standard in `academic-figures-monochrome`.

## Quality bar

- The table standard was chosen from the target's guidelines, booktabs or APA, and is recorded in the project README.
- Three horizontal rules, no vertical lines, no shading, in every table in the document.
- Every table carries a caption above it in sentence form, with a label, and a note below it in a smaller size.
- The note states the sample, the period, the estimator, what is in the parentheses, the clustering level and the number of clusters, every abbreviation used, and the source.
- Numbers are decimal-aligned with one precision per column, and uncertainty sits directly beneath its estimate at the same precision.
- Column numbers and the dependent variable are identifiable from the table alone, and a referee can tell what changes between columns.
- Every table was written to file by a script; deleting the file and rerunning reproduces it exactly, with no hand edits anywhere.
- No table has been scaled to fit; width was resolved by removing content, shortening labels, or rotating.
- The font size, decimal policy, note structure and caption style are identical across every table of the same class in the document.

## Adapting this to your context

These rules are booktabs as economics journals apply it, for regression tables of a few columns typeset in LaTeX. The typography discipline is general; the assumed standard and content are not.

- **Booktabs itself.** Assumed throughout. If the target follows the APA Publication Manual, use the APA section above instead: bold table number and italic title above, three-tier notes, exact p values and confidence intervals rather than stars, no leading zero on p and r. Pick from the author guidelines, not from habit.
- **The bottom block.** Fixed effects indicator rows, clusters, comparison-group mean: an economics table. Psychology and education want *M*, *SD*, *N* and a correlation matrix; medicine wants the effect measure, its interval and the number analysed per arm.
- **Stars.** Permitted here with the convention stated. APA deprecates them, many medical journals ban them, and confidence intervals are increasingly expected in their place. Reporting the interval costs a column and never loses information.
- **The toolchain.** LaTeX with `esttab`, Word with a named table style. In R, `modelsummary`, `gt`, `flextable`, `apaTables` and `papaja` write LaTeX, Word and HTML from one set of stored estimates, which is the cleanest route when coauthors want different formats.
- **What not to change.** No vertical lines, the note makes the table self-contained, and the table is written by a script and never edited by hand.

## Related skills

`regression-table-production` decides the content of the estimation table, meaning the columns, the bottom block, the stars-or-intervals question and the note's substance, and hands it here for form. `descriptive-statistics-tables` does the same for summary, balance and sample construction exhibits. `econometrician` sets the specification and the clustering that the note must state, and `econometric-model-writer` writes the text that reads the table. `academic-figures-monochrome` is the alternative when the reader needs a shape rather than exact numbers, and shares the regeneration discipline and the restraint about colour. `stata-do-file-craft` and `python-for-econometrics` hold the export code and the reproducibility standard these scripts sit inside. `full-manuscript-build` checks the whole document for the consistency this skill enforces table by table, `response-to-reviewers` uses the same conventions in the letter, and `replication-package` expects every table file to be regenerable from the deposited code.
