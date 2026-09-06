---
name: content-quality-gate
description: A nine-check pass or fail gate that every piece of buyer-facing content must clear before it ships, covering audience specificity, problem-first framing, the belief it advances, the method it reflects, the shift it shows, terminology fidelity, sourced proof, human voice, and a single call to action. Use this skill whenever the user asks to draft or review a LinkedIn post, email, blog, proposal, deck, landing page, one-pager, or any external content; whenever they ask whether a draft is ready to ship, on brand, or good enough; and as the final check after any other skill has produced a draft. Trigger on "QA this", "is this ready", "does this pass", "brand review", and "make this sharper".
---

# Content Quality Gate

Most weak content is not badly written. It is written to nobody, about nothing anyone is losing sleep over, with numbers no one can trace. This skill is the gate that sits above every format skill: another skill produces the draft, this one decides whether it ships. Nine checks, each with a literal pass test. Any red is a rewrite, not a discussion.

Run it in one of two modes. In drafting mode, resolve checks 1, 3, 4, and 7 before writing a word. In review mode, read the full piece once, then go check by check and quote the specific sentence that passes or fails each one. Never answer "looks good"; apply the test.

## First, load the standard

This gate is generic by design. Before the first run for a given organization, capture its specifics once and reuse them:

- The buyer segments and personas the organization sells to, with the pains each feels in their own words.
- The two or three core beliefs the organization argues for.
- The named method, process, or framework the content must reflect, with its real stage or component names.
- The terminology rules: what each proprietary term is and is not, what is capitalized, what is never said.
- The approved claims list: every statistic and client result cleared for external use, with its source.
- The house voice rules and the default call to action.

Store these in a `standard.md` beside this skill. Without them, checks 1, 3, 4, 6, and 7 can only be checked in outline.

## The nine checks

**1. Written for a named buyer.** One persona, one segment, one trigger event. State the problem in words the reader would recognize as their own sentence, not a category label. *Pass test:* can you name the persona, the segment, and the trigger, and quote the problem the way they would say it? If the honest answer is "anyone in this industry", it fails.

**2. Problem before authority.** The reader is the protagonist and the organization is the guide. Open on their world, name the cost of it, then bridge. *Pass test:* cover the organization's name in the opening paragraph. Does the reader still see themselves? If not, it fails.

**3. Anchored in a core belief.** Every piece advances one of the organization's stated beliefs, and the reader should feel it rather than read it as a footnote. *Pass test:* name the belief and the sentence that carries it.

**4. Anchored in the method.** A claim about a stalled deal maps to a named stage. A claim about maturity maps to a named component. The method is the argument, not decoration, and its names and order are used exactly. *Pass test:* name the stage or component this piece supports. If the answer is the whole discipline in general, it fails.

**5. Shows the shift.** Buyers move when standing still becomes intolerable, not when a solution sounds good. Draw the old way against the new way and, where the approved claims allow, size the cost of the old way. *Pass test:* is there a visible before and after? A piece that is purely informational moves nobody.

**6. Terminology and product fidelity.** Proprietary terms are used with their exact definition, capitalization, and category. The never-say list is checked word by word. *Pass test:* scan the never-say list. One hit is a rewrite, not a nitpick.

**7. Proof with integrity.** Only claims on the approved list, attributed where they belong to a named client. Anything else is marked `[NEEDS SOURCE]` and escalated rather than approximated. *Pass test:* point to the source for every number. One invented statistic costs more trust than the rest of the piece builds.

**8. Human voice.** Specific, confident, unpadded. No generic business vocabulary used on autopilot, no dashes standing in for commas and colons, no emoji, correct fonts and palette on any branded asset. *Pass test:* does it read as though an operator wrote it, or as though it was generated?

**9. One clear next step.** Exactly one primary ask, matched to the funnel stage: a read or a follow at awareness, a subscribe or a download at nurture, a conversation at the bottom. *Pass test:* what is the one thing the reader should do, and is it unmissable? Three asks and none are the same failure.

## The filter in one line

Right buyer, real problem, one belief, a real method, a visible shift, exact language, honest proof, human voice, clear next step.

## Output

Always render the table, filled in, with a specific fix beside every fail.

| Check | Verdict | Evidence or fix |
| --- | --- | --- |
| Named buyer | pass / fail | persona, segment, trigger, or what is missing |
| Problem first | pass / fail | the opening sentence, or the rewrite needed |
| Core belief | pass / fail | which belief, and the sentence carrying it |
| Method anchor | pass / fail | the named stage or component |
| The shift | pass / fail | the contrast, or that there is none |
| Terminology | pass / fail | any term used wrongly, quoted |
| Proof | pass / fail | source per number, or `[NEEDS SOURCE]` items |
| Voice | pass / fail | the tells found, counted |
| Next step | pass / fail | the single ask, or the competing asks |

Close with the verdict, "ship" or "rewrite", and the ordered list of rewrites required.

## Quality bar

- Every check answered with evidence quoted from the piece, never with an adjective.
- Every number traced to the approved list or flagged, never approximated.
- Fails come with the specific fix, not with a restatement of the check.
- The gate is run even when another skill produced the draft, especially then.
