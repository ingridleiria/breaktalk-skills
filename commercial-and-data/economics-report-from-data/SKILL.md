---
name: economics-report-from-data
description: Turns a revenue, sales, or operating dataset into an economic argument rather than a description. Enforces four levels of analysis from what happened to what to do, applies only the frameworks the data supports (channel economics, concentration, predictability, growth decomposition, whitespace, cost of delay, seasonality), tests every insight for specificity, consequence, traceability, and falsifiability, and delivers in a fixed template with a language standard that replaces hedging with a magnitude or a mechanism. Use it whenever someone asks what the data means, to explain a trend, to size an opportunity or a risk in words, to write an executive summary, an insight memo or a board narrative, or when a deck of charts needs an argument attached to it.
---

# Economics Report From Data

Description is not analysis. "Revenue grew 25 percent" is description, and a reader can get that from the chart without you. "Revenue grew 25 percent because one channel is structurally replacing another, which means the business compounds rather than restarts each quarter" is analysis, and no reader can get that from the chart. The failure this skill prevents is shipping the first as though it were the second, which produces a document everyone agrees with and nobody acts on. Agreement without action is the most expensive outcome in a reporting cycle, because the question has now been formally addressed and will not be raised again for two quarters.

The second failure is the untraceable number. A figure appears in a summary, someone recomputes it a different way and gets something else, and within two minutes the discussion is about the analysis rather than the business. Every other figure is now suspect, including the correct ones. Traceability is what buys the report the right to be argued with on its conclusions.

## When to use this, and when not to

Use it when numbers exist and a written argument is wanted: an executive summary, a board narrative, an insight memo, a monthly commentary, a deep dive on one account or channel, a cost-of-delay brief. Use it when a deck of charts exists and nobody can say what it means, or when a leadership team has heard the same figure three months running and nothing has changed.

Do not use it to produce the numbers themselves: `revenue-analysis-workbook` builds the tabs, `spreadsheet-analysis-workbook` audits and verifies the file, `revenue-concentration-risk` produces the exposure analysis, `client-economics-analysis` the per-client economics, and `expected-revenue-estimation` anything forward-looking. Do not use it to choose between named options, which is `decision-memo`; this skill supplies the analysis that memo reports. Do not use it to build the deck, which is `board-deck`, or a company narrative not grounded in a dataset, which is `ceo-communications`.

## What you need before starting

**A reconciled workbook, with a verification tab reading zero.** Missing: build it first, or state at the top of the report that the figures are unverified and name what was not checked. A report on an unreconciled file is dismantled by the first person who recomputes a number, and every conclusion goes with it.

**The question the report answers, and the decision behind it.** Missing: ask what changes on Monday depending on the answer. If nothing changes, the deliverable is a summary rather than a report, and it should be shorter.

**The audience, and what they already believe.** A report contradicting a widely held belief needs the mechanism up front and the evidence next; one that confirms a belief needs the magnitude. Missing: assume the belief is whatever the last report said, and check.

**The period, and how much history exists.** Missing: compute the minimum and maximum date and report the actual span, since it governs which frameworks may be applied at all.

**The prior figures already in circulation.** Missing: ask for the last report or board pack. An unexplained second number reads as a disagreement between people rather than between methods, and costs more attention than the finding it accompanies.

**The format and the length available.** One page, ten slides, or a paragraph in an email. Missing: write one page, which is the length that forces the argument to be finished.

## The method

Any workbook produced alongside the narrative follows the discipline in `spreadsheet-analysis-workbook` and does not restate it: the complete raw data lives in the workbook as its own sheet; every analysis cell is a live formula reading from it; derived fields reference computed cells rather than recomputing independently; a visible reconciliation cell on every tab reads zero; assumptions sit in labelled input cells rather than inside formulas; and every tab documents which columns it reads, from which sheet, and which row the data starts on. A figure in the report that cannot be traced to a cell does not go in the report.

1. **Fix the question and the decision in one line each,** at the top of the working file. Everything that does not serve them is an appendix.

