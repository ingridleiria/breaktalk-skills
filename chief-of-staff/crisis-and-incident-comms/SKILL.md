---
name: crisis-and-incident-comms
description: Runs stakeholder communication during and after a crisis or incident so that every audience hears one version of the facts, in the right order, on a promised rhythm. Produces a timestamped facts sheet separating confirmed from suspected, a named role list with a single spokesperson, a stakeholder sequence justified by harm and obligation, holding statements that promise a time rather than a resolution, an update cadence that is kept, a communications log that serves as the audit trail, and the resolution message and post-incident review. Use this skill the moment something has gone wrong and people have to be told: an outage, a security breach, data loss, a product failure, a safety issue, a sudden senior departure, a negative story, legal action, or a financial shock. Trigger on phrases such as we have an incident, what do we tell customers, the story is out, we are down, customers are asking, how do we handle this, and also for preparedness work before anything has happened.
---

# Crisis and Incident Communications

In the first hours of an incident, silence is not neutral. It is read as concealment by the people who are affected and as incompetence by everyone else, and both readings are worse than almost any set of facts. The organisations that come out of incidents with their relationships intact are rarely the ones that had the smallest problem. They are the ones whose customers could always say what was known, what was being done, and when they would hear next.

The specific failure this skill prevents is the divergent account. Under pressure, four people answer four channels: an account manager reassures a customer, a support agent gives a different cause, someone posts a status page update written from a stale ticket, and an executive tells the board a version that is a day old. Each is defensible alone. Together they are the discovery that ends trust, because a customer who receives two incompatible explanations concludes, correctly, that nobody in the organisation knows what happened, and that inference persists long after the incident is closed. The second failure is the promise not kept: an update pledged for 16:00 that arrives at 19:00 teaches every recipient that the next promise is worthless, and from then on they escalate rather than wait.

Both are process failures rather than writing failures, and both are prevented by a single timestamped source of facts and one named person who owns everything that goes out.

## When to use this, and when not to

Use it the moment there is a live incident with an external or internal audience: a service outage, a security or data incident, a product defect reaching customers, a safety event, a supplier failure that affects delivery, a sudden departure that customers will notice, a press story, litigation becoming public, or a financial event that must be disclosed. Use it also for preparedness, which is the same content written when nobody is under pressure and is worth more than any amount of improvisation later.

Do not use it for the technical or legal response itself. This skill covers who is told what, when, by whom. The incident response, the forensic investigation, the remediation and the legal strategy are owned elsewhere, and communications takes facts from those owners rather than generating them.

Do not use it for a planned announcement of bad news that is not an incident, such as a reorganisation, a price rise or a discontinued product. Those are `ceo-communications`, where the sequencing is chosen rather than forced and there is time to calibrate voice.

Do not use it for the decision about what to do. Where the incident forces a choice with real options, such as whether to take a system offline or whether to offer credits, that is a `decision-memo` compressed to a page, and it runs alongside rather than inside the communication.

## What you need before starting

**A single incident lead and a single communications lead, named.** Not a group. The communications lead owns every outbound message without exception, including the one an executive wants to send personally. Missing: name yourself provisionally in writing, tell the senior person present, and proceed. An unnamed owner in hour one produces the divergent account by hour three.

**The facts as currently known, timestamped, with confirmed separated from suspected.** This is the source every message is built from. Missing: write down what is known even if it is three lines, mark everything else as unknown, and put a time on it. A thin facts sheet is workable; an absent one is how the wrong cause gets published.

**The blast radius, in numbers where possible.** Who is affected, how many, since when, and whether the effect is continuing. Missing: state the bound you can defend, such as "at most the 340 accounts on the affected cluster", and say it is an upper bound. Never guess downward; a revised-upward number reads as a second incident.

**The regulatory and contractual notification clock.** Many data and safety regimes impose fixed windows measured in hours. Large customer contracts often impose their own, shorter. Missing: ask legal within the first thirty minutes and ask the commercial owner for the notification clauses in the largest contracts. This is the one input that cannot be recovered by working harder later.

**The channels and who can actually publish to each.** Status page, in-product banner, support macros, the email system, the social accounts. Missing: find out now. Discovering mid-incident that only one person, on holiday, can update the status page is a recurring and entirely avoidable failure.

**The stakeholder list with contact routes.** Affected customers and how to reach them, staff, board and investors, partners, regulators, press contacts. Missing: build the top three tiers from the customer system and the leadership list and accept it is incomplete, noting which tier is uncertain.

**The approval path, short.** Who reviews before a message goes, and their deputy. Missing: set it at one reviewer plus legal for anything touching cause, liability or personal data, and say so. An approval path with four names guarantees a missed update time.

