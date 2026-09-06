---
name: revenue-concentration-risk
description: Measures how exposed a business is to losing a few relationships and how bad that would actually be. Produces Pareto and Herfindahl measures, top-N ratios read against risk bands, an anchoring score built from data signals rather than impressions, a fragility ranking that weights share by grip, a per-client failure scenario carrying replacement cost and replacement time in months, a portfolio revenue quality score out of one hundred, and a diversification gap expressed as a sales target. Use it whenever someone asks how concentrated their revenue is, what happens if the biggest client leaves, whether the client base is too dependent on a few accounts, how a buyer or investor will see the customer book, or says something vaguer like "we are too reliant on them" or "what is our exposure here".
---

# Revenue Concentration Risk

Concentration usually gets reported as a percentage and then nothing happens. "Our top five are 62 percent of revenue" goes on a slide, the room nods, and the retention plan that follows targets the largest clients, because largest is the only ordering anyone has. That plan is often close to backwards. A client at a quarter of revenue held by a five-year framework agreement, four service lines, and an integration into their operations is not a risk; it is an asset with a renewal date. A client at eight percent buying order by order from one sponsor who could leave is the exposure, and it is nowhere near the top of a list sorted by revenue.

The second failure is that the loss is never sized in a unit anybody responds to. Told that a client worth 1.15 million might leave, a leadership team hears a number roughly the size of numbers it hears every week. Told that replacing that client requires winning nine new clients, and that at the current win rate that takes six and a half months during which nothing else is being added, the same team behaves differently. Concentration analysis that stops at the percentage produces agreement without action, which is worse than no analysis, because everyone now believes the question has been dealt with.

## When to use this, and when not to

Use it when a single client, product, or channel looks large; when a fundraise, a sale, or a bank facility is coming and the customer book will be examined by someone unsympathetic; when a retention budget has to be allocated and the ordering matters; when a large client has been lost and the question is how many more like it exist; and when concentration has already been measured but nobody changed anything.

Do not use it to produce the underlying revenue tables, which is `revenue-analysis-workbook`, or to audit the file they come from, which is `spreadsheet-analysis-workbook`. Do not use it for per-client health, lifetime value, expansion, or net revenue retention, which is `client-economics-analysis`; this skill asks only what happens if a relationship ends. Do not use it to plan the recovery of a specific lapsed account, which is `account-reengagement-plan`, or to write the board narrative, which is `economics-report-from-data`.

## What you need before starting

**A reconciled entity revenue table.** One row per client, with revenue by period, total, and share, reconciling to a ground truth. Missing: build it first with `revenue-analysis-workbook`. Concentration computed on an unreconciled table is a number nobody can defend when it is challenged, and it will be challenged.

**A channel or contract flag per client.** Whether revenue arrives under a recurring arrangement or one order at a time. This is the single strongest anchoring signal. Missing: substitute a proxy such as invoicing regularity, count the months in which a client invoiced, and label it a proxy in the header note.

**Product or service breadth per client.** The count of distinct lines, codes, or categories bought. Missing: derive it from the transaction extract with a `COUNTIFS` over distinct codes; if the extract has no code column, drop the signal and rescale the anchoring score, saying so.

**Tenure, from first activity date.** Missing: use the earliest date in the extract and mark tenure as censored, since the extract may begin after the relationship did. Censored tenure understates anchoring, which is the safe direction.

**Average revenue per new client won, over the last twelve months.** This is the denominator of the replacement calculation and it does the most work in the whole model. Missing: use the median of clients acquired in the period rather than the mean, because a single large win distorts the mean and understates the number of replacements needed.

**Acquisition cost per new client, and new clients won per month.** Missing: ask sales for both; where neither exists, use a range and label it, because the months-to-replace figure is what changes behaviour and a range still changes it. Never present a precise figure derived from an invented input.

