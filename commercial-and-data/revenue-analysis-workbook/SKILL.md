---
name: revenue-analysis-workbook
description: Builds the standard seven-tab revenue workbook from a raw transaction or invoice extract: a summary of headline figures, a monthly trend with seasonality separated from direction, a per-entity revenue table, a channel or category split, a top-N view with cumulative share, a concentration tab, and a verification tab that proves every number reconciles. Every figure is a live formula reading the raw sheet, and the same build runs the same way every time so the tenth analysis is as trustworthy as the first. Use it whenever someone asks to analyse revenue, break sales down by client or product or channel, build a revenue summary, produce a monthly trend, work out where the money actually comes from, or turn an accounting export into something a leadership team can read.
---

# Revenue Analysis Workbook

Most revenue questions get answered one at a time. Somebody asks for the top ten clients, a pivot table appears; somebody asks about last quarter, a different pivot appears; three weeks later the two figures in circulation do not agree and nobody can reconstruct either. The board pack says 18.4 million, the sales deck says 17.9 million, and the difference turns out to be one channel that one of the two views excluded for a reason the person who built it no longer remembers.

The cost is not the discrepancy. It is that revenue becomes a matter of opinion inside the organisation, so every conversation about it starts with a negotiation about the numbers instead of a discussion about the business. The second cost is subtler: one-off answers cannot see seasonality, so a routine annual peak gets reported as growth, targets are set from it, and the following quarter looks like a collapse. The same seven tabs, built in the same order, prevent both. This skill is that standard build.

## When to use this, and when not to

Use it when a revenue extract arrives and the question is any of: how much, from whom, through what, and in which direction. Use it as the first build on any new revenue dataset even when the immediate question is narrow, because six of the seven tabs are needed to answer the narrow question honestly and the seventh is what makes the answer defensible.

Do not use it when the question is exposure rather than composition, which is `revenue-concentration-risk`. Do not use it for a per-relationship view of health, lifetime value, and retention, which is `client-economics-analysis`. Do not use it for anything that has not happened yet, which is `expected-revenue-estimation`, and do not use it to write the argument, which is `economics-report-from-data`. The mechanics of reading, auditing, and verifying the underlying file are `spreadsheet-analysis-workbook`, which this build assumes throughout and does not restate.

## What you need before starting

**The transaction extract, at line or invoice grain.** Aggregated monthly totals cannot be re-cut by client or channel, so an aggregate is a report, not a dataset. Missing: ask for the line-level export before starting. If only aggregates exist, say which of the seven tabs cannot be built.

**A stable entity key.** An account ID, a customer number, anything that does not change with spelling. Missing: build the tables on the best available key, run a duplicate-name check, and state in the header note that entity counts are approximate. Names alone will duplicate roughly one client in forty in most systems.

**The value column, defined.** Gross or net, invoiced or recognised, tax in or out. Missing: state the assumption in three places, the header note, the summary tab, and the covering message, and proceed. The definition changes the headline figure and nothing else in the build.

**A usable date column.** One that is a real date rather than text, and whose convention you know: invoice date, posting date, or service date. Missing: derive it if another column supports it, and if not, build the six tabs that do not need time and say why the seventh is absent.

**A channel or category classifier.** The column that separates recurring from one-off, or product line from service line. Missing: ask whether one exists in another system. Where it does not, the split tab is dropped rather than invented, and that absence is stated.

**At least twenty-four months of data, to speak about trend.** Twelve months shows a level; twenty-four shows a direction; thirty-six lets you separate seasonality with any confidence. Missing: build the trend tab anyway, and label every directional statement with the caveat that seasonality is unseparated.

**One figure somebody already believes.** Missing: proceed, but say in the delivery that nothing external anchors the total, so a truncated export could not have been detected.

## The method

This build inherits the discipline in `spreadsheet-analysis-workbook` and does not repeat it. In short: the complete raw data lives in the workbook as its own sheet; every analysis cell is a live formula reading from it; derived fields reference computed cells rather than recomputing independently; a visible reconciliation cell on every tab reads zero; assumptions sit in labelled input cells rather than inside formulas; and every tab carries a header note saying which columns it reads, from which sheet, and which row the data starts on.

1. **Write the column map before the first formula.** Put it on the inputs tab and reference it from every other tab. Layouts differ between periods and between exports of the same report, and this is the single most common source of a wrong number in a workbook that is otherwise correct.

   ```
   Entity key       col D  in [Data]     (account ID, not name)
   Entity name      col F  in [Data]     (display only)
   Category or code col H
   Channel          col J
   Date             col K                (invoice date)
   Value            col O                (net of credit notes)
   First data row   6      Last data row  dynamic, see Verify!B6
   ```

