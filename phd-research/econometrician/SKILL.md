---
name: econometrician
description: Acts as the econometrician on a project rather than the person writing the paper. Chooses the estimator from the question and the data structure rather than from convention, names the assumption each candidate buys and what breaks it, sets the clustering level and handles the small-cluster problem, decides fixed against random effects without leaning on the Hausman test, resolves weighting and functional form, separates the diagnostics that carry a consequence from the ones that are ritual, and attaches a response rule to every diagnostic that can fail. Use this skill when someone asks which estimator to use, what to cluster on, whether to use fixed or random effects, whether to weight, whether to log the outcome, why their standard errors changed, what robustness checks to run, or what to do now that a test has failed. Trigger also on vague requests such as "is this the right model", "does this specification hold up", "the referee attacked my standard errors", or "check my econometrics".
---

# Econometrician

The failure this prevents is an estimator chosen by convention. Somebody runs two-way fixed effects because the last three papers in the field did, clusters at the level of the fixed effect because that is where the command puts it by default, reports a Hausman test because a textbook said to, and never states what the coefficient is an estimate of. Nothing in the output looks wrong. The regression converges, the stars appear, and the paper is written around a number whose meaning nobody has established.

The cost is that the result is unsupported rather than false, which is harder to fix and worse to discover late. A referee who clusters one level up finds the significance gone. A discussant points out that with staggered treatment timing the two-way fixed effects coefficient is a weighted average of comparisons that includes already-treated units as controls, with weights that can be negative. A data editor reruns the code and the sample changes because the weighting decision was never made, only defaulted. Each of these is recoverable at the design stage for an afternoon of work and costs a resubmission cycle at the referee stage.

This skill is the person on the project who asks those questions before anyone else does. It advises and it stress-tests. It does not write the methods section and it does not build the tables.

## When to use this, and when not to

Use it when choosing an estimator, when a specification decision has to be justified, when standard errors need a defensible level, when a diagnostic has failed and nobody knows what follows from that, when two specifications disagree and someone has to decide which is preferred, and when a referee has attacked the inference rather than the design.

Use it before estimation wherever possible. Most of what it does is cheap in advance and expensive afterwards, because a specification chosen after seeing the results carries a different evidentiary weight and everyone knows it.

Do not use it to write the empirical strategy section; `econometric-model-writer` does that, and it should be given the decisions this skill produces rather than making them itself. Do not use it to defend the identification strategy against a hostile reader; `identification-defense` runs that attack and builds the answer. Do not use it to choose the research design in the first place, which is `research-design`, or to lock the specification in advance of seeing outcomes, which is `preregistration-and-analysis-plan`. Do not use it to interpret magnitudes or write the results text, which is `results-writing`.

The boundary in one line: `research-design` decides what variation to use, this skill decides what to do with it, `identification-defense` decides whether anyone will believe it, and `econometric-model-writer` writes it down.

## What you need before starting

**The question stated as a comparison.** Not a topic and not a variable pair. What is being compared with what, for which units, over what horizon. Missing: write the comparison in one sentence and get it confirmed before anything else, because every decision below follows from it and none of them can be made without it.

**The data structure.** Cross-section, repeated cross-section, panel with its dimensions, hierarchy and its levels, time series and its length, and whether the sample is a random draw, a census, a stratified survey or a convenience sample. Missing: establish it from the data with `xtdescribe` or its equivalent before proceeding; assuming a balanced panel that turns out to be unbalanced changes both the estimator and the interpretation.

**The source of variation being exploited.** What makes two otherwise comparable units differ in the regressor of interest. Missing: this is not a gap to work around. If nobody can name the variation, there is no design yet, and the correct output is that finding rather than an estimator.

**Unit counts at every level.** Observations, units, clusters, treated units, treated clusters. The number of treated clusters is the single most commonly omitted number and it determines whether conventional inference works at all. Missing: count them first; the counts take one command and they change the recommendation more often than anything else on this list.

**The outcome's measurement and distribution.** Continuous, binary, count, censored, share, ordinal. Zeros, mass points, top-coding, and the units it is measured in. Missing: plot it before choosing a functional form; a histogram settles arguments that theory does not.

**The sampling and weighting scheme.** Sample weights, strata, primary sampling units, and whether the target quantity is a population parameter or a model parameter. Missing: assume the design is informative and check whether weighted and unweighted estimates differ; that comparison is diagnostic in itself.

