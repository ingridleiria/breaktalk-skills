---
name: literature-verification
description: A zero-fabrication citation and literature workflow for academic writing. Verifies every reference against a live bibliographic record before it enters a draft, checks that the paper actually supports the claim attached to it, builds reviews from an evidence matrix rather than paper by paper, and records screening counts so coverage can be judged. Use this skill whenever someone asks to find papers, build a literature review or related work section, add citations to a draft, check whether references are real, produce a bibliography or BibTeX file, or asks what the literature says about something. Trigger on any academic writing task that will contain citations, even when verification is not mentioned, because unverified generated citations are the failure this exists to prevent.
---

# Literature Verification

Language models produce citations that look right and do not exist. The author names are plausible for the field, the year is plausible for the method, the journal is plausible for the topic, and the paper was never written. They also produce a subtler and more common failure: a real paper cited for a claim it does not make, which is harder to catch because the reference resolves.

In academic work neither is a small error. A fabricated reference found by a referee ends that submission and follows the author into the next one. Found by an examiner in a viva, it changes the conversation from the research to the researcher's reliability. Found after publication, it is a correction at best.

The rule here is absolute and it is the whole skill: no citation enters a draft until it has been checked against a real record, in this session, by someone who looked.

## When to use this, and when not to

Use it for anything that will carry citations: a literature review, a related work section, a draft being revised, a grant proposal, a reference list inherited from a coauthor, a thesis chapter, a referee report that cites work back at an author.

Use it especially when the citations came from an assistant, from a coauthor's old draft, or from your own notes written more than a few months ago. Notes decay in a specific way: the finding is remembered correctly and attached to the wrong paper.

Do not use it for a formal systematic review, which needs a registered protocol, reproducible search strings, and two screeners; that is `systematic-review-protocol`. Do not use it as a substitute for reading the papers that carry your argument. Verification confirms a record exists and supports a claim; it does not make you familiar with a literature.

## What you need before starting

**The claim each citation is attached to.** Verification is against a claim, not against a name. Missing: extract the claims from the draft first, one line each, and verify against those.

**Access to at least one live lookup.** A DOI resolver, a bibliographic database, a publisher page, a search tool, or the paper itself. Missing: do not produce formatted citations at all. Write visible placeholders and say which claims are unsourced.

**The target's citation style.** Missing: use author-year and say you have assumed it.

**The scope, for a search rather than a check.** The question, the period, the fields, and whether working papers and preprints count. Missing: propose a scope in one line and ask for a yes.

## The verification standard

A citation is verified when all four of these hold, each confirmed against a live source:

1. **The record exists.** Authors, year, and exact title match a real published or archived record. Not a similar title, the title.
2. **The venue matches.** Journal, volume, issue, pages, or the conference and year. A real paper attributed to the wrong journal is a real error and referees who know the field notice.
3. **The identifier resolves.** The DOI resolves to that paper. For a working paper, the repository link resolves. A DOI that resolves to something else is the single strongest signal that a citation was generated rather than found.
4. **The paper supports the claim.** Read at least the abstract, and the relevant section when the claim is specific. A real paper cited for something it does not say is as wrong as a fake one and is far more common.

Anything failing any check is repaired against the real record or removed. There is no third option and there is no "probably real".

Where a specific number is attributed to a paper, that number must have been seen in the paper. "Roughly a twenty percent effect" recalled from memory is how a misquotation enters a literature and then propagates, because the next author cites you rather than the source.

## The method, for a search

1. **Decompose the question** into two to four themes. Typically the outcome literature, the method literature, and the setting or country literature. Write them down; a search with no stated themes wanders.

2. **Search each theme** with the tools available. Use scholarly databases and connectors where they exist, and general search where they do not. Vary the vocabulary deliberately, because fields name the same construct differently and a single phrasing finds a single community. Search the references of the two or three papers that are clearly central, and the papers that cite them, which finds work that keyword search misses.

3. **Screen on abstracts** and record counts: found, screened, relevant, kept, and the reasons for the main exclusions. These counts are what make a claim about coverage honest, and they take two minutes to keep and cannot be reconstructed later.

4. **Build the evidence matrix before writing anything.** One row per paper: authors and year, setting and period, data, method and identification, sample size, the main finding with direction and magnitude, and the relationship to your question, which is supports, contradicts, extends, or provides the method. The matrix is the actual deliverable. Writing from it is fast and accurate; writing without it produces an annotated list.

5. **Write from the matrix, organised by finding or by theme**, never paper by paper. Where the literature disagrees, name who disagrees and cite both sides. "Findings are mixed" is what an author writes when they have not looked at why.

6. **State the gap in one sentence** that follows from the matrix rather than being asserted before it.

## The method, while drafting

Verify at the moment of citing, never in a cleanup pass. Cleanup passes get skipped under deadline, which is exactly when the risk is highest.

Every empirical or theoretical claim carries its citation in the sentence that makes the claim, not at the end of the paragraph where it becomes ambiguous which sentence it supports.

Maintain the reference list in the same session, appending each verified entry as it is used, so the text and the bibliography cannot diverge. Keep the DOI in the entry even when the style does not print it, because the next person to check will need it.

## Worked example

**Situation.** A doctoral student had a thirty-one page draft chapter with sixty-four citations, due to a supervisor in four days. The chapter had been written over five months, partly with an assistant, and about a third of the references came from an earlier reading list whose provenance was no longer clear. The student's actual question was whether it was ready to send.

