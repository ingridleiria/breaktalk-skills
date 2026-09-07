---
name: references-and-bibliography
description: Produces the reference apparatus of a submission: resolves which style applies and says why, reconciles in-text citations against the list in both directions, formats entries in APA 7, Chicago author-date, ABNT, Harvard or a journal house style, converts between styles from structured records rather than by editing strings, keeps a clean BibTeX file, and confirms every entry resolves to a real record before submission. Enforces the hyperlinked author-year in-text form, Author (Year) carrying the DOI, semicolon-separated when grouped, with every citation present in the list and every list entry cited. Use this skill when someone asks to format references, fix the bibliography, convert citations to another style, reconcile the text with the reference list, produce or clean a BibTeX file, check whether citations are real, prepare references for a specific journal or a university thesis template, or says the reference list is a mess.
---

# References and Bibliography

A reference list has two jobs. It lets a reader find every source, and it tells a referee how careful the author is. Both fail on a single bad entry, and the failure is disproportionate: an editor who finds one reference that does not resolve, one citation in the text with no entry in the list, or three entries formatted three different ways, starts reading the rest of the manuscript for errors rather than for argument. That shift in attention costs more than the mistakes themselves.

The specific failures are dull and they are everywhere. A citation added during the final revision that never reached the list. An entry in the list nobody cites, left over from a paragraph that was cut. Two works by the same author in the same year with no a and b suffixes, so the in-text citation is ambiguous. A DOI that resolves to a different paper by the same first author, which is the classic near-miss and the hardest to see. A list converted from one style to another by find-and-replace, leaving forty entries half in each. And, in a thesis assembled from chapters written across three years, three styles coexisting in one document.

This skill formats, reconciles and verifies in one pass, and it runs last in the manuscript order, after `abstract-and-title`, on a reference set that has been built during drafting rather than assembled at the end.

## When to use this, and when not to

Use it to prepare the reference apparatus of a submission, to convert a list between styles, to reconcile a manuscript's citations against its list, to clean a BibTeX file, to prepare a thesis bibliography under university regulations, and to fix a list that has drifted across a long project.

Use it in particular after any revision that added or removed citations, since that is when text and list diverge, and before every submission and resubmission.

Do not use it to find literature or to check that a paper supports the claim attached to it. That is `literature-verification`, which owns the existence and claim-support standard and which runs during drafting rather than at the end. This skill assumes the sources were verified when they were cited and reconfirms that the records resolve; it does not read the papers.

Do not use it to build a systematic review's search or screening record, which is `systematic-review-protocol`. Do not use it to write the framework the citations support, which is `theoretical-framework-review`. Do not use it to assemble the rest of a submission package, such as the cover letter, title page and declarations.

## What you need before starting

**The manuscript in its final form, or as final as it gets.** Reconciliation performed on a draft that will change is performed twice. Missing: reconcile anyway, and repeat the reconciliation immediately before submission; that second pass is short because the first one fixed the structural problems.

**The reference list or the BibTeX file, and knowledge of where it came from.** A manager export, a hand-typed list, or a mix. Missing: extract every in-text citation and rebuild the list from verified records. Rebuilding is faster than repairing a list of unknown provenance, and safer.

**The target style, or the source that determines it.** The journal's author guidelines, the university's thesis regulations, or the field default. Missing: apply the resolution order below, state which rule you used, and say so in the deliverable rather than leaving it implicit.

**A DOI or a stable identifier for every entry.** Missing: look it up. Where an entry genuinely has none, such as an older book, a working paper or a government report, record the stable location and the access date instead, and say which entries fall into that category.

**A live lookup of some kind.** A DOI resolver, a bibliographic database, a publisher page, a library catalogue, a reference manager with lookup, or a search tool. Missing: do not certify entries as verified. Format what exists, mark every unverified entry visibly, and list them separately so the author cannot submit without seeing them. Never require a paid database; a public DOI resolver and a publisher page do this job.

**The submission format.** Word or LaTeX, whether the manuscript is anonymised, whether the journal accepts hyperlinks in the body, and whether the PDF is generated by the author or by the publisher. Missing: ask, because the hyperlink mechanics differ and a link that works in the author's file and not in the produced PDF is a wasted effort.

**Anything the journal does about self-citation and anonymity.** Missing: for double-blind review, check every self-citation and neutralise the phrasing without removing the work.

