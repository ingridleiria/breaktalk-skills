---
name: revenue-forecast
description: Builds and maintains the revenue number for the current year and quarter, assembled in four layers of decreasing certainty from contracted revenue through renewals, pipeline conversion, and unidentified run-rate, checked against delivery capacity, presented as a range with named assumptions, and carrying a bridge that explains every change since the last version. Enforces the standard that no figure enters the forecast without a contract, a measured rate, or a labelled assumption behind it, and that the forecast is reconciled to plan and to actuals on a fixed cadence. Use this skill whenever someone asks to build or update the revenue forecast, reforecast the year, reconcile bookings to plan, explain a forecast miss, prepare the forecast page for a board or leadership meeting, or says where will we land this year, update the number, how confident are we, what changed since last month, are we going to make plan.
---

# Revenue Forecast

A forecast loses its authority the third time it moves without an explanation. In August the year lands at 11.2 million dollars, in September at 10.4 million, in October at 10.9, and nobody in the room can say what happened between the versions. The board stops treating the number as information and starts applying its own reduction to it, usually somewhere between ten and twenty percent, applied silently and never discussed. From that point the company is run on two forecasts: the one the team produces and the one the board privately believes.

The cost is not the arithmetic. It is that every decision downstream is made on a number nobody owns. Hiring gets approved against optimism and paused against panic, both late. Cash is managed to a figure that has no stated confidence attached. And the one quarter when the forecast is right and the team says so with conviction, nobody acts on it, because the signal is indistinguishable from the previous four.

The fix is structural. Build the number in layers so the reader can see what is contracted and what is hoped for, present it as a range with the assumptions named, and attach a bridge that accounts for every movement since the last version.

## When to use this, and when not to

Use it to build or update the revenue forecast for the current year or quarter, to prepare the forecast page for a board or leadership meeting, to reconcile bookings against plan, to explain a miss after the fact, or to answer a direct question about where the year lands.

The boundaries against the neighbouring numeric skills matter, because a request for "the numbers" could mean any of them:

- `pipeline-deep-dive` diagnoses the opportunity set itself: coverage, stage conversion, velocity, concentration, hygiene. It works on data that already exists and it produces the measured conversion and slippage rates that this skill uses as inputs. If the question is why deals are stalling or which deals to work this week, that skill owns it.
- `financial-model-builder` is the company model across revenue, cost, headcount, and cash over multiple years. This skill produces one line of that model, in more detail and on a shorter cycle, and uses its workbook structure.
- `pricing-and-resourcing-model` prices a single engagement and staffs it. Its output can become one line in the contracted layer here, but it is not a forecast.
- `annual-planning-and-headcount` sets the plan this forecast is measured against. Once the plan is signed, this skill tracks against it and does not rewrite it.

Do not use this to set next year's target, which is a planning exercise with different inputs. Do not use it to forecast a business with no sales history and no pipeline; that is `expected-revenue-estimation`. Do not produce a forecast at all where the underlying pipeline data has not been cleaned, because a forecast built on unhygienic data inherits its errors and lends them false authority.

## What you need before starting

**The plan or target for the period, by month or quarter.** The forecast has no meaning without the thing it is measured against. Missing: ask for the board-approved figure specifically, since the number in the model and the number the board holds are often different, and the difference is itself worth reporting.

**Contracted revenue, with recognition timing.** Signed agreements and what portion falls in the period. Missing: get the contract list from finance rather than from the sales system, because a booking is not revenue and the two systems disagree.

**Historical renewal and net retention rates,** by segment where segments behave differently. Missing: use the overall rate and say so; if there is no history at all, use the owner's estimate, label it, and mark that layer as unverified.

**Measured stage-to-close conversion and slippage rates,** from `pipeline-deep-dive`. Missing: run that skill first. If there is no time, use the crude alternative, which is total closed-won divided by total opportunities created in comparable prior periods, and state that stage detail was unavailable.

**Delivery capacity,** for any business where revenue requires people to deliver it. Missing: ask for the billable headcount plan and utilisation assumption, because a forecast above capacity is not a forecast.

**The previous forecast version.** Without it there is no bridge, and the bridge is where credibility is built. Missing: use the plan as the starting point for the bridge and say the previous version was unavailable.

## The method

1. **Fix the period, the plan figure, and the recognition rule** before touching data. Write all three at the top of the workbook. Ambiguity about whether the forecast is bookings or revenue accounts for a large share of forecast disputes.

