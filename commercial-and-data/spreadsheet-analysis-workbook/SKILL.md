---
name: spreadsheet-analysis-workbook
description: The discipline for analysing someone else's spreadsheet without breaking it and without trusting it blindly. Read the structure before touching anything, audit columns and existing formulas, establish one ground truth figure, build every analysis cell as a live formula reading the raw sheet, compute complements by subtraction, close a visible reconciliation cell to zero, and spot-check before delivering. This is the foundation the other workbook skills assume rather than repeat. Use it whenever a workbook, CSV export, accounting extract, or data file arrives and the task is to analyse it, add tabs, check someone else's numbers, rebuild a sheet that broke, or answer a question from it, including vague requests like "can you just pull the total", "does this add up", or "have a look at this file".
---

# Spreadsheet Analysis Workbook

A file arrives from a finance team, an accounting system, or a colleague's laptop, and the request is a number by lunchtime. Two failures produce almost every wrong answer that follows. The first is answering before understanding the file: the arithmetic is right, the formula is right, and the column being summed is net of credit notes when the question was gross, or is a budget column parked two positions from the actuals under a header that abbreviates the same way. The second is hardcoding: someone pastes the value instead of the formula, the extract is refreshed a fortnight later, and the deck still carries the old number with nothing on its face to say so.

Both failures are invisible in the output. A total from a misread column looks exactly like a total from the right one, and a pasted number looks exactly like a calculated one until somebody clicks the cell. So the error survives review, gets quoted in a board pack, and is found by the one person who recomputes it from a different direction, usually in the meeting where it matters. The cost is rarely the correction. It is that every other figure from the same source is now suspect, and re-establishing that trust takes longer than the original analysis did.

## When to use this, and when not to

Use it whenever raw data arrives and something has to be computed from it: an invoice or transaction extract, a CRM export, a timesheet dump, a survey file, a workbook a colleague built and has since left behind. Use it when the task is to check someone else's numbers, when a sheet started returning errors after a refresh, and when you reopen a workbook you built yourself more than a month ago, because your own layout assumptions decay like anyone else's.

Do not use it as the build instruction for a specific deliverable. `revenue-analysis-workbook` gives the standard seven-tab revenue build; `revenue-concentration-risk` and `client-economics-analysis` take that output into exposure and per-relationship economics; `expected-revenue-estimation` covers figures that do not yet exist in any data; `economics-report-from-data` turns finished tabs into the written argument. All five assume this discipline and do not restate it. Getting a table out of a PDF or a photograph is `image-to-spreadsheet`; a forecast model driven by assumptions rather than history is `financial-model-builder`.

## What you need before starting

**The file itself, in a form you can open and inspect.** A screenshot of a pivot table is not the data. Missing: ask for the export that produced the view, and say that nothing can be reconciled against an image.

**The question, phrased so the answer is a number.** "Analyse this" produces a survey; "which customers hold the top half of revenue, and is the service line growing" produces a workbook. Missing: write the two or three questions you think are meant, one line each, and ask which. Ninety seconds here prevents the most expensive rework.

**The definition of the value column.** Gross or net, including or excluding tax, invoiced or recognised, one currency or several. Missing: state the assumption in the header note, the summary, and the covering message, then proceed. A revenue column that is sometimes net and sometimes gross is the most costly thing to discover late.

**The period the question covers, and the period the data actually covers.** These differ more often than expected, usually because the export was cut on a posting date rather than an invoice date. Missing: compute the minimum and maximum date from the raw sheet and report what you found rather than what you were told.

**A figure somebody already believes.** A prior report, a system total, a number in the chief executive's head. Missing: say so in the delivery, because a ground truth built only from the file cannot detect a truncated export, which is the failure this input exists to catch.

**Whether the data will be refreshed.** A one-off answer and a workbook somebody re-runs monthly are different builds, and the difference is decided at the start. Missing: assume it will be refreshed; retrofitting costs a rebuild.

**A tool that can compute over the file.** A spreadsheet application, or a scripting environment with a spreadsheet library. Missing: never estimate totals by eye. Report the structure and ask for a processable format.

## The method

Every step below serves one of six non-negotiables. They are easy to skip without the justification, so they come first.