## The method

1. **Resolve the style, in this order, and record the decision.** The target journal's author guidelines, taken from the journal itself and dated; then the university's thesis regulations; then the field default (APA 7 in education, psychology and much of management; Chicago author-date or a journal house style in economics; ABNT in Brazilian institutions; Harvard variants elsewhere); then the author's stated preference. State which applied and where the rule came from, because a style question that reopens later costs an hour of rework and the note prevents it.

2. **Extract every in-text citation and every list entry into two lists.** Do this mechanically rather than by reading, since the citation the eye skips is exactly the one that is broken. A search for the parenthesis-and-year pattern catches most; narrative citations of the form Author (Year) need a second pass.

3. **Reconcile in both directions and report three sets.** Cited but not listed; listed but not cited; and mismatched between the two on author spelling, year, or the use of et al. Fix all three before formatting anything. Formatting a list that does not match the text is the most common wasted hour in this work.

4. **Confirm every entry resolves, to the standard `literature-verification` sets.** That skill owns the rule that the identifier must resolve to the record cited, and states why it is the check that catches a fabricated or drifted citation; apply its rule here rather than reasoning it out again. What this pass adds is the field-level comparison against the live record: authors, year, exact title, venue, volume, issue and pages. Entries that cannot be resolved are removed and flagged to the author with the claim they supported, so the sentence can be revised or resourced; an unresolvable entry is never left in a submitted list.

5. **Apply the hyperlinked author-year standard to the in-text citations,** as set out in the section below.

6. **Format the list from structured records**, field by field, rather than by editing the strings that exist. Punctuation, capitalisation, italics, author name order, and identifier presentation all follow the resolved style. Sort as the style requires.

7. **Handle the recurring edge cases explicitly** rather than hoping they do not arise: multiple works by the same author in the same year, with the a and b suffixes applied in the text and the list together; institutional and government authors; translated works; datasets and software cited with version and identifier; preprints that have since been published, where the published version is cited and the working paper only where the argument genuinely refers to it; chapters in edited volumes; and legal or policy documents, which ABNT treats specifically.

8. **Rebuild the BibTeX file if the project uses LaTeX,** to the hygiene rules below, and regenerate the list from it rather than maintaining two sources.

9. **Check link integrity.** Every hyperlink in the delivered file resolves, and resolves to the right record. Where the file is Word, the links are real fields rather than blue text, since text that looks like a link and is not is worse than no link.

10. **Produce the deliverables** listed in the output block, including the note on any style rule that was ambiguous and how it was resolved.

11. **Repeat the reconciliation immediately before submission,** after the last edit. Every revision adds citations, and the last one always adds at least one.

## The hyperlinked author-year standard

This is the house form and it applies to every section of the manuscript.

**The form.** The citation reads as author and year in the sentence, and the author-year text carries the link, whose target is the DOI in resolver form. A narrative citation reads Vasquez and Lund (2019) with the link on the name and year. A parenthetical citation reads (Vasquez and Lund, 2019) with the link inside the parentheses.

**Grouping.** Multiple works in one parenthesis are separated by semicolons, never commas: (Vasquez and Lund, 2019; Nakamura, 2021; Oduya et al., 2023). The reason is mechanical rather than aesthetic. Author and year are already separated by a comma in most styles, so a comma between works makes a group of three ambiguous on first reading. Order within the group follows the style's rule, usually chronological or alphabetical; pick one and hold it throughout.

**Coverage.** Every in-text citation appears in the reference list, and the list contains nothing the text does not cite. This is checked mechanically in step 3, not by reading.

**Placement.** The citation sits in the sentence making the claim, not at the end of the paragraph, so it is unambiguous which claim it supports.

**Where the DOI does not exist.** Working papers link to the repository record, books to the publisher or a catalogue entry, datasets to their landing page or their own DOI, government documents to the stable official location with an access date. The principle is that the link resolves to the authoritative record, not to a copy somebody uploaded.

**Where hyperlinks are not permitted.** Some journals require plain text in the body, and some production systems strip author-supplied links. The in-text form is unchanged; the DOI travels in the reference list and is printed there according to the style. Check the target's practice in a recent published article rather than the guidelines, since production and guidelines often disagree.