2. **Climb the four levels, and know which one you are on in every paragraph.** Start at one and climb to whatever the question demands. Every report reaches level three; anything with an executive summary reaches level four.

   1. **What happened.** The number, the period, the comparison, stated precisely and without interpretation.
   2. **Why it happened.** The mechanism: which specific change produced the number, named and dated.
   3. **What it means.** The economic consequence: revenue quality, risk, scalability, unit economics, predictability.
   4. **What to do.** The recommendation the analysis supports, with the cost of not doing it.

   The rule for climbing: no level-three consequence may be asserted until the level-two mechanism is named and dated. Most reports that feel thin are level one repeated at three magnitudes.

3. **Apply only the frameworks the data supports,** from the set below, and say when one was unavailable. Applying a framework the series cannot carry is worse than omitting it, because the conclusion looks the same as a supported one.

4. **Test every insight before writing it**, on the four tests below. An insight failing any of them is fixed or cut, and cutting is usually faster.

5. **Choose the template and fill it in order,** so that two reports a quarter apart are comparable and the reader knows where to find what they came for.

6. **Enforce the language standard as a separate pass.** Doing it while drafting slows the argument down; doing it afterwards takes ten minutes and changes the register of the whole document.

7. **State the limits inside the report, not as a caveat at the end.** Where the data cannot support the conclusion, say what it shows, what it does not, and what would be needed, in specific form: this series is fourteen months long and cannot separate structural from cyclical, resolvable in October; this figure is directionally right but approximate, because of a duplication affecting roughly two percent of rows. Overstating certainty costs more than admitting a limit, and it costs it later, in front of the same audience. A report that names its own limits is also harder to argue with, because the obvious objection has been conceded and priced.

8. **End in actions, each attached to the figure that justifies it,** with an owner and a date. A report whose last section is a table has stopped a level short.

## The frameworks

**Channel economics.** Where two or more channels exist: the share of each, the rate the mix is shifting, which has the better economics, and the value of a one point shift at current scale.

```
Value of one point of shift  =$Total_revenue*0.01
Margin value of one point    =$Total_revenue*0.01*($Margin_A-$Margin_B)
```

The structural against cyclical test is defined in `revenue-analysis-workbook`, which owns it. Apply it there and report the verdict here with all three pieces of evidence in the sentence: the periods it persisted across, the named and dated change it traces to, and the fact that it is not reversing. Do not restate the test in the report and do not keep a second copy of the rule.

**Concentration risk.** A top five above half of revenue is high concentration; a single entity above fifteen percent is a meaningful dependency and above twenty-five percent a critical one. What matters is not the share but the grip: a large client held by a contract or an integration is a different risk from one buying order by order. Express exposure as replacement: losing this account requires the equivalent of N average mid-tier accounts, taking M months at the current win rate. `revenue-concentration-risk` produces the analysis; this is how it is stated in prose.

**Revenue predictability.** Split revenue into what arrives without a new selling motion and what requires one each time. Recurring revenue is worth more per unit because it capitalises at a multiple, costs nothing to re-acquire, lets operations be planned, and is harder to lose. The consequence worth writing: the conversion opportunity is real even when total revenue does not change, because the same money becomes better money. Size it, or the sentence is a platitude.

**Growth decomposition.** Total growth splits into more entities and more revenue per entity, and revenue per entity splits into frequency and average size. Naming the component tells you whether the trend is durable.

```
From more entities      =($N1-$N0)*$R0
From revenue per entity =($R1-$R0)*$N1
Residual check          =$Total1-$Total0-$D5-$D6      must read 0
```

An annualised run rate is valid only when the elapsed months are complete, no exceptional item distorts the average, and seasonality has been accounted for. State that in the sentence carrying the number, not in a footnote.

**Whitespace and conversion.** Where comparable entities show very different penetration of a valuable channel, the gap is the opportunity. Three-way sizing at the lowest, mean and highest observed penetration is defined in `expected-revenue-estimation`, which owns it; size it there and report all three figures here.

What this skill adds is how the three are written. Put the penetration assumption in the same sentence as the number, name the comparable population and how many observations it holds, and mark the mean-penetration figure as the one to cite. Presenting only the upside as "the opportunity" is the commonest way an analysis loses credibility.

**Cost of delay.** Delayed revenue is forgone, not deferred: an initiative launching in September does not recover June, July and August. The calculation, including the ramp-based figure and the naive steady-state figure shown beside it, belongs to `expected-revenue-estimation`, which owns it. Take both figures from there rather than multiplying a monthly rate by months lost inside the report, because a naive figure written into prose is the version that gets quoted afterwards. Report per initiative and in aggregate at all three scenario rates, state the horizon in the same sentence as the number, and say plainly that there is no recovery mechanism, because the instinct in the room will be to treat it as timing.

