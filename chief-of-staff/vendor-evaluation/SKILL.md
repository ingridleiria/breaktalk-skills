---
name: vendor-evaluation
description: Evaluates and compares vendors, tools, and service providers for a purchase, renewal, or replacement, producing weighted requirements fixed before any scoring, an evidence-backed comparison where every score names its source, total cost of ownership over the full term including internal effort and exit costs, verified security and viability checks, reference calls including one the vendor did not supply, a risk register, negotiation points with a walk-away, and a recommendation memo someone else can audit. Enforces the standard that requirements and weights are frozen before options are scored and that no score rests on a vendor-run demo alone. Use this skill whenever someone asks to compare vendors or software, evaluate a supplier proposal, decide whether to renew or switch, build a total cost comparison, prepare for a vendor negotiation, or says which tool should we buy, is this vendor any good, are we getting value from this contract, should we renew, review this before we sign.
---

# Vendor Evaluation

A vendor decision is a multi-year commitment usually made on the strength of a forty-five minute demonstration, run by a person whose job is to run it well, using data chosen to make the product look effortless. The requirements document, where one exists, is often written after the shortlist, which means it describes the front-runner. The decision is then made, and everything after it is procurement.

The cost surfaces in three predictable places. The first is the implementation, where the internal hours nobody counted turn a 40,000 dollar licence into a 150,000 dollar first year. The second is the renewal, where a notice period buried in an order form has already passed and the price rises by the escalation clause nobody negotiated. The third is the exit, where the data comes out in a format that requires a project to use, and switching costs more than three years of the alternative would have.

None of these are discovered by a better demo. They are discovered by writing down what the organisation needs before looking at options, by insisting on evidence for every claim, and by costing the whole term rather than the first invoice.

## When to use this, and when not to

Use it for any purchase, renewal, or replacement of a tool or service provider above trivial size, where trivial means a cost the owning manager could approve without discussion and could reverse next month. Use it for renewals in particular, because renewal by inertia is a decision made by a calendar.

Do not use it for a partner you go to market with rather than buy from: that is `partnership-assessment`, which weighs mutual commitment and channel economics rather than fitness for a defined job. Do not use it to contract individual people for delivery work, which is `contractor-msa-and-task-order`. Do not use it to draft the agreement, which is `business-agreements-drafting`, and do not treat this skill's commercial review as legal advice. Where the real question is whether to buy anything at all, run `decision-memo` first, with doing nothing as a named option, because a well-run evaluation of four vendors is a persuasive answer to a question nobody had asked.

Where the purchase concerns capability the organisation might build rather than buy, the build option is one of the candidates and gets costed on the same basis, including the internal effort and the ongoing maintenance that vendors quote and internal proposals routinely omit.

## What you need before starting

**The job to be done, with volumes.** What the tool or service must accomplish, stated as outcomes for the people who will use it, with the transaction volumes, user counts, and integrations involved. Missing: interview two of the actual users for twenty minutes each before writing anything. An evaluation built from a manager's description of what their team does is scored against a fiction.

**The must-haves that disqualify.** The short list of requirements that eliminate an option if unmet: a compliance obligation, data residency, integration with a named system, a capability without which the job cannot be done. Missing: derive them from the job and get them confirmed in writing. Keep the list short, because a long must-have list is a wish list that will quietly be relaxed for the preferred vendor.

**The budget ceiling, the timeline, and the procurement rules.** Missing: ask, because discovering a competitive tender threshold after the shortlist is set costs weeks.

**Access to the real users for a trial.** The single highest-value input, and the one most often refused for reasons of time. Missing: escalate the request once, and if it is still refused, score usability from a scripted session run on the organisation's own scenarios and mark those scores explicitly as demo-based rather than trial-based.

**Current-state data, for a renewal or replacement.** Actual usage, adoption, what the incumbent has delivered, and its performance against the existing service levels. Missing: pull whatever usage data exists before opening the conversation with the incumbent, because their account team will supply a version of it that is accurate and selectively framed.

**The security and compliance requirements, from whoever owns them.** Missing: ask for the organisation's standard due diligence questionnaire; if none exists, require certification documents, data location, subprocessor list, and breach history as a minimum, and say that a fuller review is outstanding.

## The method

1. **Write the requirements before looking at any vendor.** The job, the volumes, the must-haves, the constraints. This ordering is the whole discipline: requirements written after a shortlist describe the shortlist.

2. **Build eight to twelve weighted criteria, with anchors.** Cover functional fit, usability for the actual users, integration, security and compliance, vendor viability and support, implementation effort, and cost. Weights sum to 100. For each criterion, write what a score of 1, 3, and 5 looks like in concrete terms, so two people scoring separately land within a point. Agree the weights with the stakeholders and freeze them. Changing weights after scoring is how evaluations get rigged, usually with good intentions.

