---
name: weekly-status-update
description: Produces recurring written status that reports exceptions rather than activity: a three-line update per workstream stating done as outcomes, next as checkable commitments, and blocked with the person who can unblock it, consolidated into a leadership rollup whose first two sections tell the reader exactly where to intervene, with an honest status word, metrics from a named source in a fixed order, and the same shape every week. Use this skill for a weekly or fortnightly update, a team status, a project status report, a Friday summary, a leadership rollup, or when someone pastes several people's raw updates and asks for one consolidated version, asks what their update should say, asks for the status for the chief executive, or says nobody reads the weekly.
---

# Weekly Status Update

A status update has one reader and one job: to let the person deciding where to intervene decide faster. Most updates make that harder rather than easier, because they report activity. Eleven paragraphs describing what teams worked on give the reader no way to tell which of the eleven is in trouble, so the reader either reads everything and learns nothing actionable, or stops reading and starts asking people directly. The second outcome is the expensive one, because it recreates the meeting the update was supposed to replace, and now the company pays for both.

The second failure is quieter and worse. A workstream reports on track for five consecutive weeks and then slips by a month, which means the earlier reports were false, which teaches the reader to discount every status word in the document, including the accurate ones. Once that discount is applied, the update has negative value: it consumes an hour a week to write and the reader still has to check. Honest amber is the most valuable thing in the artefact.

## When to use this, and when not to

Use it for any recurring written status, weekly, fortnightly or monthly; for consolidating many contributors into one rollup; for repairing an update nobody reads; and for the first update from a new team or a new leader, where the shape set in week one is the shape that persists.

Do not use it for the record of a single meeting, which is `meeting-to-decisions`. Do not use it to decide which updates should exist, who receives them and where they land; that is `operating-cadence-design`, which specifies this artefact as an output of the weekly rhythm. Do not use it to set the goals being reported against, which is `okr-planning`. Do not use it for an external audience: an investor or board update is `investor-update` and `board-and-investor-management`, and it needs framing and narrative this format deliberately strips out. Do not use it as a project plan; the milestone dates it reports against come from `strategic-plan-and-action-plan` or `program-management`.

The boundary: this skill is the routine artefact of the weekly rhythm. The rhythm itself is designed elsewhere, and the decisions this update surfaces get recorded by `meeting-to-decisions`.

## What you need before starting

**The workstream list with one named owner each.** Missing: build it from the plan or the goal set, and publish it with the first update. Anything not on the list will not be reported, and its absence will not be noticed.

**The metrics, in a fixed order, each with a named source system.** Missing: choose five to eight, name the source for each, and say in the update that they are provisional until the sources are confirmed. Never take a metric from last week's update; errors propagate and become permanent.

**Last week's update.** It is the only way to detect a repeated commitment, a risk that was raised and never closed, and a status that has been green too long. Missing: say that this is week one of the format and start the comparison next week.

**The milestone calendar for the coming fortnight.** Missing: ask each owner for their next dated milestone. A milestone that passes unmentioned is the most common thing an update fails to catch.

**Who the reader is and what they can act on.** A chief executive, a functional leader and a programme sponsor need different exception thresholds. Missing: write for the most senior reader and keep the detail in the appendix, where the others will find it.

## The method

Two layers. The workstream update is written by each owner; the rollup is written by whoever holds the portfolio.

1. **Collect the three lines per workstream.** Done: what completed this week, stated as an outcome. Next: what will be done by next week, specific enough that its completion can be checked by someone else. Blocked or at risk: the blocker, who can remove it, and since when, or the risk to a date or a metric with the recovery plan. Where there is nothing, write "none" rather than leaving it empty, because an empty line reads as forgotten.

2. **Rewrite activity as outcomes.** "Worked on the contract" becomes "contract signed" or, if it is not signed, "contract in legal review since Tuesday, expected Friday". The rule: a done line must describe a state of the world, not an expenditure of effort. Do this rewriting for the owners rather than sending it back, and show them the rewrite, because they learn the distinction from seeing their own sentence changed.

3. **Take the status word and test it.** On track, at risk, or blocked. The test is a single question to the owner: what is the date, and would you bet on it. A workstream carrying a milestone due in nine days with three weeks of work left is at risk regardless of how confident the owner sounds.

4. **Read what the owners did not say.** This is where most of the value is added and it takes ten minutes. Look for a workstream with no update at all, a milestone due this week that nobody mentioned, a "next" line that repeats last week's "next", a risk raised two weeks ago that has silently disappeared, and a metric that moved materially without comment. Each of these goes into the rollup as an exception with the observation attached, not as an accusation.

5. **Verify every number against its source, never against last week's update.** Where a source is unavailable, mark the figure as unverified in the update rather than carrying forward.

