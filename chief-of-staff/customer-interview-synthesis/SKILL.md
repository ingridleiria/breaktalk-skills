---
name: customer-interview-synthesis
description: Turns a pile of customer, user or stakeholder interviews, call transcripts, survey responses and support tickets into findings that can carry a decision. Produces a coverage statement naming the gaps, a coded corpus where every tag keeps its verbatim, themes reported on both frequency and intensity, the contradictions and the absences rather than an average, five to eight findings each with counts, quotes, segment pattern and a confidence level, and implications tied to the decision the research serves. Use this skill when someone has interview notes and asks what they say, wants research synthesised, needs a findings readout, asks what customers told us, wants calls summarised, wants to move from anecdotes to evidence before a roadmap, pricing or positioning decision, or says everyone has a different view of what the customers want. Trigger for any qualitative input from more than two sources.
---

# Customer Interview Synthesis

Ten interviews produce roughly a hundred quotable moments and one or two findings. The distance between those two numbers is where the work is, and it is where most synthesis fails. The default failure is not laziness; it is that the person doing the synthesis already had a view before the first interview, and the corpus is large enough and varied enough to supply supporting quotes for almost any view someone brings to it. The output looks like evidence, reads like evidence, and is a prior belief with citations.

The second failure is the loudest interviewee. One articulate customer who described a problem vividly, at length, and with a memorable phrase will dominate a readout out of all proportion to how many people share the problem, because vividness is what survives in the analyst's memory between reading and writing. Whole roadmaps have been shaped by a single well-spoken participant nobody counted.

Both failures produce the same downstream cost. A team builds the wrong thing for two quarters, and because the decision was made on research it is harder to reverse than one made on instinct, since reversing it means admitting the research was wrong rather than that a guess was wrong. The method here is mechanical on purpose: counting, coding, and keeping the verbatim attached, so that the analyst's memory is not the instrument.

## When to use this, and when not to

Use it whenever there is qualitative input from more than two sources that has to support a decision: discovery interviews before a roadmap, win and loss interviews, churn conversations, onboarding research, pricing conversations, open-text survey responses, support ticket corpora, or user testing sessions.

Do not use it to design the research. What to ask, whom to ask and how many is upstream, and for anything that has to be defensible it belongs with `survey-and-instrument-design`. Synthesis cannot repair a sample that was chosen badly; it can only report the gap honestly.

Do not use it for a formally rigorous qualitative study with intercoder reliability, an audit trail and a published coding frame. That is `qualitative-coding-and-analysis`, and the difference is not thoroughness but reproducibility.

Do not use it to analyse one sales call, which is `sales-call-analysis`, or to build the competitive picture from loss interviews, which is `competitive-battlecard` consuming this method's output rather than replacing it.

Do not use it when the decision is already made and the research is being commissioned to support it. Say so instead. A synthesis produced to justify a settled decision is the most expensive kind, because it launders the decision as evidence and makes it unreviewable.

## What you need before starting

**Every source in full, not summaries.** Transcripts, notes, ticket text, open-text responses. Summaries have already had one round of unrecorded judgement applied, usually by the person who ran the interview and who was forming a view during it. Missing: work from what exists, and state in the coverage section that n sources were available only as summaries, since that limits what the counts mean.

**The decision this serves.** Roadmap prioritisation, pricing, positioning, a sales process change, or a strategy choice. The decision determines what a finding needs to be to be useful. Missing: ask, and if the answer is that there is no decision, say the synthesis will be descriptive and will not carry a recommendation. Research without a decision attached is a library, not an input.

**Participant metadata.** Role, segment, company size, industry, tenure, customer or prospect or churned, and who conducted the interview. Without it, segment patterns cannot be found and the counts mean less. Missing: reconstruct what you can from the customer system and mark the rest unknown, then state how many are unknown, because a segment claim resting on twelve of nineteen sources with segment data is a weaker claim.

**The team's prior hypotheses, written down before coding.** What people currently believe the research will show. This is the single cheapest safeguard in the method and it takes fifteen minutes. Missing: ask three people on the team what they expect to find, write it down, and date it. Its purpose is not to be disproved but to make its influence visible.

**The consent and confidentiality terms.** What participants agreed to, whether they can be quoted, whether attribution to a company is permitted. Missing: default to anonymised, segment-attributed quotes only, and do not name a company in any output until the terms are confirmed.

**A rough sense of who is missing.** The roles or segments not in the sample. Missing: derive it by comparing the participant list against the buying committee or the customer base, and put the answer in the coverage statement rather than discovering it at the readout.

## The method

