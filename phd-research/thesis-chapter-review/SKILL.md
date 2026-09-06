---
name: thesis-chapter-review
description: Reads a thesis chapter or a full thesis the way an examiner reads it and reports findings ranked by consequence: what would fail or require major revision, what is a required correction with a bounded fix, and what is only a preference the author may ignore. Checks that the chapter asks a question and answers it, that the design supports the claim, that the contribution survives the literature actually cited, that the chapters agree with each other, and that every exhibit earns its place, then lists the questions the text invites at the viva in an examiner's own words. Enforces the rule that a preference is labelled as a preference, so the candidate does not spend the final month on the wrong things. Use this skill when someone asks for a chapter or thesis to be reviewed, examined, marked, or pressure-tested before submission or before it goes to a supervisor. Trigger also on vague requests such as "is this good enough", "would this pass", "read this like an examiner", or "what will they attack".
---

# Thesis Chapter Review

An examiner is not a proofreader and not a supporter. They are asking one question in several forms: does this text demonstrate that the candidate can conduct independent research to a standard the field accepts, and can they defend it. Every finding an examiner makes is subordinate to that question, which is why a chapter can be full of small errors and pass, and a chapter can be clean and fail.

The failure this skill prevents is not a bad chapter. It is a candidate who cannot tell a fatal problem from a preference, and who therefore spends the last six weeks before submission reformatting tables and adding citations while the claim that the design cannot support sits untouched in the conclusion. That misallocation is caused directly by the way feedback is normally delivered: a single undifferentiated list of comments, in page order, in which "the identification does not support a causal claim" appears as item 14 between a missing definition and an inconsistent decimal convention.

Ranking by consequence is therefore not a presentational choice. It is the substance of the deliverable, and a review that does not do it has failed regardless of how accurate its individual findings are.

## When to use this, and when not to

Use it before a chapter goes to a supervisor, before a full thesis goes to examiners, before a progress review or upgrade panel, and when a candidate wants to know whether a chapter is finished. Use it on a full thesis at least once, because chapter-level problems are frequently invisible within the chapter and obvious against the rest of the document: the same variable defined two ways, a result in chapter three that contradicts a claim in chapter five, an introduction promising a contribution the chapters do not deliver.

Use it on somebody else's thesis when you have been asked to examine it, adapting the report to whatever form the institution requires.

Do not use it to decide what to work on next, whether the scope fits the remaining time, or what to cut. That is `thesis-advisor`, and the two skills routinely disagree: this one will find work that ought to be done, and the supervisor's view may correctly rule it out because the calendar does not allow it. A candidate should run both and reconcile them, using this skill's consequence ranking as the input to the other's triage.

Do not use it to referee a journal submission, which is `peer-review-simulator` for your own paper and `refereeing-for-a-journal` for somebody else's. A journal asks whether an article is publishable; an examiner asks whether a candidate has demonstrated capability, and those diverge. A chapter can be unpublishable in its target journal and entirely examinable, and a competent replication can be publishable and fail as a doctoral contribution.

Do not use it to rehearse spoken answers, which is `thesis-defense-prep`. This skill generates the questions; that one prepares the answers and the room.

Do not use it to verify that the numbers are correct, which requires rebuilding them from data; that is `analysis-audit`.

## What you need before starting

**The chapter, complete, with tables, figures and appendix.** Missing: review what exists and state at the top which parts were absent, because an examiner reaching a missing section stops evaluating the argument and starts evaluating the candidate's readiness.

**The rest of the thesis, or at minimum its abstract and chapter summaries.** Internal consistency is one of the eight things examined and it cannot be checked on a single chapter in isolation. Missing: review the chapter alone, say so explicitly, and flag consistency as unassessed rather than passing over it.

**The institution's examination criteria and thesis regulations.** What constitutes a pass, what corrections categories exist and what each permits, length limits, and whether the thesis is by publication. Missing: use the general standard of the discipline and state the assumption, because the corrections categories differ enough between institutions to change how findings should be sorted.

**The field and the intended examiners' likely orientation.** A methodologist and a field specialist examine the same chapter differently. Missing: review to both orientations and mark which findings arise from which, which is more useful than a single averaged view.

**The stated contribution, in the candidate's own words.** Missing: extract the best candidate sentence from the text and quote it back. If no such sentence can be found, that is the first finding and it is usually a major one.