**Treatment timing, where there is a treatment.** When each unit is treated, whether treatment can switch off, and whether any unit is never treated. Missing: tabulate the treatment start by unit before writing any estimation command, because staggered timing changes the estimator and a never-treated group changes what comparisons are available.

## The method

1. **Write the estimand before the estimator.** State what quantity you are trying to learn: the average effect on everyone, on the treated, on those who respond to an instrument, on those assigned regardless of compliance. The rule is that you cannot choose an estimator until you can name whose effect it is. Where the honest answer is "the effect on the units whose treatment status is moved by this variation", say that, because it is the answer that instrumental variables and most quasi-experiments actually deliver, and it determines whether the estimate speaks to the policy question that motivated the paper.

2. **Map the structure to a candidate set, then reduce it by assumption.** The structure narrows the field; the assumptions you are willing to defend choose within it.

| Structure and variation | Default candidates | What the default buys | What breaks it |
| Cross-section, selection on observables | OLS with controls, matching, inverse probability weighting | Conditional independence given the controls | An unobserved determinant of both treatment and outcome |
| Panel, time-invariant unobserved heterogeneity | Unit fixed effects | Anything fixed within the unit is absorbed | Time-varying confounders; measurement error is amplified by within transformation |
| Panel, common shocks and a treatment date | Two-way fixed effects, event study | Parallel trends conditional on the fixed effects | Treatment effect heterogeneity when timing is staggered; anticipation |
| Staggered adoption | Heterogeneity-robust estimators using clean controls | Parallel trends without homogeneous effects | No clean comparison group at some horizons |
| An excluded instrument | Two-stage least squares, limited information maximum likelihood | Relevance plus exclusion | Weak first stage; violated exclusion; heterogeneous compliance changes the estimand |
| A running variable and a cutoff | Local polynomial regression discontinuity | Continuity of potential outcomes at the cutoff | Manipulation of the running variable; the estimate is local to the cutoff |
| Non-negative outcome with many zeros | Poisson pseudo-maximum likelihood | Correct conditional mean without distributional assumptions | Nothing much; it is more robust here than logging |
| Hierarchical data, interest in how much variance sits at each level, or in a level-2 predictor | Multilevel or mixed model, random intercepts and where justified random slopes | Partial pooling across groups, estimates for small groups, a decomposition of variance by level, and coefficients on group-level regressors | Correlation between the random effect and a level-1 regressor, which biases the level-1 coefficients unless the model is written to handle it |
| Hierarchical data where a level-1 causal effect is the target and group-level confounding is suspected | Within-between or Mundlak specification: group means of the time-varying or level-1 regressors added to a random effects model | The within coefficient equals the fixed effects estimate while level-2 regressors remain estimable, and the between and within parts are separated | Nothing that fixed effects would not also break; it costs only the extra parameters |

3. **State, in writing, the assumption each candidate buys and the single most plausible thing that breaks it.** One line each. This is what makes step 2 an argument rather than a lookup, and it is the paragraph that later becomes the threats subsection. Where two candidates rest on assumptions that are not nested, neither is a robustness check on the other and both belong in the paper as separate columns.

4. **Set the clustering level from the design, not from the command's default.** Cluster at the level at which treatment is assigned, or at the level at which the sample was clustered, whichever is coarser. Not at the level of the fixed effect, which is the most common error, and not at the finest available level, which is the second. If treatment varies at province level, clustering at firm level understates the standard error however many firms there are, because the residuals are correlated within province through the treatment itself.

Where two levels are both plausible, cluster at the coarser one and report the finer as a footnote. Where the design has two crossed dimensions, such as industry and year, consider two-way clustering, remembering that it requires many units in both dimensions to behave well.

5. **Count the clusters, and treat fewer than about forty as a problem rather than a detail.** This is the threshold the library uses throughout, and `identification-defense` states the same number, so a reader is not asked to reconcile two rules. The reason for forty rather than some smaller figure: cluster-robust inference is justified asymptotically in the number of clusters, the variance estimator is downward biased in finite samples, and the bias is already material in the thirties, severe by fifteen, and not reliably fixed by a degrees-of-freedom adjustment. Forty is where the conventional standard error stops being safe to quote on its own, not where it becomes indefensible; the failure is gradual and it always runs in the same direction, towards a p-value that is too small. The number that matters most is the number of treated clusters, which can be small even when the total is not. Below roughly forty clusters, or with fewer than about ten treated, do not report the conventional standard error alone.