1. **Write the coverage statement first, before reading for content.** Total sources, the breakdown by segment and role, the date range, the format mix, and the gaps in plain words: "nineteen sources, none from procurement, twelve of nineteen from a single industry, all interviews conducted by two people from the product team". Coverage determines what the synthesis is allowed to claim, and writing it first stops the claim inflating as the findings get interesting.

2. **Record the priors.** One line per hypothesis, with who holds it. Set it aside until step seven.

3. **Read every source in full before coding any of them.** Reading and coding simultaneously means the early codes shape what you notice later, and the first three interviews end up defining the frame for the remaining sixteen. One full pass first, taking no structured notes, is worth the time it costs.

4. **Code the second pass, tagging every meaningful statement.** Each tag carries four things: a theme code, created inductively as it appears rather than from a pre-set list; the source and its segment; the type of statement, which is one of a problem, a need, a workaround, a praise, a request, a decision criterion, a competitor mention or a willingness-to-pay signal; and an intensity, which is one of mentioned in passing, discussed at length, or described as decisive. The verbatim text stays attached to every tag without exception. The judgement call is how granular a code should be; the rule is that a code should be specific enough that you could tell from the code alone whether a new statement belongs in it, and that codes are merged later rather than being invented broad.

5. **Converge the codes into themes.** Expect fifteen to thirty codes on a corpus of this size, grouping into five to eight themes. The rule for merging: two codes merge when the statements under them would lead to the same decision. Two codes that sound similar but imply different actions stay separate, and that distinction is often the most valuable output of the whole exercise.

6. **Count on both dimensions, and never report only one.** For each theme: how many sources raised it, how many raised it unprompted, how many described it as decisive, and which segments it concentrates in. Frequency and intensity are different findings. A theme raised by three of nineteen but decisive for all three is a segment-specific blocker. A theme raised by fourteen in passing is a background irritation. Reporting either as "mentioned by n" collapses them into the same sentence and loses the decision-relevant part. The rule: every theme is reported as a pair, frequency and intensity, and the ordering is by intensity where they conflict.

7. **Look deliberately for four things the default reading misses.** Contradictions: sources or segments who said the opposite, which get explained by segment rather than averaged away, because the average is true of nobody. Absences: what nobody raised that the team expected, which is where the priors from step two earn their keep, and absence across nineteen sources is evidence rather than a gap. Workarounds: what people already do to cope, which is the most reliable indicator that a problem is real, because building a workaround costs effort and nobody spends effort on a problem they do not have. Language: the words participants use for the problem and for the product, which should become the organisation's words in positioning and interface copy.

8. **Write five to eight findings, each as a claim with its evidence.** The claim is one sentence stating what is true and for whom, with the segment in it: "Mid-market finance teams abandon onboarding when the first integration takes longer than a day" rather than "onboarding is hard". Then frequency and intensity with the counts, two or three verbatim quotes with segment attribution, the segment pattern, any contradiction, and a confidence level of high, medium or low based on coverage and consistency. The rule for confidence: high needs consistency across segments and enough sources to see the pattern break if it were absent; low is honest and useful, and a low-confidence finding stated as low is far more valuable than a medium-confidence finding stated as fact.

9. **Order findings by intensity and decision relevance, not by frequency.** The most-mentioned theme is often the least actionable, because everyone mentions the thing that is easy to talk about.

10. **Write implications as options with trade-offs, carrying the confidence forward.** For each finding, the two to four things the team could do, what each costs and gives up, and the confidence inherited from the finding. Never write implications as mandates; the researcher does not own the roadmap and a synthesis that instructs gets discounted by the people who do. Where the evidence does not support a decision the team wants to make, say that plainly and state what research would.

11. **Say what the next research should be, in one paragraph.** Which gap, which segment, how many, and what question. A synthesis that ends without this leaves the team to repeat the same coverage gap next quarter.

## Sample size, and what it entitles you to say

There is no threshold at which qualitative findings become quantitative, and the most common abuse of this work is a percentage. "Sixty percent of customers said" from a sample of ten is a sentence that will be repeated in a board meeting as though it described the customer base, and it does not.

The honest formulations: n of nineteen sources raised this; this was decisive for four of the six mid-market participants; nobody in the sample mentioned it. Counts with the denominator visible, every time.

What different sizes support. Under about eight sources: directional signals and hypotheses to test, no segment claims. Roughly eight to fifteen: themes and segment patterns where a segment has four or more sources, with confidence marked medium at best. Fifteen to thirty: reasonably stable themes, defensible segment comparisons where each segment has five or more, and the ability to treat an absence as meaningful. Above thirty, the constraint stops being sample size and becomes coding consistency, which is where `qualitative-coding-and-analysis` and its reliability checks belong.

