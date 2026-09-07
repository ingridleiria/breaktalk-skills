---
name: full-manuscript-build
description: Runs a complete journal article or thesis chapter end to end rather than one section at a time: fixes the target, the claim sentence and the per-section word budget before any drafting, builds the exhibits first, writes the sections in the order that keeps the argument consistent, hands each one to its section skill with the same brief, then runs the cross-section checks that catch the drift a section-by-section process always produces. Enforces one explicit research question carried by hypotheses, numbers that agree everywhere they appear, causal language that does not inflate between the results and the abstract, and hyperlinked author-year citations reconciled with the reference list. Use this skill when someone asks for a whole paper to be written or restructured, says the manuscript does not hang together or reads like several papers, is turning a thesis chapter into an article, is assembling a draft from sections written months apart or by different coauthors, asks what order to write a paper in, or says the paper is nearly done and needs pulling together.
---

# Full Manuscript Build

Papers written one section at a time drift, and the drift is invisible from inside any single section. The introduction promises an answer to a question the conclusion does not answer. The abstract quotes a coefficient that changed two revisions ago when the clustering level was corrected. Table 4 is referenced nowhere in the text. A hypothesis stated on page six is never adjudicated. The results section says "is associated with" and the abstract says "raises". Each section is individually defensible and the manuscript is still rejected, because the referee reads it as one object and nobody on the author side ever did.

The cost is specific. A desk rejection on coherence teaches the author nothing, because the editor's letter says the paper is not a good fit rather than that the argument does not close. A rejection after review costs four to eight months of queue time and arrives with two reports that each fix a different section, which produces a revision that makes the drift worse. And the deepest cost is that the author cannot see it: after six months inside a manuscript, everyone reads what they meant rather than what is on the page.

Two standards run through every step here, and most of the checks exist to test them. First, the paper has one explicit research question, written as a sentence, and two to four hypotheses that carry the story from the first page to the last. A manuscript that describes a dataset, reports means and correlations, and never states a question or a model does not meet the standard, and no amount of section-level polish will make it meet it. Second, every in-text citation is the hyperlinked author-year form, Author (Year) with the DOI behind the link, semicolon-separated when grouped, and every one appears in the reference list.

## When to use this, and when not to

Use it when the analysis is finished and a full draft has to exist: a first manuscript, a thesis chapter being converted into an article, a draft assembled from pieces written months apart, a paper that four people have edited and that now reads like four papers, or a resubmission whose revision touches more than two sections.

Use it especially when someone says the paper is nearly done. That sentence almost always means the sections exist and the seams have never been inspected, which is precisely the condition this skill is for.

Do not use it to write a single section. Each section has its own skill and each is deeper than anything this file can be: `introduction-writer`, `data-section-writer`, `econometric-model-writer`, `results-writing`, `discussion-and-conclusion`, `abstract-and-title`, `references-and-bibliography`, plus the exhibit skills `descriptive-statistics-tables`, `academic-tables-booktabs` and `academic-figures-monochrome`.

Do not use it to choose the venue, which is `journal-targeting` and which must be settled before the budget can be set. Do not use it to design the study or fix an identification problem, which are `research-design` and `identification-defense`; a build cannot repair a design, and attempting it produces a well-written paper that gets rejected on method. Do not use it as the pre-submission review, which is `peer-review-simulator` and which runs after this. Do not use it for a revise-and-resubmit response letter, which is `response-to-reviewers`, although a heavy revision usually calls this skill afterwards to rebuild the seams the revision broke.

Do not start a build while the estimates are still moving. A manuscript written against provisional results is written twice, and the second write is done under deadline.

## What you need before starting

**The target journal, or the thesis regulations.** It sets the word limit, the section conventions, whether discussion and results are merged, the reference style, how much theory is expected, and whether a roadmap paragraph is normal. Missing: run `journal-targeting` first. If a decision genuinely cannot be made now, pick the most likely target, write to it, and record in the build log that the budget is provisional. Writing to no journal produces a manuscript that fits none of them and has to be cut by a fifth at submission, which always comes out of the results.

