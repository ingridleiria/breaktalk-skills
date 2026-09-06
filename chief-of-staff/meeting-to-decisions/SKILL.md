---
name: meeting-to-decisions
description: Converts meeting notes, transcripts, recording summaries or chat threads into a circulated record that holds: numbered decisions separated from things merely discussed, actions with an owner, a verifiable description and a date, open questions with an expected answerer, a parking lot, and a follow-up message ready to send with a confirmation deadline, plus the entry that goes into the decision log. Use this skill whenever someone pastes notes or a transcript and asks for the summary, minutes, action items, next steps or recap; whenever they ask what was decided, who owns what, or ask for the follow-up to be sent; and whenever a meeting has ended with no written record. Trigger for any meeting content, from a two-person call to a leadership offsite.
---

# Meeting to Decisions

Everyone leaves a meeting believing something was agreed, and no two people believe the same thing. The version that survives is whichever one is repeated most confidently in the following week, which is rarely the one the group actually reached. Three weeks later the topic returns to the agenda, the discussion restarts from a worse position because everyone half-remembers the last one, and the meeting is held again.

The cost is not the repeated hour. It is the commitment nobody remembers making, discovered when the thing it depended on is already late; the decision quietly reversed by a person who was not in the room and had no way to know; and the slow lesson that meetings are where things get talked about rather than settled. A meeting with no written record has to be held again, and organisations that never write records hold every important meeting between two and four times.

Meetings produce two things worth keeping: decisions and commitments. Everything else is context.

## When to use this, and when not to

Use it for any meeting that produced a decision or a commitment, including calls, offsites, review sessions and long chat threads that functioned as a meeting. Use it especially when the input is an automated transcript, where the volume of text hides how little was actually settled.

Do not use it to prepare a decision before a meeting, which is `decision-memo`; that skill produces the one page that goes into the room, and this one captures what came out. Do not use it to decide which meetings exist and what each must produce; that is `operating-cadence-design`, which specifies this record as the required artefact of most recurring moments. Do not use it for the recurring written status that feeds a meeting, which is `weekly-status-update`. Do not use it to synthesise customer or user conversations, where the value is in patterns across many sessions rather than in decisions from one; that is `customer-interview-synthesis`. Do not use it for formal board minutes, which have governance requirements and a different standard of record; that is `board-and-investor-management`.

The boundary: this skill is the artefact a single meeting produces. Which meetings produce it is decided by `operating-cadence-design`, and a decision that needed preparing should have arrived as a `decision-memo`.

## What you need before starting

**The raw input, in full.** Notes, a transcript, a recording summary or a thread. Missing: reconstruct from the attendees within 24 hours, asking each for decisions and their own actions only, which produces a usable record and takes them two minutes each. After a day the reconstruction stops being reliable.

**The attendee list, with roles, and who was absent but has actions.** Missing: infer from the input and mark inferred names, because attributing a decision to the wrong person is the error that most damages a record's credibility.

**What was already decided before this meeting.** Missing: ask, or check the decision log. Without it you will record a restatement of an existing decision as a new one, which makes the log unusable for tracking what actually changed.

**Whether anything discussed is confidential.** Personnel, legal, compensation, an unannounced deal. Missing: assume anything touching a named individual's performance or pay is confidential, keep it out of the circulated record, and ask the meeting owner before including it.

**The channel and the deadline for circulation.** Missing: default to the channel the group already uses and circulate the same day, because a record sent on day three is read as an archive rather than a call to confirm.

## The method

Read the full input before writing anything. Then extract in this order, because the order prevents the most common error, which is promoting discussion to decision.

1. **Extract the decisions.** A decision is a choice between alternatives that was closed in the meeting. Record it as a sentence, with who made or ratified it and the rationale where it was stated. The test: could someone act differently tomorrow because of this. "We should probably move to the new vendor" is not a decision, and recording it as one manufactures a commitment nobody made.

2. **Separate decided from discussed, explicitly.** Where a topic was debated at length and not closed, it belongs under open questions with the reason it did not close. This distinction is the whole value of the record, and it is the thing an automated summary reliably gets wrong, because length of discussion reads as significance.

3. **Extract every action with an owner, a verifiable description and a date.** All three are required. An action missing one is incomplete: fill it from context where that is unambiguous, and otherwise list it under open items with the missing element flagged rather than inventing a date nobody agreed.

4. **Rewrite vague actions as verifiable ones.** "Look into pricing" becomes "send a comparison of the three vendors' list prices to the group". The rule: the action must be checkable by someone other than the owner. This rewriting is where a record becomes useful, and it should be done in the writing rather than referred back, with the rewritten version visible so the owner can correct it.

5. **Record open questions with an expected answerer and a date where one was given.** A question with no name attached will not be answered, and writing "to be discussed" is how a topic reappears on four consecutive agendas.

6. **Record the parking lot.** Topics deliberately deferred, so they are not lost and not mistaken for decisions. The parking lot is what makes it possible to close a discussion in the room without the person who raised it feeling overruled.

7. **Record the few facts others need**, such as a number, a date or a change of plan stated in the meeting. Keep it short. This section is not a summary of the discussion.

