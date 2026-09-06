---
name: preregistration-and-analysis-plan
description: Writes a preregistration or pre-analysis plan specific enough to constrain the analysis rather than to decorate it: numbered directional hypotheses, one primary outcome named as primary, the exact estimating specification with its controls and fixed effects and clustering, the sample and the exclusion rules fixed before outcomes are visible, a stated approach to multiple comparisons and named subgroups, a power calculation whose assumed effect size is sourced, an explicit statement of what would count as a null, and a promised deviations table. Enforces the test that two competent analysts reading the plan and handed the same data must produce the same numbers. Use this skill when preregistering a study, writing a pre-analysis plan for a trial or field or survey experiment, preparing a registered report, meeting a funder or ethics requirement for an analysis plan, registering an analysis of existing data, or when someone asks how to avoid p-hacking, specification searching, or the accusation of HARKing.
---

# Preregistration and Analysis Plan

A preregistration is a promise made before the data can influence the promise. Its entire value is specificity. A plan loose enough to accommodate any result constrains nothing, and it is worse than writing none at all, because it claims a credibility it has not earned and it invites everyone downstream, including the author, to believe the analysis was disciplined when it was not.

The failure is rarely dishonesty. It is a plan that says "we will control for standard demographic characteristics", "we will examine several measures of wellbeing", and "outliers will be excluded", written in good faith by someone who has not yet realised that each of those phrases is a door left open. Eighteen months later the results are ambiguous, the deadline is close, and each open door gets walked through once, in the direction of significance, by a person who would sincerely deny having searched. The plan permitted every step.

What that costs is specific. A referee who compares the registered plan with the paper finds three unexplained differences and stops trusting the rest. A replication fails and nobody can tell whether the original was wrong or merely flexible. And in the worst case the field spends a decade on an effect that was a specification.

The test to apply to every line of the plan: could two competent analysts, reading this and handed the same dataset, produce different numbers? If yes, the line is not finished.

## When to use this, and when not to

Use it before any data collection whose results will be published: a field experiment, a laboratory or survey experiment, a trial, a panel wave being fielded. Use it when a funder or an ethics committee requires an analysis plan, which increasingly they do, and use it when preparing a registered report, where the design is reviewed before the data exists.

Use it also for a planned analysis of data that already exists, which is the harder and more common case in economics and sociology. It is legitimate and valuable, and it demands a disclosure this skill treats as mandatory rather than optional.

Use it when someone asks how to protect themselves against the accusation of fishing. The honest answer is that a preregistration is the only durable protection, and that it has to be written when it is inconvenient.

Do not use it to produce the underlying design. The question, the identification strategy and the exhibit list come from `research-design`, and a preregistration written without one ends up inventing the design in a document that is not built for it. Do not use it to write the methods section of a finished paper, which is `econometric-model-writer`. Do not use it to reconstruct what was planned after the analysis is done. That document has a name and the name is not preregistration; what is available at that stage is an honest robustness appendix and a clear statement that the analysis was exploratory, and `analysis-audit` is the skill for it.

Do not use it as a substitute for ethics approval or a data management plan; those are `research-ethics-and-data-protection`, and they run on a different timetable, usually a longer one.

## What you need before starting

**A finished design.** The question, the source of variation, the population, and the identification strategy. Missing: stop and run `research-design`. A preregistration is a hardening of a design, and hardening nothing produces a document full of placeholders that will be filled in later, which is the thing being guarded against.

**The primary outcome, and the willingness to name only one.** Missing: this is the most common gap and it is resolved by asking which single number the paper's headline sentence will report. If the answer is genuinely a family of outcomes, build a pre-specified index and name the index as primary, with components secondary.

**An effect size to power against, with a source.** From the closest prior study, from a pilot, or from the smallest effect that would matter practically. Missing: do not invent one. Say which of the three sources you are using and where the number came from. A power calculation with an unsourced effect size is a calculation about nothing.