The practical options, in the order to try them: the wild cluster bootstrap with the null imposed, which is well behaved down to surprisingly small numbers; randomisation inference, which is the natural choice when treatment was actually randomised at the cluster level; and aggregation to one observation per cluster and period, which throws away information but yields inference that is easy to defend. Report the conventional and the corrected result together, and let the corrected one govern the claim.

```stata
* main estimate
reghdfe earnings treat x1 x2, absorb(worker_id year) cluster(province)

* with 23 clusters, the conventional p-value is not the one to quote
boottest treat, reps(9999) boottype(wild) cluster(province) nograph
```

6. **Decide fixed against random effects on what you are willing to assume, and do not let a Hausman test decide it.** Random effects, and the multilevel models built on it, assume the unit or group effect is uncorrelated with the regressors. Whether that assumption is tolerable depends on what you are estimating and on how the units came to be what they are, and the disciplines differ for good reasons rather than out of habit.

   In observational economics the units are usually firms, regions or workers that selected into treatment, so the unobserved unit effect is correlated with the regressor of interest almost by construction, and correlated in the direction that inflates the estimate. That is why fixed effects is the economics default: it buys robustness to any time-invariant confounder at the cost of discarding between-unit variation, and in a field whose central worry is selection that trade is usually worth making.

   In education, psychology, public health and organisational research the question is often different. The pupils-in-classrooms-in-schools structure is not a nuisance to be absorbed; the variance at each level is part of the answer, the group-level predictor is often the treatment, and groups are small enough that partial pooling gives better estimates for the small ones than a separate intercept per group would. A multilevel model with random intercepts, and random slopes where the effect is expected to vary across groups, is the right tool there and not a weaker substitute for fixed effects. It also handles unbalanced and incomplete clusters gracefully, which fixed effects does not.

   Choose on these conditions rather than on discipline:

   | Use | When |
   | --- | --- |
   | Fixed effects | The target is a within-unit causal effect, selection into treatment is the main worry, there is enough within variation to identify the effect, and no level-2 regressor needs a coefficient |
   | Multilevel or mixed model | Variance decomposition, group-level predictors, cross-level interactions, small or unbalanced groups needing partial pooling, or growth curves and repeated measures where the random slope is the object of interest |
   | Within-between or Mundlak | Both: a within estimate you can defend and level-2 coefficients you still need. This is the middle path and it should be the default when the two goals conflict |

   The within-between formulation is worth stating explicitly because it dissolves most of the argument. Add the group means of the level-1 regressors to a random effects or multilevel model. The coefficient on the deviation from the group mean is numerically the fixed effects estimate, the coefficient on the group mean is the between-group relationship, and their difference is exactly what the Hausman test was trying to detect. A joint test that the added means are zero is the honest test of the random effects assumption, it can be made cluster-robust, and unlike the classical Hausman test it tells you which regressors carry the problem. It is called correlated random effects in econometrics and within-between or hybrid in sociology and education; it is the same specification.

   The classical Hausman test is a poor decision rule wherever it is used. It compares the two coefficient vectors; a rejection tells you they differ, and a failure to reject is weak evidence of anything, particularly in small samples where the test has little power. The classical form is also invalid under clustering or heteroskedasticity, which is the normal case, so the test as usually reported does not test what it is presented as testing. Use the Mundlak joint test instead, or argue the choice substantively.

Use fixed effects when the parameter of interest is identified from within-unit variation and there is enough of it; `xtsum` tells you how much, and where the within variation is thin, fixed effects is precise about nothing. Use a random effects or multilevel model when you need the coefficient on a time-invariant or group-level regressor, when the variance at each level is part of the question, or when partial pooling across small groups is what the data calls for, and in the first of those cases prefer the correlated random effects form, which adds the unit means of the time-varying regressors and recovers the fixed effects estimates for those while still permitting a time-invariant term. That specification also gives an honest test of the random effects assumption as a joint test on the added means. In Stata it is `xtreg, re` with the group means added, or `mixed`; in R it is `lme4::lmer` or `nlme`; in Mplus it is a two-level model; the specification is the same object in all of them.

Where the within variation is thin, say so and report the between estimate separately rather than presenting a fixed effects coefficient with a wide interval as though it were informative.

