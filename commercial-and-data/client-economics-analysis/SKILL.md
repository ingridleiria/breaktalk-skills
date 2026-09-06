---
name: client-economics-analysis
description: Analyses the economics of individual client relationships in any business-to-business revenue dataset: a per-client revenue profile, lifetime value computed on three bases with the churn rate taken from the data rather than a benchmark, trajectory and momentum, a five-dimension health score computed by formula, the full cost of losing a client including replacement, expansion and whitespace sizing gated on health, net revenue retention on a true cohort, and a prioritisation matrix that says where retention effort goes. Use it whenever someone asks about LTV, account or client health, churn and retention economics, revenue per client, which accounts are growing or at risk, upsell and expansion potential, or wants a per-client view rather than an aggregate revenue breakdown, including vague versions like "how are our accounts doing" or "where should the account team spend its time".
---

# Client Economics Analysis

Aggregate revenue hides the thing that matters. A portfolio growing ten percent can be one account expanding by two million while eight others quietly decline, and the headline will look identical to a portfolio where every relationship is healthy. The difference shows up two or three quarters later, when the expanding account finishes its programme and the decline underneath becomes the whole story. By then the retention window on the eight has closed, because a client that has been shrinking for four quarters has usually already chosen.

The second failure is a single lifetime value figure quoted with no method behind it. A blended LTV computed from a benchmark churn rate gets used to justify an acquisition cost, and it is routinely wrong by a factor of three, in different directions for different tiers of the same portfolio. Money then flows toward acquiring clients that the economics cannot support, and away from retaining the ones that carry the business. Nobody notices, because the blended figure keeps working as an average while being false for every client it describes.

## When to use this, and when not to

Use it when the question is about relationships rather than totals: which accounts are worth what, which are at risk, where expansion is real, whether retention is holding, and where an account team's hours should go. Use it before setting an acquisition budget, since the number that budget should be judged against comes from here.

Do not use it to build the underlying revenue tables, which is `revenue-analysis-workbook`, or to audit the file behind them, which is `spreadsheet-analysis-workbook`. Do not use it to measure exposure to losing a few relationships, which is `revenue-concentration-risk`; that skill asks what happens if a client leaves, this one asks what each client is worth and how it is doing. Do not use it to build a recovery plan for one lapsed account, which is `account-reengagement-plan`, or to write the narrative, which is `economics-report-from-data`.

## What you need before starting

**A reconciled entity revenue table with dates.** One row per client, revenue by period, first and last activity. Missing: build it first; per-client economics on an unreconciled table produces confident numbers that do not sum to anything.

**A channel or contract flag.** What separates revenue that arrives without a new selling motion from revenue that requires one each time. Missing: use invoicing regularity as a proxy, count the months in which each client invoiced, and label it a proxy everywhere it is used.

**Observed churn, by tier.** The proportion of clients present in one period and absent in the next, computed from the data, separately for the top, middle, and long tail. Missing: this is the input most often substituted with a benchmark, and doing so is the most expensive shortcut in the method. If the series is too short to observe churn, say so and present lifetime value as a range across a stated churn band rather than a figure.

**A discount rate.** Missing: use the business's own cost of capital if anyone knows it, otherwise ten percent, in a labelled input cell, and show the sensitivity of LTV to it.

**Acquisition cost and average revenue per new client won.** Missing: ask sales; where the figures do not exist, use ranges and label them. The cost-of-loss sentence still works with a range and does not work with a fabricated point estimate.

**Product or service breadth per client.** Missing: derive from distinct codes in the extract; if there is no code column, drop the breadth dimension of the health score and rescale to eighty, saying so on the tab.

**A defined dormancy window.** How long a client goes without buying before it counts as gone. Missing: set it at twice the median inter-purchase interval observed in the data, and state it. Every churn and retention figure in the workbook depends on this one number.

## The method

