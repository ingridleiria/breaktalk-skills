---
name: results-writing
description: Turns estimation output into the results section of a paper or thesis chapter: written against the finished exhibits, organised by hypothesis rather than by table, with every magnitude translated into interpretable units, causal verbs calibrated to what the design supports, precision reported as intervals rather than stars, and nulls reported as findings with the effect sizes the design can rule out. Enforces that every hypothesis is adjudicated, every number traces to a table cell, and every exhibit is used. Use this skill when someone asks to write up results, interpret a coefficient, describe a regression table, report effect sizes, handle a null or an unexpected result, or says "my results section is just a list of tables", "what does this coefficient mean", "is this effect large", "am I overclaiming", "the reviewer said the results are hard to follow". Trigger for any task converting estimation output from Stata, R or Python into academic prose.
---

# Results Writing

The commonest results section in a doctoral drawer is a tour of the tables. Column one adds controls, column two adds fixed effects, column three clusters differently, and each paragraph narrates a table row by row. It is accurate, it took a week, and it does not tell the reader what the paper found. A referee reading it writes that the results are difficult to follow, which is a polite way of saying the author has not decided what the argument is.

Three failures ride along with it, and each is more expensive than the first. Coefficients get reported without being translated, so nobody, including the author, knows whether 0.086 is a large effect or a rounding artefact of no consequence. Causal verbs drift upward: the strategy section concedes selection on unobservables, the results section says "increases", and by the abstract it says "causes". And nulls get buried under robustness checks hunting for a specification with stars, which is both visible to referees and, when it succeeds, worse than the null would have been.

The cost is not only rejection. A results section that does not commit to a finding cannot be defended in a viva, cannot be summarised by anyone else, and cannot be turned into an abstract, which is why authors who skip this discipline end up rewriting the whole paper from the results outward anyway.

The section is written fourth in the manuscript order, directly against exhibits that already exist and will not change, and immediately before `discussion-and-conclusion`.

## When to use this, and when not to

Use it to draft a results section from finished exhibits, to restructure one that reads as a table tour, to write up a null result, to translate coefficients into interpretable magnitudes, to report heterogeneity or mechanism evidence, and to check whether the language in a draft matches the design.

Use it also when a supervisor or referee says the results are hard to follow, since that comment is almost never about the prose and almost always about the organisation.

Do not use it to build the exhibits, which is `academic-tables-booktabs` for regression tables, `descriptive-statistics-tables` for the sample and balance tables, and `academic-figures-monochrome` for figures. The exhibits exist before this section is written; prose written against provisional numbers is written twice.

Do not use it to interpret the finding at the level of the question, compare with prior estimates, state limitations or draw implications; that is `discussion-and-conclusion`, which is written immediately after this and which is where meaning belongs. Where the target journal merges results and discussion, write both sections separately and then merge, because merging first is how causal language inflates.

Do not use it to defend the identification against a specific attack, which is `identification-defense`, or to state the model and its assumptions, which is `econometric-model-writer` and belongs in the preceding section. Do not use it to rescue a design: no results prose repairs an unidentified estimate, and attempting it produces the overclaiming this skill exists to prevent.

## What you need before starting

**The final exhibits, numbered and frozen.** Tables and figures in the form they will be submitted in. Missing: build them first. This is not a preference; every number in the section is read off an exhibit, and if the exhibits move, the section is rewritten.

**The hypotheses, in the order the paper tests them.** From `research-design`. They are the section's architecture: each one gets its paragraph or its subsection, and each is adjudicated. Missing: reconstruct them from what the exhibits test, in writing, and get the author to confirm. If the paper genuinely has none, see the edge case below; do not write around it.

**The estimand and the units.** What the coefficient is the effect of, on whom, measured in what. Missing: derive it from the specification and state it explicitly in the first paragraph. A section that never says what population the estimate applies to invites the referee to assume the widest one and then object.

**The translation quantities.** The outcome mean and standard deviation, the treated share, the baseline level, and any monetary or time equivalent needed to make magnitudes legible. Missing: compute them from the analysis sample, not from the raw data, and note where they came from.