8. **Do not transcribe the conversation.** Nobody rereads a narrative of who said what. People read the decisions and search for their own name, and every line of narrative makes that search slower.

9. **Check the decisions against the log** for anything that reverses or modifies an earlier decision, and say so explicitly in the record: "this supersedes the decision of 14 March". A silent reversal is how an organisation loses track of what it believes.

10. **Draft the circulation message in the same pass**, with a two-line opener stating the purpose and the single most important decision, the record itself, and a request that owners confirm or correct their actions by a stated date. Where a messaging or document tool is connected, draft it there for the meeting owner to send; where none is, produce the text ready to paste. The record should be sent by the meeting owner rather than an assistant, because a record sent by the person accountable for the meeting carries the authority to be corrected against.

11. **Append the decisions to the log the same day**, with the date and the source meeting.

## Handling transcripts

Automated transcripts need three specific defences, because their errors are systematic rather than random.

**Speaker attribution is frequently wrong**, particularly in a room with a shared microphone or where people talk over each other. Attribute decisions to the meeting or to a role rather than to an individual unless the attribution is certain. A decision misattributed to the wrong executive is worse than an unattributed one.

**Numbers are mis-transcribed more often than words**, and a wrong number in a record propagates into plans. Flag any figure that carries a decision for verification before circulation, and where it cannot be verified, write it as "approximately, to be confirmed" rather than as a precise figure.

**Length is not significance.** A twenty-minute discussion that resolved nothing produces more transcript than a nine-second decision, and any summarisation that weights by volume will invert the importance. Extract in separate passes for a long transcript, decisions first, then actions, then open questions, rather than reading linearly and summarising as you go.

Where a recording tool produces its own summary, treat it as a first pass rather than a record: usually accurate about topics, unreliable about what was settled.

## Decision log maintenance

Every decision goes into one log, kept where the team already looks: date, the decision, the decider, the reasoning in one line, and a link to the record.

The log answers the two questions that otherwise consume enormous time, which are whether something was decided and why. When a settled question is reopened, the answer is the log entry and a request for what new information has appeared. That distinction matters: a decision should be revisited on new evidence, and should not be revisited because the person who disagreed waited long enough for everyone else to forget.

Where no log exists, propose starting one and seed it with the decisions from this meeting. It is the single highest-value artefact a recurring meeting produces, and it takes about three minutes a week to maintain once it exists.

## Worked example

**Situation.** A leadership offsite at Trellis Freight, a 260-person logistics software company. Eleven attendees, one and a half days, an automated transcript running to about 46,000 words, and a shared notes document that three people had edited concurrently. The chief of staff had to circulate a record by the following morning, before people scattered into a bank holiday week.

**Task.** A record people would act on, circulated within eighteen hours, that distinguished what was actually decided from the considerable amount that was merely discussed with energy.

**Action.** The first pass was a mistake and cost two hours. It followed the agenda and summarised each session in a few paragraphs, which produced a readable three-page document that a colleague, reading it as a check, could not use to answer a simple question: what am I meant to do on Monday. The narrative form had buried four actions inside prose and had given a fifteen-minute unresolved discussion about brand positioning the same visual weight as the pricing decision that was the point of the offsite.

The rewrite extracted in passes. Decisions first, across the whole transcript and the notes together, which produced nine candidates. Three did not survive the test. One was a statement of intent about hiring pace with no choice closed. One was a strong opinion from the chief technology officer that the notes had recorded as an agreement, and which, when checked with him by message that evening, he confirmed he had meant as a position rather than a conclusion. One was a restatement of a decision already in the log from six weeks earlier, and it was recorded as a reaffirmation rather than a new decision so the log would not double-count it.

Six decisions survived. One of them superseded an earlier decision about regional pricing, and the record said so with the earlier date, which turned out to matter three weeks later when a sales leader who had been absent quoted the superseded version to a customer.

Actions produced twenty-three candidates, of which fourteen were complete. Six were missing dates, resolved from the transcript where the group had agreed "before the board meeting" and the board date was known. Three could not be resolved: two had no clear owner because the phrasing was "we should", and one had no verifiable description. All three were listed under open items with the missing element flagged, which produced two corrections within an hour of circulation and was faster than chasing beforehand.

Two transcript numbers were flagged, a churn figure quoted as 4.7 percent that appeared elsewhere as 14.7, and a contract value. Both were checked against source, and one was wrong in the transcript. One item was held out of the circulated record entirely, a discussion about a senior individual's performance, which went to the chief executive as a private note with a single line in the record saying a confidential item had been discussed separately.

**Result.** A record of about 700 words, circulated at 08:40 the next morning with a request to confirm or correct actions by 17:00 that day. Nineteen of twenty-three actions were confirmed by the deadline, two were corrected, and two owners handed their action to someone else, which is precisely the correction the deadline exists to produce. The six decisions went into the log the same morning. The superseded pricing decision was found in the log by the absent sales leader three weeks later, which is the whole argument for keeping one.

### A second scenario, where it goes differently

A weekly leadership meeting of fifty minutes, seven attendees, where the honest answer is that nothing was decided.