**The sample you can actually obtain, and its cost.** Missing: write the plan with the sample as a variable and compute the minimum detectable effect at two or three feasible sizes, because that table is what makes the funding conversation concrete.

**The exclusion rules, decided now.** Attention checks, incomplete responses, ineligible units, implausible values. Missing: this is where silent specification searching most often lives, so write the rules even where they feel obvious, and write the numeric thresholds rather than the concept.

**An honest account of what has already been seen.** For existing data: which variables have been examined, which specifications run, by whom, and when. Missing: ask directly and record the answer in the plan. This determines what can be called confirmatory and what cannot, and it cannot be determined later.

**The registry and its template.** Different registries demand different fields and some are field-specific. Missing: write the plan in the structure below and map it to the registry's fields at submission, rather than letting a form dictate the thinking.

## The method

1. **State the question in one sentence and the design in one paragraph.** Lifted from the design document, not rewritten. If rewriting improves it, fix the design document too, so the two do not diverge from the first day.

2. **Number the hypotheses and give each a direction.** Where theory implies a sign, state the sign. A hypothesis with no direction cannot fail, because any significant result confirms it and any null is explained away. Where theory genuinely gives no direction, say so explicitly and treat the test as two-sided, rather than leaving the ambiguity to be resolved by the data.

3. **Separate confirmatory from exploratory, in writing, before either exists.** Confirmatory hypotheses are being tested. Exploratory questions are being looked at. Exploratory work is legitimate and often the most interesting part of a study; what is not legitimate is reporting it in the register of a test. The rule: anything not in the confirmatory list at registration is exploratory forever, regardless of how strong the result is or how good the theoretical story becomes afterwards.

4. **Name one primary outcome.** Singular. Define how it is constructed from raw measures, including the item wording, the scale, the direction of coding, and the aggregation rule if it is an index. List secondary outcomes separately and say plainly that they are secondary. The rule that makes this bite: the paper's abstract reports the primary outcome, whatever it shows.

5. **Define the sample and every exclusion, with numeric thresholds.** Population, sampling frame, how units enter, target size, and each exclusion rule stated so that applying it requires no judgement. "Respondents failing two or more of the three attention checks" is a rule. "Inattentive respondents" is not. Commit also to reporting the main result without exclusions, which costs one extra row in a table and removes an entire class of referee suspicion.

6. **Write the power calculation with its assumed effect size sourced.** State the assumed effect, where it came from, the significance level, the power, the assumed variance, and any clustering or intra-cluster correlation. Then state the minimum detectable effect at the sample you will actually get. The judgement call: if the minimum detectable effect is larger than the effect the literature reports, the study is not powered to answer its question, and the plan must say so and say what changes. The options are more units, a lower-variance outcome, pre-specified covariate adjustment, a within-subject design, or accepting that only large effects are detectable and stating that limit in advance. Reverse-engineering an effect size from the affordable sample and presenting it as an assumption is the one move that is not available.

7. **Write the specification as an equation with every term defined.** Estimator, functional form, every covariate listed by name, fixed effects listed individually, the standard error treatment with the clustering level and its reason, and the rule for missing data. State which specification is the headline before you know what any of them show.

8. **Decide multiple comparisons and name every subgroup.** Count the hypotheses being tested. State the correction and the family it applies to, or state why none is needed. Name each subgroup analysis in advance with its predicted direction. Subgroups discovered afterwards are exploratory whatever the p-value says, and saying so in the plan is what makes it possible to report one honestly later.

9. **Write what would count as a null, and what would count as inconclusive.** Three outcomes, not two: the hypothesis is supported, the hypothesis is disconfirmed, and the study cannot tell. For the second, state the interval that would constitute evidence of a small or absent effect rather than merely a failure to reject. A plan in which no possible result disconfirms the hypothesis is not a test, and this step is where that defect becomes visible.