6. **Sort the exceptions into two buckets: needs a decision, and at risk or blocked.** The distinction matters because they require different actions from the reader. A decision item names the decision, who must make it, by when, and the cost of waiting. A blocked item names the blocker, who can remove it, and how long it has been blocked.

7. **Write the headline last, after the exceptions are visible.** Two sentences: the condition of the portfolio this week, and the one thing the reader must act on. If nothing needs action, say so explicitly, because a headline that manufactures urgency in a quiet week destroys the signal for the week that needs it.

8. **Assemble in fixed order and keep it under 400 words above the appendix.** Longer than that means activity has crept back in.

9. **Close what has closed.** A risk stated last week and resolved this week is named and closed explicitly. Without that line the reader keeps tracking it privately, and the update accumulates invisible open items.

10. **Send at the same time every week**, into the channel the reader already uses. An update that arrives at variable times gets read at variable times, which usually means Monday, which is a working day late.

## Two layers, and what each one is for

The **workstream update** is the owner's honest account of their own condition, and it is deliberately short so that writing it costs ten minutes rather than an hour. Three lines and a status word. Its audience is the person consolidating, not the chief executive.

The **rollup** is a different document with a different purpose: it is an intervention aid. Its first two sections carry everything the reader must act on, and everything else is context that a reader can skip in a busy week without missing anything that required them. The full workstream table sits at the bottom, unchanged from what the owners wrote, so that the reader who wants detail can find it and so that the consolidation can be audited against the source.

Where a project tracker, a shared document or a messaging tool is connected, collect the workstream updates through it on a fixed deadline and assemble from there. Where none is available, a single message thread with a stated cutoff works, and the cutoff matters more than the tool: updates arriving after the rollup is written are not in the rollup, and saying so once is usually enough to fix the behaviour.

## Writing rules

Past tense for done, future for next, present for blocked. Names for owners and dates for anything due, never "soon", "shortly" or "in the coming weeks". No adjectives about progress: "great week" and "solid momentum" tell the reader nothing and the outcomes carry the tone by themselves. Keep workstreams and metrics in the same order every week, so the reader can find any item by position rather than by reading. Numbers get their source named on first use in any given week.

## Worked example

**Situation.** Corvus Data, 220 people, fourteen workstreams reporting into a Monday leadership meeting. The chief executive had stopped reading the weekly rollup, which ran to about 1,900 words, and had started asking three or four leaders directly on Thursday evenings, which meant those leaders prepared twice and the other ten workstreams went unexamined.

**Task.** A rollup the chief executive would read in three minutes and act from, in the same shape every week, starting the following Monday.

**Action.** The first rewrite was organised by team, one section each, with the three lines under each heading. It was abandoned after one week. The chief executive's response was that it was shorter but she still had to read all fourteen sections to find the two that mattered, which is exactly the problem the original had. Organising by owner is comfortable for the writer and useless for the reader.

The second version inverted it. Sections one and two carried only the exceptions: what needs a decision, and what is at risk or blocked. The fourteen workstreams appeared once, in a table, at the bottom. Everything a reader had to act on was in the first 120 words.

Reading what the owners had not said produced three findings in the first week. One workstream, a data migration, had written "on track" for six consecutive weeks while its "next" line had said "finalise the cutover plan" for four of them, which is a workstream that has not moved reporting that it has. One had a milestone due that Thursday that appeared nowhere in its update. And a risk raised three weeks earlier about a vendor contract had vanished without being closed; the owner, when asked, said it had "probably resolved itself", which meant it had not.

The migration was the important one. The status word was changed to at risk over the owner's objection, with the observation stated plainly in the rollup: same next line for four weeks, cutover date unchanged. That was uncomfortable and it was the right call. At the leadership meeting the owner explained that the cutover plan was blocked on a decision about acceptable downtime that nobody had made, which had been true for a month and had never appeared in an update because "blocked on a decision" had not felt like a blocker to him.

Metrics were pinned to sources: four from the analytics platform, two from billing, one from the support desk, in a fixed order with last week's value beside this week's. Two had been copied forward from update to update for at least a month and were wrong by a material amount when checked against source.

**Result.** The rollup settled at 340 words above the appendix. The chief executive resumed reading it and stopped the Thursday calls, returning roughly three hours a week across four leaders. The downtime decision was made at the following Monday's meeting in about six minutes, having been open for a month. Over the next quarter the number of workstreams reporting on track fell from thirteen of fourteen to about nine, which was not a decline in performance but the first honest reading the company had.

### A second scenario, where it goes differently

A distributed team of nine across five time zones, where the weekly written update replaces the meeting entirely rather than feeding one.

