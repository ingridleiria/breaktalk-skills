---
name: demo-call-transcript-generator
description: Generates realistic synthetic sales call transcripts and multi-call deal histories for demonstrating, training on, or testing a call analysis process. Produces a written specification before any dialogue, a cast fixed in advance, an evidence ledger saying exactly what becomes buyer-established on which call and what stays a seller assertion, a metadata header that makes a deal history readable without opening the dialogue, calls long enough to behave like real ones, and a portfolio with genuine contrast including at least one deal that does not resolve. Use this skill when someone needs demo or test call data, sample transcripts, training material for coaching, synthetic deal histories, or a worked example to show an analysis or scoring tool against.
---

# Demo Call Transcript Generator

Synthetic transcripts fail in two directions and both are expensive. Too polished, and the first call settles the budget, the authority, the timeline and the pain, which demonstrates nothing: an analysis run over it returns a full sheet of green, the person watching concludes the analysis is trivial, and anyone trained on it learns that a good call is one where the buyer explains their own business case unprompted. Too thin, and the dialogue reads as a script with stage directions, nobody believes it, and the demonstration becomes a conversation about the transcript rather than about the work.

The specific failure this prevents is a process certified against material that was written to make it look good. A scoring approach tuned on transcripts where every claim is confirmed will not notice a real call where nothing is, which is the exact case it exists to catch. The fix is structural: design the deal and its evidence before writing a word of dialogue, and treat missing evidence as correct rather than as a gap to be filled.

This pairs with `sales-call-analysis`, which is what these transcripts are almost always generated to be read by, and it inherits that skill's evidence logic exactly: a thing is established only when the buyer says it or confirms it by adding to it.

## When to use this, and when not to

Use it to build demonstration material for an analysis or coaching process, to create a training set for new sellers or new managers, to regression-test an analysis prompt or rubric after a change, to produce worked examples for documentation, and to give a coaching workshop material that nobody has to get customer permission for.

Do not use it to rehearse a live conversation, which is `sales-roleplay` and needs a person responding in real time. Do not use it in place of analysing real calls; synthetic material calibrates a process, real material judges a deal, and `sales-call-analysis` is where that judgement belongs. Do not use it to manufacture evidence that looks like a real customer: a synthetic transcript presented as a genuine call is fabrication, whatever the intention, and that is true for case studies, references and sales collateral. Do not use it for research interview material, where `customer-interview-synthesis` sets the standard for what a body of interviews should look like.

## What you need before starting

**What the material is for, and who will read it.** A demonstration for a buyer of an analysis tool, a training set for a workshop, and a regression fixture for testing all need different things: the demonstration needs a satisfying arc, the training set needs errors worth discussing, and the fixture needs one variable changed at a time. Missing: assume a demonstration set of three deals and say so, because it is the most common case and the easiest to repurpose.

**The end state of each deal, decided before writing.** What the buyer has confirmed by the last call, what remains a seller assertion, and which decisive unknowns are still open. Missing: choose one from the portfolio patterns below and write it down in one paragraph. Writing the end state first is the single control that stops dialogue drifting into an outcome nobody intended.

**The product, the price band, and the industry.** These set what is realistic to say, and the currency belongs in the specification alongside the figure. A tool at 12,000 US dollars a year does not have a security review and a 900,000 dollar platform does not close in one call. Missing: default to a mid-market business software product at 40,000 to 80,000 US dollars annually and name both the band and the currency in the specification.

**The cast.** One seller with a title, the account, the primary buyer-side contact, and the secondary stakeholders who appear later. Missing: invent them, and check the names against the constraint that they must not resemble any real company or person connected to the work.

**How many calls, and at which stages.** Missing: default to five calls, two discovery, two ideation, one proposal, which is the smallest set that shows real movement.

**The file naming and storage convention.** Missing: use `account_stage_NN_YYYY-MM-DD.md` and make the seller name and date inside the header match the filename exactly, since the mismatch is the most common defect in a generated set.

