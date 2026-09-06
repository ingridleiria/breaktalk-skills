---
name: identification-defense
description: Attacks an empirical design the way a demanding referee or committee member will, grades every answer as strong, adequate, weak or missing, and then builds the argument, the diagnostic exhibit or the honest concession that answers each attack. Covers difference-in-differences and event studies, instrumental variables, regression discontinuity, matching and selection on observables, synthetic control, and the cross-cutting questions about clustering, attrition, measurement and power that apply to every design. Produces a defense table mapping each objection to its response and the exhibit that carries it, a verdict on whether the design survives at the venue targeted, and short spoken answers for a seminar or viva. Use this skill when someone asks whether their design is identified, asks to defend a difference-in-differences or an instrument, wonders what a committee will ask about identification, is preparing for a defense, seminar or submission, or is choosing between designs. Trigger also on vague requests such as "attack my design", "will reviewers buy this", "is parallel trends going to be a problem", "my instrument feels weak", or "poke holes in this before I send it".
---

# Identification Defense

A design is credible when its author has already asked every question the referee will ask and holds either a written answer or an honest concession for each. The failure this prevents is the opposite: a design defended by vocabulary. The paper says it uses a difference-in-differences strategy with two-way fixed effects, reports a pre-trend test, cites three method papers, and never establishes why the treated and comparison units would have moved together absent treatment in this particular setting. Naming an estimator is not defending an assumption, and experienced readers can tell the difference in about ninety seconds.

The cost lands in one of three places, and all three are worse than doing the work early. At a journal, it is a referee report saying the identification is not convincing, which is close to unanswerable because there is no specific claim to rebut and the revision required is a new design or a new set of exhibits, one cycle later. At a viva or a job seminar, it is a question the author cannot answer aloud, in a room, with their examiners watching them realise it for the first time. In the worst case it lands after publication, when somebody re-estimates with a different comparison group and gets a different sign.

There is a fourth outcome this skill has to be willing to produce: the finding that the design does not identify the effect the paper claims. Delivering that early is the most valuable thing the skill does, and decorating a broken design is the one thing it must never do.

## When to use this, and when not to

Use it before anything goes out: before a supervisor sees a chapter, before a seminar, before submission, before a resubmission where identification was raised, and before a viva. Use it while a design is still being chosen, where it is cheapest, because an objection that is fatal after the data is built is often avoidable when it is raised during design. Use it when reading somebody else's paper as a referee or discussant, where it is the same method pointed outwards.

The boundary with the two adjacent skills matters and is often got wrong.

`econometrician` decides the estimator and the inference: which estimator, what to cluster on, whether to weight, which diagnostics carry a consequence. Those are questions about whether the estimation is correct given the design.

`econometric-model-writer` writes the empirical strategy section that reports those decisions and carries the surviving threats into prose. It is where the output of this skill is published.

This skill asks whether the design is believable at all. It runs the attack, grades it, and builds the response. It does not choose the estimator and it does not write the section, though its output is the raw material for both.

Do not use it to choose a research question, which is `research-question-ideation`, or to construct a design from scratch, which is `research-design`. Do not use it to check whether the numbers in the paper are right, which is `analysis-audit`; a perfectly executed analysis of an unidentified design is still unidentified, and the two failures are found by different methods. Do not use it to predict referee reactions to the contribution, framing or literature, which is `peer-review-simulator`.

## What you need before starting

**The design, in five lines.** The outcome, the treatment and how it is assigned, the source of variation, the comparison group, and the estimand. Missing: stop and go to `research-design`. If these five cannot be stated, there is nothing to attack yet, and attacking a design that does not exist produces a list of generic worries.

**The institutional detail of how treatment was assigned.** Not the statistical description, the actual mechanism: who decided, on what criteria, in what order, with what discretion, and what was announced when. Missing: this is the single most important gap and it cannot be filled by assumption. Go and read the implementing documents, the legislation, the programme manual, or interview somebody who ran it. Most identification arguments are won or lost on a fact about assignment that is written down somewhere and nobody has looked.

**The estimates as they currently stand, with their standard errors.** Missing: the attack can still be run on the design, but the questions about power, sensitivity and magnitude cannot be graded. Run it anyway and mark those rows as pending.