**The design and its diagnostics.** Which design, which assumption, which diagnostic exhibit. Missing: read the strategy section; if it does not name a key assumption and a diagnostic, the problem is upstream in `econometric-model-writer` or `research-design`.

**What was preregistered or planned, and what was not.** Missing: ask directly. It decides which results are confirmatory and which are exploratory, and that distinction has to be stated rather than implied. Reconstructing it after the fact is not possible, so the honest move when nobody can say is to label the heterogeneity results exploratory.

**The journal's conventions.** Whether results and discussion are merged, whether stars are used, how many decimal places, whether confidence intervals are expected in text. Missing: take them from three recent articles in the target.

## The method

1. **Lay out the section against the hypotheses, before writing prose.** One line per hypothesis, with the exhibit that tests it and the outcome in three words: supported, not supported, mixed. This outline takes ten minutes and is the difference between a results section and a table tour. It also exposes, immediately, any hypothesis with no exhibit and any exhibit testing no hypothesis.

2. **Open with the answer.** The first paragraph states the headline result with its magnitude in interpretable units, its precision, and its exhibit, and it answers the research question in the paper's own words. Readers and referees form their view here. Building to the finding across four paragraphs is a structure borrowed from mystery writing and it does not work in journals.

3. **Write the estimate sentences to the anatomy below.** Direction, magnitude in interpretable units, precision, exhibit, and the translation that makes the magnitude mean something. Do the arithmetic of the translation explicitly the first time, so the reader can check it, and use the same translation consistently afterwards.

4. **Walk the specifications only where movement is informative.** Sparse to full, saying what each addition tests and what the stability or movement of the coefficient means. The rule: if the estimate is stable across columns, one sentence covers it; if it moves, that movement is a finding about confounding and gets a sentence explaining what the added variables absorbed. Narrating six columns that all say the same thing is padding, and narrating away a coefficient that halves when controls enter is the opposite failure.

5. **Report the identification diagnostics as tests that could have failed.** Pre-trends for difference-in-differences, first-stage strength for instrumental variables, density and covariate smoothness at the cutoff for regression discontinuity, balance for matching. Give the number, not the verdict alone. "The pre-treatment coefficients are individually and jointly insignificant, with a joint p value of 0.62 and point estimates within 0.02 standard deviations of zero" is a diagnostic; "parallel trends holds" is an assertion.

6. **Report heterogeneity and mechanisms only where a hypothesis predicted them**, and label anything else exploratory in the sentence that reports it, not in a footnote. The rule for subgroups: a subgroup result is confirmatory only if it was specified before the estimates were seen. Everything else is a hypothesis for the next paper, and saying so costs one clause and buys the referee's trust for the whole section.

7. **Summarise robustness in prose and put the full set in an appendix.** State what was varied and the range the estimate moved within: "across eleven specifications varying the bandwidth, the control set and the clustering level, the estimate ranges from 0.061 to 0.094 standard deviations, and remains significant at the five percent level in all but the narrowest bandwidth". That sentence is a robustness section. "Results are robust to alternative specifications" is not, and a referee will assume the worst about what it conceals.

8. **Adjudicate every hypothesis explicitly, including the ones that failed.** Each hypothesis gets a sentence saying what the evidence did to it. A hypothesis stated in the framework and quietly dropped in the results is the single easiest thing for a referee to catch, and it reads as selective reporting even when it was an oversight.

9. **Calibrate every verb to the design, in one dedicated pass.** Read only the verbs attached to the estimates. Credible causal designs get "increases", "reduces", "raises". Everything else gets "is associated with", "predicts", "is higher among". Do not upgrade in the last paragraph, where it happens most often, and do not let a hedge in the results become a claim in the discussion.

10. **Trace every number.** Build the trace table in the output block: number as written, value, exhibit and cell. Ten minutes, and it catches the rounding mismatches and the stale figures that survive into print.

