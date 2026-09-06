---
name: financial-model-builder
description: Builds and audits driver-based financial models in a spreadsheet, covering three-statement, operating, unit-economics, and runway models, with every assumption in a labelled input cell, one scenario switch that moves every output, a visible checks block, and a reconciliation cell that reads zero. Enforces the rule that no number exists anywhere except as a labelled input or a live formula, so any output traces back to its drivers in under two minutes. Use this skill whenever someone wants to build, extend, or check a financial model, budget, cash flow projection, runway model, unit economics, or business case in a spreadsheet, or says model this out, what does the profit and loss look like if, build me a scenario, check my model, how long is our runway, sanity check these numbers, or asks what happens to the plan when one assumption moves. Trigger for any spreadsheet whose purpose is projecting money over time.
---

# Financial Model Builder

A model earns its keep in the ten minutes when someone challenges it. The chief financial officer asks what happens if churn runs at three percent instead of two, and either one cell changes and every output moves, or the answer is that the analyst will come back on Thursday. The second answer ends the conversation about the business and starts a conversation about the spreadsheet. By Thursday the decision has been taken on instinct and the model is a document nobody opens again.

The expensive version is quieter. A number reaches a board pack or a data room and cannot be traced to anything, because it came from a growth rate typed inside a formula eleven months ago by someone who has since left. Under diligence, or under a plan that misses, somebody pulls the thread, and what they find is not a wrong number but a model whose logic cannot be reconstructed. At that point every figure in it is suspect, including the ones that were right.

## When to use this, and when not to

Use it to build any projection of money over time: an operating budget, a three-statement model, a runway and cash model, unit economics, a business case, a fundraising model. Use it equally to audit a model somebody else built, before its output is quoted anywhere.

This is the general construction standard. Three neighbouring skills apply it to specific questions, and the boundaries matter because all four involve numbers in a spreadsheet:

- `revenue-forecast` is the current year's revenue number, built in layers of decreasing certainty, reconciled to plan, with a bridge from the previous forecast and a fixed update cadence. It answers where the year lands. If the question is one number for a defined period, that skill owns it and this one supplies the workbook structure underneath.
- `pricing-and-resourcing-model` prices one client engagement, with its staffing plan, utilisation assumptions, and margin under downside scenarios. It answers what to charge and who delivers it. Single engagement, not the company.
- `pipeline-deep-dive` analyses a set of sales opportunities for coverage, conversion, velocity, and hygiene. It is a diagnostic on data that already exists, not a projection, and its measured conversion rates feed `revenue-forecast` rather than this skill.

Do not use this for analysing a dataset that already exists, which is `spreadsheet-analysis-workbook`. Do not use it to justify a number already promised. Do not build a model where one calculation would do: a comparison of two options belongs in `decision-memo` with the arithmetic in the text.

## What you need before starting

**The decision the model serves.** A fundraising model and an operating budget share arithmetic and almost nothing else. Missing: ask what changes depending on the output, and if nobody can say, build the smallest version that answers one named question.

**The business type and its drivers.** Subscription, services, marketplace, usage, or mixed. This sets the driver tree and cannot be inferred from the profit and loss. Missing: ask how a customer is won, what is charged and on what basis, and what limits growth.

**Actuals for at least the last twelve months.** History anchors the model and makes an assumption arguable rather than invented. Missing: mark every assumption in the register as unverified, and do not present the result as a forecast.

**The period, granularity, and start date.** Missing: default to monthly for twenty-four months and annual to five years, and say so on the cover.

**The cost categories actually in use.** A model whose line items do not map to how the company books costs cannot be compared to actuals, and a model never compared to actuals is never updated. Missing: use the management accounts as the template, imperfect categories included.

**Fixed constraints.** A cash floor, a covenant, a board-approved envelope. Missing: ask, because a model that quietly violates a known constraint gets dismissed rather than corrected.

## The method