**The diagnostics already run, and their results including the unflattering ones.** Missing: assume none exist. Do not credit a diagnostic that was run and not shown, because the reason it was not shown is usually the answer.

**The venue and the audience.** A general-interest journal, a field journal, a thesis committee, a policy audience. This sets the bar, and the same design can be defensible at one and not at another. Missing: assume a good field journal, which is the most common target and a demanding-but-fair standard, and say you have.

**The alternative designs the data could support.** Missing: generate two, briefly. This matters because the verdict may be that the current design fails and a weaker but honest one succeeds, and having the alternative in hand is what makes that finding usable rather than merely discouraging.

**The time available before the deadline.** Missing: ask. A defense plan that needs three weeks of new exhibits, delivered four days before submission, is not a plan.

## The method

1. **Restate the design in five lines and get agreement on them.** Outcome, treatment and assignment, source of variation, comparison group, estimand. Write them down. Half the disagreements that follow turn out to be disagreements about one of these five, and finding that out now is faster than arguing about parallel trends for an hour and discovering you meant different comparison groups.

2. **Establish the assignment mechanism as a matter of fact.** Write one paragraph on how units actually came to be treated, sourced from documents rather than from the paper's own description. This paragraph generates most of the specific attacks and most of the specific defences. The rule: if the paragraph contains the phrase "was rolled out gradually" and nothing about who chose the order, it is not finished.

3. **Run the attack.** Ask every question in the relevant section below plus every cross-cutting question, in the voice of a demanding but fair referee. Do not answer them as you go; write the current answer as it exists in the paper today, even where that answer is nothing. Answering while attacking produces charitable questions.

4. **Grade each answer.** Four grades, and the definitions are what keep the exercise honest:

   **Strong.** The answer rests on a fact about this setting plus evidence in an exhibit, and a referee who disagrees would need a new argument rather than a new question.

   **Adequate.** The answer is a reasonable argument with supporting evidence, and a determined referee could still press it. Most good papers have several of these and that is normal.

   **Weak.** The answer is an assertion, a citation to a paper that did something similar, or a diagnostic that does not actually test the assumption in question. A flat pre-trend estimated with standard errors wide enough to contain the treatment effect grades weak, not strong, however it looks in the figure.

   **Missing.** No answer exists.

   The grade goes on the answer, never on the design as a whole, and it is recorded before any repair work starts, because that record is what shows a supervisor or a coauthor where the effort should go.

5. **Triage by consequence, not by ease.** Rank the weak and missing rows by what happens if the objection is correct: does the sign change, the magnitude change, the interpretation change, or only the precision. Fix in that order. The common error is to spend a week on the easy robustness check while leaving the one objection that would reverse the sign unaddressed, because the easy one produces an exhibit and the hard one produces an argument.

6. **Build a response for every weak or missing row.** Exactly three permitted forms, and choosing among them is the central judgement in this skill:

   **A diagnostic or robustness exhibit** when the objection makes a testable prediction. Specify it precisely: which test, on which sample, with which comparison, appearing as which table or figure. "Run some robustness checks" is not a response.

   **An argument** when the objection is about a mechanism rather than a pattern, written as a paragraph the paper can carry, resting on a fact about the setting. Exclusion restrictions are almost always defended this way, because there is no test for them.

   **A concession** when neither is available, written in plain words for the limitations section, with the direction of the likely bias stated and, where possible, a bound on its size. A concession with a direction is a defensible position; a concession without one is an admission.

   The rule for choosing: if the objection implies something observable in this data, it gets an exhibit. If it implies something about the world that the data cannot see, it gets an argument. If the argument would not persuade you as a referee, it gets a concession.

7. **Check that the exhibits you are proposing can actually distinguish anything.** Before committing to a diagnostic, ask what it would look like if the assumption were violated to a degree that matters. A test that returns the same picture under the null and under a violation large enough to reverse the result is not evidence, and running it makes the paper look more defended than it is. Where the honest answer is that the test has no power, say so and use a sensitivity or bounding approach instead.

8. **Write the verdict.** Whether the design is defensible at the stated venue as it stands, what must be added before it is, and how long that will take. Where the honest verdict is that the design does not identify the claimed effect, say so plainly and propose the nearest question the data can answer credibly, which is usually narrower, more local, or descriptive.

