---
name: pricing-and-resourcing-model
description: Builds pricing, staffing, and margin models for services and consulting engagements, including fixed-fee proposals, retainers, time-and-materials, build-operate-transfer arrangements, and multi-year programs, with ramp curves, utilization, and scenario views. Use this skill whenever the user needs to price a proposal, estimate the team an engagement needs, check the margin on a deal, build a staffing plan, model a BOT or managed-service arrangement, compare fee structures, or says "how much should we charge", "what team do we need for this", "is this deal profitable", "price this engagement", "resourcing plan". Trigger for any question that connects people, time, and price on a client engagement.
---

# Pricing and Resourcing Model

A services deal is priced correctly when the client sees value they would pay for, the delivery team can staff it without heroics, and the margin survives the things that go wrong. The model exists to show all three at once, before the number goes into a proposal.

## Inputs to establish

1. **Scope**: the deliverables, the duration, the phases, and what is explicitly out. Pricing an undefined scope is guessing; if scope is undefined, price the discovery phase and defer the rest.
2. **Work breakdown**: for each phase, the activities and the roles required, with effort in days or hours per role. Build from the bottom up; top-down "it feels like a $200k project" is checked against the bottom-up, not substituted for it.
3. **Roles and cost**: for each role, the fully loaded daily cost (salary, benefits, overhead allocation) and the target bill rate. For subcontractors, the actual rate.
4. **Utilization and availability**: realistic billable days per person per month (usually 15 to 18, not 22), holiday periods, and existing commitments.
5. **Ramp and onboarding**: weeks before a new person is productive on the engagement, and who pays for them.
6. **Client-side dependencies**: what the client must provide, and the delay cost when they do not.
7. **Commercial structure options**: fixed fee, time and materials, retainer, milestone-based, outcome-linked, or BOT.

## The model

Build in a spreadsheet using the structure from the financial-model-builder skill in this library (assumptions separate, formulas everywhere, scenarios switchable):

- **Effort sheet**: role by phase by month, in days. Totals per role and per phase.
- **Cost sheet**: effort times loaded daily cost, plus expenses (travel, tools, subcontractors), plus a contingency line stated as a percentage with its rationale.
- **Price sheet**: the fee under each commercial structure being considered. For fixed fee, the price is cost plus target margin plus a risk premium sized to scope uncertainty; for time and materials, rate card times effort with a not-to-exceed; for retainers, capacity reserved times rate with utilization assumptions.
- **Margin view**: gross margin per phase and overall, under base, and under two downside scenarios (scope grows 20%, client delays the start by a month). If margin falls below the firm's floor in the downside, the price or the structure changes.
- **Capacity view**: named people or roles against the calendar, showing conflicts with other engagements and the hiring or subcontracting triggers.

## Build-operate-transfer and managed services

BOT and similar arrangements need three additional blocks:

- **Phase economics**: build (setup, often at low or zero margin, sometimes partly at risk), operate (recurring monthly fee against a staffed team, where the margin is earned), and transfer (knowledge transfer, handover cost, transfer fee or credit). Model each phase's revenue, cost, and margin separately, then cumulatively.
- **Staffing ramp**: the team grows through build and operate on a schedule; model headcount by month, the hiring lead time, the cost of bench between hires and billability, and the attrition assumption.
- **Transfer terms**: what transfers (people, process, tooling, IP), when the client may trigger it, the fee, and the notice period. The model shows the client's total cost across the arrangement versus building in-house, because that comparison is the sale.

Output for a BOT proposal: a monthly view for the full term, the cumulative margin curve (usually negative through build and positive after month N; state N), the sensitivity to ramp speed and attrition, and the client's cost comparison.

## Pricing judgment

The model gives the floor; value gives the ceiling. Before finalizing:

- Estimate the value to the client in their numbers (revenue gained, cost saved, risk avoided). A price above 20 to 30% of clearly demonstrable annual value will be hard to defend; a price below 10% leaves money on the table.
- Check the competitive reference: what alternatives cost, including doing it in-house.
- Choose the structure by where the risk sits: fixed fee when scope is tight and the firm controls delivery, T&M when scope is open, milestones when the client needs to gate spend, outcome-linked only when the outcome is measurable and attributable.
- Present two options in the proposal at most; three invites the client to design a fourth.

## Deliverables

1. The model file, structured as above.
2. A one-page pricing memo: the recommended price and structure, the team, the margin in base and downside, the two assumptions that matter most, and the walk-away point for negotiation.
3. The proposal-ready investment section, written plainly, using the proposal-writer skill in this library when the full proposal is needed.

## Quality bar

- Bottom-up effort exists for every phase; the price is traceable to it.
- Margin is shown under downside scenarios, not only base.
- Utilization assumptions are realistic and stated.
- For BOT, the month the cumulative margin turns positive is stated, and the client's cost comparison is included.