7. **Resolve weighting by asking what the target is.** Use sample weights when the target is a descriptive population quantity, such as the mean effect in the population the survey represents. Use unweighted estimation when the target is a model parameter, the design is exogenous conditional on the controls, and the weights are a function of variables already in the model, because weighting then costs precision and buys nothing.

The useful move is to run both. If weighted and unweighted estimates are close, report the unweighted and note the check. If they differ materially, that difference is information: it says the effect is heterogeneous across the dimension the weights vary on, or the model is misspecified. Investigate it rather than picking whichever is more convenient, and report what you found.

8. **Choose functional form from the outcome, not from habit.** Logs when the effect is plausibly proportional and the outcome is strictly positive. Levels when zeros are meaningful or the policy question is in units. Never `log(1 + y)` as a way around zeros: the transformation makes the coefficient depend on the units the outcome is measured in, which is enough to disqualify it. For a non-negative outcome with zeros, Poisson pseudo-maximum likelihood estimates a proportional model without discarding the zeros and without a distributional assumption, and it handles high-dimensional fixed effects.

For binary outcomes, the linear probability model is acceptable and usually preferred with fixed effects, with the caveats stated: fitted values can leave the unit interval and the marginal effect is constant by construction. Logit and probit are appropriate when the tails matter or when predicted probabilities are the deliverable, and in that case report average marginal effects rather than coefficients, and remember that the interaction term in a nonlinear model is not the coefficient on the product term.

Prefer splines or binned indicators to high-order polynomials for flexible functional form, particularly near a boundary. In regression discontinuity, a global high-order polynomial is a known way to manufacture a discontinuity, and local linear estimation with a data-driven bandwidth is the standard.

```stata
* proportional effect with zeros retained, high-dimensional fixed effects
ppmlhdfe exports tariff, absorb(exporter#year importer#year) cluster(pair_id)
```

9. **Run the diagnostics that carry a consequence and drop the ones that do not.** The test of whether a diagnostic is worth running is whether you can say in advance what you will do differently if it fails. If you cannot, it is decoration.

| Worth running | What it tells you | Ritual | Why it is ritual |
| Balance or overlap on covariates | Whether the comparison is between comparable units | Variance inflation factors | Collinearity is visible in the standard errors already, and there is no threshold that means anything |
| Pre-treatment trends, plotted as an event study | Whether the parallel trends assumption is plausible where testable | Breusch-Pagan for heteroskedasticity | You are using robust standard errors regardless, so the answer changes nothing |
| First-stage strength, with a weak-instrument-robust interval | Whether the instrumental variables estimate means anything | Normality tests on residuals | Irrelevant in samples large enough for the asymptotics, and uninformative in samples too small for them |
| Sensitivity to sample definition and to the control set | Whether the result is a knife edge | Hausman as a fixed against random effects decision rule | It does not test the assumption you care about, and it is invalid under clustering |
| Leave-one-out and influence, by cluster | Whether one unit is carrying the result | R-squared thresholds | Fit is not identification and no threshold exists |
| Placebo outcomes and placebo timing | Whether the design detects effects where none should exist | Durbin-Watson in a panel | Superseded by clustering, which handles serial correlation directly |
| Alternative clustering levels and bootstrap inference | Whether the p-value is robust to the inference choice | Stepwise or automated variable selection | It invalidates the reported inference and answers no stated question |

10. **Attach a response to every failure before you run the test.** A diagnostic without a pre-agreed response becomes a diagnostic that gets rerun until it passes.

| Diagnostic fails | What it means | Do this | Do not do this |
| Pre-trends differ | Parallel trends is doubtful | Report the event study in full; add unit-specific trends and show whether the result survives; consider a design with a stronger control group | Drop the pre-periods that misbehave |
| Covariates unbalanced | The comparison is not like for like | Reweight or match, and report the estimate on the common support only | Add the unbalanced covariate as a control and declare it handled |
| First stage weak | The two-stage estimate is biased toward ordinary least squares and its interval is wrong | Report the reduced form and an Anderson-Rubin or other weak-instrument-robust confidence set | Report the two-stage point estimate with a note that the F is "close to ten" |
| Result sensitive to one cluster | The finding rests on one unit | Report both with and without, and say which units drive it | Present only the version without it |
| Weighted and unweighted differ | Effect heterogeneity or misspecification | Report both, and characterise the dimension along which they differ | Choose the one that supports the hypothesis |
| Wild bootstrap p-value much larger | Conventional inference was over-confident with few clusters | Quote the bootstrap p-value in the text and the table note | Keep the conventional stars |
| Result appears only in one of several reasonable specifications | The finding is fragile | Report the full set and describe the pattern honestly | Name the surviving specification as the preferred one after the fact |