9. **Prepare the spoken answers where the purpose is a seminar or a viva.** For each of the top six objections, three sentences: the concession first, the argument second, the exhibit to point to third. Concession first is the counterintuitive part and it is what works, because an examiner who has to extract a limitation becomes an adversary, while one who hears it stated first becomes an interlocutor. Practise them aloud; an answer that reads well and cannot be said in twenty seconds is not ready.

## The attack, by design

Ask every question that applies. The point of a fixed list is that it does not soften in the presence of a result you like.

**Difference-in-differences and event studies**

- Why would treated and comparison units have moved in parallel absent treatment, in this specific setting, given what step 2 established about who chose the treatment order?
- What could make them diverge: differential shocks, policy bundling, mean reversion after a bad year, selection into treatment timing, differential composition changes?
- Do pre-period coefficients show no trend, and is the pre-period test powered enough for flatness to mean anything? What effect size could the pre-period rule out?
- With staggered adoption, is a two-way fixed effects estimator used, and if so why is negative weighting under heterogeneous effects not a concern here? Which modern estimator is reported and does it agree? If they disagree, which is believed and why?
- Is the comparison group never-treated or not-yet-treated, and does the choice move the estimate? Never-treated units may be never-treated for a reason.
- Is there anticipation, and would it show up as a pre-trend or be absorbed by the reference period choice?
- Are there spillovers from treated to comparison units, which biases in a known direction and is usually ignored?
- Does the composition of the sample change around treatment: entry, exit, attrition, reclassification?
- How sensitive is the conclusion to plausible violations of parallel trends, under a formal bounding approach rather than an assertion?

**Instrumental variables**

- What is the argument that the instrument affects the outcome only through the treatment, stated for this setting and not by analogy to another paper?
- Which alternative channels exist, and how is each closed: by a control, by a subsample, by an institutional fact, or not at all?
- How strong is the first stage, by a statistic appropriate to the case rather than a rule of thumb, and what is reported when the instrument is weak?
- Is monotonicity plausible, meaning are there units the instrument pushes the other way?
- Who are the compliers, what share of the sample are they, and does the local effect for that group answer the paper's question or a narrower one?
- Is the instrument as good as randomly assigned conditional on the controls, and what balance evidence supports that?
- Does the reduced form look like the story? A significant second stage with an unconvincing reduced form is a warning.

**Regression discontinuity**

- Can the running variable be manipulated near the cutoff, given who computes it and who knows the rule? What does the density test show, and is it powered?
- Are covariates continuous at the cutoff, tested at the bandwidth used?
- How sensitive is the estimate to bandwidth, kernel and polynomial order, and does the sign survive the range a referee would try?
- Are there other policies that change at the same cutoff? This is the objection that kills more regression discontinuity papers than manipulation.
- Is the effect local to the cutoff, and does the paper claim more than that anywhere, including in the abstract?
- For a fuzzy design, is the first stage at the cutoff strong, and is the exclusion restriction defended separately?

**Matching, reweighting and selection on observables**

- Why is selection on observables plausible here, given that treated units chose treatment? What is the story under which the observed covariates capture the selection?
- Which unobservable would a referee name first, and what bounds its influence: a sensitivity analysis, a coefficient stability argument with a stated assumption about the ratio of selection on unobservables to observables, or nothing?
- Is there common support, how many observations are off it, and what happens to the estimate when they are dropped?
- Does the covariate set include anything measured after treatment?

**Synthetic control and related methods**

- Is the donor pool clean of treated, contaminated or spillover-affected units?
- How good is the pre-treatment fit, and is it good on the outcome rather than only on the predictors?
- What do placebo-in-space and placebo-in-time inferences look like, and where does the treated unit rank?
- Would the result survive leaving out the one or two donors with the largest weights?

**Cross-cutting, every design**

- Is the clustering level the level at which treatment is assigned, and are there enough clusters for the inference to be reliable?
- Is the outcome measured the same way in treated and comparison units, and the same way before and after? A measurement change that coincides with treatment is a confounder with a nearly perfect disguise.
- Is the sample selected in a way related to treatment: attrition, endogenous entry, survivorship, a filter applied after treatment?
- What is the minimum detectable effect, and can the design distinguish the estimated effect from zero and from an economically meaningful alternative?
- Is the effect size plausible against what is known about this outcome? An estimate three times any prior effect in the literature is a finding about the design more often than about the world.
- How many specifications were run before this one, and was the analysis plan fixed in advance?

