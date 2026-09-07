---
name: peer-review-simulator
description: Runs an adversarial pre-submission review of your own manuscript, thesis chapter or proposal, in the order an editor actually works: a desk-reject screen read from the abstract and tables alone, three full referee reports from a methodologist, a field expert and a structural reader, an editor's decision with the two or three issues that determined it, and a revision plan ordered by what would sink the paper rather than by section. Enforces the rule that every concern names its consequence for the conclusion and its fix, and that the reports disagree with each other the way real referees do. Use this skill before any submission, before a chapter goes to a supervisor or committee, and whenever someone asks whether a paper is ready, what reviewer 2 will say, whether it will be desk rejected, or asks for a referee report on their own work. Trigger also on vague requests such as "be brutal with this", "tell me what is wrong with it", "would you publish this", or "I think it is done".
---

# Peer Review Simulator

A referee report received after submission costs a rejection on the record, four months, and a decision letter the author will reread for a year. The same report received before submission costs a fortnight of revision. The content of the two reports is largely identical, because the problems a demanding referee finds are visible in the manuscript before it is sent; nobody looked for them with the right attitude.

The reason nobody looked is that authors cannot read their own paper cold. They read the paper they intended to write. The introduction promises a contribution the results section does not deliver, and the author does not see it, because when they read the results they supply the missing step from memory. A referee has no memory of the intention and reads only the text. This skill manufactures that condition deliberately: it reads the manuscript as an editor and three referees would, in the order they read it, with the willingness to reject that they have and the author does not.

The failure this prevents is not a harsh review. It is the specific and very common outcome where a paper is rejected for something the author already knew about, had decided was probably fine, and never wrote a defence of.

## When to use this, and when not to

Use it before every journal submission, before a chapter goes to a supervisor or a committee, before a conference submission where acceptance is competitive, before a grant proposal goes to a panel, and after a revision, because revisions introduce new problems at the seams where new material was added.

Use it also when a paper has been rejected once without useful referee comments, which happens often, and the author needs to know what was actually wrong.

Do not use it to review somebody else's manuscript that a journal has asked you to referee. That is `refereeing-for-a-journal`, and the difference is not cosmetic: a real referee has duties about conflicts, scope creep and tone that do not apply when you are attacking your own work, and a real referee must not be as exhaustive as this skill is.

Do not use it to read a thesis chapter as an examiner would; that is `thesis-chapter-review`, which judges whether the candidate has demonstrated independent research capability, a different question from whether an article is publishable. Do not use it to decide where the paper should go; that is `journal-targeting`, which runs after this one. Do not use it to check whether the numbers are right, which requires rebuilding them from the data and is `analysis-audit`. This skill reads what is on the page; it cannot tell you that a merge silently dropped 40,000 observations.

Do not use it to rehearse a viva, which is spoken, adversarial in real time, and needs different preparation; that is `thesis-defense-prep`.

## What you need before starting

**The complete manuscript, including tables, figures and appendix.** Not a draft with placeholders where the robustness section will go. Missing: review what exists and state at the top which sections were absent, because a referee who reaches a missing section stops being a referee and becomes an editor writing a desk rejection.

**The target venue, or a stated tier.** Standards are venue-relative. A design that is adequate for a solid field journal is not adequate for a general-interest one, and the same report cannot serve both. Missing: ask. If no answer is available, review to the standard of a good field journal in the discipline and say that is what you did.

**The stated contribution, in the author's own words.** Usually one paragraph in the introduction. Missing: extract the best candidate from the text and quote it back, because if the contribution cannot be located in the manuscript, that is the first finding and probably the decisive one.

**Whether the numbers have been audited.** Missing: assume they have not, review the internal consistency of what is on the page, and add a line to the report saying that the underlying computations were not verified and that `analysis-audit` should run before submission.

**The author guidelines, where the venue is known.** Length, structure, abstract format, exhibit rules, declarations. Missing: review structure to disciplinary norms and note that compliance was not checked.

**Any known weakness the author is already worried about.** Missing: do not ask first. Run the desk-reject screen blind, then ask, because if the screen independently finds what the author feared, that is far more informative than being told where to look.

## The method

