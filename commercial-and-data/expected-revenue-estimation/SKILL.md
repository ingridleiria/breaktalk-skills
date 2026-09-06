---
name: expected-revenue-estimation
description: Estimates what something will be worth before it has a track record. Selects among five methods ranked by reliability, from a direct historical average through comparable benchmarks, top-down sizing, pipeline conversion, and a bottom-up unit build, then produces three scenario bands with the base case marked, a sensitivity table that names the dominant assumption, a ramp adjustment for anything not yet at steady state, the cost of delay when a launch slips, and an explicit update trigger that gives the estimate a shelf life. Use it whenever someone asks what a new programme, site, client, product, or initiative could be worth, for a run rate or an annualised projection, for an opportunity to be sized, for a scenario model, for a business case number, or for the revenue impact of a delay.
---

# Expected Revenue Estimation

Someone asks what a new thing could be worth. A number gets produced in an afternoon, goes into a slide, and within three weeks it is in a plan. Two quarters later the plan is missed and nobody can say why, because the number arrived without a method, without the assumption it rested on, and without any statement of what would have made it wrong. It cannot be defended and it cannot be revised, so it is either quietly abandoned or defended past the point of sense.

The second failure is the upside presented as the estimate. Nobody does this deliberately; it happens because the number that gets an initiative approved is the number that gets built, and the conservative case is left in a working file. Headcount is then hired against a figure that assumed full maturity from month one, and the gap between the assumed ramp and the real one becomes a hiring mistake rather than an estimating one.

An estimate is a claim about the future with a method behind it. The method is the part that can be argued with, so it is stated every time, alongside the assumption it rests on and the evidence that would change it. A single number with no method and no range is a guess wearing a suit.

## When to use this, and when not to

Use it for anything without its own history: a new programme, a new site or clinic or branch, a first-year client, a product line, a market entry, a channel. Use it when a run rate is wanted from partial data, when an opportunity has to be sized for a business case, when a delay needs a cost attached, and when a number already in circulation needs a method retrofitted before anyone relies on it further.

Do not use it to analyse what has already happened, which is `revenue-analysis-workbook`, or to audit the file behind it, which is `spreadsheet-analysis-workbook`. Do not use it to build the full driver-based financial model with cost lines and cash, which is `financial-model-builder`, or the committed forward number the business will be held to, which is `revenue-forecast`; this skill produces the input those consume, not the commitment. Do not use it to size an existing client's unsold potential, which is the whitespace section of `client-economics-analysis`, or to write the narrative, which is `economics-report-from-data`.

## What you need before starting

**The unit being estimated, defined precisely.** Revenue per site per month, per client in year one, per contract, per user. An estimate whose unit is unstated cannot be checked against anything later. Missing: define it yourself in one line, put it at the top of the output, and ask for confirmation.

**Whatever history exists, even if it is thin.** Six months of actuals for the thing itself changes the method entirely. Missing: move down the reliability table and say which method you are using and why the better one was unavailable.

**Comparables, with their own start dates.** Similar things already live, matched on type, customer base size, sector, and tenure. The start dates matter as much as the revenue, because a comparable three months old is measuring a ramp, not a steady state. Missing: say the benchmark method is unavailable and move to top-down or bottom-up, with the reliability drop stated.

**The addressable pool and a defensible penetration rate, for top-down.** Missing: the top-down method should not be used. A pool multiplied by an invented percentage produces a large number with no information in it, and it is the single most common way a business case loses credibility in the room.

**The pipeline with values, stage probabilities, and close dates, for pipeline conversion.** Missing: use the historical close rate on open pipeline instead, and say the stage-weighted view was unavailable.

**The decision this estimate feeds, and who will use it.** A number for a go or no-go decision needs a different treatment from a number for a target. Missing: ask. If the answer is that it will become a target, say so in the output and lead with the conservative case.

**A launch or start date, where timing is in play.** Missing: cost of delay cannot be computed. Say so rather than omitting the section silently, since delay is usually the largest single number in the analysis.

## The method

This inherits the discipline in `spreadsheet-analysis-workbook` and does not repeat it. In short: the complete raw data lives in the workbook as its own sheet; every analysis cell is a live formula reading from it; derived fields reference computed cells rather than recomputing independently; a visible reconciliation cell on every tab reads zero; assumptions sit in labelled input cells rather than inside formulas; and every tab documents which columns it reads, from which sheet, and which row the data starts on. In an estimation workbook the input cells matter more than anywhere else, because the whole output is a function of them and a reader's first move will be to change one.

