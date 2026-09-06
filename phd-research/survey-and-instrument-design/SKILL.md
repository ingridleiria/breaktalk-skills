---
name: survey-and-instrument-design
description: Designs a survey or measurement instrument that produces data worth analysing, and catches the errors that cannot be repaired after fielding. Enforces constructs defined before any question is written, a blueprint mapping every item to a hypothesis and every hypothesis to items, validated scales preferred over invented ones, wording free of leading, double-barrelled, negated and socially desirable formulations, response scales chosen deliberately and used consistently, order and routing controlled and recorded, translation by back-translation with separate piloting per language, cognitive interviews before a live pilot, and a sampling and non-response plan written before fielding. Use this skill when writing a survey or questionnaire, adapting or shortening an existing instrument, translating one, designing the measures for an experiment, adding a module to an existing panel, reviewing somebody else's draft instrument, or diagnosing why a fielded survey produced data nobody can use. Trigger also on vaguer requests such as "can you look at my questionnaire", "how many points should this scale have", "why did so many people drop out at question 12", or "we need to ask people about this".
---

# Survey and Instrument Design

A badly written question returns a number, and the number is indistinguishable from a good one. There is no diagnostic that recovers it, no estimator that corrects it, and no robustness check that reveals it. That is the whole problem. Measurement error introduced at the design stage is invisible in the output, fatal to the conclusion, and irreversible once the field period closes, because the respondents are gone and the money is spent.

The costs are concrete and they compound. A double-barrelled item produces a variable that correlates with everything weakly and with nothing interpretably, and it usually survives into the analysis because nobody wants to drop the only measure of a construct in the hypotheses. A leading question produces a distribution that supports the hypothesis and cannot be defended when a referee reads the questionnaire, which they will, because it is in the appendix. A twenty-eight minute instrument produces straight-lining in its final third, which looks like consistency and is actually abandonment. And a construct that was never defined produces an argument in the results section about what the variable means, six months after the last respondent was paid.

The order that prevents all of this is: define what you are measuring, find out how it has been measured before, then write questions, then find out what respondents think the questions mean, then field. Writing questions first is the most common mistake in applied research and it produces an instrument nobody can interpret, including its author.

## When to use this, and when not to

Use it when writing any instrument that will generate data for analysis: a standalone survey, a questionnaire module inside an existing panel, the measures attached to a field or laboratory experiment, an interview schedule with closed items, an observation protocol with coded categories, or an administrative form being repurposed as a research instrument.

Use it when adapting an existing instrument, which people treat as a small job and which is not: shortening a validated scale, changing its reference period, or moving it to a new population all break the validation and require the same care as writing new items.

Use it when a survey has already been fielded and produced unusable data, because the diagnosis is a design review and it determines whether the data can be salvaged, whether a subset of items is usable, or whether the fielding has to be repeated.

Do not use it for a purely open-ended interview guide with no closed items, where the design logic is different and the analysis is `qualitative-coding-and-analysis`; that skill also handles the coding of open-ended survey responses this instrument generates. Do not use it to write the ethics application, the consent form or the participant information sheet, which are `research-ethics-and-data-protection`, although the instrument has to be attached to the application and its content drives most of the risk assessment. Do not use it to decide the research design or the identification strategy, which is `research-design`; the instrument implements a design and cannot rescue one. Do not use it to fix the analysis plan for the resulting data, which is `preregistration-and-analysis-plan`, or to profile and clean the fielded data, which is `data-profiling-and-cleaning`.

The boundary in one line: `research-design` decides what has to be measured, this skill decides how, and `data-profiling-and-cleaning` finds out what actually arrived.

## What you need before starting

**The hypotheses, written out.** Every item exists to serve one. Missing: extract them from whatever exists, write them as sentences with a direction, and get them confirmed before drafting items, because an instrument built without hypotheses is a fishing expedition that costs the same as a study.

**The target population and how respondents will be reached.** The mode determines almost everything about the design: what a person can be asked to do on a phone differs from a self-completed web form, which differs from an interviewer-administered household visit. Missing: design for the most constrained plausible mode, because an instrument built for web and fielded by phone loses its grids, its long response lists and its visual anchors.

