---
name: data-section-writer
description: Writes the data section of an empirical paper, thesis chapter or proposal to a reproducibility standard: sources with producers and access routes, linkage and match rates, the sample construction chain with a count after every restriction, treatment and outcome measurement described precisely enough to judge measurement error, variable definitions with units, missingness and attrition with patterns rather than rates alone, and the data availability statement. Enforces counts that match the exhibits exactly, limitations stated without a reassuring clause, variables tied to the hypotheses they serve, and hyperlinked author-year citations for every dataset, codebook and register. Use this skill when someone asks to write or fix the data section, describe the sample, document variable definitions, explain where the data came from, report attrition or missing data, justify a sample restriction, write a data availability statement, or when a methods section starts estimating before anything has been said about the data.
---

# Data Section Writer

The data section is where a careful reader decides whether to believe anything that follows. Not because it is interesting, but because it answers the four questions that determine whether an estimate means what the author says it means: where did these observations come from, who measured the variables and how, what was dropped and why, and could a competent stranger assemble the same sample.

When it fails, it fails silently and late. A referee asks why N is 12,067 in Table 3 and 12,340 in Table 5, and the honest answer is that nobody knows, because the restrictions live in a do-file nobody documented. A replicator requests the data, applies the stated restrictions, and lands 900 observations away. An examiner asks how treatment was recorded and by whom, and the answer turns out to be a self-reported field in an administrative form, which changes what the paper can claim about measurement error. None of these is a small correction. Each one moves the paper from a methods discussion into a credibility discussion, and papers rarely recover from that.

The standard here is simple to state and demanding to meet: the section is documentation written as prose, and a reader with the same data access should be able to reproduce the analysis sample from it alone.

## When to use this, and when not to

Use it to draft the data section of any empirical paper, chapter or proposal, to repair one that has lost track of its own counts, to write a data availability statement, to document a linkage between two sources, or to describe a sample whose construction has changed since the section was first written.

Use it whenever the manuscript reports two different sample sizes anywhere, which is the most common symptom of a data section that was written from the codebook rather than from the code.

Do not use it to do the cleaning itself, which is `data-profiling-and-cleaning`: profiling missingness, finding outliers, checking a codebook against the data, and verifying panel coherence happen before this section can be written, and their outputs are its inputs. Do not use it to build Table 1 or the balance table, which is `descriptive-statistics-tables`; this section describes what those tables show and does not duplicate them. Do not use it to justify the identification strategy, which is `econometric-model-writer` and `identification-defense`; the data section says what exists, not why it identifies anything. Do not use it for the consent, approval and anonymisation questions, which are `research-ethics-and-data-protection`, or for the deposit itself, which is `replication-package`.

Do not write this section from the codebook. Write it from the code that produced the analysis file, and check the codebook against both.

## What you need before starting

**The script or notebook that produces the analysis sample**, not a description of it. Every restriction, in the order applied, with the count after each. Missing: this is the input that cannot be substituted. Ask for it, and if it does not exist as a single traceable chain, reconstruct it by rerunning with counts logged at each step. A data section written from memory will disagree with the exhibits, and that disagreement will be found by someone else.

**The raw source inventory.** Each dataset with its producer, the years covered, the unit of observation, the version or release, and how it was obtained. Missing: ask specifically about version and release date; administrative files are revised, and two authors working from downloads six months apart can hold different data with the same name.

**The codebooks or data dictionaries** for each source. Missing: write the variable definitions from the code and mark each as unverified against official documentation, then verify before submission. Codebooks describe intentions; the data describes what happened; where they differ, the data wins and the difference is worth a sentence.

**The design document, with the hypotheses.** It says which variables have to be described in detail and which can be summarised in one line. Missing: run `research-design`, or at minimum extract the hypotheses from the exhibits, because a data section that describes forty variables at equal depth tells the reader nothing about which ones matter.

