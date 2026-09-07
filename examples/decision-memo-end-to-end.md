# A decision that had been deferred three times

A complete run of [decision-memo](../chief-of-staff/decision-memo/SKILL.md), from the message a Chief of Staff
actually receives to the page that ended the question. The company, the people and the numbers are invented. The
shape of the request is not, because it is the shape almost every one of these arrives in.

---

## 1. The input

This is the whole brief. It is what a real one looks like: a topic, an emotion, a deadline that is not quite stated,
and no decision in it anywhere.

> **From the CEO, 22:14 on a Sunday**
>
> Can you put something together on support coverage for Thursday's leadership meeting. This has come up three
> times now and we keep going round in circles. Marta wants follow the sun, Dan says we can't afford it. The
> Nordwind renewal is the thing I'm actually worried about, they've complained twice about response times and
> that's a real number. Something short please, not a deck. Whatever you think.

Attached to it, in the sense that the Chief of Staff has to go and find them: a support ticket export nobody has
looked at, two threads in a customer channel, a headcount plan, and the fact that the CFO was absent for one of the
three previous discussions.

---

## 2. What the skill did first, which was refuse

Handed that brief, an assistant without a method writes something titled "Support Coverage Options" with three
options and a recommendation, and it is genuinely useful, and it produces a fourth deferral.

The skill's first instruction is not to write anything. It is to establish that there is a decision at all:

> **Write the decision as a closed question.** Answerable yes or no, or by choosing a named option. Test it: could
> two people give different answers and both be answering the same question?

"Support coverage" fails that test, so the run stopped and produced three candidate questions instead of a memo,
which is the useful output at that moment:

- Should we move support to follow the sun coverage before the January renewal cycle?
- Should we extend coverage for enterprise accounts only, rather than for everyone?
- Should we accept current response times for another two quarters and revisit after the January renewals?

The CEO picked the first one in a nine word reply. That exchange cost four minutes and is the reason the meeting on
Thursday ended in a decision. A skill that had produced a polished memo about a topic would have cost an hour and
produced the fourth discussion.

The second refusal came at the options stage. The draft had four options, one of which was a straw man: a
twenty four hour model with a cost so obviously unacceptable that nobody would choose it. The skill names this:

> **Three options where two are decoration.** Recognise it because two options have obvious fatal flaws stated in
> the memo itself. Experienced readers see this immediately and trust the memo less.

It came out. Three real options is a stronger document than four with a decoy, and the CFO in the room is precisely
the person who notices.

---

## 3. The output

One page, in the format the skill specifies.

```
DECISION MEMO
Decision:        Should we move support to follow the sun coverage before the January renewal cycle?
Decider:         CEO          Consulted: CFO, Head of Support     Informed: leadership team
Decide by:       14 November  If not decided:  we enter the renewal conversation on current coverage
Reversibility:   Costly but not one way. Unwinding means one contract terminated at three months notice
                 and one hire redeployed, roughly six weeks and under 40k.

RECOMMENDATION
Extend enterprise coverage to 02:00 through a contracted partner before the renewal window, and decide on
full follow the sun in March with three months of data. It buys the renewal without committing to the
permanent cost structure while the case for it is still an assertion.

WHY NOW
Two of the three enterprise renewals close in January. Nordwind, at 240k annually, has raised response
times twice in writing. Coverage changes take about eight weeks to be visible to a customer, so a decision
after November does not reach them before the renewal conversation.

OPTIONS
| Option | What it is | Cost | Gives up | Has to be true |
| A: do nothing | Keep 09:00 to 18:00, single zone | 0 | Weakest position in three renewal talks | Response time is not the real objection |
| B: partner cover to 02:00, enterprise only | Contracted overflow, our escalation rules | 90k to 110k a year, no hires | Consistency of voice on out of hours tickets | A partner can hold our quality bar on tier one |
| C: full follow the sun | Second support hub | 380k to 430k a year, 4 hires, 5 months | The Q1 hiring plan elsewhere | Volume justifies permanent coverage, which we have not shown |

REASONING
The ticket export shows out of hours volume is concentrated in six accounts, not distributed, which is
what makes B sufficient and C premature. Nordwind's two complaints both concern nights, not weekends.
What would change this to C: if out of hours volume outside those six accounts grows past roughly a
quarter of the total by February, the partner model stops being cheaper and starts being a tax.

RISKS
| Risk | Early signal | Response |
| Partner quality damages the relationship we are protecting | First escalation mishandled in the first month | Named accounts route to our own on call for the first six weeks |
| Cost lands above the range | Partner invoice in month two above 10k | Contract capped at 10k monthly with a review clause |
| B becomes permanent by inertia | March arrives with no decision on C | The March decision has its own date and default, set now |

WHAT WE DO NOT KNOW
Whether Nordwind's objection is really response time or something the account team has not surfaced. Worth
one conversation before the 14th, and it changes the recommendation only if the answer is no.
```

**Log entry, written the same day:**

```
2026-11-14 | Enterprise support extended to 02:00 via partner, full follow the sun deferred to March
CEO | Buys the January renewals without committing to permanent cost while the case is unproven | Costly,
not one way | link to memo
```

---

## 4. What the method contributed

Five things, none of which are writing quality.

**It converted a topic into a question**, before any work was done, which is the step that had been skipped in all
three previous discussions.

**It put the reversibility judgement before the analysis**, which is what justified deciding in three weeks on
partial data rather than commissioning the study that would have deferred it a fourth time.

**It made doing nothing a real option**, honestly costed. Option A is not a straw man here, and a reader who
believes response time is not the true objection can argue for it from the memo itself.

**It required a default.** Without the line saying what happens on 14 November if nobody decides, this memo is a
suggestion, and suggestions are what the previous three discussions produced.

**It wrote the reversal condition down.** The sentence naming what would change the recommendation to option C is
what makes the March decision a scheduled review rather than an argument about whether November was wrong.

The output above is not better prose than an unstructured assistant would produce. It is a different document,
because the method refused the request twice before writing anything.

---

## Try it

Take a decision your own organisation has deferred more than once. Run
[decision-memo](../chief-of-staff/decision-memo/SKILL.md) on it in whichever assistant you use, following
[USING_THESE_SKILLS.md](../USING_THESE_SKILLS.md). The interesting moment is not the memo. It is whether the first
thing you get back is a memo or a question.