**Seasonality.** With two or more full cycles, separate the seasonal baseline from the directional trend before calling anything growth or decline. Report which periods systematically outperform, the peak to trough ratio, and whether the pattern holds across years. The implication is usually timing: an initiative that misses the peak waits a full cycle, which is a cost-of-delay figure rather than a scheduling inconvenience.

## Insight quality tests

**The five second test.** If the sentence would be true for any business in any industry unchanged, it is a statement, not an insight. "Customer retention is important" fails. "Clients on the programme channel renew at 91 percent against 62 percent elsewhere, so every conversion is worth 29 points of renewal probability" passes.

**The so what test.** After every figure, ask what follows. If the answer is that it is interesting, the insight is unfinished: an insight ends in a decision, a risk, or an action.

**Traceability.** Every number points to a cell, a tab, or a stated calculation. Never round in the direction that improves the story, and never quote a figure at a precision the method cannot support.

**Falsifiability.** Say what would have to be true for the claim to be wrong and what evidence would overturn it. A claim that cannot be wrong is not analysis, and a reader who cannot see how to disagree will disagree with the whole document instead.

## Report templates

**Executive summary, one page.** Headline finding as a sentence carrying a number. Three findings at level three or four. The largest risk, sized as replacement. The largest opportunity, sized three ways. The recommended action and the cost of delaying it.

**Entity deep dive.** Revenue by period. Recurring-channel share against the portfolio average. Deseasonalised trend. Economic profile in two sentences. Opportunity where penetration is low, expansion where it is high. Risk as replacement cost and months.

**Cost of delay brief.** Count of delayed initiatives. Monthly forgone revenue at all three rates. Cumulative at three, six, and twelve months. The principle stated once. The priority list with the reason each item ranks where it does.

**Channel shift memo.** Share moved from x to y over the period. The one to three changes that drove it, named and dated. The value of a point of shift at current scale. The structural or cyclical verdict with its three pieces of evidence. The next milestone that would confirm or break the thesis.

## Language standards

Replace "revenue went up" with the rate and the comparison basis. Replace "a big opportunity" with the sized conversion and its penetration assumption. Replace "this is a risk" with the exposure and the replacement requirement in clients and months. Delete "seems to suggest", "might indicate", "significant", "strong growth", and "robust", putting the magnitude or the mechanism in their place. Hedging words are not caution; caution is a stated confidence level and a falsification condition, and it reads as more confident rather than less. If three consecutive sentences carry no figure, the draft is still in description. If a paragraph would survive being moved into a report about a different company, cut it.

## Worked example

**Situation.** Lambert Skills Group, a workplace training provider of about 200 people, had 24.6 million US dollars of revenue and a board meeting in six days. All figures in this example are in US dollars. Revenue was up 25 percent year on year and the chief executive wanted the growth explained, because the board had asked twice whether it was repeatable without getting an answer. Two channels existed: open courses sold seat by seat, and corporate programmes sold as annual agreements.

**Task.** A one-page executive summary answering whether the growth was repeatable, with the analysis behind it, in a form the board would not send back.

**Action.** The first draft was three charts and four paragraphs, leading with "revenue grew 25 percent, driven by strong performance in corporate programmes". It was abandoned after being read against the five second test: every sentence would have been true of any training business with a good year. It was level one written three times.

The rewrite started with growth decomposition, on the two figures that had to reconcile: 19,656,000 in the prior year and 24,570,000 in the current one, an increase of 4,914,000, which is the 25 percent. Client count had gone from 312 to 325, so 13 more clients at the prior year's average of 63,000 each, worth 819,000. Revenue per client had risen from 63,000 to 75,600, so 12,600 more across 325 clients, worth 4,095,000. The two components sum to 4,914,000 and the residual check read zero. Growth was overwhelmingly existing clients spending more, not new clients won, which is a different business and a different repeatability answer.

Then the mechanism. Splitting revenue per client by channel put the whole increase in corporate programmes, and tracing it to individual clients showed nine that had moved from open-course seats to annual programme agreements during the year, accounting for 3,500,000 of the 4,095,000 attributed to revenue per client, and 71 percent of the total increase of 4,914,000. Named and dated, this was level two.