## Worked example

**Situation.** Tomas Reiner had a job market paper estimating the effect of a regional apprenticeship subsidy on youth employment, using staggered adoption across 214 districts between 2013 and 2019, with a two-way fixed effects estimator producing 1.8 percentage points and a standard error of 0.6. He had a department seminar in three weeks and a submission planned for six weeks after that. His supervisor's comment on the draft was that the identification section was fine, which he correctly did not find reassuring.

**Task.** Find every objection before the seminar room did, and arrive with either an answer or a stated concession for each. Good meant no question in the seminar that he had not already written down.

**Action.** Step 2 took a day and a half and changed the paper. The subsidy's rollout order had not been random or administrative: districts applied for the scheme, and applications were approved in the order received, subject to a regional quota. That single fact, found in an annex to the programme regulations, reframed the entire attack. Districts that applied early were districts whose labour offices were active, and active labour offices plausibly do other things that affect youth employment.

The attack produced nineteen questions across the difference-in-differences and cross-cutting lists. Twelve graded strong or adequate. Seven did not, and the triage in step 5 put them in this order: selection into treatment timing through the application process, which could change the sign; negative weighting under staggered adoption with heterogeneous effects, which could change the magnitude; a concurrent training programme that overlapped in 2016 in two regions; measurement of youth employment changing when the registry was updated in 2015; spillovers to neighbouring districts; clustering at district level with treatment assigned at district level but the quota operating regionally; and the pre-period power question.

The wrong turn consumed four days. Tomas built an elaborate pre-trend exhibit: eight pre-periods, joint test, a p-value of 0.62, and a figure that looked flat and reassuring. He was going to lead the seminar with it. Step 7 killed it. The pre-period coefficients had standard errors of about 0.9 percentage points each, so the pre-period could not rule out a pre-existing differential trend that would generate the entire 1.8 point estimate over the post window. The test had almost no power against the violation that mattered. Presenting it as evidence would have been the strongest possible signal to a well-informed room that he had not thought about it, and the first question would have been what effect size the pre-test could exclude.

What replaced it was less comfortable and much stronger. He kept the event-study figure, stated in the caption what magnitude of pre-trend the pre-period could and could not rule out, and added a formal sensitivity analysis reporting how large a violation of parallel trends the result could withstand before losing significance. The answer was that it survived a violation up to roughly sixty percent of the maximum pre-period deviation, which he could state in one sentence and defend.

The application mechanism got an argument plus an exhibit. The argument was that approval order was determined by the receipt date within a regional quota, so conditional on region and application year, the timing of approval was administrative rather than chosen. The exhibit was a restricted estimate using only applicant districts, comparing earlier-approved to later-approved within region, which is a much cleaner comparison and returned 1.5 with a standard error of 0.7. That became the headline specification, and the full-sample estimate moved to a robustness table.

The staggered adoption question was not his to settle in a defense document, so it went to the project's econometrician; the decision that came back was a not-yet-treated comparison under a modern estimator, which returned 1.6 with a standard error of 0.8. The 2016 overlap became a dropped-region robustness column. The registry change became a stated concession with a direction: the update improved coverage of short spells, which would inflate measured employment in all districts after 2015 and therefore be absorbed by year effects unless it interacted with treatment, and he stated that he could not rule that out. Spillovers became a concession with a direction and a bounding exercise using distance to the nearest treated district. Clustering moved from district to region, which cut the number of clusters to 17 and required a small-cluster correction, and the standard error rose from 0.7 to 1.1, which he reported rather than hid.

**Result.** The defense table had nineteen rows: eleven strong, five adequate, three concessions with stated directions, nothing missing. Preparation took eleven working days, four of which were the abandoned pre-trend exhibit.

In the seminar he was asked six identification questions. Five were on the table. The sixth was not: a visiting economist asked whether districts that applied and were rejected could be used as a comparison group. They could, there were 38 of them, and the estimate on that comparison was 1.4 with a standard error of 0.9. It became a new column and, at the referee stage, the exhibit one report singled out as convincing.