**The claim sentence.** One sentence saying what this paper establishes that was not established before. Everything drafted afterwards either supports that sentence or is cut. Missing: try to write it, and if it cannot be written in one sentence without a semicolon, stop and go back to `research-design`. This is not a formality; a build that starts without it produces a manuscript whose introduction is rewritten four times.

**The research question and the hypotheses.** The question as a sentence with population, variation and outcome. Two to four falsifiable hypotheses, each mapped to the exhibit that tests it. Missing: reconstruct them from the analysis with the author, in writing, before drafting. If the honest answer is that the paper has no question and no model, say so plainly and stop: the fix is `research-question-ideation` and then `research-design`, not prose.

**The finished estimation output and the exhibit set.** Final tables and figures, or at minimum the headline exhibits in final form. Missing: build the exhibits first, which is step one of the method anyway. Prose written before exhibits exist is rewritten when they change, and it always changes.

**The verified reference set with DOIs.** Every source checked against a live record under the `literature-verification` standard, with the identifier stored even where the style does not print it. Missing: verify as you cite, never in a cleanup pass. Where no lookup is available at all, write visible placeholders and list the unsourced claims; do not emit formatted citations.

**The word or page limit, and the current length of what exists.** Missing: take the journal's stated limit from three recent articles rather than the guidelines, since the guidelines are often stale, and count what exists before allocating.

**What the coauthors and the supervisor have already settled.** Which framing is agreed, which result is contested, which sentence somebody insisted on. Missing: ask before drafting. Rewriting a paragraph a coauthor is attached to, without knowing they are attached to it, costs more time in argument than the paragraph is worth.

**The deadline and what happens if it passes.** Missing: assume the next realistic submission window and say you have assumed it. The build order below is designed so that a truncated build still produces a coherent paper, but only if the truncation point is known in advance.

## The method

1. **Fix the target, the claim sentence and the budget, in writing, before a word of prose.** Ten minutes, recorded at the top of the build log. The budget is a share of the journal's limit, allocated by section, using the table below. Everything after this step is written against these three fixed points, and any change to them is a decision that gets logged rather than a drift that gets absorbed.

2. **Build the exhibits first.** The tables and figures that carry the finding are the paper's spine. Every exhibit must map to a hypothesis or to an identification assumption; exhibits that map to neither are cut now, which is easy, rather than after prose has been written around them, which is not. Use `descriptive-statistics-tables` for the sample table and balance, `academic-tables-booktabs` for regression output, `academic-figures-monochrome` for figures, which are monochrome first with series separated by marker, dash pattern and texture rather than colour, and the legend outside the plot area. Number them in the order the paper will use them, and freeze the numbering.

3. **Write the data section**, using `data-section-writer`. It goes early because sample construction determines what can be claimed, and because the counts it produces are the counts every later section must match. The sample construction chain and its final N are settled here and nowhere else.

4. **Write the empirical strategy**, using `econometric-model-writer`, with the identification argument and its named threats. Where a threat needs a full defence with placebo tests and bounding, `identification-defense` goes deeper than this section should.

5. **Write the results against the exhibits**, using `results-writing`, organised by hypothesis rather than by table. Every number in the prose is read off an exhibit, never remembered. This is the section that must never be squeezed at the end for space, which is why it holds the largest share of the budget.

6. **Write the discussion and conclusion immediately after the results**, using `discussion-and-conclusion`, while the argument is still live in the author's head. Leaving a gap of days here is the single most reliable way to produce a discussion that restates the results table rather than interpreting it. The hypotheses are adjudicated here, including the ones that failed.

7. **Write the theoretical framework and the literature**, using `theoretical-framework-review` for the framework and `literature-verification` for the evidence base. Doing this now rather than at the start means it is written once, against the contribution that actually emerged, rather than twice.

8. **Write the introduction second to last**, using `introduction-writer`. It is a promise about a paper that now exists, and its five moves can be checked against real sections rather than intentions. The numbers in it are copied from the results, not recalled.

9. **Write the abstract and title last**, using `abstract-and-title`, from the finished results. Anything else produces an abstract describing the paper the author meant to write.