11. **Read the section without the tables.** If the argument does not survive, the prose is leaning on the exhibits to do work it should be doing. If the tables are never needed, the section is over-explaining and can be cut.

## The sentence that reports an estimate

The unit of results writing is one sentence carrying five things. A working template:

"The fee cap raised maternal employment by 2.1 percentage points (95 percent CI 0.8 to 3.4; Table 3, column 4), an increase of about 3.4 percent on a pre-reform base of 61.3 percent, and roughly a third of the gap between the highest and lowest employment quintiles of municipalities."

The parts, and the rule for each:

**Direction and verb.** Calibrated to the design. The verb is a claim about causality and it is the most consequential word in the sentence.

**Magnitude in interpretable units.** The raw coefficient alone is not a result. Convert to percent of the baseline mean, standard deviations, a percentile move, a monetary amount, or a comparison the reader already understands. Show the arithmetic once so the conversion can be checked.

**Precision.** Prefer the confidence interval to the star. Stars compress the information a reader needs into a categorical judgement made at an arbitrary threshold, and they make a precisely estimated zero look like a failure. Where the journal expects stars, give them and give the interval too.

**The exhibit, to the column.** Table and column, or figure and panel. "See Table 3" makes the reader search.

**A comparison that makes the size legible.** One per major result. This is the sentence readers quote back to you, and it is what separates a results section from a printout.

Two rules hold across all of them. Statistical and economic significance are different sentences: a precisely estimated tiny effect and a large imprecise one are both worth describing honestly, and neither description is supplied by a star. And every number in the text matches the exhibit exactly, at the same rounding, document-wide.

## Reporting a null honestly

A well-identified null is a finding, and in a literature full of small underpowered positives it can be the most useful paper of the year. Reported badly it looks like a failed project.

Report the interval and what it excludes: "the estimate is 0.004 standard deviations with a 95 percent confidence interval of minus 0.031 to 0.039, ruling out effects larger than about 0.04 standard deviations, well below the 0.12 reported in the closest prior study". State the minimum detectable effect at conventional power for the realised sample, so the reader can distinguish a precise zero from an uninformative one. Then say which of the two this is, in plain words.

What not to do: describe an insignificant estimate as "positive but not statistically significant", which invites the reader to treat it as a small win; run additional specifications until one crosses a threshold and report that one as the result; or bury the null in a robustness paragraph. Where a null contradicts the hypothesis, `discussion-and-conclusion` engages it directly, and the results section's job is to state it cleanly with the interval.

## Worked example

**Situation.** Dr. Priya Raman had eight exhibits and a stable set of estimates for a paper on a municipal childcare fee cap and maternal employment, using a staggered adoption design across 214 municipalities from 2012 to 2021. Her draft results section was 2,900 words in seven paragraphs, one per table. Her coauthor's comment was that he could not tell which result was the paper.

**Task.** A results section of about 1,900 words that a referee could read once and restate correctly, organised so the three hypotheses from the design document were each visibly answered.

**Action.** The outline came first. H1, the fee cap raises maternal employment, tested by Table 3. H2, the effect is concentrated among mothers of children under three, tested by Table 5 and Figure 2. H3, the mechanism is formal childcare take-up rather than substitution away from informal care, tested by Table 6. The outline immediately showed two problems: Table 4, a specification with an alternative control group, tested no hypothesis and belonged in the robustness appendix; and H3 had an exhibit but the exhibit had never been written about.

The wrong turn came in the first rewrite, and it was the one this method now guards against. The heterogeneity result in Table 5 was strong for mothers of children under three and there was also an unexpected result for single mothers, which was larger and had a small p value. The first draft reported the single-mother result in the main text alongside the predicted heterogeneity, in the same register, with a sentence speculating about liquidity constraints. It read well. It was also a subgroup nobody had specified in advance, found after the estimates were seen, in one of eleven cuts of the data. The coauthor caught it. In the final version it moved to a clearly labelled exploratory paragraph, with the number of subgroups examined stated, and it was reframed as a question for further work. The referee later cited that paragraph approvingly, which is not what anyone expected.