10. **Promise the deviations table.** State now that the paper will contain a table listing every departure from the plan, when it was made, why, and what the preregistered version would have shown. Deciding at registration that this table will exist removes the decision from the moment when it is hardest to make well.

11. **Run the two-analysts test on the finished document.** Read it as though you were an analyst who has never spoken to the author, and mark every line where you would have to make a choice. Each mark is a repair. This takes forty minutes and it is the step that separates a plan from a form that has been filled in.

12. **Register it, timestamped, before collection or before outcomes are seen.** Record the registry, the identifier and the date, and put all three in the paper.

## The specificity test, applied

The two-analysts test is abstract until it is run against real phrasings. These are the ones that fail most often, with the repair.

| What the draft says | Why it fails | What replaces it |
| Standard demographic controls | Not a specification; permits addition and removal later | Age in years, sex recorded as in the register, years of education, household size, region fixed effects |
| Several measures of wellbeing | Permits choosing the one that works | Primary: the five-item index defined below. Secondary: each item separately |
| Outliers will be excluded | The threshold is chosen after seeing the distribution | Observations with reported hours above 90 per week, a value inconsistent with the contract field |
| We will control for baseline where available | Availability is not defined and may correlate with treatment | Baseline value included; observations missing baseline retained with a missing indicator |
| We expect an effect on employment | No direction, cannot fail | We expect employment in month 12 to be higher in the treated arm |
| Robust standard errors | Robust to what, and clustered at which level | Standard errors clustered at the office level, 74 clusters, because assignment is at the office |
| Subgroup analyses will be conducted | Any subgroup, discovered later | Two subgroups, named: under 30 at baseline, and no prior claim history. Both predicted positive |
| If the main outcome shows no effect we will investigate | Investigation is undefined and outcome-dependent | Named as exploratory in advance, with the questions listed |

## Multiple comparisons without theatre

Two errors are common and they pull in opposite directions.

The first is silence: twelve hypotheses tested at the five percent level with no correction and no acknowledgement, which produces roughly one false positive by construction and a paper built around it.

The second is over-correction applied indiscriminately, which makes an adequately powered study unable to detect anything and is often a sign the plan has too many primary outcomes rather than too few corrections.

The workable approach: define families. The single primary outcome sits alone and is not corrected, which is the reason for insisting on one. Secondary outcomes form a family and are corrected within it. Exploratory analyses are not corrected and are not presented as tests. State the correction method by name and state which family it applies to.

Where a study has several arms, say whether each arm is compared with control only, or with each other as well, because that choice changes the number of comparisons and it is easy to make silently after seeing which contrast is largest.

## Registration, timing, and existing data

Register in a public timestamped repository appropriate to the field, before collection begins. Note the registry, the identifier and the date in the paper itself, not only in a cover letter, so a reader can check without asking.

Where the field supports registered reports, in which the design is peer reviewed before data collection and acceptance does not depend on the result, consider that route seriously. It is the strongest available protection against the file drawer and it changes what can be published when the answer is null, which for a doctoral student with one shot at a chapter is not a small consideration.

For analysis of data that already exists, the plan is still worth writing and the disclosure requirement is absolute. Write what has been seen, by whom, when, and at what level of detail. Three routes are available and the plan must say which is being used. First, register before requesting or accessing the outcome variables at all, which is clean and requires planning ahead with the data provider. Second, split the sample, explore in a holdout and register the confirmatory analysis for the remainder, stating the split rule and the seed. Third, register with a full exploration log and describe the analysis as a preregistered analysis of previously examined data, which is weaker and is still far better than nothing, provided nobody describes it as more than it is.

A preregistration written after exploration and presented as though written before is not an imprecision. It is misconduct, and the timestamp makes it discoverable.

## Worked example

