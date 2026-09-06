---
name: econometric-model-writer
description: Writes the empirical strategy or methods section of a paper, chapter or proposal so that a referee can reproduce the specification from the text alone. Produces the design paragraph in words before any symbol, the numbered estimating equation with every term defined, the parameter of interest named and its estimand stated, the identifying assumption written in plain language and made specific to the setting, the credible threats each paired with a response and the exhibit that carries it, the inference and clustering statement, and estimation code that implements exactly the equation as written. Covers OLS, panel fixed effects, difference-in-differences including staggered adoption, event studies, instrumental variables, regression discontinuity, matching and reweighting, and multilevel models. Use this skill whenever someone asks to write the methods, empirical strategy, estimation or identification section, asks what a coefficient identifies, asks for the equation for their design, needs the model section of a proposal, or has been told their methods section is unclear. Trigger also on vague requests such as "write up my specification", "the referee said the method was not clear", or "put this regression into words".
---

# Econometric Model Writer

The empirical strategy section has one reader in mind: the referee deciding whether the coefficient means what the paper says it means. That reader is not hostile, but they are fast, and they are reading to find the sentence that does not hold. Everything else in the section exists to make that sentence easy to find and, ideally, already answered.

The failure this prevents is a methods section that describes a regression instead of an argument. It names an estimator, prints an equation, lists the controls, and never states in words what variation identifies the effect or what would have to be true for the coefficient to be causal. Referees read this as evasion even when it is only carelessness, and their response is the comment every author dreads: the identification strategy is not clearly articulated. That comment is expensive because it is unarguable. There is nothing to rebut, and answering it means rewriting the section anyway, one review cycle later.

The second failure is quieter and worse. The equation printed in the paper and the command that produced the table are not the same model. A fixed effect is in one and not the other, the sample in the code has an extra restriction, the clustering in the note differs from the clustering in the estimation. Nobody notices until a data editor or a coauthor runs the code, and then every number in the paper is in question rather than just one.

## When to use this, and when not to

Use it when a section has to be written that explains how an effect is estimated: the empirical strategy of an article, the methods chapter of a thesis, the analysis section of a grant proposal, the specification paragraph in a referee response, or the equation block in a preregistration.

The boundary with the two adjacent skills is worth stating plainly, because these three are constantly confused and doing them in the wrong order wastes the most time.

`econometrician` decides the estimator and the inference. Which estimator, what to cluster on, fixed against random effects, whether to weight, what functional form, which diagnostics carry a consequence. Those are decisions, and they are made before anything is written.

`econometric-model-writer`, this skill, writes the section that reports those decisions to a reader. It does not make them. When the writing exposes a decision that was never taken, and it often does, the correct action is to go back to `econometrician`, not to make the decision in prose.

`identification-defense` argues for the design when it is under attack. It runs the referee's questions before the referee does, grades each answer, and builds the diagnostics and concessions. The threats paragraph in this section is where the surviving output of that work is reported; the adversarial work itself happens there.

Do not use this skill to choose a research design, which is `research-design`. Do not use it to build the tables that report the estimates, which is `regression-table-production`, or to interpret the magnitudes, which is `results-writing`.

## What you need before starting

**The design, stated as a source of variation.** What varies, across which units, over what time, and why that variation is informative about the effect. Missing: stop and go to `research-design`. A methods section written before the design is settled becomes a description of a regression, which is exactly the failure above.

**The estimator and the inference decision, with their reasons.** Which estimator, the clustering level and why, the weighting decision, any small-cluster correction. Missing: go to `econometrician`. Do not infer the reason from the command that was run; the reason is what the section has to carry, and reconstructing it after the fact produces a justification rather than a rationale.

**The estimand.** An average treatment effect on the treated, a local average treatment effect for compliers, an effect local to a cutoff, a within-unit effect under a specific weighting. Missing: this is the single most common gap, and it cannot be filled by assumption. Name the candidate estimands the design could deliver and ask which the paper claims.

**The data structure.** Unit of observation, panel or cross-section, the time dimension, the number of units and the number of clusters, whether the panel is balanced. Missing: write the section with explicit placeholders for the counts and mark them, rather than writing round numbers that will be forgotten.

**The variable definitions as they are constructed in the code.** Not as the author remembers them. Missing: read the construction script. The definition in the section must match the definition in the file, and where they differ the file is right.

**The exhibits that already exist or are planned.** Table and figure numbers for the first stage, the event study, the balance table, the density test. Missing: write the threats with the exhibit named as forthcoming and keep a list, because a threat with no exhibit is a limitation and needs relabelling as one.

