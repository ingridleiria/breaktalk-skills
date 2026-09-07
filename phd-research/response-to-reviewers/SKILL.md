---
name: response-to-reviewers
description: Builds the point-by-point response letter and the revision it documents, deciding for every referee comment whether to comply, partially comply with a justified alternative, or decline with evidence, and producing a comment ledger in which nothing is unanswered and every claimed change points to a location an editor can check. Enforces the rule that no change is claimed that was not made, that every decline carries evidence rather than an argument, and that the editor's own priorities override the referees' where they conflict. Use this skill when referee reports arrive and someone asks to answer the reviewers, write the response letter, handle an R and R, decide whether to revise or take the paper elsewhere, or draft an appeal. Trigger also on vague requests such as "we got a major revision", "reviewer 2 wants something impossible", "how do I say no to a referee", or "the editor sent this back".
---

# Response to Reviewers

A revise-and-resubmit is a conditional offer, and the response letter is the document that proves the conditions were met. Editors read it before they reread the paper, and often instead of rereading most of the paper. Referees read it to decide whether to fight. It is therefore the single highest-leverage document in the publication process and the one authors write last, tired, in a weekend, after the revision is already done.

The failures are specific and they are all recoverable if caught before sending. A comment answered in the letter but not actually changed in the manuscript, which editors check and which destroys credibility for every other answer in the document. A comment quietly skipped because it was hard, which the referee who wrote it will notice immediately. A refusal argued from conviction rather than evidence, which converts a sympathetic referee into a hostile one. A tone that is either defensive or so effusive that it reads as anxiety. And the structural failure underneath all of them: the author treated twenty-three comments as a pile rather than as a numbered list, and lost four of them.

A second-round rejection after a major revision is the most expensive outcome in academic publishing. It consumes six to twelve months, it usually cannot be appealed, and the paper arrives at the next journal with a revision history that satisfied nobody.

## When to use this, and when not to

Use it for any decision letter that invites resubmission, whether labelled minor revision, major revision, or reject and resubmit. Use it when the reports are contradictory and the author cannot see how to satisfy both. Use it when a comment demands something infeasible and the author needs to decline without losing the paper. Use it for a committee's required revisions after a defence, which behave identically. Use it when deciding whether to revise at all or take the paper elsewhere, which is a decision this skill makes explicitly rather than by drift.

Use it also for an appeal, under the narrow conditions set out below.

Do not use it before submission to anticipate what referees will say; that is `peer-review-simulator`. Do not use it to write a report on somebody else's paper; that is `refereeing-for-a-journal`. Do not use it to choose the next venue after a rejection that does not invite resubmission; that is `journal-targeting`. Do not use it to perform the analysis a referee asked for, which is real work in `analysis-audit`, `identification-defense`, or the relevant estimation skill; this skill decides what to do and documents that it was done.

If the required revision amounts to a different paper and the honest answer is to withdraw, this skill says so; it does not manufacture compliance with a request that cannot be met.

## What you need before starting

**The editor's letter and every referee report, complete.** Not a summary, not the author's recollection of the main points. Missing: ask for the originals. The editor's letter in particular contains the priorities that override everything else, and it is the document authors most often skim.

**The submitted version of the manuscript, and the code and data behind it.** Every rerun analysis has to start from what was actually submitted, not from a working copy that has drifted since. Missing: reconstruct the submitted version from the portal before touching anything, and note any difference found, because a difference between the submitted file and the working file is itself a problem.

**The journal's resubmission rules.** Deadline, length limits for the response letter where they exist, whether tracked changes are required, whether the response goes in a separate file or in the manuscript, and whether the same referees will see it. Missing: fetch the guidelines; where no live lookup is available, produce both a tracked and a clean version, keep the letter under about fifteen pages, and note the assumption.

**An honest read of the editor's enthusiasm.** A letter saying the paper is promising and the concerns are addressable is different from one saying the referees have raised substantial concerns and a revised version would be considered without commitment. Missing: read the verbs. Editors signal deliberately and authors read optimistically.

