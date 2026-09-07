---
name: sales-team-competency-assessment
description: Assesses a sales team against a defined ideal profile by blending two views of each competency, the seller's own self-assessment and their leaders' evaluation, into one score per area and per person, with the gap between the two treated as a finding in its own right. Produces a team dashboard, a perception-gap view, an auditable workbook where every figure is a formula reading the response data, per-person profiles, and coaching plans seeded from the results. Optionally includes a personality component from whatever validated instrument the organisation already licenses. Use this skill when self-assessment and manager-evaluation data exist for a sales team and need scoring, when someone asks for an ideal seller profile assessment, a team capability review, a skills gap analysis, per-rep coaching plans, or wants to know where the team is strong and where it is not.
---

# Sales Team Competency Assessment

A self-assessment on its own measures confidence. A manager evaluation on its own measures visibility: what the manager has had occasion to see, which is heavily weighted toward the accounts they joined and the calls that went wrong. Either one alone produces a ranking that feels authoritative and reorganises coaching, territories and sometimes careers around an artefact of who talks about their own work.

The cost lands in three places. Coaching goes to the people who describe their difficulties rather than the people who have them. A capable seller who under-rates themselves gets treated as a development case and eventually leaves. And the report itself gets challenged in the room by someone whose number looks wrong, at which point the only defence is being able to show the response that produced it, which most such reports cannot do.

Two things make this assessment useful rather than decorative: the blended score, and the gap. A person who rates themselves two points above their leaders has a fundamentally different problem from a person who rates themselves below, and neither problem is visible in a single number.

## When to use this, and when not to

Use it when self-assessment and leader-evaluation data exist, or can be gathered, for a defined team. Use it when a capability picture is needed before a territory redesign, a change in the sales motion, an enablement investment, or a decision about who is ready for larger accounts. Use it to calibrate an ideal profile before hiring against it, since a profile nobody currently meets is a warning about the profile as often as about the team.

Do not use it as the sole basis for a compensation, promotion or exit decision. It is a development instrument built partly on self-report, and using it that way corrupts the next cycle's data within one round, because people learn to score strategically. Do not use it to judge capability from a single call, which is `sales-call-analysis`. Do not use it to rehearse or drill the behaviours it identifies, which is `sales-roleplay`. Do not use it to design an interview process for candidates, which is `hiring-scorecard-and-interview-kit`. Do not use it to size a team or plan capacity, which is `annual-planning-and-headcount`.

## What you need before starting

**Self-assessment responses, per person, with numeric answers.** Missing for an individual: report them as leader-only, with a visible note, rather than substituting a team mean, which invents a person.

**Leader evaluations covering the same competency areas, one response set per leader per person.** Missing entirely: the assessment cannot be run as designed. Say so and offer the reduced version, a self-assessment summary with no blending and no fit labels, clearly titled as such.

**The mapping from instrument questions to competency areas.** Kept in a `framework.json` beside this skill so the framework can be retuned without touching the method. Missing: derive it from the question text, write it into the file, and have whoever owns the instrument confirm it before any number is published. A mapping nobody signed off is where challenges land.

**The scale, its direction, and any reverse-coded items.** A single reverse-coded item scored the wrong way moves an area mean by a quarter of a point and is invisible in the output. Missing: check the question wording for negatives and confirm the direction against two completed responses by hand.

**The ideal profile, with the source of each rating.** Whether it came from a leadership workshop, from the record of the top performers, or from one executive's judgement, and which, because the answer changes how much weight the comparison carries. Missing: build it from the framework areas at a stated target level, and label it as provisional.

**Who evaluated whom.** Uneven leader coverage is the most common data problem in this exercise and the one that most distorts rankings. Missing: reconstruct it from the response file and publish the coverage count per person.

**Open-ended comments, as written.** Missing: leave the section out. Never paraphrase, and never generate a comment.

**Personality results, where the organisation licenses a validated instrument.** Optional. Missing: run the assessment on competency alone, and say in the output that the personality component is absent rather than leaving a blank column that implies a missing value.

