---
name: theoretical-framework-review
description: Reviews, builds, or repairs the theoretical framework (referencial teórico) of a thesis chapter, journal article, or research proposal, using the Consensus academic search connector when available and other scholarly sources otherwise, so every theory, mechanism, and prior finding is anchored to a verified paper. Use this skill whenever a researcher asks to write or review a theoretical framework, conceptual framework, theory section, background section, or "referencial teórico", wants to know which theory explains a mechanism, needs to connect hypotheses to established theory, asks "what does the evidence say about X", or is told by a reviewer that the theoretical grounding is weak. Trigger for any academic text that must justify why an effect is expected, not just whether it was found.
---

# Theoretical Framework Review

The theoretical framework answers one question a referee will ask: why should this effect exist at all? A results section shows what happened; the framework explains the mechanism that made it happen, anchored to theory and to prior evidence. A framework that lists famous authors without connecting them to the paper's hypotheses is decoration, and reviewers recognize it immediately.

## Two modes

**Review mode**: the user has a draft framework. Diagnose it before rewriting.
**Build mode**: the user has a research question and hypotheses but no framework yet. Construct it from the question outward.

Both modes run on verified sources only; see the literature-verification skill in this library for the citation standard, which applies in full here.

## Review mode: the diagnostic

Read the draft and score it against these criteria, quoting the draft where it fails:

1. **Traceability**: can each hypothesis in the paper be traced to a specific theoretical mechanism in the framework? List every hypothesis and the paragraph that grounds it. An unhypothesized paragraph or an ungrounded hypothesis is a gap.
2. **Mechanism, not name-dropping**: does the framework explain how the theory produces the expected effect in this setting, or does it only state that Author (Year) proposed the theory? The test: could a reader predict the sign of the main coefficient from the framework alone?
3. **Currency and relevance**: are the key sources the ones the field currently cites for this mechanism, including work from the last five years, and are they from the setting or population that matters (country, sector, level of education, market type)?
4. **Contested ground**: where the literature disagrees about the mechanism or the sign, does the framework name both sides, or does it present one side as settled?
5. **Verification**: does every citation resolve to a real record that says what the draft claims? Check each one. Fabricated or misattributed references are the most common and most damaging failure in AI-assisted drafts.
6. **Structure**: does the section move from the general theory to the specific setting to the hypotheses, or does it wander? Is each subsection there because a hypothesis needs it?

Deliver the diagnostic as a short table (criterion, finding, evidence from the draft, fix), then a rewritten section if the user wants one.

## Build mode: the construction sequence

1. **Name the mechanism** for each hypothesis in plain words before searching. "Institutions raise entry costs, which pushes marginal entrepreneurs into informality" is a mechanism. "Institutional theory" is a label.
2. **Search for the anchoring theory** per mechanism. With the Consensus connector available, run focused queries on the mechanism as a claim ("does regulatory burden reduce formal business entry"), read the returned abstracts, and note the direction of evidence, the settings studied, and the sample sizes. Use other scholarly databases (Crossref, OpenAlex, Semantic Scholar, discipline repositories) and web search to locate the foundational theory papers Consensus may not surface, and to confirm every DOI.
3. **Build the evidence matrix**: per source, one row with authors and year, theory or mechanism, setting and data, method, finding with direction and magnitude, and which hypothesis it grounds. Mark whether each source supports, qualifies, or contradicts the expected effect.
4. **Write from the matrix**, in this order:
   - The general theory and its core prediction, with the foundational sources.
   - The mechanism in this paper's setting, with the empirical evidence closest to the setting, numbers included where the sources give them.
   - Where the literature disagrees, both sides named and cited.
   - The hypothesis, stated formally, as the conclusion of the paragraph that grounded it.
5. **Close the section** with the hypotheses restated together, each traceable to the paragraph above it. No summary of the summary.

## Writing standards

- Impersonal academic register unless the field or journal expects first person.
- Every empirical or theoretical claim carries an author-year citation in the sentence that makes it, formatted in the target style consistently.
- Dense in specifics: settings, years, sample sizes, effect sizes from the cited work. A framework that could preface any paper on any topic has failed.
- Contradicting evidence is engaged, not omitted. If the closest study to the user's setting found the opposite sign, the framework says so and explains why this paper expects a different result, or revises the hypothesis.
- The reference list is built in the same session, one verified entry per citation used, in the style the target requires.

## Quality bar before returning

- Every hypothesis has a grounding paragraph; every grounding paragraph feeds a hypothesis.
- Every citation verified against a live record this session, and the abstract read to confirm it supports the attached claim.
- The main coefficient's expected sign can be predicted from the framework alone.
- The section is the length the target venue expects, and no longer.
