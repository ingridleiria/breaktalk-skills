---
name: revenue-analysis-workbook
description: Builds the standard revenue analysis workbook from a raw transaction or invoice extract: a summary tab with the headline figures, a monthly trend tab, a per-entity revenue tab, a channel or category split, a top-N tab, a concentration tab, and a verification tab that proves every number reconciles. Every figure is a live formula reading the raw sheet. Use this skill whenever the user asks to analyse revenue, break down sales by client or product or channel, build a revenue summary, produce a monthly trend, or turn an accounting export into something a leadership team can read.
---

# Revenue Analysis Workbook

The same seven tabs answer almost every revenue question a leadership team asks, and building them in the same order every time is what makes the tenth analysis as trustworthy as the first. This skill is that standard build. It assumes the discipline in `spreadsheet-analysis-workbook` and does not repeat it.

## Before building: the column map

Write the column map at the top of the workbook and refer to it from every tab. Layouts differ between periods and this is the single most common source of a wrong number.

```
Entity name      col [ ] in [sheet]   (the client, customer, or account)
Category or code col [ ]
Channel          col [ ]
Date             col [ ]
Value            col [ ]
First data row   [ ]      Last data row  [ ]
```

## Tab 1: Revenue summary

A block of headline figures at the top, each a formula, none typed.

Total revenue, revenue by period, period over period change, count of active entities, mean and median revenue per entity, and the share through each channel. Then the period splits and the mix. Every figure here is repeated somewhere below in more detail, and every one must agree with it.

## Tab 2: Monthly trend

One row per entity or segment, one column per month, the same formula pattern across the row using SUMIFS on entity and month. Add month on month change, a cumulative running total anchored on the first cell, and an annual subtotal row that must equal the ground truth. Seasonality is visible here and nowhere else, so read it before describing any month as growth.

## Tab 3: Entity revenue

One row per entity, sorted by revenue descending. Columns: revenue by period, total, share of total, cumulative share, channel revenue, channel share, first and last activity date, active months, and year over year growth. Non-channel revenue is total minus channel, computed by subtraction. This tab is the input to the concentration and top-N tabs, so it is built once and referenced rather than recomputed.

## Tab 4: Channel or category split

Revenue by channel per period, share of total, and the shift in share across periods. State whether a shift is structural, persisting across periods and driven by a product or programme change, or cyclical, tracking a season or a promotion. Size the value of one point of shift at current scale, because that is the number a leader can act on.

## Tab 5: Top N

The largest entities by revenue with their share, cumulative share, trend, and channel adoption. Mark the row where cumulative share crosses half of total revenue and the row where it crosses four fifths. The count of entities needed to reach four fifths is the concentration statistic worth stating in a sentence.

## Tab 6: Concentration

Top one, top three, top five, and top ten shares, and the Herfindahl index as the sum of squared shares multiplied by ten thousand. Read against thresholds: below 1,500 diversified, 1,500 to 2,500 moderate, above 2,500 concentrated, above 5,000 dominated by a few relationships. `revenue-concentration-risk` takes this further into anchoring and failure scenarios.

## Tab 7: Verification

Not optional and not hidden. It holds the ground truth figure computed directly from the raw sheet, the same figure as computed by each segmentation, the difference for each, which must be zero, and three named spot-checks with the entity, the expected value, the tab value, and the match. A workbook without this tab has not been checked, whatever anyone says.

## Reading the result

Report in this order: the headline figure and its change, what drove it, where the concentration sits, whether the mix is shifting and whether that shift is structural, and the two or three entities whose trajectory would change the picture. Do not describe a seasonal peak as growth or a seasonal trough as decline. `economics-report-from-data` turns this output into the written argument.

## Quality bar

- Column map written before the first formula, and referenced from every tab.
- All seven tabs present, the verification tab included.
- Every segmentation reconciles to the ground truth with a zero difference.
- The complement computed by subtraction, never by a second criteria-based sum.
- Seasonality separated from trend before any figure is described as growth.
