---
name: client-economics-analysis
description: Analyses the economics of individual client relationships in any B2B revenue dataset: lifetime value on three bases, revenue trajectory and momentum, a five-dimension health score, the full cost of losing a client including replacement, expansion and whitespace sizing, net revenue retention, and a prioritisation matrix that says where to spend retention effort. Use this skill whenever the user asks about LTV, client or account health, churn and retention economics, revenue per client, which accounts are growing or at risk, upsell and expansion potential, or wants a per-client view rather than an aggregate revenue breakdown.
---

# Client Economics Analysis

Aggregate revenue hides the thing that matters. A portfolio growing ten percent can be one account expanding while eight decline. This skill works one relationship at a time: what it is worth, where it is heading, how healthy it is, what it would cost to lose it, and what is still unsold inside it.

## Workbook discipline

Every deliverable is a workbook that anyone can audit.

1. The complete raw data lives in the workbook as its own sheet. Analysis tabs never stand alone, and no formula references an external file.
2. Every calculated cell is a live formula reading from the raw sheet. `=SUMIF('Data'!$B$2:$B$40000, $A5, 'Data'!$H$2:$H$40000)`, never a pasted number. The test: change one row in the raw data and every analysis figure moves.
3. Derived fields reference the cells above them rather than recomputing from raw data. Non-programme revenue is total minus programme, not a second SUMIF with the complementary criteria, because complementary criteria rarely complement perfectly.
4. Every tab carries a visible reconciliation cell, `= SourceTotal - SUM(segments)`, which must read zero. A non-zero value means a gap or a double count, and it is surfaced before delivery.
5. Genuine inputs, such as churn assumptions, discount rates, and benchmarks, sit in labelled cells in a distinct colour and are referenced, never typed inline.
6. Each tab documents in a header note which columns it reads and from which sheet, because layouts differ between periods.

## The client revenue profile

Build one row per client, with each metric as a formula: total revenue, revenue by period, share of portfolio, first and last activity date, active months, revenue through the recurring or programme channel, that channel's share, product or service breadth, and year over year growth.

## Lifetime value

Compute all three and state which one the recommendation uses.

```
Simple            LTV = annual_revenue * expected_years
Churn adjusted    lifespan = 1 / annual_churn ; LTV = annual_revenue * lifespan
Discounted        LTV = annual_revenue / (discount_rate + churn_rate)
```

At 100,000 in annual revenue, fifteen percent churn and a ten percent discount rate, discounted LTV is 400,000. Compute LTV separately for the top, middle, and long tail tiers; the ratio between tiers is the argument for where retention money goes.

## Trajectory and momentum

Classify each client on annual direction, then on the last three months against the prior three. A client with flat annual revenue and a falling quarter is the one the annual view will not catch for another two quarters.

```
YoY          = current_period / prior_period - 1
Growing      YoY > 10%      Stable  -10% to 10%
Declining    YoY < -10%     At risk YoY < -25%
Momentum     +2 growing and rising, +1 one of the two, 0 flat,
             -1 one falling, -2 declining and falling
```

## Health score

Five dimensions, twenty points each, zero to one hundred.

| Dimension | 20 | 12 | 5 | 0 |
| --- | --- | --- | --- | --- |
| Revenue trend | growing above 10% | stable within 10% | declining 10 to 25% | declining beyond 25% |
| Recurring channel adoption | above 50% | 25 to 50% | 5 to 25% | none |
| Revenue size | top fifth of portfolio | middle | bottom two fifths | below the floor |
| Tenure | over 3 years | 1 to 3 years | 6 to 12 months | under 6 months |
| Breadth | 3 or more lines | 2 lines | 1 line | none |

Tiers: 80 and above strategic, invest in expansion; 60 to 79 core, protect and deepen; 40 to 59 developing, monitor; below 40 at risk, intervene. Every score is a nested IF reading the profile columns, never a judgement typed in.

## Cost of loss

Direct revenue is only part of it.

```
replacement_clients = CEILING(client_revenue / avg_new_client_revenue, 1)
acquisition_cost    = replacement_clients * CAC_input
cost_of_loss        = client_revenue + acquisition_cost
```

For a client with no recurring anchor, add a fragility premium: the uplift in loss probability multiplied by annual revenue. State it as a sentence a leader can act on: losing this client requires acquiring N new clients at average new client revenue, at an estimated acquisition cost of X, so the economic cost is Y.

## Expansion and whitespace

Flag each client for a location or division not yet served, a tier upgrade its volume already justifies, and a line it does not buy. Whitespace is the assumed full potential minus current revenue, with the potential assumption labelled as an input. Size the pool only across clients above the health threshold; whitespace inside an at-risk account is not an opportunity, it is a retention problem.

## Net revenue retention

`NRR = revenue this period from the clients present last period / their revenue last period`. New clients are excluded, which is the whole point. Above 110 percent is strong expansion, 100 to 110 healthy, 90 to 100 mild contraction, below 90 net contraction. NRR below 100 with growing headline revenue means acquisition is paying for churn.

## Prioritisation

Place every client in a quadrant of revenue size against health: large and healthy, protect and deepen; large and unhealthy, intervene now; small and healthy, scale the model; small and unhealthy, evaluate whether the effort earns its keep. Assign the quadrant by formula, then write the action per quadrant, not per adjective.

## Report structure

Portfolio overview with counts, total, mean and median. Health distribution by tier with client count, revenue, and share. Trajectory counts. LTV by tier with the assumptions stated. The largest risks, each with revenue, health score, and reason. The expansion list with sized whitespace. Net revenue retention with one sentence of interpretation. Then five specific client-level actions, each traceable to a figure above.

## Quality bar

- Raw data in the workbook, every analysis cell a live formula, reconciliation reading zero.
- Every assumption in a labelled input cell, never buried inside a formula.
- Health scores computed, never assigned by impression.
- Cost of loss includes replacement, not just the lost revenue.
- Every recommendation names a client and points to the number behind it.