11. **Fix the preferred specification and the robustness set in advance, and report all of it.** Write down, before estimating, which specification is preferred and why, and which variations will be reported whatever they show. This is what separates a robustness section from a curated one. Where the set is large, a specification curve showing the distribution of estimates across all defensible combinations is more honest and more compact than eight tables, and it is read faster.

12. **Say what would change your conclusion.** One sentence, in the paper. It costs nothing, it is what a good referee is looking for, and writing it forces the author to notice when the answer is "nothing", which means the claim is not empirical.

## Worked example

**Situation.** An evaluation team was estimating the earnings effect of a public training programme rolled out across 23 provinces between 2015 and 2019, with different provinces starting in different years and two never adopting. The data were an administrative worker panel, roughly 180,000 individuals observed annually from 2012 to 2022, with province of residence, sector, and annual earnings. A first draft reported a two-way fixed effects difference-in-differences estimate of 4.2 percent, clustered at the individual level, significant at one percent, with a Hausman test in a footnote justifying fixed effects.

**Task.** Establish whether that number was defensible before the paper went to a policy audience that would act on it, in about two weeks, and produce a written record of every estimation decision.

**Action.** Three problems were identified in the first hour, and the order they were addressed in turned out to matter.

The clustering was wrong and was the easiest to fix. Treatment varied at province by year, so clustering at the individual level was clustering below the level of assignment; it produced standard errors roughly a fifth of the correct size. Moving to province clustering took the t-statistic from 9.1 to 2.3.

That immediately created the second problem. There were 23 clusters, of which 21 were ever treated. The conventional cluster-robust standard error at that count is downward biased. A wild cluster bootstrap with the null imposed gave a p-value of 0.11 against the conventional 0.03. The team's first instinct was to report the conventional figure and mention the bootstrap in an appendix. That was the wrong turn, and it was abandoned after the question was put plainly: if the bootstrap is the more reliable procedure at this cluster count, and it is, then the bootstrap number is the result and the conventional one is the footnote. Reversing the two changed the paper's claim from an established effect to a positive point estimate that the data could not distinguish from zero at conventional levels.

The third problem was the estimator itself. With staggered adoption and effects that grew with exposure, the two-way fixed effects coefficient was a weighted average that used already-treated provinces as controls for later adopters, and some of those weights were negative. Re-estimating with a heterogeneity-robust estimator that uses only never-treated and not-yet-treated units as controls gave 5.6 percent rather than 4.2, with an event study showing effects rising over four years from near zero to about 9 percent. The two-way fixed effects estimate had been averaging a growing effect against comparisons that pointed the wrong way.

The Hausman footnote was removed rather than repaired. Fixed effects was justified in one sentence on the grounds that province and cohort characteristics correlated with programme placement, which was true, checkable, and did not require a test.

Weighting was checked and made no difference: the administrative data were a census of formal employment, weighted and unweighted estimates agreed to the second decimal, and one sentence recorded the check.

**Result.** The reported estimate became 5.6 percent, with a bootstrap p-value of 0.04, an event study figure showing the profile, and an explicit statement that with 21 treated provinces the inference rests on a bootstrap rather than on asymptotics. The policy audience received a weaker but defensible claim. Two months later a referee at a field journal raised exactly the staggered-adoption point about the original estimator, and the answer already existed in the paper. The work took nine days, of which six were re-estimation and three were writing down the decisions.

### A second scenario, where it goes differently

A different project had a single cross-section of 2,340 manufacturing firms, an instrument for technology adoption based on distance to a fibre optic backbone, and no panel dimension at all. Almost nothing above applied.

Clustering was a non-issue: with no repeated observations and no group assignment, heteroskedasticity-robust standard errors were the correct choice and there was no small-cluster problem to solve. Fixed against random effects did not arise. Weighting did not arise, since the sample was a stratified survey and the strata indicators were already in the model.

What dominated instead was instrument strength. The first-stage F was 6.4, which is weak, and the two-stage estimate of 0.31 came with a conventional interval that was not trustworthy at that strength. The response was the one in the failure table: report the reduced form, which was clean and significant, report an Anderson-Rubin confidence set, which ran from 0.04 to 1.02, and state in the text that the design supports a positive effect whose magnitude the data cannot pin down. The authors had wanted to argue that an F of 6.4 was "close enough to the conventional threshold". It is not, and the weak-instrument-robust interval is the honest way to report a weak instrument rather than a reason to hide one.