## The method

### The first hour

1. **Write the facts sheet and put a timestamp on it.** What happened, when it was detected, how it was detected, who is affected and how many, what is being done, and when the next update comes. Two columns: confirmed and suspected. The judgement call is what counts as confirmed; the rule is that a fact is confirmed when a named person will put their name to it, and everything else is suspected no matter how confident the room feels. Every later message is built from a version of this sheet, and the sheet is versioned rather than overwritten.

2. **Name the roles out loud and in writing.** Incident lead, communications lead, decision-maker, legal contact, and one spokesperson. Nobody else speaks externally, and that instruction goes to staff in the same hour. Where an executive objects to routing their message through the communications lead, the concession is speed of review, never an exception.

3. **Sequence the stakeholders by harm, then obligation, then exposure.** Anyone who can reduce their own harm by acting hears first, which is the rule that overrides every other consideration including legal caution about admitting cause. Then anyone under a statutory or contractual clock. Then the people who will be asked: front-line staff, support, account managers, who need lines to take before their phones ring. Then the board and investors, who must not learn from a customer. Then the wider organisation. Then partners. Then press and the public where relevant. Regulators sit wherever their clock puts them, which is often earlier than instinct suggests.

4. **Issue the holding statement.** It says what is known, what is being done, and when the next update will come. It does not promise a resolution, a cause or a time to fix. The judgement call is how early to send when the facts are thin; the rule is that a holding statement with three true sentences beats a complete statement two hours later, because the first hour of silence is what gets remembered.

### Through the incident

5. **Run war-room check-ins on a fixed interval.** Hourly at first, then lengthening as the situation stabilises. Each check-in produces one output: an updated, re-timestamped facts sheet. Messages are drafted from that version, never from what someone said in the meeting.

6. **Keep every promised update time, including when there is nothing to report.** "No change since 14:00, next update 18:00" is a complete and valuable update. The rule that makes this work: never promise an interval you cannot keep at three in the morning. A four-hour cadence held for two days is worth more than an hourly cadence abandoned after five updates.

7. **Adapt per audience in emphasis, never in substance.** One version of the facts, differently weighted. The specific thing to check before each send: could two recipients on different channels compare their messages and find a contradiction. If yes, one of them is wrong.

8. **Maintain the communications log as messages go, not afterwards.** Every message, to whom, when, by whom, through what channel, and which version of the facts sheet it carried. This is the audit trail a regulator or a customer's security team will ask for, and it is the only reliable input to the review. Reconstructed logs are wrong in exactly the places that matter.

9. **Correct errors fast and visibly.** Where something published turns out to be wrong, the correction goes to everyone who received the original, says plainly what was wrong, and does not bury the change. An organisation that corrects itself quickly is trusted more than one that was never caught, and far more than one that quietly edits a status page.

### After

10. **Send the resolution message to every audience that received an incident message.** What happened, including the cause where it is confirmed. What was affected, with the final numbers. What was done. What changes to prevent recurrence, stated as commitments with dates rather than intentions. Any remedy: credits, remediation steps, support. Where the cause is not yet confirmed, say the incident is resolved and the cause investigation is open, and give the date for that.

11. **Run the post-incident review within two weeks.** Timeline, cause, what worked and what did not in the communication specifically, the gaps in the plan, and the changes made with owners and dates. Blameless in tone and specific in findings. The rule for what makes it real: at least one change to the preparedness plan, made and dated, or the review did not happen.

12. **Update the preparedness plan the same week.** Whatever was improvised becomes a template. Whatever was slow gets a named deputy.

## Preparedness, written before anything happens

A one-page plan, current, reachable without corporate network access, because some incidents remove access to the systems the plan lives in.

It holds the roles with deputies and mobile numbers; the stakeholder sequence; holding statement templates by incident type, each three sentences long; the approval path with its deputy; the channels and every person who can publish to each; the notification requirements by jurisdiction and by major contract with the clock length stated; and a quarterly tabletop exercise on a scenario nobody has seen before.

The plan is what allows the first hour to take an hour. Without it, the first hour takes four, and the four hours are entirely spent on questions with known answers.

## Worked example

**Situation.** A payments infrastructure company, roughly 400 staff, serving 1,900 business customers. At 03:12 on a Tuesday, a database migration failed and 610 customers could not process transactions. Detection was automatic at 03:14; the on-call engineer paged the incident lead at 03:21. By 04:00 the cause was suspected to be a schema change but not confirmed, and there was a second, more serious open question: whether any transaction data had been written incorrectly rather than merely failing. That question would not be answerable for several hours.

