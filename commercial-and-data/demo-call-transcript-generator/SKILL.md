---
name: demo-call-transcript-generator
description: Generates realistic synthetic sales call transcripts for demonstrating, training, or testing a call analysis system: a full cast defined before writing, a metadata header that makes a deal history trackable, a length band that produces a genuine thirty to forty minute call, deliberately partial evidence so scores start low and move, and portfolio patterns that give a set of deals real contrast rather than three versions of the same story. Use this skill when the user needs demo or test call data, sample transcripts, training material for coaching, or a worked deal history to show a scoring tool against.
---

# Demo Call Transcript Generator

Synthetic transcripts fail in two directions. Too polished, and every dimension scores green on the first call, which demonstrates nothing and quietly teaches the wrong standard. Too thin, and the dialogue reads as a script rather than a conversation. The fix is to design the deal before writing the dialogue, and to treat missing evidence as correct rather than as a gap to fill.

Pairs with `sales-call-analysis`, which is what these transcripts are usually generated to be scored by.

## Hard requirements

**Length.** Thirty to forty minutes, roughly four thousand to five and a half thousand words. That is a floor, not a ceiling to undershoot. Allocate the word budget across the call rather than padding one section: an opening and rapport, an agenda, the substance in two or three movements, and a close. Check the finished length rather than assuming it.

**One owner per deal.** The same seller runs every call on an opportunity for its whole life. Swap them only for an explicit handoff scenario, and if so make the handoff a visible moment in the dialogue rather than a silent change of name.

**Stage range.** Discovery, ideation, and proposal by default, weighted toward the first two. In a portfolio, one deal may run through negotiation to show a fuller cycle, but not all of them, or the contrast disappears.

**Minimum four calls per deal.** Three does not leave room to show real movement. A reliable default is two discovery calls, two ideation calls, and one proposal call, plus a negotiation call for whichever deal runs the longer arc.

**Partial evidence is correct.** A single good call should leave several scoring dimensions untouched or low. Keep the distinction alive in the dialogue between a buyer politely agreeing with urgency the seller stated and a buyer stating their own reason to change now. The first is not evidence, and writing it as though it were is the most common way a synthetic transcript becomes useless.

**No fabricated links.** Never invent a recording URL or a clickable-looking placeholder. Every transcript does carry a plain metadata header: seller with title and company, account, buyers with titles and roles, attendees for this specific call, date, and stage. That header is what makes a deal history readable by a person or a script without opening the dialogue, and the seller name and date in it match the filename exactly.

**Score bands, so an outcome means something.** On a hundred-point deal health index with eight dimensions worth twelve and a half points at green and half that at amber: below thirty-four is red, thirty-four to seventy is amber, above seventy is green. A deal described as ending amber lands inside that band rather than at seventy-one, and a deal described as reaching green clears seventy rather than stopping at fifty.

## Portfolio patterns

Build contrast rather than three copies of one story.

- **The advancing deal.** Starts red, moves cleanly through amber to green, reaches proposal or negotiation, ends above seventy. The coach dimension usually turns green first and stays there, because proactive buyer behaviour is what unlocks the rest.
- **The stalled deal that recovers.** Flat for two or three calls against a real obstacle such as a passive contact or a budget freeze, then a specific named turning point: a new stakeholder stepping up, a blocker lifting. The turn is a moment in the dialogue, not a vague improvement.
- **The honest early deal.** Cautious, stops at discovery or ideation, ends amber, never forced to green. This is the one that shows a patient sales motion, and a set without it teaches that every deal resolves.

## Workflow

Define the cast before writing a word: the seller with title, the account, the primary buyer-side contact and whether they are written as someone who acts or someone who only talks, and the secondary stakeholders who appear later. Fix the stage, which determines what is realistic to include. Write the header. Write the dialogue with interruptions, unfinished sentences, and at least one place where the seller asks a weak question and pays for it. Check the length. Then read it once as the scoring skill would, and confirm the evidence present matches the outcome intended.

## Quality bar

- Length inside the band, checked rather than assumed.
- Metadata header complete, and matching the filename.
- Several dimensions legitimately unevidenced on any single call.
- Buyer-stated and seller-stated urgency clearly distinguishable in the dialogue.
- A portfolio contains contrast, and at least one deal that does not resolve.