1. **Define the unit, then choose the method by what the data supports.** Use the highest-reliability method available and name it in the output, along with the reason a more reliable one was not used.

   | Method | Use when | Reliability |
   | Direct historical average | The thing exists with six or more months of actuals | Highest |
   | Comparable benchmark | It is new, but similar things are live and measurable | High |
   | Top-down sizing | The addressable pool is known and penetration can be defended | Medium |
   | Pipeline conversion | A pipeline exists with values and a historical close rate | Medium |
   | Bottom-up unit build | Only unit economics are known: volume, frequency, size | Medium to low |

   Where two methods are available, run both and reconcile the difference in a sentence. Where they disagree by more than a third, that disagreement is the finding and it goes in the output above the number.

2. **Method one, direct historical average.** Mean revenue per period over the active periods, with incomplete periods excluded rather than averaged in. Adjust for anything known and non-recurring. Report the confidence band from the observed variability rather than a flat percentage.

   ```
   Active-period mean =IFERROR(SUM($E12:$P12)/SUMPRODUCT(--($E12:$P12<>0)),0)
   Stripped of one-off=$Q12-$R12
   Band, low          =$Q12-STDEV.S($E12:$P12)
   ```

3. **Method two, comparable benchmark.** Pick two to four comparables matched on type, customer base size, sector, and tenure. Compute each one's own active-period mean, then the composite. Name them in the output, because the estimate is only as defensible as they are, and a reader who disagrees with a comparable can then say so precisely rather than rejecting the whole number.

   Apply the scenario band: forty percent of the composite as the conservative case during ramp, seventy percent as the base once established, one hundred percent at full maturity matching the benchmark. Then apply the ramp separately, because the two are different adjustments and collapsing them hides the timing.

   ```
   Composite    =AVERAGE($Q$12:$Q$17)
   Base monthly =$Q$19*Inputs!$B$5
   Ramp factor  =SUM(Ramp!$B$2:$B$13)/12
   Year one     =$T$19*12*$Ramp_factor
   ```

   Build the ramp curve from the comparables themselves: what proportion of steady-state revenue they achieved in months one, two, three and so on. A ramp assumed rather than observed is where optimistic year-one numbers come from.

4. **Method three, top-down sizing.** Addressable pool multiplied by penetration multiplied by value per unit. The penetration rate is the whole argument, so anchor it on penetration observed among comparable populations and report the low, mean, and high observed rates rather than one chosen number. If no comparable population can be observed, do not use this method.

5. **Method four, pipeline conversion.**

   ```
   Weighted pipeline  =SUMPRODUCT($D$12:$D$88,$E$12:$E$88)
   Time adjusted      =SUMPRODUCT($D$12:$D$88,$E$12:$E$88,--($F$12:$F$88<=$Window_end))
   Historical rate    =Closed_won/Total_entered   over a comparable prior period
   Converted estimate =Open_pipeline*$Historical_rate
   ```

   Where the stage-weighted figure and the historical-rate figure disagree, report both and say which the business has been closer to before. That comparison is usually more informative than either number, because a persistent gap between them says something about how stages are being applied.

6. **Method five, bottom-up unit build.** For a programme or site: active users times purchases per user per year times average purchase size. For a recurring service: accounts times revenue per account, adjusted for first-year churn. For a new client: the comparable first-year average times a ramp factor, reaching the full comparable average in year two. Every input labelled, every input changeable, and no input buried inside another formula.

7. **Report three scenarios and mark the base as the figure to cite.** Never a point estimate. Where the estimate will become a target, lead with the conservative case and say why.

8. **Run the sensitivity, always.** One-variable: the key assumption varied by thirty percent either side in steps, with the resulting estimate at each point. Two-variable: a matrix across the two assumptions that matter most. The decision rule: if the estimate swings by more than half across a plausible range of one assumption, that assumption is the finding rather than the estimate, and it goes at the top of the output with a note on what would resolve it.

9. **State the update trigger.** What new data would cause this to be revised, when that data will exist, and who will look at it. An estimate without a stated shelf life stays in circulation long after it has been overtaken, which is how a reasonable number becomes an indefensible one.

## Cost of delay

Delayed revenue is forgone, not deferred. An initiative live in September does not recover June, July, and August, and the instinct in the room will be to treat the shortfall as timing that will be made up later. Say explicitly that there is no recovery mechanism.

Per initiative: the monthly estimate multiplied by months lost, at all three scenario rates. Then the aggregate across initiatives, then the cumulative position at three, six, and twelve months.

```
Monthly forgone      =$T$19
Delay cost, 3 months =$T$19*3
Aggregate            =SUMPRODUCT($T$12:$T$30,$U$12:$U$30)
```

Where the initiative has a ramp, the cost of a delay is not the steady-state rate multiplied by the months lost; it is the ramp curve shifted, which usually costs more than the naive figure in the first year and less thereafter. Compute it both ways once, show the difference, and use the ramp-shifted figure.