Level three came from the predictability framework. Programme revenue arrives without a new selling motion; open-course revenue is re-sold every cycle. Programme clients renewed at 91 percent against 62 percent, both from the data. The mix shift therefore meant the business was moving from restarting each year to compounding, and it passed all three structural tests: persistent across three consecutive periods, traceable to a programme launched eighteen months earlier, not reversing.

The second wrong turn was the opportunity sizing. The first version put conversion whitespace at 4.1 million using the highest observed programme penetration among comparable clients. The finance director took it apart in a preparatory read, correctly, because it assumed every remaining client would behave like the best. Rebuilt three ways on the method `expected-revenue-estimation` defines: 1.2 million at the lowest observed penetration, 2.4 million at the mean, 4.1 million at the highest, base marked and the penetration assumption in the same sentence as each figure.

The falsification condition was written in: the thesis is wrong if programme renewals fall below 80 percent, or if conversions stop coming from the existing base. Both observable within two quarters.

**Result.** The summary led with the sentence that growth was 71 percent driven by nine existing clients converting to annual programmes rather than by new clients won, and that this made it more repeatable rather than less, conditional on conversion capacity. The board asked one question, how many more clients fit the conversion profile, which the whitespace section answered at three levels.

Two sales roles were reallocated from new business to conversion. The cost-of-delay section priced waiting, using both figures from `expected-revenue-estimation` rather than a monthly rate multiplied by months. At maturity the 2.4 million base case implies 200,000 a month, so a quarter of delay looks like 600,000. On the conversion ramp observed from the nine clients already converted, the first three months of a delayed start are worth 0.94 of a mature month between them, an average of about 62,700 a month, so a quarter of delay forgoes roughly 188,000 within the first year and converges on the full 600,000 only once the motion is mature. Both figures went in, with the horizon stated, and the sentence that none of it is recoverable. Nine months later programme renewal was 89 percent, inside the falsification band, and the thesis stood.

The report took about nine hours including workbook checks. The abandoned first draft took two of them, and what saved it was reading its opening sentence aloud against the five second test.

### A second scenario, where it goes differently

The same request from a company with fourteen months of data and one channel. Growth decomposition still runs, and so does concentration. Seasonality cannot be separated, channel economics does not apply, and the structural against cyclical verdict cannot be reached, because three consecutive periods of evidence do not exist.

The report changes shape rather than dropping to a lower standard. It states in the body that fourteen months cannot separate structural from cyclical and that the settling evidence arrives in October. The recommendation is framed as a bet: the assumption it rests on, what it costs if that assumption is wrong, the date the answer exists. The opportunity is still sized three ways, with a wider band and the reason given. The report ends in a monitoring line rather than an action list, naming the two figures to watch and their thresholds.

What changed is the length of the series. What did not change is that every figure is traceable, every claim falsifiable, and the document ends in something someone does.

## Output

One page, in this order, whatever the format.

```
HEADLINE
[One sentence carrying a number and a mechanism. Not a description.]

WHAT HAPPENED
[The figures, the period, the comparison basis. Level one, kept short.]

WHY
[The mechanism, named and dated. Level two. This is the section that earns the report.]

WHAT IT MEANS
[Revenue quality, risk, predictability, scalability. Level three.]

THE LARGEST RISK
[Sized as replacement: N clients, M months at the current win rate.]

THE LARGEST OPPORTUNITY
| Sizing | Penetration assumed | Value |
| Low    | lowest observed     |       |
| Base   | mean observed       |       |  <- the figure to cite
| High   | highest observed    |       |

RECOMMENDATION
[The action, the owner, the date, and the cost of not doing it this quarter.]

WHAT WOULD MAKE THIS WRONG
[The falsification condition, and when the evidence exists.]

LIMITS
[What the data does not show, stated plainly.]
```

Where the report carries charts, keep them monochrome first: series separated by marker shape, dash pattern, and fill texture rather than colour, legend outside the plot area, and an accent colour on only the series the sentence is about. Every chart's title states the point it makes, not the variable plotted.

## Failure modes

**Level one repeated at three magnitudes.** Recognise it when every paragraph is a number and a direction. Add the mechanism, named and dated.

**A consequence asserted without a mechanism.** Recognise it when a sentence jumps from a figure to an implication with nothing between. Name the change that produced the figure, or drop the implication.

