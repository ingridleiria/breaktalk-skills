---
name: pipeline-deep-dive
description: Analyses a sales pipeline from a CRM export or connected system and produces the diagnostics a leadership team can act on: quantified hygiene problems reported before any conclusion, raw and weighted coverage, measured stage conversion and slippage from closed history, velocity and ageing, win rate by segment, concentration, a forecast built three ways and reconciled, deal cards for the opportunities that carry the number, and an action list with owners and dates. Enforces the standard that every metric is reproducible from the data supplied and that CRM default probabilities are never used as conversion rates. Use this skill whenever someone shares pipeline or opportunity data, asks about coverage, win rates, stage conversion, deal velocity, stale deals, slippage or quota attainment, or says analyse our pipeline, are we going to hit the number, why is the forecast off, prepare the pipeline review, which deals should we focus on, what is really in there.
---

# Pipeline Deep Dive

Most pipeline reviews review the pipeline. Two hours, deal by deal, each owner narrating the last conversation they had, and a closing instruction to push hard on the top ten. Nothing in the meeting was arithmetic. Nobody left knowing whether the quarter closes, and the one number produced was a sum of amounts entered by the people whose bonus depends on them.

The cost lands in the last fortnight of the quarter. The gap that was visible in the data in week three gets discovered in week eleven, when the only remaining levers are discounting and pressure, both of which cost more than they recover. Discounting to close a quarter resets the price for the renewal; pressure applied to a deal that was never real produces a closed-lost with a burnt relationship. Meanwhile the pipeline needed for the following quarter was not built, because everyone spent the last month on this one.

This skill replaces narration with measurement, and it is only finished when it ends in named actions with dates.

## When to use this, and when not to

Use it whenever opportunity-level data is available and someone needs to know whether the period lands: a quarterly pipeline review, a forecast that has started missing, a new sales leader taking over a team, a board question about coverage, or a diagnosis of why deals stall.

The boundaries with the other numeric skills matter, because a request for "pipeline numbers" can mean any of them:

- `revenue-forecast` builds the revenue number for the year or quarter from four layers, of which pipeline conversion is one. This skill produces the measured conversion, slippage, and timing inputs that layer needs, and it should run first whenever that layer is material. If the question is where the year lands overall, including contracted revenue and renewals, that skill owns it.
- `financial-model-builder` builds the company model over multiple years. This skill is a diagnostic on data that already exists, not a projection built from drivers.
- `pricing-and-resourcing-model` prices and staffs one engagement. It answers what to charge if a deal closes; this skill answers whether it will.

Do not use it to coach an individual on a specific deal, which is a conversation and not an analysis. Do not use it where the data has fewer than about twenty closed opportunities in comparable prior periods, because measured conversion rates cannot be computed from that; see the edge cases. Do not use it to build a compensation case against a person; a pipeline analysis used that way stops being answered honestly within one cycle, and the data quality never recovers.

## What you need before starting

**The opportunity export, open and closed.** Open deals alone give coverage and nothing else. Closed deals from prior comparable periods are what make every rate in the analysis measured rather than assumed. Missing: ask for at least four prior quarters of closed opportunities, and if only open deals are available, say clearly that conversion rates are unavailable and report coverage in deal counts rather than weighted value.

**Stage definitions and exit criteria.** What each stage means and what has to be true for a deal to leave it. Numbers computed across stages nobody has defined are arithmetic without meaning. Missing: ask the sales leader to describe each stage in one sentence, and record the answers in the workbook, because this is often the first time they have been written down.

**The target for the period, and the remaining gap.** Missing: ask for the board figure specifically. Coverage against a team's internal stretch number is a different diagnosis from coverage against the committed one.

**The fields that carry the diagnosis.** Amount, stage, close date, created date, owner, account, source, last activity date, next step. Missing: run the diagnostics the available fields support and list the ones you could not compute. A missing last-activity field removes the whole staleness analysis and should be said plainly rather than approximated.

**The period being forecast, and any known seasonality.** Missing: use the current quarter and note that no seasonal adjustment was applied.

**Access to the owners for the top deals.** The deal cards need a next step and a risk, and those are not in the export. Missing: build the cards from the data, mark the fields you could not verify, and hand the verification list to the sales leader as part of the output.

