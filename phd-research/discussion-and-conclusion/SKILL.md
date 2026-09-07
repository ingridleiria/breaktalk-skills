---
name: discussion-and-conclusion
description: Writes the discussion and conclusion of a paper or thesis chapter immediately after the results, while the argument is still live: restating the finding at the level of the research question with a comparison a reader can picture, explaining the mechanism in the terms of the framework, comparing with prior estimates by number and by hyperlinked citation, adjudicating every hypothesis, stating limitations with the direction of bias and no reassuring clause, sizing implications to the estimand, and closing on the finding. Handles the conventions of economics, education and management, and the thesis chapter that must also close one chapter and open the next. Use this skill when someone asks to write the discussion, the conclusion, concluding remarks, the limitations section, policy or managerial implications, or says "my conclusion just repeats the results", "am I overclaiming", "how do I end this chapter", "the reviewer said the contribution is unclear", "what do I do with a result that contradicts my hypothesis".
---

# Discussion and Conclusion

Two failures live in these sections and they pull in opposite directions.

The first is the discussion that restates the results. Table 3 said 2.1 percentage points, and the discussion says that the effect was 2.1 percentage points, in longer sentences. Nothing has been added, so the reader learns that the author either does not know what the finding means or is unwilling to commit to an interpretation. Referees describe this as a thin contribution, which sounds like a comment about the analysis and is actually a comment about these two pages.

The second is the discussion that inflates. The results section said "is associated with", the discussion says "drives", the policy implication proposes national rollout on the strength of a local estimate from one region, and each limitation is followed by a sentence explaining why it does not really matter. This is more common among good papers than bad ones, because a strong result invites the author to claim the general version of it. It is also the failure that ends papers, since a referee who catches one overclaim rereads the entire manuscript looking for others and usually finds them.

Between the two sits the actual job: say what the finding means, how much of it to believe, and what follows from it, in that order and at no greater strength than the design allows. These sections are written sixth in the manuscript order set by `full-manuscript-build`, which puts the results fifth and the introduction eighth. They come immediately after `results-writing` and before the framework and the introduction, because the interpretation is sharpest while the estimates are still in the author's head and because the introduction's contribution paragraph is copied from here rather than the other way round.

## When to use this, and when not to

Use it to draft a discussion and a conclusion from finished results, to repair a discussion that restates the results, to write or rewrite a limitations paragraph, to size a policy or managerial implication to the evidence, to adjudicate a hypothesis that failed, and to write the chapter-closing paragraphs of a thesis chapter.

Use it when a reviewer says the contribution is unclear. That comment is usually about the discussion, not about the analysis, and rewriting the analysis in response is the expensive way to answer it.

Do not use it to report the estimates themselves, which is `results-writing`; nothing new is reported here, no new number appears that is not already in an exhibit, and no new citation appears that changes the argument. Do not use it to write the introduction's contribution paragraph directly, which is `introduction-writer`; write it here first, then hand the wording over. Do not use it to mount a full defence of the identification, which is `identification-defense`; the discussion concedes threats and states their direction, and the defence lives in the strategy section and its appendix. Do not use it to write a referee response, which is `response-to-reviewers`, although a revision that changes the results will send you back here.

Do not use it to fix a paper whose results do not support any interesting claim. Interpretation cannot manufacture a contribution, and the attempt is visible in the first paragraph.

## What you need before starting

**The finished results section and its exhibits.** Missing: finish `results-writing` first. A discussion drafted against provisional estimates is rewritten entirely when they move, and unlike the introduction it cannot be repaired by swapping numbers, because the interpretation itself depends on the magnitudes.

**The hypotheses and what happened to each.** Supported, not supported, mixed. Missing: reconstruct from the results section's adjudication. Every hypothesis is answered here in the terms of the question, not the coefficient.

**The estimand and the population it applies to.** Local to a cutoff, an average across treated units, an effect for compliers, an effect for the years observed. Missing: derive it from the design and state it explicitly, because every implication in this section is bounded by it and a mismatch between estimand and implication is the most reliable overclaim.

**The two to five closest prior estimates, as numbers, with DOIs.** Not a list of related papers; the specific estimates yours will be compared against, with their settings and designs. Missing: search for them under the `literature-verification` standard before writing. A discussion that says "consistent with prior work" without numbers is the version referees ask to have rewritten.