**What breaks it.** Links applied to the whole parenthesis including surrounding punctuation; links applied to a sentence rather than a citation; links to a publisher search result rather than a record; links to a personal copy on a departmental page; and, most often, a link copied from an earlier draft after the citation next to it was changed. Step 9 exists for the last one.

## BibTeX and reference manager hygiene

One `.bib` file per project, and it is the single source. Keys in a consistent scheme, such as authorYEARkeyword, generated by one rule rather than by whatever the manager produced on the day. Fields complete for the entry type: author, title, journal, year, volume, number, pages and doi for an article, with publisher and edition for a book. No duplicate entries, which accumulate when two coauthors export from different libraries and which produce the same work cited twice under different keys.

Capitalisation protected where it must survive the style's transformation, by bracing the words that need it rather than the whole title, since bracing everything defeats sentence-case styles. No trailing whitespace, no stray braces, no fields the style will not use but that carry stale information such as an abstract field with a different paper's abstract in it, which happens more than one would expect.

For authors working in a reference manager rather than LaTeX, deliver the corrections as a keyed list of entries to fix, by title, with the specific field and the correct value, since that is what can actually be applied in the manager's interface. Do not deliver a corrected list that has to be retyped into the library, because it will not be, and the library will produce the same errors next time.

## Converting between styles

Convert from the structured records, never by editing the existing strings. String editing produces entries that are correct in the places the pattern matched and wrong everywhere else, and the wrong ones are invisible because they look like the style they came from.

The practical route: rebuild each entry as fields, apply the target style's rules to the fields, and regenerate. Convert the in-text citations in the same pass, because the two are coupled: a style that uses et al. from three authors and one that uses it from six will produce different in-text text for the same entry, and converting the list without the text leaves the manuscript internally inconsistent.

Style points that most often need explicit attention when converting: the ampersand versus "and" in APA depending on position; sentence case versus title case for article titles; whether the issue number appears; whether the DOI is printed as a URL or with a prefix; how many authors before et al.; and, for ABNT, surnames in capitals in the list, the specific in-text form depending on whether the citation is narrative or parenthetical, and page numbers required for direct quotations.

## Worked example

**Situation.** Karin Almeida was depositing a doctoral thesis with 214 references, assembled from four chapters written over three years. Chapter one had been formatted in APA 6 from an early manager library, chapters two and three in APA 7, and chapter four in the house style of a journal that had rejected it. The university regulations required ABNT. The deposit deadline was eleven days away.

**Task.** One reference list in ABNT, every in-text citation matching it, every entry resolving, and a BibTeX file that would still be usable when the chapters were submitted as articles.

**Action.** The extraction ran first and produced the reconciliation, which was worse than expected. Of 214 list entries, 189 were cited somewhere in the text. Of the 25 uncited, 19 came from a literature section cut from chapter two and were removed. Six turned out to be cited in the text under a different spelling of the author's name, which is the mismatch case rather than the uncited case. In the other direction, 11 in-text citations had no list entry, all of them added during the final year of writing, which is the pattern: the entries added last are the ones that never reach the list.

The wrong turn cost two days. The first approach was to convert the existing entries to ABNT with a series of find-and-replace patterns, since the transformations looked regular: surnames to capitals, initials after surnames, the year to a specific position. It worked for the 140 journal articles and failed for everything else. Book chapters, institutional reports, and the eight entries with four or more authors each broke a different pattern, and by the time this became apparent the file contained a mix of converted, half-converted and untouched entries that could no longer be told apart by looking. The file was discarded and the work restarted from the BibTeX records, converting field by field. That is the rule the method now states: convert from structured records, and if the structured records do not exist, build them first.

Verification found four problems worth naming. Two entries did not resolve at all and were traced to a manager import that had merged two records; both were repaired from the publisher pages. One DOI resolved to a different paper by the same first author in the same year, which is the near-miss that reads as correct in every visual check. And three working papers cited in chapter one had since been published, one with a different title and a materially smaller headline estimate than the version the thesis discussed, which meant a sentence in chapter one was true of the working paper and false of the published version. That sentence was rewritten and the published version cited.

The in-text citations were converted in the same pass as the list. Two ABNT-specific issues came up: the thesis contained fourteen direct quotations, all of which needed page numbers that four of them lacked, and the institutional authors, of which there were nine, needed the acronym and full name handled consistently on first and later mentions.