## The method

1. **Profile the export before computing anything.** Row count, date range, fields present, and the meaning and unit of each field that matters. Establish the ground truth figure, which is total open pipeline value for the period, computed directly from the raw sheet. Every later number reconciles to it.

2. **Quantify hygiene, and report it before any conclusion.** Count and value for each of: close dates in the past, no activity in more than thirty days, no next step, amounts that are obviously placeholders such as the same round number repeated, duplicate opportunities on one account, and deals older than twice the median cycle. Hygiene is a finding, not a footnote, because it bounds how far the conclusions can be trusted. State plainly what share of the pipeline value is affected.

3. **Compute coverage two ways.** Raw coverage is open pipeline for the period divided by the remaining gap to target. Weighted coverage applies measured stage-to-close rates. Report both, because three times raw coverage made of early-stage deals is not three times anything. The judgement call is which to lead with: lead with weighted where you have at least twenty closed deals per stage to measure from, otherwise lead with raw and say why.

4. **Measure stage conversion from closed history, never from the system defaults.** For each stage, the share of deals that reached it and eventually closed won, computed over prior comparable periods. Where the business changed materially during that history, such as a segment being discontinued or a price change, exclude the affected period and say so. Compare your measured rates against the system defaults in the output; the gap between them is frequently the single most useful finding.

5. **Measure velocity and ageing.** Median days in each stage and total cycle for won deals, then flag every open deal sitting in a stage longer than twice that median. Use median rather than mean throughout, because one eighteen-month deal distorts the mean and the mean is what gets quoted.

6. **Cut win rate by the dimensions that could carry a story:** segment, deal size band, source, owner, and product. Look for where the rate collapses rather than for the average. A blended win rate is almost always hiding two opposite movements.

7. **Measure concentration and slippage.** The share of the forecast carried by the top three and top ten deals, and the count and value of deals whose close date moved out during the period. Where one deal exceeds a quarter of the number, say explicitly that the forecast is that deal's forecast. Chronic slippage concentrated in one stage or one owner is a process finding, not luck.

8. **Check pipeline creation against what next period needs.** New qualified pipeline created this period, against the run rate required to support the next one at measured conversion. A healthy current quarter sitting on an empty next quarter is a finding that belongs near the top of the brief.

9. **Build the forecast three ways and reconcile them.** Commit is the sum of what owners commit, after the reviewer's adjustments. Weighted is measured conversion multiplied by amount. Trend is the run rate of the last three or four periods adjusted for known seasonality. Where the three disagree materially, say which is more trustworthy for this pipeline and why: commit is most trustworthy where owners have a track record of accurate calls, weighted where history is deep and the mix is stable, trend where the business is transactional and volumes are high.

10. **Write deal cards for the opportunities that carry the number.** The top deals by amount plus any deal the likely case depends on. Stage, amount, close date, days in stage, last activity, next step, how many contacts are engaged, the named risk, and the single action that most raises the probability this period.

11. **End in an action list with owners and dates.** Deals to push and the specific action. Deals to remove from the forecast or close out, with the reason, because a clean forecast is worth more than a large one. Hygiene fixes with counts. Process findings with a recommended change. And the pipeline generation required for next period, quantified.

## The workbook

The analysis lives in a workbook built to the discipline in `spreadsheet-analysis-workbook`, and this matters here more than in most analyses because the export will be refreshed and the review repeated.

Raw export in the workbook, untouched, with the column map recorded. Every metric a live formula reading that sheet, so refreshing the export refreshes the analysis. Derived fields referencing computed cells rather than recomputing them: weighted pipeline reads the stage totals already computed, and late-stage value is total minus early stage rather than a second independent criteria sum, because two independently built segments rarely complement perfectly and the gap surfaces as an unexplained difference. A visible reconciliation cell on every tab reading zero, confirming that the segments sum to total open pipeline. Every assumption, including the conversion rates and the staleness threshold, in a labelled input cell so the review can be rerun with different ones.

## Worked example

**Situation.** A software company selling to mid-market operations teams, quarterly target of 4.1 million, six weeks into the quarter. The sales leader reported 12.3 million of open pipeline and described coverage as three times, which the leadership team had accepted for two quarters running while both quarters missed.