**Contract end dates, where contracts exist.** Missing: proceed without them and note that the timing dimension is absent, which matters most in exactly the portfolios that look safest.

## The method

This inherits the discipline in `spreadsheet-analysis-workbook` and does not repeat it. In short: the complete raw data lives in the workbook as its own sheet; every analysis cell is a live formula reading from it; derived fields reference computed cells rather than recomputing independently; a visible reconciliation cell on every tab reads zero; assumptions sit in labelled input cells rather than inside formulas; and every tab documents which columns it reads, from which sheet, and which row the data starts on. Every threshold below is an input cell so a reader can retune it and watch the ranking move.

1. **Build the ranked distribution.** Sort the entity table descending by revenue, add share and cumulative share, and mark the rows where cumulative share crosses one half and four fifths. Lead with the count of clients needed to reach four fifths rather than any ratio: a number of relationships travels further in a meeting than a percentage does.

2. **Compute both a distribution measure and a cut-point measure, never one alone.** Top-one, top-three, top-five, and top-ten shares give the cut points; the Herfindahl index gives the distribution.

   ```
   Top three share  =SUMPRODUCT(LARGE($E$12:$E$107,ROW(INDIRECT("1:3"))))/$E$8
   Herfindahl       =SUMPRODUCT(($F$12:$F$107)^2)*10000
   ```

   Read the index against bands: below 1,500 diversified, 1,500 to 2,500 moderate, above 2,500 concentrated, above 5,000 dominated. The index is the more honest of the two because it responds to the whole distribution rather than to where the cut happens to fall, and a portfolio can pass a top-five test while failing the index. For business-to-business services, the high-risk bands are a largest client above a fifth of revenue, a top three above two fifths, or a top five above three fifths.

3. **Score anchoring out of ten, from data signals only.** The rule that matters: no signal enters the score unless it can be computed from the extract. Impressions of how sticky a relationship feels are systematically optimistic, and they are most optimistic about the relationships in most danger.

   | Signal | Points |
   | Active on the recurring or contract channel | 3 |
   | Buys under more than three codes or lines | 2 |
   | Revenue across three or more categories | 2 |
   | Tenure beyond three years | 2 |
   | Growing year on year | 1 |

   ```
   =IF($H12>0,3,0)+IF($I12>3,2,0)+IF($J12>=3,2,0)+IF($K12>36,2,0)+IF($L12>0,1,0)
   ```

   Eight and above is deeply anchored, with a high switching cost on the client's side. Five to seven is moderately sticky. Two to four is relationship-dependent, which in practice usually means dependent on one person on each side. Zero to one is purely transactional and maximally fragile.

4. **Compute fragility and rank by it.** Fragility is share weighted by the inverse of grip.

   ```
   =IFERROR($F12*100/($M12+1),0)
   ```

   Sorted descending, this is the real risk register. A client at eight percent with no anchor outranks a client at fifteen percent with a deep one, and that inversion is the entire point of the exercise. Where the fragility ranking and the revenue ranking agree at the top, say so explicitly, because that is a materially worse position than the usual case and it is easy to miss when the list looks conventional.

5. **Model the failure scenario for the top ten by fragility, not by revenue.** Every assumption in a labelled input cell.

   ```
   revenue at risk     =$E12
   share lost          =$E12/$E$8
   clients to replace  =CEILING($E12/Inputs!$B$4,1)
   replacement cost    =$N12*Inputs!$B$5
   months to replace   =IFERROR($N12/Inputs!$B$6,"n/a")
   net economic loss   =$E12+$O12
   ```

   Present it as a recovery gap: lose this, the gap is that, it takes this many new clients, and at the current win rate that takes this long. State the months figure in the sentence, because it is the one that changes behaviour. Add the sentence that makes it real: during those months the sales team is replacing lost revenue rather than adding new revenue, so the growth plan pauses.