**The missingness and attrition profile.** Rates by variable, patterns across units and time, and whether missingness correlates with treatment. Missing: run `data-profiling-and-cleaning` first. Reporting a rate without a pattern is the version of this paragraph that referees do not accept.

**The access conditions.** Whether the data can be shared, under what agreement, and what a replicator would have to do. Missing: ask the data provider or read the licence before writing the availability statement. Promising data that cannot legally be shared is worse than stating the restriction plainly.

**The target journal's data policy and word budget for this section.** Missing: take both from three recent empirical articles in the target. Data policies changed at many journals in the last few years and the stated guidelines are often behind the practice.

## The method

1. **Rebuild the sample construction chain from the code, with counts.** Run the pipeline and log the number of observations, and the number of units where the data is a panel, after every restriction. This is step one because everything else in the section is checked against it, and because it routinely surfaces a restriction nobody remembered applying. Where the chain has a step that cannot be explained, stop and find out what it does before writing about it.

2. **Write the sources paragraph, one source at a time.** Name the producer, the exact dataset and its version, the years, the unit of observation, and the access route: public download, request to the agency, restricted access under agreement, or purchase. For administrative data, name the register and the institution responsible for it. For surveys, the survey name, the sampling design, the fieldwork period and the published response rate. Cite the data documentation as a source in the hyperlinked author-year form, so the register or agency appears in the reference list like any other work.

3. **Document the linkage, where there is one.** The identifier used, whether it is exact or probabilistic, the match rate, and what happened to the unmatched. The rule: a merge that drops observations is reported with counts and a sentence on whether the unmatched differ systematically from the matched. An unexplained match rate below about 95 percent is something a referee will ask about, so answer it before they ask.

4. **Write the sample construction chain as prose with a table beside it.** Each restriction gets its rationale and the count remaining after it. Restrictions driven by data availability are stated as such and left there: "the outcome is populated for only 15 of the 20 states across the full period, and the analysis is restricted to those 15" is complete on its own and needs no reassurance about representativeness. Where a restriction is a judgement call rather than a necessity, say which and say what happens without it, in one clause, pointing to the robustness table.

5. **Describe the treatment.** Exactly how it is defined, where the indicator comes from, the timing rule that decides when a unit counts as treated, and who recorded it. For a policy treatment, both the legal or administrative definition and any gap between formal adoption and actual implementation, because that gap is a measurement error the referee will raise. The test to apply: could someone else reproduce the treatment variable from this paragraph and the source?

6. **Describe the outcome.** How it is measured, by whom, at what frequency, on what scale, with what known coverage limits, and what transformation was applied with its reference group where standardised. Then the honest sentence about what it does not capture. An outcome section that reads as though the measure is perfect signals an author who has not thought about measurement, and the discussion later has nothing to build a limitation on.

7. **Describe the covariates briefly and put the full list in an appendix.** Grouped by function, with units at first use, and with a note on any variable whose definition changed during the period, giving the years of each definition and the harmonisation rule applied.

8. **Write the descriptive paragraph, three to six sentences.** The sample in plain terms and the two or three descriptive facts the reader needs before the results: how large the treated group is, how the outcome moved over the period, how much variation there is to work with. Every number identical to `descriptive-statistics-tables` output. No estimates; descriptive facts only.

9. **Write missingness and attrition with patterns, not just rates.** The rate by variable, whether it is concentrated in particular units or years, the handling rule applied with its method named, and for panels, how many units are observed in every period, the entry and exit pattern, and whether attrition correlates with treatment. The last one is the point of the paragraph; the others are context.

10. **Write the data availability statement.** Where the data can be obtained, under what conditions, what cannot be shared and why, and where the code is deposited. This is a factual statement, checked against the licence, not an aspiration.

11. **Reconcile every count in the section against every exhibit note.** Data section N, exhibit note N, results prose N. This takes ten minutes and catches a real error in a large share of drafts. Where two numbers legitimately differ, because a specification drops singletons or requires a lagged variable, say so at the point of difference rather than leaving the reader to work it out.