**Whether the material will ever be seen outside the team.** Missing: assume it will, and label every file as synthetic in the header, which costs nothing and prevents the one serious accident this skill can cause.

## The method

1. **Write the specification before any dialogue.** One page per deal: the account and industry, the cast with roles, the number of calls and their stages, the end state in a paragraph, and the evidence ledger. This is the actual work. Dialogue written from a specification takes an hour and holds together; dialogue written first and reconciled afterwards takes longer and still drifts.

2. **Build the evidence ledger.** One row per fact that matters, with a column per call, marking each cell as established by the buyer, asserted by the seller only, or absent. This is what makes a generated set testable, because it is the answer key: run the analysis, compare its established list against the ledger, and any difference is either a defect in the transcript or a defect in the analysis, and you now know which.

3. **Fix one owner per deal.** The same seller runs every call on an opportunity for its whole life. Swap them only for a deliberate handoff scenario, and then make the handoff a visible moment in the dialogue rather than a silent change of name, since a silent change is read as a generation error and destroys confidence in everything else.

4. **Distribute evidence across the calls deliberately, not evenly.** Realistic deals move in steps and plateaus. A workable default across five calls: three or four established items on call one, two on call two, then either a jump of five or six when a new stakeholder joins, or a flat call where nothing is added, which is the most instructive transcript in any training set. Ensure at least one item established early is contradicted or qualified later, because deals do that and no synthetic set ever includes it.

5. **Write the metadata header before the dialogue.** Seller with title and company, account, buyers with titles and roles, attendees for this specific call, date, stage, and the synthetic label. The header is what makes a deal history readable by a person or a script without opening the dialogue. Never invent a recording URL, a link, or anything shaped like one; a plausible-looking link in a demonstration file will eventually be clicked, and it teaches the reader that fabricated artefacts are acceptable in this material.

6. **Allocate the word budget before writing, then write to it.** Thirty to forty minutes of real conversation is roughly 4,000 to 5,500 words, and that is a floor rather than a ceiling to undershoot. A workable split: 8 percent opening and rapport, 7 percent agenda, 70 percent substance in two or three distinct movements, 15 percent close and next step. Padding one section to hit a count is visible immediately; a call that spends nine hundred words on the weather is not a long call, it is a short call with a preamble.

7. **Write the dialogue with the textures that make analysis meaningful.** Every call needs interruptions, at least one unfinished sentence, one place where the seller asks a weak question and pays for it, and at least one buyer non-answer of each of the four kinds the analysis is built to catch: the polite acknowledgement, the subject change, the question that ignores the claim, and the silence the seller fills. Keep the distinction alive between a buyer politely agreeing with urgency the seller supplied and a buyer stating their own reason to change now. The first is not evidence, and writing it as though it were is the single most common way a synthetic transcript becomes useless.

8. **Calibrate the next step to the intended state.** Real, when the deal is meant to be advancing: a date, a named person on each side, something the buyer does, a stated purpose. Partial, when it is meant to be ambiguous: two of the four. Hollow, when it is meant to be stalled: "we will circle back." A set where every call ends in a real next step cannot demonstrate the next-step test at all.

9. **Check the length, by counting.** Do not assume. A generated transcript that feels long is usually around 2,600 words, well under the band, and short transcripts are the reason demonstration sets feel thin without anyone being able to say why.

10. **Read it back as the analysis would, and reconcile against the ledger.** Run the four passes: what the buyer established, what the seller asserted without uptake, what remains unknown and decisive, and whether the next step is real. Compare with the ledger. Where they disagree, the transcript is wrong, not the ledger, because the ledger is the specification. This step catches roughly one defect per call and takes ten minutes.

## The evidence ledger

The artefact that makes the difference between a set that can be tested and a set that can only be admired. Mark each cell E for established by the buyer in their own words, A for asserted by the seller with no buyer uptake, and a blank for not raised.