3. **Longlist, then cut to three to five on must-haves only.** Do not score the longlist; it wastes effort and creates a false impression of rigour. Record why each eliminated option failed, because that record is what stops the same option being reintroduced in the meeting by someone who saw a good advertisement.

4. **Gather evidence per option, and name the source of every score.** In descending order of weight: a hands-on trial by the actual users on their own work, a scripted session using the organisation's scenarios and data rather than the vendor's, documentation, and reference calls. A score with no evidence source is a guess and is marked as such in the table. This is the rule that most changes the outcome, because it makes the difference between a demonstrated capability and a claimed one visible in the comparison itself.

5. **Build the total cost of ownership over the full intended term,** usually three years. Include licence or subscription fees with user or volume growth modelled, implementation and migration, internal time at fully loaded cost, integration work, training, ongoing administration, support tier, the price escalation clause, and exit costs including data extraction and switching. The list price is frequently less than half the total, and the ranking of options changes once the whole cost is present more often than not.

6. **Verify viability and security against documents, not marketing pages.** Company age, funding or profitability signals, customer base, roadmap credibility, acquisition risk, and support responsiveness observed during the trial. Certifications checked against the actual certificate and its scope and date. Where a research or news tool is available, use `external-insights` for the background; where it is not, use the vendor's own filings, published customer lists, and public incident history, and cite sources with dates.

7. **Call references, including one the vendor did not supply.** Two or three current customers of similar size and use. Ask what implementation was actually like, what does not work, how support behaves when something breaks, what they would do differently, and whether they would buy again. Then find one customer the vendor did not offer, through a professional network or a published customer list. That call is worth the other two combined, and it is the step most often skipped.

8. **Review the commercial terms.** Term and renewal mechanics, with the auto-renewal notice period read carefully because it is the commonest trap; price protection and escalation caps; service levels and their remedies; termination rights; data ownership and export format; liability caps. Flag anything beyond commercial terms for legal review rather than interpreting it.

9. **Score, then test the scoring.** Must-have pass or fail shown first, then the weighted table with evidence notes in each cell, then total cost of ownership beneath it. Where the top two are close, run the sensitivity: how far would a weight have to move to flip the result. If a two-point shift in one weight changes the winner, say so plainly rather than presenting a false margin.

10. **Write the risk register and the recommendation.** Top three risks per shortlisted option with likelihood, impact, and mitigation. Then the memo, in `decision-memo` format: the decision, the recommendation with its reasoning, the cost over the term, the risks being accepted, the negotiation points, the implementation outline, and the decision requested with a date and a default.

11. **Set the negotiation position before the call.** The competing quote as the reference, the term traded for price, the escalation cap, an extended renewal notice period, service levels with credits, implementation support included, a pilot or opt-out clause, and price locks for growth tiers. The walk-away is the second-ranked option, costed. An evaluation that produces only one acceptable answer has also produced no negotiating position.

## The cost model

The total cost of ownership lives in a workbook built to the discipline in `financial-model-builder` and `spreadsheet-analysis-workbook`, because this is the number that gets challenged and the one most often assembled by hand.

Raw price lists, quotes, and rate assumptions in the workbook, with their source and date. Every cost cell a live formula, so changing the user growth assumption reprices every option at once. Derived fields referencing computed cells rather than recomputing: year three licence cost reads year two multiplied by the escalation input, never a separately typed figure. A visible reconciliation cell reading zero, confirming that the sum of the cost lines equals the headline total for each option. And every assumption in a labelled input cell: user growth, escalation percentage, internal hourly cost, implementation days, and the term length. Present the base case and one growth scenario, because most contracts are priced per seat and most organisations grow.

## Worked example

**Situation.** A 300-person services company replacing an applicant tracking system after four years. The head of talent had seen a demonstration of a product she liked and asked for approval to proceed. All figures in this example are US dollars. Nine years of candidate records sat in the incumbent system, and the incumbent's renewal date was five months away.

**Task.** Produce an auditable recommendation within four weeks, in time to negotiate rather than to accept.

**Action.** Requirements were written first, from twenty-minute conversations with three recruiters and one hiring manager. Two findings emerged before any vendor was contacted. The recruiters' actual bottleneck was interview scheduling across four time zones, which had not appeared in the original brief at all, and the reporting requirement the head of talent had emphasised was needed once a quarter by one person. Both facts moved weights substantially: scheduling went to 18, quarterly reporting to 8.

