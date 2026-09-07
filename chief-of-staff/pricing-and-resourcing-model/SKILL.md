---
name: pricing-and-resourcing-model
description: Prices a single client engagement and staffs it in one model: a bottom-up effort build by role and phase, fully loaded cost, realistic utilisation and ramp, the fee under each commercial structure being considered, gross margin under base and two downside scenarios, and a named-people capacity view against the calendar. Enforces the standard that the price is traceable to the effort build, that margin is shown under downside as well as base, and that the walk-away point is set before negotiation begins. Use this skill whenever someone needs to price a proposal, size the team an engagement requires, check whether a deal is profitable, build a staffing plan, model a retainer or a build-operate-transfer arrangement, compare fee structures, or says how much should we charge, what team do we need for this, is this deal worth doing, can we afford to discount, price this engagement.
---

# Pricing and Resourcing Model

The failure begins with a round number. Somebody says the client will probably pay around 250,000 dollars, the proposal is written to that figure, and the team is assembled afterwards from whoever is free. Four months into delivery the engagement is running two people heavier than priced, the lead is working weekends, and the margin is discovered by the finance team in a quarterly review rather than by anyone who could have acted on it.

The direct loss on that engagement is the smaller half of the cost. The larger half is that the number becomes a reference. The client now knows what this kind of work costs from this firm, the account team quotes the same shape next time, and a price set by intuition in one meeting sets the economics of a relationship for years. Worse, the delivery team learns that the numbers in a proposal have nothing to do with the work, which is the point at which they stop giving honest estimates.

A pricing model exists to make three things visible at once, before the number goes into a document: what the client will see as value, what the team can actually staff without heroics, and what the margin survives when the predictable things go wrong.

## When to use this, and when not to

Use it to price any client engagement where people deliver the work: a fixed-fee project, a time-and-materials arrangement, a retainer, a milestone-gated programme, a managed service, or a build-operate-transfer deal. Use it also to check the economics of a deal already under negotiation, and to work out whether a requested discount is survivable.

The boundaries against the other numeric skills matter, because all four produce spreadsheets full of money:

- `financial-model-builder` models the whole company or business unit over multiple years. This skill models one engagement, in weeks and months, and borrows that skill's workbook structure. If the question is about the firm's economics rather than this deal's, that skill owns it.
- `revenue-forecast` builds the annual and quarterly revenue number in layers of certainty. A signed engagement priced here becomes one line in its contracted layer, but pricing a deal is not forecasting.
- `pipeline-deep-dive` analyses the opportunity set and its conversion. It tells you whether the deal is likely to close; this skill tells you what to charge if it does.

Do not use this to write the proposal, which is `proposal-writer`, or to define scope and acceptance criteria, which is `sow-and-scope`. Both consume this model's output. Do not use it to price a product or a subscription, where the economics are set by unit economics and market position rather than by effort. Do not price at all where scope is genuinely undefined: price a paid discovery phase and defer the rest, which is a better commercial position than a large number with a wide error band.

## What you need before starting

**The scope, as deliverables with a boundary.** What is produced, over what duration, in what phases, and what is explicitly excluded. Missing: price the discovery phase only, and say plainly that the remainder will be priced when the outputs of discovery exist. Pricing an undefined scope is guessing with a decimal point.

**A bottom-up work breakdown.** For each phase, the activities and the roles they require, with effort in days per role. This is the load-bearing input and the one most often skipped. Missing: build it with the delivery lead who would actually run the engagement, not with the account owner. An hour with the right person is the difference between a model and a wish.

**Fully loaded daily cost by role.** Salary, employer costs, benefits, and the overhead allocation the firm uses. For subcontracted people, the actual contracted rate. Missing: ask finance for the current loaded rate table; if unavailable, use salary multiplied by the firm's standard overhead factor and label the whole cost block as estimated.