The hyperlinks were applied last, on the author-year text, with the DOI behind each. A final integrity check found six links pointing at records that no longer matched their citation, all of them in chapter one, all copied from an earlier draft where the neighbouring citation had since been changed.

**Result.** 206 entries, all resolving, one style, deposited with two days to spare. The BibTeX file went into the project repository as the single source, and the two chapters that later went out as articles were converted to their journals' styles in about ninety minutes each, from the structured records, without a reconciliation problem. The total cost was roughly twenty hours, of which the two days lost to find-and-replace were avoidable and are the reason the method's step six is worded as it is.

### A second scenario, where it goes differently

A journal submission where the house style is numbered in order of first appearance and the production system strips author-supplied hyperlinks.

The reconciliation and verification steps are identical, and two things change. The in-text form is no longer author-year, so the hyperlinked house standard cannot apply in the body; the DOI moves into the reference list where the style prints it, and the manuscript keeps a separate author-year working copy so the authors can still read their own draft. The numbering introduces a failure mode the author-year form does not have: renumbering after an insertion. A citation added in revision to paragraph three shifts every subsequent number, and a manuscript edited by three coauthors in a word processor without a citation manager will get this wrong. The rule for that case is to keep the manuscript in author-year form until the final submission version and convert to numbers once, at the end, from the structured records.

The second difference is anonymisation. That journal used double-blind review, so nine self-citations had to be checked. Three were phrased as "in our earlier work", which identifies the authors; they were rewritten to third person while keeping the citation, which is the standard that preserves the scholarly record without breaching anonymity. Removing the citations entirely, which the authors initially proposed, would have made the literature review incomplete and would have looked strange to any referee who knew the field.

## Output

Four deliverables, in this order.

**Reconciliation report:**

| Set | Count | Items | Action taken |
| --- | --- | --- | --- |
| Cited but not listed | 11 | [author, year, location in text] | Entry added from verified record |
| Listed but not cited | 25 | [entry] | 19 removed, 6 were spelling mismatches |
| Mismatched text and list | 6 | [what differs] | Corrected in both |

**Verification report:**

| # | Entry as listed | Identifier | Resolves to the right record | Status | Action |
| --- | --- | --- | --- | --- | --- |

Status is verified, corrected, superseded by a published version, or unresolvable. Unresolvable entries are listed separately with the claim each supported.

**The formatted reference list**, in the resolved style, ready to paste, with the in-text citations converted in the same pass and the hyperlinks applied and tested.

**The style note:** which style applied, the source of that decision with its date, and every rule that was ambiguous with how it was resolved. Two paragraphs at most, and it saves the argument that otherwise happens at the next submission.

Plus, where the project uses LaTeX, the cleaned `.bib` file; and where it uses a reference manager, the keyed list of field-level corrections to apply in the library.

## Failure modes

**Converting by find-and-replace.** Recognise it when a spot check of five entries passes and the sixth is half converted. Journal articles are regular and everything else is not. Convert from structured records.

**Reconciling in one direction.** Recognise it when the list has entries nobody cites. Checking that every citation has an entry is the half people do; the other half is what removes the cut-paragraph leftovers.

**Trusting the DOI because it exists.** Recognise it by following three at random and finding one that lands on a neighbouring paper. This is `literature-verification`'s resolution rule applied a second time, at the end, because links drift during revision; visual inspection never catches it.

**Formatting before reconciling.** Recognise it when the beautifully formatted list still contains eleven entries that do not correspond to anything in the text. Reconcile first.

**The manager as the source of truth.** Reference manager records are imported from publisher metadata, which is frequently wrong about page ranges, issue numbers and author initials. Check the fields against the record, not against the library.

**Leaving an unresolvable entry in place.** Recognise it by any entry marked "could not verify" that is still in the list at submission. Remove it and flag the claim; an unsupported sentence is a smaller problem than a fabricated reference.

**Citing the working paper after the article appeared.** Recognise it by any preprint more than about two years old. Recheck each one; the published version often differs in sample and in headline number.

**Duplicate entries under different keys.** Recognise it when the same work appears twice in the list with different capitalisation. It comes from merged libraries and it survives because the two entries sort apart.