- **The complete raw data lives in the workbook as its own sheet.** Analysis tabs never stand alone, and no formula points at an external file.
- **Every analysis cell is a live formula reading that sheet.** The test is mechanical: change one row of raw data and the analysis must move.
- **Derived fields reference computed cells rather than recomputing independently.** The complement is the total minus the part, never a second criteria-based sum.
- **A visible reconciliation cell reads zero.** Every tab carries one, on the tab, not in a footnote.
- **Assumptions sit in labelled input cells,** in a distinct colour, referenced by formula and never typed inline.
- **Every tab documents which columns it reads,** from which sheet, and which row the data starts on.

The sequence that delivers them follows.

1. **Inventory the file before changing anything.** List every sheet, its used range, its header row, and its first data row. Headers sit on row one far less often than people assume: exports carry title blocks, filter rows, and merged banner cells above them.

2. **Establish one ground truth figure.** Usually the grand total of the value column, computed directly from the raw sheet across its full extent, with the row count beside it. It goes into the verification tab before any analysis exists. The rule for choosing it: pick the figure the person who commissioned the work would recognise. If they would recognise none of them, that is itself a finding worth one line in the delivery.

3. **Establish what each column that matters actually measures.** Unit, granularity, and whether a blank means zero or unknown. That last distinction is not pedantry: a blank meaning unknown but treated as zero drags every average down while every total stays correct, which is why it survives review.

4. **Audit the columns for the defects that break criteria-based sums.** Numbers stored as text, mixed date formats, leading and trailing spaces in key fields, inconsistent entity naming, duplicate rows, merged cells inside the data region. Run each as a formula in the workbook rather than by eye, so it is repeatable after a refresh.

   ```
   Numbers stored as text  =SUMPRODUCT(--ISTEXT('Data'!$O$6:$O$150267))
   Untrimmed keys          =SUMPRODUCT(--(TRIM('Data'!$F$6:$F$150267)<>'Data'!$F$6:$F$150267))
   Non-dates in date col   =SUMPRODUCT(--NOT(ISNUMBER('Data'!$K$6:$K$150267)))
   Full-extent row count   =COUNTA('Data'!$F:$F)-1
   Duplicate keys          =SUMPRODUCT(--(COUNTIF('Data'!$A$6:$A$150267,'Data'!$A$6:$A$150267)>1))
   ```

   Each should read zero, or read a number you have explained. When one does not, repair in a helper column, never by editing raw values, so the repair is visible, reversible, and reapplied on refresh.

5. **Audit the existing formulas before building on them.** Where they point, whether their ranges reach the last data row, whether any hold a typed constant, whether any reference a deleted sheet, and whether copied formulas kept the absolute references they needed. The commonest defect is a range that stopped at row 50,000 when the export grew to 150,262, understating every total by a consistent proportion and therefore looking plausible. The rule: an inherited formula you have not traced is not evidence, and you do not quote a number from it.

6. **Check the tabs against each other and against the raw sheet.** Where two disagree, find which is wrong before building on either. Building a third view that happens to agree with one of them resolves nothing and adds a claimant.

7. **Design the output before writing a formula.** One sentence saying what the tab answers, then the column headers, the row structure, and the reconciliation row.

8. **Build the primary column first, then derive from it.** Compute the main figure per output row, check its sum against the ground truth from step 2, and only then add shares, complements, growth rates, and cumulative columns, each referencing cells already checked.

9. **Close the reconciliation before delivery, not after review.** The cell subtracts the sum of the segments from the ground truth and must read zero. A non-zero value is a gap or a double count, and both have to be found. Tolerance rule: round to two decimal places and treat anything above one currency unit as a defect rather than as rounding, because rounding noise across 150,000 rows does not accumulate to eleven thousand.

10. **Spot-check three entities by an independent route.** The largest, one from the middle, and one with an awkward key: punctuation, an ampersand, a trailing space, a name that is a substring of another. Filter the raw sheet, total by hand, compare.

11. **Write the header note on every tab.** Source sheet, columns read with their letters and meanings, first data row, extract date, and the assumptions in force. Write it as if the reader has never seen the file, because in six months that reader is you.

12. **Escalate rather than guess.** Stop and ask when the raw data contradicts itself, when the ground truth cannot be established, when a load-bearing column is genuinely ambiguous, when the reconciliation will not close, or when the answer rests on an assumption nobody has stated. A question asked late costs a day; an analysis delivered on a misunderstood column costs the credibility of the whole file.