**Task.** Communicate through an outage of unknown length, with an unresolved data-integrity question, without either understating a possible data problem or announcing one that did not exist. Three of the affected customers had contractual notification clauses of two hours.

**Action.** The facts sheet was opened at 03:40 with four confirmed lines and six suspected. Roles were named at 03:45. The communications lead was the chief of staff, on the reasoning that the head of support needed to run support rather than approve messages.

The first holding statement went to the status page and to all 610 affected customers at 04:05: transactions failing since 03:12, cause under investigation, engineering engaged, next update 05:00. Fifty-three minutes from detection, which the review later judged twenty minutes slower than it should have been.

The wrong turn happened at 04:30. A draft customer update prepared by a well-meaning account director stated that no customer data had been affected. It was intercepted before sending. At that point nobody knew whether data had been affected; the honest position was that failed transactions had not been written, which was confirmed, and that a check for partial writes was running, which was not yet complete. The distinction is small in engineering terms and enormous in communication terms, because "no data was affected" said at 04:30 and retracted at 09:00 would have been the story rather than the outage. The 05:00 update instead said: no failed transaction has been recorded as successful, we are running a full integrity check on the affected window and will report its result by 09:00 whatever it shows. That sentence, promising to report a result before knowing what it would be, was what the customer security teams later cited as the reason they trusted subsequent messages.

The three contractual notifications went at 04:40, inside the two-hour clock, using the same facts with the contractual reference added. Staff were briefed at 05:30 with a lines-to-take sheet before support opened at 07:00. The board chair was called at 06:15 and the board emailed at 06:30. No press statement was issued, because no press enquiry came; a statement was drafted and held.

Updates went at 05:00, 07:00, 09:00, 13:00 and 17:00, all on time. The 09:00 update reported the integrity check clean across 610 accounts. Service was restored at 11:40 and confirmed stable at 13:00.

**Result.** The resolution message went at 17:00 on the same day with the confirmed cause, the final numbers, four named remediation commitments with dates, and a fee credit for the affected window offered without customers having to ask. Two customers escalated during the incident, both in the first two hours before the cadence had established. None cancelled.

The post-incident review, held nine days later, produced three communications changes: the status page publisher list went from two people to five, the holding statement template acquired a standing line about integrity checks for any data-adjacent incident, and the detection-to-first-message target was written down as thirty minutes with the 04:05 timing recorded as the reason.

The honest uncertainty: it is not knowable whether the careful handling of the integrity question preserved the relationships or whether a clean check result would have done that anyway. What is knowable is that the alternative message was drafted, and would have been wrong.

### A second scenario, where it goes differently

A twelve-person professional services firm discovers that a departing employee copied a client file to a personal account. Nothing is down, nobody is inconvenienced, and there is no status page.

The method changes shape in three ways. The sequence collapses to almost nothing, because there is one affected client and the right first action is a phone call from the firm's principal within the hour, not a written statement. The written record still matters and is created afterwards, but the medium is a conversation, and a written notification arriving first would be the wrong choice.

The regulatory clock, however, becomes the dominant constraint rather than a background one. A personal-data incident in most regimes starts a fixed notification window from the point of awareness, and awareness is a defined moment that has just occurred. The communications lead's first act is to establish, with legal, whether the clock has started and when it expires, before drafting anything.

And the spokesperson rule inverts. In a large incident the rule exists to stop many people speaking. Here there is only one person who will speak, and the risk is the opposite: that the principal, embarrassed, delays the call and speaks too late. The discipline that matters is the deadline rather than the channel.

What stays constant: a timestamped facts sheet separating what is known from what is assumed, one version of the account, a promised next contact that is kept, and a written log. Those four hold at every size.

## Output

**Facts sheet**, versioned and timestamped:

```
INCIDENT [name]        Facts sheet v[n]        [date, time, timezone]

CONFIRMED
  What happened        [one line]
  Detected             [time, and how]
  Affected             [who, how many, since when, still ongoing? yes/no]
  Action in progress   [one line per workstream, with owner]

SUSPECTED, NOT CONFIRMED
  [item, and what would confirm or rule it out, and by when]

UNKNOWN AND BEING ESTABLISHED
  [question, owner, expected answer time]

NEXT UPDATE            [time]     Owner of this sheet: [name]
```

**Stakeholder sequence:**

| Order | Audience | Why this position | Channel | By whom | By when | Sent |
| 1 | Affected customers, 610 | Can pause their own processing | Email plus status page | Comms lead | 04:05 | yes |
| 2 | Three contract-clock customers | Two-hour contractual clause | Direct, named contact | Account directors | 05:12 | yes |
| 3 | Support and account teams | Will be asked from 07:00 | Internal channel plus lines sheet | Comms lead | 05:30 | yes |