**Task.** Establish whether the quarter would land, before the halfway point, with enough specificity to change something.

**Action.** The export held 214 open opportunities and 173 closed from the previous four quarters. Hygiene came first and reshaped the conversation before any forecast was built. Forty-one open deals, worth 1.9 million, had close dates already in the past. Sixty-three, worth 3.4 million, had no recorded activity in more than thirty days. Twenty-two had no next step. After removing deals with past close dates that had not moved in sixty days, the genuinely open figure for the quarter was 9.6 million rather than 12.3, and raw coverage fell from three times to 2.3.

Measured conversion was the substantive finding. The system carried defaults of 60 percent at proposal and 30 at qualification. Measured from the 173 closed deals, proposal converted at 29 percent and qualification at 9. Weighted coverage was therefore 1.4 times, not three.

The wrong turn: the first conversion calculation used all 173 closed deals and gave 38 percent at proposal. That included two quarters of a small-business segment the company had stopped selling to in the spring, which had closed fast and cheaply. Excluding it left 118 deals and dropped proposal conversion to 29 percent. The blended figure was arithmetically correct and would have overstated the quarter by roughly 600,000. The rule taken from it: before computing any rate, ask what changed in the business during the history you are measuring, and exclude the periods that answer.

Velocity showed the mechanism. Median time in proposal for won deals was 21 days; 34 open deals had been in proposal for more than 42, carrying 2.7 million. Win rate cut by size band showed deals above 100,000 converting at 11 percent against 34 percent below, and every one of those large deals was single-threaded, with one contact engaged.

The three-way forecast: commit 3.2 million, weighted 2.9, trend 3.4. Likely case 3.1 against a target of 4.1.

**Result.** The brief opened with the gap of one million, stated in week six rather than week eleven. Twenty-nine deals were removed from the forecast, reducing reported pipeline by 2.2 million, which was uncomfortable in the meeting and made the remaining number believable. Three actions carried owners: a second contact identified in each of the eleven large open deals within two weeks, a multi-threading requirement added to the proposal stage exit criteria, and 1.8 million of new pipeline required in the following six weeks to protect the next quarter.

The quarter closed at 3.4 million, above the likely case and below target. The forecast was accurate to within ten percent, which had not happened in the previous three quarters, and the multi-threading change moved large-deal win rate to 19 percent over the following two quarters.

### A second scenario, where it goes differently

An enterprise business with a nine-month sales cycle, 31 open opportunities, and 19 closed deals across the last four quarters. Measured stage conversion cannot be computed from 19 deals in any way that survives scrutiny; splitting them by stage leaves cells with three or four observations, and a rate built on four observations will be quoted as though it were a rate.

The method changes shape. Rates are abandoned in favour of deal-level qualification, assessed against named criteria: is there a written business case, is there an identified budget, has a decision process been described by the client rather than assumed, are three or more contacts engaged, has a security or procurement review been scheduled. Coverage is reported in deal counts against the number of wins needed, not in weighted value. The forecast is built one way, from commit, with each deal's inclusion argued explicitly, and the range is set by which deals are contested rather than by a percentage band.

The hygiene work matters more, not less, because with 31 opportunities a single stale deal is three percent of the pipeline. And the most useful output is not a number at all: it is the list of deals failing two or more qualification criteria, which is where the quarter is actually lost.

## Output

A short written brief for leadership, with the workbook behind it.

```
PIPELINE REVIEW, [period]                      [date]
Sample: [n] open opportunities, [value]; [n] closed from [periods]
Exclusions applied: [what and why]

HEADLINE
[On track / at risk / off track]. Likely case [x] against target [y].

DATA QUALITY, BEFORE THE CONCLUSIONS
| Issue | Count | Value | Share of open pipeline |
| Close date in the past |  |  |  |
| No activity in 30+ days |  |  |  |
| No next step |  |  |  |
| Possible duplicates |  |  |  |

COVERAGE
Raw: [x] times. Weighted at measured conversion: [y] times.
Measured conversion by stage, against system defaults:
| Stage | Measured | System default | Deals measured |

THE FIVE FINDINGS
[Each one sentence, with the number, most important first.]

FORECAST, THREE WAYS
| Method | Number | What it assumes |
| Commit |  |  |
| Weighted |  |  |
| Trend |  |  |
Likely case: [ ]. Range: [ ] to [ ]. Most trustworthy method here: [ ] because [ ].

ACTIONS
| Action | Deal or scope | Owner | By when | Effect |
Pipeline generation required for next period: [ ]
```