## The formula patterns that carry the discipline

**The complement, by subtraction and never by a second criteria-based sum.**

```
Right   =$D12-$E12
Wrong   =SUMIFS('Data'!$O$6:$O$150267,'Data'!$F$6:$F$150267,$A12,'Data'!$H$6:$H$150267,"<>SVC*")
```

The wrong version fails on blanks, on codes carrying the pattern in another position, and on text-formatted code cells.

**Month buckets by date bounds, not by formatted text.** The wrong version merges the same month across different years and leans on a helper column a refresh may not regenerate.

```
Right   =SUMIFS('Data'!$O$6:$O$150267,'Data'!$K$6:$K$150267,">="&E$9,'Data'!$K$6:$K$150267,"<"&EDATE(E$9,1))
Wrong   =SUMIF('Data'!$L$6:$L$150267,TEXT(E$9,"mmm"),'Data'!$O$6:$O$150267)
```

**Anchoring, so a copied formula still reads the right range.**

```
Cumulative share   =SUM($F$12:F12)
Per-entity total   =SUMIF('Data'!$F$6:$F$150267,$A12,'Data'!$O$6:$O$150267)
```

Anchor source ranges fully, the key column by column only, and in a running total the first cell only.

**Wrap every division and every lookup.**

```
Growth   =IFERROR($E12/$D12-1,"n/a")
Share    =IFERROR($D12/$D$8,0)
```

Use `"n/a"` where a blank is a real answer and `0` where it is not.

**The reconciliation and the containment check.** Containment catches the wildcard matching more than intended, which reconciliation alone will not: a channel figure exceeding its own entity total can still leave the grand total balanced. The range below covers the 486 customers of the worked example on a table whose first data row is 12, so it ends at row 497. Derive the last row from your own entity count every time rather than copying a range: a range that stops short of the last data row is the first entry in the error catalogue below and the most common defect in this whole file.

```
Reconciliation   =ROUND('Verify'!$B$4-SUM($D$12:$D$497),2)
Containment      =IF($E12>$D12+0.005,"CONTAINMENT FAIL","ok")
```

## The error catalogue

Ranges that stop short of the last data row. Wildcards matching more than intended. Numbers stored as text, ignored by every criteria-based sum and counted by `COUNTA`. Two segments computed independently that do not complement. Absolute and relative references mixed after a copy. Division by zero left unwrapped, or wrapped so aggressively that a real failure returns zero. A blank treated as zero when it means unknown. A period column reading the wrong month after a layout change. Entity names differing by a trailing space, an ampersand against the word "and", or a legal suffix present in some rows only. Two currencies in one column with no rate column. A manually typed total below the data region and inside the range. A filter left applied so a hand-computed check excludes half the rows.

## Worked example

**Situation.** An operations lead at Kestrel Components, an industrial parts distributor of about 240 people, sent an invoice extract: 150,262 rows over thirty-four months, one row per invoice line, twenty-three columns. The question was which customers held the top half of revenue and whether the service line was growing faster than parts. All figures in this example are in US dollars. The lead believed the three-year total was "about 41.2 million" from a prior board pack, and needed something a leadership meeting could read in four days.

**Task.** A workbook with a customer table, a monthly trend, a parts against service split, and enough verification that the finance director could open it and satisfy himself in ten minutes. Good meant every figure clickable to a formula and a reconciliation reading zero.

**Action.** The inventory found four sheets: the extract, a pivot cache, an abandoned working tab, and a lookup table mapping product codes to lines. Headers sat on row five under a title block, so the first data row was six. Column O held "Net Amt" and column P held "Gross Amt"; the prior board pack had used gross. That was the first finding, and it took eleven minutes.

Ground truth on the net column came to 41,187,344.18 across 150,262 rows. Against the believed 41.2 million that looked like rounding, and the first draft of the summary said so. It was not. The customer table, keyed on the customer name in column F, reconciled to 41,176,209.91, leaving a gap of 11,134.27 the reconciliation cell refused to close.

The trailing-space check returned 34: thirty-four rows carried a trailing space in the customer name, creating near-duplicate entities that sorted apart and fell outside the top-200 cut. The text check returned 7, value cells imported as text and ignored by every `SUMIF` while still counted by `COUNTA`. The name-keyed approach was abandoned and the table rekeyed on the customer ID in column D, with the name pulled in by lookup for display only. That closed the gap to zero.

