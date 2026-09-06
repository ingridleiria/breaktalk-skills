---
name: ai-adoption-program
description: Runs the adoption of AI inside an organisation as a sequenced programme rather than a scatter of tool purchases. Produces a capability audit of where the work and the time actually sit, a shortlist of two or three pilots each with a baseline measured before anything starts and a stop threshold agreed in advance, a one-page usage policy naming the data categories and the decisions that must stay human, a procurement test run against real tasks with known answers, a fluency programme measured by task rather than by licences, and a quarterly report that carries the failures as prominently as the wins. Use this skill when someone asks which AI tools to buy, wants an AI policy or an acceptable use rule, has been asked by a board or an investor what the AI strategy is, is evaluating an AI vendor, wants to know why last year's tool purchase changed nothing, says the team is already using these tools and nobody knows what data is going into them, or asks how to measure whether any of this is working.
---

# AI Adoption Program

The common failure is not that the tools do not work. It is that an organisation buys licences and has no mechanism by which a licence becomes a changed process. Three or four enthusiasts do genuinely impressive things and talk about them. Everyone else opens the tool twice, finds it does not fit the shape of their work, and returns to the spreadsheet. Twelve months later the only artefact is the invoice, and the honest answer to the board's question is that nobody knows.

The second failure runs alongside the first and costs more. While the official programme stalls, the work continues on personal accounts, because the people under the most time pressure are the most motivated to find a shortcut. Client material, candidate records and unreleased financials go into consumer tools with no contract, no retention terms and no log. The organisation carries the risk without the benefit, and finds out during a customer's security questionnaire or during an incident.

Both have the same root: adoption was treated as a purchase rather than as a programme with a sequence, a named owner, a measurement, and an explicit rule for stopping.

## When to use this, and when not to

Use it when deciding what to adopt and in what order; when a policy is needed because usage is already happening; when a board, an investor or a large customer has asked what the position is; when a previous purchase visibly changed nothing and someone must explain why; or when the leadership team wants a measurement that separates real time saved from enthusiasm.

Do not use it to compare named vendors on price, security and terms, which is `vendor-evaluation`. Do not use it to write the contract, which is `business-agreements-drafting`. Do not use it for the one-off question of approving one tool for one team, which is a `decision-memo` and should take an afternoon rather than a quarter. Do not use it to document the new process once a pilot succeeds; that is `process-documentation-sop`, and skipping it is how a successful pilot dies with the person who ran it.

Where the real question is which tasks a single team should try this month, run the audit and the pilot design and stop there. The policy, procurement and fluency steps are for organisation-wide adoption and are overhead at smaller scope. Below about fifty people compress the whole sequence: one audit conversation per function, one pilot rather than three, a half-page policy, and no procurement test where the tool is cheap and cancels monthly. Above a few thousand the binding constraint moves from choosing to propagating, and the work becomes a `program-management` problem.

## What you need before starting

**Where the time actually goes, by function.** Not the org chart, the recurring work. This is what stops the shortlist being set by whoever is loudest. Missing: run a two-week time audit across the four or five functions that matter most, or interview two people per function for forty minutes and reconstruct the tasks from calendars and the shared drive. Do not proceed on assumption; the tasks people say consume their time and the tasks that do are reliably different.

**A named executive owner with budget authority.** Cross-functional work without a single owner defaults to nobody. Missing: say so as the first finding and stop.

**The current state of usage, including the unofficial part.** What people already do, on what accounts, with what data. Missing: ask in a way that does not punish the answer. An anonymous three-question survey gets a truer picture than a manager asking their own team, and a finding that forty percent already use a personal account is what sets the policy deadline.

**The data classification already in use.** Public, internal, confidential, personal, regulated, or the local equivalent. The policy has to attach to categories that already exist or nobody applies it. Missing: write a four-category version and get it agreed as part of this work, flagging that you created a classification rather than found one.

**The regulatory and contractual constraints.** Customer contracts restricting subprocessors, sector rules, data residency commitments, and any clause requiring notification before new processing. Missing: ask legal for the three largest customer agreements and read the data processing terms. Adoption plans that ignore a contractual constraint get reversed publicly, which costs more than the delay would have.

**A baseline for anything you intend to claim improved.** Cycle time, error rate, volume, cost per unit. Missing: measure it for two to four weeks before the pilot starts. This is the most skipped step and the reason most programmes cannot answer the only question finance will ask.

**The stopping budget.** How much time and money will be spent before a result is expected. Missing: propose a figure as a fraction of one function's quarterly cost and get it confirmed. A programme with no stopping budget runs until it is embarrassing.

## The method

1. **Audit the work before looking at a single vendor.** For each function, list the recurring tasks with four attributes: rough hours per month across the team, how structured the task is, how much judgement it needs, and the cost of an undetected error. The rule for what counts as a task: it has a recognisable start, a recognisable output, and someone who could say whether it was done well. Name no output and you have named a responsibility, which cannot be piloted.