**Realistic billable days per person per month.** Fifteen to eighteen is the range in the mid-size project-based services firms this file is written from, not twenty-two. Holidays, internal work, sales support, and sickness are not optional. Missing: use sixteen as a default, label it in the cell as a default rather than a measurement, and replace it with your own figure from the last two quarters of timesheets before the model leaves the building. Agencies carrying heavy internal product work, in-house teams and firms with large sales-support obligations commonly run lower; dedicated managed-service teams run higher. This single number moves the required headcount more than any other, which is exactly why it should not be inherited from somebody else's firm.

**Ramp time.** Weeks before a person new to the engagement is productive, and who pays for those weeks. Missing: assume two weeks at fifty percent productivity for a person new to the client and four for a person new to the firm, and label it.

**Client-side dependencies.** What the client must supply, by when, and what the delay costs when they do not. Missing: list the dependencies you can infer and put the delay cost in the downside scenario. Every services engagement that ran late has one of these in its history.

**The firm's margin floor and rate card.** Your firm's, not the ones in this file. Missing: ask, because a price below the floor is a decision for someone other than the person building the model, and finding that out after the proposal is sent is expensive.

## The method

1. **Write the scope boundary first,** including the exclusions, in the workbook. Everything priced later refers to it. Scope written after the price is scope written to justify the price.

2. **Build effort bottom-up, by role and phase, with the delivery lead.** Days per role per phase. Ask for the estimate as a range and take the upper end for anything the team has not done before. The rule: any phase estimated by one person in isolation gets a second opinion, because single-source estimates in services work run low with remarkable consistency.

3. **Cross-check against a top-down reference.** What did the two most similar past engagements cost and take? A bottom-up build more than about thirty percent away from the closest comparable is investigated before proceeding, in either direction. Top-down is the check, never the substitute.

4. **Convert effort into people using realistic utilisation.** Days required divided by billable days available per month gives the headcount curve. The judgement call is whether to round up to whole people or to plan on partial allocation. Rule: round up wherever a role is on the critical path or requires continuity of context, and allow partial allocation only for advisory or review roles.

5. **Apply ramp and continuity.** Add the ramp cost for anyone new, and check for handovers. A person leaving mid-engagement costs roughly their replacement's ramp plus a week of the person handing over, and if the plan contains a known handover it belongs in the base case, not the downside.

6. **Cost it, then add contingency with a stated basis.** Contingency is a percentage tied to a named uncertainty, not a comfort blanket. Typical basis: scope definition quality, client dependency risk, technology novelty. Write the reason beside the number, because an unexplained contingency is the first thing a client's procurement function will challenge.

7. **Price under each structure being considered,** from the same cost base. For fixed fee, cost plus target margin plus a risk premium sized to scope uncertainty. On the margin numbers: the forty percent target and twenty-five percent floor used in the worked example are the defaults of one kind of firm, a mid-size specialist services business selling defined project work to corporate buyers. They are defaults, not a standard. Staff augmentation and resourcing models run viably at fifteen to twenty-five percent gross margin; highly specialised advisory and firms with product leverage run well above forty. Get the target and the floor from your own finance function and write both in labelled cells before either is used as a test. For time and materials, rate card multiplied by effort with a not-to-exceed figure. For a retainer, reserved capacity multiplied by rate, with a utilisation assumption and a rollover rule.

8. **Test the margin under two downsides, always the same two.** Scope grows twenty percent, and the start slips by one month while the team is already committed. If margin falls below your firm's own floor under either, and not the illustrative twenty-five percent used here, change the price or change the structure. Do not proceed on the argument that it will not happen; the two downsides are chosen precisely because they are the ones that do.

9. **Set the ceiling from client value, not from cost.** Estimate the value in the client's own numbers: revenue gained, cost saved, risk avoided, time released. A price above roughly twenty to thirty percent of clearly demonstrable annual value is hard to defend in a procurement conversation; a price below ten percent of it leaves money on the table and can signal that the work is minor. Where value cannot be quantified, price from cost and comparables and say so internally.