**The threats conceded in the strategy section.** Missing: read that section and list them. The limitations paragraph must contain the threats a referee would raise first, and the fastest way to fail that test is to write limitations from scratch without rereading what the paper already admitted.

**The target's conventions.** Whether discussion is a separate section, whether implications are expected for policy or for practice, whether the theoretical contribution is stated first, whether future research is expected and in what form. Missing: take them from three recent articles in the target.

**For a thesis chapter, the thesis question and the neighbouring chapters' claims.** Missing: ask. A chapter conclusion that duplicates the next chapter's contribution is a structural problem an examiner will name.

## The method

Write the discussion in this order. The order is the argument.

1. **Restate the finding at the level of the question, with a comparison the reader can picture.** One paragraph. Not "the coefficient on treatment is 0.086" but "the tutoring programme raised mathematics attainment by about a tenth of a standard deviation, roughly a third of the average gain a pupil makes in a school year, and about the size of the gap between the median school and one at the sixtieth percentile". The rule for the comparison: it must use a quantity the reader already has intuition for, and the same comparison is then used consistently everywhere else in the paper, including the abstract.

2. **Answer the research question in one sentence, and adjudicate each hypothesis.** This is the paragraph the introduction's promise is redeemed in. Every hypothesis stated anywhere in the paper is answered here, including the ones that failed, in the terms of the question rather than the estimate.

3. **Explain the mechanism, in the terms of the framework, and mark what is inferred.** Cite the paper's own mechanism or heterogeneity exhibits by number. Where the mechanism is inferred rather than tested, say so in the sentence that proposes it. The rule: a mechanism the paper did not test is a hypothesis for the next paper, and labelling it as one costs a clause and prevents a referee from calling the whole section speculative.

4. **Compare with prior estimates by number.** "The estimate of 0.086 standard deviations is smaller than the 0.15 reported by Okonkwo and Whitfield (2019) for a similar programme with voluntary enrolment, and close to the 0.09 in Barreto (2021), which also uses administrative outcomes." Then the reason for the difference: setting, population, design, measurement, period. The rule: each comparison names the likely source of the difference, because a list of other people's numbers with no explanation is a table, not an argument. Citations here are the hyperlinked author-year form with the DOI behind them, semicolon-separated when grouped, and every one appears in the reference list.

5. **State the boundary conditions.** For whom, where and when the finding holds, drawn from the heterogeneity results, and where it probably does not, drawn from theory and from the setting. The external validity claim is made explicitly here rather than left for the reader to infer, because the inference the reader makes will be broader than the one you would have made.

6. **State the limitations, each with the direction of the likely bias and the evidence that bounds it.** A limitation without a direction is decoration: "measurement error in the outcome" tells a referee nothing, while "measurement error in the self-reported outcome is likely to attenuate the estimate toward zero, so the reported effect is plausibly a lower bound, and the administrative subsample in Table A7 gives a larger estimate consistent with that" is an argument. The rule that makes this section credible: no limitation is followed by a sentence explaining why it does not matter. If it does not matter, it is not a limitation and should not be listed. Include the threats the strategy section conceded, first.

7. **Size the implications to the estimand.** One implication the design clearly supports beats three it might. Name the population it applies to, the conditions under which it would fail, and where the numbers exist, the cost comparison. The test: could a policy adviser act on this sentence and would you defend the action in front of the referee who read your identification section?

8. **Write the conclusion, one to three paragraphs, doing three things only.** Restate the question and the answer with the main number; state the contribution in one or two sentences that will be copied verbatim in substance into the introduction's fifth move; end on the finding. Future research, where the field expects it, is one sentence naming the specific question this paper could not answer and the data or design that would answer it. Not a list, and never a list that begins with "future research could examine other contexts".

9. **Run the calibration pass.** Read only the verbs and the modal words, in the results, the discussion and the conclusion together. Any place the discussion is stronger than the results, the discussion is wrong. Then read only the sentences containing a policy or practice claim and check each against the estimand.

10. **Check that nothing new appeared.** No new estimate, no new citation that changes the argument, no mechanism claim without evidence or a label. New material in a discussion is the fastest way to lose a referee's trust, because it suggests the analysis was not complete when the paper was written.

## Calibrating the claim

The verb attached to the finding is the paper's central claim about causality and it should be chosen deliberately rather than inherited from a draft. A workable ladder, strongest at the top:

| Design | Verb that fits | What must be defensible for it |
| --- | --- | --- |
| Randomised assignment, high compliance | causes, raises, reduces | Randomisation held, attrition balanced |
| Regression discontinuity, credible cutoff | raises, reduces, at the cutoff | No manipulation, smooth covariates, local claim stated |
| Difference-in-differences with clean timing | raised, increased | Pre-trends flat, no anticipation, treatment timing exogenous |
| Instrumental variables | raises, for compliers | Relevance shown, exclusion argued in prose, estimand named |
| Panel fixed effects with controls | is associated with, predicts | Time-varying confounding addressed, and the phrase stays |
| Cross-sectional regression | is associated with, is higher among | Selection acknowledged as unresolved |
| Matching on observables | is associated with, after adjustment | Balance shown, unobservables conceded |

Two rules. The verb in the discussion is never stronger than the verb in the results, and the verb in the abstract is never stronger than the verb in the discussion. And where the design supports only association, the word "effect" is itself a claim; "the estimated association" costs three characters and is honest.

## Field conventions

**Economics.** The discussion is often short or folded into the results, with a separate conclusion of one to two pages. Magnitudes compared with prior estimates by number are expected. Policy implications are brief and specific, and long implication sections are read as padding.

**Education.** A distinct discussion section, implications for practice and for policy stated separately, limitations often as a labelled subsection, and a conclusion that returns to the practical question. Effect sizes are compared against benchmarks the field recognises, such as typical annual growth, so give the benchmark and its source.

**Management.** Theoretical contribution stated first and at length, then managerial implications, then limitations and future research, often each with its own subheading. The discussion is frequently longer than the results section, and a discussion that does not state what theory it extends will be rejected as atheoretical however good the analysis is.

**Health and public health.** Structured discussion with a standard opening summary, comparison with prior literature, strengths and limitations as a named subsection, and implications. Reporting-guideline compliance often extends into this section.

Take the actual convention from three recent articles in the target journal rather than from the field label, since journals within a field differ more than the field descriptions suggest.

## The thesis chapter variant

A chapter conclusion does everything above and then closes the chapter's place in the thesis: one paragraph saying what this chapter established that the next chapter builds on, and how it answers its part of the thesis question. Two failure patterns are specific to theses and both are found by examiners. A chapter that claims the thesis-level contribution rather than its own, leaving the final chapter with nothing to say; and three chapters whose conclusions are interchangeable, which signals that the chapters are three analyses rather than one argument.

The final chapter is different in kind: it synthesises across chapters by number, states the thesis-level contribution once, states the limitations that apply to the whole programme of work rather than repeating each chapter's, and ends on the thesis finding. `thesis-chapter-review` reads a chapter the way an examiner will, and `thesis-defense-prep` prepares the defence of these claims.

## Worked example

**Situation.** Dr. Samuel Okonkwo had finished the results for a paper on a rural electrification programme and small business formation, using a regression discontinuity around a village population threshold that determined eligibility. The headline estimate was a 3.6 percentage point increase in the share of households operating a registered business, from a base of 11.2 percent. His draft discussion was four pages and had been written in one sitting the day the results stabilised.

**Task.** A discussion and conclusion for a development economics journal, about 1,400 words together, that would survive a referee who specialises in regression discontinuity designs.

**Action.** The draft was diagnosed paragraph by paragraph against the six discussion moves. Two paragraphs restated the results table. One paragraph compared with prior literature qualitatively, using the phrase "in line with previous studies" three times. The limitations paragraph listed four limitations, three of which were followed by a sentence explaining why they were not serious. The implications paragraph recommended extending the programme nationally.

The wrong turn was that national recommendation, and it survived two rounds of self-editing because it felt like the point of the paper. The estimate was local to villages near a population threshold of 2,000, in a setting where villages just above the threshold differ from the median village in the country on almost everything: density, road access, distance to a market town. The design identifies an effect at the cutoff and says nothing about villages of 8,000 people. The replacement implication was narrower and more useful: the programme's threshold could be lowered to about 1,500 without the effect disappearing, because the estimate is stable across the bandwidths tested and the density of villages in that range is high, and the cost per additional business formed at that margin is roughly comparable to the current margin. That is a recommendation an official could act on and the paper could defend.