6. **Score portfolio revenue quality out of one hundred**, from three components, each computed by nested `IF` against input-cell thresholds rather than assigned.

   Diversification, up to 40: a top-three share below a fifth scores full marks, falling in steps to zero above half. Recurring adoption, up to 30: above two fifths of revenue on the recurring channel scores full marks, falling to zero at none. Trend, up to 30: growth above fifteen percent scores full marks, decline beyond ten percent scores zero.

   Eighty and above is high quality, diversified, anchored, and growing. Sixty to seventy-nine is solid with managed concentration. Forty to fifty-nine calls for action on concentration. Below forty is structurally fragile, and worth saying in those words rather than softer ones.

7. **Compute the diversification gap and convert it into a target.** Set targets for the largest share, the top-three share, and minimum recurring adoption. The gap is the excess revenue above each target, expressed in currency rather than percentage points, plus the count of mid-tier clients that would have to be added to close it at the current average new client size. That last number is the one the sales director can plan against, and it is what turns a risk observation into a quota.

8. **Write the narrative to the pattern the numbers fall into,** rather than describing every measure in turn. The four patterns are below.

## Narrative patterns

**High concentration, low anchoring.** The dangerous case and the one worth the most words. State the share, state plainly that nothing holds it, and give the recovery gap in months. Recommend the specific anchoring move: a contract, a second service line, a second sponsor inside the account. Anchoring a client is usually cheaper than replacing one, and the fragility table shows which clients repay it fastest.

**High concentration, high anchoring.** Managed risk, not absent risk. Name what holds it, then name what would break that hold: a contract expiry, a change of sponsor, an acquisition of the client, a procurement review. Convert the analysis into a renewal calendar and a named-relationship map rather than a retention budget.

**Low concentration.** Say so in one sentence and move to the growth question. Manufacturing a concern here spends credibility you will want later.

**Moving from transactional to anchored.** Frame it as revenue quality improving while revenue is flat, size the shift in quality-score points and in fragility reduction, and say what it would be worth in a valuation conversation. This is the pattern most often missed, because nothing in the headline revenue figure moves.

## Worked example

**Situation.** Trevane Managed Services, an IT managed services firm of about 130 people, had 14.2 million of revenue across 96 clients and was eighteen months from a likely sale. The chair had asked for a concentration analysis after a diligence conversation went badly on a smaller deal elsewhere. The largest client, a regional hospital group, held 23.4 percent of revenue and everyone in the leadership team named it immediately when asked where the risk was.

**Task.** A concentration and exposure workbook in a week, and a retention priority list the sales director would actually work from.

**Action.** The distribution was built first from the reconciled entity table. Eleven clients of 96 held half of revenue and 34 held four fifths. The Herfindahl index came out at 2,810, in the concentrated band, and the top-three share at 41.2 percent, just over the high-risk threshold. So far this confirmed what the room believed.

The first version of the retention plan ranked by revenue and put the hospital group at the top. That version was abandoned after the anchoring scores were computed. The hospital group scored 9 out of 10: a five-year contract with three years remaining, seven service lines, six years of tenure, and growing. Its fragility came out at 2.34. The fourth-largest client, a distribution business at 8.1 percent of revenue, scored 1: no contract, one service line, twenty-six months of tenure, and declining eleven percent year on year. Its fragility was 4.05, the highest in the portfolio, and it was not in anyone's top three worries. Two more clients in positions seven and nine scored 2 and 1 respectively and ranked second and fourth on fragility.

There was an earlier wrong turn worth recording. The first attempt at anchoring scored each account by asking its account manager three questions about stickiness. The results were unusable: every account manager rated their own accounts sticky, the scores had almost no variance, and the two accounts that had been lost in the previous year would both have scored highly under that method a month before they left. The scoring was rebuilt entirely from data signals already in the extract, which took less time than the interviews had.