10. **Choose the structure by where the risk sits.** Fixed fee when scope is tight and the firm controls delivery. Time and materials when scope is genuinely open. Milestones when the client needs to gate spend. Retainer when the value is availability rather than output. Outcome-linked only where the outcome is measurable, attributable, and inside the firm's control, which is rarer than it sounds.

11. **Set the walk-away point before any negotiation,** with its reason: margin floor, capacity opportunity cost, or a strategic value that is written down rather than asserted. A walk-away decided during a call is decided by whoever is most tired. Then present at most two options, because three invites the client to design a fourth from the parts they like, which is always the cheapest combination.

## The workbook

Built with the structure and discipline in `financial-model-builder` and `spreadsheet-analysis-workbook`: raw inputs in the workbook, every analysis cell a live formula, derived fields referencing computed cells rather than recomputing them, a visible reconciliation cell reading zero, and every assumption in a labelled input cell.

**Effort sheet.** Role by phase by month, in days, with totals per role, phase, and month. The source of everything downstream.

**Cost sheet.** Effort multiplied by loaded daily cost, referencing the effort sheet rather than repeating it, plus expenses, subcontractors, and a contingency line stated as a percentage with its rationale beside it.

**Price sheet.** The fee under each commercial structure considered, each built from the same cost base so the comparison is honest.

**Margin sheet.** Gross margin by phase and overall, under base and both downside scenarios, with a reconciliation cell confirming that revenue minus cost equals the margin shown.

**Capacity sheet.** Named people or open roles against the calendar, showing conflicts with other engagements and the point at which hiring or subcontracting becomes necessary.

## Build-operate-transfer and managed services

These arrangements need three additional blocks, because the economics change shape across the term.

**Phase economics.** Build, operate, and transfer are modelled separately for revenue, cost, and margin, then cumulatively. Build is often at low or zero margin and sometimes partly at risk; operate is where the margin is earned; transfer carries a handover cost and sometimes a fee or a credit. State the month at which cumulative margin turns positive. That single figure is what tells the firm how much of the deal is a loan to the client.

**Staffing ramp and attrition.** Headcount by month through build and operate, with hiring lead times, the cost of bench between a hire starting and becoming billable, and an explicit attrition assumption. In a multi-year operate phase, attrition is not a risk, it is a certainty, and a model that omits it will be wrong by more than its margin.

**Transfer terms.** What transfers, being people, process, tooling, and intellectual property, when the client may trigger it, the fee, and the notice period. The model also shows the client's total cost across the arrangement against building the capability in-house, because that comparison is the sale, and a client who has not seen it will build their own version with worse assumptions.

## Worked example

**Situation.** A sixty-person data engineering firm asked to price a nine-month platform migration for a mid-sized insurer. The account owner had already told the client the work would be "in the region of 300,000 dollars". Procurement wanted a fixed fee. All figures in this example are US dollars, and the firm's own margin target and floor are used throughout. The client's own team would supply data access and business rules validation.

**Task.** Produce a defensible fixed-fee price with a staffing plan, in five working days, and establish whether the figure already mentioned was survivable.

**Action.** The effort build was done with the engineer who would lead delivery, over two sessions. It came to 412 person-days across four phases: discovery 46, build 214, migration and parallel run 112, handover 40. Loaded daily costs, in dollars, were 780 for the principal, 520 for the lead engineer, 390 for an engineer, 300 for an analyst. Direct cost was 187,400 dollars, and contingency at twelve percent, on the stated basis that the source system documentation was known to be incomplete, took it to 209,900 dollars.

The wrong turn came at the staffing conversion. The first pass divided effort by twenty-two working days a month and concluded the engagement needed 2.8 full-time people, which produced a comfortable-looking plan and an impossible one. Rebuilt at sixteen billable days, the requirement was 3.9, which meant four, with the fourth needed from month three. The firm had no fourth engineer free then, so the plan added a subcontracted engineer at 460 dollars a day against an internal cost of 390 dollars, adding 11,000 dollars. That correction, from one assumption cell, moved the required price by about nine percent and was the difference between a plan that worked and one that would have consumed the lead's weekends from month four.