1. **Write the question on the cover before building anything.** One sentence, with the decision and the date. This takes four minutes and removes about a third of what would otherwise be built.

2. **Choose the model type from the business, not from a template.** Subscription: new customers by channel, conversion, contract value, retention by cohort, expansion. Services: billable headcount, utilisation, bill rate, win rate. Marketplace or usage: transactions, take rate, activity per active user. Cash and runway: collections and payment timing, payroll, financing events. Where the business is genuinely mixed, model the segments separately and consolidate; never average two economic engines into one set of drivers.

3. **Set the spine.** Periods left to right, one granularity per block, with the first forecast period adjacent to the last actual on the same rows and a divider column between them. A model whose actuals live somewhere else is never reconciled against them.

4. **Write the assumptions register before the first formula.** Every input, unit, value, source, and confidence. If an input is not in the register it does not exist. Building the register first is what stops values being invented mid-build to make a row work.

5. **Build the driver tree from the customer inwards.** Volume before price, price before revenue, revenue before cost, cost before cash. One formula per row copied across, unit in every label. Where you need a number not in the register, stop, add it, and reference it. That interruption is the mechanism, not an inconvenience.

6. **Build outputs by reference only.** A figure on the outputs sheet that is not a reference to a computed cell is a defect. This is what makes the trace test pass later.

7. **Build the checks sheet alongside the outputs, not after.** Checks written at the end are calibrated to the answer you already have. Minimum: revenue, cost, and cash roll-forward reconciliations to zero; the balance sheet balancing where one exists; a bounds check flagging any period growth rate outside a stated range.

8. **Wire the scenarios through one switch and test it.** Change the switch and confirm every headline output moves. An assumption that never moves is either genuinely fixed, and should be labelled so, or orphaned, which is a defect. Never build separate files per scenario; they diverge within a fortnight and someone quotes the wrong one.

9. **Run sensitivity and name the two assumptions that matter.** Flex each material assumption by a stated amount, usually twenty percent each way, and rank outputs by how far they move. This is often the most useful output of the exercise, because it says where the argument actually rests, which is frequently not where the debate has been.

10. **Do the trace test yourself.** Follow the headline output back to inputs. More than two minutes, or a value you cannot explain, means it is not finished. Then write the summary: question, base case, the two assumptions that matter, the range, and the one thing you would verify next.

## Workbook discipline

The same standard as `spreadsheet-analysis-workbook`, and not negotiable in a model, where a defect compounds across every period column.

1. **Raw data lives in the workbook.** Actuals, the headcount list, the rate card. No formula references an external file, so an update recalculates rather than requiring a rebuild.
2. **Every calculated cell is a live formula.** The test is mechanical: change one assumption and every dependent output must move. A pasted value that once came from a formula is the commonest defect in an inherited model, and it is invisible.
3. **Derived fields reference computed cells rather than recomputing.** Gross profit reads revenue and cost of sales where they were computed. Two independent builds of one quantity diverge, and the divergence surfaces weeks later as a difference nobody can locate.
4. **A visible reconciliation cell reads zero.** Outputs revenue minus the sum of the driver revenue lines; closing cash from the cash sheet minus the same figure from the balance sheet. Non-zero means a gap or a double count, fixed before delivery, never footnoted.
5. **Assumptions live in labelled input cells,** with label, unit, value, source, and a distinct fill declared on the cover. Nothing hard-coded elsewhere, formulas included.
6. **Layout is documented on the cover:** which sheet holds what, which column the periods start on, and the sign convention.

Sheets, in order: cover and guide; assumptions with scenario columns and one switch cell; drivers and calculations; outputs; checks; scenario summary with sensitivity.

## Auditing a model somebody else built

