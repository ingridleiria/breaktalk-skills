---
name: peer-review-simulator
description: Runs an adversarial pre-submission review of a manuscript, thesis chapter, or proposal before an editor sees it: a desk-reject audit, full referee reports from a methodologist, a field expert, and a handling editor, a decision recommendation, and a revision plan ordered by what would sink the paper. Use this skill whenever a researcher asks "review my paper", "will this get rejected", "what will reviewer 2 say", "referee report", "pre-submission review", "is this ready to submit", "critique my manuscript", or "defend this chapter". Trigger before every submission and before sending a chapter to a supervisor or committee.
---

# Peer Review Simulator

A referee report received before submission is worth three received after it, because it can still be acted on without a rejection on the record. This skill produces the reports a demanding journal would send, in the order editors actually read: the desk-reject screen first, then the referees, then the decision.

## Stage 1: Desk-reject audit (the editor's ten minutes)

Editors reject most papers without review, on the abstract, introduction, and a skim of the tables. Simulate exactly that, reading only those parts, and answer:

- Is the research question stated and answerable?
- Is the contribution specific and credible relative to the closest work?
- Does the design plausibly identify the effect claimed?
- Is the main finding stated with a number in the abstract and introduction?
- Is the paper in scope for the stated target venue?
- Is the writing clear enough that the argument is followable on a skim?
- Are there immediate red flags: unverifiable citations, tables that do not match text, missing sample sizes, undefined variables, formatting far from the venue's norms?

Verdict: send to review, or desk reject with the reason. If desk reject, stop here and report; the revision plan starts with the desk-reject reasons.

## Stage 2: Three referee reports

Each report follows the standard structure: summary of the paper in the referee's words (which exposes whether the paper is understandable), major concerns numbered and ordered by severity, minor concerns, and a recommendation. Each concern states what is wrong, why it matters for the conclusion, and what would resolve it. No concern is raised without a proposed fix or an explicit statement that no fix exists.

**Referee 1, the methodologist**: identification and inference. Uses the identification-defense skill's attack list for the design in question. Checks that the equation, the code description, and the tables agree; that clustering matches treatment assignment; that pre-trends, first stages, or density tests are reported and powered; that robustness addresses the real threats rather than decorative ones; that magnitudes are interpreted and causal language matches the design.

**Referee 2, the field expert**: contribution and literature. Checks the closest papers are engaged and the difference from them is real; that the theoretical framework predicts the sign; that the setting's institutional details are right (the referee knows the setting); that the interpretation is consistent with what the field has found elsewhere, with disagreements named; that the policy implications match the estimand. Verifies a sample of citations against real records and reports any that fail.

**Referee 3, the handling editor's reader**: structure, writing, exhibits, and compliance. The five moves of the introduction, the abstract's traceability to results, table and figure standards (booktabs, monochrome, legends outside), consistency of numbers across abstract, text, and tables, length against the venue's limit, reference style, and ethics or data availability statements.

Each report ends with a recommendation from the usual set: accept, minor revision, major revision, reject and resubmit, reject.

## Stage 3: The editor's decision

Weigh the three reports as an editor would: methodological concerns dominate; contribution concerns decide between major revision and rejection; writing concerns rarely sink a paper alone but compound the others. State the decision, the two or three issues that determined it, and what the editor would write in the decision letter.

## Stage 4: The revision plan

Ordered by what would sink the paper, not by section order:

1. Issues that change the conclusion (identification, wrong estimator, sample problems).
2. Issues that change the credibility (missing diagnostics, unverified citations, mismatched numbers).
3. Issues that change the reception (framing, contribution, magnitude interpretation).
4. Issues that change the reading (structure, exhibits, length, style).

Each item: the issue, the fix, the exhibit or section affected, and an effort estimate (hours or days). The user should be able to start on item one immediately.

## Conduct

- Read the entire manuscript before writing any report; a referee who skims is the failure being simulated, not the standard.
- Quote the manuscript when identifying a problem, with the page or section.
- Be as hard as a top journal's referee and as specific as a good one. Vague hostility ("the contribution is unclear") is not a report.
- Do not invent problems to appear thorough; if a section is sound, say so in one line.
- Verify citations and numbers rather than assuming them.
- When the honest verdict is that the paper should not be submitted yet, say so first.

## Quality bar

- The desk-reject audit reads only what an editor reads.
- Every major concern has a stated consequence and a proposed fix.
- The three reports disagree where real referees would; they are not one report in three voices.
- The revision plan is ordered by severity with effort estimates.