12. **Read it as a replicator.** Take the finished section and ask, at each paragraph, whether you could act on it without asking a question. Every place the answer is no gets a sentence.

## What a referee is actually asking

Four questions sit behind almost every referee comment on a data section, and writing to them directly is more efficient than writing to a template.

**Is the sample the population you claim to speak about?** Answered by the construction chain and by one sentence naming who is excluded and in which direction that biases the estimand.

**Does the treatment variable measure treatment?** Answered by the timing rule, the recording process, and the honest statement of any gap between formal and actual treatment.

**Does the outcome measure the construct?** Answered by who measures it, on what scale, how often, and what it misses. Self-reported outcomes, administrative outcomes with reporting lags, and test scores with ceiling effects each need their own sentence.

**Could missingness produce your result?** Answered by the pattern, not the rate, and by whether attrition correlates with treatment.

A data section that answers these four in identifiable places is doing its job, whatever order the journal wants them in.

## Worked example

**Situation.** Lucia Marchetti, a third-year doctoral student, was writing the data section for a chapter on a national school meals expansion. Two sources: an annual schools register maintained by the education ministry, covering 2013 to 2021, and a household panel survey covering the same years with about 26,000 households per wave. The chapter's exhibits were built and the results were stable. Her draft data section was 900 words, written six months earlier, and reported a sample of 18,432 school-year observations. Table 2 reported 12,067.

**Task.** A data section a replicator could act on, with counts that reconcile, in time for a supervisor meeting in five days.

**Action.** The chain was rebuilt from the do-file first, which took a morning and produced the answer to the discrepancy. Raw register: 18,432 school-year observations. Restriction one, schools with the outcome recorded in at least three years: 15,908. Restriction two, dropping the 2013 wave because the outcome definition changed in 2014: 14,120. Restriction three, matching to the household survey at municipality level, match rate 96.4 percent, with unmatched concentrated in two sparsely populated regions: 13,610. Restriction four, dropping schools with fewer than 20 pupils in any observed year, on the grounds that the outcome is a school-level average and noisy in small schools: 12,067.

Restriction four was in the code and in nobody's memory. It was defensible and it was undocumented, which is the case that matters, because it had been applied before any results were seen but there was no record proving that. It went into the chain with its rationale and into the robustness table without it, where the estimate moved from 0.071 to 0.064 standard deviations, well inside the confidence interval.

The wrong turn: the first rewrite was drafted from the codebooks, because the codebooks were tidy and the do-file was not. It produced a clean, wrong section. Two variable definitions in it did not match what the code actually constructed, because the register changed the coding of one field in 2017 and the do-file harmonised it in a way the codebook did not describe. That draft was abandoned after the reconciliation step at the end failed on two counts and one definition. The rule that came out of it, and that is now step one of the method above: write from the code, then check the codebook against it, and where they differ say so in the section.

The measurement paragraphs were the part that changed the paper. Treatment was recorded by school administrators in an annual return, and the return asked whether the school "participates in the expanded meals programme", which schools in a transition year could answer either way. That produced a timing ambiguity for roughly 4 percent of school-years around adoption. Writing it down led to a robustness check dropping transition years, which the referee later asked for and which already existed.

Attrition was written with a pattern rather than a rate: 71 percent of schools appear in all eight years, exits are concentrated in small rural schools that closed, and exit is uncorrelated with treatment status in a regression reported in the appendix.

**Result.** The section went from 900 to 1,480 words, one table, one appendix table. Every count in the manuscript reconciled. The supervisor's only comment was on the transition-year ambiguity, which he called the most useful paragraph in the chapter, because it converted a hidden weakness into a stated one with a robustness check attached. Time cost was about nine hours including the abandoned draft.

### A second scenario, where it goes differently