The comparison paragraph was rebuilt with numbers. The estimate of 3.6 percentage points was larger than the 1.9 reported in a study of a similar programme in another country that measured business formation through a household survey rather than a business register, and the paragraph named that measurement difference as the likely reason, since registration is a narrower outcome than self-reported enterprise activity. It was smaller than a third study's 6.1, which examined a programme bundled with a credit component. Naming the bundling changed the comparison from a discrepancy into evidence about mechanism.

The limitations were rewritten with directions. Registration as an outcome misses informal enterprises, which biases the estimate downward if electrification shifts activity from informal to formal, and the paper could not distinguish formalisation from creation; that was stated as the paper's main limitation rather than its fourth. The reassuring clauses were deleted, all three.

One hypothesis had failed: the predicted heterogeneity by distance to market town was absent, with a precisely estimated interval that ruled out meaningful differences. The original draft did not mention it. The rewrite adjudicated it in two sentences and used it, since a null on that dimension is informative about which mechanism is operating.

**Result.** 1,390 words. Two referees; one asked for exactly the local-versus-national point that had been removed before submission, which the paper answered by pointing at the paragraph that already made it. The paper was accepted with minor revisions. The author's note afterwards was that the discussion took eleven hours and the first version had taken two, and that the difference was almost entirely in the four numbers used for comparison and the four directions of bias.

### A second scenario, where it goes differently

A management journal, a study of 34 interviews across seven firms, and a discussion that has to carry a theoretical contribution rather than an effect size.

The moves are the same and the weights invert. The mechanism move becomes the longest part of the section, because the contribution is the mechanism: the paper proposes a boundary condition on an established theory, and the discussion has to state precisely which existing account fails to explain the negative cases, and what the revised account predicts that the old one does not. The comparison move compares theoretical claims rather than magnitudes, and the rule that replaces "compare by number" is "name the specific proposition in the prior work that this evidence contradicts or qualifies".

Limitations change character too. Transferability replaces external validity, and the honest statement is about the sampling of firms and the conditions under which the pattern would not be expected, supported by the negative cases the study found rather than by an appeal to sample size. The implications section splits into theoretical and managerial, in that order, and the managerial implications are sized to the seven firms rather than to the industry.

What holds across both scenarios: no new evidence in the discussion, every claim calibrated to what the design supports, limitations with a direction and no reassurance, and the last sentence a finding.

## Output

```
DISCUSSION
[1. The finding at the level of the question, with a comparison the reader can picture]
[2. The question answered; each hypothesis adjudicated]
[3. Mechanism, in the framework's terms, with inference marked as inference]
[4. Comparison with prior estimates by number, each with the reason for the difference]
[5. Boundary conditions: for whom, where, when, and where not]
[6. Limitations, each with direction of bias and bounding evidence, no reassurance]
[7. Implications, sized to the estimand, with the population and the failure conditions]

CONCLUSION
[Question and answer with the main number]
[Contribution, one or two sentences, to be copied into the introduction's fifth move]
[Closing sentence: a finding]
[Future research, one sentence, only where the field expects it]
```

Limitations table, used while drafting and often kept in an appendix:

| Limitation | Direction of likely bias | Evidence that bounds it | What would resolve it |
| --- | --- | --- | --- |
| Outcome captures registered businesses only | Downward if formalisation dominates | Survey subsample in Table A5 | Linked informal enterprise data |

## Failure modes

**The discussion that restates the results.** Recognise it by paragraphs that contain coefficients and no comparison, no mechanism and no boundary. Rewrite move one first; if the finding cannot be restated at the level of the question, the question may not be settled.

**Qualitative comparison.** Recognise it by "in line with", "consistent with the literature", "similar to previous findings". Replace each with a number, a citation and a reason for the difference.

**Reassurance after every limitation.** Recognise it by "however" following a concession. Delete the reassurance. Referees read the pattern as anxiety and start looking for what else is being managed.

**Implications that outrun the estimand.** Recognise it when the implication names a population wider than the one the design identifies. Rewrite to the margin the design speaks to; the narrower implication is usually more useful anyway.

**Verb inflation.** Recognise it by comparing the verbs across results, discussion, conclusion and abstract in one pass. The discussion is where the upgrade usually happens because it is written in one sitting after a good result.

**A hypothesis quietly dropped.** Recognise it by listing every hypothesis and searching the discussion for each. A dropped hypothesis reads as selective reporting whatever the intention was.

**New material.** Recognise it by any number or citation in the discussion that appears nowhere earlier. Move it into the results and its exhibit, or remove it.

