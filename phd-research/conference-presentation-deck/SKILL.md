---
name: conference-presentation-deck
description: Builds a research talk that leads with the finding, fits the slot with time left for questions, gives the identification evidence a full slide, and survives a hostile question period, and delivers the deck, the appendix, the timed script and an anticipated-questions sheet with the slide to point to for each answer. Enforces the rule that slide titles are sentences carrying the argument, that the number appears in the first minute and the last, and that figures are readable from the back of a room in monochrome. Use this skill when someone asks to turn a paper into slides, prepare a seminar or conference talk, build a job-market talk, make a poster, present at a lab meeting, or rehearse a presentation, and whenever an existing deck opens with a literature review instead of a result. Trigger also on vague requests such as "I have twelve minutes", "how do I explain this to a general audience", "my talk runs long", or "what will they ask me".
---

# Conference Presentation Deck

A paper is read by one person at a time, at their own pace, with the ability to turn back. A talk is received once, by a room, at your pace, by people who are also thinking about their own work and their lunch. Those are different media and the near-universal failure is to treat the second as a compressed version of the first: the paper's section order preserved, the literature review at the front, the equation shown before the audience knows why anyone should care, and the result arriving at minute eleven of a twelve-minute slot, to a room that stopped listening at minute three.

The cost is concrete. A conference talk is often the only exposure your paper gets to the twenty people in your field who could cite it, referee it, invite you somewhere, or hire you. A talk that buries the finding produces no questions, no follow-up, and no memory of the paper. A talk that overruns is cut off before the conclusion, which means the audience leaves with the setup and not the result. A job-market talk that cannot survive the third interruption ends a candidacy.

The specific failure this skill prevents is a room that never learns what you found. Everything else in the method is downstream of that.

## When to use this, and when not to

Use it for any spoken presentation of research: a conference session, a departmental seminar, a workshop, a job-market talk, a lab meeting update, a policy briefing, a poster. Use it when a deck already exists and runs long, opens with a literature review, or has produced silence in the question period. Use it when the same paper has to be given at twelve minutes and again at ninety, which is two different talks from one paper and not a matter of adding slides.

Use it to build the defence talk for a viva, taking the sizing and structure from here while the question preparation and the committee dynamics belong to `thesis-defense-prep`.

Do not use it to decide whether the paper's claims survive scrutiny, which has to happen before the talk is built; that is `peer-review-simulator` for the paper as a whole and `identification-defense` for the design. A polished talk about an indefensible result is worse than a rough one, because it draws attention. Do not use it to build the figures themselves; that is `academic-figures-monochrome`, and this skill only specifies what the talk needs from them. Do not use it to write the paper's abstract, which is a different compression with different rules; that is `abstract-and-title`.

Do not use it for a general public talk with no technical audience. The structure holds but the identification section, which is a third of the value here, has no audience there.

## What you need before starting

**The finished paper, or at minimum the main result with its number and unit.** A talk cannot be built before the finding is known, and the attempt produces a deck that hedges for twenty minutes. Missing: build the identification and setting slides, which are stable, and stop. Do not construct a talk around a result that might move.

**The slot length, and whether it includes questions.** This determines everything and is the fact most often assumed rather than checked. A twenty-minute slot including questions is a twelve-minute talk. Missing: ask the organiser. Where no answer is available, build to the shorter interpretation, because finishing early costs nothing and overrunning costs the conclusion.

**Who is in the room.** A field seminar, a general economics audience, a mixed policy and academic room, or a committee. This decides how much of the setting has to be explained and which objections will actually be raised. Missing: assume a mixed audience of competent researchers who do not know your setting, which is the safest default and the one that most talks wrongly assume away.

**The venue's format constraints.** Aspect ratio, whether a template is required, whether the room projects in colour and how well, whether slides are distributed to a discussant in advance. Missing: build 16:9, monochrome-safe, and self-contained.

**Whether there is a discussant.** A discussant reads the paper and prepares an attack, which changes the appendix from a convenience into a requirement. Missing: ask the organiser; conference sessions in some fields always have one.