**The available time per respondent, and who decided it.** Missing: assume twelve to fifteen minutes for a general population self-completion, and treat that as a hard budget rather than an aspiration.

**Whether the study joins an existing survey or panel.** If so, the item slots, the house style and the existing measures constrain everything. Missing: ask for the previous wave's questionnaire, which is the single most useful document, since repeating an existing item exactly buys comparability that no new item can.

**Any measures the analysis requires as controls or as sample descriptors.** Missing: derive them from the analysis plan; if there is no analysis plan, that is the more urgent problem.

**The languages the instrument will be fielded in, and who will translate.** Missing: establish this before drafting, because items written in an idiom that does not survive translation have to be rewritten rather than translated, and finding that out at translation stage costs a redesign.

**Access to five to ten people from the actual population for cognitive interviews.** Missing: use the closest available proxy, state the difference, and treat their feedback as weaker evidence. Never skip this step entirely; three interviews with imperfect participants beats none.

**The ethics approval status and timeline.** Missing: assume the instrument must be final before submission, which is usually true, and build the pilot into the pre-submission schedule rather than after it.

## The method

1. **Define every construct before writing anything.** For each quantity in the hypotheses: what it is, at what level it exists, over what period, and what would count as more or less of it. "Job satisfaction" is not a construct until you have said whether you mean satisfaction with the role, the employer or the career, whether it is a momentary state or a stable disposition, and whether it is a single dimension or several. The judgement call is how many dimensions to admit, and the rule is to admit only the dimensions the hypotheses distinguish between, because every additional dimension costs items and the items come out of the time budget.

2. **Search for an existing validated instrument, and prefer it even when it is imperfect.** Three reasons, and each is worth more than the elegance of your own wording: its measurement properties are already known, its results are comparable to other work, and referees do not have to take your word for it. Search the literature and the archives of large panel studies, which publish their questionnaires. The rule for choosing between two candidates: prefer the one used in your population over the one with better psychometrics in a different population, because population fit is harder to argue back than a reliability coefficient.

3. **Decide what to do when nothing suitable exists, explicitly.** Three options, in order of preference. Adapt an existing instrument and document every change with its reason. Use a short form or a subset of a validated scale, reporting reliability in your own data and acknowledging that a subset is not the validated instrument. Or write new items, in which case treat the measure as something to be validated within the study rather than assumed: plan the factor structure check, the reliability estimate, and, where possible, a convergent measure to correlate against.

4. **Build the blueprint before writing item wording.** A table with one row per item: the construct, the hypothesis it serves, the item's source, whether it is original or adapted, its scale, and its role in the analysis. Then read it in both directions. Every hypothesis must have items; every item must have a hypothesis. Items that belong to nothing are what make questionnaires long and analyses vague, and they are always defended on the grounds that the data might be useful later. The rule: cut them, and if the sponsor insists, put them in a clearly labelled optional block at the end where their dropout cost is contained.

5. **Write the items, one idea each.** "Was the service fast and friendly" cannot be answered by a person who found it fast and rude, and their answer is noise indistinguishable from signal. Neutral wording: a question that signals the expected answer will get it, so ask how a person would describe something rather than how satisfied they were with it, when satisfaction is what you are trying to measure rather than assume. Concrete beats abstract: "how many times in the last thirty days" is answered from memory, "how often, generally" is answered from self-image. Match the reference period to what people can recall, which for most behaviour is about a month, beyond which recall becomes reconstruction of a rate. Avoid negations, and never double ones. Avoid any word the respondent would not use unprompted.

6. **Handle social desirability deliberately wherever the topic invites it.** Income, effort, prejudice, adherence, health behaviour, compliance, and anything the respondent's employer might see. The rule: decide in advance whether you need the level or only the variation. Where you need the level, use an indirect technique, guarantee anonymity and describe concretely how it is protected, and separate the sensitive block from anything identifying. Where variation suffices, accept the biased level, say so in the paper, and check that the bias is not correlated with your treatment.