## Worked example

**Situation.** Meridian Facilities Group, a commercial cleaning and maintenance company operating at 41 client sites, wanted to know what rolling out a planned maintenance programme to 18 further sites would be worth. Six sites already ran it. The board wanted a figure in ten days to decide whether to fund a programme manager and two technicians, and the head of operations had already circulated an estimate of 4.9 million a year.

**Task.** A defensible year-one and steady-state estimate with scenarios, the dominant assumption identified, and a cost of delay, in a workbook the finance director could retune.

**Action.** The 4.9 million figure was traced first, since a number in circulation has to be dealt with before a new one will be heard. It was top-down: 18 sites multiplied by the revenue of the best-performing existing site, annualised. It assumed every new site would match the best of six, from month one.

The comparable benchmark method was the right one, because six comparables existed with their own histories. Building it exposed two problems with any simple average of them. Two of the six had been live for under six months, and their partial ramp had been averaged in as though it were steady state. One carried a one-off equipment sale of 61,000 inside its monthly average, which alone moved the composite by 850 a month.

Recomputed properly, on active months, excluding incomplete months and stripping the non-recurring item, the composite steady-state figure was 12,800 per site per month, with a range across the four mature comparables of 8,100 to 19,400. The ramp curve, built from the four mature sites, showed roughly 9 months to steady state: 22 percent of steady state in month one, 41 in month three, 78 in month six, 96 in month nine. The average of the twelve monthly ramp factors was 0.63.

The first version of the estimate applied the scenario band and the ramp together in one multiplication and produced a year-one figure that nobody could interpret, because it was not clear whether 70 percent meant a weaker site or a slower start. That version was abandoned and the two adjustments were separated onto their own input cells, which is how the workbook shipped.

Scenarios at steady state, across 18 sites: conservative at 40 percent of composite, 92,160 a month; base at 70 percent, 161,280 a month, or 1.94 million a year; upside at 100 percent, 2.76 million. Year one, with the 0.63 ramp factor applied to the base case: 1.22 million.

The sensitivity table varied the number of sites that actually adopt, which was the dominant assumption by a distance. At 12 sites adopting, the base annual figure was 1.29 million; at 18, 1.94 million; the swing across that plausible range was 50 percent of the estimate. Varying the composite by thirty percent moved it by only 30 percent. So the finding stated at the top of the output was that the estimate is governed by adoption, not by site performance, and that the resolving evidence was the first six sign-ups, which would exist within a quarter.

Cost of delay was computed on the ramp-shifted basis: 161,280 a month at the base rate once mature, but 78,000 a month in the first six months of any delayed cohort. Three months of delay across the full rollout cost 484,000, six months 968,000, twelve months 1.94 million, none of it recoverable.

**Result.** The board funded the programme manager and one technician rather than two, staged on adoption, with the second technician triggered by the eighth site signing. The estimate cited was 1.94 million steady state and 1.22 million in year one, both marked base case, against the 4.9 million previously circulating; the difference was explained in one line as full maturity from month one assumed at the best site's rate.

The update trigger was written in: revise when six sites are live for three months each, expected within two quarters. At that point the observed composite came in at 11,600, below the 12,800 assumption, and the estimate was revised down by nine percent without argument, because the trigger and the method had been agreed in advance.

The workbook took about seven hours, of which two went on the ramp curve. That was the part nobody had asked for and the part that changed the hiring decision.

### A second scenario, where it goes differently

The same request for something genuinely first of its kind: a new service line with no internal comparables, no external population whose penetration can be observed, and no pipeline, because nothing has been sold yet. Four of the five methods are unavailable, and the fifth, a bottom-up unit build, rests entirely on assumptions with no evidence behind any of them.

Producing a three-scenario estimate here would be false precision, and the honest move is to reverse the question. Instead of asking what this will be worth, ask what it would have to be worth to justify the investment, then assess whether that level is plausible against anything observable. The output becomes a break-even statement: at the proposed cost, the line needs 340,000 of annual revenue by month eighteen, which is 28 clients at the current average deal size, against a sales capacity that has historically added 17 new clients a year across all lines. That is a decision the board can take without a forecast, and it is defensible in a way a bottom-up number would not have been.

What changed is that no method above medium-low reliability was available. The rule is that when the best available method cannot support a number anyone should act on, the deliverable changes shape rather than the confidence being inflated to fill it.

## Output

A workbook with an inputs tab, a comparables tab, a scenario tab, a sensitivity tab, and a cost-of-delay tab, plus this block as the summary anyone will actually read.