**The identification evidence as an exhibit, not as a paragraph.** The pre-trend plot, the first stage, the density test, the balance table. Missing: build it before building the talk, because if the identification evidence cannot be shown in one figure, the audience will not believe the result, and that is a paper problem rather than a slide problem.

## The method

1. **Write the one sentence the room should be able to repeat afterwards.** Question and answer with the number and the unit: "A student finance reform raised four-year completion by 6.8 points, concentrated entirely among first-generation students." Everything in the deck either supports this sentence or is cut. Write it down before opening any slide software; a deck built without it will be organised by the paper's section order by default.

2. **Size the talk to the slot** using the table below, and set the slide count as a ceiling rather than a target. One slide per minute is the maximum sustainable rate and most good talks run slower.

3. **Order the deck by the structure below**, which is not the paper's order. The finding comes first. The literature comes third and briefly. The identification evidence gets a full slide and a full minute, in the middle, before the main result.

4. **Write the slide titles as sentences before making any slide.** Not "Results" but "The effect is concentrated in the bottom two income terciles". Then read the titles alone, in order. If they do not tell the whole argument, the deck's structure is wrong and no amount of content will fix it. This test takes two minutes and it is the highest-yield step in the method.

5. **Build each slide to one idea.** Where a slide contains two, split it. Where a slide contains an idea and a decoration, delete the decoration. Text at 24 point or larger, no paragraphs, no more than about five lines.

6. **Build the figures for a room, not for a page.** Larger fonts than the paper's, thicker lines, legend outside the plot area so it cannot cover a data point, series distinguished by marker shape and dash pattern and texture rather than by colour, and a single accent used at most once to mark the estimate that matters. A figure that depends on colour will fail on the third projector you meet, and it excludes part of any large audience.

7. **Write the script in speaking sentences and time it aloud.** Not bullet notes. What you will actually say, on each slide, with the number said out loud where it appears. Timing it in your head produces an estimate low by twenty to thirty percent, reliably, because silent reading skips the pauses.

8. **Cut to the slot with a margin of about fifteen percent.** Talks run long, never short. The cut is made from the setting and the literature, in that order, and never from the identification evidence or the main result. If the talk still does not fit, the claim is too broad for the slot and should be narrowed rather than accelerated.

9. **Build the appendix from the questions sheet**, one slide per anticipated question, each reachable by a number you can state aloud: "That is on slide 34." Being able to show the answer rather than describe it converts a challenge into a demonstration, and the audience sees that the objection was anticipated.

10. **Rehearse the first ninety seconds until it is automatic**, and the answers to the three hardest questions until they fit in sixty seconds each. The opening is where nerves do the most damage and the questions are where the talk is actually judged.

## Sizing the talk to the slot

| Slot | Talk length | Slides, ceiling | What survives the cut |
| 12 to 15 min, conference session | 10 to 12 min | 10 to 12 | Finding, setting in one slide, design in one, identification evidence, main result, implication |
| 20 to 25 min, workshop | 18 to 20 min | 15 to 18 | The above plus one mechanism or heterogeneity slide and a robustness summary |
| 45 to 60 min, seminar | 40 to 45 min | 25 to 32 | The above plus literature, data construction, and room for interruption |
| 75 to 90 min, job talk | 55 to 65 min | 30 to 40 | The above, built to be interrupted from the third slide onward |
| Poster | 3 min read | One panel | Question and answer in the title, one identification figure, one result figure |

In a seminar or job talk, assume the talk will be interrupted and that the interruptions will consume between a fifth and a third of the time. Build so that the main result is reached by the halfway point even after interruption; a job-market talk that has not shown its result by minute forty is in trouble regardless of how good the setup was.

## The deck structure