**The consent and data protection basis for processing the responses.** Who sees individual-level results, who sees only aggregates, and how long the data is kept. Missing: ask before analysing anything. This is faster to establish now than to unwind after a person has seen their own name in a ranking they did not know existed.

Never invent a response, a comment, or a personality result. Where something was not answered, it is absent, and the output says so.

## The method

1. **Fix the framework, and record the crosswalk.** Map the instrument's questions to five or so competency areas and record both the mapping and the crosswalk between the instrument's names for the areas and the names used in the output. They are rarely the same, and the mismatch is where reports lose credibility, because a reader who knows the instrument reads a familiar label attached to an unfamiliar number. A workable default set for a business-to-business team: relationship management, executive communication, industry and domain insight, managing accounts and opportunities, and adaptability including digital fluency.

2. **Validate the responses before computing anything.** Check completeness per person and per leader; check for straight-lining, where a respondent gave the same answer to every item, which is a response pattern rather than an assessment and should be flagged rather than silently averaged; check the scale direction; and reverse any negatively worded items. Record every exclusion with its reason. Twenty minutes here prevents the single most damaging outcome, which is a published number that turns out to be wrong.

3. **Convert words to numbers using a recorded mapping.** Where leaders answered in words rather than on a scale, the text-to-number mapping lives in the framework file and is applied uniformly. An ad hoc conversion made while scoring cannot be defended a week later, and it will be asked about.

4. **Compute the five figures per area, in this order.**

```
area self          = mean of that area's questions, self responses
area per leader    = mean of that area's questions, that leader's responses
area leadership    = mean across leaders of each leader's area mean
area combined      = mean(area self, area leadership)
gap                = area leadership - area self
overall per source = grand mean of all questions for that source
overall combined   = mean(overall self, overall leadership)
```

   Average the leaders' means rather than pooling their raw items, so that a leader who answered more questions does not silently carry more weight. Where a leader did not evaluate someone, they are absent and the consensus uses whoever did; publish the count so a score built on one leader is never read as a score built on three.

5. **Compute the gap and apply the flag rule.** Flag any person whose leadership and self scores differ by 0.75 points or more on a one to four scale, in either direction. Set the threshold in the framework file so the same rule applies next cycle.

   The threshold is calibrated, not chosen for roundness. A one to four scale has three points of usable range, so a gap of two points is two thirds of everything the instrument can express, and in practice it is rarer than a straight-lined response set; a rule set there flags almost nobody and the gap analysis quietly stops existing. Area means, which are what is being compared, sit inside a much narrower band than raw items do. A quarter of the usable range, which is 0.75 points here, flags roughly a fifth to a third of a team, which is the number of coaching conversations a leader can actually hold in a cycle. Convert it proportionally when the instrument differs: a quarter of the usable range is 1.0 on a one to five scale and 1.75 on a one to eight. Where the flag rate comes out above about a third of the team, the finding is calibration between the two sources rather than perception on individuals, and it is reported that way.

   The flag is a coaching conversation regardless of the underlying level, and it is often the most valuable single output of the whole exercise.

6. **Map to fit labels on one scale.** Read on the blended score across a one to four instrument: 3.5 and above is high, 3.0 to 3.49 moderate to high, 2.5 to 2.99 moderate, 2.0 to 2.49 low to moderate, below 2.0 low. Use the same five labels for the competency score, the personality fit and the overall fit, so the three read on one scale rather than three vocabularies. Where the instrument uses a different range, convert once, at the start, and state the conversion.

7. **Blend the personality component only where it exists.** Convert to the same five-label scale, average with competency fit, and map back. Where no instrument is licensed, competency fit is the overall fit and the output says so plainly. Never infer personality from competency responses or from a manager's description of someone: that is invention about a person, it will be read as a clinical claim, and it has no place in a document with their name on it.

8. **Build the team view.** One row per person: competency score, competency fit, personality fit where present, overall fit, leader coverage count, and the gap flag. Then a quadrant placing each person by competency against personality, and a perception-gap view showing self against leadership per person, sorted by gap size rather than alphabetically, because the sort is what makes the pattern visible.

