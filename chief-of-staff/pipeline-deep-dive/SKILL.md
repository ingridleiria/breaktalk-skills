---
name: pipeline-deep-dive
description: Runs a rigorous deep-dive analysis of a sales pipeline from a CRM export, spreadsheet, or connected CRM, producing coverage, conversion, velocity, concentration, and hygiene diagnostics with a prioritized action list and a forecast the leadership team can defend. Use this skill whenever the user shares pipeline or opportunity data, asks about forecast accuracy, pipeline coverage, win rates, stage conversion, deal velocity, stale deals, quota attainment, or says "analyze our pipeline", "are we going to hit the number", "why is the forecast off", "prepare the pipeline review", "which deals should we focus on". Trigger for any analysis of opportunities moving through stages, whether the user calls it pipeline, funnel, or forecast.
---

# Pipeline Deep Dive

A pipeline review answers one question: will the number be hit, and if not, what has to change this week. Every metric below exists to answer that question, and the analysis is only done when it ends in owners and actions.

## Step 1: Understand and clean the data

Before any metric, profile the export:

- Fields available: stage, amount, close date, created date, owner, account, source, last activity, probability, next step.
- Stage definitions: ask the user what each stage means and what exit criteria move a deal forward. Numbers mean nothing without this.
- Time frame: which quarter or period is being forecast, and the quota or target for it.
- Hygiene issues to detect and report before analysis: deals with close dates in the past, deals with no activity in more than 30 days, deals with no next step, amounts that are placeholders (round numbers repeated), duplicate opportunities, stages inconsistent with age. Quantify each issue (count and amount) because hygiene is a finding, not a footnote.

State the sample plainly: number of open opportunities, total pipeline value, period covered, and the exclusions applied.

## Step 2: The core diagnostics

Compute and present each with the number, the benchmark or prior period where available, and the one-line implication.

1. **Coverage**: open pipeline for the period divided by the remaining target. Report overall and by stage-weighted value. State the assumption used for weights, and show both raw and weighted coverage; a 3x raw coverage made of early-stage deals is not 3x.
2. **Stage conversion**: historical rate of movement from each stage to the next, and stage-to-close. Use closed deals from prior periods; if history is thin, say so and use the user's estimates, labeled.
3. **Velocity**: average and median days in each stage, and total cycle length for won deals. Flag open deals sitting in a stage longer than twice the median; these are the most likely to slip or die.
4. **Win rate**: by period, by owner, by source, by deal size band. Look for the segment where the rate collapses; that is usually the real story.
5. **Concentration**: share of the forecast carried by the top three and top ten deals. When one deal is more than 25% of the quarter, the forecast is that deal's forecast, and the review should say so.
6. **Slippage**: deals whose close date moved out during the period, count and amount. Chronic slippage in one owner or stage indicates a process problem, not a luck problem.
7. **Age and creation**: new pipeline created this period versus needed run-rate for next period. A healthy quarter with an empty next quarter is a finding.

## Step 3: Build the forecast three ways

Present each with its method visible, then reconcile:

- **Commit-based**: sum of deals the owners commit to, after the reviewer's adjustments.
- **Weighted**: stage probability times amount, using historical conversion rather than CRM default probabilities.
- **Trend-based**: run-rate from the last three to four periods adjusted for known seasonality.

Deliver best case, likely, and worst case with the assumptions under each. Where the three methods disagree materially, explain which is more trustworthy for this pipeline and why.

## Step 4: Deal-level review for the ones that matter

For the top deals by amount and the deals that carry the likely case, produce a short card each: stage, amount, close date, days in stage, last activity, next step, single-threaded or multi-threaded (number of contacts engaged), known risks, and the one action that most increases the probability this period. If a connected CRM or conversation tool provides call history, use it; otherwise flag what the user needs to verify with the owner.

## Step 5: The action list

End with a prioritized list, each item carrying an owner and a date:

- Deals to push this week and the specific action.
- Deals to move out of the forecast or close-lost, with the reason, because a clean forecast is worth more than a large one.
- Hygiene fixes with counts (close dates, next steps, stale deals).
- Process findings: the stage where deals stall, the segment where win rate falls, the owner or source with chronic slippage, each with a recommended change.
- Pipeline generation needed for next period, quantified.

## Output

A short written brief for leadership: headline (on track, at risk, off track, with the likely-case number against target), the five findings that matter, the three-way forecast, the action list. Tables for the diagnostics, charts only where they change understanding (stage funnel, forecast waterfall, aging distribution), each chart with one message stated in its title and no legend inside the plot area. Full deal cards and the hygiene report in an appendix. When the user needs a file, follow the environment's spreadsheet or document skill for formatting.

## Quality bar

- Every number is reproducible from the data provided; the method for each is stated.
- Hygiene problems are quantified and listed before conclusions, because they bound how much the conclusions can be trusted.
- The forecast is a range with stated assumptions, never a single point.
- The brief ends in owners, actions, and dates, or it is not finished.