1. **Read the entire manuscript once, without writing anything.** A referee who takes notes on page three has already decided what kind of paper this is and will read the remaining thirty pages confirming it. The first pass is for understanding the argument as the author built it. This is not optional and it is the step most often skipped, including by real referees, which is why real referee reports are frequently wrong about what the paper claims.

2. **Run the desk-reject screen, reading only what an editor reads.** The abstract, the introduction, the main table, and a skim of the remaining exhibits. Ten minutes. Answer the seven questions in the section below and give one verdict: send to review, or desk reject with the reason. If the verdict is desk reject, stop and report it. Producing three referee reports on a paper that will never reach referees wastes the author's attention on the wrong problems, and the desk-reject reason is the entire revision plan.

3. **Write the three referee reports, independently.** Do not write them as one analysis split into three voices. Each referee reads for their own concerns, in their own order, and reaches their own recommendation, and they will disagree. The disagreement is information: where the methodologist recommends rejection and the field expert recommends major revision, the paper's fate depends on which referee the editor weights, and the author needs to know that.

4. **Write the editor's decision.** Weigh the reports as an editor would, using the weighting rule below. State the decision, the two or three issues that determined it, and the substance of the letter the editor would write. Editors do not average referees; they identify which concerns are fatal and which are addressable, and a decision that reads like an average is not simulating anything.

5. **Build the revision plan, ordered by consequence.** Four tiers, described below, each item with the issue, the fix, the exhibit or section affected, and an effort estimate in hours or days. The author should be able to start item one within five minutes of reading it. A plan ordered by section number is a to-do list, not a triage.

6. **State the honest submission verdict in one sentence, at the very top of the deliverable.** Ready to submit; ready after the tier-one items; not ready and here is why. Authors under deadline read the first sentence and then skim, so the sentence that costs them a rejection has to be the first one.

## The desk-reject screen

Editors reject the majority of submissions without sending them out. They do it from the abstract, the introduction and a glance at the tables, in the time between two meetings. Simulate exactly that and answer:

- Is there a research question, stated as a question, answerable as posed?
- Is the contribution specific and credible relative to the closest published work, and is that work actually named?
- Does the design plausibly identify what the paper claims to identify?
- Is the main finding in the abstract with a number and a unit, or is it a direction?
- Is the paper in scope for this venue, judged against what the venue has recently published?
- Is the argument followable on a skim, meaning the introduction's five moves are present and in order?
- Are there immediate red flags: a table whose numbers do not match the text, a missing sample size, an undefined dependent variable, a citation that does not resolve, formatting far outside the venue's norms, or an abstract that promises something the tables do not show?

One "no" on the first three is usually a desk rejection. One "no" further down is usually a warning that becomes fatal when combined.

## The three referees

**Referee 1, the methodologist.** Reads for identification and inference and does not care whether the topic is interesting. Works through the attack list appropriate to the design, using `identification-defense` conventions. Checks that the estimating equation printed in the paper is the one the description of the code implies and the one the table reports. Checks that the clustering level matches the level at which treatment is assigned, and that the number of clusters supports the inference method used. Checks that pre-trends, first stages, density tests or balance tables are reported, and reported with enough power to be informative rather than reported and underpowered, which is a different and weaker claim. Checks that robustness tests address the threats a sceptic would name rather than the ones the author found convenient. Checks that causal language in the abstract, introduction and conclusion is no stronger than the design supports, which is the single most common place a paper overclaims. Checks that magnitudes are interpreted in units a reader can evaluate.

**Referee 2, the field expert.** Knows the setting and the literature and does not care about the estimator. Checks that the closest three papers are engaged and that the stated difference from them is real rather than a difference in wording. Checks the institutional details of the setting, which is where field experts catch papers that methodologists cannot: a policy described as beginning in one year that in fact began in another, a population that is not what the sample selects, an administrative rule that mechanically produces the result. Checks that the theoretical framework predicts the sign that was found, and that a result inconsistent with the framework is discussed rather than passed over. Checks whether the finding is consistent with what the field has found elsewhere, and where it is not, whether the disagreement is named and explained. Checks that the policy implications match the estimand and the population actually studied. Verifies a sample of citations against real records and reports any that fail, because a fabricated or misattributed citation found by a real referee ends the submission.