| Fact | Call 1 discovery | Call 2 discovery | Call 3 ideation | Call 4 ideation | Call 5 proposal |
| --- | --- | --- | --- | --- | --- |
| Current process and its cost | A | E | E | E | E |
| Why now, in the buyer's words | | A | A | E | E |
| Who else approves | | | A | E | E |
| Budget range | | | | A | A |
| Alternatives being considered | | A | | | E |
| Consequence of doing nothing | A | A | A | A | A |

The bottom row is deliberate. A fact that stays at A for the whole set is what produces a realistic unresolved deal, and it is what an analysis process should surface at the end as the thing nobody ever established.

## Portfolio patterns

Build contrast rather than three versions of one story. A set of three should contain one of each.

**The advancing deal.** Little established at first, then the buyer progressively owns the problem, the numbers and the process, and by the last call most of what matters is confirmed in their own words. The reliable signal that a deal is really advancing is a buyer who starts acting rather than only talking: sending data, booking a colleague in, running a comparison themselves.

**The stalled deal that recovers.** Two or three calls of little movement against a real obstacle such as a passive contact or a spending freeze, then a specific named turning point: a new stakeholder joining, a budget cycle opening, a competitor's failure. The turn is a moment in the dialogue with a person and a sentence attached, not a general improvement in tone.

**The honest early deal.** Cautious, stops at discovery or ideation, ends with decisive unknowns open, and is never forced to a resolution. This is the one that shows a patient sales motion, and a set without it teaches that every deal resolves, which is the most damaging thing a training set can teach.

Where the set runs to four or five deals, add one that is lost for a reason visible on call two and invisible to the seller until call five, which is the most useful transcript a manager will ever read.

## Worked example

**Situation.** A team building an internal coaching process needed material for a workshop with nine new sellers. Customer recordings existed but could not be used, since consent covered internal quality review only and the workshop included two contractors. The requirement was three deal histories, five calls each, in a facilities management context, ready in four days.

**Task.** Three deal histories of up to five calls each, roughly 70,000 words in total, where an analysis run over them produces visibly different verdicts and the differences are explainable in a room. All monetary figures in this example are in US dollars.

**Action.** The first attempt wrote dialogue first, three calls of the advancing deal, on the theory that the specification could be inferred afterwards. It was abandoned after a check on call two. Reading it back through the four passes showed the buyer had restated the seller's savings figure in their own words at minute nineteen, and had named the finance approver unprompted, which meant the deal was already largely qualified at call two of five. Everything intended for calls three and four had nowhere to go, and the honest options were to rewrite the later calls as a formality or to rewrite call two. The cost of the wrong turn was about 4,500 words discarded. The lesson generalises: dialogue drifts toward resolution, because writing a buyer who withholds is uncomfortable in a way that writing a buyer who cooperates is not.

The rebuild started with three ledgers. The advancing deal moved eleven facts from blank to established across five calls, with a deliberate plateau at call three where nothing moved and the seller talked too much. The recovering deal kept everything flat for two calls behind a capital freeze, then introduced a new operations director on call three who had run a similar project elsewhere and who moved four facts in one conversation. The honest early deal established six facts in total and left both the money and the approval route at asserted-only for the whole set, ending on a hollow next step at call four and a fifth call that never happened, which was recorded as a note rather than written. That is why the set runs to fourteen transcripts rather than fifteen: the unwritten call is the point of the deal, and writing it to make the count round would have removed the only unresolved outcome in the portfolio.

Word counts were checked rather than assumed. The first drafts came in at 2,900, 3,100 and 2,700 words against a 4,000 floor, which is the usual undershoot. Expanding them meant adding a second movement to each call, typically a tangent about an adjacent problem that goes nowhere, which is what real calls contain and what makes the transcript feel like a recording.