The rule that generalises: the binding constraint differs by design. In the panel case it was the number of clusters and the treatment timing. In the cross-section it was instrument strength. Identifying which constraint binds is most of the work, and the diagnostics worth running are the ones that bear on it.

## Output

The deliverable is an estimation decision record, one page, produced before estimation and updated when a decision changes. It is what `econometric-model-writer` is handed, and it is what makes a specification defensible six months later.

```
ESTIMATION DECISION RECORD
Project        : Provincial training programme, earnings effects
Estimand       : ATT on workers in adopting provinces, 1 to 5 years after adoption
Data structure : Unbalanced worker panel, 180,412 workers, 23 provinces, 2012-2022
Variation used : Staggered provincial adoption, 2015 to 2019; 2 never-treated provinces
```

| Decision | Choice | Alternative considered | Rule applied | What would change it |
| Estimator | Heterogeneity-robust staggered DiD | Two-way fixed effects | Staggered timing with dynamic effects makes TWFE weights unreliable | Uniform adoption date, or flat effects |
| Comparison group | Never-treated and not-yet-treated | Never-treated only | Two never-treated provinces are too few to carry the design alone | More never-treated units |
| Clustering | Province, 23 clusters | Individual; province-year | Cluster at the level of assignment, which is province | Treatment assigned at a finer level |
| Inference | Wild cluster bootstrap, null imposed, 9,999 reps | Conventional cluster-robust | Fewer than 40 clusters | 50 or more clusters |
| Unit effects | Worker fixed effects | Random effects | Placement correlates with province characteristics | Interest in a time-invariant regressor, which would call for correlated random effects |
| Weighting | Unweighted | Survey weighted | Administrative census, weighted and unweighted agree | A difference above one standard error |
| Functional form | Log earnings, positive earners only | Level; inverse hyperbolic sine | Proportional effect expected; zeros handled by a separate employment margin | Zeros central to the question, which would call for Poisson |
| Preferred specification | Column 3 | Columns 1, 2, 4, 5 reported | Fixed before estimation | Nothing after estimation |

Followed by the diagnostics table with a stated response for each, and one sentence naming what would change the conclusion.

## Failure modes

**Clustering at the level of the fixed effect.** Recognise it when the cluster variable and the absorbed variable are the same and treatment varies more coarsely. Fix by clustering at the level of assignment.

**Reporting conventional standard errors with few clusters.** Recognise it by counting clusters; below forty, or below ten treated, the conventional figure is not the one to quote. Fix with a wild cluster bootstrap or randomisation inference, and lead with that result.

**Two-way fixed effects on staggered treatment with dynamic effects.** Recognise it from a tabulation of adoption dates showing more than two cohorts, combined with an event study whose effect grows. Fix with an estimator that restricts comparisons to clean controls.

**The Hausman test as a decision rule.** Recognise it in a footnote justifying fixed effects by a test statistic. Fix by justifying the choice on substantive grounds, or by running the Mundlak joint test on the added group means, which is valid under clustering and says which regressors carry the correlation, and deleting the classical test.

**Dismissing a multilevel model because the field does not use them.** Recognise it when a hierarchical dataset with a group-level treatment is run as unit fixed effects and the group-level coefficient is then reported as absorbed and unavailable. Fix with the within-between specification, which gives both.

**Adding a control to fix an imbalance.** Recognise it when a covariate that failed a balance test appears as a regressor with no other justification. Fix by reweighting or restricting to common support, and by reporting the imbalance.

**`log(1 + y)` for an outcome with zeros.** Recognise it in the variable construction. Fix with Poisson pseudo-maximum likelihood, or by modelling the extensive and intensive margins separately.

**Robustness sections that only contain surviving specifications.** Recognise it when every robustness column is significant and no variation is reported that changes the conclusion. Fix by defining the set in advance and reporting all of it, or by using a specification curve.

**Diagnostics with no consequence.** Recognise it when a test appears in the paper and nothing anywhere depends on its result. Fix by deleting it and running something that would change a decision.

**Choosing the estimator after seeing which one gives the expected sign.** Recognise it from the absence of any written record of the decision predating the results. Fix by writing the decision record, which is the only defence available after the fact and a complete one before it.

## Edge cases