Run this before any output is quoted, and report findings with cell references. Find every hard-coded number outside the assumptions sheet, with a count, because that count alone usually settles whether the model can be trusted. Trace the three most important outputs back to inputs, noting every break: a pasted value, an external reference, a circular reference. Recompute the headline total by a different route and compare. Check period alignment, units, and sign conventions across sheets, since a cost block positive on one sheet and negative on another forces a recheck of everything downstream. Stress the two biggest assumptions twenty percent each way, and if the conclusion flips that goes in the first line of the report. Finally, list every assumption with no stated source; that list is the agenda for the conversation with whoever owns the number.

Report as a findings table ranked by whether the item changes the answer, then by effort to fix. Repair against rebuild: more than about a dozen hard-coded values outside the assumptions sheet means rebuild, because repair time scales with the interaction between defects and rebuild time does not.

## Worked example

**Situation.** A business software company, seventy-two people, roughly 6.4 million in annual recurring revenue, five months from a Series B conversation. The existing model was one sheet, 340 columns wide, last maintained by a finance manager who had left six weeks earlier. Its headline said eighteen months of runway, and the chief executive had quoted that figure to two prospective investors and to the leadership team.

**Task.** Establish whether eighteen months was defensible and produce a model the chief financial officer could take into diligence, within two weeks.

**Action.** The audit came first and took a day and a half. It found 61 hard-coded numbers outside any assumptions block, including the churn rate, which appeared as 0.02 inside four formulas and as 0.025 in a fifth, apparently from an abandoned edit. The marketing cost line was pasted as values from month fourteen onward. Headcount and payroll had been built independently, so the model carried two different headcounts for the same month, differing by four people from month nine.

Recomputing runway from the underlying cash movements rather than from the model's own cash row gave 13.5 months, not 18. Almost all of the difference was the pasted marketing line, frozen at its month-thirteen level while the acquisition assumptions kept growing volume.

The wrong turn: the first instinct was to repair the sheet in place, because a rebuild seemed not to fit the deadline. That was abandoned after half a day. With 61 hard-coded values and two competing headcount blocks, every repair required checking what else referenced the cell, and the checking was slower than rebuilding.

The rebuild ran to five sheets over six working days. Headcount became a single named block that payroll referenced, removing the contradiction structurally rather than by correction. Churn became one input cell with cohort retention derived from it. Four reconciliation cells covered revenue, cost, cash roll-forward, and headcount cost against the headcount plan.

Sensitivity then found the two assumptions that mattered, and neither was the one under debate. The leadership team had spent three meetings on pricing, but flexing price twenty percent moved runway by 1.1 months, while flexing the account executive ramp from four months to six moved it by 3.4 and flexing gross retention by five points moved it by 2.9.

**Result.** 13.5 months in the base case, 10.2 in the downside, 16.8 in the upside. The chief executive corrected the figure with both investors that week, which was uncomfortable and cheaper than having it surface in diligence. The fundraise timeline moved forward by about six weeks, and the ramp finding changed the sales onboarding programme and the hiring sequence for two quarters.

What mattered was not the arithmetic, which was ordinary. It was that one structural fix, a single headcount block referenced by everything, removed a class of error rather than an instance of it.

### A second scenario, where it goes differently

A twenty-eight person services business asking the same question. The driver tree inverts: cash is constrained by delivery capacity rather than by burn against a plan, so the model is built from billable people, utilisation, and bill rate, and revenue becomes an output of capacity rather than an input to it. Cash timing dominates, because clients pay between thirty and seventy-five days after invoicing while payroll runs monthly regardless, so the first six months are modelled weekly and the runway question becomes a question about the worst collections week rather than the average month.

The scenario switch does different work too. In the software model the downside was lower conversion; here it is one large client paying late, a timing shock rather than a rate change, so the downside assumption is a delay in weeks. Unchanged: the register, the reconciliation cells, the single switch, the trace test.

## Output

The model file, structured as above, plus this summary in the message body and on the cover sheet.