The format changes in three ways. It carries more context, because there is no meeting in which to ask a question, so each exception includes a short paragraph of background that a synchronous rollup would leave out. It has an explicit response mechanism: each decision item names the person and a deadline for their written answer in the thread, since a decision that would take four minutes in a room takes two days in writing and needs a stated cutoff. And it is published on a fixed schedule that suits the widest span rather than the writer's Friday afternoon.

What does not change: exceptions first, outcomes not activity, one named owner per workstream, an honest status word, and the same shape every week.

## Output

**The workstream update, written by each owner:**

```
WORKSTREAM: [name]        OWNER: [name]        STATUS: on track / at risk / blocked
Done:     [outcomes completed this week]
Next:     [what will be true by next week, checkable]
Blocked:  [blocker, who can remove it, since when] or "none"
```

**The rollup, in this order, under 400 words above the appendix:**

```
WEEKLY ROLLUP  |  week ending [date]

HEADLINE
[Two sentences: portfolio condition, and the one thing to act on.]

NEEDS A DECISION OR INTERVENTION
[Each item: the decision, who makes it, by when, cost of waiting.
 If none, write "nothing this week".]

AT RISK OR BLOCKED
[One line per workstream not on track, with the recovery plan or
 the unblock needed and from whom.]

SHIPPED THIS WEEK
[Completed outcomes, one line each, with numbers where they exist.]

METRICS
| Metric | Source | Last week | This week | Movement |

COMING NEXT WEEK
[Milestones due, with owner and date.]

APPENDIX: ALL WORKSTREAMS
| Workstream | Owner | Status | Done | Next | Blocked |
```

Where metrics are charted, keep the chart monochrome, distinguish series by marker shape and dash pattern rather than colour, put the legend outside the plot area, and reserve a single accent for the metric that has moved outside its expected range.

## Failure modes

**Activity instead of outcomes.** Recognise it by the verbs: worked on, continued, progressed, focused on. Rewrite each as a state of the world, and where the state has not changed, say that.

**Organised by team rather than by exception.** Recognise it when the reader has to read every section to find the problems. Invert it: exceptions first, the full table at the bottom.

**Green for weeks, then a slip.** Recognise it by comparing status words across four weeks against a repeated "next" line. Change the status yourself, state the observation that prompted it, and let the owner correct you in the meeting.

**Silence read as fine.** Recognise it when a workstream is missing from the rollup. Every workstream appears every week, including as "no update received", which is itself a status.

**Numbers copied forward.** Recognise it when a metric has not moved at all in three weeks. Check it against its source; a suspiciously stable number is usually a stale one.

**Risks that vanish rather than close.** Recognise it by comparing this week's risks against last month's. Close them explicitly or carry them.

**The rollup that grows.** Recognise it at over 400 words above the appendix. The growth is almost always context that belongs in the appendix or in a decision memo.

## Edge cases

**A workstream is genuinely fine for a long period.** Report it as steady with its next milestone date, and drop it to the appendix only. Do not remove it, because a workstream that disappears from the artefact stops being managed.

**Bad news the owner has not yet told their manager.** Do not publish it in a rollup first. Tell the owner you are including it, give them the hour it takes to have the conversation, and publish on schedule. Surprising someone in a leadership document destroys the trust the update depends on.

**Confidential content, such as a personnel matter or an unannounced deal.** It does not go in the circulated update. It goes in a private note to the reader with a placeholder line in the rollup saying a private item exists, so the record is complete without the disclosure.

**A crisis week.** Suspend the format and say so. A daily one-paragraph update with the current state, the next checkpoint and the single decision needed serves better, and the weekly resumes when the incident closes.

**Nobody sends their updates.** Publish the rollup with the missing workstreams marked as "no update received" and the owner named. This corrects itself within two weeks and requires no confrontation.

## Quality bar

- The reader can act after the headline and the decision section, without reading further.
- Every non-green workstream carries a recovery plan or a named unblock request with a person and a date.
- Every workstream appears, including those with no update, which are marked as such.
- Every done line is an outcome, not an effort.
- Every metric names its source and shows movement since last week.
- Repeated commitments and silently dropped risks are surfaced explicitly.
- The update is the same shape, order and length as last week's.
- It arrives at the same time every week, before the meeting it feeds.

## Related skills

`operating-cadence-design` decides that this update exists, who writes it, who reads it and which meeting it feeds. `okr-planning` supplies the key results and their measurement sources that the metrics section reports against, and `strategic-plan-and-action-plan` supplies the workstreams and milestone dates. `meeting-to-decisions` records what happens in the meeting this update prepares, and the decision items surfaced here become its agenda. `decision-memo` is what a recurring decision item should become when it needs preparing rather than raising again. `investor-update` and `board-and-investor-management` cover the external versions, which need narrative this format deliberately excludes.