Value was estimated in the client's terms: the legacy platform cost roughly 340,000 dollars a year to run and the migration removed most of it, so demonstrable annual value was around 300,000 dollars. A fee near that level is defensible for a one-off migration with a permanent saving behind it.

The fixed fee was set at 348,000 dollars, being cost plus contingency plus this firm's forty percent target margin. Scope growing twenty percent took margin to 27 percent, above this firm's floor of 25. A one-month start slip with the team already committed took it to 24, below the floor, so the proposal carried a mobilisation clause: the team is reserved from a named date, and a delayed start bills reserved capacity at half rate. That clause, not the price, was the most valuable output of the model.

**Result.** Priced at 348,000 dollars against the 300,000 dollars the client had heard, with the difference explained by the effort build and the migration parallel run, which the earlier conversation had not accounted for. The client negotiated to 335,000 dollars in exchange for a two-week extension on the handover phase, which cost the firm 4,000 dollars of effort against a 13,000 dollar price reduction, so margin closed at 36 percent. The walk-away had been set at 310,000 dollars and was never reached, which is what a walk-away is for.

The start slipped by three weeks. The mobilisation clause billed 22,000 dollars and margin closed at 38 percent, above the base case.

### A second scenario, where it goes differently

A twelve-month advisory retainer at a fixed monthly fee for a named team's availability. The risk inverts. In a fixed-fee project the danger is over-delivery. In a retainer the immediate danger is under-consumption, because a client who uses half the reserved capacity for three months starts to see the fee as poor value and cancels at the first review, even though those were the profitable months.

The model changes in three ways. It carries a utilisation floor and ceiling rather than one figure, so the fee is set at expected consumption while margin is shown at both ends. It carries a rollover rule with a cap, usually one month, because unlimited rollover converts a retainer into a deferred liability that all arrives in the final quarter. And it makes a consumption report a delivery obligation, because retainer risk is managed by visibility rather than by pricing. The downside modelled is not scope growth but the client consuming at the ceiling for three consecutive months while the team is committed elsewhere, and that scenario is what sets the contractual ceiling.

## Output

Three deliverables: the workbook, a one-page pricing memo, and the investment section for the proposal.

```
PRICING MEMO
Engagement:     [client, work, duration]
Structure:      [fixed fee / T&M / retainer / milestones / BOT]
Recommended price: [ ]        Walk-away: [ ] because [reason]

THE TEAM
| Role | Phase | Days | Loaded daily cost | Cost | Named person or to be hired |

THE NUMBERS
| Line | Base | Downside A: scope +20% | Downside B: start slips one month |
| Revenue |  |  |  |
| Direct cost |  |  |  |
| Contingency |  |  |  |
| Gross margin |  |  |  |
| Gross margin % |  |  |  |
Margin floor: [ ]. Breaches floor under: [none / A / B]

ASSUMPTIONS THAT MOVE THE ANSWER MOST
| Assumption | Value used | Basis | Effect if wrong by 20% |

CLIENT VALUE
[Value in the client's numbers, and the fee as a percentage of it.]

TERMS THAT PROTECT THE MARGIN
[Mobilisation, change control, dependency delay, payment schedule.]
```

Where a chart is used, show the monthly staffing curve and the cumulative margin curve, monochrome, series separated by dash pattern and marker rather than colour, legend outside the plot area, with the month cumulative margin turns positive marked on the axis.

## Failure modes

**The price set first and the effort built to match.** Recognise it when the bottom-up total lands within a few percent of a round number mentioned earlier. Fix by having the delivery lead estimate before seeing any price, and by reporting the bottom-up figure before any adjustment.