The failure scenarios were then run for the top ten by fragility. Average revenue per new client won over the previous twelve months was 128,000 on a median basis, acquisition cost 22,000, and new clients won 1.4 per month. Losing the distribution client at 1.15 million meant replacing nine clients at a cost of 198,000, taking 6.4 months at the current win rate, with a net economic loss of 1.35 million. The equivalent for the hospital group was 26 clients and 18.6 months, which is the figure that made everyone quiet, but it sat behind a contract with three years to run.

The revenue quality score came out at 54: diversification 14 of 40, recurring adoption 22 of 30, trend 18 of 30. Below sixty, in the band that calls for action on concentration.

**Result.** The retention plan was rebuilt around fragility. The distribution client was moved onto a twelve-month agreement with a second service line inside seven weeks, which took its anchoring score from 1 to 6 and its fragility from 4.05 to 1.16 without changing its revenue by anything. Two of the other four high-fragility clients were anchored over the following two quarters; one declined and was reclassified as expected attrition with a replacement plan attached; one was lost, at 340,000, which the recovery gap had sized at three clients and 2.1 months and which therefore surprised nobody.

The diversification gap was 1.71 million of revenue above the top-three target, which converted to thirteen mid-tier clients at the current average size. That became the following year's new-business target rather than a percentage on a slide.

The number the chair used in the sale conversation was not the concentration ratio. It was that the top client sat under a contract with three years to run and seven service lines, evidenced from the data, alongside a quality score that had moved from 54 to 63 in nine months. Whether that materially changed the price is not known; it did change the questions.

### A second scenario, where it goes differently

An engineering design firm of 40 people, 6.8 million of revenue, two clients holding 71 percent between them, both under ten-year framework agreements, both anchored at 9 out of 10. The Herfindahl index is 5,940, deep in the dominated band.

Here the fragility ranking is nearly useless. Both large clients score almost identically, the ordering between them is noise, and the register produced is a list of two names everybody already knows. The method has to change rather than be reported. Three things replace the ranking: a renewal calendar showing every framework expiry and re-tender date on one timeline, because in this portfolio the risk is entirely a matter of dates; a named-person map showing which individual on each side holds the relationship and what happens if they move, since a framework agreement does not survive a hostile procurement review; and a scenario run at the framework level rather than the client level, because these clients do not leave, they re-tender, and the realistic downside is a margin reduction on renewal rather than a total loss.

What changed is that concentration and anchoring are both extreme, which removes the variance the fragility ranking depends on. The measurement steps still run; the register is replaced by a calendar.

## Output

A workbook and a one-page summary. The risk register is the deliverable that gets used.

| Rank | Client | Revenue | Share | Anchor /10 | Fragility | Clients to replace | Months to replace | Action |
| 1 | Northgate Distribution | 1,150,400 | 8.1% | 1 | 4.05 | 9 | 6.4 | contract plus second line |
| 2 | Perrin Retail | 604,900 | 4.3% | 1 | 2.15 | 5 | 3.6 | contract |
| 3 | Halcyon Foods | 812,300 | 5.7% | 2 | 1.90 | 7 | 5.0 | second sponsor |
| 4 | Kestrel Components | 498,100 | 3.5% | 1 | 1.75 | 4 | 2.9 | monitor |
| 5 | Braddon Hospital Group | 3,322,800 | 23.4% | 9 | 2.34 | 26 | 18.6 | renewal calendar |

The summary block carries the measures and the verdict.

```
CONCENTRATION SUMMARY
Clients:                96        Revenue: 14,201,300
Clients to 50% / 80%:   11 / 34
Top 1 / 3 / 5 / 10:     23.4% / 41.2% / 52.8% / 68.9%
Herfindahl:             2,810     band: concentrated
Revenue quality:        54 / 100  (diversification 14, recurring 22, trend 18)
Highest fragility:      Northgate Distribution, 8.1% share, anchor 1
Diversification gap:    1,710,000 above top-three target, 13 mid-tier clients to close
Assumptions:            avg new client 128,000 (median); CAC 22,000; win rate 1.4/month
```

