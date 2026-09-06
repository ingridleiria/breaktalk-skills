---
name: literature-verification
description: Zero-hallucination citation and literature workflow for academic writing. Verifies every reference against real bibliographic records before it enters a draft, and builds literature reviews from confirmed sources only. Use this skill whenever a researcher asks to find papers, build a literature review or related-work section, add citations to a draft, check whether references are real, create a bibliography or BibTeX file, or asks "what does the literature say about X". Trigger on any academic writing task that will contain citations, even when the user does not mention verification, because unverified AI-generated citations are the failure this skill exists to prevent.
---

# Literature Verification

AI-generated text is very good at producing plausible citations to papers that do not exist. In academic work this is not a small error; a fabricated reference can sink a submission, a defense, or a reputation. The rule of this skill is absolute: no citation enters a draft until it has been verified against a real record.

## The verification standard

A citation counts as verified when all of the following are confirmed against a live source (a DOI resolver, a publisher page, a bibliographic database, or the paper itself):

1. The authors, year, and exact title match a real published record.
2. The venue (journal, volume, or conference) matches that record.
3. The DOI resolves, when one exists. For working papers, the repository link resolves instead.
4. The paper actually supports the claim it is attached to. Read at least the abstract; a real paper cited for something it does not say is as wrong as a fake one.

Anything that fails any check is either repaired against the real record or removed. There is no third option, and there is no "probably real". When search tools are unavailable and verification is impossible, do not emit a formatted citation; write a visible placeholder such as [citation needed: staggered DiD estimator paper, around 2021] and tell the user which claims still need verified sources.

## Workflow for a literature search

1. **Decompose the question** into 2 to 4 search themes (the outcome literature, the method literature, the setting or country literature).
2. **Search each theme** using the available tools (web search, and scholarly databases or MCP connectors when connected, such as Crossref, OpenAlex, Semantic Scholar, or Consensus). Prefer peer-reviewed and well-cited work, but include recent working papers where the frontier lives.
3. **Screen** by reading abstracts, and record simple counts: how many found, how many relevant, how many kept. This keeps the review honest about coverage.
4. **Build an evidence matrix** before writing: per paper, one row with authors and year, setting and data, method, sample size where stated, main finding with its direction and magnitude, and how it relates to the user's question (supports, contradicts, extends). The matrix is the deliverable that makes the written review fast and accurate.
5. **Write the review from the matrix**, organized by theme or by finding, never as an annotated list marching paper by paper. Where the literature disagrees, name who disagrees and cite both sides rather than writing that findings are mixed.

## Workflow for citing while drafting

- Every empirical or theoretical claim in academic prose carries a citation, placed in the sentence that makes the claim.
- Verify at the moment of citing, not in a cleanup pass at the end. Cleanup passes get skipped.
- Maintain the reference list in the same session: each verified citation is appended to the bibliography (or BibTeX file) as it is used, so text and references never diverge.
- Match the citation format the user's target requires (author-year, numbered, or a journal house style) and keep it consistent through the document.

## Failure modes to refuse

- Citing from memory. Model memory of bibliographic details is unreliable by construction; the details must come from a live lookup performed in this session.
- Padding a review with tangential famous papers to look thorough.
- Attributing a specific number to a paper without having seen that number in the paper's abstract or text.
- Silently dropping a contradicting paper the search surfaced. If the literature cuts against the user's hypothesis, the review says so; that is what the review is for.