Then all fourteen were read back through the four passes. Six defects surfaced: two next steps that were stronger than the ledger intended, one seller name that changed spelling between call three and call four, one buyer confirming a fact the ledger had marked as never established, one call at 3,400 words after editing, and one invented reference to a shared folder that read like a real link.

**Result.** Fourteen transcripts, 66,600 words, delivered in three and a half days, with the ledgers included as the answer key and a one-line note in place of the fifteenth call. In the workshop, the eleven-fact advancing deal and the six-fact honest deal produced exactly the argument the material was built to produce, which was whether the honest deal should be in the forecast at all. Two of the nine sellers said afterwards that the flat call three was the most useful of the fourteen, because it was the one that resembled their own week.

One caveat worth recording: two participants found the recovering deal's turning point convenient. It was written as a single conversation in which a new stakeholder solved the blockage, which happens, but less often and less cleanly than the transcript showed. The next version spread the recovery across two calls with a partial setback in between.

### A second scenario, where it goes differently

Building a regression fixture to test whether a change to an analysis process still catches near-miss confirmations. Different requirements throughout.

Length drops: twelve to fifteen hundred words per fixture, because the fixture tests one behaviour and a full-length call adds noise without adding coverage. Volume rises: sixteen short transcripts rather than three long histories. And the design principle inverts, from realism to isolation. Each pair differs in exactly one thing: in the first, the buyer says "yeah, that is right" to the seller's cost figure; in the second, the buyer says "yeah, that is right, we worked it out at about 300,000 dollars last year". Everything else in the two transcripts is identical, word for word. The analysis must mark the first as asserted and the second as established, and if it does not, the fixture has located the failure precisely.

The ledger becomes the assertion set, one expected classification per fixture, and the whole set can be rerun automatically after any change. Portfolio contrast, arc and emotional realism all stop mattering. What matters is that only one variable moves.

## Output

Every transcript opens with the same header, then the dialogue, then nothing else.

```
SYNTHETIC TRANSCRIPT: generated training material, not a real call
Account:     Northgate Facilities Group (invented)
Industry:    Facilities management, 2,400 staff, 11 regional sites
Seller:      Priya Ramanathan, Account Executive, [vendor]
Buyers:      Tom Ellery, Head of Operations (primary)
             Dawn Whitcombe, Finance Business Partner (from call 4)
Attendees:   Priya Ramanathan, Tom Ellery
Call:        3 of 5
Stage:       Ideation
Date:        2026-03-11
Length:      34 minutes, 4,410 words
File:        northgate_ideation_03_2026-03-11.md
```

Deliver alongside it a set-level file containing, for each deal, the end state paragraph, the evidence ledger, and a one-line note of what the deal is meant to demonstrate. The ledger is the answer key and the reason the set can be used as a test rather than only as an illustration.

## Failure modes

**The buyer who narrates the business case.** Recognise it when a buyer speaks a paragraph containing a quantified problem, a timeline and an approval route. Real buyers give one of those at a time and only when asked. Fix by splitting the paragraph across three calls, or by having the seller ask for it and get two thirds of it.

**Dialogue written before the ledger.** Recognise it when the deal is resolved by call two and the later calls are ceremonial. Fix by rebuilding from the specification and accepting the discarded words.

**Undershooting the length while feeling finished.** Recognise it by counting: under 4,000 words for a call described as thirty to forty minutes. Fix by adding a second movement rather than lengthening the existing one.

**Cast drift.** Recognise it when a name, a title, a company size or a site count changes between calls. Fix by keeping the cast block in the specification and copying it into each header rather than retyping it.

**Fabricated artefacts.** Recognise it by anything that looks like a link, a recording identifier, a system reference or an attachment. Fix by removing it. The header carries all the metadata that is needed.

**Every deal resolving.** Recognise it when all three deals end in agreement. A set with no unresolved deal teaches a false standard and cannot exercise the parts of an analysis that matter most.