**Holding statement**, three sentences:

```
[What is happening, and since when.]
[What we are doing.]
[When the next update will come: a specific time.]
```

**Communications log:**

| Time sent | Audience | Channel | Sent by | Facts sheet version | Approved by |

**Resolution message**, and the **post-incident review** with its timeline, cause, communication findings, and the changes made with owners and dates.

## Failure modes

**Four people answering four channels.** Recognise it when a customer quotes back an explanation nobody in the war room recognises. Fix immediately by instructing all staff that responses come from the lines sheet only, and by sending a corrected single account to everyone who may have received a variant.

**Speculating on cause because the room is confident.** Recognise it by the word "likely" appearing in an outbound draft. Confidence in an engineering discussion is not confirmation. Fix by moving the statement to the suspected column and publishing only what a named person will attest to.

**The missed update time.** Recognise it at the moment it happens, and treat it as an incident within the incident. Send immediately with an apology of one clause, and lengthen the promised interval rather than repeating the miss.

**The reassurance that outruns the evidence.** Recognise it in any absolute negative: no data was affected, no customers were impacted, nothing was accessed. These are the sentences most often retracted. Fix by stating the specific thing that has been checked and the check still running, with a time for its result.

**Apology written by committee into meaninglessness.** Recognise it when the sentence contains "any inconvenience" and no subject. Legal properly reviews language touching liability, but "we are sorry this happened and that it disrupted your work" is almost always both safe and correct. Fix by proposing that exact form.

**Blame in an outbound message.** Recognise it when a vendor, an individual or a customer's configuration is named as the cause. Do not do it, even when it is true. Cause attribution goes in the review, described as a system, not in a message, described as a party.

**The log written afterwards.** Recognise it because the times are round numbers. A reconstructed log is unreliable exactly where a regulator will look. Fix by assigning the log to a named person in the first hour whose only job it is.

**The board learning from a customer.** Recognise it from an inbound message from a director asking what is going on. Fix the sequence, and call the chair rather than emailing.

## Edge cases

**The facts are contested inside the organisation.** Publish only what is agreed, name the disagreement as an open question with an owner and a time, and do not let the internal argument delay the holding statement.

**Legal advises saying nothing at all.** Distinguish two things: the cause and the liability, on which legal governs, and the operational facts and the next update time, on which they usually do not. Almost always a statement can be issued that contains no admission and still tells people what is happening and when they will hear next. Where legal genuinely blocks everything, escalate to the decision-maker, because total silence is itself a decision with consequences.

**An individual is at the centre of the incident.** Never name them, internally or externally, and remove identifying detail that would make them identifiable by inference to a small team. Employment and privacy obligations run alongside the communication.

**A statutory clock is close to expiring and the facts are incomplete.** Notify inside the clock with what is known, marked as preliminary, and supplement. Late notification with better facts is a breach; early notification with partial facts is normally the intended behaviour of the regime.

**The story appears publicly before internal communication is ready.** Move immediately to the shortest true statement, publish to all audiences simultaneously rather than in sequence, and accept that the sequence is gone. Continuing a broken sequence is worse than abandoning it.

**A very long-running incident, measured in days.** Lengthen the cadence deliberately and announce the change: "updates will now be daily at 09:00 until resolved". An unannounced lengthening reads as abandonment. Rotate the communications lead with a written handover of the facts sheet, because fatigue produces the contradictions this method exists to prevent.

## Quality bar

- A timestamped facts sheet exists, separates confirmed from suspected, and every outbound message names the version it was built from.
- One named spokesperson, and no message went out that the communications lead did not see.
- Anyone able to reduce their own harm by acting was told first, and every statutory or contractual clock was met with the time recorded.
- Staff had lines to take before the first customer called them.
- Every message promised a specific next update time, and every promised time was met.
- No absolute reassurance was published that was not the result of a completed check.
- The communications log was written as messages went, and is complete enough to hand to a regulator.
- The review happened within two weeks and produced at least one dated change to the preparedness plan.

## Related skills

`ceo-communications` writes the reflective message from the leader that follows a resolved incident, and handles planned bad news that is not an incident. `decision-memo` is the one-page form for a real choice forced by the incident, such as whether to take a system offline or what remedy to offer. `meeting-to-decisions` captures what the war room actually decided so the facts sheet and the log stay consistent with it. `process-documentation-sop` turns the preparedness plan into a maintained runbook with named owners and deputies. `board-and-investor-management` and `investor-update` carry the incident and its consequences to the board on their own cadence. `executive-briefing` prepares the spokesperson for a hostile interview where one is unavoidable. `program-management` runs the remediation commitments made in the resolution message, which are the promises most often quietly dropped.