**Situation.** Dr Yusuf Baran, a postdoctoral researcher at the Verrell Institute for Social Research, had funding to field a survey experiment on public support for a proposed housing density reform. The design had three arms: a control vignette, a vignette emphasising local affordability, and a vignette emphasising construction jobs. Fielding was booked with a panel provider for six weeks' time, and the funder required a registered analysis plan before the money was released. The budget covered 3,000 completed responses.

**Task.** A registered plan specific enough that the analysis could be run by someone else, submitted to the funder in ten days.

**Action.** The first draft failed the two-analysts test in four places and two of them changed the study rather than the document.

The first was the outcome. The draft named five primary outcomes: support for the reform on a seven-point scale, willingness to sign a petition, a feeling thermometer towards developers, perceived fairness, and an open-text sentiment measure. All were described as central. Under step 4 this is not a plan, because with five primaries and three arms there are fifteen headline contrasts and one of them will be significant. The repair was to build a three-item support index defined in advance, specifying the items, the coding direction and the aggregation as the mean of standardised items, and to name that index as the single primary outcome. The petition measure and the thermometer became secondary. The open-text measure moved to exploratory, because its coding scheme did not exist yet and a coding scheme built after seeing responses cannot be confirmatory.

The second was power, and it nearly ended the study. The closest prior experiment reported framing effects on policy support of about 0.08 standard deviations. With 1,000 respondents per arm, a two-sided test at the five percent level and eighty percent power, the minimum detectable effect between two arms was roughly 0.13 standard deviations. The study was therefore unable to detect the effect the literature would lead one to expect, and would have produced a null that meant nothing.

The wrong turn here is worth naming precisely. The first response was to assume a larger effect on the grounds that the vignettes in this study were stronger than in the prior work, and to write 0.15 standard deviations into the plan as the assumed effect. That is reverse-engineering the assumption from the affordable sample, and it is the most common way a power section becomes fiction. It was abandoned after a colleague asked the obvious question: what evidence supports 0.15. There was none.

The repair was structural. A fourth arm, which had been included out of interest rather than necessity, was cut, redistributing the sample across three arms at 1,600 each. Pre-specified covariate adjustment on three baseline variables collected before the vignette was added, which the prior literature suggested would absorb enough variance to matter. Together these moved the minimum detectable effect to roughly 0.10 standard deviations. The plan stated openly that effects below 0.10 would not be detectable and that a null would be interpreted as evidence against effects larger than that, not as evidence of no effect.

The third repair was exclusions. The draft said inattentive respondents would be excluded. The plan replaced this with a rule: respondents failing two or more of three attention checks, with the checks and their correct answers written into the appendix, plus respondents completing the survey in under a third of the median completion time from a soft launch of 200 responses. The plan committed to reporting the primary result both with and without exclusions.

The fourth was subgroups. The draft mentioned that heterogeneity by tenure would be examined. Two subgroups were named instead, renters and owners, with the predicted direction stated as a larger affordability-frame effect among renters, and everything else about heterogeneity was moved to exploratory.

**Result.** The plan was registered eleven days before fielding, with the identifier recorded. The affordability frame moved the primary index by 0.14 standard deviations, significant, and the jobs frame by 0.03, not distinguishable from zero. The renter subgroup showed the predicted larger effect.

Two deviations occurred and both went into the deviations table. The panel provider delivered 4,712 rather than 4,800 completes, and one attention check turned out to be ambiguously worded, so the rule was applied on the remaining two checks with the change documented and the original rule also reported. Neither changed the conclusion, and a referee said the deviations table was the reason they trusted the rest of the paper.

The plan cost about three days of work. Cutting the fourth arm was the decision that made the study answerable, and it was made only because the power calculation was done honestly under step 6.

### A second scenario, where it goes differently

A doctoral student at the same institute wanted to preregister an analysis of an existing national longitudinal survey, examining whether a change in disability benefit assessment affected labour market exit. The data had been in her possession for nine months and she had run descriptive tabulations and two exploratory regressions on the outcome.

Everything about the method survives except step 12, and the difference is decisive.