**The target venue's conventions.** Section length, whether equations are numbered, whether stars are used, whether an appendix carries the derivations. Missing: use the general economics convention described here and say you have assumed it. `journal-targeting` resolves this properly.

## The method

Write in this order. The order matters more than it looks, because writing the equation first causes the words to be reverse-engineered from the notation, and the words are the part the referee reads.

1. **Write the design in one paragraph, in words, with no symbols in it.** What varies, across which units, over what period, and why that variation is plausibly unrelated to whatever else drives the outcome. A reader should be able to state the strategy back after this paragraph and before seeing an equation. The test: delete every equation from the section and see whether the strategy is still comprehensible. If it is not, this paragraph has not been written yet.

2. **State the estimand in one sentence, immediately after.** Not the estimator, the quantity. "The parameter we estimate is the average effect of the programme on the units that received it, over the four years following receipt." This sentence is what the results section is allowed to make claims about, and putting it here means the discussion cannot quietly promote it later.

3. **Write the estimating equation, numbered, and define every symbol immediately below it.** In sequence: the outcome and the units it is measured in, the treatment variable and how it is coded, each set of fixed effects and what each absorbs, the controls and why they are there, the error term, and the subscripts. Every variable that varies carries a subscript; a variable written without one is a claim that it is constant, and referees read subscripts.

4. **Name the coefficient of interest explicitly and say what it measures in the units of the data.** "The coefficient of interest is beta, which measures the change in log employer firm registrations per municipality-year associated with rollout." Not "beta is the treatment effect". The units matter because they are what makes the results section interpretable, and they are where the mismatch between a level, a log, and a standardised outcome usually appears.

5. **State the identifying assumption in plain words before any notation, and make it specific to this setting.** The rule for whether it is specific enough: the sentence should be false if you swapped in a different paper's setting. "Treated and comparison units would have followed parallel paths absent treatment" is generic and worth nothing. "Municipalities that received rollout in 2016 would have followed the same registration path as those receiving it in 2019, absent rollout, which requires that the regulator's ordering was not driven by expected local business formation" is an assumption a reader can attack, which is the point. Then, where it clarifies, restate it in notation.

6. **Say what would violate it here.** Two or three specific mechanisms, named in this setting, not a generic list of confounders. This is the paragraph that persuades a referee the author has thought about their own design, and it is also the paragraph that makes the next one credible.

7. **Write the threats and responses as pairs.** For each of the two to four most credible threats: the threat in a sentence, the response, and the exhibit number where the reader will find the evidence. Where there is no response, say so and carry it explicitly into the limitations rather than leaving it out. A named threat with an honest concession reads as competence; an unnamed threat that the referee finds reads as concealment, and the two are indistinguishable in the text until the referee looks.

8. **Write the inference paragraph.** The clustering level and the reason for it, stated as the level at which treatment is assigned or at which errors are plausibly correlated, the number of clusters, and any correction used when that number is small. Say whether standard errors are heteroskedasticity-robust. Where the clustering choice is contestable, say what happens under the alternative and name the table where that is shown. The rule: the clustering statement in this paragraph, in the table notes, and in the estimation command must be the same three statements.

9. **Write the estimation details paragraph.** Software and version, the sample used and how it differs from the full data, the treatment of missing values, weights, any standardisation of the outcome, and any two-step or bootstrap procedure with the number of replications and the seed. This paragraph is short, dull, and the reason a replication succeeds.

10. **Write the code block that implements the equation exactly, and reconcile the two line by line.** Same fixed effects, same controls, same sample restriction, same clustering, same weights. Read the equation and the command side by side and tick each element. This takes four minutes and catches the failure that costs a revision cycle.

11. **Read the section once as the referee.** One pass, looking only for the sentence that does not hold. Where you find yourself hoping the reader will not ask something, write the answer.

## Design-specific requirements

**Panel fixed effects.** State what within-unit variation identifies the effect and what the unit fixed effects absorb. State explicitly that time-invariant confounders are absorbed and time-varying ones are not, and name the time-varying confounder a referee would raise in this setting.

**Difference-in-differences.** Parallel trends stated for this outcome, these groups, and this period. Where adoption is staggered, state why a two-way fixed effects estimator can be biased under heterogeneous treatment effects, which modern estimator is used, and how the comparison group is constructed, whether never-treated or not-yet-treated. Name the estimator's source paper and verify that citation against a live record. Where both the two-way fixed effects and the modern estimator are reported, say which is the headline and why.

