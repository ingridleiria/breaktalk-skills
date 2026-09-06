---
name: program-management
description: Turns an initiative into owned, dated, trackable workstreams and keeps it moving when priorities shift. Produces the four artefacts every program runs on, a one-pager with a written definition of done, a workstream plan with one named owner per stream, a tracker small enough to update in five minutes, and a decision log, plus the weekly cadence and the escalation rules that make them stay true. Enforces the standard that every milestone is a verifiable event with a date and a single accountable name, and that status is written before it is discussed. Use this skill whenever someone wants to plan a project or program, set up a tracker, define milestones, run a kickoff, write a status update, prepare a steering committee or leadership review, manage cross-functional workstreams, recover a slipping project, or says things like "we keep dropping the ball", "who owns this", "set up a cadence", "this keeps slipping", or "turn this meeting into next steps". Trigger for any request involving multiple people delivering something over time, even when the words program and project are never used.
---

# Program Management

An initiative gets a name, a kickoff, and a room full of people who agree it matters. Six weeks later nobody can answer whether it is on track, because there is no definition of what on track would mean. The slip is discovered on the day the date passes, by which point the options that existed in week three have gone: scope could have been cut cheaply then, a contractor could have been booked, the customer could have been told early. In week ten the only remaining option is the expensive one.

That is the failure this skill exists to prevent, and its cost is almost never the project itself. It is the promise attached to the date: a customer commitment, a board expectation, a contract expiry, a compliance deadline. A program is a promise with a date on it, and the chief of staff's version of program management has one goal, which is that nothing important loses momentum when priorities shift. Everything below serves that.

## When to use this, and when not to

Use it whenever more than one person has to deliver something by a date: a system migration, a product launch, a compliance programme, an integration after an acquisition, a new operating process rolling out across teams, an office move. Use it when an initiative already exists and is drifting, which is the more common request and arrives as "can you get your arms around this". Use it when a leadership team keeps asking for a status update and getting a description.

Do not use it for one person's task list, which belongs in `weekly-review-and-planning`. Do not use it to design the company's recurring meeting rhythm, which is `operating-cadence-design`; this skill sets the cadence for one program inside that rhythm. Do not use it to capture the decisions from a single meeting, which is `meeting-to-decisions`. Do not use it to make the choice that starts the program, which is `decision-memo`. Do not use it for a single event with one date and no dependencies, which is `event-and-offsite-planning`. Do not use it to set company goals, which is `okr-planning`; goals and programs are different objects and conflating them produces goals nobody can deliver and programs nobody can measure.

## What you need before starting

**The objective in one sentence, and a written definition of done.** Done is the test somebody could apply on the last day and get a yes or a no. Missing: write the version you think is meant, send it to the sponsor, and ask them to correct it. Do not start without a reply. Almost every scope dispute later traces to this sentence not existing.

**A named executive sponsor.** One person who can settle a dispute between two functions and who will be in the room when scope has to be cut. Missing: ask who would make the call if two heads of function disagreed. If the answer is "we would work it out", the program has no sponsor and will stall at its first real conflict.

**The date, and what it is attached to.** A contract expiry, a customer go-live, a regulatory deadline, or an internal preference. These are not the same and they set how much the date can move. Missing: ask what happens on the day after. If nothing happens, the date is a preference and should be labelled as one.

**The people, and the share of their time that is genuinely available.** Not the names on the org chart. Missing: assume half of what was offered, write the assumption into the one-pager, and let it be corrected. A plan built on nominal availability slips in week two and everyone acts surprised.

**The dependencies outside your control.** A vendor, another team's release, a legal review, a procurement cycle. Missing: list what you think they are and ask the owners to confirm. Unowned dependencies are where dates go to die, because nobody escalates a thing they did not know they were waiting for.

**Where the team already looks.** A shared board, a spreadsheet, a wiki, a channel. Missing: pick the least effortful place the team already opens daily. A shared tracking tool helps if one is available and adopted; where none is, a single shared spreadsheet with the columns below works, and is better than a new tool nobody has logged into. Never introduce a tool the program has to pay for in order to be run.

## The method

Steps 1 to 4 create the four artefacts every program runs on, whatever its size: the one-pager, the workstream plan, the tracker, and the decision log. Create them at kickoff and never let them drift apart. Steps 5 to 10 are what keeps them true.

### 1. Write the one-pager, and get done agreed

Objective in one sentence, why now, definition of done, sponsor, owner, date, budget or resourcing, and the two or three metrics that define success. If the objective cannot fit in one sentence without an "and", it is two programs; split it and let each have its own date.