7. **Choose response scales once and use them throughout.** Number of points, presence of a midpoint, whether all points are labelled or only the ends, and whether "do not know" and "not applicable" are offered. Each of those changes the distribution you get. Offer "do not know" where not knowing is genuinely possible, or you will collect guesses; do not offer it as an easy exit on a question everybody can answer. Treat agreement scales with suspicion, since some respondents agree with whatever is put in front of them: include reverse-worded items and check in the pilot that they behave, and if they do not, the respondents were not reading, which is a finding about your instrument rather than about them. Decide now whether the scale will be analysed as ordinal or as an interval measure, state the choice, and note that the decision belongs with the analysis plan rather than being made later by convenience.

8. **Sequence the instrument, and treat order as a design variable.** Easy and non-threatening items first; sensitive items late; demographics at the end unless they route. Group by topic so respondents are not switching context, but be aware that grouping creates context effects within blocks. Where order could plausibly affect the answers, randomise the order of blocks or items and record what each respondent saw, so order can be controlled for. Recording the order costs one variable and rescues an entire analysis when a referee asks about priming.

9. **Design the routing, then draw it.** Every skip pattern written out as a condition, and the whole thing drawn as a diagram before it is programmed. The judgement call is how much to route, and the rule is that routing that saves less than about thirty seconds is not worth the risk, because every branch is a place where a programming error silently sends a subgroup past a question and produces missingness that looks substantive.

10. **Enforce the length budget by cutting, not by squeezing.** Beyond roughly fifteen minutes, quality falls in ways that are visible in the data: straight-lining, shortening response times, item nonresponse rising through the instrument, and dropout. The rule for cutting: remove whole constructs rather than trimming items from every scale, because a three-item scale reduced to two is often worse than not measuring the construct at all.

11. **Translate by back-translation, then by meaning.** Translate forward, have a second independent translator return it to the original without seeing the source, and reconcile every difference. Then have a bilingual reviewer with domain knowledge check for meaning rather than words. Concepts that do not exist in the target culture need adaptation and disclosure, not literal translation. A translated instrument is a new instrument, so pilot every language version separately and report reliability per language.

12. **Run cognitive interviews before any live pilot.** Five to ten people from the actual population, answering aloud, saying what they think each question is asking and how they arrived at their answer. Probe specifically on the reference period, on any quantifier, and on any word with a technical meaning. This finds misreadings that no amount of desk review does, and it is the single highest-yield hour in the whole process. Record every misreading and what was changed in response.

13. **Run a live pilot, and analyse it as data.** Enough respondents to see the distributions, typically thirty to a hundred depending on the population's accessibility. Check completion time by section, dropout points, routing behaviour, item nonresponse, floor and ceiling effects, straight-lining, and the reliability of every multi-item scale. An item where nearly everybody answers the same way carries no information: cut it or rewrite it. The judgement call is whether a pilot problem needs a redesign or a tweak, and the rule is that anything found in cognitive interviewing about meaning requires a rewrite, while anything found in the live pilot about distribution may be acceptable if the analysis can tolerate it.

14. **Write the sampling and non-response plan before fielding.** The population, the frame, how units are selected, and an honest statement of the gap between frame and population. Then the non-response plan: the expected rate, the number and timing of reminders, the incentive if any, and specifically how you will assess whether respondents differ from non-respondents. Plan that assessment now, because it requires either frame variables held for everyone or a short non-respondent follow-up, and neither can be arranged afterwards. A low response rate that has been examined is a limitation; an unexamined one is a hole.

15. **Field with monitoring, and freeze the instrument.** Watch dropout and item nonresponse in the first days, when a fixable programming error is still fixable. But changing item wording mid-field creates two instruments and two samples: if a change is unavoidable, record the exact date and time of the change and treat the two periods as separate in analysis.

16. **Document the instrument as a deliverable.** The final questionnaire with item numbers, the blueprint, the routing diagram, the translation record, the pilot report, and the changes made after piloting. This becomes the appendix, and assembling it later from memory takes longer than keeping it.

## Item review checklist

Run every item through this before piloting. It takes about a minute per item and catches most of what cognitive interviews would otherwise have to find.