A paper using data the researcher collected herself: a survey of 412 small firms in three regions, fielded over eleven weeks, with a 38 percent response rate.

The structure holds and the weight shifts. There is no register to name and no linkage, so those paragraphs shrink to nothing. In their place come the paragraphs that only primary data needs: the sampling frame and where it came from, how the sample was drawn from it, the fieldwork period and mode, the number of contacts and reminders, the response rate calculated by a named standard rather than by an informal ratio, and the non-response analysis comparing respondents with the frame on the characteristics the frame carries.

The measurement paragraphs get longer rather than shorter, because the instrument is the measurement: which items came from validated scales and which were written for this study, what the reliability statistics are, and what pretesting was done. That material comes from `survey-and-instrument-design`, and the data section cites the instrument rather than reproducing it, with the full instrument in an appendix.

The availability statement changes character too. Primary data is usually shareable in de-identified form, which makes the statement a commitment rather than a restriction, and the de-identification standard applied belongs in it. That is `research-ethics-and-data-protection` territory and the data section states the outcome of it.

## Output

Prose in the order below, with one table in the body and one in the appendix.

```
DATA
[Sources: producer, dataset and version, years, unit, access route, cited]
[Linkage: identifier, match rate, treatment of unmatched]
[Sample construction: prose, with the table below]
[Treatment: definition, source, timing rule, recorder, formal versus actual]
[Outcome: measure, measurer, frequency, scale, transformation, known limits]
[Covariates: grouped, brief, full list in appendix]
[Descriptives: 3 to 6 sentences, numbers identical to Table 1]
[Missingness and attrition: rates, patterns, correlation with treatment, handling rule]
[Data availability statement]
```

Sample construction table, in the body:

| Step | Restriction | Rationale | Observations | Units |
| --- | --- | --- | --- | --- |
| 0 | Raw extract | | 18,432 | 2,304 schools |
| 1 | Outcome recorded in at least three years | Panel requirement | 15,908 | 1,988 |
| 2 | Drop 2013 | Outcome definition changed in 2014 | 14,120 | 1,988 |
| 3 | Matched to household survey | Municipality identifier, 96.4 percent match | 13,610 | 1,914 |
| 4 | Schools with 20 or more pupils in all years | School-level average unstable below | 12,067 | 1,703 |

Variable definition table, in the appendix:

| Variable | Definition | Source and years | Unit | Notes on changes |

## Failure modes

**Writing from the codebook.** Recognise it because the section is clean and the counts do not match the exhibits. The codebook says what the data was meant to contain. Write from the code and check the codebook against it.

**Undocumented restrictions.** Recognise it when the chain's final count does not equal the exhibit's N. Every such gap is a restriction someone applied and nobody wrote down, and each one is a question a referee can ask that the author cannot answer.

**Rates without patterns.** "Missingness is 8 percent" answers nothing. The question is whether the missing 8 percent is random, concentrated in one region, or concentrated among treated units. Report the pattern.

**Reassurance after a limitation.** Recognise it by any sentence starting "however, this is unlikely to affect" immediately after a stated constraint. It reads as anxiety and invites the referee to check. State the constraint, put the evidence that bounds it in the robustness section, and let the discussion carry the consequence.

**Treating the outcome as self-evident.** Recognise it when the outcome gets one sentence and the covariates get four paragraphs. The outcome is where measurement error does the most damage to the interpretation, and it deserves the most careful paragraph in the section.

**Results in the data section.** Recognise it by the appearance of a coefficient or a regression-based comparison. Descriptive facts belong here; anything estimated belongs in results.

**A promise the licence does not allow.** Recognise it in an availability statement saying data are available on request when the agreement forbids redistribution. Read the licence and state the actual route, including the fact that a replicator would need their own agreement.

**Describing forty variables at equal depth.** Recognise it when the section runs to five pages. Depth follows the hypotheses: treatment and outcome in full, the covariates that appear in the main specification briefly, everything else in the appendix.

## Edge cases