1. **Title slide, then the finding.** Slide one or two states the question and the answer with the number. The audience decides in the first minute whether to listen properly, and this is the only chance to give them a reason.
2. **Why it matters.** One slide, the problem in the world, one number with its source.
3. **What was known and what was not.** One slide, two or three closest papers, framed as what their designs could not establish. This is not a literature review and it should take under ninety seconds.
4. **Setting and data.** The institution, the policy, the years, the units, the sample size, readable in twenty seconds. A timeline of the policy where the rollout matters.
5. **Design.** The source of variation in words first, then the estimating equation once, then the identifying assumption in one sentence. One or two slides. The words come before the equation because an audience that has not understood the variation cannot read the equation.
6. **Identification evidence.** A full slide and a full minute: the pre-trend plot, the first stage, the density test, or the balance table. This is where the informed part of the room decides whether to believe anything that follows, and rushing it saves forty seconds at the cost of the whole talk.
7. **Main result.** One figure, or one table with the relevant column highlighted and the rest greyed. The magnitude translated into interpretable units on the slide itself, not just spoken.
8. **Mechanism or heterogeneity.** One slide each, only where the evidence actually establishes them.
9. **Robustness.** One slide summarising what was varied and that the conclusion held. Details in the appendix.
10. **What it means.** One slide, the implication sized to the evidence and no larger.
11. **Conclusion.** The finding restated with the number, and the contribution in one line. End on the finding, not on thanks or on future work; the last slide stays up during the entire question period and should therefore be the sentence you want the room looking at.

## The questions sheet

Fifteen to twenty questions for a seminar, ten for a conference slot, forty or more for a job talk. Sources: the attack list from `identification-defense` for the design in use, the concerns `peer-review-simulator` raised on the paper, the setting-specific objections a field expert would make, and the two or three questions the talk itself seems designed to avoid, which are the ones that will be asked.

Each entry: the question in the words someone would actually use, a two-sentence answer, and the appendix slide number.

The rule for the answers: concede first where a concession is due. "Yes, that is the main limitation, and the bias runs downward, so the estimate is conservative" is a stronger answer than three sentences of defence, and rooms respond to it visibly. An answer that begins by defending, when the objection is correct, invites a second question from the same person.

Answers are under sixty seconds. A long answer signals uncertainty regardless of its content, and it eats the question period so that fewer people get to engage, which is the opposite of what a talk is for.

## The poster variant

Question and answer in the title. Left column: setting, data, design. Centre: the identification figure and the main result figure, both large. Right: magnitude, mechanism, implication. Under 300 words of body text in total, which is far less than feels possible and is the entire discipline of a poster. A link or code to the paper. Prepare a spoken thirty-second version and a spoken three-minute version, because those are the two lengths people actually ask for at a poster session.

## Worked example

**Situation.** A doctoral candidate, Tomás Iglesias, had fifteen minutes at a field conference to present a paper on whether a municipal childcare expansion raised maternal employment. Administrative records, 214 municipalities, staggered rollout over seven years, headline estimate of 4.9 percentage points on maternal employment with a standard error of 1.4, and a substantial heterogeneity result: the effect was 8.2 points for mothers with a single child and near zero for mothers with three or more. His existing deck had 24 slides and had been built by exporting the paper's sections.

**Task.** A twelve-minute talk, with three minutes of questions, that left the room knowing the number and believing the design.

**Action.** The one sentence was written first, and writing it exposed a decision that had been avoided in the paper: was the talk about the average effect or about the heterogeneity? The heterogeneity was the more interesting finding and the average effect concealed it. The sentence became: "Childcare expansion raised maternal employment by 4.9 points, but almost all of it came from mothers with one child, which tells us the constraint is the first child rather than childcare cost in general."

The title test then destroyed the existing deck. Read in order, the 24 titles were: Motivation, Literature, Contribution, Institutional Background, Institutional Background 2, Data, Sample, Descriptive Statistics, Empirical Strategy, Identification, Results, Results 2, Heterogeneity, Robustness, Robustness 2, Conclusion. That sequence tells nobody anything. Rewritten as sentences, the deck came to eleven slides and the titles alone read as an argument.