The second wrong turn was the parts against service split, first built as two separate `SUMIFS` on `"SVC*"` and `"<>SVC*"`. The halves summed to 41,203,880, some 16,536 above ground truth, and containment flagged four customers whose service figure exceeded their total. The cause was codes beginning "SVCX" that the lookup table classified as parts, plus 212 blank-code rows the negation criterion excluded. The rebuild referenced the lookup table explicitly for service and derived parts by subtraction. Both problems went at once.

Spot-checks ran on the largest customer, a mid-table one, and one whose registered name held an ampersand. That third one failed first time, because the pivot cache spelled it "and" while the extract used the symbol; on the ID key it passed.

**Result.** The workbook went out on day three with six analysis tabs and a verification tab holding the ground truth, four segmentation totals each reconciling to zero, and three named spot-checks. The headline was that eleven customers of 486 held 50.4 percent of revenue, and that the service line had gone from 18.2 to 26.9 percent over thirty-four months.

Two things came out of the process rather than the analysis. The gross against net difference meant the board pack figure and the workbook figure would never agree, so that was stated in one sentence at the top rather than left to be discovered. And the trailing-space defect traced back to a manual step in order intake, which the operations lead fixed at source. Build time was about nine hours, two of them on the 11,134.27 gap, which would have been none had the file been keyed on ID from the start.

### A second scenario, where it goes differently

The same extract, but the request is a workbook the operations lead refreshes each month by pasting a new export over the data sheet. Nothing about the six non-negotiables changes. Almost everything about the build does.

Fixed ranges become the enemy rather than the discipline. Every source range becomes a structured table reference or a whole-column reference, so the analysis does not silently ignore rows 150,263 onward next month. The verification tab gains a row-count cell and a maximum-date cell, both compared against the previous refresh, because the failure this build must catch is not a wrong formula but a short paste: an export cut at 100,000 rows reconciles perfectly to itself and understates everything by a third. The header note gains a four-line refresh procedure, and the product code lookup becomes a maintained input with an unmatched-code counter that must read zero.

What changed is the refresh expectation, which changes the build rather than the standard. A workbook built for a single answer and then refreshed anyway is where most broken spreadsheets come from.

## Output

A workbook and a short covering note. The workbook carries, in order: the raw data sheet unmodified, an inputs tab, the analysis tabs, and a verification tab. Every analysis tab opens with a header note like this.

```
TAB: Customer revenue
Answers:        Revenue per customer for the full extract period, with share and cumulative share.
Source sheet:   Data
Columns read:   D customer ID (key), F customer name (display only), K invoice date, O net amount
First data row: 6        Last data row: 150267 (dynamic; see Verify!B6)
Extract dated:  2026-08-31
Assumptions:    Net of credit notes. Single currency, USD. Blank code rows counted in totals, excluded from line split.
```

The verification tab is not optional and not hidden.

| Check | Expected (USD) | Computed (USD) | Difference | Status |
| Ground truth, net amount | 41,187,344.18 | 41,187,344.18 | 0.00 | ok |
| Sum of customer table | 41,187,344.18 | 41,187,344.18 | 0.00 | ok |
| Sum of monthly trend | 41,187,344.18 | 41,187,344.18 | 0.00 | ok |
| Parts plus service | 41,187,344.18 | 41,187,344.18 | 0.00 | ok |
| Row count | 150,262 | 150,262 | 0 | ok |
| Untrimmed keys | 0 | 34 | 34 | repaired in helper col |

| Spot-check | Route | Expected (USD) | Tab value (USD) | Match |
| Largest customer, ID 10442 | raw filter | 3,088,406.97 | 3,088,406.97 | yes |
| Mid-table, ID 20871 | raw filter | 214,930.00 | 214,930.00 | yes |
| Awkward name, ID 30119 | raw filter | 88,412.55 | 88,412.55 | yes |

The covering note runs to five lines: the ground truth and how it was computed, what reconciles, what was repaired and where, the assumption the reader inherits, and what you could not resolve.

## Failure modes

**Answering the question sent rather than the question the data supports.** Recognise it when the answer needs a column you have not defined. Define it, and if it cannot be defined, say what the file can and cannot show before producing a number.

**Treating a small reconciliation gap as rounding.** Recognise it by shape: rounding noise is fractions of a currency unit, so anything in the thousands is structural. It is nearly always a key defect or a truncated range, both five minutes to diagnose once you accept they exist.