10. **Finish the references**, using `references-and-bibliography`: style resolved, text and list reconciled in both directions, every entry verified, every in-text citation in the hyperlinked author-year form with the DOI behind it.

11. **Run every cross-section check below, and fix rather than note.** A list of noted problems handed to an author under deadline is a list of problems that ships. The check pass is not finished until each line either passes or has a logged decision.

12. **Read the assembled manuscript once, straight through, without editing.** Mark only three things: where you lose the thread, where you have to look something up that should have been in front of you, and where you stop believing the argument. Those three marks are worth more than another line-editing pass. Then hand it to `peer-review-simulator` before anyone else sees it.

Where a step's section already exists in acceptable form, do not rewrite it; check it against the brief, fix what fails, and spend the time on the sections that need it. The order matters most when writing from scratch and matters less when repairing, but the check pass at step 11 is mandatory either way.

## The word budget

Allocate before drafting, as a share of the journal's limit. A workable default for an empirical article in economics or the social sciences, with the shares adjusted after reading three recent articles in the actual target:

| Section | Share of limit | What overrun usually means |
| --- | --- | --- |
| Abstract | 3 percent | The finding is not settled, so the abstract is describing intentions |
| Introduction | 15 percent | The contribution is unclear and is being argued at length instead of stated |
| Framework and literature | 15 percent | The review is organised paper by paper rather than by finding |
| Data | 15 percent | Cleaning detail that belongs in an appendix or the replication package |
| Empirical strategy | 15 percent | The identification argument is being defended before it has been stated |
| Results | 25 percent | Rarely overruns; if it is under budget, robustness or heterogeneity is missing |
| Discussion and conclusion | 12 percent | Speculation beyond the estimand, or implications the design cannot support |

Two rules make the budget bite. First, when a section runs over, it is cut in that section rather than paid for out of the results, which is what happens by default and is the reason so many manuscripts have a thin results section behind a long introduction. Second, an introduction at double budget is a diagnostic finding, not a length problem: it means the claim sentence is not settled, and the fix is upstream.

Thesis chapters carry roughly the same proportions with a longer framework and a longer data section, and they add the chapter-linking paragraphs that `discussion-and-conclusion` covers.

## The cross-section checks

This is the part only a whole-manuscript pass can do. Run all of them, in this order, and fix what fails.

| # | Check | How to run it in two minutes | What failure looks like |
| --- | --- | --- | --- |
| 1 | One question | Copy the question sentence out of the abstract, the introduction, the hypotheses block and the conclusion, and put the four side by side | Four sentences that are compatible in spirit and differ in population, outcome or period |
| 2 | Hypotheses carry the story | List every hypothesis stated anywhere, then find where each is tested and where its outcome is reported | A hypothesis stated in the framework and never mentioned again, or a result that answers no stated hypothesis |
| 3 | One claim, one strength | Compare the contribution paragraph with the conclusion's contribution sentences | The conclusion claims more than the introduction promised, or a third contribution that appeared from nowhere |
| 4 | Numbers agree | Take every number in the abstract, introduction, results prose and conclusion, and trace each to a table cell | Same coefficient at two roundings, or a figure that changed when the sample was corrected |
| 5 | Causal language is level | Read only the verbs attached to the main finding, in all four places | Results say associated with, abstract says raises. Abstracts inflate silently and referees read them first |
| 6 | Every exhibit works | For each exhibit: is it referenced, does the text need it, is it readable without the text | A table nobody cites, a figure whose message is in the caption only |
| 7 | Sample sizes agree | Compare N in the data section, the exhibit notes and the results prose | The construction chain ends at one N and Table 3 reports another with no explanation |
| 8 | The literature is used | Find the second appearance of every work cited in the framework | Works cited once in the introduction and never again, which is decoration |
| 9 | Citations are complete and linked | Extract every in-text citation and reconcile against the list in both directions; check that each is the hyperlinked author-year form and each link resolves | Cited but not listed, listed but not cited, a link pointing at the wrong record, a group joined with commas instead of semicolons |
| 10 | Notation and terms | Search for each key term and each symbol at first use | Two names for one object, a symbol defined twice with different meanings |
| 11 | Limitations match the threats | Compare the limitations paragraph with the threats named in the strategy section | The convenient limitations are listed and the identification threat the referee will raise first is absent |
| 12 | Budget respected | Word count by section against the allocation | The results section at 15 percent because the introduction took its space |