```
MODEL SUMMARY
Question:      [the decision this serves, one sentence]
Version:       [n]    Date: [ ]    Author: [ ]
Period:        [start] to [end], [granularity]
Anchored on:   actuals through [month]

BASE CASE ANSWER
[One or two sentences. The number and what it means.]

RANGE
| Scenario | Headline output | Key assumption that differs |
| Downside |  |  |
| Base     |  |  |
| Upside   |  |  |

THE TWO ASSUMPTIONS THAT MOVE THE ANSWER MOST
| Assumption | Base value | Flexed by | Effect on headline | Source |

CHECKS
Reconciliation cells all zero: [yes / no, and which]
Balance sheet balances:        [yes / not applicable]
Trace test:                    headline traced to inputs in [n] minutes

WHAT I WOULD VERIFY NEXT
[The input whose weakness most limits confidence, and how to check it.]
```

For an audit, deliver the findings table: finding, cell reference, effect on the headline number, effort to fix.

## Failure modes

**The model built backwards from a wanted number.** Recognise it by an assumption sitting at an oddly specific value with no source, usually a conversion or growth rate. Fix by anchoring every rate to history or a labelled assumption, and report what the anchored model gives before any adjustment.

**Precision standing in for accuracy.** Forty-eight monthly columns for a business that cannot forecast next quarter. Recognise it when granularity exceeds evidence. Fix by shortening the horizon or coarsening the periods.

**Hard-coded numbers inside formulas.** The defining defect. Recognise it by searching for digits in formula cells. Fix by moving each into the register; the count found is itself a reportable finding.

**Two independent computations of the same quantity.** Recognise it because the two disagree at some period and nobody noticed. Fix structurally: compute once, reference everywhere.

**Scenarios as separate files.** Recognise it by three filenames sharing a stem. Fix with one switch cell.

**The model nobody can update.** Recognise it because the last version is four months old and no actuals were ever entered, usually because the line items do not map to the chart of accounts. Fix by rebuilding the output lines to match how costs are booked.

## Edge cases

**No history at all.** Build bottom-up from unit economics with every assumption benchmarked to an external comparable and labelled with source and date. Widen the range beyond what feels comfortable and state the single assumption the model rests on. `expected-revenue-estimation` carries the estimation methods.

**A material assumption is genuinely unknowable.** Do not average a guess. Model both ends of the plausible range and state the threshold at which the decision changes. "This works if retention holds above eighty-four percent" is more useful than a point estimate of eighty-eight.

**The model is going into a data room.** Add a locked read-only version, remove any tab carrying individual salaries or personal data, and confirm no formula references a file the recipient will not have. `fundraise-readiness` holds the wider list. Where multiple currencies are involved, put the rate in the register with its date and source and convert in one place only.

**Someone insists on a single point estimate.** Give the base case as the headline with the range attached in the same sentence. Refusing a number reads as evasion; giving one without a range invites it to be treated as a commitment.

## Quality bar

- Every input is in the assumptions register, labelled with unit and source, and visually distinct as an input.
- No hard-coded number exists inside any formula anywhere in the workbook.
- Changing the single scenario switch moves every headline output.
- Every reconciliation cell reads zero and the checks block reads pass, visibly.
- Any headline output traces to its inputs in under two minutes by someone who did not build the model.
- The two assumptions that move the answer most are named, with the size of their effect.
- Actuals and forecast sit on the same rows, so the model reconciles to the management accounts.
- The summary states the question, the base case, and the range, in that order.

## Related skills

`structured-problem-solving` frames the question this model answers and runs first when it is still vague. `spreadsheet-analysis-workbook` is the underlying workbook discipline. `revenue-forecast` builds the current year revenue number on this structure; `pricing-and-resourcing-model` applies it to a single engagement; `pipeline-deep-dive` supplies the measured conversion rates that reach it through the forecast. `annual-planning-and-headcount` consumes the cost and headcount blocks built here. `expected-revenue-estimation` covers the case with no history to anchor on. `board-deck` and `investor-update` present the outputs, and `decision-memo` is the home for a comparison that needs no model at all.
