---
name: revenue-concentration-risk
description: Measures how exposed a business is to losing a few relationships, and how bad that would actually be: Pareto and Herfindahl concentration measures, top-N ratios against risk thresholds, an anchoring score for how costly each client would find it to leave, a fragility ranking that weights share by anchoring, a single-entity failure scenario with replacement cost and time, a portfolio revenue quality score, and the diversification gap. Use this skill whenever the user asks how concentrated their revenue is, what happens if the biggest client leaves, whether the client base is too dependent on a few accounts, or how to think about customer concentration before a raise or a sale.
---

# Revenue Concentration Risk

Concentration on its own says very little. A client at a quarter of revenue held by a multi-year integration is a different business from a client at a quarter of revenue buying order by order. This skill measures both the share and the grip, then puts a number on what losing each relationship would actually cost.

It assumes the workbook discipline in `spreadsheet-analysis-workbook` and reads the entity table built by `revenue-analysis-workbook`.

## Measuring concentration

**Pareto.** Sort entities by revenue descending, add share and cumulative share, and mark where cumulative share crosses one half and four fifths. The count of entities needed to reach four fifths is the statistic to lead with.

**Herfindahl.** The sum of squared shares times ten thousand. Below 1,500 is diversified, 1,500 to 2,500 moderate, above 2,500 concentrated, above 5,000 dominated. It is more honest than a top-five ratio because it responds to the whole distribution rather than a cut point.

**Top-N ratios.** The share held by the largest one, three, five, and ten. For a business-to-business services portfolio, the largest client above a fifth of revenue, the top three above two fifths, or the top five above three fifths each mark the high-risk band.

## Anchoring: how costly is it to leave

Score each entity out of ten from signals already in the data.

| Signal | Points |
| --- | --- |
| Active on the recurring or programme channel | 3 |
| Buys under more than three codes or lines | 2 |
| Revenue across three or more categories | 2 |
| Tenure beyond three years | 2 |
| Growing year over year | 1 |

Eight and above is deeply anchored with a high switching cost. Five to seven is moderately sticky. Two to four is relationship-dependent, which usually means dependent on one person. Zero to one is purely transactional and maximally fragile.

## Fragility: share weighted by grip

`fragility = share of revenue in points / (anchoring score + 1)`

Sort descending. The top of this list is the real risk register: large revenue with nothing holding it. A client at eight percent with no anchor outranks a client at fifteen percent with a deep one, and that inversion is the point of the whole exercise.

## The failure scenario

For each of the largest ten, model the loss with the replacement assumptions in labelled input cells.

```
revenue at risk        = entity annual revenue
share lost             = revenue at risk / total
clients to replace     = CEILING(revenue at risk / average new client revenue, 1)
replacement cost       = clients to replace * acquisition cost
months to replace      = clients to replace / new clients won per month
net economic loss      = revenue at risk + replacement cost
```

Present it as a recovery gap table: if you lose this, the gap is that, it takes this many new clients, and at the current win rate that takes this long. The time figure is what changes behaviour, more than the revenue figure.

## Revenue quality score

Out of one hundred, from three components.

- **Diversification, up to 40.** Top three below a fifth scores full marks, and the score falls in steps to zero above half.
- **Recurring adoption, up to 30.** Above two fifths of revenue on the recurring channel scores full marks, falling to zero when none of it is.
- **Trend, up to 30.** Growing above fifteen percent scores full marks, declining beyond ten percent scores zero.

Eighty and above is high quality: diversified, anchored, growing. Sixty to seventy-nine is solid with managed concentration. Forty to fifty-nine calls for action on concentration. Below forty is structurally fragile, and worth saying in those words.

## The diversification gap

Set targets for the largest share, the top three share, and minimum recurring adoption. The gap is the excess revenue above each target, expressed in currency rather than percentage points, plus the count of mid-tier clients that would have to be added to close it. That converts a risk observation into a sales target.

## Narrative patterns

- **High concentration, low anchoring.** The most dangerous case. State the share, state that nothing holds it, and give the recovery gap in months.
- **High concentration, high anchoring.** Managed risk. Name what holds it, and name what would break that hold.
- **Low concentration.** Say so plainly and move to the growth question.
- **Moving from transactional to anchored.** Frame it as revenue quality improving without revenue changing, and size the value of the shift.

## Quality bar

- Both a distribution measure and a cut-point ratio reported, never one alone.
- Anchoring scored from data signals, not from impressions of the relationship.
- The risk register ordered by fragility, not by revenue.
- The failure scenario includes replacement cost and time, not just lost revenue.
- Every threshold and assumption in a labelled input cell so a reader can retune it.