Check 4 catches an error in most drafts, including careful ones. Check 5 catches the failure that costs the most, because a referee who sees an inflated abstract reads the whole paper as an overclaim.

## Worked example

**Situation.** Dr. Helena Vasques, two years into a postdoctoral position, had a thesis chapter on a municipal childcare fee cap and maternal employment that she needed to turn into an article. The target journal had an 8,000-word limit excluding tables and references. The chapter was 14,300 words, had eleven exhibits, and had been written over eighteen months in three separate bursts. Two coauthors were on the paper. The submission window she wanted was five weeks away.

**Task.** One manuscript inside the limit, coherent enough to survive a referee reading it in one sitting, with the identification argument intact and the results section not squeezed.

**Action.** The build log was opened with the three fixed points: target journal, claim sentence ("municipal fee caps raised maternal employment by about two percentage points, concentrated among mothers with children under three, and the effect operates through formal childcare take-up rather than through informal care substitution"), and the budget from the table above.

The exhibits went first. Of the eleven, four mapped to no hypothesis and no assumption. Two of those were descriptive figures that had been made early, were attractive, and answered nothing; they went to an appendix and were later dropped entirely. One was a robustness table that duplicated another. The set came down to seven, and the numbering was frozen at that point.

The wrong turn came next and cost four days. Dr. Vasques started with the introduction, because it was the weakest section and felt like the front door, and produced a good one. Then a coauthor corrected the clustering level from municipality-year to municipality, which was right, and the standard errors widened enough that the heterogeneity result for mothers of children aged three to five lost significance. Three numbers in the new introduction were now wrong and the second hypothesis had a different outcome. The introduction was rewritten. After that the build reverted to the order above, and the introduction was written once more, at the end, in ninety minutes, because by then the results were fixed and every number could be copied rather than recalled.

The data section came in at 1,540 words against a budget of 1,200 and was cut in place rather than out of the results: the harmonisation detail for a variable whose definition changed in 2016 went to an appendix, and the sample construction chain stayed. The results section was written against the seven exhibits and organised by hypothesis, which made it obvious that hypothesis three had never been tested by any exhibit. It was tested, with an existing specification, and reported as a null.

The check pass took an afternoon and found six problems. The abstract carried an effect of 2.4 percentage points where the final table said 2.1. The conclusion used "caused" twice where the results section used "raised" and the strategy section conceded a threat that made "caused" unsupportable. Table 5 was referenced nowhere. Two works cited in the framework never returned. Three in-text citations were plain text rather than linked, and one link resolved to a different paper by the same first author in the same year, which is the classic near-miss. And N appeared as 41,208 in the data section and 41,180 in two exhibit notes, which turned out to be a real discrepancy: a restriction applied in the do-file had not been documented in the chain.

**Result.** The manuscript went out at 7,860 words with seven exhibits, three days before the window closed. The N discrepancy was the finding that mattered most, because it was a real documentation gap that a replicator would have hit, and it was found by a two-minute check rather than by a referee. The paper received a revise-and-resubmit with two reports, neither of which raised a coherence issue; both were about the identification, which is the argument the authors wanted to be having.

Total build time was about eleven working days, of which the four lost to writing the introduction first were the avoidable part.

### A second scenario, where it goes differently

The same method applied to a management journal article changes at two points. That journal expects formally numbered hypotheses derived from theory before the method appears, and it expects the theoretical contribution stated first in the discussion. So the framework moves from step 7 to step 3, before the data section, because the hypotheses have to be developed from theory rather than reconstructed afterwards, and because a reviewer in that field reads the hypothesis development as the paper's core contribution. The budget shifts too: framework rises to 22 percent, empirical strategy falls to 10 percent, and the discussion rises to 18 percent because managerial implications carry weight there.