| Check | Fails when |
| One idea | The item contains "and" or "or" joining two attributes |
| Neutral | The stem asserts the thing being measured, or names a socially approved answer |
| Concrete | The item asks about a general tendency where a countable event would do |
| Recallable | The reference period exceeds what a respondent could reconstruct |
| Plain | Any word a respondent would not use unprompted, including your discipline's terms |
| Not negated | The item asks agreement with a negative statement |
| Scale fits | An intensity scale on a frequency question, or the reverse |
| Answerable by all | Respondents to whom it does not apply have no honest option |
| Analysable | You can name the table or model the item appears in |

## Worked example

**Situation.** A doctoral researcher was studying workload and intention to leave among secondary school teachers in a mid-sized education authority covering 62 schools. The authority agreed to distribute the survey through school leaders on condition that it took no more than twelve minutes and that no school could be identified in any output. Ethics approval required a final instrument. The field window was one term, and there would be no second chance, because the authority would not distribute twice in an academic year.

**Task.** An instrument measuring workload, three hypothesised mediators, and intention to leave, in twelve minutes, that would support a mediation analysis and survive a referee reading the appendix.

**Action.** Constructs were defined first. Workload was split into hours worked and perceived unmanageability, on the argument that the hypotheses treated them differently, and that split turned out to matter. Intention to leave was defined as intention to leave the profession, not the school, since an early draft conflated them and the two behave differently.

The wrong turn was in workload. The researcher drafted a new nine-item unmanageability scale, on the reasonable-sounding grounds that existing measures were built for other occupations. Cognitive interviews with seven teachers broke it. Four of the nine items were read as being about hours rather than about manageability, so the scale would have measured the other construct and the mediation model would have been estimating a relationship between a variable and a noisier copy of itself. Two further items were read as being about the school leadership rather than the workload, which is a different construct again. The interviews also revealed that the phrase "a typical week" was interpreted as term time by some teachers and as an average across the year including holidays by others, a difference of several hours.

The scale was abandoned after eleven days of work. A validated four-item workload appraisal measure from the occupational health literature was adopted instead, with one word changed to name the school context and the change documented. That freed four minutes of instrument time, which went to the mediators.

Remaining decisions: a five-point fully labelled agreement scale throughout, chosen for consistency and because grids of that width work on a phone, which mattered since a third of responses were expected on mobile devices. No "do not know" on the attitude items, since every teacher can answer them, but a "not applicable" on the two items about examination classes. Hours worked was asked as a count for the last complete term-time week, with the date of that week stated in the question stem, which was the direct fix for the ambiguity the interviews found. Demographics last. The two blocks of mediator items were randomised in order and the order recorded.

The live pilot ran with 48 teachers in three schools that were then excluded from the main field. Median completion was 10 minutes 40 seconds. Two problems appeared. First, a routing error sent teachers who selected "no examination classes" past a subsequent block they should have seen, which was a programming fault found and fixed in the pilot. Second, one reverse-worded item behaved badly, correlating weakly and with the wrong sign against its scale mates, and it was dropped, reducing that scale from five items to four with reliability reported for the four.

Non-response was planned for. The authority held teaching hours and school size for the whole frame, so respondents could be compared with the frame on both.

**Result.** 1,187 responses from 3,410 teachers, a 34.8 percent response rate, with a median completion of 11 minutes 10 seconds and 4.1 percent dropout after the first substantive question. The frame comparison showed respondents were slightly over-represented in larger schools and slightly under-represented among teachers with fewer than three years of service, both reported and both controlled for. Straight-lining, defined as identical responses across a whole randomised block, appeared in 2.3 percent of cases and those cases were flagged rather than dropped, with the analysis reported both ways.

The abandoned scale cost eleven days. The cognitive interviews that killed it took four hours. Had it been fielded, the mediation analysis would have run, produced coefficients, and been uninterpretable in a way nobody could have diagnosed from the data.

### A second scenario, where it goes differently

The same researcher was later given six item slots in an established national household panel, fielded annually, to measure attitudes to caregiving responsibilities. Everything about the method changed shape.

With six slots, the choice among validated instruments narrows to short forms, and the rule reverses: it is better to use a validated three-item short form of an established scale and spend the other three slots on a second construct than to spread six original items across two constructs, because the panel's value is comparability with other waves and other countries, and an original item has none.