**Whether the numbers have been independently checked.** Missing: assess only internal consistency, and add a line stating that the underlying computations were not verified and that `analysis-audit` should run before deposit.

## The method

1. **Read the whole text before writing anything.** For a full thesis this is a day. Findings drafted during a first read are almost always findings about the reader's confusion at that point, which the next chapter resolves, and a review full of those loses the candidate's trust in the ones that matter.

2. **Extract the spine and lay it out on one page.** The question as stated in the introduction, the hypotheses, the specifications actually estimated, the tables presented, and the claims made in the conclusion. Put them side by side. Drift between these five is the single most common serious finding in doctoral work, it is invisible to the author who has been inside the document for two years, and it is immediately visible to anyone reading cold. A hypothesis that no table tests, or a conclusion that claims something the question did not ask, is found here in ten minutes and nowhere else.

3. **Examine the eight dimensions** set out below, in that order. The order matters: the question and the answer come before the design, because a chapter with no question cannot have its design assessed against anything.

4. **Assign every finding a consequence category** as it is made, using the rule below, and never defer this to a sorting pass at the end. A finding whose category is unclear is nearly always a required correction, and saying so is more honest than promoting it.

5. **For every fatal or major finding, state the smallest change that fixes it.** Not the best change, the smallest sufficient one. Examiners and supervisors both tend to describe the ideal remedy, which for a candidate with eight weeks left is equivalent to describing no remedy. Where the smallest sufficient fix is to reduce the claim rather than to strengthen the evidence, say so explicitly, because candidates rarely consider that route and it is frequently the right one.

6. **Check consistency across chapters** where the full thesis is available: definitions, sample sizes, variable construction, notation, and whether any two chapters' results can both be true.

7. **Generate the viva questions**, ten to fifteen per chapter, in an examiner's words, ordered by likelihood of being asked first. Include the two or three the text appears designed to avoid, which is where the defence will actually be fought.

8. **Write the summary judgement in one paragraph at the top**: whether, as it stands, this would pass, pass with corrections, or require major revision, and the two or three findings that determine that. A review whose overall verdict has to be inferred from the length of its list is not usable.

## What is examined

**The question.** Is there one, stated in a single sentence, and is it a question rather than a topic. A chapter about a subject cannot fail well or succeed well because there is nothing to be right about. The test: could two competent researchers give different answers to it, and would evidence distinguish them?

**The answer.** Does the chapter answer the question it asked, in the conclusion, in words, without retreating into a summary of what was done. Where the answer is negative or partial, is it stated as a finding rather than buried in a paragraph about limitations. A conclusion that lists activities rather than stating a result is a reliable signal that the candidate is not certain what they found.

**The design.** Does the method support the claim being made. This is where most theses are actually decided. The examiner's questions are: what would have to be true for this estimate to mean what the text says it means, has that been argued or merely assumed, what is the most obvious rival explanation, and where in the text is it addressed. A chapter that never names its own identifying assumption is not defending a weak design, it is failing to show that the candidate knows a design needs one.

**The contribution.** Stated explicitly, and defensible against the literature actually cited in the chapter rather than against the literature in general. Being first in a setting is a contribution only if the setting changes something; if the contribution is that nobody has studied this country, the examiner will ask why that matters and the text must already answer. The examiner's harshest version of this question is whether, if every result here is correct, anything in the field changes.

**Internal consistency.** The five elements from the spine must be the same object throughout. Also: does the chapter agree with the other chapters, is the same variable constructed the same way, do the sample sizes reconcile, and can the results in two chapters both be true simultaneously.

**Evidence to claim.** Every claim in the text traces to a number in a table or a figure. Every table and figure is referred to in the text and does work. Anything appearing in only one direction is a finding: an unsupported claim, or an exhibit that should be cut or moved to an appendix.

**Limitations.** Stated by the candidate before the examiner states them, and stated at the size they actually are. A limitations section listing sample size and generalisability while ignoring the identification problem reads as either unaware or evasive, and both are worse than the limitation itself. The examiner's inference from an honest limitations section is that the candidate understands their own work; that inference is worth more in a viva than most of the results.