**Utilisation assumed at working days.** Twenty-two billable days a month. Recognise it by dividing total effort by duration and comparing to what people actually bill. Fix by putting utilisation in one labelled cell and setting it from the firm's own history.

**Contingency as a comfort blanket.** A round ten percent with no basis. Recognise it by the absence of a reason beside the number. Fix by naming the specific uncertainty it covers, which usually also identifies the term that would remove it.

**Margin shown only in the base case.** Recognise it by a single margin figure on the memo. Fix with the two standard downsides. A deal that only works when nothing goes wrong is a deal that does not work.

**The discount granted without recomputing.** A client asks for ten percent, someone agrees in the room, and nobody checks what it does to the floor. Fix by setting the walk-away before the call and by holding the model open during it.

## Edge cases

**Scope genuinely undefined.** Price a paid discovery phase with a fixed fee and a fixed duration, and state that the remainder is priced from its output. Clients accept this more often than teams expect, and it is a stronger position than a wide range.

**The client asks for a price before any scoping conversation.** Give a range with the assumptions that would narrow it, explicitly labelled, and offer the discovery phase. Never give a single number, because it will be quoted back as a commitment.

**A strategic loss-leader.** Where the firm chooses to price below the floor for a named reason, such as entering a sector or securing a reference, write the reason, the amount being invested, and the specific thing the firm gets for it, and have that approved by whoever owns the margin. An unwritten strategic discount is just a discount.

**Fixed price demanded on open scope.** Price the fixed portion tightly, put the open portion behind a change control mechanism with a stated day rate, and be explicit that the fixed price covers the defined boundary. If the client will not accept change control, the risk premium rises steeply and the model should show what it becomes.

## Quality bar

- A bottom-up effort build exists for every phase, and the price traces to it.
- Utilisation, ramp, and loaded cost are in labelled input cells, with utilisation set from the firm's own history.
- Margin is shown in the base case and under both standard downsides, against a stated floor.
- The walk-away price is set, with its reason, before any negotiation.
- The capacity view names people or open roles against the calendar and shows conflicts.
- Client value is estimated in the client's own numbers, and the fee is expressed as a percentage of it.
- For build-operate-transfer or managed services, the month cumulative margin turns positive is stated.
- The terms that protect the margin are listed with the price, not left to the contract stage.

## Adapting this to your context

Every number here, the sixteen billable days, the forty percent target margin and the twenty-five percent floor, comes from one kind of firm: a mid-size project-based services business of fifty to three hundred people. Defaults, not standards.

- **Sixteen billable days a month.** Pull your own figure from the last two quarters of timesheets. Agencies with heavy internal product work and in-house teams run lower; dedicated managed-service pods run higher.
- **Forty percent target margin, twenty-five percent floor.** Resourcing and staff augmentation operate viably at fifteen to twenty-five percent; specialised advisory runs well above forty. Ask finance for both and write them in the workbook as your firm's own.
- **Two weeks at fifty percent ramp.** Regulated environments with clearance, credentialing or system access queues run to months, and that wait belongs in the base case rather than the downside.
- **The two standard downsides.** Where the recurring risk is client staff turnover, a regulatory date or a seasonal access window, replace one of them with the downside your own history keeps producing.
- **What not to change.** The price traces to a bottom-up effort build made by the person who would run the work, and the walk-away is set with its reason before the first negotiation.

## Related skills

`financial-model-builder` supplies the workbook structure and models the firm's overall economics. `sow-and-scope` turns the priced scope into deliverables and acceptance criteria, and should be written from this model rather than beside it. `proposal-writer` carries the investment section to the client. `revenue-forecast` consumes signed engagements into its contracted layer, and its capacity check uses the same utilisation assumptions. `pipeline-deep-dive` assesses whether the deal will close at all. `contractor-msa-and-task-order` and `business-agreements-drafting` handle the paper once the commercial shape is agreed. `decision-memo` is the right format when the real question is whether to bid at all.