2. **Build tab 7 first.** The verification tab holds the ground truth total and the row count computed straight from the raw sheet, and every later tab reports into it. Building it last means building it after you have stopped being suspicious, which is exactly when it stops working.

3. **Tab 1, revenue summary.** Headline figures as a block, each a formula and none typed: total revenue, revenue by period, period on period change, count of active entities, mean and median revenue per entity, and share through each channel. Report the mean and the median together and always in that order, because the gap between them is the concentration finding stated in two numbers. Where mean revenue per entity is more than twice the median, say so in the summary; that is a portfolio carried by a few relationships and every later tab will confirm it.

4. **Tab 2, monthly trend, with seasonality separated before anything is called growth.** One row per entity or segment, one column per month, the same `SUMIFS` pattern across the row using date bounds rather than a formatted month string.

   ```
   =SUMIFS('Data'!$O$6:$O$150267,'Data'!$D$6:$D$150267,$A12,
           'Data'!$K$6:$K$150267,">="&E$9,'Data'!$K$6:$K$150267,"<"&EDATE(E$9,1))
   ```

   With two or more full cycles, add a seasonal index per calendar month and a deseasonalised series beside the raw one.

   ```
   Seasonal index    =AVERAGEIFS($D$12:$D$47,$C$12:$C$47,MONTH(E$9))/AVERAGE($D$12:$D$47)
   Deseasonalised    =E12/INDEX(Seasonal!$C$2:$C$13,MONTH(E$9))
   ```

   The decision rule: describe a movement as growth only when it survives deseasonalisation, or when the comparison is like for like against the same month a year earlier. With fewer than two cycles neither is available, so use year on year where possible and state plainly that seasonality is unseparated. Add a cumulative running total anchored on the first cell only, and a subtotal row that must equal the ground truth.

5. **Tab 3, entity revenue.** One row per entity, sorted descending. Columns: revenue by period, total, share of total, cumulative share, channel revenue, channel share, first and last activity date, active months, and year on year growth. Non-channel revenue is total minus channel revenue, by subtraction, never a second criteria-based sum. This tab is the input to tabs 5 and 6, so it is built once and referenced rather than recomputed; two independently built top-N tables will disagree eventually and the disagreement will surface in front of an audience.

   ```
   Total       =SUMIF('Data'!$D$6:$D$150267,$A12,'Data'!$O$6:$O$150267)
   Share       =IFERROR($E12/$E$8,0)
   Cumulative  =SUM($F$12:F12)
   Non-channel =$E12-$G12
   Active mths =SUMPRODUCT(--(E12:P12<>0))
   ```

6. **Tab 4, channel or category split.** Revenue by channel per period, share of total, and the change in share across periods. Then the judgement that gives the tab its value: is the shift structural or cyclical. Treat it as structural when it persists across three or more consecutive periods, is traceable to a named product, pricing, or programme change, and is not reversing. Otherwise call it cyclical and say what you think is driving it. Size one point of shift at current scale, because that is the only figure on the tab a leader can act on directly.

7. **Tab 5, top N.** The largest entities by revenue with share, cumulative share, trend direction, and channel adoption. Mark the row where cumulative share crosses half of revenue and the row where it crosses four fifths. The count of entities needed to reach four fifths is the concentration statistic to state in a sentence; it travels better than any ratio because it is a number of relationships rather than a percentage.

8. **Tab 6, concentration.** Top one, top three, top five, and top ten shares, plus the Herfindahl index as the sum of squared shares multiplied by ten thousand.

   ```
   =SUMPRODUCT(('Entity'!$F$12:$F$486)^2)*10000
   ```

   Read against thresholds: below 1,500 diversified, 1,500 to 2,500 moderate, above 2,500 concentrated, above 5,000 dominated by a few relationships. Report both a distribution measure and a cut-point ratio, never one alone. `revenue-concentration-risk` takes this further into anchoring and failure scenarios; this tab stops at measurement.

9. **Close tab 7 and spot-check.** Every segmentation total against the ground truth, each difference reading zero, plus three named spot-checks with the entity, the expected value, the tab value, and the match. Choose the largest entity, one from the middle, and one with an awkward key. A workbook without this tab has not been checked, whatever anyone says about it.

## Reading the result

Report in this order, and resist reordering it to lead with the most interesting finding, because the order is what stops a reader misjudging scale.

The headline figure and its change, with the basis of comparison named. What drove it, in mechanism rather than adjective: more entities, more revenue per entity, or a mix shift. Where the concentration sits, stated as a count of relationships. Whether the mix is moving and whether that movement is structural, with the evidence for the verdict. Then the two or three entities whose trajectory would change the picture on its own.