**Hyperlinks pointing at last draft's records.** Recognise it by testing rather than by looking. This is why step 9 is a separate step.

**Doing this at the end for the first time.** The reference apparatus is built during drafting, per `literature-verification`. This skill is the reconciliation and formatting pass, not the first time anyone checks whether the sources are real.

## Edge cases

**No lookup tool available.** Format from what exists, verify nothing, and deliver the list with every unverified entry visibly marked plus a separate list of them. Do not certify. Say plainly that verification is outstanding and what it would take.

**A thesis assembled from published articles.** Each chapter may keep the style it was published in where the regulations allow, but the consolidated bibliography, where the regulations require one, is in the university's style. Check the regulations, since institutions differ on this, and record the answer in the style note.

**Non-English sources.** Cite in the original language, with a translated title in brackets where the style requires. Do not cite a translated title as though it were the record. Transliterate consistently where the script differs, using the standard the field uses.

**Institutional and government authors.** Use the form the institution uses for itself, keep the acronym convention consistent between first and later mentions, and check the producer's own preferred citation for datasets and official statistics.

**A source that has moved or disappeared.** Cite the archived version with the archive date and note it. Grey literature, official reports and web sources move more often than journal articles, and an archived copy is the only thing that makes such a citation checkable later.

**Two works by the same author in the same year.** Assign the a and b suffixes by the style's ordering rule and apply them in the text and in the list in the same pass. Applying them in one place only is the most common ambiguity in a long thesis.

**A coauthor who will not use the reference manager.** Accept it and centralise: one person owns the `.bib` file, the others send citations as DOIs in the draft, and the owner adds them. Arguing about the workflow costs more than absorbing the work.

**A revision that changes the argument.** Rerun the reconciliation from scratch rather than patching. Revisions cut paragraphs, and the citations in those paragraphs are the ones that end up orphaned in the list.

## Quality bar

- Every in-text citation has a list entry, and every list entry is cited, checked mechanically in both directions.
- Every entry resolves to the correct record, confirmed by following the identifier, not by inspecting it.
- Every in-text citation is the hyperlinked author-year form, with groups separated by semicolons, and every link tested.
- The style is applied consistently to every entry, including the chapters, institutional authors, datasets and translated works.
- The list was produced from structured records, not by editing the previous style's strings.
- Unresolvable entries were removed and their claims flagged, with nothing left marked as unverified in the submitted file.
- The style note records which rule was applied, from what source, and how each ambiguity was resolved.
- The reconciliation was rerun after the final edit, not before it.

## Adapting this to your context

The house form here is hyperlinked author-year, the worked example is a Brazilian thesis in ABNT, and the tooling assumed is BibTeX. All three are defaults, not the method.

- **The field default in step 1.** The resolution order lists Chicago author-date for economics. Substitute yours: APA 7 in psychology, education and management, ASA in sociology, AMA or Vancouver in medicine and public health, ABNT in Brazilian institutions.
- **The hyperlinked author-year form.** It assumes an author-year style. Vancouver, Nature and IEEE number citations in order of appearance. Keep the manuscript in author-year and convert to numbers once, at the end, from the structured records.
- **The identifier.** DOI is assumed. Add PMID or PMCID for health sources, ERIC document numbers in education, registry numbers for trials, and dataset DOIs from ICPSR, OSF or a national archive. Record whichever your field's readers will search.
- **The tooling.** BibTeX assumes LaTeX. Zotero with a CSL style, EndNote or Mendeley do the same job in Word; keep one library as the single source and deliver field-level corrections rather than a retyped list.
- **What not to change.** Reconcile mechanically in both directions, convert from structured records rather than editing strings, and let nothing unresolvable reach a submitted list.

## Related skills

`literature-verification` owns the standard that a citation must exist and must support its claim, and it runs during drafting; this skill assumes that work was done and confirms the records still resolve. `full-manuscript-build` places this last in the writing order and includes citation reconciliation as one of its cross-section checks. `introduction-writer`, `data-section-writer`, `results-writing` and `discussion-and-conclusion` all generate citations under the hyperlinked author-year house form that this skill formats and reconciles. `theoretical-framework-review` and `systematic-review-protocol` produce the largest reference sets and are the most common source of duplicates. `journal-targeting` supplies the house style that step one resolves to. `replication-package` deposits the `.bib` file alongside the code.