### 2. Cut the program into workstreams by deliverable, not by department

Each workstream has a single named owner. Not a team, not two co-leads, a person. Three to six workstreams is the workable range. Above seven, this is a portfolio and the top level should be split into programs with their own one-pagers.

The decision rule for cutting: organise by the thing being produced, not by the function producing it. Department-shaped workstreams generate shared milestones, and a shared milestone is an unowned milestone. If two owners must both act to hit a milestone, it belongs to one of them and the other appears as a named dependency with a date.

### 3. Build the milestone map and find the critical path

Milestones are verifiable events. "Contract signed", "data migrated and reconciled to within 0.5 percent", "version one live to ten users". Not activities: "continue development" and "80 percent complete" are feelings with a date attached.

Then trace the single chain of dependent milestones that sets the end date. That chain is the critical path, and it is the only place where effort moves the date. Write it down and mark those milestones in the tracker, because the most common waste in a slipping program is heroic effort applied off the critical path.

### 4. Set the tracker and define what the statuses mean

One source of truth, ruthlessly simple: workstream, owner, next milestone, date, status, and a one-line note explaining any status that is not green. Keep it small enough to update in five minutes, because a tracker nobody updates is worse than no tracker, and it is worse because people believe it.

Define the statuses objectively before the first update, and write the definitions at the top of the tracker:

- **Green**: the next milestone will be met on its current date, with the work currently in flight.
- **Amber**: at risk of missing a named date or metric, with a recovery plan stated and a date by which it will be known.
- **Red**: the date will be missed, or the workstream is blocked by something its owner cannot resolve.

Without written definitions, green means "I am working hard" and the tracker measures effort.

### 5. Run the kickoff as a contract, not an introduction

Walk the one-pager, confirm the definition of done out loud, name every workstream owner while they are in the room, and agree the cadence and the escalation rule. End with each owner stating their first milestone and its date in their own words. That last step takes ten minutes and converts attendance into ownership.

### 6. Run the weekly cadence on exceptions only

Written status per workstream, submitted before the meeting, in three lines: done last week, planned this week, blockers. The meeting discusses exceptions and decisions. It never goes round the room reading updates aloud, because a meeting that reads the tracker is a meeting that exists because the tracker is not trusted.

Every meeting ends with next steps captured as owner, action, date. An action missing any of the three does not exist. Circulate within twenty-four hours, into the same place the tracker lives.

### 7. Escalate on rules, not on feeling

Agree the rules at kickoff so escalation is mechanical rather than political. The workable defaults: anything amber for two consecutive weeks goes to the sponsor; anything red goes to the sponsor the day it turns red; any dependency owned outside the program that is late by more than five working days goes to the sponsor with a named person and a specific ask.

### 8. Hold a milestone review that asks for something

Monthly, or at each major milestone. Lead with the headline in one sentence: on track, at risk, or off track and why. Then the metrics from the one-pager. Then the decisions needed from the room, each with the options and their costs.

### 9. Recover deliberately when it slips

Run the four-step sequence in the section below rather than adding meetings. A meeting added to a slipping program removes capacity from the critical path and adds nothing.

### 10. Close it properly

A program that fades out teaches the organisation that dates are decorative. Write a closure note: what was delivered against the definition of done, what was cut and why, the final metrics, who owns what from here, and the two or three things that would be done differently. Archive the decision log with it, and hand any repeatable process the program leaves behind to `process-documentation-sop`.

## Status writing

Status updates follow one shape: headline, evidence, ask.

The headline states the program's condition in one honest sentence. On track written five weeks in a row before a slip announcement means the earlier four updates were false, and the cost is paid the next time you write on track and it is true.

At risk means at risk of missing a named date or a named metric. Name which one, state the recovery plan, and give the date by which it will be known whether the recovery worked.

Blocked names the blocker, the person who can unblock it, and the date the block became binding. That third element is what stops a two-week-old blocker being reported as new.

## Recovering a slipping program

1. **Re-verify the definition of done.** Scope creep hides here more often than anywhere else, and it usually arrived one reasonable request at a time. Compare what is now being built against the sentence agreed at kickoff.
2. **Re-trace the critical path.** It moves. The chain that set the date in week one is frequently not the chain setting it in week nine, and teams keep pushing on the old one.
3. **Present exactly three options with costs attached**: cut scope, move the date, or add resources. Working harder is not an option, it is the plan that already failed. Each option carries a number: what is lost, how long the date moves, or what the extra capacity costs and how much time it actually buys, accounting for the ramp.
4. **Reset the plan publicly, once.** Serial small slips destroy more trust than one honest re-baseline, because each small slip is a fresh surprise and a re-baseline is a single conversation. After the reset, the new dates are treated as the original ones.