The plan opened with a disclosure paragraph: which waves had been accessed, which variables examined, that two regressions of exit on the reform indicator with year fixed effects had been run in March, and what those had shown, which was a coefficient of the expected sign that was not significant. Writing that paragraph was uncomfortable and it is the reason the rest of the document is worth anything.

The sample split route was chosen. The survey covered eleven regions; five were designated as the exploratory sample and the remaining six as the confirmatory sample, with the split defined by a stated rule rather than at random so that it could not be re-drawn. The exploratory work already done was declared as applying to the whole sample, which weakened the split, so the plan stated that the confirmatory analysis was quasi-confirmatory and described exactly why.

Power ran differently too. With existing data the sample is fixed and the only honest exercise is the minimum detectable effect at the sample available, which came out at 1.8 percentage points against a literature effect of about 1 point. The plan said so and reframed the contribution: the study could rule out effects larger than 2 points, which was itself useful because the policy debate had assumed effects several times that size. Reframing the contribution around what the data can establish is the move that rescues an underpowered study, and it is only available if the power calculation is done before the results are known.

What did not change: one primary outcome, numeric exclusion rules, the specification written as an equation, named subgroups, a stated null criterion, and a promised deviations table.

## Output

```
PRE-ANALYSIS PLAN
Title:           [study]
Authors:         [names, roles]
Registry:        [name]          ID: [identifier]        Registered: [date]
Data status:     [not yet collected / collected, outcomes not accessed / existing, see disclosure]
Design source:   [link or reference to the design document]

DISCLOSURE (existing data only)
[What has been seen, by whom, when, and what it showed. Route chosen: pre-access / sample split / logged exploration.]

QUESTION AND DESIGN
[One sentence, then one paragraph: what varies, assignment, unit of treatment, unit of analysis, timing of measurement.]

HYPOTHESES
| # | Hypothesis | Direction | Confirmatory or exploratory | Outcome it uses | Exhibit |

OUTCOMES
Primary:         [one, with full construction rule: items, coding, aggregation]
Secondary:       [listed, with construction rules]
Exploratory:     [listed, labelled]

SAMPLE AND EXCLUSIONS
Population, frame, recruitment, target N, realised N.
| Exclusion rule, numeric | Expected share | Reported also without exclusions? |

POWER
Assumed effect: [value] from [source]. Alpha: [ ] Power: [ ] ICC: [ ]
MDE at realised N: [value]. If the true effect is below this, the study cannot detect it.

SPECIFICATION
[Equation, all terms defined. Covariates listed by name. Fixed effects listed.]
Estimator:       [ ]        Missing data: [rule]
Standard errors: [clustered at ___, n clusters ___] because [reason]
Headline spec:   [named now]

MULTIPLE COMPARISONS
Families: [primary alone / secondary family / exploratory uncorrected]
Correction: [method] applied to [family], because [reason].
Named subgroups: [each, with predicted direction]

INTERPRETATION RULES
Supported if:    [ ]
Disconfirmed if: [ ]
Inconclusive if: [ ]

DEVIATIONS
The paper will contain a table of every departure from this plan: what changed, when,
why, and what the preregistered version would have shown.
```

## Failure modes

**Several outcomes and no primary.** Recognise it because every outcome is described as central. It permits choosing afterwards. Fix by naming one, or by building a pre-specified index and naming the index.

**The reverse-engineered power calculation.** Recognise it when the assumed effect size has no source and happens to be exactly detectable at the affordable sample. Fix by sourcing the effect from prior work or from a practical threshold, computing the minimum detectable effect honestly, and changing the design or the claim.

**Controls described as a category.** "Standard controls", "the usual covariates", "demographics". Fix by listing every variable by name.

**Exclusions decided once outcomes are visible.** Recognise it because the rule appears in the paper and not in the plan. Fix by writing numeric thresholds in advance and reporting the result without exclusions as well.