2. **Build each of the four layers defined below separately, in its own block,** with its inputs in labelled cells. Contracted from the contract list, renewals from the renewal book times a rate, pipeline from the opportunity list times measured conversion, unidentified from creation rate times conversion. Never blend two layers in one calculation.

3. **Reconcile each layer to its source.** The contracted layer must sum to the contract list total for the period. The renewal layer must sum to the renewal book times the stated rate. Put a visible reconciliation cell on each block that reads zero. A layer that does not tie to its source is a layer somebody has adjusted by hand.

4. **Check capacity where delivery constrains revenue.** Compare monthly forecast revenue against billable capacity, which is people multiplied by utilisation multiplied by rate, allowing for ramp. Where forecast exceeds capacity, either the forecast comes down or a hiring plan with lead times is attached to it. Present the constraint explicitly. In services businesses this is usually the most useful finding in the whole review.

5. **Build three cases, each with its assumptions written beside it.** Commit is contracted plus renewals at the measured rate plus pipeline at a conservative conversion, and it is the number the leadership team would bet on. Likely uses measured rates throughout and is the headline. Upside requires specific named evidence, such as one identified deal with a signed term sheet, not a general improvement in conversion. The rule: any case you cannot attach a named cause to is not a case, it is a multiplier.

6. **Build the bridge from the previous version.** Start at the last forecast, then one line per change with its cause and value, ending at the new number. Causes are specific: a named deal slipped, a renewal was lost, a segment converted above rate, pricing changed. A line reading "pipeline reassessment" is an admission that the change is not understood. The bridge is what experienced readers turn to first, because it reveals whether movement is understood or merely absorbed: a drop of 600,000 dollars with four lines naming four deals is a team in control of its number, while the same drop under one line reading "revised assumptions" is a team presenting a surprise as an analysis. Include upward movements too.

7. **Reconcile the total to the financial model.** The forecast revenue line and the model's revenue line must agree, or the difference must be explained in one sentence. Two live revenue numbers in one company is how a plan and a forecast drift apart unnoticed.

8. **Identify the three actions that most improve the likely case,** each with an owner and a date. A forecast that ends at a number is a report. A forecast that ends in actions is a management tool.

9. **Record this version and set the cadence.** Store the likely case with its date, keep every prior version, and update monthly on a fixed day, weekly in the final quarter. The fixed day matters more than the frequency, because a forecast produced on request is a forecast produced under pressure to say something particular. At period end, compare each layer against actuals and update the rates used next time. Track the likely case at each month against the eventual actual: a team that runs fifteen percent high in the first quarter and accurate by the third does not have a forecasting problem, it has a known bias, and naming the bias converts a credibility problem into an adjustment.

## The four layers

Each layer is estimated separately and shown separately, so the reader can see certainty decline down the stack.

1. **Contracted.** Revenue already under signed contract for the period, spread by month on the recognition rule confirmed with finance. A 120,000 dollar annual contract signed in March is not 120,000 dollars of March revenue, and getting this wrong is the most common single error in a first forecast.
2. **Renewals and expansion.** Contracts due to renew in the period multiplied by the measured renewal rate, plus expected expansion from the existing base at the historical net retention rate. State both rates and the period they were measured over.
3. **Pipeline conversion.** Open opportunities weighted by measured stage-to-close conversion and by expected close timing after slippage. Customer relationship management system default probabilities are not evidence; measured conversion is. Where the two differ, show both and explain which you used.
4. **Unidentified.** Revenue expected from deals not yet created, estimated from the historical rate of pipeline creation and within-period conversion. Small for long sales cycles, large for transactional businesses. This layer is the most uncertain and is always shown as the top band of the stack.

Sum by month. Show the composition as a stacked view: a year that is thirty percent contracted in October is a different conversation from one that is eighty percent contracted, and the composition, not the total, is what should drive the discussion.

## Worked example

**Situation.** A business software company with about 9.1 million dollars in annual recurring revenue and a plan of 12.4 million dollars in total revenue for the year. All figures in this example are US dollars. In early October the forecast presented to the board was 11.9 million dollars, produced by summing weighted pipeline using the values the sales system reported. The chief financial officer had asked twice how the number was built and had not received an answer she could follow.

