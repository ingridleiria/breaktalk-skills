---
name: identification-defense
description: Stress-tests and defends the identification strategy of an empirical paper (difference-in-differences, event studies, instrumental variables, regression discontinuity, matching, synthetic control) as a committee member or referee would, then builds the argument and the diagnostics that answer each attack. Use this skill whenever a researcher asks "is this identified", "defend my DiD", "will reviewers accept this instrument", "what will the committee ask about identification", "attack my design", "parallel trends", "exclusion restriction", "is this a valid instrument", or is preparing for a defense, a seminar, or a submission where the design will be questioned. Trigger before any paper is sent to a supervisor or journal and whenever a design decision is being made.
---

# Identification Defense

A design is credible when its author has already asked every question the referee will ask and has a written answer or an honest concession for each. This skill runs the attack first, then builds the defense, and refuses to decorate a design that cannot be defended.

## Step 1: State the design precisely

Before attacking, restate the design in five lines: the outcome, the treatment and how it is assigned, the source of variation, the comparison group, and the estimand (ATT, LATE, a local effect at a cutoff). If any of these cannot be stated, the problem is upstream; return to research-design.

## Step 2: The attack, by design

Ask every question below that applies, in the voice of a demanding but fair referee, and record the answer as strong, adequate, weak, or missing.

**Difference-in-differences and event studies**
- Why would treated and comparison units have moved in parallel absent treatment, in this specific setting? What could make them diverge (differential shocks, policy bundling, mean reversion, selection into treatment timing)?
- Do pre-period coefficients show no trend, and is the test powered enough for a flat pre-trend to mean anything?
- With staggered adoption, is a two-way fixed effects estimator used, and if so, why is negative weighting under heterogeneous effects not a concern? Which modern estimator is reported, and does it agree?
- Is the comparison group never-treated or not-yet-treated, and does the choice change the estimate?
- Are there anticipation effects? Spillovers from treated to comparison units? Compositional changes in the sample around treatment?
- What is the sensitivity of the conclusion to plausible violations of parallel trends (bounding approaches)?

**Instrumental variables**
- What is the argument that the instrument affects the outcome only through the treatment, specific to this setting? Which alternative channels exist and how are they closed?
- First-stage strength by a modern statistic, not a rule of thumb; with many instruments or heteroskedasticity, which test?
- Is monotonicity plausible: can there be units that the instrument pushes the other way?
- Who are the compliers, and does the LATE answer the paper's question or a different one?
- Is the instrument itself as-good-as-randomly assigned conditional on controls? What balance evidence supports this?

**Regression discontinuity**
- Can the running variable be manipulated around the cutoff? What does the density test show?
- Are covariates continuous at the cutoff?
- How sensitive is the estimate to bandwidth, kernel, and polynomial order?
- Is the effect local to the cutoff, and does the paper claim more than that?
- For fuzzy designs, is the first stage at the cutoff strong?

**Matching, reweighting, and selection on observables**
- Why is selection on observables plausible here, given that the treated units chose treatment?
- Which unobservables would the referee name, and what evidence bounds their influence (sensitivity analysis, coefficient stability)?
- Is there common support, and what happens to the estimate off support?

**Synthetic control**
- Is the donor pool clean of treated or contaminated units?
- How good is the pre-treatment fit, and how do placebo-in-space and placebo-in-time inferences look?

**All designs**
- Is the clustering level the level of treatment assignment, and are there enough clusters?
- Is the outcome measured the same way in treated and comparison groups and over time?
- Is the sample selected in a way related to treatment (attrition, endogenous entry)?
- What is the minimum detectable effect, and can the design distinguish the estimated effect from zero and from economically meaningful alternatives?

## Step 3: Build the defense

For each question answered weak or missing, one of three responses:

1. **A diagnostic or robustness exhibit** that addresses it, specified precisely (which test, which table, which figure), added to the paper's plan.
2. **An argument** specific to the setting, written as a paragraph the methods or results section can carry.
3. **A concession**, written for the limitations section in plain words, with the direction of the likely bias stated.

The output is a table: question, current answer, strength, response, and where it lives in the paper.

## Step 4: The verdict

State plainly whether the design is defensible at the venue targeted, what must be added before submission, and, if the honest answer is that the design does not identify the effect, say so and propose the closest question the data can answer.

## Conduct

- Be adversarial in the questions and constructive in the responses.
- Cite method papers only through the literature-verification standard; never from memory.
- Do not accept vocabulary as evidence: naming an estimator is not defending an assumption.
- Prepare the user to answer these questions aloud when the purpose is a defense or seminar: short answers, the exhibit to point to, and the concession stated first rather than extracted.