This inherits the discipline in `spreadsheet-analysis-workbook` and does not repeat it. In short: the complete raw data lives in the workbook as its own sheet; every analysis cell is a live formula reading from it; derived fields reference computed cells rather than recomputing independently; a visible reconciliation cell on every tab reads zero; assumptions sit in labelled input cells rather than inside formulas; and every tab documents which columns it reads, from which sheet, and which row the data starts on. Health scores, momentum flags, and tiers are computed by nested `IF` from the profile columns; nothing in this workbook is typed in as a judgement.

1. **Build the client revenue profile, one row per client, every cell a formula.** Total revenue, revenue by period, share of portfolio, first and last activity date, active months, revenue through the recurring channel, that channel's share, breadth, and year on year growth.

   ```
   Total          =SUMIF('Data'!$D$6:$D$96401,$A12,'Data'!$O$6:$O$96401)
   Recurring      =SUMIFS('Data'!$O$6:$O$96401,'Data'!$D$6:$D$96401,$A12,'Data'!$J$6:$J$96401,"Contract")
   Non-recurring  =$C12-$D12
   First activity =MINIFS('Data'!$K$6:$K$96401,'Data'!$D$6:$D$96401,$A12)
   Active months  =SUMPRODUCT(--(F12:Q12<>0))
   Breadth        =SUMPRODUCT((COUNTIFS('Data'!$D$6:$D$96401,$A12,'Data'!$H$6:$H$96401,Codes!$A$2:$A$40)>0)*1)
   ```

2. **Compute lifetime value on all three bases and declare which the recommendation uses.**

   ```
   Simple          =$C12*Inputs!$B$3
   Churn adjusted  =$C12*(1/Tier_churn)
   Discounted      =$C12/(Inputs!$B$4+Tier_churn)
   ```

   At 100,000 of annual revenue, fifteen percent churn and a ten percent discount rate, discounted lifetime value is 400,000. The judgement is which churn rate goes in, and the rule is that it comes from the data and it is computed per tier. Blending a portfolio whose top tier churns at four percent and whose tail churns at twenty-three percent produces a number that is wrong for both. Compute LTV separately for the top, middle, and long tail; the ratio between tiers is the argument for where retention money goes, and it is usually larger than anyone expects.

3. **Classify trajectory on the annual view, then momentum on the recent view.** Annual direction alone is too slow: a client with flat annual revenue and a falling last quarter will not appear in the annual view for another two quarters, and by then the conversation is a renewal rather than a save.

   ```
   YoY       =IFERROR($E12/$D12-1,"n/a")
   Growing   YoY > 10%       Stable  -10% to 10%
   Declining YoY < -10%      At risk YoY < -25%
   Momentum  +2 growing and last 3 months above prior 3
             +1 one of the two,  0 flat,  -1 one falling,  -2 both
   ```

   The combination that deserves a name is stable annual with negative momentum. Flag it separately, because it is the only category in the matrix where intervention is both possible and not yet obvious to anyone else.

4. **Score health across five dimensions, twenty points each.**

   | Dimension | 20 | 12 | 5 | 0 |
   | Revenue trend | growing above 10% | stable within 10% | declining 10 to 25% | declining beyond 25% |
   | Recurring adoption | above 50% | 25 to 50% | 5 to 25% | none |
   | Revenue size | top fifth of portfolio | middle | bottom two fifths | below the floor |
   | Tenure | over 3 years | 1 to 3 years | 6 to 12 months | under 6 months |
   | Breadth | 3 or more lines | 2 lines | 1 line | none |

   Tiers: 80 and above strategic, invest in expansion; 60 to 79 core, protect and deepen; 40 to 59 developing, monitor; below 40 at risk, intervene. Every score is a nested `IF` reading profile columns. The reason for the rule is not purity: hand-scored health is systematically generous about the accounts closest to the people doing the scoring, and those are the accounts the score exists to catch.