**Task.** Produce a forecast for the remaining quarter that the leadership team could defend line by line, ahead of a board meeting eighteen days away, and explain the gap to plan if there was one.

**Action.** The first build used the sales system's own probability field, which is what had produced the 11.9 million dollar figure. Running `pipeline-deep-dive` first showed why that was wrong: measured stage-to-close conversion from the eighty-one closed opportunities of the previous four quarters was 34 percent at proposal against a system default of 60, and 11 percent at qualification against a default of 25. The defaults had never been recalibrated after a segment change eighteen months earlier.

Rebuilt in layers, the picture changed. Contracted revenue for the year was 8.6 million dollars, of which 7.9 million was already recognised through September. Renewals due in the quarter were 1.4 million dollars at a measured renewal rate of 89 percent, giving 1.25 million, with expansion at 104 percent net retention adding 0.11 million. Open pipeline of 4.3 million dollars gave 0.94 million once conversion was recalibrated and slippage applied, against the 2.04 million the system defaults implied. Of that 1.10 million difference, 0.76 million was the conversion recalibration and 0.34 million was two named deals moving out of the quarter. The unidentified layer was near zero, because the average cycle was 94 days and only 12 days of the quarter remained within a full cycle.

The four layers summed to a likely case of 10.9 million dollars, which is 8.6 contracted plus 1.25 renewals plus 0.11 expansion plus 0.94 pipeline, against a plan of 12.4 million, with commit at 10.4 million and upside at 11.3 million, the upside resting on one named renewal expansion with an order form pending countersignature rather than on a general improvement.

The wrong turn: the first version of the pipeline layer applied one blended conversion rate across all segments, producing 1.31 million dollars, which looked reasonable. Splitting by segment showed the blend hiding two opposite errors. Mid-market converted at 41 percent; enterprise, carrying 68 percent of the open value, converted at 19 because those deals required a security review nobody had scheduled. The blended rate was arithmetically defensible and practically misleading, and the split is what turned the forecast into an action.

**Result.** 10.9 million dollars likely, with the composition showing 79 percent of the year contracted and 9 percent resting on pipeline. The bridge carried four lines against the 11.9 million previously presented: recalibrated conversion at negative 0.76 million, two named deals slipped at negative 0.34 million, one renewal lost at negative 0.09 million, one expansion signed at plus 0.19 million. Those four movements sum to negative 1.0 million exactly, which is the whole of the distance from 11.9 to 10.9.

The board conversation moved off the number within ten minutes and onto the security review backlog, which was the real constraint on the enterprise segment and had never surfaced as a revenue issue. Two reviewers were contracted the following week. The year closed at 11.1 million dollars, inside the range, which mattered less than the fact that the next quarter's forecast was believed on first presentation.

### A second scenario, where it goes differently

A transactional business selling to small companies, average deal value 4,200 dollars, average cycle eleven days. The layer weighting inverts. Contracted revenue for the quarter is trivial, the pipeline layer covers only the next fortnight, and the unidentified layer carries more than half the number, which makes this a marketing forecast wearing a sales label.

The method adapts in two ways. The unidentified layer is built properly, from lead volume by channel multiplied by measured lead-to-opportunity and opportunity-to-close rates, rather than left as a residual. And the cadence tightens to weekly all year, because with an eleven-day cycle a month is a third of a quarter's information. The capacity check that dominated the services case is irrelevant; the constraint here is demand, not delivery.

## Output

One page for leadership or the board, with the workbook behind it.

```
REVENUE FORECAST, [period]                     Version [n], [date]

HEADLINE
Likely case [x] against plan [y], a gap of [z].
Direction since last forecast: [up / down] [amount], driven by [one cause].

THE RANGE
| Case   | Number | What it assumes |
| Commit |  |  |
| Likely |  |  |
| Upside |  | [the named evidence, not a multiplier] |

COMPOSITION, by month
| Month | Contracted | Renewals and expansion | Pipeline | Unidentified | Total | Plan |
Percentage of the period contracted: [ ]

BRIDGE FROM LAST FORECAST
| From [last version] | [amount] |
| [named cause] | +/- |
| [named cause] | +/- |
| To [this version] | [amount] |

CAPACITY
Forecast revenue against billable capacity by month. Binding in [months], or not binding.

THE THREE ACTIONS THAT MOVE THE LIKELY CASE
| Action | Owner | By when | Effect on likely case |
```