The headline estimate fell from 1.8 to 1.5 and the standard error rose. The paper was substantially stronger, which is the usual shape of this exercise and worth saying out loud to anyone running it for the first time.

### A second scenario, where it goes differently

The same method applied to a regression discontinuity design, where the verdict came out the other way.

The paper estimated the effect of a means-tested university grant on completion, using an income cutoff. Step 2 established that the income figure used for eligibility was self-reported on the application form, reviewed by the awarding office, and that applicants received written guidance about the threshold before submitting. That is a manipulation story with a mechanism, not a hypothetical one. The density test showed excess mass just below the cutoff, and covariate balance failed on two of six covariates at the chosen bandwidth.

There was no exhibit that could rescue this, because the objection was not about a pattern that might or might not be present; the pattern was present and the mechanism for it was documented. The temptation was to narrow the bandwidth until the density test passed, and that was refused: a test that passes only in the window where it has least power is not evidence, and choosing the window by the test result is the specification search the whole exercise exists to prevent.

The verdict was that the design does not identify the effect of the grant on completion. What it can identify is stated narrowly: among applicants whose reported income was verified against tax records, a subgroup of about 31 percent of the sample where manipulation is not possible, the discontinuity is estimable and the density test passes. The estimand becomes a local effect for verified applicants near the cutoff, which is a narrower claim and a defensible one. The paper's title, abstract and policy section all changed.

What differs between the two scenarios is the outcome of step 8. In the first, the design survived attack with repairs and a lower headline number. In the second, it did not survive, and the useful deliverable was the nearest question the data could answer rather than a longer list of robustness checks. A skill that can only produce the first outcome is not a defense, it is decoration.

## Output

**The defense table**, the primary deliverable:

| # | Objection, stated as a referee would | Current answer | Grade | Response type | Response, specified | Exhibit | Owner and date |
| 1 | Districts self-selected into treatment timing by applying | none | Missing | Exhibit and argument | Restrict to applicants; compare earlier to later approval within region | Tab 3 col 2 | TR, 14 Mar |
| 2 | Two-way fixed effects with staggered adoption and heterogeneous effects | TWFE only | Weak | Estimator decision | Refer to econometrician; not-yet-treated comparison | Tab 3 col 4 | pending |
| 3 | Registry definition change in 2015 | none | Missing | Concession | Absorbed by year effects unless interacted with treatment; direction stated | Limitations | TR, 16 Mar |

Grade is strong, adequate, weak or missing. Response type is exhibit, argument, or concession. Every weak or missing row must reach a response before submission, and a response of concession is a completed row, not an unfinished one.

**The verdict**, four short paragraphs:

```
VERDICT
Venue assumed:      [journal, committee, or seminar]
Design as it stands: [defensible / defensible with the additions below /
                      not defensible for the claimed effect]
Required before submission: [numbered list, each with an estimate of days]
If not defensible:  [the nearest question the data can answer, stated as a
                     design in five lines, with what changes in the paper]
```

**The spoken answers**, for a seminar or viva, six at most:

```
Q: Why should I believe parallel trends when districts applied for the scheme?
A: [concession] The application is a choice, so timing is not random.
   [argument]   Conditional on region and application year, approval order was
                by receipt date under a quota, so it is administrative.
   [exhibit]    Table 3 column 2 restricts to applicants and compares earlier
                to later approvals within region: 1.5, standard error 0.7.
```

## Failure modes

**Vocabulary as evidence.** Naming the estimator, citing the method paper, and treating that as the defence. Recognisable because the identification paragraph would be unchanged if the setting were different. Fix by requiring every answer to rest on a fact about this setting.

**The powerless diagnostic presented as reassurance.** A flat pre-trend with standard errors wide enough to hide the effect, a density test on 200 observations, a balance table where nothing is significant because the sample is small. Recognisable by asking what the test would show if the assumption failed by an amount that matters. Fix with a sensitivity or bounding approach, and state what the test could and could not rule out.

**Attacking and answering in the same pass.** Produces gentle questions with ready answers. Fix by writing all questions before any answers, and recording the current answer as it exists rather than the one you would like.

**Triage by ease.** Six new robustness columns and nothing on the objection that could reverse the sign. Recognisable by comparing where the time went to the consequence ranking. Fix by ordering the work by consequence before starting it.

