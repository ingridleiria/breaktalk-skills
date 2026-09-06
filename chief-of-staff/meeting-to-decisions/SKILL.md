---
name: meeting-to-decisions
description: Converts meeting notes, transcripts, recordings summaries, or chat threads into a circulated record of decisions, owners, actions with dates, open questions, and parking-lot items, then drafts the follow-up message. Use this skill whenever the user pastes notes or a transcript and asks for the summary, minutes, action items, next steps, or recap; whenever they say "what did we decide", "turn this into next steps", "send the follow-up from the meeting", "who owns what"; and whenever a meeting has ended without a written record. Trigger for any meeting content, from a two-person call to a leadership offsite.
---

# Meeting to Decisions

Meetings produce two things worth keeping: decisions and commitments. Everything else is context. A meeting with no written decisions gets held again. This skill extracts the record, writes it in a form people will act on, and gets it circulated within the day.

## Extraction method

Read the full input before writing anything, then extract in this order:

1. **Decisions made**: a decision is a choice between alternatives that was closed in the meeting. Record the decision as a sentence, who made or ratified it, and the rationale if stated. Distinguish decided from discussed: "we should probably" is not a decision, and recording it as one creates a fake commitment.
2. **Actions**: every commitment to do something, with owner, the specific action, and the date. An action missing any of the three is incomplete; fill it from context if unambiguous, otherwise list it under open items with the missing element flagged. Rewrite vague actions as verifiable ones: "look into pricing" becomes "send a pricing comparison of the three vendors".
3. **Open questions**: things raised and not resolved, each with who is expected to answer and by when if stated.
4. **Parking lot**: topics deliberately deferred, so they are not lost and not mistaken for decisions.
5. **Information shared**: the few facts stated in the meeting that others need (a number, a date, a change). Short.

Do not transcribe the discussion. Nobody rereads a narrative of who said what; they read the decisions and search for their name.

## The record

Format, in this order, under 300 words for a normal meeting:

- Meeting name, date, attendees (and absentees who have actions).
- **Decisions**: numbered list.
- **Actions**: table with owner, action, date, sorted by date.
- **Open questions**: with expected answerer.
- **Parking lot**.
- **Next meeting** or checkpoint, if set.

Actions are the searchable heart of the record; people scan for their own name. Make owners' names bold or lead each line with the name.

## Handling transcripts

- Speaker attribution can be wrong in automated transcripts. Attribute decisions to roles or the meeting as a whole unless the attribution is certain.
- Numbers in transcripts are frequently mis-transcribed. Flag any number that carries a decision for verification.
- Long transcripts: extract in passes (decisions first, then actions, then questions) rather than summarizing linearly.
- Sensitive content (personnel, legal, compensation) discussed in the meeting is recorded only if the user confirms it belongs in the circulated version; otherwise it goes in a private note to the meeting owner.

## The follow-up message

Draft the circulation message in the same turn: a two-line opener stating the purpose and the one most important decision, the record pasted or attached, and a request that owners confirm or correct their actions by a date. Match the channel (email, Slack, or a shared document) and keep the tone plain. Use the environment's message drafting tool when one is available.

## Decision log maintenance

If the user keeps a running decision log, append the meeting's decisions to it with the date and source meeting. If no log exists, propose starting one; the decision log is the artifact that stops decisions being relitigated.

## Quality bar

- Every action has an owner, a verifiable description, and a date.
- Nothing appears under decisions that was only discussed.
- The record can be read in one minute and searched by name.
- The follow-up is ready to send, with a confirmation deadline.
