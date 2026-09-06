---
name: full-manuscript-build
description: Runs a complete journal article end to end rather than one section at a time: sets the word budget per section from the target journal, writes in the order that keeps the argument consistent, calls each section skill in turn, and then runs the cross-section checks that catch the drift a section-by-section process always produces. Use this skill whenever the user wants a whole paper drafted or restructured, says the paper needs to be written rather than a particular section, is turning a thesis chapter into an article, or asks why the paper does not hang together.
---

# Full Manuscript Build

Papers written section by section drift. The introduction promises something the results do not deliver, the abstract quotes a coefficient that changed three revisions ago, the conclusion answers a question the introduction did not ask. Each section can be individually good and the paper still fail, because nobody read it as one object. This skill runs the sequence and then checks the seams.

It orchestrates the section skills rather than replacing them: `research-design`, `literature-verification`, `data-section-writer`, `econometric-model-writer`, `results-writing`, `discussion-and-conclusion`, `introduction-writer`, `abstract-and-title`, `references-and-bibliography`, and the exhibit skills.

## Settle three things first

**The target**, because it sets the word budget, the section conventions, the reference style, and how much theory is expected. Use `journal-targeting` if it is not decided. Writing to no journal produces a manuscript that fits none.

**The claim**, in one sentence: what this paper establishes that was not established before. Everything written afterwards either supports that sentence or is cut. If it cannot be written, stop and go back to `research-design`.

**The budget**, allocated before drafting, as a share of the journal's limit. A workable default for an empirical economics or social science article: abstract 3 percent, introduction 15, literature and framework 15, data 15, empirical strategy 15, results 25, discussion and conclusion 12. Adjust for the journal's own habits by looking at three recent articles in it, not at the guidelines.

## The order

Not the order the paper is read in.

1. **Exhibits.** The tables and figures that carry the finding, built first. They are the paper's spine, and writing before they exist produces prose that has to be rewritten when they change.
2. **Data**, because sample construction determines what can be claimed.
3. **Empirical strategy**, including the identification argument and its threats.
4. **Results**, written directly against the exhibits.
5. **Discussion and conclusion**, immediately after results, while the argument is live.
6. **Theoretical framework and literature**, once the contribution is settled, so it is written once rather than twice.
7. **Introduction**, second to last. It is a promise about a paper that now exists.
8. **Abstract and title**, last, from the finished results.
9. **References**, verified.

Where a section skill exists, use it rather than improvising, and hand it the target journal and the claim sentence so it writes to the same brief.

## The cross-section checks

This is the part that only a whole-manuscript pass can do. Run every one, and fix rather than note.

- **One question.** The question in the abstract, the introduction, the hypotheses, and the conclusion is the same question, in compatible words.
- **One claim.** The contribution promised in the introduction is the contribution the conclusion delivers, at the same strength.
- **Numbers agree.** Every figure quoted in the abstract, introduction, results, and conclusion matches the table it comes from, to the same rounding. This check catches an error in most drafts.
- **Causal language is level.** The verbs in the abstract are not stronger than the verbs in the results. Abstracts inflate silently, and referees read the abstract first.
- **Every exhibit works.** Each is referenced in the text, does something the text needs, and is readable without the text. Anything failing this is cut or moved to an appendix.
- **Every hypothesis lands.** Each one stated is tested, and its outcome is reported, including when it is null.
- **The literature is used.** Every work in the framework returns somewhere, in the results or the discussion. Citations that appear once and never recur are decoration.
- **Notation and terms.** Defined at first use, used consistently, never two names for one object.
- **Limitations match.** The limitations acknowledged include the ones a referee would raise first, not only the convenient ones.
- **Budget respected.** Section lengths near their allocation. An introduction at double budget usually means the contribution is unclear and is being argued at length instead of stated.

## The final read

Read the assembled manuscript once, straight through, without editing. Note only where you lose the thread, where you have to look something up that should have been in front of you, and where you stop believing the argument. Those three notes are worth more than another pass of line edits.

Then run `peer-review-simulator` before anyone else sees it.

## Quality bar

- The target journal, the claim sentence, and the word budget are fixed before any drafting.
- Sections are written in the order above, not the order they are read.
- All ten cross-section checks are run and the failures fixed, not listed.
- Every number in the abstract and the introduction traces to a table.
- The finished manuscript sits inside the journal's limit without last-minute cutting of the results.