5. **Compute the cost of loss, which is not the lost revenue.**

   ```
   replacement clients =CEILING($C12/Inputs!$B$6,1)
   acquisition cost    =$V12*Inputs!$B$7
   cost of loss        =$C12+$W12
   ```

   For a client with no recurring anchor, add a fragility premium: the uplift in loss probability multiplied by annual revenue. Write the result as a sentence a leader can act on: losing this client requires acquiring N new clients at the average new-client size, at an estimated acquisition cost of X, so the economic cost is Y.

6. **Size expansion and whitespace, and gate it on health.** Flag each client for a location or division not yet served, a tier upgrade its volume already justifies, and a line it does not buy. Whitespace is assumed full potential minus current revenue, with the potential assumption in a labelled input cell. Size the pool only across clients above the health threshold. Whitespace inside an at-risk account is not an opportunity; it is a retention problem wearing an opportunity's clothes, and counting it is how expansion targets get set that the account team knows are fiction.

7. **Compute net revenue retention on a true cohort.** Revenue this period from the clients present last period, divided by their revenue last period. New clients are excluded, and excluding them is the entire point.

   ```
   Cohort member =IF($R12>0,1,0)
   NRR           =SUMIF($T$12:$T$225,1,$S$12:$S$225)/SUMIF($T$12:$T$225,1,$R$12:$R$225)
   ```

   Above 110 percent is strong expansion, 100 to 110 healthy, 90 to 100 mild contraction, below 90 net contraction. The reading that matters: net revenue retention below 100 alongside growing headline revenue means acquisition is paying for churn, and the business is running to stand still at full cost.

8. **Place every client in the prioritisation quadrant by formula,** revenue size against health. Large and healthy, protect and deepen. Large and unhealthy, intervene now. Small and healthy, scale the model that produced it. Small and unhealthy, evaluate whether the servicing effort earns its keep, and be willing to write the answer down. Assign the quadrant by formula, then write the action per quadrant rather than per adjective.

9. **End in five named client actions,** each traceable to a figure in the workbook, each with an owner and a date. An analysis that ends in a distribution has not finished.

## The churn rate, and why it is usually wrong

Almost every bad lifetime value figure traces to this input, and there are four specific ways it goes wrong.

It is taken from a published benchmark for an adjacent industry, where the contract length, the buying unit, and the definition of a lost client are all different. It is computed as logo churn when the money is in revenue churn, so a portfolio losing many small clients and growing its large ones looks like it is haemorrhaging. It is blended across tiers that behave nothing alike. Or it is computed with no dormancy window, so a client that buys every eight months is counted as churned every time it pauses.

The rule: compute it from the data, per tier, on revenue as well as logos, with a dormancy window set at twice the median inter-purchase interval and stated on the inputs tab. Where the series is too short, present LTV as a band across a stated churn range and say what would resolve it. A band that is honest is more useful than a point estimate that is not.

## Worked example

**Situation.** Ashcombe Data Systems, a business-to-business analytics firm of about 90 people, had 8.6 million of revenue from 214 clients and had just approved a 40 percent increase in the acquisition budget on the strength of nine percent headline growth. The chief executive wanted a per-client view before the money was committed, in two weeks.

**Task.** A client economics workbook with lifetime value, health, and retention, and a defensible answer to whether the acquisition increase made sense.

**Action.** The profile tab was built first from a reconciled entity table, 214 rows, every cell a formula. Then lifetime value, and this is where the first version went wrong.

The first pass used a twelve percent annual churn rate taken from a published figure for the sector, producing a blended discounted lifetime value of 391,000 against a fully loaded acquisition cost of 34,000: a ratio of about eleven to one, which looked like a licence to spend. That version was abandoned when observed churn was computed from the data with a dormancy window of nine months, twice the median inter-purchase interval of four and a half. Actual churn was 4.1 percent in the top quintile, 11.8 percent in the middle three, and 23.4 percent in the bottom quintile. On tier-level churn, discounted lifetime value came out at 1,240,000 for the top tier, 262,000 for the middle, and 61,000 for the tail. Against a 34,000 acquisition cost, the tail returned less than two to one before any servicing cost, and the tail was where 61 percent of new clients had been landing for two years.