**Scholarly apparatus.** Citations that exist and support what they are cited for, notation defined at first use and used consistently, tables readable without the surrounding text, figures legible in monochrome with legends outside the plot area, and a reference list that matches the citations in both directions.

## Ranking findings by consequence

**Would fail or require major revision.** The claim the design cannot support. The question the chapter does not answer. The contribution that does not survive the literature cited. A result that contradicts another chapter. An analysis whose sample or construction is wrong in a way that changes the estimate. Each one with what is wrong, why it is fatal, and the smallest change that fixes it, including reducing the claim.

**Required corrections.** Real problems with bounded fixes, of the kind an examiner would list as corrections: a diagnostic an examiner will certainly ask for, an unsupported sentence, a table that does not show what the text says it shows, an undefined term, a limitation not acknowledged, a citation that does not support its claim. These are the bulk of a normal review and they are what corrections periods exist for.

**Preferences.** Say plainly that these are preferences and that the author may ignore them. Alternative framings, a table the reviewer would have built differently, a section order, a stylistic habit. Mixing these into the first category is the most common way a review does damage, because it teaches the candidate that everything is equally urgent, and under deadline they will do the cheap items first.

Where a finding sits between categories, place it lower and say why. An inflated review is discounted wholesale.

## The viva questions

Ten to fifteen per chapter, in the words an examiner would use rather than in the reviewer's analytical vocabulary. "Why should I believe the regions that adopted early were on the same trajectory as the ones that did not?" is an examiner's question. "The parallel trends assumption is not defended" is a finding, and the candidate cannot rehearse against it.

Order them by likelihood of being asked in the first twenty minutes, which is when the tone of a viva is set.

Include, and mark, the two or three questions the text appears to be avoiding: the result presented without comment, the specification mentioned once and never returned to, the appendix table whose implication is not discussed. Examiners find these reliably, because a paragraph that changes its footing is visible to a reader who has no investment in the argument.

## Tone

Direct about the work, never about the person. There is no anonymity here: the candidate usually knows who wrote the review and has to keep working for months afterwards.

No praise that is not specific. Generic encouragement makes the criticism unreadable, because the candidate cannot tell which parts were sincere. Where something is genuinely well done, say what and why, because during revision a candidate will change things that were not broken unless they know what to protect.

State the verdict plainly. A candidate who reads a review and cannot tell whether the chapter is in trouble will assume the worst, which is both demoralising and frequently wrong.

## Worked example

**Situation.** A third-year candidate, Ruth Adeyemi, sent chapter three of a four-chapter thesis, 41 pages, before sending it to her supervisor. The chapter asked whether a national teacher retraining programme improved student attainment. Administrative data, 3,100 schools, five years, a difference-in-differences design on programme rollout, headline estimate of 0.07 standard deviations on a national test, standard error 0.02. Chapters two and four were available in draft.

**Task.** An examiner's read, ranked by consequence, with viva questions, three months before the intended submission.

**Action.** The full read took four hours. The spine was extracted onto one page and produced the first major finding immediately. The introduction asked whether retraining improved attainment. Three hypotheses were stated, of which the third concerned differential effects by school socioeconomic composition. Four specifications were estimated. The tables presented six results. The conclusion claimed that retraining improved attainment and that it narrowed the attainment gap between advantaged and disadvantaged schools.

The gap-narrowing claim was tested nowhere. Table 5 showed effects estimated separately for two school groups, 0.09 and 0.05, with standard errors of 0.03 and 0.04, and no test of the difference between them. The difference was not distinguishable from zero on any reasonable test, and the conclusion had converted two separately estimated coefficients into a claim about their difference. This is an extremely common error, it is invisible to an author who has looked at the table for a year, and an examiner with any quantitative background finds it in the first pass.

Categorised as fatal, because it was a claim the evidence did not support, and it appeared in the abstract as well. Smallest sufficient fix: not more analysis. Test the difference, report the interaction coefficient with its standard error, and rewrite the claim to say that the point estimates are larger in disadvantaged schools but the difference is not statistically distinguishable. Two hours of work and a rewritten paragraph.

The second major finding was the design. The chapter described the rollout as phased by administrative region and treated it as quasi-random. The institutional background section, three pages earlier, said that regions were prioritised partly on the basis of prior attainment. The chapter did not connect these two statements and never named the identifying assumption. Categorised as major. Smallest sufficient fix: name the assumption, present the event study that already existed in the appendix in the main text, and add one paragraph on why prioritisation on prior attainment does or does not threaten it, with an honest concession if it does.