The stacked composition chart carries one message stated in its title, with the plan line overlaid, the legend outside the plot area, monochrome with the layers separated by fill texture rather than colour, and at most one accent used for the plan line. Deal-level detail, the renewal book, and the full workbook go in the appendix.

## Failure modes

**System probabilities used as conversion rates.** Recognise it because the weighted pipeline number is suspiciously close to the target. Fix by measuring conversion from closed history, and if history is thin, say so rather than borrowing the default.

**A blended rate hiding two opposite errors.** Recognise it when one segment carries most of the open value but the rate applied is an average across all segments. Fix by splitting on the dimension that carries the concentration.

**The bridge line that explains nothing.** "Reforecast" or "revised assumptions" as a cause. Recognise it instantly. Fix by decomposing until every line names a deal, a rate, or a decision.

**A forecast above delivery capacity.** Recognise it by comparing forecast revenue to billable days available. Fix by cutting the forecast or attaching a hiring plan with lead times, and never by assuming utilisation above what the team has ever achieved.

**Silent smoothing.** A forecast held flat because a drop would be awkward, with the shortfall pushed into the final month. Recognise it by a monthly profile that rises sharply at the end for no named reason. Fix by reporting the drop when it is known, because it will be reported by arithmetic eventually.

## Edge cases

**No pipeline history at all,** a new product or a new segment. Build the contracted and renewal layers normally, present the pipeline layer as a range from zero to full conversion, and state that the range is wide because there is no rate to apply. Do not invent a benchmark conversion rate and present it as measured.

**One deal dominates the quarter.** Where a single opportunity is more than a quarter of the forecast, the forecast is that deal's forecast. Present it separately, above the layers, with its own probability reasoning, and show the number with and without it.

**The plan is already unreachable.** Say so in the first line, with the gap and the date at which it became unreachable. A forecast that keeps presenting an achievable-looking path to a plan everyone privately knows is dead costs more credibility than the miss does.

**Mid-period change to the target.** Keep both lines visible for the rest of the year, the original plan and the revised one, and bridge to each. Quietly replacing the target is how a miss becomes invisible and how the next plan loses its meaning.

## Quality bar

- Every figure traces to a contract, a rate measured over a stated period, or a labelled assumption.
- The four layers are shown separately, with the contracted percentage of the period stated.
- The forecast is a range of three named cases, and the upside rests on named evidence.
- The bridge accounts for every movement since the last version, each line naming a deal, a rate, or a decision.
- Every layer block carries a reconciliation cell reading zero against its source.
- Capacity has been checked wherever delivery constrains revenue, and the constraint is stated as binding or not.
- The forecast total agrees with the revenue line in the financial model, or the difference is explained in one sentence.
- The page ends in three actions with owners and dates.

## Adapting this to your context

The four layers, the monthly cadence and the capacity check come from software and professional services companies with sales cycles of weeks to months. The structure travels; the weightings do not.

- **The relative size of the layers.** This example is 79 percent contracted with the unidentified layer near zero. A transactional business inverts that: build the unidentified layer from channel volumes and treat pipeline as a fortnight of visibility.
- **Monthly, weekly in the final quarter.** Match the cadence to the sales cycle, not the calendar. An eleven-day cycle needs weekly all year; a nine-month enterprise cycle needs monthly on a fixed day that never moves.
- **The capacity check.** Written for businesses where people deliver the revenue. In product businesses, replace it with the constraint that actually binds, which is usually demand, supply or a certification date.
- **Recognition timing.** The example assumes subscription revenue spread over a term. Usage-based, milestone-based and percentage-of-completion revenue each need a rule agreed with finance and written at the top of the workbook.
- **What not to change.** Every figure traces to a contract, a measured rate or a labelled assumption, and the bridge accounts for the whole movement with each line naming a deal, a rate or a decision.

## Related skills

`pipeline-deep-dive` produces the measured conversion, slippage, and coverage inputs for the pipeline layer, and should run before this skill whenever the pipeline layer is material. `financial-model-builder` supplies the workbook structure and holds the wider company model this forecast reconciles to. `annual-planning-and-headcount` sets the plan this is measured against and consumes the capacity finding. `pricing-and-resourcing-model` prices the individual engagements that enter the contracted layer. `expected-revenue-estimation` covers forecasting something with no history. `board-deck` and `investor-update` carry this page to their audiences, and `weekly-status-update` carries the in-quarter movement between formal versions.
