---
name: spreadsheet-analysis-workbook
description: The discipline for analysing someone else's spreadsheet without breaking it or trusting it blindly: read the structure before touching anything, audit columns and existing formulas, build analysis tabs from live formulas that read the raw data, reconcile every segmentation to zero, and verify by spot-check before delivering. Covers the universal formula patterns, the common error catalogue, and the escalation triggers. Use this skill whenever a workbook, CSV export, or data file arrives and the task is to analyse it, add tabs to it, check someone else's numbers, or answer a question from it.
---

# Spreadsheet Analysis Workbook

Two failures account for almost every bad spreadsheet analysis. The first is answering before understanding the file, so the number is right for a column that means something else. The second is hardcoding, so the number is right today and silently wrong the moment the data updates. This skill is the sequence that prevents both.

## The non-negotiables

1. **Raw data lives in the workbook.** Analysis tabs never stand alone. No formula references an external file. When the data updates, everything recalculates.
2. **Every calculated cell is a live formula.** `=SUMIF('Data'!$F$6:$F$150267,"CODE",'Data'!$O$6:$O$150267)`, not `=3088406.97`. The test: change one row of raw data and the analysis must move.
3. **Derived fields reference computed cells.** Non-programme revenue is total minus programme, never a second SUMIF on the complementary criteria, because wildcards and criteria rarely complement perfectly and the gap appears as an unexplained difference weeks later.
4. **Every tab reconciles.** A visible cell reading `= SourceTotal - SUM(segments)` that must equal zero. Non-zero means a gap or a double count, and it is fixed before delivery, not footnoted.
5. **Inputs are visually distinct.** A benchmark percentage, a month count, a scenario multiplier: labelled cell, distinct colour, referenced by formula, never typed inline.
6. **Column positions are documented.** Layouts differ between sheets and between periods. Every tab carries a header note saying which column it reads from which sheet, and which row the data starts on.

## Phase 1: Read before you touch

**Structure.** List every sheet, its row and column count, its header row, and its first data row. Headers are often not on row one.

**Ground truth.** Establish the single figure everything else must reconcile to, usually the grand total of the value column, computed directly from the raw sheet. Every later number is checked against it.

**Meaning.** For each column that matters, establish what it measures, its unit, its granularity, and whether blanks mean zero or unknown. A revenue column that is sometimes net and sometimes gross is the single most expensive thing to discover late.

## Phase 2: Structural audit

**Columns.** Type consistency, numbers stored as text, mixed date formats, trailing spaces in keys, inconsistent entity naming that will break every SUMIF, and duplicate rows.

**Existing formulas.** Where they point, whether ranges cover the full data, whether any are hardcoded, whether any reference deleted sheets, and whether copied formulas kept their absolute references.

**Cross-tab integrity.** Do the tabs agree with each other and with the raw sheet. Where they do not, find which one is wrong before building anything on top.

## Phase 3: The formula patterns

```
SUMIF        one condition          =SUMIF(criteria_range, criteria, sum_range)
SUMIFS       several conditions     =SUMIFS(sum_range, r1, c1, r2, c2)
COUNTIFS     rows matching          =COUNTIFS(r1, c1, r2, c2)
SUMPRODUCT   flexible multi-condition maths, and weighted sums
IFERROR      wrap every division and every lookup
Complement   =Total - Segment       never a second criteria-based sum
Share        =Segment / Total
Change       =Current / Prior - 1
Run rate     =YTD / MonthsElapsed * 12
Cumulative   =SUM($B$2:B5)          anchor the first cell only
```

## Phase 4: Segmentation, time series, and concentration

Break revenue down by entity with one row per entity and a live formula per cell. Sort descending, add share and cumulative share, and mark where cumulative share crosses half and four fifths of the total. Split by channel or category with the complement computed by subtraction. For time series, build one column per period with the same formula pattern across the row, add period-on-period change and a running total, and add a subtotal row that must match the ground truth.

## Phase 5: Verification

**The three-step spot-check.** Take one entity. Compute its total from the raw data by filter. Compare against the analysis tab. Repeat for the largest entity, one mid-sized, and one with an unusual name. Names with punctuation or trailing spaces are where SUMIF criteria fail silently.

**The reconciliation check.** Every segmentation sums to the ground truth. Zero gap, no exceptions.

**The containment check.** Any subset must be less than or equal to its parent. A channel figure larger than the entity total means the criteria are matching rows they should not, usually through a wildcard.

## Phase 6: The error catalogue

Hardcoded values in a formula cell. Ranges that stop short of the last data row. Criteria with wildcards that match more than intended. Numbers stored as text so they are ignored by SUMIF. Two segments computed independently that do not complement. Absolute and relative references mixed after a copy. Division by zero left unwrapped. A blank treated as zero when it means unknown. A period column that reads the wrong month because the layout changed between sheets.

## Phase 7: Building a tab from scratch

Define in one sentence what the tab answers. Define the output structure before writing a formula. Build the ground truth column first and check it. Add derived columns that reference it. Add the reconciliation row. Add the header note documenting sources, columns, and first data row.

## Phase 8: Escalation

Stop and say so rather than guessing when: the raw data contradicts itself, the ground truth cannot be established, a column's meaning is genuinely ambiguous, the reconciliation cannot be closed, or the answer depends on an assumption nobody has stated. An analysis delivered on a misunderstood column is worse than a question asked late.

## Quality bar

- Raw data in the workbook, every analysis cell a live formula, no hardcoded values.
- Reconciliation cell present and reading zero on every tab.
- Three spot-checks done, including one awkward entity name.
- Assumptions in labelled input cells and stated in the header note.
- Anything ambiguous escalated rather than assumed.