**Capacity and calendar.** Who will do the reruns, by when, and what else is due. Missing: establish it before promising the editor a timeline, because an extension requested at the start is granted routinely and one requested a week after the deadline is not.

**The referees' identities, where guessable.** Not to flatter them, but because a referee who is plainly the author of a paper you criticised needs a more careful and more evidenced response. Missing: proceed without speculating in writing. Never name a guessed referee in the letter.

## The method

1. **Read everything twice, and do not start work for a day.** The first read produces the emotional response, which is universal and useless. The second read, made after a night, finds that roughly half of what felt like hostility is a request for clarification, and that the two comments that matter were stated calmly in the middle of the report. Authors who begin the ledger during the first read produce a defensive letter.

2. **Classify the decision and extract the editor's priorities.** Which category the letter falls into, and which two or three points the editor named as theirs. Editor priorities are mandatory. Where the editor and a referee conflict, follow the editor and say in the letter that you have done so, courteously and explicitly, because the referee will otherwise read it as being ignored.

3. **Decide whether to revise here or go elsewhere, and state the recommendation with reasons.** Revise when the concerns are addressable with the data you have, the venue remains right, and the editor's letter carries enthusiasm. Go elsewhere when the referees are asking for a different paper, when the required work exceeds the value of this venue over the next one, or when a reject-and-resubmit letter reads as a decline written politely. Say which and why in one paragraph. The failure mode here is drift: nine weeks of work begun without ever making this decision.

4. **Build the comment ledger before writing a word of the letter.** Every distinct comment from every source becomes a numbered row, including the small ones and including comments embedded mid-paragraph, which is where authors lose them. Columns: source, the comment quoted in full, category, severity, disposition, the action taken, and the location of the change. Where two referees raise the same issue, link the rows, answer once in full, and cross-reference the second, saying so explicitly.

5. **Set each disposition honestly, using the rule below.** Do this for the whole ledger before doing any of the work, because the shape of the revision is decided by the pattern of dispositions and doing them one at a time in report order produces an incoherent manuscript.

6. **Do the work, and keep the ledger updated as you go.** Every rerun analysis regenerates its exhibit from code. Every new number propagates to the abstract, introduction, results, discussion and every table where it appears. The location column is filled in as each change lands, not reconstructed at the end from memory, which is how a claimed change with no corresponding edit gets into a letter.

7. **Write the letter from the completed ledger.** Structure below. The letter is a rendering of the ledger, which is why the ledger is built first.

8. **Run the consistency and verification passes.** Every number in the revised manuscript agrees everywhere it appears. Every claimed change exists at the location claimed, checked by opening the file at that location. Every new citation is verified against a real record. Any change to the analysis propagates into the replication package.

9. **Re-review the revised manuscript adversarially.** Revisions introduce new problems, most often at the seams where new material was added and where a number changed in one place and not another. Run `peer-review-simulator` on the revision, restricted to what changed.

10. **Submit with a short cover note to the editor** naming the two or three most substantial changes in three sentences, so the editor knows what to look at first.

## The disposition rule

**Comply** when the referee is right, or when the change is cheap and harmless even if you disagree. The great majority of comments belong here, and treating them so is not weakness; a letter with twenty-one complies and two evidenced declines reads as competence, while a letter with eight declines reads as a fight.

**Partially comply** when the concern is legitimate but the proposed remedy is wrong, infeasible, or would damage the paper. Address the concern by another route and explain the substitution in one sentence: what the referee was worried about, what you did instead, and why it addresses the worry. This is the disposition authors underuse, and it resolves most apparent impasses.

**Decline** only with evidence, and evidence means one of exactly four things: a result already in the paper or newly added that shows the concern does not change the conclusion; a citation, verified, that the referee appears not to have seen; a documented feature of the data or the setting that makes the request impossible, stated plainly and added to the limitations; or an explicit instruction from the editor that supersedes the request. Conviction is not evidence. "We respectfully disagree" without one of those four is the most reliable route to a second-round rejection.