The second finding came from net revenue retention. The first calculation, run across all clients present in the current twelve months, produced 118 percent and a comfortable story. Recomputed on the true cohort, the 187 clients present twelve months earlier, it was 94 percent. Headline revenue was growing nine percent while the existing book was contracting six. Acquisition was paying for churn.

The health scores then located it. Of 214 clients, 31 scored 80 or above, 74 between 60 and 79, 62 between 40 and 59, and 47 below 40. Cross-tabulating against the quadrant showed nine clients in the large-and-unhealthy cell holding 1.42 million between them, six of which had stable annual revenue and negative momentum, which is the category that would not have surfaced for another two quarters on an annual view alone.

Whitespace was sized at 2.1 million across the portfolio on the first pass. Gated on the health threshold of 60, it fell to 1.24 million, and three of the largest whitespace entries turned out to sit inside accounts scoring below 40. Those three moved from the expansion list to the retention list.

**Result.** The acquisition increase was redirected rather than approved as proposed. About a third of it went to a retention programme aimed at the nine large-and-unhealthy accounts, and the qualification criteria for new business were tightened to exclude the profile that had been landing in the tail. Six of the nine accounts were stabilised over the following two quarters; two churned, one of which had been sized in the cost-of-loss table at four replacement clients and 3.1 months, so the impact was known in advance rather than discovered.

Net revenue retention was 101 percent nine months later, on a cohort basis, with headline growth of six percent. Lower headline growth, better economics. The tier-level lifetime value table became a standing input to the pricing conversation.

The workbook took about fourteen hours. The churn rework cost three of them and changed the recommendation entirely, which is why the method now treats the churn input as the step to get right before anything else is computed.

### A second scenario, where it goes differently

A project-based engineering consultancy, 5.2 million of revenue from 71 clients, where work arrives as discrete commissions six to eighteen months apart and there is no recurring channel at all. Two dimensions of the standard method stop working.

Churn is not well defined, because a client with no activity for a year may be entirely healthy and simply between projects. The dormancy window does the heavy lifting here rather than being a footnote: set at twice the median inter-commission interval, which was fourteen months, it reclassified 19 of the 71 clients from churned to dormant. Lifetime value moves from a subscription lifespan basis to a repeat-purchase basis: expected number of future commissions multiplied by average commission value, discounted, with the repeat rate observed from the data by cohort. The recurring adoption dimension of the health score is unusable and is replaced by repeat rate, which measures the same thing in this business, and the tenure dimension is reweighted because a three-year relationship with one commission is weaker than an eighteen-month relationship with three.

What changed is the shape of the revenue, not the standard. The prioritisation quadrant, the cost of loss, and the whitespace gate all run unmodified.

## Output

A workbook and a report. The report has a fixed structure so two runs are comparable.

Portfolio overview with client count, total revenue, mean and median per client. Health distribution by tier, with client count, revenue, and share of revenue in each. Trajectory and momentum counts, with the stable-and-falling category called out separately. Lifetime value by tier with the churn rate and discount rate stated beside each. The largest risks, each with revenue, health score, and the specific reason. The expansion list with sized whitespace, gated. Net revenue retention with one sentence of interpretation. Then five named client actions.

The client table is the working deliverable.

| Client | Revenue | Share | Recurring % | Breadth | Tenure mths | YoY | Momentum | Health | Tier | LTV (disc.) | Cost of loss | Quadrant | Action |
| Halden Freight | 412,600 | 4.8% | 71% | 4 | 74 | +14% | +2 | 88 | strategic | 1,486,000 | 512,600 | protect and deepen | expansion review |
| Perrin Retail | 388,100 | 4.5% | 12% | 1 | 29 | -3% | -1 | 47 | developing | 214,000 | 490,100 | intervene now | contract and second line |
| Corven Foods | 96,400 | 1.1% | 0% | 1 | 11 | -31% | -2 | 24 | at risk | 38,000 | 130,400 | evaluate | no further investment |

