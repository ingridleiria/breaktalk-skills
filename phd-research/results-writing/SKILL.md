---
name: results-writing
description: Writes and repairs the results and discussion sections of empirical papers and thesis chapters, turning regression output into prose that reports findings honestly and at the strength the evidence supports. Use this skill whenever a researcher asks to write up results, interpret coefficients, describe a regression table, report effect sizes, discuss findings, handle a null result, or says "my results section is just a list of tables", "what does this coefficient mean", "is this effect large", "am I overclaiming". Trigger for any task converting estimation output (Stata, R, Python) into academic prose.
---

# Results Writing

A results section is not a tour of the tables. It is the argument of the paper, made with numbers. Every paragraph leads with a finding; the table citation supports it.

## Reporting a single estimate

The unit of results writing is one well-built sentence containing: the direction, the magnitude in interpretable units, the precision, and the exhibit. A working template:

"Treatment increases the outcome by 0.12 standard deviations (p < 0.01; Table 3, column 2), equivalent to moving a median institution from the 50th to roughly the 55th percentile."

Rules that keep it honest:

- **Translate the magnitude.** A coefficient means nothing to a reader until it is converted: percent of the mean, standard deviations, monetary units, or a concrete comparison. Do the conversion explicitly and show the arithmetic once.
- **Match the language to the design.** "Increases" and "causes" belong to credible causal designs; correlational results get "is associated with". The verb is a claim; calibrate it. Do not upgrade association to causation in the discussion section after being careful in the results section.
- **Statistical and economic significance are different sentences.** A precisely estimated tiny effect and a large noisy effect both deserve honest description. Never let stars do the interpreting.
- **Numbers in text match the exhibit exactly.** Same estimate, same decimals, same sign. Any rounding is consistent document-wide.

## Section architecture

1. **Main result first.** Open with the answer to the research question, in one paragraph, with the headline estimate. Readers and referees decide here.
2. **Build-up across specifications.** Walk the columns from sparse to full specification, explaining what each addition tests and what stability or movement of the coefficient means. Movement is information; do not narrate it away.
3. **Identification diagnostics** where the design requires them: pre-trends for DiD, first-stage strength for IV, density and covariate smoothness for RDD. Report them as tests that could have failed.
4. **Heterogeneity and mechanisms**, only where a hypothesis predicted them. Subgroup fishing reported as discovery is the fastest way to lose a referee.
5. **Robustness**, summarized in prose with the full set in an appendix. State what was varied and the range of estimates, not just "results are robust".

## Null and uncomfortable results

A well-identified null is a finding. Report it with the confidence interval and state what effect sizes the design can rule out ("the estimates rule out effects larger than 0.05 SD"). Do not bury a null under ten robustness checks hunting for stars, and do not describe an insignificant estimate as "positive but not significant" as if it were a small victory; describe what the interval contains.

When a result contradicts the hypothesis, the discussion engages it directly: possible mechanisms, what in the data or design could produce it, and which interpretation the evidence favors. Explaining away is visible and costly; explaining is the work.

## Discussion without inflation

- Restate the finding at the level of the question, not the coefficient.
- Compare magnitudes with prior literature by number: "larger than the 0.08 SD reported by [verified citation] in a comparable setting", not "consistent with previous studies".
- State limitations plainly and let them stand without a reassuring clause after each one.
- Policy implications are sized to the evidence: one credible implication beats three speculative ones.
- End on the finding. The final sentence of the section is a result, not an uplift statement about future research directions.

## Mechanical checks before returning any draft

- Every number in the text traced to a specific table or figure.
- Every table referenced in the text at least once.
- Units stated at first use of every variable.
- Sample sizes reported and consistent across the narrative and the exhibits.