Saturation, the point where new sources stop producing new codes, is worth tracking as you code. Record the source number at which the last new theme appeared. Where new themes were still appearing at the last source, the sample is too small for the claims being made, and that is itself a one-line finding.

## Worked example

**Situation.** A company selling inventory software to independent retail chains had twenty-three sources on why customers stopped expanding after their first three sites: fourteen interviews across nine customers, six open-text survey blocks and three sets of support tickets. The product leadership team was two weeks from a roadmap decision and had a working theory that the blocker was the mobile stocktake experience, which had the most support tickets and had been raised loudly in a customer advisory session.

**Task.** Produce findings that could carry the roadmap decision, or say clearly that they could not.

**Action.** The coverage statement was written first and was uncomfortable. Twenty-three sources, but the nine interviewed customers were all in the 4 to 12 site band, none above; two of the nine accounted for six of the fourteen interviews; and every interview had been conducted by the same product manager, who held the mobile stocktake hypothesis. The last point went in the readout.

Priors were recorded from four team members. Three named mobile stocktake. One named pricing.

The full read took a day and a half. Coding produced 31 codes converging into 7 themes. Mobile stocktake was real: raised by 12 of 23 sources, which was the highest frequency in the corpus. But only 2 described it as decisive, and both were single-site franchise operators rather than expanding chains. The intensity split was the finding.

The theme that carried the decision had a much lower frequency. Six of 23 raised the difficulty of transferring stock between sites without a central view, and all six described it as decisive, using words like "we stopped" and "we could not". All six were in the 7 to 12 site band. Below seven sites nobody raised it, which made sense once stated: the problem does not exist until there are enough sites to move stock between.

The wrong turn: the first draft reported themes ranked by frequency, which put mobile stocktake at the top with 12 mentions and inter-site transfer fifth with 6. That draft was shown to two team members and both read it as confirming the mobile hypothesis, because the ranking is what people read. Rewriting the readout to lead with intensity and to present every theme as a frequency-and-intensity pair changed how both of them read the same data. Nothing in the underlying counts changed; the ordering was doing the persuasion, and it had been doing it in the wrong direction.

Two contradictions were reported rather than averaged. On pricing, four sources said the per-site model was the reason they stopped and three said it was the fairest thing about the product. The split was clean by segment: the four were seasonal operators with sites that closed for part of the year. Averaging those seven into "views on pricing are mixed" would have hidden a specific, addressable and previously unnoticed problem.

One absence was reported. The team had expected integration with a widely used accounting package to appear. It appeared in none of the 23 sources, which given the coverage was weak evidence rather than none, and the honest statement was that it was not a spontaneous concern in this sample, not that it did not matter.

**Result.** Six findings, four medium confidence and two low, with the low ones marked and the reason given. The roadmap decision moved inter-site stock transfer to the next quarter and kept mobile stocktake in the following one rather than cancelling it, on the reasoning that high frequency and low intensity describes something worth fixing but not worth fixing first.

The follow-up research question was specific: eight interviews with chains above twelve sites, conducted by someone who did not hold the hypothesis, since the coverage gap above twelve sites made the whole synthesis silent about the segment the company most wanted to grow into.

Fourteen months later the transfer work had shipped and expansion beyond three sites had improved, though a pricing change shipped in the same period and the two cannot be separated cleanly.

### A second scenario, where it goes differently

Five churn interviews, conducted over three weeks after five customers left in a quarter, with a leadership team wanting an explanation on Friday.

Five sources cannot carry themes, segment patterns or confidence levels, and pretending otherwise is the failure. The method compresses to what five sources can actually support, and the shape of the output changes rather than shrinking.

Code and count as normal, but report as five individual accounts side by side rather than as themes, with a short section on what the five have in common and an explicit statement that a commonality across five is a hypothesis, not a finding. No percentages, no confidence levels, no segment claims. The workaround signal becomes disproportionately valuable here, because it is the one indicator that does not need volume to mean something: a customer who built a spreadsheet to work around a gap has demonstrated the gap costs them more than the spreadsheet.

The most important output at this size is the research design for the next round, and the honest sentence to the leadership team is that five interviews tell you what to ask twenty people.

What changed: coverage collapsed, so the claims collapsed with it. What did not change: full reading, verbatims attached, contradictions reported, and the prior written down first.

## Output

**Coverage statement**, a quarter page, before anything else:

| Dimension | Detail |
| Sources | 23 total: 14 interviews across 9 customers, 6 survey blocks, 3 ticket sets |
| Date range | March to May |
| Segments present | 4 to 12 sites |
| Segments absent | Above 12 sites; no franchise operators; no procurement roles |
| Concentration | 2 customers account for 6 of 14 interviews |
| Conducted by | One product manager, who held one of the recorded priors |
| Saturation | Last new theme appeared at source 17 |