Everything else holds. Exhibits still come first, results are still written against them, the introduction is still second to last, and all twelve checks still run. What changed is where the theory sits in the order and how much room it gets, and both changes came from reading three recent articles in the target rather than from a general rule about the field.

A third variation worth naming: for a thesis chapter rather than an article, the introduction is written second to last as usual, but the chapter also needs its link paragraphs, and the checks gain one line. The question in this chapter must be a sub-question of the thesis question, and the chapter's contribution must not duplicate the neighbouring chapters' contributions. `thesis-chapter-review` reads it the way an examiner will.

## Output

Two artefacts: the manuscript itself, and a one-page build log that travels with it.

```
BUILD LOG
Target:          [journal or thesis regulation] / limit [n words] / style [name]
Claim sentence:  [one sentence, what this establishes that was not established before]
Question:        [one sentence: population, variation, outcome]
Hypotheses:      H1 [...] H2 [...] H3 [...]
Deadline:        [date] / if missed: [what happens]

EXHIBITS (frozen numbering)
| # | Exhibit | Type | Tests which hypothesis or assumption | Status |

BUDGET AND ACTUAL
| Section | Budget (words) | Actual | Skill used | Status |

CROSS-SECTION CHECKS
| # | Check | Pass / fail | What was fixed | Where |

OPEN DECISIONS
[Anything changed from the three fixed points, with the date and who agreed it.]

FINAL READ
Lost the thread at:      [locations]
Had to look up:          [what]
Stopped believing at:    [where, and why]
```

The build log is not bureaucracy. It is what lets a coauthor see what changed, what lets the author reconstruct a decision six weeks later when a referee asks about it, and what makes the second paper in the same project take half the time.

## Failure modes

**Writing the introduction first.** Recognise it because the author describes the introduction as the hardest part and starts there to get it over with. The introduction is a promise about a paper that does not exist yet, so it gets written against intentions and rewritten every time a result moves. Write it second to last.

**Polishing prose while exhibits are provisional.** Recognise it when someone is editing sentences about a coefficient that is still being re-estimated. Stop and finish the exhibits. Sentence-level work on unstable numbers is the most expensive kind of wasted effort in manuscript preparation, because it feels productive.

**Running the checks and noting the failures.** A list of noted problems handed over at the deadline ships as a list of noted problems. Fix each one when found, or log an explicit decision not to.

**Cutting the results to make the length.** Recognise it when the last edit before submission removes robustness or heterogeneity discussion. The introduction is nearly always the section with slack, and the budget exists to make that visible before the deadline rather than during it.

**Treating the section skills as optional.** Recognise it when a section was improvised because it seemed quicker. Each section skill carries decision rules this file does not repeat, and the improvised version reliably misses the same two or three of them.

**Letting the abstract inflate.** Recognise it by reading only the verbs. It happens because the abstract is written last, in a hurry, by someone who wants the paper to sound important. Check 5 exists for this and should be run twice, once at assembly and once immediately before submission.

**Building on a design that does not hold.** Recognise it when the strategy section is being rewritten repeatedly to sound more convincing while the specification is unchanged. Prose cannot repair identification. Stop and use `identification-defense`, or accept a weaker claim and rewrite the claim sentence to match.

**Assembling a manuscript from coauthors' sections without a shared brief.** Recognise it by three different terms for the same variable. Send every coauthor the same claim sentence, question and hypothesis list before they write, and reconcile terminology at check 10.

## Edge cases

**A paper with no research question and no model.** A dataset described, means reported, a few correlations, and nothing at stake. This does not meet the standard and building it will not fix it. Say so directly, and go back to `research-question-ideation` and `research-design`. There is one legitimate variant: a paper whose contribution genuinely is a measurement, a new dataset or a descriptive pattern nobody has documented. That paper still needs an explicit question, a stated framework for why the pattern matters and what would explain it, and a claim about what changes now that the pattern is known. Presented that way it can be excellent. Presented as "we describe X" it will not survive review.

