---
name: revenue-forecast
description: Builds and maintains the annual and quarterly revenue forecast from pipeline, run-rate, renewals, and capacity, reconciles it with the financial plan, and produces the forecast page leadership and the board will see. Use this skill whenever the user asks to build or update a revenue forecast, reforecast the year, reconcile bookings to plan, explain a forecast miss, prepare the forecast for a board or leadership meeting, or says "where will we land this year", "update the forecast", "how confident are we in the number", "bridge from last forecast to this one". Trigger for any projection of revenue beyond the current period; for the diagnostic analysis of the pipeline itself use pipeline-deep-dive.
---

# Revenue Forecast

The forecast is the one number the board, the CEO, and the team will remember. It has to be built from sources that can be audited, presented as a range with named assumptions, and updated on a rhythm, so that the trajectory of the forecast itself becomes information.

## Build the forecast from four layers

Each layer is estimated separately, so the reader sees what is certain and what is hoped for.

1. **Booked and contracted**: revenue already under contract for the period, by month, from signed agreements. Recognition timing matters: a $120k annual contract signed in March is not $120k of March revenue. Confirm the recognition rule with finance.
2. **Renewals and expansion**: contracts due to renew in the period, times a renewal rate from history (by segment if segments differ), plus expected expansion from the existing base at the historical net retention rate. State the rates and where they come from.
3. **Pipeline conversion**: open opportunities weighted by historical stage-to-close rates and by expected close timing, using the pipeline-deep-dive skill in this library to get honest conversion and slippage inputs. CRM default probabilities are not evidence; measured conversion is.
4. **Unidentified or run-rate**: revenue expected from deals not yet in the pipeline, estimated from the historical rate of pipeline creation and conversion within the period. Small for long sales cycles, large for transactional businesses. This layer is the most uncertain and is shown as such.

Sum the layers by month. Show the composition (how much of the year is contracted versus hoped for) as a stacked view; a forecast that is 30% contracted in October is a different conversation from one that is 80% contracted.

## Capacity check

For services and delivery-constrained businesses, the forecast cannot exceed what the team can deliver. Compare forecast revenue to billable capacity (people, utilization, rates, ramp) month by month. Where the forecast exceeds capacity, either the forecast comes down or a hiring plan with lead times is attached. Present the constraint explicitly; it is usually the most useful finding in the review.

## Scenarios and the range

Present three cases, each with the assumptions written next to it:

- **Commit**: contracted plus renewals at the historical rate plus pipeline at a conservative conversion; the number the leadership team would bet on.
- **Likely**: the base case; historical rates throughout.
- **Upside**: improved conversion or a large deal landing, only if there is specific evidence for it.

A single-point forecast is not accepted. State the likely case as the headline and the range around it.

## The bridge

Every reforecast includes a bridge from the previous forecast (or the plan) to the current one: starting number, then each change with its cause (a deal slipped, a renewal lost, pricing changed, a segment outperformed), ending at the new number. The bridge is where credibility is built or lost; it shows that changes are understood rather than absorbed.

## Presentation

The forecast page for leadership or the board:

1. Headline: likely case against plan, in one sentence, with the direction since last forecast.
2. The range with the three cases and their key assumptions.
3. The layered composition chart (contracted, renewals, pipeline, run-rate) by month or quarter, plan line overlaid. One message per chart, legend outside the plot area, monochrome or restrained palette.
4. The bridge from last forecast.
5. The capacity constraint, if binding.
6. The three actions that most improve the likely case, with owners.

Under one page plus the chart. Detailed deal lists and the full model go in the appendix or the spreadsheet, built with the financial-model-builder skill's structure.

## Cadence and accuracy tracking

- Update monthly at minimum, weekly in the final quarter, on a fixed day.
- Keep every prior forecast. Track forecast accuracy over time (likely case at each month versus actual); a forecast that is consistently 15% high in Q1 has a bias to correct, and the pattern is the correction.
- After each period, reconcile actuals to the forecast layers, so the conversion and renewal rates used next time come from measured results.

## Quality bar

- Every number traces to a contract, a rate with a stated history, or a named assumption.
- The forecast is a range, with the composition by certainty visible.
- The bridge explains every change from the last forecast.
- Capacity has been checked for delivery-constrained businesses.
- The page ends in actions that move the number.