Eleven criteria were agreed with weights summing to 100, with anchors written for 1, 3, and 5. Six candidates were longlisted and cut to four on must-haves, two failing on data residency.

Trials ran for eight working days with two recruiters using live requisitions. The product the head of talent had seen scored 4 on demonstration and 2 in the trial, because its scheduling flow required the coordinator to leave the system for calendar conflicts, which the scripted demonstration had avoided. That single gap between demonstrated and trialled behaviour was the most valuable finding in the exercise.

Total cost of ownership over three years reordered the field again. The apparent leader listed at 48,000 dollars a year, but implementation and the migration of nine years of records was quoted at 34,000 dollars, the payroll integration required 22 days of internal engineering at loaded cost, and the escalation clause was seven percent annually uncapped. Total came to 214,000 dollars. The option listed at 31,000 dollars a year, with migration included and a native integration, came to 178,000 dollars with escalation capped at four percent after negotiation.

The wrong turn: after scores were in and the head of talent's preferred option ranked third, a proposal was made to raise the reporting weight from 8 to 15 on the argument that reporting had been underrated. The change would have moved her preference to first. It was declined and handled instead by sensitivity analysis, which showed the ranking held unless reporting rose above 19, at which point it would also have exceeded the weight on scheduling, which no one was prepared to defend out loud. Running the sensitivity rather than refusing the request kept the process intact and kept the head of talent in it.

Reference calls found the last material fact. Two references were supplied by the leading vendor and were positive. A third customer, found through a recruiter's professional network, reported that support response times had roughly doubled after the vendor was acquired the previous year, which was consistent with a slower trial response nobody had thought worth recording.

**Result.** The recommendation was the second option, first on weighted score by 0.4 points and first on total cost by 36,000 dollars, with the closeness of the score stated in the memo rather than smoothed. The support finding became a negotiated service level with credits, and the renewal notice period was moved from 90 days to 30. The incumbent, told there was a live competitive process, offered a 22 percent reduction to stay, which was declined and which usefully established what the organisation had been overpaying.

Approved in one meeting with no further analysis requested. The migration ran two weeks late.

### A second scenario, where it goes differently

A different situation: a monitoring tool renewal, discovered three weeks before the renewal date, with a 60-day cancellation notice that had already passed. The evaluation cannot be run, because the deadline it would inform is gone. Attempting one anyway produces a rushed comparison whose only possible conclusion is to renew.

The method inverts. The first action is to establish the exact contractual position and write it down. The second is a single negotiation with one objective, which is to convert the auto-renewal into a shorter term or to extend the notice window, accepting a worse price if necessary in exchange for the option to leave. The third is a calendared reminder at the new notice date minus ninety days, owned by a named person, at which point the full evaluation runs with time to use its result.

What changed is not the standard but the sequence: with no time to decide well, the goal becomes buying the ability to decide well later. It is worth paying a few percent for that. It is not worth running an evaluation whose conclusion is fixed by the calendar and then presenting it as a choice.

## Output

Two artefacts: the comparison workbook and a recommendation memo of one page with appendices.

```
VENDOR EVALUATION, [what is being bought]              [date]
Decision requested by: [date]     Decider: [name]     Term evaluated: [n] years

RECOMMENDATION
[One or two sentences. The option, the cost over the term, the single strongest reason.]

MUST-HAVES
| Requirement | Option A | Option B | Option C |   (pass / fail only)

WEIGHTED COMPARISON
| Criterion | Weight | A: score, evidence | B: score, evidence | C: score, evidence |
Weighted totals: A [ ]  B [ ]  C [ ]
Evidence key: T = user trial, S = scripted session on our scenarios, D = documentation, R = reference call, N = no evidence
Sensitivity: the result flips if [criterion] rises above [weight].

TOTAL COST OF OWNERSHIP, [n] years
| Line | A | B | C |
| Licence or fees, with growth |  |  |  |
| Implementation and migration |  |  |  |
| Internal effort, at loaded cost |  |  |  |
| Integration and training |  |  |  |
| Ongoing administration |  |  |  |
| Exit and switching |  |  |  |
| Total |  |  |  |
Assumptions: user growth [ ], escalation [ ], internal hourly cost [ ]

RISKS ACCEPTED
| Risk | Likelihood | Impact | Mitigation | Early signal |

REFERENCES
| Company | Size and use | Supplied by vendor? | What they said that mattered |

NEGOTIATION POINTS AND WALK-AWAY
[The asks in priority order. The walk-away option, costed.]
```

## Failure modes

**Requirements written after the shortlist.** Recognise it when a requirement matches one vendor's feature naming. Fix by rewriting from user interviews and re-agreeing weights before scoring resumes.