9. **Write the findings as the story behind the numbers.** A restatement of the table is not a finding. A finding names a pattern and what it implies: that the team's weakest area is the one that most differentiates in the deals they are losing, or that the three highest self-scores in executive communication belong to the three people with no executive relationships in their accounts.

10. **Build coaching plans, one per person, and mark what is provisional.** Their profile against the ideal, the competency detail with all three averages, their own reflections as written, and a development plan seeded from the blended results and from what the person asked for themselves. Specifics are set in the live conversation, and the document says so rather than inventing objectives on their behalf.

11. **Make it auditable.** Every figure in the workbook is a formula reading the response sheet, never a pasted number. The test is that changing one response moves every figure that depends on it. This is the file that gets challenged, and the ability to trace a number to a cell ends the challenge in thirty seconds.

## Reading the perception gap

The gap is diagnostic, not a score. Read it as four cases.

| Pattern | What it usually means | What to do |
| --- | --- | --- |
| Self well above leadership | Unrecognised weakness, or work the leaders cannot see | Ask for evidence in both directions before concluding; the second case is common in remote and named-account teams |
| Self well below leadership | Under-confidence, or a high internal standard | Say so explicitly to the person; this group is the most likely to be lost to a competitor who flatters them |
| Both high and aligned | A reliable signal, and the closest thing here to a fact | Use them to calibrate the ideal profile and as the peer coach for one area |
| Both low and aligned | An agreed development need, which is the easiest conversation in the set | Move straight to the plan; no persuasion is required |

A gap on one area with alignment on the rest is a specific coaching topic. A gap across every area is about the relationship between that person and that leader, and it is a management finding rather than a capability one.

## Worked example

**Situation.** A fourteen-person team selling maintenance software into industrial accounts. Two regional leaders, an instrument of forty questions on a one to four scale, and a licensed personality instrument covering nine of the fourteen people, the five most recent hires never having taken it. The sales director wanted a capability picture before splitting the team into a named-account group and a volume group.

**Task.** Score the team, identify who was ready for named accounts, and produce coaching plans, in a form that would survive being questioned by the two leaders in the room.

**Action.** Validation came first and produced three findings before any scoring. One seller had answered 4 to all forty self questions, which was flagged as straight-lining and reported alongside their leader scores rather than blended. Leader coverage was uneven: leader A had evaluated all fourteen, leader B only nine, so five people had a leadership consensus resting on one evaluator, and that count went into the dashboard as its own column.

The wrong turn came next. Because leader coverage was incomplete, the first version ranked the team on self-scores, with leader scores shown beside them as context. It was abandoned once leader B's nine evaluations were added, which changed the top five by three positions and moved one person from second to ninth. Ranking on the more complete source is not the same as ranking on the better source, and a ranking that inverts when more data arrives was never a ranking.

A second question then had to be settled. Leader A's overall mean across all fourteen was 2.6; leader B's across their nine was 3.4, a difference of 0.8. Adjusting for leader severity was considered and rejected: with nine and fourteen evaluations there is no way to separate a stricter leader from a stronger group, and an adjustment applied on that evidence would be a judgement dressed as a correction. Instead, per-leader means were shown in every table, the difference was named in the findings, and the two leaders were asked to calibrate on three people together, which took an hour and moved leader B down about 0.3 on the areas where they had been most generous.

Results: team competency mean 2.81, moderate. The strongest area was relationship management at 3.24, the weakest executive communication at 2.38, with the widest spread of any area, from 1.6 to 3.8. Four people of fourteen were flagged on the 0.75-point gap rule, three of them over-rating in executive communication by between 0.8 and 1.3 points, one under-rating across everything by an average of 0.9. Of the nine with a personality component, six had overall fits at moderate to high or above.

The finding that changed the decision was not in the ranking. Executive communication was both the weakest area and the one the leaders had named as decisive for named accounts, and the three people scoring highest on it in their self-assessment were all in the over-rating flag group. The named-account split was made on the blended score for that area alone, and two people the leaders had expected to move did not.

