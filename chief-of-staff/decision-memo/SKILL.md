---
name: decision-memo
description: Writes the one-page memo that ends a decision instead of scheduling another meeting about it. Produces a closed question, options including doing nothing, a recommendation stated before the analysis, an explicit reversibility judgement that sets how much analysis the decision deserves, one named decider with a tie-break rule, a date with a default, and a decision log entry. Use this skill when a choice has to go to a leader or a group, when the same question keeps returning to the same meeting, when someone asks for a recommendation or a business case for a choice, when a decision needs recording so it stays decided, or when someone says they need to get sign-off on something.
---

# Decision Memo

Decisions rarely drift because they are hard. They drift because nobody wrote down what was being asked, what the options actually cost, who was deciding, and by when. The same question comes back to the same meeting three times, each time with slightly different framing, and the third discussion is worse than the first because everyone half-remembers the second.

The cost is not the meeting time. It is that the decision eventually gets made under time pressure by whoever is in the room, on partial information, with no record of why. Six months later somebody reopens it, and nobody can defend the original reasoning because there is none written down.

This skill produces one page whose only job is to end that loop.

## When to use this, and when not to

Use it when a choice between named options has to be made by someone else, when a question has come back twice, when a decision needs to survive being revisited, or when you are about to ask for approval of anything with a cost.

Do not use it for a decision you can make yourself, which needs a note in the log and nothing more. Do not use it to present a conclusion already reached and unchangeable, which is an announcement and should be written as one. Do not use it when the real problem is that nobody knows who decides; fix that first, because a memo addressed to nobody is an invitation to defer.

`structured-problem-solving` covers memo structure and the underlying analysis generally. `meeting-to-decisions` captures decisions made in conversation rather than prepared beforehand. This is for the decision prepared before the conversation.

## What you need before starting

**The decision, as a choice between named things.** If you only have a topic, go back and find the choice. Missing: write the two or three candidate versions of the question and ask which one they mean.

**Who decides.** One name, or a group with a tie-break rule. Missing: ask directly, in those words. The most common answer is that nobody has thought about it, which is itself the finding.

**The deadline, and what happens if it passes.** Missing: propose one and say what the default is, because a memo without a date is optional.

**The options, including the status quo.** Missing: generate them, but never present three where two are obviously unacceptable.

**Rough costs.** Money, people, time, and what each option gives up. Missing: state ranges and label them as estimates. A wrong order of magnitude is worse than an honest range.

**The constraints already fixed.** A budget cap, a commitment made to a customer, a preference the chief executive has expressed that nobody will contradict. Missing: ask. Analysis that ignores a fixed constraint is theatre.

## The method

1. **Write the decision as a closed question.** Answerable yes or no, or by choosing a named option. "Should we move support to follow-the-sun coverage before the January renewal cycle" is a decision. "Support coverage" is a topic. Test it: could two people give different answers and both be answering the same question?

2. **Establish reversibility before anything else.** This single judgement sets how much work the decision deserves. Ask what it would cost to undo, and how long it would take. A decision that can be reversed in a week for a small cost should be made fast on partial information; an expensive one-way decision earns another week of analysis. Most wasted decision time comes from confusing the two, in both directions.

3. **Write the recommendation.** Before the analysis, in one sentence. A reader who agrees can stop. A reader who disagrees now knows exactly what to argue with. Burying the recommendation under the reasoning makes the reader do the work of finding the point, and busy readers do not do that work, they defer.

4. **Build the options.** Two to four, always including doing nothing. For each: one sentence of what it is, the cost in money and people and time, what it gives up, and what has to be true for it to work. Present doing nothing honestly; it is often the strongest option and a straw-man version of it discredits the whole memo.

5. **Write the reasoning.** One short paragraph. Why this option, what evidence supports it, and what evidence would change it. That last clause is what makes the memo a document rather than an advertisement.

6. **Name the risks and their early signals.** Two or three, each with the thing you would observe first if it were happening. A risk with no signal cannot be managed, only regretted.

7. **Set the decision rights.** One named decider. Who is consulted, who is informed. If the decider is a group, state what happens when they do not agree, because that case is what produces the fourth meeting.

8. **Set the date and the default.** When this must be decided, and what happens automatically if it is not. The default is what gives the date teeth.

9. **List what you would need to know, only if it would change the answer.** Unknowns that would not alter the recommendation are a reason to decide now, and saying that explicitly is more useful than gathering more.