**Restricted or proprietary data.** Describe the access route precisely enough that a replicator could start it: which body grants access, what the application requires, roughly how long it takes, and what cannot be shared under any conditions. Deposit the code publicly even when the data cannot be, and say so.

**A constructed panel from several releases.** Document harmonisation variable by variable, with the years each definition applied and the rule used to bridge them. Where a definition change cannot be bridged, restrict the period and say so rather than assuming continuity.

**Text, scraped or platform data.** State collection dates, the retrieval procedure, deduplication, the share of the target population captured, and the terms under which collection was permitted. Archive a copy of anything that can disappear, since pages and endpoints change.

**Survey data with weights.** Say which weights, why, and whether the estimates change materially without them. Where the analysis is unweighted for a stated reason, give the reason.

**Secondary data whose codebook contradicts the data.** Report the discrepancy in one sentence, say which you used, and cite both the codebook and any correspondence with the producer.

**A sample that changed after the section was written.** The section is rewritten, not patched. Patched data sections are how a manuscript ends up with three different values of N.

**Data from a source that requires acknowledgement or has a citation policy.** Follow it exactly, in the hyperlinked author-year form, and check the producer's preferred citation rather than inventing one.

**A paper with no hypotheses to guide the depth.** Describing everything equally is the symptom, not the disease. Go back to `research-design`; a data section cannot decide what matters on its own.

## Quality bar

- A reader with the same access could apply the stated restrictions and arrive at the same N.
- Every count in the prose matches the construction table and every exhibit note, or the difference is explained where it occurs.
- Treatment and outcome are described precisely enough for a reader to judge measurement error, including who recorded them.
- Missingness and attrition are reported as patterns, with the correlation with treatment stated.
- Every restriction has a rationale, and the judgement calls are marked as judgement calls with a robustness pointer.
- No limitation is followed by a reassuring clause, and no estimate appears in the section.
- Every dataset, register and codebook is cited in the hyperlinked author-year form and appears in the reference list.
- The availability statement matches what the licence actually permits.

## Adapting this to your context

The twelve steps assume secondary quantitative data, administrative or survey, with a treatment variable and an estimation sample. The reconciliation discipline is universal; the paragraph list is not.

- **The missing paragraphs.** Primary data collection needs what this list omits: recruitment and sampling, consent and ethics approval with its reference number, the instrument and its provenance, translation and back-translation, and reliability and validity evidence for every scale. In a trial the registration identifier goes here and CONSORT governs the flow counts.
- **The treatment paragraph.** Assumes a policy or programme. For an experiment it becomes the manipulation, the randomisation procedure and the unit of assignment; in psychology, the exposure measure and its psychometrics; in qualitative work, participants, setting and access.
- **The 95 percent match rate.** A linked administrative data convention. Survey response rates run far lower and are judged against field norms and a nonresponse analysis, not a fixed number. State the rate, the norm and the comparison.
- **Data availability.** Written for economics deposits. Health and psychology usually want an explicit statement plus an OSF or repository DOI, and restricted human data has wording the ethics approval specifies.
- **What not to change.** Every count reconciles with every exhibit note and with the results prose, and the section is written so a replicator could act on it without asking a question.

## Related skills

`full-manuscript-build` places this section third in the writing order, after the exhibits and before the empirical strategy, and its counts feed every later check. `data-profiling-and-cleaning` produces the missingness, outlier and coherence profile this section reports. `descriptive-statistics-tables` builds Table 1 and the balance table this section describes without duplicating. `stata-project-scaffold` and `stata-data-management` produce the traceable construction chain step one depends on. `econometric-model-writer` takes the sample this section defines and states what it identifies. `research-ethics-and-data-protection` covers consent, approval and de-identification; this section reports their outcome. `survey-and-instrument-design` supplies the instrument for primary data. `replication-package` turns the availability statement into an actual deposit. `references-and-bibliography` formats the data citations.