The cut was severe. Four slides of institutional background became one, holding a timeline of the rollout and three facts. Two slides of descriptive statistics were deleted entirely and moved to the appendix; nobody in a twelve-minute talk needs a means table. The literature slide went from nine papers to three, framed as what their designs could not separate.

**The wrong turn.** The first rebuild put the identification evidence in the appendix to save time, on the reasoning that a twelve-minute conference audience would not scrutinise it. The rehearsal killed this: a colleague sitting in asked, at the main result slide, how he knew the municipalities that expanded early were not different. Without the event study on screen, the answer took ninety seconds of talking and did not land. The event study came back into the main deck, at a full slide, and the robustness summary went to the appendix instead. The talk was the same length and considerably more convincing. The lesson generalises: the identification slide is the last thing to cut and the first thing people want to cut, because it feels like preamble to the author and it is the evidence to everyone else.

The figures were rebuilt for the room. The event study had been a colour plot with a legend inside the panel covering the period immediately before treatment, which was the exact region the audience needed to see. It became monochrome, with hollow circles and solid capped intervals, the legend beneath the panel, a dashed vertical line at the treatment period, and font sizes roughly doubled. The heterogeneity result became a coefficient plot with three rows rather than a six-column table.

The script timed at 13 minutes 40 seconds on the first read-aloud, against a silent estimate of eleven. Two sentences came out of the setting slide and one example came out of the mechanism discussion, bringing it to 11 minutes 20 seconds, which left a margin.

The questions sheet had sixteen entries. Three came from the identification attack list, four from the setting, and two were the ones the talk avoided: why the effect for larger families was zero when the childcare places were available to them, and whether the employment measure captured informal work.

**Result.** The talk ran 11 minutes 50 seconds. Six questions, of which four were on the sheet, including both of the avoided ones. The informal work question was answered by showing appendix slide 19, which held a comparison against a household survey measure; the answer took forty seconds and ended the line of questioning. A researcher from another university asked for the paper afterwards and later cited it.

The one question not on the sheet was about whether municipalities that expanded early were also expanding other family policies at the same time, which was a real gap and became a robustness check in the next draft. That is the second thing a conference talk is for.

### A second scenario, where it goes differently

The same paper as a 90-minute job-market talk. Almost nothing carries over except the figures.

The finding still comes first, but the audience will interrupt from slide three onward and the deck has to be built to absorb it. The institutional background expands from one slide to four, because the committee will test whether the candidate understands the setting rather than only the estimator. The identification section triples: the event study, a test of the rollout's determinants, a discussion of the estimator's behaviour under staggered adoption with heterogeneous effects, and a slide on what the design cannot rule out. The appendix goes from six slides to about thirty-five, indexed, with the numbers memorised for the ten most likely questions.

The pacing rule changes entirely. In a conference talk the objective is to finish. In a job talk the objective is to reach the main result by the halfway point with the room still engaged, and then to demonstrate depth under interruption for the second half. A candidate who defends the pace against interruption in order to reach the last slide has misread what is being assessed: the questions are the interview.

One thing that does not change is the sentence. If the candidate cannot state the finding in one sentence with a number, ninety minutes will not help.

## Output

Delivered together:

**The deck**, built with whatever presentation tooling is available in the environment, following the slide rules above. Where no presentation tool is available, deliver the slide-by-slide specification: slide number, sentence title, the exhibit or content, and the source of the exhibit.

**The appendix**, numbered continuously with the main deck so slide numbers can be stated aloud.

**The script**:

| Slide | Title, as a sentence | What is said | Elapsed time |

**The questions sheet**:

| # | Question, in the words it will be asked | Answer, two sentences, concession first | Appendix slide |

**The one-slide summary** for a discussant, a hallway conversation, or a follow-up email.

## Failure modes

**The paper's order.** Recognise it when the deck's titles are section names. Rewrite every title as a sentence and reorder around the finding.

**The result at the end.** Recognise it when the main number first appears after the halfway point. Move it to slide one or two and use the rest of the talk to justify it.