Nine required corrections, including a variable, teacher experience, constructed differently in chapter three than in chapter two, which was only visible because both chapters were available; a figure whose legend sat inside the panel and covered two points; and two claims in the discussion with no supporting exhibit.

Six preferences, clearly labelled, including a suggestion about section order that the review explicitly said could be ignored.

**The wrong turn.** The first draft of the review had eleven items in the major category, including "the robustness section does not consider an alternative estimator for staggered adoption" and "the mechanism is asserted rather than tested". Both are true and both are the kind of thing a good examiner might raise. Neither is fatal: the estimator question would change a robustness table, and the mechanism claim could be softened in a sentence. Promoting them meant the review presented eleven roughly equal crises, and when it was read back, the two findings that actually determined whether the chapter passed were no longer visible.

They were demoted to required corrections and the major list dropped to two. That was the review's real contribution. The candidate later said the two-item major list was what made the chapter fixable rather than overwhelming.

**Result.** The gap-narrowing claim was corrected in an afternoon. The identification paragraph took a week, including a placebo test the candidate ran unprompted after writing the concession, which strengthened the argument. Chapter three went to the supervisor two weeks later. Of the fourteen viva questions supplied, five were asked at the actual viva nine months later, including the highest-ranked one, which was about regional prioritisation. The candidate passed with minor corrections.

The finding that mattered most was found by a mechanical step: putting the question, hypotheses, specifications, tables and conclusion on one page next to each other. It took ten minutes and no expertise.

### A second scenario, where it goes differently

A qualitative chapter in a sociology thesis: 38 interviews, thematic analysis, a claim about how mid-career workers interpret automation risk.

The eight dimensions hold but four of them change substance entirely. The design dimension becomes sampling and case selection logic, whether saturation was reached and how that was judged, how the coding scheme was developed and whether anyone else applied it, and the chain from a data extract to an interpretive claim. The evidence-to-claim dimension asks whether each interpretive claim is illustrated by extracts that actually show it, and whether negative or disconfirming cases are presented rather than only supporting ones, which is the qualitative equivalent of a robustness check and the thing weak qualitative chapters most reliably omit. The limitations dimension asks about the researcher's position relative to the participants and whether reflexivity is done or merely announced. The internal consistency dimension asks whether the themes reported are the themes the coding scheme would produce.

The failure to avoid is importing quantitative vocabulary. Asking a thematic analysis about external validity, or about whether 38 interviews is a large enough sample in a statistical sense, produces a review that is confidently wrong and that a competent candidate will correctly discount in full, including the parts that were right.

The consequence ranking works identically, which is the point: the fatal findings in a qualitative chapter are the same shape, a claim the evidence cannot carry and a question the chapter does not answer.

## Output

Open with the summary judgement in one paragraph: pass, pass with corrections, or major revision as it stands, and the two or three findings that determine it.

**The spine**

| Element | As stated | Location |
| Question | | |
| Hypotheses | | |
| Specifications estimated | | |
| Exhibits presented | | |
| Claims in the conclusion | | |

With any drift between rows marked.

**Findings, ranked by consequence**

```
WOULD FAIL OR REQUIRE MAJOR REVISION
1. [What is wrong] [Page, section, table]
   Why it is fatal: [...]
   Smallest sufficient fix: [...] [including reducing the claim, where that is the fix]

REQUIRED CORRECTIONS
1. [Page] [Issue] [Fix]

PREFERENCES, WHICH THE AUTHOR MAY IGNORE
1. [...]
```

**Cross-chapter consistency**, where the full thesis was available:

| Item | Chapter | Chapter | Discrepancy |

**Viva questions**

| # | Question, in an examiner's words | Chapter and section it arises from | Avoided by the text? |

**What is well done**, three to five specific items, so the candidate knows what to protect during revision.

## Failure modes

**One flat list in page order.** Recognise it when the review's first item is on page two rather than being the most serious thing found. Rank by consequence, always.

**An inflated major category.** Recognise it when more than about four items are fatal. Ask of each: would a competent examiner refuse to pass this? Demote everything else.