**Undirected hypotheses.** Recognise them because no result could contradict them. Fix by stating the sign, or by declaring the test two-sided and saying why theory gives no direction.

**Subgroups introduced after the main result disappoints.** The most damaging pattern in applied work because it is almost invisible. Fix by naming subgroups in advance and treating everything else as exploratory in print.

**Silence about what a null would look like.** Recognise it when the interpretation section only describes success. Fix with step 9 and its three outcomes.

**The plan so long nobody reads it.** Forty pages of contingencies is a different way of hiding the decisions, because the referee cannot check compliance. Fix by keeping the plan to the fields above and putting instrument text and code in an appendix.

**The plan and the paper diverging silently.** Recognise it when the paper's specification differs from the registered one and nothing says so. Fix with the deviations table, which is why it is promised at registration rather than considered at submission.

**Registering the wrong thing.** A registration listing hypotheses that were never the point, filed to satisfy a funder, while the real analysis proceeds unconstrained. Fix by writing the plan for the analyst, not for the form.

## Edge cases

**Data already collected and partly explored.** Disclose fully, choose one of the three routes, and describe the resulting plan at its true strength. Never call a quasi-confirmatory analysis confirmatory.

**Pilot data exists.** A pilot used for power calculation and instrument refinement is fine and should be described. A pilot used to select which outcome to make primary makes that selection exploratory, and the plan should say so.

**Adaptive or sequential designs.** Legitimate, and they require the stopping rule, the interim analysis timing, and the alpha spending approach to be specified in advance. The rule is that any flexibility must be a rule, not a judgement.

**The intervention changes during fielding.** Common in field experiments run with partner organisations. Document the change with its date, state which units were exposed to which version, and preregister an amendment before looking at outcomes. Amendments are visible in most registries and that visibility is the point.

**Qualitative and mixed-methods studies.** Preregistration adapts rather than transfers. What can be committed in advance: the sampling and recruitment strategy, the interview or observation protocol, the coding framework's starting categories, the analytic approach, and the stopping rule for data collection. What cannot: the codes that emerge. Register the first list and label the second as emergent, which is honest and is what the tradition actually requires.

**A registry with a rigid template that omits something important.** Fill the template and attach the full plan as a document, so the timestamp covers the real plan and not only the fields.

**The result is already known because the data is public and the analysis has been done by others.** A preregistration cannot restore ignorance. Write the study as a replication with a stated improvement, register it as such, and say what was known at registration.

**No plan was written and the analysis is complete.** Do not write one now. Report the analysis as exploratory, include a full specification curve or robustness appendix showing the choices that were available, and state clearly which decisions were made after seeing results. `analysis-audit` handles this.

## Quality bar

- Written and timestamped before outcomes are seen, with any prior exploration disclosed in the document itself.
- One primary outcome, named as primary, with its construction rule complete enough to compute from raw data.
- Every hypothesis is numbered, directional where theory allows, and labelled confirmatory or exploratory.
- The specification is an equation with every covariate named, the estimator stated, and the clustering level justified with a cluster count.
- Every exclusion is a numeric rule requiring no judgement, and the plan commits to reporting results without exclusions.
- The power calculation states its assumed effect size and its source, and the minimum detectable effect is compared against a published effect.
- The multiple comparison families and every subgroup are named in advance.
- What would count as a null and what would count as inconclusive are both written down.
- A deviations table is promised in the plan itself.

## Related skills

`research-design` produces the design this plan hardens and should always run first. `research-ethics-and-data-protection` runs in parallel on a longer timetable and gates fielding. `survey-and-instrument-design` supplies the instrument whose items the primary outcome is built from. `econometric-model-writer` turns the registered specification into the paper's methods prose. `analysis-audit` checks a completed analysis against the plan and is also the right skill when no plan exists. `replication-package` delivers the code and data that let someone else verify the plan was followed. `identification-defense` handles the threats to the design that a plan records but does not argue.