**Referee 3, the structural reader.** Stands in for the reader an editor uses to check that a paper is finished. Reads for the five moves of the introduction, whether the abstract's every claim traces to an exhibit, whether every table and figure is referred to in the text and does work, whether numbers agree across abstract, text and tables, whether notation is defined at first use and used consistently, whether the length fits the limit, whether the reference style is right, and whether the declarations the venue requires are present and true. This referee finds the least important problems and the largest number of them, which is why they go last: a report that opens with reference formatting teaches the author to ignore it.

Each report follows the same shape: a summary of the paper in the referee's own words, major concerns numbered and ordered by severity, minor concerns numbered separately, and a recommendation from accept, minor revision, major revision, reject and resubmit, or reject. The summary is not filler. If the referee's summary does not match what the author thinks the paper says, the paper is not written clearly, and that is a finding worth more than most of the rest of the report.

No concern is raised without stating what it changes about the conclusion and what would resolve it, or an explicit statement that nothing would resolve it, which is a fair thing for a referee to say and a hard thing for an author to hear.

## The editor's weighting rule

- Methodological concerns that would change the sign, the magnitude or the causal interpretation of the main result dominate everything else, and one of them is enough to reject.
- Contribution concerns decide between major revision and rejection. A sound paper that adds little is rejected at a good venue and revised at a modest one, which is precisely why the target venue must be known.
- Writing, structure and exhibit concerns rarely sink a paper alone, but three referees each spending half their report on them signals a manuscript that was not finished, and editors reject unfinished manuscripts to protect referee time.
- Where two referees agree on a concern, it becomes a condition of any revision. Where they disagree, the editor picks a side and says so, and the author must satisfy the side the editor picked.

## Worked example

**Situation.** A team of three, led by an associate professor, Daniel Okonjo, had a 42-page manuscript on whether a workplace training subsidy raised wages. Firm-level administrative data, 18,000 firms, six years, a subsidy allocated by regional budget rounds that the authors treated as a staggered difference-in-differences. Headline: a 3.1 percent wage effect, standard error 0.9, clustered at the firm level. The target was a well-regarded field journal in labour economics. The paper had been through four internal drafts and everyone on the team believed it was finished.

**Task.** Decide whether to submit, and if not, produce the shortest path to a submittable manuscript. The team had a co-author leaving for industry in six weeks, after which the revision capacity would drop sharply.

**Action.** The full read took ninety minutes. The desk-reject screen then ran on the abstract, introduction and Table 3 alone, and passed: the question was clear, the number was in the abstract with a unit, the closest papers were named, and the venue was right. That verdict mattered, because the team's own worry had been that the paper was too narrow for the journal, and the screen said the framing was not the problem.

The methodologist's report found the problem the team had known about and never written down. Treatment was assigned at the regional budget-round level, 14 regions across six rounds, and standard errors were clustered at the firm level, which is far below the level of assignment. Reclustering at the region level with 14 clusters would multiply the standard error by roughly two to three and the headline effect would no longer be distinguishable from zero at conventional levels. This was concern one, marked as changing the conclusion. The report also flagged that the event-study figure showed a visible pre-trend in the two periods before treatment, plotted but never discussed, and that the text described the design as identifying a causal effect while the introduction described the allocation as based partly on regional need, which is a selection story stated by the authors themselves and then not addressed.

The field expert's report found something the methodologist could not. The subsidy scheme had changed eligibility rules in the fourth year of the panel in a way that altered which firms could apply, and the manuscript treated the six years as a single regime. The referee's note: whatever the clustering issue, the estimand changes at year four and the paper does not say so. This referee recommended major revision rather than rejection, on the grounds that the underlying question was worth answering and the data could support a defensible version of the paper.

The structural reader found 23 items, including three numbers in the abstract that did not match Table 3 after a specification change in the third draft, a figure with a legend inside the plot area obscuring two data points, and a data availability statement that claimed the data were available on request when they were held under an agreement that forbade redistribution.

The editor's decision: reject and resubmit. The clustering and the pre-trend together meant the main result was not established, which is a rejection; the quality of the data and the importance of the question meant the editor would want to see it again, which is the resubmit.