**Robustness as volume.** Twenty specifications, all significant, none addressing the identifying assumption. Referees read this as an attempt to substitute quantity for an argument. Fix by mapping each check to the specific objection it answers and deleting the ones that answer none.

**Bandwidth or specification chosen by the test result.** Narrowing until the density test passes, or picking the controls that make the pre-trend flat. Recognisable because the chosen value is the one where the diagnostic just passes. Fix by fixing the choice by a stated rule before looking, and reporting the full range.

**The concession that has no direction.** "We cannot rule out unobserved heterogeneity." This tells a referee nothing and reads as a formality. Fix by stating which way the bias would run and, where possible, how large it would have to be to overturn the result.

**Defending a design that cannot be defended.** The most damaging failure, because the work of defence makes the paper look more credible than it is and delays the rewrite by months. Recognisable when every response is a concession. Fix by writing the verdict honestly and proposing the narrower question.

**Preparing written answers for a spoken occasion.** A perfectly argued paragraph is useless in a viva. Fix by practising aloud, in three sentences, concession first.

## Edge cases

**No comparison group exists.** A national policy with simultaneous adoption everywhere. Interrupted time series, a synthetic comparison built from other outcomes, or an honest descriptive framing. Say which and do not present a time trend as identification.

**The instrument is weak and there is no other.** Report the weak-instrument-robust confidence set rather than a point estimate with an implausibly wide interval, and be explicit that the design supports a bound rather than a number. Do not add controls until the first-stage statistic crosses a threshold; the threshold is not the point and the controls change the estimand.

**Few clusters.** Under roughly thirty, and certainly under fifteen, the asymptotic justification for cluster-robust inference is thin. Report a wild bootstrap or a randomisation inference procedure, state the number of clusters prominently, and do not let the number appear only in a table note.

**The design is fine and the effect is null.** Attack it exactly as hard, and then attack the power. A null result is only informative if the design could have detected an effect worth detecting; state the minimum detectable effect and compare it to a magnitude that matters.

**The data was collected for another purpose and the design is opportunistic.** Additional obligations: whether the sample frame relates to treatment, whether the outcome was measured consistently across the units being compared, and whether attrition differs. These are the three that opportunistic designs fail on.

**The committee or referee has already raised an objection.** Answer that one first and in its own terms, even where you think it is misdirected, and only then present the wider table. Reframing somebody's objection before answering it reads as evasion.

**The result is a replication or an extension of a well-known design.** Inheriting a published design does not inherit its credibility in a new setting. Run the attack on the setting, particularly the assignment mechanism, which is what usually differs.

**Time has run out before the exhibits can be built.** Convert the unanswered rows to concessions with stated directions and put them in the limitations. A stated limitation costs far less than an unstated one found by a referee.

## Quality bar

- Every objection in the relevant list was asked and its current answer recorded before any repair work started.
- Each answer carries a grade, and no weak or missing row reaches submission without an exhibit, an argument, or a concession with a stated direction.
- Every defence rests on a fact about this setting rather than on the name of an estimator or a citation to a similar paper.
- Every proposed diagnostic was checked for whether it could distinguish the violation that matters, and the ones that could not were replaced by sensitivity or bounding.
- Repair effort was ordered by the consequence of the objection, not by the ease of the check.
- The verdict states plainly whether the design survives at the named venue, and where it does not, the nearest defensible question is written out as a design.
- The top six objections have spoken answers of three sentences, concession first.
- Method citations were verified against live records.

## Related skills

`research-design` builds the design this skill attacks, and is where the work returns when the verdict is that it does not hold. `econometrician` decides the estimator and the inference, and owns any row whose response is an estimation decision rather than a design argument. `econometric-model-writer` writes the empirical strategy section that carries the surviving threats and concessions into the paper. `preregistration-and-analysis-plan` prevents several of these objections by fixing the choices before outcomes are seen. `regression-table-production` and `academic-figures-monochrome` produce the exhibits the responses point to. `peer-review-simulator` predicts objections to the contribution and framing rather than the design, and `refereeing-for-a-journal` is this method turned outwards onto somebody else's paper. `thesis-defense-prep` uses the spoken answers. `analysis-audit` checks whether the numbers are right, which is a different question from whether they identify anything.