**Event studies.** Write the specification out with the reference period stated, the binning of endpoint coefficients described, and the normalisation made explicit. State that the pre-period coefficients are evidence on the assumption rather than results, and say what power the pre-period test actually has, because a flat pre-trend estimated imprecisely is not evidence of anything.

**Instrumental variables.** Relevance and exclusion stated as two separate assumptions, in two separate sentences. Exclusion defended with an argument specific to the setting that names the alternative channels and says how each is closed. First-stage strength reported with a statistic appropriate to the case rather than a rule of thumb. The estimand named as a local average treatment effect, with the complier population described in words a reader can picture. Monotonicity stated.

**Regression discontinuity.** Running variable, cutoff, and whether the design is sharp or fuzzy. Bandwidth selection method, kernel, polynomial order, and bias correction, each named rather than implied. The manipulation test and the covariate continuity tests referenced by exhibit. The estimand stated as local to the cutoff, and the paper's claims held to that.

**Matching and reweighting.** Selection on observables written as an assumption, not as a procedure. The covariate set justified by why those variables close the relevant paths. The balance diagnostic named with its threshold. The estimand stated as an effect on the treated or on the whole population, and common support described.

**Synthetic control.** The donor pool and how it was screened, the pre-treatment fit statistic, the predictor set, and the inference procedure, whether placebo-in-space, placebo-in-time, or a permutation distribution.

**Multilevel models.** The nesting structure, which coefficients are random and which fixed, the variance components reported, and, critically, why a multilevel model rather than fixed effects with clustered errors. That last sentence is the one referees in economics ask for and authors most often omit.

## Notation rules

One notation throughout the paper, established here and never varied. Latin letters for variables, Greek for parameters, bold only for vectors, and design-specific indices introduced once with their range. Use i for units and t for time unless the design demands otherwise. Number every equation and refer to it by number in the text rather than by "the equation above", which breaks when the layout changes.

Do not introduce a symbol that appears once. Do not use the same symbol for two things in different sections, which happens most often with k and with j. Where the paper has an appendix with derivations, the notation there is the notation here.

## The equation and the code must agree

This deserves its own check because it is the most common concrete error in the section and the only one that makes the whole paper suspect rather than one paragraph. Build a short reconciliation list and work through it before the section is finished:

| Element | In the equation | In the command | Match |
| Outcome and transformation | | | |
| Treatment variable and coding | | | |
| Fixed effects, each set | | | |
| Controls, each block | | | |
| Sample restriction | | | |
| Weights | | | |
| Clustering level | | | |

Where they differ, the resolution is a decision, not an edit: either the code is wrong and is fixed and the tables regenerated, or the equation was written to describe an intention rather than the estimation and the equation is corrected. Never resolve it by changing whichever is easier to change.

## Worked example

**Situation.** Dr Helena Broz was writing the empirical strategy section of a paper on a national school meal programme rolled out to municipalities in three waves between 2014 and 2018, with attendance as the outcome. She had 1,842 municipalities, nine years, and a two-way fixed effects specification already run, producing an estimate of 2.4 percentage points with a standard error of 0.7. A coauthor had described the existing draft of the section as "a paragraph about a regression".

**Task.** A four-page empirical strategy section for a field journal, written in eight days, that a referee could reproduce the specification from and that would not attract the comment about unclear identification.

**Action.** The first draft started with the equation, because the equation existed. The paragraph written under it, in words, then turned out to be a restatement of the equation in English: unit and year fixed effects control for time-invariant municipal characteristics and common shocks. That is not a design paragraph, it is a caption. The draft was abandoned at about six hundred words.

The rewrite started with step 1 and no symbols. Writing it forced a question nobody on the project had answered in writing: why did the wave ordering happen as it did? Two hours with the programme's implementation documents established that waves were ordered by an administrative readiness score built from school infrastructure returns, and that the score correlated with baseline attendance at 0.31. That single fact reorganised the whole section, because it named the violation mechanism precisely: municipalities treated earlier were systematically those with better infrastructure, and infrastructure plausibly affects attendance growth, not only its level.

Step 2 exposed the second gap. The draft's results section spoke about "the effect of the programme", but with staggered adoption and a two-way fixed effects estimator, the quantity being estimated was a weighted average of two-by-two comparisons with weights that could be negative for the later waves. This was an estimator question, not a writing question, so it went back to the project's econometrician rather than being resolved in prose. The decision that came back was to report a modern staggered-adoption estimator with not-yet-treated comparisons as the headline, with the two-way fixed effects estimate retained in the same table for comparability with the prior literature. The section was then written around the estimand that decision produced: an average effect on treated municipalities over the four years following rollout, aggregated across waves with weights proportional to cohort size.