**The opportunity sized only at the upside.** Recognise it when one number is labelled "the opportunity". Three sizings, base marked, assumption in the sentence.

**Structural declared from magnitude.** Recognise it when the evidence for a structural shift is that the shift is large. Apply persistence, cause, and non-reversal, or write cyclical.

**Hedging in place of a confidence statement.** Recognise it by "seems to suggest" and "may indicate". Replace with a magnitude, a mechanism, and a falsification condition.

**A figure that cannot be traced.** Recognise it when you cannot say which tab it came from without opening the file. Fix the trace or remove the figure, because the first challenge in the room otherwise ends the report.

**Caveats collected at the end.** Recognise it when nothing above the limits section is qualified. Move each limit next to the claim it qualifies.

**A report that ends in a table.** Recognise it when the final section has no owner and no date in it. End in actions.

**Rounding toward the story.** Recognise it when every figure rounds the same way. It is the cheapest way to lose a reader who checks, and readers who check are the ones whose agreement you need.

## Edge cases

**The data contradicts what the sponsor expects.** Lead with the mechanism rather than the conclusion, so the reader arrives at it having followed the evidence, and show the reconciliation to the figure they already believe. Do not soften the finding; soften the route to it.

**Two prior reports disagree.** Reconcile them in a short section before your own analysis, naming the methodological difference. Until that is done, no new number will be heard.

**The series is too short for the framework the question needs.** Say so in the body, give the date the evidence will exist, and frame the recommendation as a bet: its assumption, its cost if wrong, its resolution date.

**The finding is that nothing has changed.** A legitimate report, and it should be one page rather than four. State the stability, size what it means at the current trajectory, and name what would have to change for the picture to move.

**The audience will act on one number only.** Choose it deliberately, put it in the headline sentence, and everything else below the fold. A report distributing emphasis evenly across nine findings transmits none of them.

**The decision has already been made.** Write the analysis anyway, saying in the first line that it records the reasoning rather than informing a choice. A report pretending a settled decision is open is transparent to the reader.

## Quality bar

- Every report reaches level three, and every executive summary reaches level four.
- Every level-three consequence has a level-two mechanism named and dated above it.
- Every number is traceable to a tab or a stated calculation, and no number is rounded toward the story.
- Opportunities are sized three ways with the base case marked and the penetration assumption in the sentence.
- Structural and cyclical are distinguished explicitly, with all three pieces of evidence given.
- A falsification condition is stated, with the date the evidence will exist.
- The limits of the data appear beside the claims they qualify, not collected at the end.
- The report ends in actions, each with an owner, a date, and the figure that justifies it.

## Adapting this to your context

The frameworks assume a services or software company with two or more channels, a reconciled workbook behind it, and a leadership team meeting on a cycle. The templates and the language standard travel further than the frameworks do.

- **Which frameworks apply.** Channel economics needs two channels; a single-channel business drops it and says so rather than inventing a split. Grant-funded and public sector bodies replace it with funder mix and award expiry, since the question there is which awards end when.
- **Growth decomposition.** More entities against more revenue per entity assumes a countable entity. Usage-based businesses need a third component, price against volume, or a tariff change is reported as expansion. A marketplace decomposes into participants, transactions each and take rate.
- **The audience.** A funder or a regulator reads for compliance against stated objectives, so the template becomes objectives, evidence, variance and action. Keep the four levels and the falsification condition; change the headings.
- **Whitespace and cost of delay.** Both are borrowed from `expected-revenue-estimation`. A solo practice with no comparable population cannot size whitespace three ways, and should state what the ceiling would have to be instead.

- **What not to change.** Every report reaches level three, no consequence is asserted without a mechanism named and dated above it, and every figure traces to a cell.

## Related skills

`revenue-analysis-workbook` produces the tabs this reads, and `spreadsheet-analysis-workbook` is the foundation that makes them trustworthy. `revenue-concentration-risk` supplies the exposure stated here as replacement cost and months, `client-economics-analysis` supplies health, lifetime value, and retention, and `expected-revenue-estimation` supplies every forward figure including the cost of delay. Downstream, `decision-memo` takes this analysis when it feeds a choice between named options, `board-deck` and `investor-update` when it feeds a governance cycle, and `executive-briefing` is the short verbal form. `human-voice-editor` is the pass to run if the draft reads as assembled rather than written.