Never describe a seasonal peak as growth or a seasonal trough as decline. Never annualise a partial year in a seasonal business without saying which way the bias runs. `economics-report-from-data` turns this output into the written argument and enforces the same language standard.

## Worked example

**Situation.** Brightfield Laboratory Services, an environmental testing business of about 180 people, had a board meeting in nine days and no agreed revenue picture. Two figures were in circulation: 18.4 million and 17.9 million over three years. The extract was 96,400 invoice lines across thirty-six months, 312 clients, and two channels: contract testing under annual programmes, and ad hoc sample submissions. The chief executive's question was simply whether the business was growing.

**Task.** One workbook, seven tabs, a single reconciled total, and a defensible answer on growth. Good meant the finance director and the sales director would both accept the same number.

**Action.** The column map went in first. The value column was net of credit notes; the 18.4 million figure turned out to be gross, and the gap was 512,000 of credit notes over three years. That resolved the discrepancy in twenty minutes and became line one of the summary.

The trend tab was built next, and this is where the analysis went wrong first. September revenue was 22 percent above the trailing three-month average, and the first draft of the summary said the business had accelerated sharply in the third quarter. That statement survived about an hour. Plotting all thirty-six months made it obvious: September was the highest month in each of the three years, because an annual regulatory testing deadline falls in early October and clients submit in September. The seasonal index put September at 1.34 and February at 0.71. Deseasonalised, the underlying trend was 6.1 percent annualised, not 22 percent. The whole growth section was rewritten, and the peak-to-trough ratio of 1.9 became a finding in its own right, because it explained a recurring cash squeeze every February that the finance director had been treating as a collections problem.

The second wrong turn was in the entity tab. Built on client name, it returned 327 clients against 312 in the CRM. Fifteen were duplicates: eight from a trading name against a registered name, five from a trailing space, two from an ampersand. On the account ID key the count came back to 312 and the top-N table changed materially, because one of the duplicated clients moved from position fourteen to position six once its two halves were combined.

The channel tab showed contract revenue moving from 41 percent to 58 percent of the total across the three years. The structural test was applied: the shift persisted across all three years rather than one, it was traceable to a programme launched in the second year that converted ad hoc submitters onto annual contracts, and it was not reversing. Verdict structural, stated with those three pieces of evidence. One point of shift was worth about 62,000 a year at current scale.

**Result.** Total revenue reconciled at 17,912,441 net across 96,400 lines, with a zero difference on all four segmentations. Underlying growth was 6.1 percent, not the 22 percent the quarter had suggested. The top eight clients of 312 held half of revenue, and it took 47 clients to reach four fifths. The Herfindahl index was 2,180, in the moderate band.

The board conversation moved off whether the business was growing and onto the February trough and the contract conversion programme, which was the useful outcome. The seasonal index went into the following year's cash forecast. The duplicate-name defect was passed back to the sales operations team, who found the same duplicates in the CRM.

Build time was about eleven hours, of which the seasonality rework was three. The rework would not have been needed had the trend tab been built with the seasonal index from the start, which is why step 4 now carries that instruction rather than leaving it to judgement.

### A second scenario, where it goes differently

The same build requested by a company nine months old, with 4,100 invoice lines and one channel. Two things change, and neither is the standard.

Seasonality cannot be separated at all, so the trend tab reports raw monthly figures with a single sentence stating that no directional claim is supported by nine months of data, and the comparison used is month against the trailing three-month mean rather than year on year. Where an external anchor exists, for instance a published seasonality pattern for the sector or the founders' prior experience of the buying cycle, it is named as an assumption on the inputs tab rather than baked into a formula. The concentration tab, by contrast, becomes the most important tab in the workbook rather than the sixth: with 22 clients, the top one held 31 percent of revenue and the Herfindahl index was 1,940 on a base so small that a single loss moves it by hundreds of points, which is worth saying explicitly.

What changed is the length of the series and the number of entities. The tab list did not change; what each tab is allowed to claim did.

## Output

A workbook of seven tabs plus an inputs tab, and a covering note of five to eight lines. The summary tab is the deliverable most people will read, and it has this shape.

| Figure | Value | Basis |
| Total revenue, 36 months | 17,912,441 | net of credit notes, invoice date |
| Latest 12 months | 6,704,880 | Sep 2025 to Aug 2026 |
| Prior 12 months | 6,318,102 | like for like |
| Growth, year on year | 6.1% | deseasonalised, index on inputs tab |
| Active clients, latest 12 months | 268 | at least one invoice |
| Mean revenue per client | 25,018 | latest 12 months |
| Median revenue per client | 9,340 | latest 12 months |
| Contract channel share | 58.0% | up from 41.2% three years earlier |
| Clients to reach 50% of revenue | 8 | of 312 |
| Clients to reach 80% of revenue | 47 | of 312 |
| Herfindahl index | 2,180 | moderate concentration |