The temptation is to manufacture a record so the meeting appears productive: three "decisions" that are restatements of existing positions, and five actions that are continuations of work already underway. That record is worse than none, because it teaches readers that the decisions section contains filler, and once they learn that they stop reading it in the week it matters.

The correct record is short and says so. Decisions: none. Then the open questions that did not close, each with the reason, which is usually that a person was absent, that a number was missing, or that the trade-off was not framed as a choice. That last reason is the useful one, because it is the signal that the topic should arrive next time as a `decision-memo` rather than as a discussion item. A record that names why nothing closed is the most direct route to the next meeting closing something.

What did not change: the same shape, actions still carry owner and date, and the record still goes out the same day.

## Output

Under 300 words for a normal meeting, in this order.

```
[Meeting name]  |  [date]  |  [duration]
Attendees: [names]
Absent, with actions: [names]

DECISIONS
1. [Decision, in one sentence.] Decided by: [name or "the group"].
   Rationale: [one line, if stated.]
   [Where relevant: supersedes the decision of [date].]
2. ...
   [If none: "No decisions were taken. See open questions."]

ACTIONS
| Owner | Action | Due | Status |
| --- | --- | --- | --- |
[Sorted by date. Owner name first so people can find themselves.]

OPEN QUESTIONS
| Question | Who answers | By when | Why it did not close |
| --- | --- | --- | --- |

PARKING LOT
[Topics deliberately deferred, one line each.]

FOR INFORMATION
[The few facts others need: a number, a date, a change. Short.]

NEXT MEETING / CHECKPOINT
[Date, and what will be reviewed.]
```

**The circulation message**, drafted in the same pass and sent by the meeting owner:

```
Subject: [Meeting name], [date]: decisions and actions

[Two lines: what the meeting was for, and the single most important
decision taken.]

[Record pasted or linked.]

Please confirm or correct your actions by [date and time]. Anything
not corrected by then is taken as agreed.
```

## Failure modes

**Discussion promoted to decision.** Recognise it when a decision line contains "should", "probably", or "we agreed to explore". Move it to open questions with the reason it did not close.

**Actions without all three elements.** Recognise it by scanning the table for a blank cell. Fill from context where unambiguous, otherwise flag the gap in the record rather than inventing the missing part.

**Vague actions that cannot be checked.** Recognise it when the description starts with look into, think about, explore, or circle back. Rewrite as a deliverable with a recipient.

**Transcribing the discussion.** Recognise it by length and by the presence of names attached to opinions. Cut to decisions, actions and open questions; the discussion is not the record.

**Wrong speaker attribution from a transcript.** Recognise it when a decision is attributed to someone who would not normally make it. Attribute to the group unless certain.

**Numbers taken from a transcript unchecked.** Recognise it because the figure is oddly precise or oddly round. Verify anything that carries a decision.

**A silent reversal.** Recognise it by checking each decision against the log. Name the superseded decision and its date in the record.

**Confidential content in a circulated record.** Recognise it by scanning for named individuals in any context other than as an action owner. Move it to a private note and leave a placeholder line.

## Edge cases

**No notes and no recording.** Reconstruct within 24 hours by asking each attendee for decisions and their own actions only. Circulate it marked as a reconstruction and ask for corrections, which arrive quickly because people correct their own commitments readily.

**The meeting was a decision meeting and no decision was reached.** Record that plainly, with the reason and what has to be true next time, usually a named absentee, a missing number, or a trade-off nobody framed as a choice. Then propose that the topic returns as a `decision-memo`.

**A decision was made that the group is not authorised to make.** Record it as a recommendation rather than a decision, name who must ratify it and by when, and say so in the circulation message. Recording it as settled creates a commitment that will be reversed publicly.

**Attendees disagree afterwards about what was decided.** Do not adjudicate in the record. Circulate what you have with the disputed item marked as disputed, name the two readings, and ask the meeting owner to settle it. A record that quietly picks a side loses its standing as a record.

**A two-person call.** The same shape, three lines long. Decisions, actions, next checkpoint. The discipline is what makes a small commitment survive, and the format costs almost nothing at this size.

## Quality bar

- Every action has an owner, a description someone else could verify, and a date.
- Nothing appears under decisions that was only discussed, and where nothing was decided the record says so.
- Any decision that supersedes an earlier one names it and its date.
- Numbers carrying a decision were verified against a source, not taken from a transcript.
- The record can be read in one minute and searched by name.
- Confidential content is excluded, with a placeholder noting a private item exists.
- The follow-up is ready to send, with a confirmation deadline and a stated default.
- The decisions are in the log the same day.

## Related skills

`decision-memo` prepares a decision before the meeting and receives the topics this record shows are not closing; both feed the same decision log. `operating-cadence-design` decides which meetings must produce this record and where it lands. `weekly-status-update` supplies the written status that should have removed the round-robin from the meeting, and takes the actions from this record into the following week's tracking. `strategic-plan-and-action-plan` and `okr-planning` are where actions belonging to a bet or a key result should be carried rather than living only in a meeting record. `customer-interview-synthesis` handles conversations whose value is in patterns across sessions rather than decisions from one.
