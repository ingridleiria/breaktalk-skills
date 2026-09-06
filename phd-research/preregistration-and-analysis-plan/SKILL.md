---
name: preregistration-and-analysis-plan
description: Writes a preregistration or a pre-analysis plan that is specific enough to constrain the analysis rather than to decorate it: the hypotheses with their directions, the primary outcome named as primary, the exact specification including controls and fixed effects, the sample and exclusions defined before seeing outcomes, how multiple comparisons and subgroups are handled, what counts as success or failure, and how deviations will be reported. Use this skill when preregistering a study, writing a pre-analysis plan for a trial or an experiment, preparing a registered report, responding to a funder or ethics requirement for an analysis plan, or when someone asks how to avoid specification searching.
---

# Preregistration and Analysis Plan

A preregistration is a promise made before the data can influence the promise. Its value is entirely in its specificity: a plan vague enough to accommodate any result constrains nothing and is worse than none, because it claims a credibility it has not earned.

The test to apply to every line: could two competent analysts, reading this and handed the same data, produce different results? If yes, the line is not specific enough.

## Write it before

Before outcome data is collected, or before outcomes are looked at where data already exists. Where the data exists and has been partly explored, say so plainly and describe exactly what has already been seen. A preregistration written after exploration, presented as if written before, is misconduct rather than an imprecision.

## What it must contain

**The question**, as one sentence, and why it matters.

**The hypotheses**, numbered, each with a direction where theory implies one, each stated as something that could be false. Distinguish confirmatory hypotheses, which are being tested, from exploratory questions, which are being looked at. Exploratory work is legitimate and must be labelled, and its results reported as exploratory in the paper.

**The design**: what varies, how assignment happens, the unit of treatment and the unit of analysis, and the timing of measurement.

**The sample**: the population, how units are selected, the target size, and the power calculation with its assumed effect size and where that assumption comes from. A power calculation reverse-engineered from the sample you can afford should be described as such.

**Exclusions**, defined before outcomes are seen: which observations will be dropped and on what rule. This is where most silent specification searching happens.

**The variables**: the primary outcome, named and singular; secondary outcomes, listed; how each is constructed from the raw measures; and the covariates that will be included, distinguishing those in the main specification from those in robustness checks.

**The specification**, written as an equation with every term defined, the estimator, the standard error treatment including the clustering level and its justification, and how missing data will be handled. Say which specification is the headline result before you know what any of them show.

**Multiple comparisons.** How many hypotheses are tested, and the correction applied or the reason none is needed. Any subgroup analysis is named in advance, because subgroups discovered afterwards are exploratory whatever the p-value says.

**What counts as support**, in advance. What result confirms the hypothesis, what disconfirms it, and what would be inconclusive. A plan with no possible disconfirming result is not a test.

**Deviations.** How any departure from the plan will be reported: a table in the paper listing what changed, when, why, and what the preregistered version would have shown. Say now that this table will exist, because deciding later is deciding under pressure.

## Common failures

A hypothesis with no direction, which cannot fail. Several outcomes with no primary, which permits choosing afterwards. Controls described as "standard demographic controls", which is not a specification. Exclusions decided once the outcomes are visible. Subgroups introduced after the main result disappoints. Silence about what would count as a null. And a plan so long nobody reads it, which is a different way of hiding the decisions.

## Registration

Register in a public timestamped repository appropriate to the field, before collection begins. Note the registry, the identifier, and the date in the paper. Where the field supports registered reports, in which the design is peer reviewed before data collection and acceptance does not depend on the result, consider that route; it is the strongest available protection against the file drawer and it changes what you are able to publish when the answer is null.

## Quality bar

- Written and timestamped before outcomes are seen, with any prior exploration disclosed.
- Every hypothesis is directional where theory allows and could be disconfirmed.
- One primary outcome, named as primary.
- The specification is an equation with defined terms, a stated estimator, and a justified clustering level.
- Exclusions and subgroups are defined in advance.
- The multiple comparison approach is stated with its reasoning.
- What would count as a null result is written down.
- A deviations table is promised in the plan itself.