**Theme table:**

| Theme | Sources raising | Unprompted | Decisive for | Concentrated in | Contradicted by |

**Findings**, five to eight, each in this shape:

```
FINDING [n]  [One sentence: what is true, for whom]
Frequency    [n of N sources, m unprompted]
Intensity    [decisive for n, at length for m, in passing for k]
Segment      [where it concentrates, and where it is absent]
Contradiction[who said the opposite, and the explanation]
Confidence   [high / medium / low, and why]
Evidence
  "[verbatim]"  [segment, source id]
  "[verbatim]"  [segment, source id]
```

**Contradictions and absences**, as their own short section, because they are the parts a summary drops.

**Implications:**

| Finding | Option | What it costs | What it gives up | Confidence carried |

**Next research**, one paragraph: the gap, the segment, the number, the question.

## Failure modes

**The prior with citations.** Recognise it when every finding matches what the team believed beforehand and the quotes are all vivid. Fix by recording the priors first and checking each finding against them at the end, explicitly asking which finding would have surprised the team.

**The loudest interviewee.** Recognise it when one source supplies three or more of the quotes in the readout. Fix by counting quotes per source and rebalancing; if only one person said it well, the finding rests on one person.

**Sampling the transcripts.** Recognise it when the analyst read the first four in full and skimmed the rest, which is invisible in the output and detectable only by asking. This is the failure the whole method exists to prevent. There is no fix but reading.

**Percentages from small samples.** Recognise it in any sentence with a percent sign and a denominator under thirty. Replace with counts and the denominator, every time.

**Averaging a contradiction.** Recognise it in the phrase "views were mixed". Fix by finding the variable that splits the group. There nearly always is one, and it is usually the most useful thing in the corpus.

**Frequency ordering doing the persuading.** Recognise it when the readout is ranked by mention count. Reorder by intensity and decision relevance, and present both numbers on every theme.

**Quotes tidied up.** Recognise it when every quote is grammatical. Fix by restoring the verbatim; light trimming with ellipses is acceptable, rewriting is not, and a quote that has been improved is no longer evidence.

**Implications written as instructions.** Recognise it when a finding is followed by a single course of action with no alternatives. The people who own the decision discount it, and rightly.

## Edge cases

**Fewer than six sources.** Report as individual accounts side by side, with the commonalities labelled as hypotheses. No themes, no confidence levels, no segment claims.

**All the interviews were run by one person who held a hypothesis.** Report it in the coverage statement as a limitation. Where possible, have someone else code independently and compare the code lists before merging; the divergence is informative.

**The sample is entirely happy customers.** Common, because happy customers accept interview requests. State it, and treat the absence of complaints as an artefact of the sample rather than a finding. Churned and lost accounts are a different corpus and usually need a different recruiter.

**Support tickets mixed with interviews.** Tickets are self-selected, skew to problems, and carry no counterfactual. Count them separately, never pooled with interview counts, and use them to test whether an interview theme appears at volume rather than to establish a theme.

**Participants can be identified from their quotes even when anonymised.** In a small market a role plus a company size identifies a person. Aggregate the attribution further, or paraphrase with the paraphrase marked as such, and check with the participant where the quote is consequential.

**The findings contradict a decision already announced.** Deliver them anyway and separately from the recommendation, so that the evidence is on the record even if the decision does not change. Softening findings to fit an announced decision is the failure that ends the credibility of every future synthesis.

## Quality bar

- The coverage statement names the gaps and the concentrations, and appears before the findings.
- Every finding carries frequency, intensity, quotes with segment attribution, and an explicit confidence level.
- Every count shows its denominator, and no percentage appears from a sample under thirty.
- Contradictions are explained by a variable rather than averaged, and absences are reported.
- Every source was read in full, and every tag kept its verbatim.
- The team's priors were written down before coding and are checked against the findings.
- Implications are options with trade-offs, carrying the finding's confidence.
- The next research question is specific enough to recruit against.

## Related skills

`survey-and-instrument-design` designs the research this synthesises, and is where a sample that cannot carry the decision should be fixed. `qualitative-coding-and-analysis` is the formal version with a published coding frame and reliability checks, for findings that must be reproducible. `market-research` places these findings against market and category evidence. `competitive-battlecard` consumes the loss and competitor mentions coded here. `pipeline-deep-dive` supplies the deal records that give interview claims a quantitative counterpart. `decision-memo` is where the implications become a decision with a named decider. `pricing-and-resourcing-model` takes the willingness-to-pay signals, which this method flags but does not size. `sales-call-analysis` handles a single call rather than a corpus.