Charts only where they change understanding: the stage funnel, the forecast waterfall, the ageing distribution. One message per chart, stated in the title, legend outside the plot area, monochrome with series separated by marker and dash pattern rather than colour. Deal cards and the full hygiene list go in the appendix.

## Failure modes

**Analysing before cleaning.** Recognise it when coverage is quoted and hygiene appears later as a note. Fix by putting the hygiene table above the conclusions, where it bounds them.

**System probabilities used as conversion rates.** The commonest defect, and it always flatters. Recognise it because the weighted number lands close to target. Fix by measuring from closed history and showing both figures side by side.

**Rates measured across a business that changed.** Recognise it by a conversion rate that looks better than the team's lived experience. Fix by asking what changed during the measurement window, and excluding the affected periods explicitly.

**Means where medians belong.** One long deal drags the average cycle and the average deal size. Fix by reporting medians, and by reporting the mean only alongside them where the skew is itself the point.

**The blended win rate.** Recognise it when one rate is quoted for a business selling into two segments. Fix by cutting on size band and segment before drawing any conclusion.

**A review that ends in encouragement.** Recognise it because the output contains no dates. Fix by requiring an owner and a date on every action, and by removing any finding you cannot attach one to.

**Removing deals quietly.** Cleaning the forecast without saying what was removed and why destroys trust faster than a bad number. Fix by listing every removal with its reason in the appendix.

## Edge cases

**Fewer than about twenty closed deals in comparable periods.** Do not compute stage conversion. Switch to the qualification-criteria method in the second scenario, report coverage in deal counts, and say explicitly that rates were not computable.

**One deal is more than a quarter of the number.** Present it separately above the analysis with its own reasoning, and show the forecast with and without it. Averaging it into a weighted total hides the only risk that matters.

**The data is in someone's head, not the system.** Where the export is materially incomplete, say so as the first finding and scope the analysis to what the data supports. A confident analysis of a system nobody uses is worse than no analysis, because it will be quoted.

**A connected CRM or conversation tool is available.** Use it for last activity, contacts engaged, and call history, which are the fields most often stale in a manual export. Where no such tool exists, mark those fields as unverified on the deal cards and hand the verification list to the owners. Never require a paid tool for the analysis to be possible.

**Mid-period stage redefinition.** Where stages were redefined during the history being measured, conversion rates across the boundary are not comparable. Measure from the redefinition forward, state the shorter window, and widen the range accordingly.

**The review is being used to build a case against an individual.** Decline that framing and report at the level of process and segment. Once a pipeline review is understood as evidence-gathering, the data stops being entered honestly, and every future analysis is worse.

## Quality bar

- Every number is reproducible from the data supplied, with its method stated.
- Hygiene problems are quantified in count and value, and appear before any conclusion.
- Conversion rates are measured from closed history, with the count of deals behind each rate shown, and compared against the system defaults.
- Coverage is reported raw and weighted, with the assumption behind the weighting stated.
- The forecast is presented three ways, reconciled, with the most trustworthy method named and justified.
- Concentration is stated, and any deal above a quarter of the number is shown separately.
- Every reconciliation cell in the workbook reads zero against total open pipeline.
- The brief ends in actions with owners and dates, including the pipeline generation needed for next period.

## Related skills

`revenue-forecast` consumes the conversion, slippage, and timing outputs of this skill as its pipeline layer, and is where the full-year number belongs. `spreadsheet-analysis-workbook` is the underlying workbook discipline. `financial-model-builder` holds the wider company model. `pricing-and-resourcing-model` prices the deals this analysis says will close. `sales-call-analysis` and `account-reengagement-plan` work the individual deals this review flags. `revenue-concentration-risk` covers concentration in the customer base rather than in the pipeline. `weekly-status-update` carries the between-review movement, and `decision-memo` is the format when the finding requires a decision rather than an action.