**Result.** Fourteen coaching plans, a dashboard, and an auditable workbook where every figure traced to a response cell. Two figures were challenged in the review meeting and both were resolved inside a minute by opening the formula. The named-account group was set at five people rather than the seven originally planned, and enablement spend for the following two quarters went to executive communication for the whole team rather than to a general programme.

The person who under-rated themselves across every area scored 3.1 blended and had been on an informal development list. They came off it. That single correction was the most defensible outcome of the exercise, and it came from the gap rather than from the score.

### A second scenario, where it goes differently

A five-person team, one leader, and self-assessments returned by only three of the five.

Blending is not available for two people, the leadership consensus is one person's opinion by definition, and a quadrant of five points invites the reader to see a pattern in noise. What changes: no ranking is published, no quadrant is drawn, and fit labels are reported per area rather than as an overall label per person, because a single overall number built on one evaluator carries an authority the data cannot support.

What stays: the framework, the recorded mapping, the auditable workbook, the per-person profiles, and the coaching plans, which are the deliverable that actually gets used. The two people without self-assessments are shown as leader-only with the reason stated, and the gap analysis simply does not exist for them rather than being estimated.

The honest framing for a team this size is that the exercise is a structured conversation with the leader, supported by data, rather than a measurement. Saying that in the document is what keeps it credible.

## Output

Three deliverables.

**1. Team assessment.** An executive summary in four lines: the situation, the headline, what stands out, and the recommendation. Then the dashboard.

| Person | Competency score | Competency fit | Personality fit | Overall fit | Leaders evaluating | Gap flag |

Then the quadrant, the perception-gap view sorted by gap size, the ideal profile with the source of its ratings and an explanation of the scale, and the findings written as the story behind the numbers.

**2. Leadership workbook.** Auditable, one row per person per area:

| Person | Area | Self | Leader A | Leader B | Leadership mean | Combined | Gap | Fit |

Plus the overall rows, the open-ended comments as written, the validation log with every exclusion and its reason, and the framework mapping. Every figure is a formula reading the response sheet.

**3. Coaching plan, one per person.**

```
Profile against the ideal:   [area by area, blended, with the ideal alongside]
Perception gap:              [where self and leadership diverge, and by how much]
Personality component:       [where licensed; otherwise stated as not held]
Their own reflections:       [reproduced from source, unedited]
Strengths to deploy:         [two, each tied to an area score]
Development focus:           [one or two, with the evidence]
Plan:                        [seeded from results and from what they asked for]
Note:                        [specifics are agreed in the coaching conversation]
```

## Failure modes

**Ranking on the self score because it is complete.** Recognise it when the leadership column is present but not driving the order. Completeness is not authority. Rank on the blend, and publish the coverage count.

**Pooling leader responses instead of averaging their means.** Recognise it when a leader who answered more items moves a score more than one who answered fewer. Compute each leader's area mean first, then average those.

**Silently correcting for leader severity.** Recognise it when an adjustment factor appears with no stated basis. With small teams there is no way to separate a strict leader from a strong group. Show the per-leader means and let the reader see it.

**Three vocabularies in one report.** Recognise it when competency uses high and low, personality uses strong and weak, and the summary uses ready and not ready. One scale, five labels, everywhere.

**Personality read as capability.** Recognise it when a personality fit label is used to explain a competency result. They are separate inputs on one scale, and inferring either from the other is unsupported and unfair to the person it is written about.

**Inventing the qualitative content.** Recognise it when a comment reads smoother than the others. People recognise their own words, and a paraphrase in a document with their name on it destroys trust in every number beside it.

**Flagging a gap and never having the conversation.** Recognise it when the flag appears in the dashboard and in no coaching plan. The flag is the start of a conversation, and it does more harm than good if it only ever appears in a table a manager reads.

**Circulating individual results as a league table.** Recognise it when the dashboard travels further than the coaching plans. Aggregate views for the team, individual views for the individual and their leader.

**Numbers that cannot be traced.** Recognise it when a challenged figure takes more than a minute to explain. Formulas throughout, and the response sheet in the same file.