The threats paragraph carried three pairs. Readiness-correlated trends, answered by an event-study figure with five pre-periods and by a specification adding baseline infrastructure interacted with year, in Figure 2 and Table 4 column 3. A concurrent conditional transfer expansion in 2016 that overlapped one wave, answered by dropping that wave and showing the estimate is 2.1 with a standard error of 0.9, in Table 5. Attendance measurement changing in 2017 when reporting moved to an electronic system, answered honestly with a concession: the change affected all municipalities in the same year, so it is absorbed by year effects unless it interacted with treatment status, which could not be ruled out, and this went into the limitations with the direction of the likely bias stated.

The reconciliation check in step 10 caught one real error. The equation as written included municipality-specific linear trends; the command that produced the headline table did not, because the trends had been dropped during an earlier run to check something and never restored. The estimate with trends was 1.9 rather than 2.4, with a standard error of 0.8. The tables were regenerated and the difference became a robustness row rather than a silent discrepancy.

**Result.** The section ran three and a half pages: design paragraph, estimand, equation with definitions, assumption in words and then in notation, violation mechanisms, three threat-response pairs, inference at the municipality level with 1,842 clusters, and estimation details. It took eleven days rather than eight, and nine of those days were the two questions the writing exposed rather than the writing itself, which is the usual ratio.

Two referees. Neither raised identification as unclear. One asked for the readiness score to be shown as a balance exhibit, which took a day because the argument was already written and only the table was missing.

### A second scenario, where it goes differently

The same author, a different paper, using a rainfall-based instrument for local agricultural income to estimate its effect on secondary school enrolment. Here the writing did not expose a missing decision; it exposed an overclaim.

The draft said the paper estimates the effect of agricultural income on enrolment. Step 2 forced the estimand to be written, and the honest estimand is the effect for households whose income responds to rainfall variation, which in this setting means rain-fed smallholders and not irrigated or non-farm households, roughly forty-one percent of the sample by the first-stage decomposition. That is a materially different claim, and it changed three things beyond the methods section: the abstract's sentence, the title's implicit scope, and one policy paragraph in the discussion that had generalised to all rural households.

The exclusion paragraph also had to be rewritten from a single sentence into three, because writing "rainfall affects enrolment only through agricultural income" made its own implausibility visible: rainfall also affects road passability in the wet season and the local labour demand for children. Both channels were named, and one was closed by controlling for road surface type interacted with season while the other became a stated limitation with the direction of bias.

What changed between the two scenarios is which gap the writing exposed. In the first it was an unmade estimator decision, which goes back to `econometrician`. In the second it was a claim wider than the design supports, which is a rewrite of the paper's contribution and reaches into the abstract and the conclusion. Both are found by the same step, and both are cheaper found here than in review.

## Output

The section, in this order, with these components present:

```
EMPIRICAL STRATEGY

[1] Design in words. One paragraph, no symbols. What varies, across what,
    over what period, why it identifies the effect.

[2] Estimand. One sentence naming the quantity, the population, and the horizon.

[3] Equation (1), numbered, followed immediately by definitions of:
      outcome and units | treatment and coding | each fixed effect and what it
      absorbs | controls and why | error term | subscripts

[4] Coefficient of interest, named, with what it measures in the data's units.

[5] Identifying assumption in plain words, specific to this setting;
    then in notation where it clarifies.

[6] What would violate it here. Two or three named mechanisms.

[7] Threats and responses, as pairs:
      Threat | Response | Exhibit
    Any threat without a response appears again in the limitations.

[8] Inference. Clustering level, reason, number of clusters, correction if any,
    and what changes under the alternative clustering.

[9] Estimation details. Software and version, sample, missing values, weights,
    standardisation, bootstrap replications and seed.

[10] Code block implementing exactly the above.
```

The threats table as it appears in the working file, before being written into prose:

| Threat, specific to this setting | Response | Exhibit | Status |
| Wave ordering correlated with baseline attendance growth | Event study with five pre-periods; baseline infrastructure by year | Fig 2, Tab 4 col 3 | Answered |
| Transfer expansion overlaps wave 2 | Drop wave 2; estimate 2.1 (0.9) | Tab 5 | Answered |
| Reporting system change in 2017 | Absorbed by year effects unless interacted with treatment | none | Limitation, sign stated |

## Failure modes