Order and routing were not the researcher's to decide, since the module sits inside a long interviewer-administered instrument whose order is fixed by the panel. What could be controlled was placement, and the request was for the module to sit away from the household finance section, on the argument that answering about money changes how people answer about family obligation. The panel agreed and recorded the placement.

Cognitive interviewing was run by the panel's own field team to their protocol, which meant the researcher supplied probes rather than conducting interviews. Piloting was the panel's dress rehearsal, and the researcher had access to its distributions but no power to change the instrument afterwards, which made the pre-submission item review the only real opportunity and raised its stakes considerably.

What changed: the constraint moved from time to slots, comparability outranked bespoke fit, the pilot became somebody else's, and the leverage moved earlier. What did not change: the constructs were defined first, every item was mapped to a hypothesis, and the item review checklist ran on all six.

## Output

**The construct and item blueprint**, the central document:

| Item no. | Construct | Dimension | Hypothesis | Source (original, adapted, validated) | Change from source | Stem | Scale | Analysis role |

**The item specification**, for each new or adapted item:

```
Item 14
Construct       Perceived unmanageability of workload
Source          Adapted from [instrument], item 3
Change          "your job" replaced by "your teaching and related duties"; reason: respondents
                in cognitive interviews read "your job" as including union and pastoral roles
Stem            Thinking about the last complete teaching week (week beginning 3 November),
                how manageable was the amount of work you were expected to do?
Scale           5 points, fully labelled, "not at all manageable" to "completely manageable"
Missing options None
Routing         Asked of all respondents
Notes           Reverse-scored in analysis
```

**The routing diagram**, as a list of conditions if a drawing is not available:

| From item | Condition | To item | Skipped items | Expected share routed |

**The pilot report:**

| Check | Result | Action |
| Median completion time, overall and by section | | |
| Dropout by item | | |
| Item nonresponse rate, per item | | |
| Floor and ceiling, per item | | |
| Straight-lining rate, per grid | | |
| Reverse-item behaviour | | |
| Scale reliability, per scale and per language | | |
| Routing behaviour against expected shares | | |

**The fielding and non-response plan:**

```
Population, frame, and the gap between them, in one sentence each
Selection method and target n, with the calculation behind the target
Mode, and the device mix expected
Contact schedule: invitation and reminders, with dates
Incentive, if any, and how it is administered
Expected response rate and its source
Non-response assessment: which frame variables are held for everyone, or the
   follow-up design for a non-respondent subsample
Stopping rule for the field period
```

**The appendix set:** final questionnaire with item numbers, blueprint, routing, translation record with the back-translation reconciliation, cognitive interview findings and the changes made, pilot report, and a change log for anything altered after fielding began.

## Failure modes

**Questions written before constructs.** Recognise it when the questionnaire exists and nobody can say which hypothesis an item serves. Fix by building the blueprint retrospectively and cutting everything that maps to nothing; this typically removes a quarter of an instrument.

**A new scale where a validated one exists.** Recognise it by the absence of a source column in the blueprint. Fix by searching the panel study archives before drafting, since large panels publish their instruments and are the fastest place to find a fielded, tested item.

**Adapting a validated scale and reporting it as validated.** Changing the reference period, the population reference or the response format breaks the validation. Fix by reporting the change and your own reliability, and describing the measure as adapted every time it is named.

**The item everybody answers the same way.** Recognise it in the pilot by a distribution with ninety percent in one category. It contributes nothing and costs time. Fix by rewriting to spread the distribution or by cutting it.

**Agreement scales without reverse items.** Recognise it when every item in a scale is positively worded. Fix by adding reverse items, and then actually check them in the pilot, because adding them without checking is worse than not adding them.

**Sensitive questions early.** Recognise it by a dropout spike at a specific item. Fix by moving the block later, and by preceding it with a sentence about why it is asked and how it is protected.

**Routing complexity that outruns the testing.** Recognise it when the routing cannot be drawn on one page. Fix by simplifying, and by testing every path with a fabricated respondent before fielding, which takes an hour and is not optional.