10. **Log it the day it is decided.**

## Worked example

**Situation.** A ninety-person software company. Support currently runs 09:00 to 18:00 in one time zone. Two enterprise customers in another region have complained about response times, one of them in a renewal conversation worth about 240,000 a year. The head of support has been asking for a follow-the-sun model for two quarters. It has come up in three consecutive leadership meetings and been deferred each time, twice because the cost was unclear and once because the chief financial officer was absent.

**Task.** Get a decision at the next leadership meeting, eight days away, or accept that the renewal conversation happens with nothing changed. Good means a decision either way, with a reason on record.

**Action.** The first draft was a three-page analysis of coverage models with a comparison table of five options. It was abandoned after a conversation with the chief financial officer, who asked one question the draft did not answer: what does this cost in the first twelve months and how quickly can we stop if it does not work. That question reframed the whole memo.

The rewrite led with reversibility, which had not been considered. Hiring two support engineers in the second region is expensive and slow to reverse, roughly six months and a redundancy cost. Contracting the same coverage through an existing partner is reversible inside a notice period of thirty days at a higher unit cost. That distinction turned a difficult decision into an easy one, because the reversible option could be tried without needing to be right.

Options came down to three. Do nothing, cost zero, risk the renewal and the pattern of complaints continuing. Hire two engineers in region, roughly 190,000 fully loaded in year one, live in four to five months, hard to reverse. Extend the existing partner contract to cover the gap, roughly 96,000 in year one at a worse margin, live in three weeks, cancellable on thirty days.

The recommendation was the partner option, explicitly as a six-month test, with a stated success threshold agreed in advance: first response under two hours for the region during their working day, measured monthly, and the renewal closed. If both hold at six months, convert to hiring.

The wrong turn worth recording: the first draft compared five coverage models in detail. Four of them could not be distinguished with the information available, and comparing them made the memo look thorough while making the decision harder. Cutting to three options that were genuinely different was the change that made it decidable.

**Result.** Decided in eleven minutes at the leadership meeting, with the chief executive as the named decider and the chief financial officer consulted. The partner extension went live nineteen days later. At the six-month review the response time threshold held and the renewal closed, so the decision converted to hiring, and the second memo took an hour to write because the first one had already established the frame and the threshold.

The part that mattered was not the analysis. It was that the reversibility judgement moved the decision from a category where people wait for certainty to a category where they can act and find out.

### A second scenario, where it goes differently

Same company, a decision about which customer data platform to standardise on. Here reversibility runs the other way: migration is expensive, the contract is three years, and the integration work touches four teams. That decision deserves the extra two weeks, a reference call with two companies who made the same choice, and a written statement of what would have to be true for the second-place option to be right. The memo is still one page, and the appendix is eleven.

The shape does not change. What changes is how much evidence the recommendation is allowed to rest on.

## Output

```
DECISION MEMO
Decision:        [the closed question]
Decider:         [one name]   Consulted: [names]   Informed: [names]
Decide by:       [date]       If not decided:      [what happens by default]
Reversibility:   [easy / costly / effectively one way] + [what undoing costs, in time and money]

RECOMMENDATION
[One or two sentences. The recommendation and the single strongest reason.]

WHY NOW
[What forces this, and what changes if it waits.]

OPTIONS
| Option | What it is | Cost (money, people, time) | Gives up | Has to be true |
| A: do nothing | | | | |
| B: | | | | |
| C: | | | | |

REASONING
[One paragraph. Why B, and what evidence would change it to C.]

RISKS
| Risk | Early signal | Response |

WHAT WE DO NOT KNOW
[Only the unknowns that would change the answer. If none, say so.]
```

Appendix for anything longer. The one page is the deliverable.

## The decision log

This skill owns the decision log. `meeting-to-decisions` feeds the same log with decisions taken in conversation rather than prepared beforehand, and the two write into one place; where the two descriptions differ, this one governs.

Every decision made goes into one log, kept where the team already looks. Six fields and no more: the date, the decision in one sentence, the decider, the reasoning in one line, the reversibility judgement, and a link to the memo or the meeting record behind it. Six is deliberate. A log that acquires a status column and an owner column becomes a project tracker, stops being written in within a month, and the decisions go back to being remembered rather than recorded.