**The equation with no design paragraph.** Recognisable because the section opens with "we estimate the following equation". Fix by writing the words first and deleting the equations to test whether the strategy survives.

**The generic assumption.** "Parallel trends holds" or "the instrument is exogenous", with nothing setting-specific attached. Recognisable because the sentence could be pasted into another paper without alteration. Fix by writing the version that would be false in a different setting.

**Threats without exhibits.** A list of concerns each followed by a reassuring sentence and no evidence. Referees read this as a list of unanswered problems, which is what it is. Fix by pairing each with an exhibit or by relabelling it as a limitation.

**The estimand promoted between sections.** A local effect at a cutoff in the methods becomes the effect of the policy in the abstract. Recognisable by reading the abstract and the estimand sentence side by side. Fix in the abstract, not by widening the methods.

**Equation and code disagreeing.** The failure with the highest cost. Recognisable only by the reconciliation check, because both artefacts look correct alone. Run the check every time the specification changes.

**Controls listed without reason.** A vector of covariates with no statement of what each is for. Two specific errors hide here: a control that is a mediator, and a control that is a bad control affected by treatment. Fix by saying, for each block, what confounding path it closes.

**The clustering stated in three places and agreeing in two.** Fix by treating the estimation command as the source and propagating from it.

**Method citations from memory.** Estimator and test papers cited without checking. Fix by applying `literature-verification`; a misattributed estimator paper is noticed immediately by anyone who works with that estimator.

**Writing the section before the diagnostics exist.** Produces confident sentences about evidence not yet seen, which then cannot be softened without the section reading oddly. Fix by writing the threats table first with the status column, and the prose only for the rows that are answered.

## Edge cases

**No credible identification exists.** The data supports a descriptive or predictive claim only. Write the section as descriptive, say so in the first paragraph, and remove causal language from the whole paper rather than hedging it. A clearly framed descriptive paper is publishable; a causal paper with a broken design is not, and hedging is the version that gets rejected slowly.

**The design is a horse race between two estimators.** Write one equation with the shared structure, then state precisely what each estimator changes and what different assumption each buys. Do not print two full equations; print the difference.

**A structural or calibrated model.** The section still needs the same skeleton: what identifies each parameter, what moments are matched, and what the identifying variation is. The vocabulary changes and the obligation does not. Put derivations in an appendix and keep the section readable without them.

**The venue caps the methods section at one page.** Keep steps 1, 2, 4, 5 and 8 in the body: design, estimand, coefficient, assumption, inference. Move the equation definitions, the threats and the estimation details to an appendix, and reference it by number. Never cut the assumption sentence.

**A machine learning component in the pipeline.** State the sample split, whether the same observations train and estimate, and how inference accounts for the first stage. A prediction step whose uncertainty is ignored in the second stage is a specific and increasingly common error, and the section must say what was done about it.

**Multiple outcomes or many hypotheses.** State the family, the correction used, and whether the correction was decided before the estimates were seen. `preregistration-and-analysis-plan` is where that commitment belongs; the section reports it.

**The author cannot remember why a control is in the model.** Do not invent a reason. Either find the justification in the project record or drop the control and rerun. A justification written after the fact for a decision nobody remembers is the definition of the thing referees are looking for.

## Quality bar

- A referee can reproduce the specification from the text alone, without the code.
- The identifying assumption is stated in words, specific to this setting, before any notation, and would be false in a different setting.
- The estimand is named in one sentence, and no later section claims anything wider.
- Every threat named has either a response with an exhibit number or an explicit place in the limitations.
- The clustering level, its reason, and the number of clusters appear in the section, and match the table notes and the estimation command.
- Every symbol in every equation is defined, and every varying variable carries a subscript.
- The code block implements the printed equation element by element, verified against the reconciliation list.
- Every method paper cited was checked against a live record.

## Related skills

`econometrician` decides the estimator, the clustering and the inference that this section reports, and any decision the writing exposes as unmade goes back there rather than being settled in prose. `identification-defense` runs the adversarial questioning that produces the threats and responses written up in step 7. `research-design` establishes the source of variation before either. `preregistration-and-analysis-plan` locks these choices before outcomes are seen, and where it exists this section reports it rather than restating it. `stata-do-file-craft` and `python-for-econometrics` hold the code the section must agree with. `regression-table-production` builds the tables the threats reference, and `academic-tables-booktabs` their typography. `results-writing` reads those tables under the estimand this section fixes, and `data-section-writer` describes the data this section estimates on. `literature-verification` governs the method citations.