**Task.** Verify all sixty-four before it left the building, and repair or remove whatever failed, without rewriting the argument.

**Action.** The claims were extracted first, one line per citation, which took ninety minutes and turned out to be the most useful step. Twelve citations were attached to no identifiable claim; they were decoration in the second paragraph of the introduction and were cut immediately, which reduced the work by a fifth before any checking started.

Of the remaining fifty-two, forty-one verified cleanly on the first pass. Eleven failed, in four distinct ways:

Three did not exist. All three had plausible author combinations from the field and years consistent with the method they were cited for. Two were cited for the same claim, which was the signal that prompted a closer look: a claim supported by two references nobody could locate.

Four existed but were attributed to the wrong venue, all four to a more prestigious journal than the real one. Repaired in minutes once the real record was found.

Three existed, resolved correctly, and did not support the claim. One was the worst case in the set: a paper cited for a specific elasticity, where the paper reported a different quantity entirely and the number in the draft appeared nowhere in it. That number had been in the student's notes for over a year and had already been quoted in a conference presentation.

One was a working paper that had since been published with a different title, a changed sample, and a materially smaller headline effect. The draft's sentence was true of the working paper and false of the published version.

The wrong turn: the first attempt tried to verify by searching for the title as written. For the fabricated ones this returns near-matches, and near-matches are exactly what makes a person conclude the citation is fine and move on. Switching to author-plus-year plus a distinctive phrase from the claim found the real papers where they existed and returned nothing where they did not, which is a much clearer signal.

**Result.** Sixty-four citations became forty-nine, all verified, with two claims rewritten because the supporting evidence turned out to be weaker than the sentence claimed. The chapter went to the supervisor a day late. The elasticity was corrected in the conference slides before the next presentation.

The verification took eleven hours across two days. The student's estimate beforehand had been two hours, which is the usual estimate and is wrong by roughly the factor seen here.

### A second scenario, where it goes differently

Verifying a coauthor's contribution to a joint paper is the same method with a different social problem. The finding that three of their references do not support their claims has to be raised, and raising it badly damages the collaboration.

What works: verify everything including your own, present the list without attribution to who wrote what, and treat it as a joint cleanup. What does not work: sending a list of their errors. The technical task is identical; the framing determines whether it gets done.

## Output

**For a search**, the evidence matrix:

| Authors (year) | Setting and period | Data | Method | N | Finding, with direction and size | Relation to our question | DOI |

Followed by the screening counts, the written review organised by finding, and the gap statement.

**For a check on an existing draft**, the verification table:

| # | Citation as written | Claim it supports | Status | Action |

Status is verified, wrong venue, wrong claim, superseded, or not found. Action is kept, repaired, claim rewritten, or removed. End with the counts and, separately, the list of claims now carrying no source, since those need either a new source or a softened sentence.

## Failure modes

**Verifying the title as written.** Returns near-matches for fabricated citations and reads as confirmation. Search author, year, and a distinctive phrase from the claim instead.

**Verifying the reference and not the claim.** The most common surviving error, because the DOI resolves and everyone stops there.

**The cleanup pass.** Deferred verification is skipped verification. Verify at the moment of citing.

**Trusting your own old notes.** Notes preserve the finding and lose the attribution. Treat a reference from your own notes exactly as you would treat one from an assistant.

**Working papers that moved.** A preprint cited three years ago may now be published with a different sample and a different number. Recheck every working paper citation before submission.

**Padding with famous tangential work.** Recognisable because the paper is cited once, in the introduction, and never returns. Cut it.

**Silently dropping the paper that contradicts you.** If the literature cuts against the hypothesis, the review says so. That is what the review is for, and a referee who knows the field will know what is missing.

## Edge cases

**No lookup tools available.** Do not emit formatted citations. Write `[citation needed: staggered difference-in-differences estimator, around 2021]` in the text, and list the unsourced claims separately so they are impossible to miss.

**The paper is behind a paywall and only the abstract is visible.** Verify the record fully, and verify the claim only to the extent the abstract supports it. Where the claim depends on a specific number in the body, mark it as unverified rather than assuming.

**Non-English literature.** Verify in the original language and cite it in the original, with a translation of the title where the style requires. Do not cite a translated title as though it were the record.

**A retracted paper.** Check retraction status for anything load-bearing, particularly in fast-moving areas. Where a retracted paper must be discussed, cite it explicitly as retracted.

**Grey literature, government statistics, and institutional reports.** Verify to the publishing institution, the exact document, and its version and date, and archive a copy, since these move and disappear more often than journal articles.

**Citing something you were told about and cannot find.** Do not cite it. Ask the person for the reference.

## Quality bar

- Every citation in the delivered text was checked against a live record in this session.
- Every citation was checked against the claim it supports, not only against its own existence.
- Every number attributed to a paper was seen in that paper.
- Screening counts are recorded for any search.
- The evidence matrix exists before any review prose is written.
- Contradicting work found during the search appears in the review.
- Where verification was impossible, the text carries a visible placeholder and the unsourced claims are listed.
- The reference list was built during drafting and matches the text exactly.

## Related skills

`systematic-review-protocol` is the formal version for a review that must be reproducible. `theoretical-framework-review` builds the framework this evidence supports. `references-and-bibliography` handles style conversion and BibTeX hygiene once the sources are verified. `research-assistant` applies this standard when the work is being done to somebody else's brief. `full-manuscript-build` runs this as one of its cross-section checks before submission.
