---
name: econometric-model-writer
description: Writes the empirical strategy or methods section of a paper or thesis chapter: the estimating equation in correct notation, every term defined, the parameter of interest named, the identifying assumption stated in words before symbols, the threats and what is done about each, the inference and clustering choice, and matching estimation code. Covers OLS, panel fixed effects, difference-in-differences including staggered adoption, event studies, instrumental variables, regression discontinuity, matching, and multilevel models. Use this skill whenever a researcher asks to write the methods, empirical strategy, identification, or estimation section, asks "what does beta identify", "write the equation for my design", "explain my specification", or needs the model section for a proposal. Trigger for any academic text that must state how an effect is estimated.
---

# Econometric Model Writer

The methods section has one reader in mind: the referee who will decide whether the coefficient means what the paper says it means. It succeeds when the equation is unambiguous, the assumption is stated in plain words before any symbol, and the threats are named by the author before the referee names them.

## Section architecture

Write in this order, in prose with equations set apart, no bullets:

1. **The design in one paragraph, in words.** What varies, across which units, over what time, and why that variation identifies the effect. A reader should understand the strategy before seeing an equation.
2. **The estimating equation**, numbered, with every symbol defined immediately after: the outcome and its unit, the treatment variable and how it is measured, the fixed effects and what each absorbs, the controls and why they are included (or why they are not), the error term, and the subscripts for unit and time. The parameter of interest is named explicitly: "the coefficient of interest is β, which measures...".
3. **The identifying assumption in words**, then, where useful, in notation. For each design the assumption has a name and a plain-language meaning; write both. Then state what would violate it in this setting specifically, not generically.
4. **Threats and responses**: the two to four most credible threats to the assumption in this setting, each followed by the diagnostic or design feature that addresses it and the exhibit where the reader will find it. Threats without responses are honest and allowed; they become limitations.
5. **Inference**: the clustering level and the reason (the level at which treatment is assigned or errors are plausibly correlated), the number of clusters, and any small-cluster correction. State whether standard errors are heteroskedasticity-robust and why.
6. **Estimation details**: estimator and software, weights, sample used, treatment of missing values, standardization of outcomes, and any two-step or bootstrapped procedure.

## Design-specific requirements

- **Panel fixed effects**: state what within-variation identifies the effect and what time-invariant confounders are absorbed; acknowledge that time-varying confounders are not.
- **Difference-in-differences**: parallel trends stated for this outcome and these groups; with staggered adoption, state why two-way fixed effects may be biased under heterogeneous effects and which modern estimator is used (for example, Callaway and Sant'Anna, Sun and Abraham, de Chaisemartin and D'Haultfœuille, or Borusyak, Jaravel and Spiess), with the comparison group defined (never-treated or not-yet-treated). Event-study specification written out with the reference period and the binning of endpoints.
- **Instrumental variables**: relevance and exclusion stated separately; exclusion defended with an argument specific to the setting; first-stage strength reported with a modern weak-instrument statistic; the estimand named as a LATE and the complier population described.
- **Regression discontinuity**: running variable, cutoff, bandwidth selection method, kernel, polynomial order, bias correction, and the manipulation and covariate continuity tests; sharp versus fuzzy stated.
- **Matching and reweighting**: the selection-on-observables assumption stated as an assumption, the covariate set justified, the balance diagnostic named, and the estimand (ATT or ATE) stated.
- **Multilevel models**: the nesting structure, which effects are random, and why a multilevel model rather than fixed effects and clustering.

## Notation rules

- One consistent notation throughout the paper: i for units, t for time, and design-specific indices introduced once.
- Greek letters for parameters, Latin for variables, bold only for vectors.
- Every equation numbered and referenced by number in the text.
- Subscripts on every variable that varies; a variable written without subscripts is a claim that it is constant.

## Citations

Method citations for estimators and tests are required and follow the literature-verification skill's standard: every cited method paper verified against a real record. Do not cite an estimator paper from memory.

## Matching code

Provide the estimation command for the user's software (Stata by default, R or Python if requested) that implements exactly the equation written, with the same fixed effects, controls, clustering, and sample. The code and the equation must agree; a mismatch between them is the most common methods-section error.

## Quality bar

- A referee can reproduce the specification from the text alone.
- The identifying assumption is stated in words, specific to the setting, before any notation.
- Every threat named has a response or is carried explicitly into the limitations.
- The code implements the written equation exactly.