**The wrong turn.** The first attempt at the revision plan was ordered by referee, taking Referee 1's points, then Referee 2's, then Referee 3's. The team read it and started on Referee 1's minor points, because they were easy and could be done that afternoon, and spent two days there. The plan was rebuilt in four tiers by consequence, which put the clustering decision alone in tier one and moved everything else below it. That reordering exposed something the by-referee plan had hidden: the tier-one item was not a fix, it was a decision about whether the paper survived, and it had to be resolved before anyone touched anything else, because if the effect did not survive reclustering there was no paper to format.

**Result.** Reclustered at the region level, the effect was 3.1 percent with a standard error of 2.4, not distinguishable from zero. The team spent the co-author's remaining six weeks on a wild-cluster bootstrap and a randomisation inference procedure appropriate to 14 clusters, which returned a p-value of 0.11. The paper was rewritten around a substantially weaker and honest claim, restricted to the pre-reform regime the field expert had identified, and submitted five months later to a field journal one rung down. It received a major revision and was eventually published.

The estimated cost of not having run this: a rejection at the original target, four months, and then the same discovery made by a referee whose report would have said the same thing in harsher terms and on the record.

### A second scenario, where it goes differently

The same skill on a thesis chapter that will never be submitted to a journal, handed to a supervisor next week. Here the desk-reject screen is the wrong instrument, because there is no editor, and running it produces a verdict the student cannot act on and will be demoralised by.

What changes: the screen is replaced by a single question, whether the chapter's claim and its evidence are the same size, and the three referees collapse into two, the methodologist and the field expert. The structural reader's concerns are held back entirely, because a supervisor reading a first full chapter will not care about reference formatting and the student's attention is a scarce resource that should not be spent there. The revision plan has three tiers rather than four, and the effort estimates are stated in days rather than hours, because doctoral students consistently underestimate by a factor of about three.

The register changes too. A referee report is written to an anonymous author who will never meet the referee. A chapter review is read by a person who has to keep working for another two years, and a report that is technically correct and demoralising costs more than it recovers. State what is good, specifically, and state it first.

## Output

Open with one line: the submission verdict.

**Desk-reject screen**

| Question | Answer | Evidence, with location |

Verdict: send to review, or desk reject with the reason in one sentence.

**Referee reports**, three of them, each in this shape:

```
REFEREE [n]: [methodologist / field expert / structural reader]
Recommendation: [accept / minor / major / reject and resubmit / reject]

Summary of the paper in the referee's words
[Three to five sentences: question, data, design, finding, claimed contribution.]

Major concerns
1. [What is wrong] [Where, with page, section, table]
   Consequence for the conclusion: [what changes if this is right]
   What would resolve it: [specific, or "nothing would"]
2. ...

Minor concerns
1. ...
```

**Editor's decision**

The decision, the two or three issues that determined it, and the substance of the decision letter.

**Revision plan**

| Tier | Issue | Fix | Section or exhibit affected | Effort | Raised by |

Tier 1, changes the conclusion. Tier 2, changes the credibility. Tier 3, changes the reception. Tier 4, changes the reading.

## Failure modes

**One report in three voices.** Recognise it when all three referees raise the same concerns in the same order and reach the same recommendation. Real referees have different competences and different obsessions. Rebuild by giving each referee a fixed remit and forbidding them from straying into another's.

**Skimming, then reviewing.** The failure being simulated, reproduced by the simulator. Recognise it when the referee's summary of the paper is a paraphrase of the abstract. Read the whole manuscript first.

**Manufactured concerns to appear thorough.** Recognise it when a major concern has no stated consequence, because there is none. If a section is sound, say so in one line and move on. A padded report trains the author to discount the whole thing, including the two concerns that mattered.

**Vague hostility.** "The contribution is unclear" and "the identification is unconvincing" are not findings. Name the assumption, why it is doubtful in this setting, and what evidence would support it.

**Reviewing the paper you would have written.** Recognise it when a concern amounts to a preference about estimator or framing where the author's choice is defensible. Defensible choices are not concerns. This is scope creep and it is the most common defect of real referee reports.

**Ignoring the venue.** A report calibrated to a top general-interest journal delivered on a paper going to a field journal produces a false rejection and wastes months of unnecessary work. Fix the target before reviewing.

**Confusing what is on the page with what is true.** This skill reads text. A table can be internally consistent and still wrong because the code that made it was wrong. Say so in the report and route to `analysis-audit`.