The verification tab carries the reconciliation and the spot-checks.

| Check | Ground truth | Computed | Difference |
| Entity table | 17,912,441 | 17,912,441 | 0 |
| Monthly trend | 17,912,441 | 17,912,441 | 0 |
| Channel split | 17,912,441 | 17,912,441 | 0 |
| Top N plus remainder | 17,912,441 | 17,912,441 | 0 |

Where a figure is charted, keep it monochrome first: series separated by marker shape, dash pattern, and fill texture rather than by colour, legend outside the plot area, and an accent colour used only on the one series the sentence is about.

## Failure modes

**Calling a seasonal peak growth.** Recognise it when a directional claim rests on a single period against the one before it. Deseasonalise, or compare against the same period a year earlier, before the sentence is written.

**Building the top-N table twice.** Recognise it when tab 5 and tab 3 disagree by a few thousand. Build the entity tab once and have every other tab reference it.

**Keying on entity name.** Recognise it when the entity count differs from the count anyone else in the business would give. Rekey on ID and report the duplicates you found, because they are a finding for whoever maintains the source system.

**Computing the complementary channel with a negated criterion.** Recognise it when the two channels sum to more or less than the total, or when a client's channel figure exceeds their total. Subtract instead.

**A mix shift declared structural on one period.** Recognise it when the evidence for structural is the size of the shift rather than its persistence and cause. Apply all three tests, or call it cyclical.

**Annualising a partial year.** Recognise it in any figure carrying the phrase run rate without an elapsed-months input cell beside it. State the elapsed months, state the seasonality position, and say which way the bias runs.

**Reporting the mean without the median.** Recognise it when a portfolio of hundreds is described by one average. The pair is the finding; either one alone is misleading in a concentrated book.

**Delivering six tabs.** Recognise it when the verification tab is missing or empty. It is the tab that makes the other six worth reading.

## Edge cases

**Fewer than twenty-four months of data.** Build all seven tabs and restrict what tab 2 is allowed to claim. Say in the summary that seasonality is unseparated, and prefer period-on-period comparisons against a trailing mean over any annualised figure.

**One channel only.** Drop tab 4 rather than inventing a split, and say why it is absent. A category split invented from product codes nobody uses operationally will be argued with rather than acted on.

**Revenue recognised over time, not at invoice.** The invoice date and the revenue period differ, sometimes by months. Build on the recognition basis if the extract supports it, and if it does not, build on invoice date and state the basis in every tab header. Do not mix the two in one workbook.

**Very long tail, thousands of entities.** Build the entity tab in full, then present tab 5 as top fifty with a single remainder row that reconciles. The remainder row is what keeps the tab honest.

**Multi-entity or multi-currency group.** Build one workbook per reporting currency and a consolidation tab that uses the rate table finance already applies, with its date convention stated. Never convert on a rate you sourced yourself.

**Intercompany or internal revenue in the extract.** Identify it before the ground truth is fixed, report it as a separate line, and give the total both including and excluding it. Removing it silently makes every figure fail to tie to the accounts.

**A single client above forty percent of revenue.** The composition question is largely answered by that one fact. Complete the build, then hand straight to `revenue-concentration-risk`, because the useful question has become exposure rather than mix.

## Quality bar

- The column map is written before the first formula and every tab references it.
- All seven tabs are present, and the verification tab shows a zero difference for every segmentation.
- Seasonality is separated, or the absence of separation is stated in the same sentence as every directional claim.
- Complements are computed by subtraction and the entity tab is built once and referenced.
- Mean and median revenue per entity are reported together.
- Every share and ratio is traceable to a cell in the entity tab, not recomputed on the tab that displays it.
- The structural against cyclical verdict on any mix shift carries its three pieces of evidence.
- Three spot-checks are recorded with expected and actual values.

## Related skills

`spreadsheet-analysis-workbook` is the foundation this build assumes: the file audit, the formula patterns, and the verification discipline all live there. `image-to-spreadsheet` produces the raw sheet when the source is a scan or a PDF. Downstream, `revenue-concentration-risk` takes the entity and concentration tabs into exposure, anchoring, and failure scenarios; `client-economics-analysis` takes the same entity table into lifetime value, health, and retention; `expected-revenue-estimation` uses the trend and channel tabs as the historical base for anything forward-looking; and `economics-report-from-data` turns the finished workbook into the written argument. `revenue-forecast` covers the forward planning cycle that consumes these figures, and `financial-model-builder` the driver-based model that sits above it.