**The literature review at the front.** Recognise it when slides two through five are about other people's papers. Three papers, one slide, framed as what they could not do.

**Silent timing.** Recognise it when the estimate came from reading slides in your head. Time it aloud, standing, once.

**The identification slide cut for time.** Recognise it when robustness survived and the pre-trend plot did not. Reverse the decision.

**Colour-dependent figures.** Recognise it by printing one slide in greyscale. If two series become indistinguishable, rebuild with markers, dash patterns and texture.

**Legends inside the plot.** Recognise it when the legend covers any data region. Move it outside, below or beside.

**Reading the slides aloud.** Recognise it when the script and the slide text are the same words. The slide carries the claim, the speaker carries the argument.

**Equations before variation.** Recognise it when the estimating equation appears before the audience knows where the variation comes from. Words first, always.

**No appendix.** Recognise it when the answer to a foreseeable question has to be described rather than shown. Every question on the sheet gets a slide.

**Ending on acknowledgements or future work.** Recognise it because the last slide is what the room looks at for the entire question period. End on the finding.

## Edge cases

**The result is null.** Lead with it anyway, and lead with the power: "We can rule out effects larger than 1.2 points." A null presented as an absence produces a room that thinks the study failed; a null presented with its confidence interval and its minimum detectable effect is a finding.

**The work is preliminary.** Say so on slide one, state what is done and what is not, and ask the room for the specific input you want. A talk that presents preliminary work as finished invites the wrong questions and wastes the best resource in the room.

**A discussant has the paper in advance.** Build the appendix first and send the slides early where the format allows. The discussant's attack is usually the paper's real weakness, and the appendix slide that answers it, shown during the discussion, is the strongest possible response.

**Fifteen minutes for a paper that needs forty.** Do not compress; narrow. Present one chapter of the argument properly and say that the rest is in the paper. A compressed forty-minute talk delivers nothing at all.

**A hostile senior person in the room who has a competing paper.** Prepare the specific comparison as an appendix slide, concede what is genuinely better about their design, and state precisely what your design does that theirs cannot. Do this in under a minute, in the answer, and then move on without arguing further.

**The projector fails or the room is very large.** Have the one-slide summary as a printout and know the talk well enough to give it from the sentence alone. This happens more than it should.

**Remote or hybrid delivery.** Slides carry more of the load because the speaker is a small rectangle. Increase font sizes, reduce content per slide further, state slide numbers aloud, and pause deliberately for questions, because remote audiences will not interrupt.

**The same talk twice in a week to different audiences.** Rebuild the setting slides and the literature slide, keep everything else. Those two are what differ between a field audience and a general one.

## Quality bar

- The finding, with its number and unit, appears on slide one or two and on the final slide.
- Reading the slide titles alone, in order, gives the whole argument.
- The identification evidence has a full slide and a full minute in the main deck, not the appendix.
- The talk was timed aloud and fits the slot with about fifteen percent of margin.
- Every figure is legible in monochrome from the back of a room, with the legend outside the plot area.
- Every anticipated question has a two-sentence answer that concedes first where a concession is due, and an appendix slide number.
- No slide carries more than one idea, and no slide carries a paragraph.
- The deck ends on the finding rather than on thanks or future work.

## Related skills

`identification-defense` supplies the identification evidence the talk shows and the attack list the questions sheet is built from. `peer-review-simulator` supplies the referee concerns that will surface as questions from the room. `academic-figures-monochrome` builds the exhibits to the projector standard this skill requires. `abstract-and-title` is the written compression of the same finding and should agree with the talk's opening sentence exactly. `thesis-defense-prep` uses this skill to build the defence talk and adds the committee dynamics and the rehearsal discipline. `analysis-audit` is what guarantees that the number spoken from the slide is the number in the paper, which matters more here than anywhere else because a talk is where a discrepancy gets asked about in public. `thesis-advisor` decides whether a conference is worth the week it will cost. `journal-targeting` often follows a conference, because the questions asked in the room are the referee reports arriving early and free.