2. **Classify each task into one of four buckets.** Automate: frequent, structured, low consequence when wrong, currently done by expensive people. Assist: high volume but carrying judgement, so the output is a draft a person owns. Leave alone: an undetected error is expensive, the judgement is the job, or someone is accountable to a regulator or customer. Fix first: slow for a reason a tool cannot touch. The rule for that last bucket is the most valuable here. Before shortlisting anything, name the binding constraint on the process. Where a proposal sits four days in an approval queue and two hours in drafting, faster drafting saves two hours and the tool gets blamed for a queue it never touched.

3. **Shortlist two or three pilots, not ten.** Score on four criteria: hours per month at stake, whether a baseline exists or can be measured in under a month, whether the owning team wants this, and whether a visible outcome is reachable inside a quarter. Willingness is not a soft criterion; a pilot run by a reluctant team measures reluctance. On a tie, take the one whose result is legible outside the function, because the next round of funding depends on an outsider being able to describe what happened.

4. **Design each pilot so it can fail cleanly.** Each needs a named owner who does the work rather than supervises it, a scope stated as task instances rather than an area, a baseline measured before anything changes, a threshold agreed before the start, an end date, and a decision rule at that date: continue, change, or stop. The threshold must be a number with a comparison. "Faster" is not a threshold; "median time from request to first draft below four hours, against a baseline of eleven, across at least forty instances" is. Where no threshold can be written, the task has no measurable output and belongs back in step one.

5. **Write the usage policy before the tools arrive.** One page. Which data categories may go into which class of tool, with the confidential and personal categories named explicitly. The approved tools and the route to request another, which must take days rather than months or it will be bypassed. What must always carry a human decision, as concrete cases rather than principles: anything creating a legal or financial commitment, anything affecting a person's employment or pay, anything issued externally in the organisation's name, anything whose error would reach a customer unchecked. What is disclosed and to whom. Retention, and whether the vendor trains on inputs, which is a contractual fact with a real answer. And that accountability for the output stays with the person who used it. The rule on length: a policy running past one page is not read before someone drafts an email, and the shadow usage continues.

6. **Test vendors on the work, not on the demonstration.** Assemble twenty to fifty real task instances with known good answers from completed work, and run each candidate against them blind. Count errors by type rather than recording impressions. Define what counts as an error before the test, in the receiving function's terms, and have one person grade every tool. Where two tools land within a few points, decide on contract terms and exit cost, because the difference sits inside the noise of a fifty-item test. Insist that any vendor demonstration runs against three of the organisation's own task instances, chosen by the organisation, in the meeting.

7. **Check the overlap before signing anything.** List the platforms already licensed and what each has shipped in the last two release cycles. In most organisations at least one shortlisted capability is already owned and unconfigured. The rule: the existing platform's version wins unless its tested error rate is materially worse, because the integration, security review and procurement cycle are already paid for.

8. **Build fluency with the organisation's own material.** Run short sessions on the tasks the attending team actually does, using their own documents and quality standard, because generic training produces capability nobody uses. Name one interested person per function and give them protected time rather than a title. Keep a shared library of instructions that produced good output, tagged with the task, so a discovery made once reaches everyone within the week.

9. **Measure the same thing you measured at baseline.** Time on task, error rate, throughput, and whether the person doing the work wants to keep the tool. That last is not sentiment: a tool people quietly stop using has an adoption rate of zero whatever the time study said. Measure adoption as weekly active use on a named workflow with the denominator stated. Seats assigned is a purchase, not a result.

10. **Report quarterly, with the failures first.** What was piloted, what the measurement showed, what was stopped and why, what is being scaled, what it cost, and where the risk position sits. The rule that makes this credible: report at least one thing that did not work, in the same detail as the things that did. A programme that only reports wins is not believed at the second budget request, and the second request is always larger.

## The risk position, stated at any time

Separately from the pilots, the programme owner should be able to answer five questions on any day without preparation, and being unable to answer one is itself the finding.

Which tools are approved, and for which data category each. What is actually flowing into each of them, established by asking the functions rather than by reading the policy. What the current estimate of unapproved usage is, and when it was last measured. What contractual or regulatory exposure the position carries, named by customer or regime rather than in general. And what happens when an output causes harm: who reports it, to whom, and how it reaches the person accountable.

Keep the answers on one page beside the policy and refresh them quarterly. This page, not the pilot results, is what a customer's security questionnaire and a board's risk committee will ask for, and reconstructing it under deadline is where the unpleasant discoveries happen.

## Worked example