## Worked example

**Situation.** Bramley Logistics, a 340-person distribution business, had to replace its order management system. The incumbent contract expired on 31 January and the vendor had quoted 180,000 for a three-month extension. Peak trading ran from late October to the third week of December, during which the operations director would not accept any change to live systems. The program had existed for seven weeks with a name, a weekly meeting, and no tracker, and three people gave three different answers to what was in scope.

**Task.** Get the new system live before 31 January without touching production during peak, or establish early enough that it could not be done to negotiate the extension from a position other than desperation. Good meant that by the end of week three, the leadership team could see the critical path and knew what the realistic options were.

**Action.** The definition of done was written first and it was contentious, which was the point. The draft said: all order types processed in the new system, all five integrations live, historical orders migrated for two years, and the incumbent contract terminated on 31 January. The finance director objected that the returns module had never been agreed. That objection, surfaced in week one, was worth more than any analysis done later.

The wrong turn came next. The first workstream cut mirrored the org chart: sales, operations, finance, and information technology. Two weeks were lost to it. Every milestone had two or three functions attached, so no milestone had an owner, and the first status round produced four updates that each described the same integration from a different angle. It was re-cut by deliverable into four workstreams, each with one owner: data migration, integrations, process redesign and training, and cutover and contingency. Fourteen milestones, all verifiable events.

The critical path ran through data migration, seven of the fourteen milestones. That single finding changed the staffing: two people came off training material, which had felt urgent and was not on the path.

In week nine the data migration owner turned the workstream amber with a specific note: 61 percent of stock-keeping unit records were failing validation against the new schema, mostly because of a legacy free-text field used for three different purposes by three different depots. Amber for two consecutive weeks triggered the escalation rule, and it went to the sponsor in week ten with three costed options.

Cut scope: defer the returns module, which removed five weeks from the critical path and required a manual process for roughly forty returns a week until March. Move the date: the 180,000 extension, plus the risk that the same problem reappeared in a longer run. Add resources: two data contractors at 46,000 for eight weeks, expected to save around two weeks after allowing for a ten-day ramp.

The sponsor chose cut scope plus one contractor: not the cheapest option and not the fastest, but the combination that put the most slack on the critical path for the least money. The plan was re-baselined once, publicly, in a twenty-minute session, and the new dates were treated as the real ones from that point.

**Result.** The system went live on 24 January, seven days before the contract expiry, with the returns module deferred to March and two of the five integrations running in a reduced mode that needed a daily reconciliation for six weeks. The extension was not needed, so the 180,000 was not spent, against 46,000 for the contractor.

The deferred returns module cost real operational pain: about forty manual returns a week for nine weeks, absorbed by two people in customer service who were not happy about it and said so in the closure retrospective. That is the honest ledger. The program hit its date by choosing which promise to break, early enough to choose.

### A second scenario, where it goes differently

A twelve-month programme to move a services team onto a new way of scoping and pricing work. No contract expiry, no external date, and a sponsor who added two reasonable requests a month.

Almost nothing on the critical path is worth computing, because with no fixed end date the path has no teeth. The discipline moves to two other places. First, a scope contract: the definition of done is versioned, and every addition is accepted only with a named thing removed or a date moved, decided by the sponsor in the monthly review and written into the decision log. Second, time-boxed increments with a kill rule agreed at kickoff: if the first two teams using the new approach have not cut scoping time by a quarter within ninety days, the programme stops rather than expands.

The four artefacts are identical. The weekly cadence is identical. What changed is that the constraint enforcing honesty is no longer the date, so it has to be a written scope contract and a stated condition for stopping. Programs without deadlines do not fail loudly; they fail by continuing.

## Output

**The one-pager:**

```
PROGRAM:        [name]
OBJECTIVE:      [one sentence, no "and"]
WHY NOW:        [what forces this, and what changes if it waits]
DEFINITION OF DONE: [the test somebody applies on the last day, yes or no]
SPONSOR:        [one name]        OWNER: [one name]
DATE:           [date]            ATTACHED TO: [contract, customer, regulator, preference]
RESOURCING:     [people, share of time, budget, who approves an overrun]
SUCCESS METRICS: [two or three, each with a current value and a target]
OUT OF SCOPE:   [the things people will assume are included and are not]
ESCALATION RULE: [what triggers going to the sponsor, and how fast]
```