**The ideal fix rather than the smallest one.** Recognise it when the remedy would take a month. State the smallest sufficient change, and consider whether reducing the claim is that change.

**Reviewing the chapter you would have written.** Recognise it when a finding amounts to a different research design. That is a preference unless the chosen design cannot support the claim.

**Preferences unlabelled.** Recognise it when the candidate cannot tell from the text which items are optional. Label them and say explicitly that they may be ignored.

**Missing the spine drift.** Recognise it when the review has no cross-check between the question, the hypotheses, the tables and the conclusion. This step finds the most serious findings and takes ten minutes.

**Reviewing a chapter in isolation when the thesis was available.** Recognise it when consistency findings are absent. Half of a thesis's real problems live between chapters.

**Generic praise.** Recognise it in any sentence that would apply to any chapter. Name what is good and why, or say nothing.

**Confusing publishability with examinability.** Recognise it when a finding is about journal fit or novelty for a literature rather than about demonstrated capability. Those belong to `journal-targeting` and `peer-review-simulator`.

## Edge cases

**The chapter is a published paper.** It passed peer review, which examines a different question. Examine what the thesis regulations require: the candidate's own contribution where there are coauthors, whether the chapter connects to the thesis argument, and whether the linking material does the work. Do not re-referee the paper; that is settled.

**The chapter is a literature review or a theoretical chapter.** The design dimension becomes the selection and organisation of the literature: is the scope stated, is the selection reproducible in principle, is it organised by argument rather than by author, and does it end in a gap that the empirical chapters actually address. The commonest fatal finding here is a review that is a summary rather than an argument.

**The result is null.** Examine whether the chapter is powered to detect an effect worth detecting, whether the null is stated as a finding with an interval rather than as an absence, and whether the framing survives. A well-executed null is examinable; an underpowered null presented as evidence of no effect is a fatal finding.

**The candidate is in serious difficulty and the review will be the third piece of bad news.** The content does not change. Lead with the specific things that are good, state the verdict plainly, keep the major list to what is genuinely fatal, and make it explicit that these findings are cheap now and expensive at the viva. Route the workload question to `thesis-advisor`, because a candidate in difficulty needs a triage more than they need a longer list.

**You are also the supervisor.** Say which hat you are wearing, and run both readings separately. The examiner's read produces the findings; the supervisor's read decides which of them there is time for. Delivering a blended view leaves the candidate unable to tell what is required and what is advisable.

**Submission is in two weeks and cannot move.** Report the fatal findings and the corrections that can be made in the time, and say plainly which fatal findings cannot be fixed and will therefore be met at the viva. A candidate who knows a question is coming can prepare an honest answer to it, and an honest answer to a known weakness is survivable in a way that surprise is not.

**The thesis is by publication and chapters were written years apart.** Consistency findings dominate: notation, definitions, and whether the earliest chapter's claims survive what the later ones found. The linking introduction is where an examiner decides whether this is a thesis, so examine it as hard as any empirical chapter.

## Quality bar

- The summary judgement is the first paragraph and names the two or three findings that determine it.
- Findings are ranked by consequence, with fatal separated from required corrections and from preferences.
- Preferences are labelled as preferences and the author is told they may be ignored.
- Every finding points to a specific page, table, or sentence.
- Every fatal finding carries the smallest sufficient fix, including reducing the claim where that is the fix.
- The spine was extracted and any drift between question, hypotheses, specifications, exhibits and conclusion is reported.
- The viva questions are in an examiner's words and the ones the text avoids are marked.
- Three to five specific things that are well done are named, so the candidate knows what to protect.

## Related skills

`thesis-advisor` triages these findings against the time available and decides which are worth doing; run both and reconcile them. `thesis-defense-prep` converts the viva questions here into rehearsed spoken answers with an exhibit to point to. `identification-defense` supplies the attack list behind the design dimension and builds the response to a major finding about identification. `analysis-audit` verifies the numbers this skill can only read for internal consistency, and should run before deposit. `literature-verification` checks the citations behind the contribution finding. `peer-review-simulator` asks whether a chapter is publishable, a different question from whether it is examinable. `refereeing-for-a-journal` applies a journal's criteria to somebody else's paper. `replication-package` closes the project and is a deposit requirement at many institutions.