**Situation.** A three-hundred-person specialist insurance broker with four functions: underwriting support, claims, client servicing and finance. The board had twice asked what the AI strategy was and twice received a slide listing four tools bought the previous year at a combined 118,000 a year. Vendor consoles showed 214 licences issued and 31 accounts active in the last thirty days. An anonymous survey of 180 staff found 44 percent had used a consumer AI tool for work that month, 12 percent by pasting client documents into one.

**Task.** Produce, within six weeks, a programme the board could fund or refuse: what to do, in what order, at what cost, with a stated basis for judging it a year later. Good meant the finance director, sceptical since the previous purchase, would agree the measurement was fair.

**Action.** The audit ran three weeks and produced 61 recurring tasks with rough monthly hours. Four dominated: renewal submission packs at about 340 hours a month, claims first-response drafting at 290, broker statement reconciliation at 210, client report assembly at 180.

The first shortlist put all four into pilots. That was the wrong turn, abandoned in week three once the claims constraint was examined. First-response drafting looked ideal: high volume, structured, expensive people. But measured cycle time from notification to first response was 2.9 days, of which drafting was about 25 minutes; the rest was waiting for a loss adjuster allocation. A drafting tool would have moved 2.9 days to 2.87, and the claims team, who had asked for it, would have concluded correctly that it changed nothing. Claims moved to fix first, with the allocation queue named as the real problem.

Reconciliation went to leave alone: high error consequence, errors undetected until quarterly close, and a finance director personally accountable for the figures. The right answer was a rule in the policy, not a pilot.

That left two pilots. Renewal packs, owned by an underwriting support team leader: baseline 4.6 hours median per pack over 52 packs in the four weeks before the start, threshold 2.8 across at least 40 packs, eleven-week end date. Client report assembly, owned by a client servicing associate: baseline 3.1 hours, threshold 2.0.

Procurement tested three vendors against 40 real renewal packs, with the completed versions as the answer key, graded by one senior underwriter who defined three error classes before the test: a missing required section, a wrong figure, and a format failure needing a rewrite. Vendor A produced 4 factual errors across 40, B produced 3, C produced 11. A and B sat inside the noise of a 40-item test, so the decision moved to terms: B cancelled monthly and would not train on inputs, A wanted two years. B won on reversibility, not score. The overlap check also found the firm's existing document platform had shipped a summarisation feature nine months earlier, covering about a third of the client report use at no extra cost; that was configured for the second pilot instead of buying a third tool.

**Result.** The renewal pack pilot finished at a median of 2.6 hours across 47 packs against a threshold of 2.8, and scaled to the whole function the following quarter. The client report pilot finished at 2.7 against a threshold of 2.0 and was stopped, for a reason that mattered more than the number: reports varied more between clients than the pilot assumed, and the assembly time saved was consumed by checking. Stopping it, and reporting it in the same detail as the success, was what the finance director later said changed her view of the programme.

Twelve months on the firm spent about 41,000 a year against 118,000, on two tools rather than four, with weekly active use on the renewal workflow at 78 percent of the function. Consumer tool usage in the repeat survey fell to 9 percent, which the programme owner attributed to the three-day request route rather than to the policy language. The honest uncertainty: the 340 hour baseline was reconstructed partly from calendars and is accurate to perhaps 15 percent. The saving is real; its size is less precise than the report implied.

### A second scenario, where it goes differently

A forty-person clinical services company, where the method takes a different shape. There are three teams and a founder, and the audit is two conversations over a day. There is no procurement test, because the two candidates cost under 200 a month each and cancel monthly, so a fifty-item blind test costs more in senior time than a year of the wrong choice.

What expands is the policy and the leave alone bucket, because most recurring work touches patient-adjacent records. The constraint is regulatory rather than operational: the highest-hours tasks are precisely the ineligible ones, and the honest audit finding is that two of eleven recurring tasks qualify. The programme becomes one pilot on internal document drafting, a policy that is mostly prohibitions, and a data processing review that takes longer than the pilot.

What changed: reversibility is cheap and regulation is binding, so effort moves from choosing well to bounding risk. The measurement discipline does not change. The baseline is still taken before the pilot starts, because a forty-person company that cannot say whether a tool helped is in the same position as a three-hundred-person one.

## Output

Four artefacts. The audit and the pilot designs are the working documents; the policy and the quarterly report are what circulate.

**Capability audit.**

| Function | Task | Hours/month | Structure | Judgement | Error consequence | Binding constraint | Bucket |
| Underwriting support | Renewal pack | 340 | High | Low | Medium, caught at review | Drafting time | Automate |
| Claims | First response draft | 290 | High | Low | Low | Adjuster allocation queue | Fix first |
| Finance | Statement reconciliation | 210 | High | Medium | High, undetected to close | None | Leave alone |

**Pilot design, one per pilot.**