**Workstream and milestone plan:**

| Workstream | Owner | Milestone (verifiable event) | Date | On critical path | Depends on | Dependency owner |
|---|---|---|---|---|---|---|

**Tracker**, with the status definitions written at the top:

| Workstream | Owner | Next milestone | Date | Status | Note if not green |
|---|---|---|---|---|---|

**Weekly written status**, one block per workstream, before the meeting:

```
WORKSTREAM:  [name]        OWNER: [name]        STATUS: [green / amber / red]
DONE:        [last week, verifiable]
NEXT:        [this week]
BLOCKERS:    [blocker, who can clear it, date it became binding]
```

**Decision log:**

| Date | Decision | Decider | Rationale in one line | Link |
|---|---|---|---|---|


## Failure modes

**Green until the week it slips.** Recognise it when a workstream reports green for five weeks and then moves straight to red. The cause is almost always undefined statuses. Fix by writing the definitions into the tracker and asking, each week, what would have to be true for this to be amber.

**Two accountable names on one row.** Recognise it in any RACI with more than one A. Two accountable people is nobody accountable. Fix by picking one and making the other a named dependency with a date.

**Milestones expressed as percentages.** Eighty percent complete is a feeling. Fix by rewriting each milestone as an event somebody outside the workstream could verify.

**The status meeting that exists because the tracker is not trusted.** Recognise it when the meeting is spent establishing facts rather than making decisions. Fix the tracker, then shorten the meeting; do not do the reverse.

**An owner with no date, or a date with no owner.** Both mean the item is not real work yet. Fix at the point of capture: nothing is recorded without owner, action, and date.

**Effort applied off the critical path.** Recognise it when a program is late and everyone is busy. Re-trace the path; it has usually moved since the plan was written.

**The program that is actually two programs.** Recognise it when the objective needs an "and", or when two workstreams never depend on each other and never appear in the same conversation. Split it and give each its own date.

## Edge cases

**The sponsor leaves.** The program is at its most fragile in the two weeks after. Get a replacement named within one week, walk them through the one-pager and the decision log rather than the tracker, and re-confirm the definition of done in writing. Assume every settled scope argument will be reopened, and have the log ready.

**The date genuinely cannot move.** A regulator, a contract expiry, a stadium booking. Then scope is the only variable, and it should be ranked at kickoff: which parts go first if capacity is short. Ranking scope while things are calm takes an hour; ranking it in week nine takes a fortnight and a fight.

**A critical workstream is owned by a vendor or another company.** You cannot manage their internal work, so manage the interface: a named individual on their side, a fortnightly written status in your format, and milestones defined as things you can verify from outside. Where their status is not written, treat the workstream as amber by default.

**The program depends on a decision nobody has made.** Do not plan around it and do not wait. Put the decision on the critical path as a milestone with a named decider and a date, and take it to them through `decision-memo`. An undecided decision is the most common hidden critical path item.

**The program should be killed.** Recognise it when the definition of done no longer describes something the business wants, or when the honest recovery options are all worse than stopping. Say so, in writing, with what has been spent and what would be recovered. Proposing to stop a program is the highest-value and least-rewarded thing a program manager does, and it is easier when a kill rule was agreed at kickoff.

## Quality bar

- Every workstream has exactly one named owner, and every milestone is an event somebody outside the workstream could verify.
- The definition of done is written, agreed by the sponsor, and dated.
- The critical path is identified and marked, and it has been re-traced since the plan was written.
- Every status that is not green names a date or a metric at risk, a recovery plan, and when it will be known.
- The tracker can be updated in five minutes and was updated this week.
- Every action carries owner, action, and date, and was circulated within twenty-four hours.
- The escalation rule is written down and has actually been used at least once.
- Decisions are in the log on the day they are made, with a one-line rationale.

## Related skills

`decision-memo` produces the choice that starts a program and settles the costed options when it slips. `structured-problem-solving` supplies the analysis behind those options. `meeting-to-decisions` converts the program's meetings into the actions and decisions this method tracks. `operating-cadence-design` sets the wider meeting rhythm that this program's cadence sits inside. `weekly-status-update` rolls several programs into one leadership view. `okr-planning` sets the goals that programs are chosen to serve, and should not be used as a tracker. `process-documentation-sop` takes over whatever repeatable process the program leaves behind. `event-and-offsite-planning` covers single-date events that do not need workstreams.
