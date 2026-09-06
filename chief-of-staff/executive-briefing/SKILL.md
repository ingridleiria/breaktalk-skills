---
name: executive-briefing
description: Produces one-page briefs for an executive walking into a meeting, call, negotiation, or trip with limited context, covering who is in the room, what is at stake, what has already been said, the positions to take, and the traps to avoid. Use this skill whenever the user asks to brief the CEO or a leader, prepare talking points for a call, write a pre-read, prepare someone for a meeting they are joining cold, or says "prep me for", "what do I need to know before", "brief for tomorrow", "one-pager for the board chair call". Trigger for any request to compress a situation into what a busy decision maker needs in two minutes, and always before external meetings, investor calls, and partner negotiations.
---

# Executive Briefing

A briefing succeeds when the executive can walk into the room having read only the first paragraph, and nothing in the meeting surprises them. Everything in the document serves that test. It is written to be read in two minutes, standing up, on a phone.

## Inputs to gather first

- The meeting: who requested it, when, format, duration, and what the other side expects to leave with.
- The attendees on both sides, by name and role, and who actually decides.
- Relationship history: prior meetings, emails, commitments made on either side, open threads. Pull from connected CRM, email, or calendar tools when available; otherwise ask the user and mark what is unverified.
- The user's objective for the meeting, in one sentence. If the user cannot state it, propose one and confirm.
- External context on the other party, using the external-insights skill in this library when research is needed.

Never brief from assumptions about the other party. A wrong fact in a briefing costs more than a gap, because the executive will repeat it.

## The one-page structure

1. **Headline** (two sentences): the purpose of the meeting and the single outcome we want. "Partnership call with X; goal is agreement in principle on a pilot before their Q4 budget closes."
2. **Where things stand** (three to five lines): the state of the relationship or deal, the last interaction and its outcome, any open commitments with dates and owners. Dated facts only.
3. **The room**: each attendee with role, what they care about, their likely position, and one relevant fact (recent move, stated priority, known concern). One line each.
4. **What we want and what they want**: two short columns. The overlap is the deal; the gap is the negotiation.
5. **Positions to take**: the three points to make, in order, each with the evidence behind it in one line. If numbers will be discussed, the numbers are here, exact, sourced.
6. **Questions to ask**: three to five that advance the objective or surface what the research could not.
7. **Do not**: the sensitive topics, the commitment not to make, the number not to reveal, the name not to raise. One to three lines. This section is often the most valuable one.
8. **Next step we will propose**: one action, one date, one owner, so the meeting ends with momentum.

Appendix if needed: fuller background, source list, prior correspondence excerpts. The page itself stays at one page.

## Writing rules

- Lead every section with the conclusion. Background follows only if it changes what the executive should say.
- Names, numbers, dates. No adjectives about people ("very sharp", "difficult"); describe behavior and stated positions instead.
- Verified facts and inferences are visibly different: "stated on their Q2 call" versus "likely, based on their hiring pattern".
- Short lines. Bullet form is correct here, because the reader is scanning, not reading.
- Sensitive content stays factual and professional; never speculate about a person's motives or private circumstances.

## Variants

- **Pre-call brief** (default): the structure above, one page.
- **Trip brief**: one page per meeting, plus a cover page with the trip objective, the sequence of meetings, and logistics that affect the conversations (time zones, who travels with whom).
- **Standing brief** for a recurring relationship: sections 2, 3, and 4 maintained and updated after each interaction, with a change log at the bottom.

## Quality bar

- The executive could speak from the headline and section 5 alone.
- Every fact about the other party carries a source or an explicit "unverified".
- The "do not" section exists and is specific.
- The page ends with the next step we intend to propose.