## Failure modes

**Ranking the risk register by revenue.** Recognise it when the largest client is at the top. Rank by fragility and show both columns, so the inversion is visible rather than asserted.

**Scoring anchoring from impressions.** Recognise it when scores cluster high and have little variance, or when the people scoring are the people who own the relationships. Score from data signals; where a signal is unavailable, drop it and rescale rather than substituting a judgement.

**Reporting a ratio without a distribution measure.** Recognise it when the only statistic is a top-five share. A portfolio can pass a top-five test and still be dominated by one relationship inside that five.

**Sizing the loss only in revenue.** Recognise it when the output has no months in it. Replacement time is the figure that moves a leadership team, and it is the figure a reader cannot compute themselves.

**Precise replacement figures built on invented inputs.** Recognise it when the acquisition cost is a round number nobody can source. Use a range, label it, and show the months-to-replace at both ends.

**Treating anchoring as permanent.** Recognise it when a contract is cited with no expiry date beside it. Every anchor has a date or a person behind it, and both change.

**Confusing concentration with dependency.** A client that is large but easily replaced from a deep market is a different problem from a client that is large and irreplaceable because it is the only buyer of that capability. Say which, since the responses have nothing in common.

**Producing agreement instead of a decision.** Recognise it when the output ends in a percentage. End in a named client, a named action, and a date.

## Edge cases

**Fewer than fifteen clients.** The Herfindahl index and the top-N ratios both become unstable, and a single win moves them by hundreds of points. Report the full distribution instead, one line per client, and use the failure scenario as the primary analysis rather than the concentration measures.

**Concentration in a channel, a product, or a geography rather than a client.** The method transfers unchanged with the entity redefined; the anchoring signals change, since what holds a channel is a route to market or a platform integration rather than a contract. Say in the header note which dimension the entity represents.

**Revenue concentrated in a client that is itself an intermediary.** A distributor or a prime contractor carrying many end customers is a different exposure: the anchoring lives with the end customers, not with the intermediary. Score both levels where the data allows, and where it does not, say that the analysis is blind below the intermediary.

**A client that is large because of a one-off project.** Exclude non-recurring project revenue from the concentration measures, report it separately, and show the concentration figures both ways. Including a completed project overstates exposure to a relationship that has already ended.

**A group of clients under common ownership.** Aggregate them before ranking. Three subsidiaries at seven percent each are one relationship at twenty-one percent and one procurement decision, and the ownership check is worth the twenty minutes it takes.

**Deliberate concentration.** Some businesses concentrate on purpose, in exchange for scale or margin. Say so, measure it anyway, and shift the output to the terms of that bet: what the strategy assumes, what would falsify it, and what the recovery plan is if it fails.

## Quality bar

- Both a distribution measure and a cut-point ratio are reported, with the bands they are read against.
- Anchoring is scored from data signals that can be recomputed, with the signal list visible.
- The risk register is ordered by fragility, with the revenue rank shown alongside it.
- Every failure scenario carries replacement cost and replacement time in months, not just lost revenue.
- Every threshold and replacement assumption sits in a labelled input cell and is stated in the summary.
- Clients under common ownership are aggregated before ranking.
- The output ends in named clients, named actions, and a diversification target expressed in clients to win.

## Related skills

`revenue-analysis-workbook` builds the entity table and the concentration tab this skill starts from, and `spreadsheet-analysis-workbook` is the foundation both assume. `client-economics-analysis` covers the other half of the per-client picture: health, lifetime value, expansion, and net revenue retention, where this skill covers only exposure to loss. `account-reengagement-plan` acts on a specific account this analysis flags. `economics-report-from-data` turns the register into the board narrative, and `expected-revenue-estimation` sizes what replacing a lost client would realistically produce and by when. `fundraise-readiness` and `board-deck` consume the quality score and the diversification gap directly.