**Piloting as a spell check.** Recognise it when the pilot report contains only typographical corrections. Fix by running cognitive interviews, which are about meaning, and by analysing the pilot data as data.

**Length agreed with the sponsor and then exceeded.** Recognise it when the pilot median is above the agreed budget. Fix by cutting a construct, not by trimming items across all scales.

**Translation done by one bilingual colleague as a favour.** Recognise it by the absence of a back-translation record. Fix by commissioning the back-translation, and by piloting each language separately.

**No non-response plan.** Recognise it after fielding, when somebody asks how respondents compare with non-respondents and the answer is that nothing was collected. Fix in advance by identifying frame variables or designing a follow-up.

## Edge cases

**A very short instrument, three or four items.** Everything still applies except length management. Prioritise validated single items with known properties over abbreviating a multi-item scale, and state that a single item cannot support a reliability estimate.

**Piloting is impossible because the population is tiny or unreachable.** Where the population is, for example, forty regulators in one country, piloting on them consumes the sample. Pilot with the closest available proxy, such as recently retired members of the same population, state the difference, and add a small number of open comment fields so respondents can flag a question that does not work.

**An instrument imposed by a sponsor.** Where the questions are fixed and cannot be changed, run the item review anyway and produce a memo naming the items whose results will not be interpretable and why, before fielding. That memo is the record that the limitation was known, and it is what protects the analysis later.

**Repeated waves of the same survey.** Comparability outranks improvement. Where an item is known to be flawed, the choice is between fixing it and breaking the series; the usual answer is to run both versions in one wave, on split samples, so the change can be calibrated.

**Mixed modes in one study.** Design for the most constrained mode and keep the wording identical across modes. Record the mode for every respondent and treat mode as a covariate, since mode effects on sensitive items are large and well documented.

**Proxy respondents.** Where one household member answers for another, restrict to items a proxy can answer factually and mark every proxy response, because attitude items answered by proxy measure the proxy.

**Children, or populations with limited literacy.** Reading level, response format and interviewer administration all change. Use instruments validated in that population or adapt with expert input, and treat any adaptation as new.

**Administrative data would answer the question better.** Where a variable exists in records that the study can access lawfully, do not ask for it. Self-reported earnings, dates and diagnoses are worse than records, and asking for them costs instrument time and introduces error. `research-ethics-and-data-protection` covers the permissions this requires.

**The survey has already been fielded and the data is bad.** Run the item review on the fielded instrument, identify which constructs are still interpretable, and report those. Be prepared to conclude that a construct is not recoverable; saying so is better than analysing it and hoping.

## Quality bar

- Every construct is defined, with its level and reference period, before any item wording exists.
- Every item maps to a hypothesis and every hypothesis has items, shown in a blueprint a reader can check in both directions.
- Validated instruments are used where they exist, and every adaptation is documented with its reason.
- No double-barrelled, leading, negated or jargon item survives the item review.
- Response scales are chosen deliberately, used consistently, and their treatment in analysis is decided in advance.
- Cognitive interviews were run with the actual population, and the changes they produced are recorded.
- The live pilot was analysed as data, with completion time, dropout, item nonresponse, distributions and scale reliability reported.
- Translations are back-translated, reconciled, and piloted separately, with reliability reported per language.
- The non-response assessment was designed before fielding, and its inputs exist.
- The final questionnaire, blueprint, routing and pilot report are assembled as an appendix rather than reconstructed later.

## Related skills

`research-design` decides what has to be measured and hands this skill the hypotheses. `preregistration-and-analysis-plan` locks how the resulting variables will be analysed, and should be written alongside the instrument rather than after fielding. `research-ethics-and-data-protection` covers consent, information sheets, recruitment routes and the permissions for using administrative records instead of asking. `qualitative-coding-and-analysis` handles the open-ended responses this instrument collects and the interview work that often precedes item writing. `data-profiling-and-cleaning` is the first thing run on the returned data, and it will find what the pilot missed. `descriptive-statistics-tables` builds the sample description, and `data-section-writer` turns the fielding and non-response record into the paper's data section. `systematic-review-protocol` is where to look for what has been measured before when the search for an existing instrument becomes a review in its own right.