**Weights adjusted after scores are in.** Always well intentioned, always fatal to the evaluation's credibility. Recognise it by any proposal to reweight that arrives after the table is populated. Fix by running sensitivity instead, which answers the underlying question honestly and keeps the requester engaged.

**The demo scored as though it were a trial.** Recognise it when usability scores are high and no user has touched the product. Fix with an evidence key on every cell, which makes the absence visible in the comparison itself.

**List price treated as cost.** Recognise it when internal effort, migration, and exit appear nowhere. Fix with the full-term model, and note that the ranking changes more often than not.

**References all supplied by the vendor.** Recognise it because every reference is enthusiastic. Fix by finding one the vendor did not offer, which is usually possible through a professional network or a published customer list.

**The auto-renewal discovered late.** Recognise it by checking notice dates at the start of every evaluation rather than the end. Fix by calendaring the notice date minus ninety days with a named owner, on the day the contract is signed.

**The evaluation with only one acceptable outcome.** Recognise it because no second option was costed. Fix by costing the runner-up properly, since without it there is no negotiating position and the vendor knows it.

## Edge cases

**Only one viable vendor.** Say so, and shift the work from comparison to negotiation and risk mitigation. Cost the build option and the do-nothing option anyway, because they are what set the ceiling on price.

**A renewal where switching is genuinely impractical.** Be honest that leverage is limited, and negotiate on the terms that survive lock-in: escalation cap, notice period, service levels, and data export commitments. Note the lock-in as a risk with a plan to reduce it before the following renewal.

**An executive has effectively decided already.** Run the evaluation on the merits and present the result, including the sensitivity. If the decision goes against the analysis, record the reasoning in the decision log rather than reworking the analysis to agree with it. The record is what makes the next evaluation credible.

**A free or open-source option is in scope.** Cost it on the same basis. Zero licence cost with 30 days a year of internal maintenance at loaded cost is not free, and stating that in the same table as the paid options is usually more persuasive than arguing it.

**The purchase is small but the switching cost is large.** Proportionality is about switching cost, not price. A cheap tool that becomes embedded in a workflow gets the full evaluation; an expensive one that can be cancelled monthly does not.

**Security review is required and there is no security function.** Use the vendor's certification documents, ask for their most recent penetration test summary and subprocessor list, and state in the memo which questions remain unanswered and who would need to answer them. Do not imply a review happened that did not.

## Quality bar

- Requirements, criteria, weights, and anchors were fixed and agreed before any option was scored.
- Every score carries an evidence source, and trials were run by the people who will use the product.
- Total cost of ownership covers the full term including internal effort, escalation, and exit costs, in a workbook where every cell is a live formula.
- At least one reference was found that the vendor did not supply.
- The auto-renewal notice period is stated, and a named owner holds a dated reminder before it.
- Where the top two options are close, the sensitivity is stated rather than the margin smoothed.
- The memo names the risks accepted, the negotiation points, and the costed walk-away.
- The recommendation appears before the analysis, with one named decider and a date.

## Adapting this to your context

The eight to twelve criteria, the three-year term and the three to five shortlist come from software and service purchases inside commercial companies of one hundred to a thousand people, buying without a formal tender.

- **Three years as the term evaluated.** Use five or seven for infrastructure or anything where migration cost dominates, and one year for a tool that can be cancelled monthly. The term sets the cost model.
- **Eight to twelve weighted criteria.** Below a certain size, four criteria and a total cost line is proportionate. Where a formal tender applies, the buyer's published evaluation framework replaces yours.
- **Freezing weights before scoring.** Public procurement usually requires the weights to be published to bidders in advance, which makes the freeze contractual rather than a matter of discipline. Sensitivity analysis is still the answer to a late reweighting request.
- **The eight-day user trial.** Where a trial is impossible, for infrastructure or a regulated system, substitute a scripted session on your own scenarios plus a site visit, and mark the scores as what they are.
- **What not to change.** Requirements and weights are fixed before any option is scored, every score names its evidence, and at least one reference is found that the vendor did not supply.

## Related skills

`decision-memo` is the format the recommendation is written in and where the decision is logged. `structured-problem-solving` frames the question when it is still unclear whether to buy at all. `external-insights` and `market-research` supply the viability and landscape research. `financial-model-builder` supplies the workbook discipline for the cost model. `partnership-assessment` covers partners rather than suppliers, and `contractor-msa-and-task-order` covers contracting individual people. `business-agreements-drafting` handles the agreement once the commercial shape is agreed. `process-documentation-sop` documents the workflow the chosen tool supports, and `ai-adoption-program` covers the adoption work that decides whether the purchase was worth making.