The log answers the two questions that otherwise consume enormous time: was this decided, and why. When someone reopens a settled question, the answer is the log entry and a request for what new information has appeared. A decision should be revisited on new evidence and should not be revisited because the person who disagreed waited long enough for everyone to forget.

Two habits make it usable rather than decorative. Write the entry on the day the decision is made, because the reasoning is the part that cannot be reconstructed a fortnight later. And log the decisions to do nothing, which are the ones nobody remembers making and the ones most often reversed by drift rather than by argument.

Where no log exists, start one and seed it with the last three decisions people are still arguing about. It takes minutes a week to maintain once it exists, and it is the cheapest institutional memory an organisation can hold.

Review the log quarterly for decisions whose assumptions have since been disproved. Reopening those deliberately is healthy; reopening by attrition is not.

## Failure modes

**The topic disguised as a decision.** Recognise it because the options are not mutually exclusive. Fix by asking what changes on Monday depending on the answer.

**Three options where two are decoration.** Recognise it because two options have obvious fatal flaws stated in the memo itself. Experienced readers see this immediately and trust the memo less. Fix by presenting two real options, or by presenting one with the recommendation stated as a recommendation.

**Analysis proportionate to the writer's interest rather than the decision's weight.** Recognise it when a reversible decision has a fifteen-page appendix. Fix with the reversibility judgement, done first.

**No decider.** Recognise it when the memo is addressed to a meeting. Fix by naming one person, even provisionally, and letting them correct you.

**The date with no default.** Recognise it because the date passes without anyone noticing. Fix by writing what happens automatically.

**Costs without ranges.** A single precise number for something estimated invites an argument about the number instead of the decision. Fix with a range and a label.

**The memo that hides the recommendation to seem balanced.** Recognise it when the reader has to reach page two to find out what you think. Balance is in presenting options fairly, not in withholding your view.

## Edge cases

**The decision has already been made.** Say so and write an announcement instead. A memo that pretends a settled decision is open wastes everyone's time and is transparent to the reader.

**The decider will not decide.** Escalate the fact rather than the decision: tell them the date, the default, and that you will proceed on the default. This is usually what unsticks it.

**Two options are genuinely equal.** Say so, pick one on a stated tiebreaker such as reversibility or speed, and note that the choice was close. Manufacturing a difference to justify a recommendation is worse than admitting the coin flip.

**The information you need does not exist and cannot be got in time.** Frame the decision as a bet: state the assumption it rests on, the cost if the assumption is wrong, and the date you will know.

**A group decides and they will not agree.** Set the tie-break in advance, in the memo. The most workable rules are that the person accountable for the outcome decides, or that the chief executive decides on a stated date.

## Quality bar

- The decision is a closed question, answerable by choosing one named option.
- Reversibility is stated with what undoing would cost in time and money, and the depth of analysis matches it.
- The recommendation appears before the analysis.
- Doing nothing is one of the options and is presented fairly.
- One named decider, with the tie-break rule where it is a group.
- A date, and what happens by default if it passes.
- Every cost is either a real figure or a labelled range.
- One page, with everything else in an appendix.
- The decision is written to the log with its reasoning on the day it is made.

## Adapting this to your context

The examples come from software companies of fifty to two hundred people where one named person can decide. Fix the decision rights before you fix the format.

- **One named decider.** Assumes an executive hierarchy. In a partnership, a co-operative, a trustee board or a works council the equivalent is a body plus a written tie-break, and the memo has to name the quorum and the majority the decision needs.
- **The reversibility judgement.** Sized here in weeks and money. Where undoing costs a licence, a reputation, a clinical outcome or someone's employment, say so in those terms rather than converting it into a number that understates it.
- **The one-page limit.** Suits readers who read. Where the decider is a committee working through fifty pages, keep the one page and put the reference material behind it, which is what the appendix is for.
- **Costs as ranges.** Fine commercially. Public bodies and grant-funded organisations usually have a mandated business case template; write this memo first and fill their form from it, never the other way round.
- **What not to change.** The decision is a closed question, doing nothing is presented fairly as an option, and the date carries a stated default.

## Related skills

`structured-problem-solving` produces the analysis this memo reports. `meeting-to-decisions` catches decisions taken in conversation and feeds the same log. `principal-simulator` predicts how the named decider will react before the memo is sent. `vendor-evaluation` and `partnership-assessment` produce their own recommendation memos in this format.