Never claim a change that was not made. Editors check, referees check the parts they wrote, and one discovered false claim retroactively discredits every other answer in the letter.

Never make an undisclosed change either. A specification quietly altered, a sample redefined, an outlier rule introduced: all of these must appear in the letter, because a referee who finds an unannounced change assumes the worst about why it was made.

## The letter

1. **Opening paragraph.** Thanks stated once, briefly. Three to five sentences summarising the substantial changes. A note of where the tracked and clean versions are. Nothing else. Long openings delay the editor's first useful information.
2. **Response to the editor**, first, point by point.
3. **Response to each referee in turn**, in the journal's numbering. Each comment quoted verbatim and set off visually, followed by the response, followed by the exact change with its location: section, page, table or figure number. Where the change is a sentence or two, quote the new text so the editor does not have to open the manuscript.
4. **Summary of changes not requested**: updated data, corrected errors found during the revision, added citations, anything that moved. List them briefly. An editor who finds an unexplained change is entitled to wonder what else moved.

Tone: respectful, direct, unornamented. Address the argument, never the referee. Do not thank a referee for each individual comment, which reads as nervousness by the fourth repetition. Do not apologise more than once. Do not call a comment insightful. Where you agree, say so and move to the change. Where you disagree, open with what you accept before stating what you do not.

Length: the editor should get the shape of it in ten minutes and each referee should find their own section in five. Anything that cannot be said briefly goes into an appendix to the letter, which is a normal and accepted device.

## Worked example

**Situation.** A two-author paper on hospital consolidation and patient outcomes received a major revision from a health policy journal after five months. Three referees, thirty-one distinct comments, and an editor's letter naming two priorities: the definition of the treated market, and whether the outcome measure was comparable across the consolidation event. The first author, Priya Raman, was on the job market with a February deadline. The reports arrived in October and the journal allowed ninety days.

**Task.** A resubmission by early January, with every comment answered and the two editor priorities addressed to the editor's satisfaction.

**Action.** The ledger came to thirty-one rows, which was already more than the twenty-something the authors had counted from a first read; four comments had been embedded in the middle of Referee 2's paragraphs and would have been missed. Dispositions: twenty-two comply, six partially comply, three decline.

The two editor priorities were placed first. The market definition comment was a comply: the authors rebuilt the market definition on a different geographic unit, reran everything, and the headline estimate moved from a 4.2 percent reduction in the readmission rate to 3.6 percent, standard error 1.1. That change then had to propagate through the abstract, two paragraphs of the introduction, four tables, one figure, and the discussion, which took a full day on its own and is the step that is usually underestimated.

The three declines were the difficult part. Two were straightforward and evidenced: Referee 1 asked for a robustness check that already existed in the appendix, so the response pointed to Table A7 and moved the reference into the main text so the next reader would find it; Referee 3 asked for a patient-level analysis that the data licence did not permit, which was documented with the licence clause and added to the limitations.

**The wrong turn.** The third decline was Referee 2's request for an instrumental variables specification alongside the difference-in-differences design. The authors drafted a decline arguing that no valid instrument existed in this setting and that the difference-in-differences design was preferable on its merits. The draft was three paragraphs, well argued, and entirely unevidenced. It was abandoned after asking the question this skill forces: which of the four kinds of evidence supports this. None of them did.

The disposition was changed to partial compliance. The authors implemented the weakest defensible version of the requested instrument, reported it in an appendix table with its first-stage F statistic of 4.1, and wrote two sentences saying that the instrument was too weak to support inference and that they were reporting it because the referee asked, with the point estimate directionally consistent with the main result. That response occupied eight lines instead of three paragraphs, and it converted the comment from an argument into a documented dead end that the referee could verify.

The second draft of the letter ran nineteen pages, mostly from quoting the authors' own new text at length. It was cut to eleven by moving the long quotations into an appendix to the letter and leaving location references in the body.