## Edge cases

**A team of three or four.** Do not publish a ranking or a quadrant. Report per-area findings, the gaps, and the coaching plans, and say in the document that the group is too small for comparative reading.

**One leader only.** The leadership consensus is one opinion. Say so in the header of every table rather than in a footnote, and widen the gap threshold from 0.75 to 1.0 points on a one to four scale before flagging, since a single evaluator's calibration cannot be checked against anything and a stricter or more generous leader will otherwise flag half the team. Widen it, and record in the output that you did and by how much.

**Someone who is both assessed and an assessor.** Keep the roles separate in the data, and never let a person's evaluations of others touch their own scores. Where a team lead assesses peers, say so on the coverage line.

**A competency area with too few questions.** Fewer than three items is not an area mean, it is an item. Either merge it into an adjacent area, with the merge recorded in the framework file, or report it as a single indicator and exclude it from the overall.

**The instrument changed between cycles.** Do not compare the new scores to the old ones as though they were the same measurement. Report the new cycle standing alone, and where a trend is genuinely wanted, restrict it to the areas whose questions did not change.

**A person new in role.** Score them, and mark tenure on the dashboard. Three months in a new segment produces low scores that mean something entirely different from three years in it, and a reader without the tenure column will not make that adjustment.

**Works councils, unions, or a regulated jurisdiction.** Individual-level assessment data may be subject to consultation requirements before collection, not after. Confirm the position before the survey goes out, not before the report goes out.

**Nobody licenses a personality instrument.** Run competency alone. Do not substitute an unvalidated questionnaire found online, and do not infer traits from behaviour described in comments. The competency assessment is complete on its own; a fabricated personality component is worse than none.

## Quality bar

- The blended score, not the self score, drives every fit label and every ranking.
- Every figure in the workbook is a formula reading the response data, and one changed response moves everything downstream.
- The leader text-to-number mapping and the question-to-area mapping are recorded in the framework file, not applied ad hoc.
- Leader coverage is published per person, and single-evaluator scores are marked as such.
- Gaps above the stated threshold are flagged and appear in that person's coaching plan.
- Open-ended comments and any personality text are reproduced from source, never invented or paraphrased.
- One scale and one set of five labels throughout the report.
- Coaching objectives are presented as a data-grounded scaffold, with specifics agreed in the live conversation.

## Adapting this to your context

The five competency areas, the one to four scale and the 0.75-point gap threshold come from business-to-business sales teams of ten to forty people with two or more leaders evaluating. The framework file exists so all of it can change without touching the method.

- **The five areas.** They suit a named-account motion. A transactional or inbound team replaces executive communication and account management with qualification speed and multi-threading. A team selling into public sector procurement needs bid discipline and compliance as areas in their own right.
- **The scale and the gap threshold.** 0.75 assumes a one to four instrument. Convert proportionally, a quarter of the usable range, then check the flag rate on the first cycle: far outside a fifth to a third of the team means the threshold is wrong, not the team.
- **Two leaders per person.** With one leader, widen the threshold to 1.0 and publish the coverage count. Where peers or an account team evaluate instead, per-evaluator means go in every table.
- **The self-assessment.** It assumes people answer honestly because the exercise is developmental. Where the data touches pay or promotion, they will not, and the instrument should not be run.

- **What not to change.** The blended score drives every label, and every figure is a formula reading the response sheet.

## Related skills

`sales-call-analysis` supplies behavioural evidence from real calls, which is the strongest corrective to a self-assessment and the natural place to check an executive communication score. `sales-roleplay` drills the behaviours this assessment identifies, and its debriefs feed the next cycle. `demo-call-transcript-generator` provides common material when a team needs to be assessed against the same case rather than against their own deals. `hiring-scorecard-and-interview-kit` turns a validated ideal profile into a selection process for candidates. `annual-planning-and-headcount` consumes the capability picture when the question is how many people are needed rather than how good the current ones are. `pipeline-deep-dive` shows whether the strengths claimed here are visible in the deals.