**The contribution paragraph that differs from the introduction.** Recognise it by putting them side by side. Write it here, then copy it there; the reverse order produces a conclusion that inherits the introduction's optimism.

**The uplift ending.** Recognise it by any final sentence about the growing importance of the topic. The last sentence is a finding.

**Future research as a list.** Recognise it by three or more sentences beginning "future work could". Name one question and the data that would answer it, or cut the paragraph.

## Edge cases

**A null headline result.** The discussion is more important than usual, not less. Move one states what the design rules out and why that matters given what the literature claimed; move four compares the excluded range with prior estimates; the implications concern what should stop being assumed. Do not spend the section speculating about why the effect was absent unless the paper has evidence about it.

**A result that contradicts the paper's own hypothesis.** Engage it directly: the candidate explanations, what in the data or design could produce it, and which the evidence favours. Explaining away is visible and costly; explaining is the work, and a contradicted hypothesis honestly handled is often the most interesting part of a paper.

**A result that contradicts a well-known prior finding.** Compare designs, samples, periods and measures before proposing that the prior work is wrong. Where the difference is genuinely unresolved, say so; an honest unresolved discrepancy is publishable and a dismissive one is not.

**The journal merges results and discussion.** Write them separately, run the calibration pass, then merge. The merge is a formatting operation performed last.

**A descriptive paper with no model.** The discussion cannot supply the question the paper never asked. Either state the question and the framework explicitly, retrospectively and honestly, so the pattern has a reason to matter and a claim about what changes now it is known, or accept that the paper is not ready. `research-design` is the fix, not prose.

**A supervisor or coauthor who wants a stronger claim.** Put the calibration ladder in front of them and identify the specific design property that would have to hold. Disagreement about strength is resolvable with evidence; do not resolve it by splitting the difference in the wording, which produces a claim nobody can defend.

**A thesis chapter that will also become an article.** Write the chapter version with its linking paragraphs, then strip them for the article and add the positioning the article needs. Do not submit the chapter conclusion unchanged; examiners and referees want different closings.

## Quality bar

- The finding is restated at the level of the question, with a comparison the reader can picture, and the same comparison is used in the abstract.
- Every hypothesis is adjudicated, including the failures.
- Prior estimates are compared by number, with hyperlinked citations and a stated reason for each difference.
- Every limitation carries a direction of bias, and no limitation is followed by a reassuring clause.
- Every implication names the population it applies to and stays inside the estimand.
- The verbs are no stronger than in the results, checked in a dedicated pass.
- Nothing new appears: no new number, no argument-changing citation, no untested mechanism claim without a label.
- The contribution sentences match the introduction's fifth move exactly in substance, and the last sentence of the conclusion is a finding.

## Adapting this to your context

The ten moves assume a quantitative paper with one headline estimate, a separation of discussion from conclusion, and policy implications as the end point. The calibration discipline generalises; the furniture does not.

- **Section shape.** Health and psychology journals often run one Discussion containing findings, comparison, limitations and conclusions, sometimes with mandated subheadings. Merge moves 1 to 8 under those headings; the order of the argument stays the same.
- **Implications.** Written here as policy implications with a cost comparison. In psychology it is theoretical implications and what the result does to the model; in education and nursing, implications for practice; in sociology, what the case says about the wider claim.
- **Comparison by number.** That assumes a literature of comparable effect sizes. Where there is none, compare with the closest qualitative findings and say what converges and what does not; in a meta-analytic literature, compare with the pooled estimate and its interval, not with individual studies.
- **The estimand.** An econometrics word. Elsewhere it means stating the target population and the conditions of transfer, and in qualitative work a claim to transferability rather than generalisability.
- **What not to change.** Nothing new appears in the discussion, every limitation carries a direction, and no sentence claims more than the design supports.

## Related skills

`full-manuscript-build` places these sections sixth in the writing order, immediately after the results at step 5 and before the framework and the introduction at step 8. `results-writing` supplies the estimates and the hypothesis adjudication this section interprets. `introduction-writer` copies its contribution wording from here. `identification-defense` supplies the conceded threats that the limitations must include. `literature-verification` supplies the prior estimates compared in move four, and `references-and-bibliography` formats them. `abstract-and-title` takes the finding and the comparison from here. `thesis-chapter-review` and `thesis-defense-prep` test the chapter-level version of these claims. `peer-review-simulator` attacks the overclaims before a referee does, and `response-to-reviewers` handles what comes back.