**Building on an inherited formula you have not traced.** Recognise it when you cannot say out loud which cells a figure came from. Trace it or rebuild it.

**Computing two complementary segments independently.** Recognise it when the parts do not sum to the whole, or when containment fires. Derive one by subtraction.

**A reconciliation cell that exists but is never read.** Recognise it when the cell sits on a hidden tab, is formatted white on white, or reads a stale range after rows were added. Put it on the tab it verifies with visible status text.

**Spot-checking only the easy entities.** Recognise it when all three checks passed first time. Deliberately pick one key with punctuation and one that is a substring of another.

**Reporting a defect in someone else's workbook with an adjective attached.** Recognise it when the finding reads as a judgement. Report the defect, its size, and its cause, showing the failing reconciliation beside the one that closes.

**Delivering without saying what the reader is inheriting.** Recognise it when the covering note contains no assumptions. Every workbook rests on at least one, usually about what the value column means.

## Edge cases

**No external figure to check against.** Compute the total from the raw sheet, state that it is self-referential, and name the failure it cannot detect: a truncated or filtered export. Ask for a system total, since one number from the source converts the workbook from plausible to verified.

**The extract is too large for the spreadsheet application.** Aggregate in a scripting environment, bring the aggregate in, and keep a sample of the raw data with a note saying where the full extract lives and how the aggregate was produced. The raw-data non-negotiable bends here; traceability does not.

**Multiple currencies with no rate column.** Do not convert on a rate you found yourself. Report by currency and ask for the rate table finance already uses, with its date convention.

**The data contradicts itself, with two rows for one invoice line at different values.** Quantify the contradiction as a count and a value before deciding anything. Under a tenth of a percent, document it and proceed on a stated rule; above that, stop, because the export is the problem.

**The answer is needed in twenty minutes.** Compress to four steps: ground truth, the figure asked for, one reconciliation cell, one spot-check. Say in the reply that the file was not fully audited and name the checks not run.

## Quality bar

- The raw data is in the workbook and every analysis cell is a live formula reading it, with no typed constants outside the labelled input cells.
- A reconciliation cell is visible on every analysis tab and reads zero.
- Complements are computed by subtraction, and a containment check exists wherever a subset is reported.
- Three spot-checks are recorded with expected and actual values, one on an awkward key.
- Every tab carries a header note naming its source sheet, columns, first data row, and assumptions.
- The ground truth is stated with its row count, and any difference from a previously believed figure is explained rather than absorbed.
- Anything ambiguous was escalated rather than assumed, visibly, in the delivery.

## Adapting this to your context

This is written for a spreadsheet holding an extract of tens to hundreds of thousands of rows, read by a finance or operations reader who will click a cell. The six non-negotiables travel further than the mechanics do.

- **The spreadsheet itself.** Every pattern has an equivalent elsewhere: a criteria-based sum is a `GROUP BY`, a helper column a derived field, a header note a docstring, a reconciliation cell a failing test. In SQL, R or Python, keep the six rules and drop the formulas.
- **The ranges and row numbers.** Row 6 as the first data row and 150,262 rows of extract are one file's shape, not a convention. Derive every range from your own inventory, and prefer a structured table reference wherever the file will be refreshed.
- **Single currency.** A multi-currency extract needs a rate column with its date convention stated and taken from whoever owns it, and a ground truth established per currency before anything is consolidated.
- **Who receives it.** A finance reader wants the reconciliation tab first. A research reader wants the audit trail and every helper column reproducible from a script.

- **What not to change.** The raw data stays in the file, every analysis cell is a live formula reading it, and a visible reconciliation cell reads zero on every tab.

## Related skills

This skill is assumed by every other workbook skill in the track. `revenue-analysis-workbook` is the standard build that sits directly on it; `revenue-concentration-risk` and `client-economics-analysis` consume the entity table that build produces; `expected-revenue-estimation` applies the same discipline to figures with no history behind them; `economics-report-from-data` converts finished tabs into an argument and will not accept a figure that cannot be traced to a cell here. `image-to-spreadsheet` produces the raw sheet when the source is a picture or a PDF. `financial-model-builder` covers forward models built from assumptions rather than an extract, and `analysis-audit` the equivalent discipline for statistical code.