**Numbers that do not survive arithmetic.** Recognise it when a stated headcount, site count and cost per site do not multiply out, or when a figure changes between calls with no one noticing in the dialogue. Fix by keeping the deal's few real numbers in the specification and deriving anything else from them. A buyer correcting the seller's arithmetic is realistic; the transcript contradicting itself silently is a defect.

**Synthetic material escaping into a real system.** Recognise it when a demonstration account appears in a customer record or a report. Fix with the synthetic label in the header, an invented account name that could not be mistaken for a customer, and storage separate from anything operational.

## Edge cases

**One call needed rather than a history.** Write the specification anyway, in five lines, with the end state and the four or five facts that will be established. A single transcript with no specification drifts faster than a set, because there is no later call to keep it honest.

**A very short sales cycle.** Where a real deal closes in two calls at 8,000 US dollars a year, do not stretch it to five. Shorten the set, keep the evidence sparse, and note in the specification that the pattern being demonstrated is velocity rather than complexity.

**Audio-style artefacts.** Where the material will be shown next to real machine transcription, include what that produces: false starts, crosstalk marked as such, an occasional mis-heard word, timestamps if the real ones carry them. Where the material is for reading, leave them out; they cost legibility and buy nothing.

**A second language, or a mixed-language call.** Write the language switch where it would really happen, usually in an aside between two colleagues on the buyer side, and keep the agreement markers accurate to the language, since their strength varies and the analysis depends on it.

**Basing a synthetic set on a real lost deal.** Useful and risky. Change the industry, the region, the numbers, the names, the headcount and the timeline, keep only the shape of the failure, and have someone who knows the account confirm it is unrecognisable before the file is stored anywhere shared.

**Material shown to a customer or in a public demonstration.** Keep the synthetic label visible on screen, not only in the file. A realistic transcript displayed without a label in front of an audience is a claim about a customer conversation, and someone will screenshot it.

## Quality bar

- A written specification and evidence ledger exist for every deal, before the dialogue.
- Length is inside the band and was counted, not estimated.
- The metadata header is complete, carries the synthetic label, and matches the filename exactly.
- Much is left legitimately unestablished on any single call, and at least one fact stays asserted for the whole set.
- Buyer-stated and seller-supplied urgency are distinguishable in the dialogue without effort.
- Each of the four buyer non-answers appears somewhere in the set.
- Next steps vary in strength across the set, including at least one hollow one.
- The set contains contrast, and at least one deal that does not resolve.
- A four-pass read of the finished transcripts matches the ledger.

## Adapting this to your context

The defaults, five calls per deal, four to five and a half thousand words each, a mid-market US dollar deal and a three-deal portfolio, come from software and services selling with a named seller on every call.

- **Five calls and the stage names.** Discovery, ideation and proposal are a services sequence. A transactional cycle closes in two calls and should be written as two. A tender-led cycle has no discovery call: the set is a briefing, a clarification round and a presentation, and the ledger tracks what the authority put in writing.
- **The price band and the currency.** The band drives what is realistic in dialogue more than the industry does. State figure and currency in the specification, and derive every other number from the two or three real ones fixed there.
- **One seller per deal.** Where your motion runs a seller plus a solutions engineer, put the second person in the cast from call one and make any handoff a visible moment.
- **Word budgets.** Four thousand words is a floor for a thirty to forty minute call in English. Calibrate against two real transcripts before setting it.

- **What not to change.** The specification and the evidence ledger are written before the dialogue, and at least one deal in the set does not resolve.

## Related skills

`sales-call-analysis` is what this material is written for, and its four-pass evidence logic is the specification this skill writes against. `sales-roleplay` covers live rehearsal, which needs a person rather than a transcript. `sales-team-competency-assessment` uses this material where a team needs a common case to be assessed against rather than their own live deals. `content-quality-gate` applies where any of this material will be shown outside the team, including the labelling rule.