```
PILOT: [name]
Owner:            [one name, does the work]
Scope:            [task instances included, and what is excluded]
Baseline:         [metric, value, sample size, dates measured]
Threshold:        [metric, target value, minimum sample]
Start / end:      [dates]
Decision at end:  continue / change / stop, decided by [name]
Cost to run:      [licence, time, integration]
Cost to stop:     [notice period, data extraction, retraining]
Risk notes:       [data categories touched, policy cases engaged]
```

**Usage policy, one page.**

```
APPROVED TOOLS          [names, and the data class each is approved for]
REQUEST ROUTE           [who, how, how long it takes]
DATA CATEGORIES         [public / internal / confidential / personal, each
                         with the tools it may be used in]
ALWAYS A HUMAN DECISION [concrete cases, one line each]
DISCLOSURE              [what is disclosed, to whom, in what words]
RETENTION AND TRAINING  [per approved tool, as stated in the contract]
IF THE OUTPUT IS WRONG  [accountability sits with the user; how to report]
Owner: [name]   Version: [n]   Reviewed: [date]
```

**Quarterly report.**

| Pilot | Baseline | Threshold | Result | Decision | Cost to date | Next |

Then three short sections: what was stopped and why, the risk position including measured shadow usage, and adoption by named workflow with its denominator.

## Failure modes

**The tool bought for a queue.** Recognise it when cycle time barely moves although task time halves: a large improvement in the wrong denominator. Fix it in step two by naming the binding constraint before shortlisting, and be willing to report that the highest-hours task is not eligible.

**No baseline, so the result is a feeling.** Recognise it when the report says the team finds it much faster and carries no number with a date on it. There is no fix after the fact, because a baseline cannot be reconstructed once the process has changed. The only remedy is to insist on the measurement window before the licence is issued, which is why step four sits before procurement.

**The pilot with no stop condition.** Recognise it when the end date passes and the pilot continues, usually because stopping would embarrass whoever proposed it. Fix by writing the threshold and decision rule before the start, with a decider who is not the pilot owner.

**The policy written after the tools arrive.** Recognise it when the first version has to grandfather existing usage, at which point it can no longer prohibit anything people already do. Where this has happened, write it anyway with a stated transition date rather than a grandfather clause.

**The enthusiast mistaken for an authority.** Recognise it when the shortlist matches one person's tool preferences and the audit was done after the choice. This is a sequencing problem, not a character one. Fix by running the audit before the vendor conversations and having the blind test graded by someone from the receiving function.

**Success reported without the failures.** Recognise it when three quarterly reports contain no stopped pilot. Either nothing ambitious was attempted or failures are being absorbed quietly, and both are visible to a board that has seen other programmes.

## Edge cases

**Usage is already widespread and unofficial.** Do not open with prohibition. Open with the request route and two approved tools, so there is somewhere legitimate to go, then set a transition date after which the unofficial route becomes a policy matter. Prohibition with no sanctioned alternative moves usage further out of sight.

**A large customer's contract restricts new subprocessors.** Check before the pilot, not before the rollout. Where notification or consent is required, the pilot scope excludes that customer's data entirely and the contractual change becomes a separate workstream, usually measured in months.

**The tool works and the team will not use it.** Treat this as a finding about the task, not the people. The usual cause is that the output needs more checking than it saves, meaning the error rate sits above the point where review is cheaper than drafting. Measure the checking time; where it exceeds the saving, stop the pilot and say why.

**A pilot succeeds and its owner leaves.** The most common way a scaled success quietly reverts. The remedy is `process-documentation-sop` written during the pilot rather than after it.

## Quality bar

- The audit shows where hours actually go, by function and by task, and predates any vendor conversation.
- Every shortlisted task has its binding constraint named, and any task whose constraint a tool cannot touch has been moved out of the shortlist.
- Every pilot has a baseline measured before the start, with its sample size and dates, and a numeric threshold agreed in advance.
- Every pilot has an end date and a named decider who is not the pilot owner.
- The policy is one page, names the data categories in use, and lists concrete cases requiring a human decision rather than principles.
- Contract review covers training on inputs, retention, processing location, exit cost and renewal price, for every approved tool.
- Adoption is reported as active use on a named workflow with the denominator stated, never as licences issued.
- At least one failure appears in each quarterly report, in the same detail as the successes.

## Related skills

`vendor-evaluation` runs the head-to-head comparison the procurement step feeds, and produces the recommendation. `decision-memo` is the format for the go or no-go on a single tool, and supplies the reversibility judgement that sizes the procurement effort. `process-documentation-sop` records the changed process once a pilot succeeds, which is what makes the gain survive a departure. `program-management` runs delivery when adoption spans more than three functions or two quarters. `okr-planning` places the adoption targets alongside the rest of the operating plan. `board-and-investor-management` and `investor-update` carry the quarterly report outward. `business-agreements-drafting` writes the contract this skill specifies. `structured-problem-solving` takes over when the audit shows the real problem is a process rather than a capability.