The opening paragraph was rewritten to lead with the answer: the cap raised maternal employment by 2.1 percentage points, 95 percent confidence interval 0.8 to 3.4, from a pre-reform base of 61.3 percent, an increase of about 3.4 percent. The translation was then used consistently, so the same effect was never expressed three ways.

The specification walk was cut from five paragraphs to one, because the estimate moved only from 2.3 to 2.1 across the columns. The one place it did move materially, when municipality-specific linear trends were added and the estimate fell to 1.6, got its own two sentences saying what that implied and pointing to the event study for why the trends specification was not the preferred one.

Diagnostics were reported with numbers: the event study showed pre-treatment coefficients within 0.6 percentage points of zero with a joint p value of 0.48, and that was stated rather than summarised as "no pre-trends".

Robustness went to one paragraph with the range: nine specifications, estimates from 1.6 to 2.6 percentage points, significant at conventional levels in eight of nine, with the exception named.

H3 was adjudicated as mixed: formal take-up rose by 4.9 percentage points, consistent with the mechanism, but the informal care measure was too noisy to rule out substitution, and that limitation was stated in the results and carried into the discussion rather than being smoothed over.

**Result.** 1,870 words, five paragraphs and two subsections, eight exhibits reduced to six in the body with two moved to the appendix. The coauthor's second reading produced no structural comments. In review, one referee disagreed with the interpretation of the mechanism, which is the argument the authors wanted to have, and neither referee said the results were hard to follow. The rewrite took about seven hours, of which two were the abandoned draft with the unlabelled subgroup.

### A second scenario, where it goes differently

The same design, the same author, and a null. A second paper on a related reform found an effect of 0.3 percentage points with a confidence interval of minus 1.1 to 1.7, and the temptation to write it as a smaller version of the first paper was strong.

The architecture changes at three points. The opening paragraph leads with the interval and what it rules out rather than with a point estimate, because the point estimate is not the finding. The power discussion moves from an appendix into the main text, immediately after the headline paragraph, since a reader cannot evaluate a null without knowing what the design could have detected; here the minimum detectable effect at 80 percent power was 1.9 percentage points, which is smaller than the effect found in the first paper, so the null is informative rather than merely quiet. And the comparison with prior estimates moves earlier, because the paper's contribution is that it excludes effects other studies reported.

The robustness paragraph also changes purpose. In the positive paper it defends a finding; here it demonstrates that the null is not an artefact of one specification, so it reports the full range of point estimates and shows that all of them sit inside an interval that excludes the prior literature's effect size. What does not change is the hypothesis-by-hypothesis architecture, the calibrated verbs, and the trace of every number to a cell.

## Output

The results section as prose, plus a trace block the author keeps and does not submit.

```
RESULTS
[Headline paragraph: the answer to the question, magnitude translated, interval, exhibit]
[Specification walk, only where movement is informative]
[Identification diagnostics, reported as tests with numbers]
[H2: predicted heterogeneity, with its exhibit]
[Mechanism evidence, with what it cannot rule out]
[Exploratory results, labelled as exploratory, with the number of cuts examined]
[Robustness in one paragraph: what varied, the range, the exceptions named]
[Hypothesis adjudication, explicit, including nulls]

TRACE (not submitted)
| # | Sentence in the text | Number as written | Exhibit and cell | Rounding checked |
| Hypothesis | Exhibit | Outcome (supported / not / mixed) | Where adjudicated |
Verb pass done:            [date]
Exhibits used in the text: [n of n]
```

## Failure modes

**The table tour.** Recognise it because paragraph breaks fall where table numbers change. Rebuild the outline against hypotheses, not exhibits.

**The untranslated coefficient.** Recognise it when the section contains numbers but no comparison a non-specialist could picture. Convert to a percentage of the baseline, a standard deviation, a percentile move, or money, and do the arithmetic once in the open.

**Verb drift.** Recognise it by reading only the verbs attached to the main estimate, in the results, the discussion and the abstract. Fix at the results, since that is where the discussion and the abstract will copy from.