## Failure modes

**A blended lifetime value figure.** Recognise it when one LTV number describes a portfolio with tiers that behave differently. Compute per tier and show the ratio; that ratio is usually the most actionable number in the workbook.

**Churn from a benchmark rather than the data.** Recognise it when the churn input has a source outside the file. Compute it, per tier, with a stated dormancy window.

**Net revenue retention that includes new clients.** Recognise it when the figure is comfortably above 110 in a business that feels harder than that. Rebuild on the cohort present at the start of the prior period.

**Health scores typed in.** Recognise it when scores are round numbers, cluster high, or disagree with the revenue trend in the same row. Compute them from profile columns.

**Whitespace counted inside at-risk accounts.** Recognise it when the expansion target and the retention list name the same clients. Gate the whitespace pool on the health threshold and say what was excluded.

**Annual trajectory used alone.** Recognise it when no recent-period comparison exists. Add momentum, and treat stable annual with negative momentum as its own category.

**Cost of loss stated as lost revenue.** Recognise it when the figure equals the client's annual revenue exactly. Add replacement clients and replacement cost, and put both in the sentence.

**A report that ends in a distribution.** Recognise it when the last section is a table. End in five named actions with owners and dates.

## Edge cases

**Fewer than eighteen months of data.** Churn cannot be observed. Present lifetime value as a band across a stated churn range, use momentum rather than year on year for trajectory, and say which conclusions the series cannot support.

**Usage-based or consumption revenue.** Revenue per client moves without any commercial event, so trajectory needs a usage denominator to be meaningful. Report revenue per unit of usage alongside revenue, or the health score will misread a pricing change as a relationship change.

**A client with one enormous non-recurring project.** Exclude the project from trend, lifetime value, and health, and report it separately. Left in, it produces a strategic-tier score for a relationship that has already ended.

**A portfolio where the median client is unprofitable.** The analysis is still correct and the recommendation changes: the finding is about the acquisition profile and the service model, not about individual accounts. Say so plainly, and size what the tail costs to serve.

**Clients under common ownership.** Aggregate for revenue and concentration, but score health separately per operating entity, because the buying decisions and the sponsors are usually separate even when the contract is not.

**A relationship carried by one person on your side.** No data signal captures it. Add it as a flagged column populated by hand, keep it out of the computed health score, and report it as a separate risk line so it is visible without contaminating the scoring.

## Quality bar

- The churn rate is computed from the data, per tier, with a stated dormancy window on the inputs tab.
- Lifetime value is reported on all three bases, per tier, with the basis used by the recommendation named.
- Health scores are computed by formula from profile columns, with no typed judgements anywhere in the tab.
- Net revenue retention is computed on the cohort present at the start of the prior period, and the exclusion is stated.
- Cost of loss includes replacement clients and replacement cost, not just lost revenue.
- Whitespace is gated on health, and the excluded amount is shown rather than dropped silently.
- Every assumption sits in a labelled input cell, and the report states each one in the sentence that uses it.
- The report ends in five named client actions, each traceable to a figure above it.

## Related skills

`revenue-analysis-workbook` builds the entity table this starts from, and `spreadsheet-analysis-workbook` is the foundation both assume. `revenue-concentration-risk` covers the exposure question this deliberately excludes: what happens if a relationship ends, and how long replacement takes. `account-reengagement-plan` acts on a single account this analysis flags as at risk. `expected-revenue-estimation` sizes the whitespace and the replacement revenue this identifies. `economics-report-from-data` turns the workbook into the written argument, and `pipeline-deep-dive` covers the acquisition side of the same economics.