**Result.** Resubmitted on day 84. Second-round reports came back in nine weeks: Referee 1 satisfied, Referee 3 satisfied, Referee 2 accepting the weak-instrument response explicitly and noting that the appendix table was the right way to handle it. Accepted with minor revisions in the second round. The paper was in press before the job market ended.

The decision that mattered was converting the one argued decline into an evidenced partial compliance. On the authors' own reading afterwards, the abandoned three-paragraph decline would probably have produced a hostile second report from the referee who wrote the request.

### A second scenario, where it goes differently

A reject-and-resubmit where the reports demand a different paper. Two referees ask for a different dependent variable and a different theoretical framing; complying would take a year and produce work the authors do not want to do.

Here the method stops at step three and produces a decision rather than a letter. The ledger is still built, because it is the only way to see the scale of what is being asked, and it showed that eleven of nineteen comments were about the framing rather than the execution. The recommendation was to withdraw and retarget, and the letter written was a two-paragraph note thanking the editor and declining to resubmit, which costs nothing and keeps the relationship.

What changes: the ledger becomes an input to `journal-targeting` rather than to a revision. The comments classified as execution problems become the revision plan for the next submission, because they will be raised again wherever the paper goes. The comments classified as framing become evidence about which venues will not take the paper as conceived.

The mistake to avoid in this scenario is a partial revision that satisfies neither the old referees nor the new venue: eight weeks of work responding to referees who will never see it again, on a paper going somewhere with different expectations.

## Output

**The comment ledger**

| # | Source | Comment, quoted in full | Category | Severity | Disposition | Action taken | Location in revision |

Categories: identification, estimation, data, literature, framing, interpretation, writing, exhibit, compliance. Severity: must address, should address, optional. Disposition: comply, partially comply, decline.

**The response letter**

```
Response to reviewers: [manuscript title], [journal], MS reference

[Opening: thanks once, three to five sentences of substantial changes, where the
tracked and clean versions are.]

RESPONSE TO THE EDITOR
E1. [Editor's point, quoted]
    Response: [...]
    Change: [section, page, table] [new text quoted where short]

REFEREE 1
1.1 [Comment, quoted verbatim]
    Response: [...]
    Change: [location] or, where declined, the evidence

REFEREE 2 ...

OTHER CHANGES NOT REQUESTED
[Brief list.]
```

**The delivery set**: tracked-changes manuscript, clean manuscript, regenerated exhibits, an updated replication package where any analysis changed, and a three-sentence cover note to the editor.

## Failure modes

**A comment lost.** Recognise it by counting: the number of rows in the ledger against the number of numbered points in the reports plus the unnumbered ones found by rereading the paragraphs. Referees notice their own missing comment before anything else in the letter.

**A claimed change that does not exist.** Recognise it by opening the manuscript at every location cited in the letter, one at a time. This check takes an hour and prevents the worst available outcome.

**An unevidenced decline.** Recognise it when the response runs longer than one paragraph and contains the word "however" more than once. If none of the four kinds of evidence applies, convert it to a partial compliance.

**Answering the referee rather than the argument.** Recognise it in phrases such as "the referee appears to have misunderstood". Rewrite as a statement about the paper: "This was not clear in the submitted version; Section 3.2 now states ..."

**Numbers that moved and did not propagate.** Recognise it by searching the revised manuscript for the old figure. A revision that changes an estimate changes it in six to ten places, and the abstract is the one most often missed.

**The unannounced change.** Recognise it by diffing the submitted and revised versions and checking every difference against the ledger. Anything not in the ledger goes into the "other changes" section.

**Effusiveness.** Recognise it by counting the words "grateful", "insightful" and "excellent". Once each in the opening is the budget.

**Revising without deciding to revise.** Recognise it when work has started and nobody has written the paragraph in step three. Stop and write it.

## Edge cases

**Referees contradict each other.** Say so explicitly in the letter, quote both, and explain the route chosen. Where the editor named a priority that resolves it, cite the editor. Where they did not, choose the option that is defensible on the evidence, implement the other in an appendix where feasible, and let both referees see that their concern was taken seriously.