```
ESTIMATE: planned maintenance programme, 18 sites
Unit:            revenue per site per month
Method:          comparable benchmark (6 live sites, 4 mature)
                 chosen over direct historical average: no history for these 18 sites
Comparables:     Sites 4, 9, 17, 22 (mature); Sites 31, 38 excluded from composite, under 6 months
Key assumption:  18 of 18 sites adopt; composite steady state 12,800/site/month
Source:          active-month mean of mature comparables, one-off equipment sale stripped
Ramp:            9 months to steady state; year-one factor 0.63 (observed, 4 sites)

                 Monthly (steady)   Annual (steady)   Year one
Conservative      92,160             1,105,920         696,700
Base             161,280             1,935,360       1,219,300   <- the figure to cite
Upside           230,400             2,764,800       1,741,800

Sensitivity:     adoption count dominates. 12 sites = 1,290,000; 18 sites = 1,935,000.
                 A 30% swing in composite moves the estimate 30%; adoption moves it 50%.
Cost of delay:   161,280 per month at steady state, 78,000 per month during ramp.
                 3 months 484,000 | 6 months 968,000 | 12 months 1,935,000. Not recoverable.
Update when:     6 sites live for 3 months each, expected within 2 quarters.
```

## Failure modes

**A point estimate.** Recognise it by the absence of a range. Three scenarios, base case marked, every time.

**The upside presented as the estimate.** Recognise it when the cited figure equals the best comparable's performance. Mark the base case explicitly and state the percentage of composite it represents.

**Ramp collapsed into the scenario band.** Recognise it when a single percentage is doing two jobs and no one can say whether it means a weaker outcome or a slower start. Separate them into two input cells.

**A ramp assumed rather than observed.** Recognise it when the curve is a straight line or a set of round numbers. Build it from the comparables; if there are none, say the year-one figure is unsupported and give steady state only.

**Incomplete periods averaged in.** Recognise it when a comparable's mean is far below the others and it started recently. Exclude incomplete periods rather than averaging them.

**Non-recurring items left inside a benchmark.** Recognise it when one comparable is an outlier. Inspect it before including it; a single equipment sale or settlement inside a monthly average distorts the composite for every site downstream.

**A top-down number built on an invented penetration rate.** Recognise it when the rate is a round percentage with no observed population behind it. Change method.

**An estimate with no update trigger.** Recognise it when nothing in the output says when it expires. Write the trigger, the expected date, and who looks at it.

**Annualising partial-year data in a seasonal business.** Recognise it in any run rate without an elapsed-months cell and a seasonality note beside it. State which way the bias runs.

## Edge cases

**Two methods disagree by more than a third.** Report both, name the difference as the finding, and say what evidence would resolve it. Do not average them; the average is a number neither method supports.

**The estimate will become a target rather than a plan input.** Lead with the conservative case, say why, and put the base and upside below it. A target set at the base case with a ramp in front of it is missed in the first two quarters by construction.

**Only one comparable exists.** Use it, name it, and widen the scenario band rather than narrowing it: conservative at thirty percent rather than forty. A single comparable carries its own idiosyncrasies and there is no way to see them.

**The comparables are all from a different market or period.** Adjust explicitly for the difference, state the adjustment as its own input cell, and show the estimate with and without it.

**The thing being estimated cannibalises existing revenue.** Estimate gross and net separately, with the cannibalisation rate as a labelled input. Presenting only the gross figure is the most common way a business case survives approval and fails delivery.

**No method above medium-low reliability is available.** Change the deliverable. Produce a break-even statement and a plausibility assessment rather than an estimate, and say which one you are giving them.

**Someone else's number is already in circulation.** Trace it and explain the difference before presenting a new one. An unexplained second number is treated as a disagreement between people rather than between methods, and the better estimate frequently loses.

## Quality bar

- The method is named, along with the reason a more reliable one was not used.
- Three scenarios are reported and the base case is marked as the figure to cite.
- Comparables are named individually, with their maturity, wherever the benchmark method is used.
- Ramp and scenario band are separate input cells, and the ramp is observed rather than assumed.
- A sensitivity table exists and the dominant assumption is stated above the number.
- Cost of delay is computed on the ramp-shifted basis and stated as forgone, not deferred.
- An update trigger is written, with the expected date and the owner.
- Every assumption sits in a labelled input cell and appears in the sentence that uses it.

## Related skills

`spreadsheet-analysis-workbook` is the foundation this assumes; `revenue-analysis-workbook` produces the historical base and the comparables this reads. `client-economics-analysis` supplies the whitespace and replacement-revenue figures this sizes, and `revenue-concentration-risk` supplies the replacement requirement when the thing being estimated is recovery from a lost client. Downstream, `revenue-forecast` turns these estimates into the committed forward number, `financial-model-builder` embeds them in a driver-based model with costs and cash, and `economics-report-from-data` writes the argument around them. `decision-memo` is where the estimate goes when it is feeding a specific choice.