**Burying the verdict.** Recognise it when the reader has to reach page four to learn whether to submit. The verdict is the first sentence.

## Edge cases

**The paper is a proposal or a registered report, with no results.** The methodologist reviews the design and the power calculation, the field expert reviews the contribution conditional on the result going either way, and the structural reader reviews compliance with the call. The decisive question changes: not whether the evidence supports the claim, but whether any realistic result would be informative. A design that is only interesting if the effect is positive is the finding.

**The paper is qualitative.** The methodologist's remit becomes sampling and case selection logic, saturation, the coding procedure and its reliability, the chain from data extract to interpretation, and reflexivity. Applying quantitative identification language to qualitative work produces a report that is confidently wrong and the author will correctly ignore all of it.

**The result is null.** Review whether the paper is powered to detect an effect worth detecting, whether the null is stated as a finding with a confidence interval rather than as an absence, and whether the framing survives the null. Most null-result papers are rejected for framing, not for the null.

**The author is the person asking, and they are fragile.** The content does not soften. The order does. Lead with what is good and specific, then the tier-one issues, and make it explicit that a reject verdict on a pre-submission simulation is a cheap outcome and the point of the exercise.

**You are one of the authors.** You cannot fully simulate a cold reader on your own work. Compensate by running the desk-reject screen strictly on the text with the intention forgotten, and by taking every concern you dismiss and writing one sentence of defence. If the defence cannot be written, the concern stands.

**A revision after referee reports already exist.** Do not re-run the whole simulation. Review the revision against the real reports first, then run the three referees only on the sections that changed, because new material at the seams is where new problems appear.

## Quality bar

- The submission verdict is the first line of the deliverable.
- The desk-reject screen was run on the abstract, introduction and main table alone, and its answers cite locations.
- Every major concern states its consequence for the conclusion and what would resolve it.
- The three reports disagree somewhere, and the disagreement is visible in their recommendations.
- Each referee's summary of the paper is written in that referee's own words and can be compared against what the author believes the paper says.
- The revision plan is ordered by consequence, not by referee or by section, and every item carries an effort estimate.
- Anything sound is credited in one line rather than passed over, so the criticism is readable.
- Where the numbers were not independently rebuilt, the report says so and names `analysis-audit`.

## Adapting this to your context

The three referee roles, the desk-reject screen and the editor's weighting are modelled on empirical social science journals with two or three referees and a blind process. The adversarial structure carries; the reviewers you should simulate do not.

- **The three referees.** Methodologist, field expert, handling editor. Swap the methodologist for the reviewer your field fields: a statistician in medicine, a psychometrician where the paper rests on a scale, a qualitative methodologist for interpretive work. Add a patient or practitioner reviewer where the journal uses them, now common in health.
- **The desk-reject screen.** Built around fit, contribution and identification. In health and psychology, add what triggers a return before review: missing trial registration, no ethics approval number, no reporting checklist, a structured abstract that does not meet the guidelines.
- **The methodological attack.** Assumes a causal design. For scale-based work the first attacks are common method bias, construct validity, measurement invariance, and whether the model was specified before the data were seen. For qualitative work, expect reflexivity, sampling adequacy and the basis for each theme.
- **Open review.** The file assumes anonymity. Where review is open or signed, or a preprint is public, tone and specificity matter more: write the report you would sign.
- **What not to change.** The desk-reject verdict comes first, the referees are written independently and allowed to disagree, and the revision plan is ordered by consequence.

## Related skills

`identification-defense` supplies the methodologist's attack list and, run first, prevents the most common tier-one finding. `analysis-audit` rebuilds the numbers this skill can only read, and should run in parallel before any submission. `literature-verification` supplies the citation checks the field expert performs. `journal-targeting` runs after this one, using its editor decision as the honest input to the top of the submission ladder. `response-to-reviewers` handles the real reports when they arrive and reuses this skill's ledger discipline. `refereeing-for-a-journal` is the same activity performed on somebody else's manuscript under a journal's invitation, with duties this skill does not have. `thesis-chapter-review` reads a chapter as an examiner rather than as a referee. `thesis-defense-prep` converts these concerns into spoken answers. `full-manuscript-build` performs the restructuring a tier-three finding calls for. `replication-package` closes the project once the paper is accepted.