**The comment rests on a factual error about your paper.** Comply with the underlying concern anyway, then note the point of fact neutrally: "Section 2 (page 7) does report the balance test; we have moved it forward to make it easier to find." Never write that the referee did not read the paper, even when it is obviously true.

**The requested analysis is impossible under the data licence or ethics approval.** Decline with the clause quoted, add it to the limitations, and where possible offer a bounded substitute on the data you do have. Naming the restriction precisely is what makes this decline credible.

**A comment requests a citation to what is transparently the referee's own work.** If it genuinely bears on the argument, cite it, and move on; the cost of one citation is far lower than the cost of the fight. If it does not, decline in one sentence on relevance grounds, without commenting on the apparent motive.

**The deadline cannot be met.** Ask for an extension before the deadline, with a specific new date and a one-line reason. Editors grant these routinely. Silence past the deadline is what converts an R and R into a new submission.

**An appeal.** Only when the decision rests on a demonstrable factual error by a referee or editor, and only in one page: the error, the evidence, and a request for reconsideration. Appeals against judgement fail, take two months, and spend goodwill with an editor you may need again. Where the appeal is warranted, write it as a short factual note rather than an argument, and state that you will accept the outcome either way.

**Coauthors disagree about a disposition.** Settle it on the ledger, not in the letter. Each disputed row gets the evidence for both positions written out, and the decision rule is which position can be evidenced under the four-part test. That usually ends the disagreement without anyone having to concede on preference.

## Quality bar

- Every distinct comment from every source appears as a numbered row in the ledger and as a numbered response in the letter.
- Every comply corresponds to a change that exists at the location named, verified by opening the file there.
- Every decline carries one of the four kinds of evidence, named.
- The editor's stated priorities are answered first and are visibly satisfied.
- Every number in the revised manuscript agrees across the abstract, text, tables and figures.
- Changes not requested by anyone are disclosed in their own section.
- The letter contains no sentence about a referee, only sentences about the paper.
- The decision to revise here rather than elsewhere was made explicitly, in writing, before the work began.

## Adapting this to your context

The example is a health policy journal, three referees, thirty-one comments, ninety days. The ledger and the disposition rule travel; the calendar and the evidence do not.

- **The revision window.** Ninety days is generous. Many psychology and medical journals allow thirty to sixty, some twenty-one for a minor revision. Check the letter before planning reruns: an extension is routine only before the deadline.
- **What counts as evidence for a decline.** The four kinds hold, but the documents differ. Outside economics the strongest declines cite the preregistration, a reporting guideline item such as a CONSORT or PRISMA requirement, the ethics protocol, or the instrument's published validation. Name the document, not the reasoning.
- **What referees ask for.** Here, an instrumental variables specification. In psychology, a mediation test, a Bayes factor or a preregistered replication; in health, a sensitivity analysis; in qualitative work, a second coder with an agreement statistic or member checking. Partial compliance works on all of them.
- **The response format.** Some journals require per-comment boxes with a character limit; open-review venues publish the letter with the paper. Build the ledger first regardless, then render it into what the portal wants.
- **What not to change.** Never claim a change that was not made, never make one undisclosed, and never decline without one of the four kinds of evidence.

## Related skills

`peer-review-simulator` anticipates these reports before submission and, run again on the revision, catches what the revision broke. `identification-defense` produces the evidence for methodological complies and declines. `analysis-audit` reruns the numbers a referee has queried and catches the discrepancy that a rerun exposes. `literature-verification` verifies every citation added during the revision, including any the referee suggested. `journal-targeting` takes over when the decision is to go elsewhere, and takes the ledger as its input. `full-manuscript-build` performs a restructuring that goes beyond a section-level change. `replication-package` is updated whenever a revision changes any analysis, and closes the project at acceptance. `thesis-defense-prep` uses this same ledger discipline for a committee's required revisions.
