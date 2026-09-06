---
name: financial-model-builder
description: Builds driver-based financial models in spreadsheets (three-statement, operating, or unit-economics models) with explicit assumptions, scenario toggles, and an audit trail, and reviews existing models for errors and hidden assumptions. Use this skill whenever the user wants to build, extend, or check a financial model, budget, cash flow projection, runway model, unit economics, or business case in a spreadsheet, or says "model this out", "what does the P&L look like if", "build a scenario model", "check my model", "how long is our runway", "sanity check these numbers". Trigger for any spreadsheet whose purpose is projecting money over time.
---

# Financial Model Builder

A financial model is an argument about the future expressed in arithmetic. Its value lies in how visibly the assumptions are stated and how easily someone can change one and see what happens. A model that produces a number nobody can trace is a calculator with a hidden agenda.

## Structure every model the same way

Separate sheets (or clearly separated blocks in a small model), in this order:

1. **Cover and guide**: purpose, author, date, version, the question the model answers, and a map of the sheets.
2. **Assumptions**: every input in one place, each with a label, unit, value, source or rationale, and a cell style that marks it as an input (blue text or shaded fill, stated in the guide). Nothing hard-coded anywhere else. Scenario columns (base, upside, downside) live here, selected by one switch cell.
3. **Drivers and calculations**: the operating logic, built from the assumptions: customers, pricing, volumes, headcount, capacity. Formulas only, every row labeled with its unit.
4. **Outputs**: the financial statements or the summary the decision needs (P&L, cash flow, balance sheet where relevant, or the unit economics and payback). Formulas that reference the calculation sheet, never re-typed values.
5. **Checks**: balance sheet balances, cash never negative without a flag, growth rates within plausible bounds, totals reconciling across sheets. A visible "all checks pass" cell.
6. **Scenario summary**: the key outputs side by side under each scenario, plus sensitivity tables for the two or three assumptions that move the answer most.

## Building rules

- Time runs left to right, one period per column, consistent granularity (monthly for the first 24 months is usual for operating models; quarterly or annual beyond).
- One formula per row, copied across, so the logic is readable by reading one column.
- No hard-coded numbers inside formulas. A growth rate typed into a formula is invisible to the reviewer and will be forgotten.
- Units in every label: currency, count, percent, months.
- Sign convention stated once (costs negative or costs positive) and kept.
- Circularity avoided unless essential; if essential, documented and switchable.
- Version the file; keep a change log on the cover.

## Common model types and their core drivers

- **Subscription business**: new customers by channel, conversion, average contract value, churn or retention by cohort, expansion, gross margin, sales and marketing cost per acquisition, headcount plan. Outputs: ARR, revenue, gross profit, burn, cash, runway, CAC payback, LTV to CAC.
- **Services business**: billable headcount, utilization, bill rate, project pipeline and win rate, delivery cost per person, bench cost. Outputs: revenue, gross margin per engagement, capacity constraint, hiring triggers.
- **Marketplace or usage**: transactions, take rate, active supply and demand, activity per user. Outputs: GMV, net revenue, contribution margin.
- **Runway or cash model**: opening cash, collections timing, payment timing, payroll, fixed and variable costs, financing events. Outputs: monthly cash balance, months of runway, the date the company runs out of money under each scenario.

Ask which type applies and what decision the model serves before building; a fundraising model and an operating budget share arithmetic but not emphasis.

## Reviewing an existing model

Run this audit and report findings with cell references:

1. Find every hard-coded number outside the assumptions sheet.
2. Trace the three most important outputs back to inputs; note any break in the chain.
3. Recompute totals independently and compare.
4. Check period alignment, units, and sign conventions.
5. Stress the two biggest assumptions by 20% each way; if the conclusion flips, say so.
6. List the assumptions that have no stated source.

## Delivery

When producing the file, follow the environment's spreadsheet skill for construction and formatting, and apply the structure above. Deliver with a one-paragraph summary: the question, the base-case answer, the two assumptions that matter most, and the range across scenarios. When the user only needs the logic, deliver the assumptions table and the driver tree in text and offer the file.

## Quality bar

- Every input is in the assumptions sheet, labeled, sourced, and styled as an input.
- Changing the scenario switch changes every output.
- All checks pass and are visible.
- A reviewer can trace any output number to its inputs in under two minutes.