**Stars doing the interpreting.** Recognise it when significance is reported and magnitude is not. Report the interval, and describe the size in words.

**Subgroup discovery presented as prediction.** Recognise it when a heterogeneity result appears in the main text and no hypothesis anticipated it. Label it exploratory, state how many cuts were examined, and move it after the confirmatory results.

**The buried null.** Recognise it when an insignificant main result is described in a subordinate clause or appears after two pages of robustness. Lead with it, give the interval, give the minimum detectable effect.

**Narrating away a moving coefficient.** Recognise it when an estimate halves between columns and the text says the results are broadly stable. Movement is evidence about confounding; explain it or concede it.

**Explaining a contradictory result rather than reporting it.** Recognise it when the results section contains speculation about why an estimate came out unexpectedly. Report the estimate here; the speculation, clearly labelled, belongs in the discussion.

**Reporting more decimal places than the estimate supports.** Recognise it in a coefficient with four decimals and a standard error of similar size. Match the precision to the exhibit, and match the rounding document-wide.

## Edge cases

**A paper with no hypotheses.** If nothing was predicted, there is nothing to adjudicate, and the section has no architecture except the tables. This does not meet the standard. Go back to `research-design` and state the question and the hypotheses, even retrospectively and honestly labelled as such, or reframe the paper as an explicitly exploratory study whose contribution is the pattern and whose claims are correspondingly weaker. A descriptive paper with no question and no model is not rescued by good prose.

**The design is weak and everyone knows it.** Write the results as associations, in those words, throughout, and say what would be needed to make them causal. A paper that reports associations honestly can be published; a paper that reports associations as effects usually cannot.

**Results that contradict the author's prior work.** Report the estimate, then in the discussion address the difference by design, sample and measurement rather than by preference. Referees who know the field will already have noticed.

**Multiple outcomes.** Where several outcomes are tested, either preregister a primary outcome or report a multiple-testing adjustment and say which one. Reporting six outcomes and discussing the two that reached significance is the most common form of the problem and the easiest to spot.

**Very small samples or few clusters.** Report the inference method used and why, and give the estimate under at least one alternative. Where clusters number fewer than about forty, say so at the point the standard errors are first reported rather than in a footnote.

**Qualitative or mixed evidence.** The architecture is unchanged: organised by proposition, with the evidence for each, its scope, and the negative cases. Magnitudes become counts and conditions, and the calibration rule applies to claims about mechanism rather than to causal verbs. `qualitative-coding-and-analysis` supplies the coded material and the agreement statistics.

**The journal merges results and discussion.** Write them separately, calibrate the verbs, then merge. Merging first is the most reliable way to produce an inflated section.

## Quality bar

- The first paragraph answers the research question with a translated magnitude and an interval.
- The section is organised by hypothesis, and every hypothesis is adjudicated in a sentence, including the failures.
- Every magnitude is translated into interpretable units, with the arithmetic shown once.
- Every verb attached to an estimate matches what the design supports, checked in a dedicated pass.
- Every number in the text traces to a specific exhibit cell at the same rounding, and every exhibit in the body is used by the text.
- Diagnostics are reported with their numbers, as tests that could have failed.
- Exploratory results are labelled where they are reported, with the number of cuts examined.
- Robustness states what varied and the range of estimates, never "results are robust".

## Related skills

`full-manuscript-build` places this section fourth in the writing order, after the data and strategy sections and immediately before the discussion, and it holds the largest share of the word budget. `research-design` supplies the hypotheses that organise the section. `econometric-model-writer` states the model this section estimates, and `identification-defense` handles a threat that needs more than a diagnostic paragraph. `academic-tables-booktabs`, `descriptive-statistics-tables` and `academic-figures-monochrome` build the exhibits this section is written against. `discussion-and-conclusion` takes the finding and interprets it, and must not strengthen the verbs. `abstract-and-title` takes its numbers from here. `peer-review-simulator` attacks the finished section the way a referee will.
