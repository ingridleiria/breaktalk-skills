---
name: references-and-bibliography
description: Manages citations and reference lists for papers, chapters, and theses: resolves which style applies, formats in-text citations and reference entries in APA 7, Chicago author-date, ABNT, Harvard, and journal house styles, converts a list between styles, keeps BibTeX and reference-manager libraries clean, and verifies that every entry resolves to a real record before submission. Use this skill whenever a researcher asks to format references, fix the bibliography, convert citations to another style, check that citations are real, produce a BibTeX file, reconcile in-text citations with the reference list, or prepare references for a specific journal or a university thesis template. Trigger for the reference list of every submission and for any citation formatting question.
---

# References and Bibliography

A reference list has two jobs: let a reader find every source, and prove to a referee that the author is careful. Both fail on a single fabricated or malformed entry. This skill formats to the required style and verifies every entry against a live record, in the same pass.

## Step 1: Resolve the style

Determine the style from, in order: the target journal's author guidelines (fetch them and cite the rule), the university's thesis regulations, the field default (APA 7 in education and management, Chicago author-date or a house style in economics, ABNT in Brazilian institutions), or the user's stated preference. State which applies and why before formatting.

Key differences to handle explicitly:

- **APA 7**: author-year in text with "and" or "&" per context; reference list alphabetical, sentence-case titles, DOI as a URL.
- **Chicago author-date**: similar in text; title-case titles; DOI or URL at the end.
- **ABNT (NBR 6023 and 10520)**: author surnames in capitals in the reference list, in-text citations in the form (SURNAME, year) or Surname (year) depending on the sentence, specific rules for "et al.", page numbers for direct quotes, and Brazilian conventions for institutional authors.
- **Numbered house styles**: numbered in order of first appearance, with the list in that order.
- **Journal house styles** (economics journals often have their own): fetch and follow; do not assume.

## Step 2: Reconcile text and list

Extract every in-text citation from the manuscript and every entry in the reference list. Report three sets:

- Cited but not listed (must be added).
- Listed but not cited (must be removed or cited).
- Mismatches in author spelling, year, or "et al." usage between text and list.

Fix all three before formatting; formatting a list that does not match the text is wasted work.

## Step 3: Verify every entry

Apply the literature-verification standard to each entry: authors, year, title, venue, volume, pages, and DOI confirmed against a live record (DOI resolver, publisher page, or a bibliographic database). Working papers and reports are verified against their repository or institutional page. Books are verified against the publisher or a library catalog.

Report the outcome per entry: verified, corrected (with what changed), or unresolvable. Unresolvable entries are removed from the list and flagged to the user with the claim they supported, so the text can be revised. Never leave an unverified entry in a submitted list.

## Step 4: Format

Produce the reference list in the resolved style with consistent punctuation, capitalization, italics, and DOI presentation. Sort as the style requires. Handle the recurring edge cases: multiple works by the same author in the same year (a, b suffixes, applied in both text and list), institutional authors, translated works, datasets and software (cited with version and DOI where available), preprints with later published versions (cite the published version), and legal and policy documents under ABNT.

## BibTeX and reference managers

- One clean `.bib` file per project, entries keyed consistently (authorYEARkeyword), fields complete (author, title, journal, year, volume, number, pages, doi), no duplicate entries, no trailing whitespace or stray braces.
- Titles protected where capitalization must be preserved.
- Provide the cleaned `.bib` when the user works in LaTeX, and a formatted list for Word.
- For Zotero or Mendeley users, provide the corrections as a list of entries to fix, keyed by title.

## Conversion between styles

Convert from the verified structured data (not by editing strings), so the output is correct in the new style rather than a patched version of the old one. Convert in-text citations and the list together.

## Deliverables

1. The reconciliation report (three sets).
2. The verification report per entry.
3. The formatted reference list in the target style, and the `.bib` file when relevant.
4. A short note on any style rule that was ambiguous and how it was resolved.

## Quality bar

- Every in-text citation has a list entry and vice versa.
- Every entry is verified against a live record or removed.
- Style is applied consistently to every entry, including edge cases.
- The list can be pasted into the submission without further editing.