**Results that are still moving.** Do not build. Write the data and strategy sections, which depend on the sample and the design rather than the estimates, and stop there until the numbers are fixed.

**A hard deadline that does not allow the full sequence.** Truncate deliberately, in this order of sacrifice: the framework section gets shorter first, then the robustness prose, then heterogeneity. Never truncate the check pass; it is four hours and it catches the errors that cost most.

**A revise-and-resubmit that changed three sections.** Run `response-to-reviewers` for the letter, then run checks 1 to 5 and 9 on the revised manuscript. Revisions break seams that were sound, particularly numbers and causal language, because new results get inserted into old prose.

**Two coauthors who disagree about the claim.** Do not build around a compromise sentence that neither believes; it produces a paper that argues for nothing. Surface the disagreement, write both claim sentences, and get a decision before drafting. Where the disagreement is about strength rather than substance, write the weaker one; it is the one that survives review.

**A journal with an unusual structure**, such as a strict IMRaD template, a merged results and discussion, or a required structured abstract. Take the structure from three recent articles in that journal, remap the budget, and keep the writing order unchanged. The order is about dependency between sections, not about how the paper is laid out.

**Second-language manuscripts.** Build in the language of submission. Translating a finished manuscript reliably breaks check 5, because causal verbs do not map one to one across languages, and it breaks check 10 for technical terms.

## Quality bar

- The target, the claim sentence, the research question and the word budget are fixed in writing before any prose is drafted.
- Every exhibit maps to a hypothesis or an identification assumption, and the exhibits existed before the prose that describes them.
- All twelve cross-section checks were run and every failure was fixed or carries a logged decision.
- Every number in the abstract, introduction and conclusion traces to a specific table cell at the same rounding.
- The verbs attached to the main finding are the same strength in the results, the discussion and the abstract.
- Every hypothesis stated anywhere is tested somewhere and its outcome reported, including the nulls.
- Every in-text citation is the hyperlinked author-year form with a resolving DOI, and text and list reconcile in both directions.
- The manuscript sits inside the journal's limit without the results section having been cut to get there.

## Adapting this to your context

The eleven-step order and the section budget come from empirical social science papers of 8,000 to 12,000 words with a separate empirical strategy section. The order encodes dependency between sections and survives any layout; the budget does not.

- **The section budget.** Fifteen percent to empirical strategy and twenty-five to results is an economics allocation. An IMRaD paper in psychology or health gives Methods more and runs a shorter introduction; a qualitative paper puts a third of its length into findings because the extracts sit there. Reallocate from three recent articles in the target, keeping results the largest block.
- **Exhibits first.** Right when tables and figures carry the finding. For qualitative work the spine is the theme table and the extract register, built first for the same reason.
- **The writing order.** Results fifth, discussion sixth, introduction eighth. That holds wherever the introduction promises a paper that already exists. In a registered report the introduction and methods were accepted before any data, so only results and discussion are in play.
- **Reporting standards.** Absent from the checks. Add the one your field requires as a check 13: CONSORT, PRISMA, STROBE, JARS or COREQ, each with a checklist journals increasingly demand at submission.
- **What not to change.** One claim sentence fixed before any prose, and every cross-section check fixed rather than noted.

## Related skills

`research-design` supplies the question, the hypotheses and the exhibit plan this build assembles, and is where to go back to when the claim sentence cannot be written. `journal-targeting` fixes the target that sets the budget. The section skills do the actual writing and are called in this order: `data-section-writer`, `econometric-model-writer`, `results-writing`, `discussion-and-conclusion`, `theoretical-framework-review`, `introduction-writer`, `abstract-and-title`, `references-and-bibliography`. The exhibits come from `descriptive-statistics-tables`, `academic-tables-booktabs` and `academic-figures-monochrome`. `literature-verification` supplies the verified reference set and runs as one of the checks. `identification-defense` handles a threat too heavy for the strategy section. `peer-review-simulator` reads the assembled manuscript adversarially before submission, and `thesis-chapter-review` does the same for a chapter. `response-to-reviewers` handles the revision, and hands the revised manuscript back here for the seam checks.