**Very few treated units, sometimes one.** Conventional inference does not apply. Use synthetic control or permutation-based inference where the design permits, report the estimate as a case study with an explicit permutation p-value, and resist reporting a standard error that implies more information than exists.

**Treatment that switches on and off.** Most heterogeneity-robust staggered estimators assume absorbing treatment. Where treatment reverses, say so, use an estimator that permits it, and check whether the reversals are a distinct population.

**A dependent variable that is a share or a rate bounded at zero and one.** Fractional response methods respect the bounds; a linear model is acceptable when the mass is away from the boundaries and is not when much of it sits at zero or one. Check the histogram before deciding.

**Serial correlation with a long time dimension and few units.** Clustering by unit relies on many units; with few units and long series, consider aggregating to before and after, or use inference designed for the time series case. This is the case where the clustering habit fails silently.

**Multiple outcomes or many subgroups.** Pre-specify the primary outcome and adjust for multiplicity on the rest, or state clearly that the secondary results are exploratory. Both are acceptable; an unadjusted table of twenty outcomes with two stars in it is not.

**Machine learning used for prediction inside a causal estimate.** Sample splitting or cross-fitting is required for valid inference; a model selected on the same data used for estimation invalidates the standard errors. Where the deliverable is genuinely a prediction rather than an effect, say so, and evaluate it out of sample rather than reporting coefficients.

**A design where no estimator is defensible.** This happens and the correct output is to say so early. Recommend either a different source of variation, a descriptive paper stated as descriptive, or data collection. Delivering an estimator for a design that cannot support one is the most expensive possible outcome, because everything downstream is then built on it.

## Quality bar

- The estimand is stated in words, naming whose effect it is, before any estimator is named.
- The clustering level is justified by the level of treatment assignment or sampling, and the number of clusters and treated clusters is reported.
- Where clusters are few, an inference method valid at that count governs the reported result and the conventional figure is secondary.
- Every diagnostic reported has a stated consequence, and every diagnostic that failed has a stated response that was decided before it was run.
- The fixed against random effects choice rests on a substantive argument about what the parameter of interest is and how the units came to be treated, not on a classical Hausman test, and where both a within estimate and a group-level coefficient are needed the within-between specification is used rather than one of them being abandoned.
- Weighted and unweighted estimates were compared, and any material difference is reported and explained rather than resolved by preference.
- The preferred specification was fixed in advance, and the full robustness set is reported including the results that weaken the claim.
- One sentence states what evidence would change the conclusion.

## Adapting this to your context

These are economics defaults: observational panels, selection into treatment as the central worry, fixed effects as the first move, cluster counts set by administrative geography. The decision logic transfers; the defaults should be reset.

- **Fixed effects as the starting point.** Right when selection into treatment is the main threat and the target is a within-unit effect. In education, psychology and public health, where the hierarchy is part of the question and treatment is often at the group level, start from a multilevel model and use the within-between specification when you need both. Step 6 sets the conditions.
- **Clustering at the level of assignment.** Same rule, different vocabulary: the randomisation unit in a cluster randomised trial, the primary sampling unit in survey work, the participant in repeated measures.
- **The forty cluster threshold.** It applies wherever cluster-robust inference is used, trials and multisite studies included. Corrections exist everywhere: `boottest` in Stata, `fwildclusterboot` and `clubSandwich` in R.
- **Stata commands.** `reghdfe`, `ppmlhdfe`, `xtsum`, `boottest`. The R equivalents are `fixest::feols`, `fixest::fepois`, `lme4::lmer` and `clubSandwich`; SPSS `MIXED` and SAS `PROC MIXED` or `PROC GLIMMIX` cover the multilevel side.
- **What not to change.** Name the estimand before the estimator, state the assumption each candidate buys and what breaks it, and let the inference procedure that is valid at your cluster count govern the claim.

## Related skills

`research-design` chooses the source of variation this skill then estimates from, and `preregistration-and-analysis-plan` locks these decisions before outcomes are seen. `identification-defense` stress-tests whether the design is believable, where this skill stress-tests whether the estimation is correct given the design. `econometric-model-writer` turns the decision record into the empirical strategy section. `regression-table-production` builds the tables and carries the clustering and sample statements into their notes. `stata-data-management` and `python-for-econometrics` supply the analysis file and the estimation commands. `results-writing` interprets the magnitudes, and `analysis-audit` checks afterwards that the reported numbers came from the specification described.
