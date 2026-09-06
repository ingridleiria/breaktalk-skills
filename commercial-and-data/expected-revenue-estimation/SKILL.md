---
name: expected-revenue-estimation
description: Estimates what something will be worth before it has a track record: five estimation methods ranked by reliability, from a direct historical average through comparable benchmarks, top-down sizing, pipeline conversion, and a bottom-up unit economics build, each with scenario bands, a sensitivity table, a stated update trigger, and the cost of delay when a launch slips. Use this skill whenever the user asks what a new programme, store, client, or initiative could be worth, for a run rate or an annualised projection, for an opportunity to be sized, for a scenario model, or for the revenue impact of a delay.
---

# Expected Revenue Estimation

An estimate is a claim about the future with a method behind it. The method is the part that can be argued with, so it is stated every time, alongside the assumption it rests on and the evidence that would change it. A single number with no method and no range is a guess wearing a suit.

This skill assumes the workbook discipline in `spreadsheet-analysis-workbook`.

## Choose the method, and say which one

Use the highest-reliability method the available data supports.

| Method | Use when | Reliability |
| --- | --- | --- |
| Direct historical average | The thing exists and has six or more months of actuals | Highest |
| Comparable benchmark | It is new, but similar things are live and measurable | High |
| Top-down sizing | The addressable pool is known and a penetration rate can be defended | Medium |
| Pipeline conversion | There is a pipeline with values and a historical close rate | Medium |
| Bottom-up unit build | Only the unit economics are known: volume, frequency, size | Medium to low |

## Method 1: direct historical average

Mean monthly revenue over the active months, with incomplete months excluded rather than averaged in. Adjust for anything known and non-recurring. Report a confidence band from the observed variability rather than a flat percentage.

## Method 2: comparable benchmark

Pick two to four comparables matched on type, customer base size, sector, and tenure. Compute each one's monthly average over its own active months, then the composite. Apply the scenario band: forty percent conservative for the ramp, seventy percent as the base once established, one hundred percent at full maturity matching the benchmark. Name the comparables in the output, because the estimate is only as defensible as they are.

## Method 3: top-down sizing

Addressable pool multiplied by a penetration rate multiplied by value per unit. The penetration rate is the whole argument, so anchor it on observed penetration among comparable populations and report the low, mean, and high observed rates rather than one chosen number.

## Method 4: pipeline conversion

```
weighted pipeline   = SUMPRODUCT(deal value, probability)
time adjusted       = only deals whose close date falls in the window
historical rate     = closed won / total entered, over a comparable prior period
converted estimate  = open pipeline * historical rate
```

Where the stage-weighted figure and the historical-rate figure disagree, report both and say which one the business has been closer to before.

## Method 5: bottom-up unit build

For a programme or a store: active users times orders per user per year times average order size. For a recurring service: accounts times revenue per account, then adjusted for churn in year one. For a new client: the comparable first-year average times a ramp factor, reaching the full comparable average in year two. Every input labelled, every input changeable.

## Cost of delay

Delayed revenue is forgone, not deferred. An initiative live in September does not recover June, July, and August. Per initiative, the monthly estimate times months lost, at all three scenario rates, then the aggregate across initiatives, then cumulative at three, six, and twelve months. Say explicitly that there is no recovery mechanism, because the instinct in the room will be to treat it as timing.

## Sensitivity, always

One-variable: the key assumption varied by thirty percent either side in steps, with the resulting estimate at each point. Two-variable: a matrix of the two assumptions that matter most. If the estimate swings by more than half across a plausible range of one assumption, that assumption is the finding, not the estimate.

## Quality standards

State the method, the key assumption, and the source of that assumption beside every estimate. Report a range, never a point. Do not annualise partial-year data in a seasonal business without saying so and saying which way it biases the number. State the update trigger explicitly: what new data would cause this to be revised, and when it will exist.

## Output

```
ESTIMATE: [initiative]
Method:        [which, and why this one]
Key assumption:[value, source]
Conservative:  [monthly] / [annual]
Base:          [monthly] / [annual]      <- the cited figure
Upside:        [monthly] / [annual]
Sensitivity:   [the assumption that moves it most, and by how much]
Cost of delay: [per month, and cumulative at 3, 6, 12 months]
Update when:   [the trigger]
```

## Quality bar

- The method named, and the reason it was chosen over a more reliable one.
- Three scenarios reported, with the base case marked as the figure to cite.
- Comparables named where the benchmark method is used.
- A sensitivity table on every estimate, and the dominant assumption identified.
- An update trigger stated, so the estimate has a stated shelf life.
