---
name: research-design
description: Produces the written design document that has to exist before any estimation starts: one answerable research question, two to four falsifiable hypotheses each mapped to the exhibit that would test it, an identification strategy chosen to fit the available variation with its key assumption and diagnostic named, the estimating equation with every term defined and the clustering level justified, the data and its three likely problems, the full exhibit list, and the kill criteria. Enforces the rule that the method is chosen after the source of variation is named, never before. Use this skill when starting a new paper, thesis chapter or proposal, when someone asks "is this identified", "what method should I use", "should this be DiD or IV", "how should I study this", when a supervisor asks for a design before data work, or when a project has a dataset, an idea, and no written plan.
---

# Research Design

The most expensive week in empirical research is the one where someone opens the data and starts running regressions before deciding what the paper is arguing. It does not feel expensive. It feels like progress, because output appears: coefficients, tables, a folder of do-files. What has actually happened is that the specification is now being chosen by looking at results, and every choice made from that point is contaminated by having seen them.

The costs arrive later and separately. A referee asks what the identifying variation is and the answer has to be reconstructed after the fact, which reads exactly as it is. An examiner asks which hypothesis a table tests and there is no answer because the table was produced before the hypotheses existed. Half the exhibits in the draft test nothing and cannot be cut because the student cannot tell which half. And the deepest cost is silent: an unidentified design gets three years of competent work poured into it and the defect is structural, so no amount of robustness checking repairs it.

A design document takes about a week and is one page. It is written before the data is opened, and it is the artefact that makes everything after it checkable.

## When to use this, and when not to

Use it at the start of any empirical paper, thesis chapter, proposal or grant application, and use it again whenever the question, the data or the identification changes materially, because a design document that no longer describes the project is worse than none. Use it when a supervisor asks whether something is identified, when a choice between methods is on the table, and when a project has been running for weeks and nobody can say in one sentence what it is testing.

Use it especially when the enthusiasm is high and the plan is verbal. Verbal designs are always more coherent than they turn out to be in writing, and the gap between the two is where the project fails.

Do not use it to choose the question itself. If there is a topic and no question, or several candidate questions competing, that is `research-question-ideation`, which hands its recommended question to this skill. Do not use it to defend a design that already exists against a specific referee attack; that is `identification-defense`, which goes deeper on threats and placebo tests than a design document should. Do not use it to write the estimating equation into publishable prose, which is `econometric-model-writer`, or to lock the analysis against specification searching in a registrable form, which is `preregistration-and-analysis-plan` and which takes this document as its input.

Do not use it as a substitute for the theory. A design says how the effect will be measured; it does not say why the effect should exist, and a referee will ask both. `theoretical-framework-review` covers the second.

## What you need before starting

**The research question, as one sentence.** With population, the treatment or variable of interest, and the outcome named. Missing: stop and run `research-question-ideation`. Writing a design around a topic produces a document that agrees with everything and constrains nothing, and it takes two days to discover this.

**The source of variation, or the honest admission that there is none.** What makes some units treated and others not, or the same unit treated at one time and not another. Missing: this is the single most important gap and it is usually filled by reading the institutional history of the setting rather than by thinking harder. Look at eligibility rules, reporting thresholds, rollout dates, and years when definitions changed.

**The data, its structure, and its limits.** Unit of observation, period covered, frequency, expected sample, and which variables actually measure treatment and outcome. Missing: write the design conditionally, marking every claim about the data as an assumption to verify, and make verifying them the first task. Do not assume a variable exists because the codebook lists it; codebooks describe intentions, and administrative variables are frequently populated for only part of the period.

**The nearest existing papers, verified.** Two or three, for what they did and what a referee will therefore expect. Missing: search before designing. The design's method choices are partly conventional, and departing from the field's convention without knowing you are departing from it is how a paper collects an avoidable rejection.

**The constraints.** Time, the target venue, the methods the researcher can execute now, and whether the data access is settled. Missing: assume the conservative case and say you have assumed it. A design that requires a method the researcher will have to learn is viable only if the timeline says so explicitly.

**Whether anything has been looked at already.** Missing: ask directly, and record the answer in the document. It determines whether this design can honestly become a preregistration later, and that determination cannot be made retrospectively.

## The method

1. **Write the research question in one sentence and test it.** Population, variation, outcome. The test: could two competent readers give different answers and both be answering the same question? "Does the childcare fee cap raise maternal employment among mothers of children under six in adopting municipalities" passes. "The effects of childcare policy" does not. If the sentence needs a semicolon, it is two questions and one of them is the paper.

2. **Write what is new and who changes their mind, in two sentences.** The gap this fills, and the named reader or decision affected by the answer. The rule for the second: name a person, a literature with a specific disagreement, or a policy choice. If the honest answer is that nobody changes their mind, the question is not ready, and no amount of design work will repair that. A question already answered well is worth asking again only with better data, better identification, or a better measure, and the document must say which of the three.

3. **State two to four hypotheses, each falsifiable, each mapped to its exhibit.** Write the exhibit next to the hypothesis: a coefficient in a named table, an event-study figure, a difference between two subgroup estimates. The rule: if no possible result could reject it, it is a belief and gets cut or rewritten. Order them so the narrative runs main effect, then mechanism, then heterogeneity, because that is the order a reader needs them and the order the paper will be written in.

4. **Name the source of variation in plain words, before any method is mentioned.** One paragraph, no notation. What varies, across which units, over what period, and why that variation is plausibly unrelated to the outcome except through the treatment. This paragraph is the paper. If it cannot be written in plain words, the design is not understood yet, and writing it in notation will conceal that from everyone including the author.

5. **Choose the method to fit the variation.** Only now, and using the decision rules below. The direction of this step is the whole point: variation first, method second. Choosing the method first and then hunting for variation that suits it is the most common structural error in doctoral empirical work and it is visible to referees in the first two pages.

6. **Name the key assumption and the diagnostic that will probe it.** One assumption, one diagnostic, both written down. Parallel trends and a pre-treatment event study. No manipulation at the cutoff and a density test. Exclusion and a defence in prose plus a first-stage F statistic. Selection on observables and a balance table with the limitation stated as a limitation. A design that cannot name its own biggest threat has not been stress-tested, and the threat it cannot name is the one a referee will find.

7. **Write the estimating equation with every term defined.** Unit and time subscripts explicit, fixed effects listed individually rather than as "the usual controls", the parameter of interest identified by name, and the clustering level stated with its reason. The rule for clustering: cluster at the level at which treatment is assigned, and where that produces fewer than roughly forty clusters, say now what inference method will be used instead, because discovering the problem after the results exist creates pressure to choose the method that gives the answer you want.

8. **Write the data section as facts and problems.** Source, years, unit, expected sample, and the exact variables measuring treatment and outcome including who records them and how. Then list the three data problems most likely to appear, with a plan for each. Almost always among them: attrition or entry and exit of units, measurement error in the outcome, and treatment misclassification. Naming them in advance converts them from crises into scheduled work.

9. **List every exhibit the finished paper will contain, in order.** Descriptives, main result, identification diagnostic, robustness, heterogeneity, and any mechanism exhibit. The rule: every exhibit maps to a hypothesis from step 3 or to the assumption from step 6. An exhibit that maps to neither gets cut now, which is far easier than cutting it after it exists and someone is attached to it.

10. **Write the kill criteria.** What data reality or result would mean this project should stop or change shape? Common ones: fewer than a stated number of treated units, pre-trends that do not flatten, a first stage below a stated threshold, an outcome variable populated in too few years. Write the numbers. This is the section people skip and it is the one that distinguishes a research programme from a sunk cost, because when the moment comes the researcher will be tired, invested, and the worst possible judge of whether to continue.

11. **Have someone else read it who is not on the project.** Twenty minutes. The question to ask them is not whether it is good but what they think the paper is arguing. If their answer differs from yours, the document is not finished.

## Matching the design to the variation

Read this as a decision table, entered from the left column. The variation determines the method; the method never determines what to look for.

| What the variation looks like | Design | Key assumption | Diagnostic that must appear | Most common failure |
| Policy adopted by different units at different times | Difference-in-differences with a staggered-adoption estimator | Parallel trends conditional on covariates, and no anticipation | Event study with at least three pre-periods, plotted | Using naive two-way fixed effects with staggered timing, which weights already-treated units as controls |
| Policy adopted by all units at one date | Interrupted time series, or DiD against an unaffected group | The counterfactual trend is knowable | Placebo dates, and a plot of the raw series | No control group at all, leaving a before-and-after comparison |
| A threshold or cutoff assigns treatment | Regression discontinuity | No precise manipulation of the running variable | Density test at the cutoff, covariate smoothness, bandwidth sensitivity | Too few observations near the cutoff, discovered after the design is fixed |
| Assignment is random or lottery-based | Randomised or lottery-based comparison | Randomisation held, and attrition is not differential | Balance table, attrition by arm | Ignoring differential attrition |
| Something moves treatment and plausibly nothing else | Instrumental variables | Exclusion restriction, relevance, monotonicity | First-stage strength, and a written defence of exclusion | An instrument defended by assertion, which referees reject on sight |
| Units differ persistently and treatment varies within them | Panel fixed effects | No time-varying confounder correlated with treatment timing | A specification showing the estimate under different fixed effect sets | Treating within-unit variation as though it were exogenous |
| Nothing exogenous is available | Selection on observables: matching, reweighting, or controls | Conditional independence, which is rarely credible | Balance after matching, and a sensitivity or bounding analysis | Presenting the estimate as causal when the design does not support it |

Two rules govern the table. First, when the variation fits two rows, prefer the design whose key assumption is more testable with the data in hand, not the one that sounds more sophisticated. Second, when the variation fits no row, the honest design is descriptive, and the document says so in step 2 by changing what the paper claims rather than by decorating a weak design with an estimator.

## Writing the equation so it constrains

The equation is not decoration and it is not for the referee. It is the thing that stops the specification drifting once results appear.

Define every subscript. Write the fixed effects out: municipality fixed effects, year fixed effects, and municipality-specific linear trends are three different commitments and "controls" is none. Name the coefficient of interest with a symbol and say in words what it estimates and for whom, which is where the difference between an average treatment effect on the treated and a local average treatment effect actually gets thought about rather than asserted in a footnote.

State the standard error treatment and the reason. State how missing data is handled. State which specification is the headline before you know what any of them show, because the headline chosen afterwards is chosen for its coefficient.

Where a modern estimator is required, name it and name the fallback, so that a package problem in month four does not become a design decision made under time pressure.

## Worked example

**Situation.** A third-year doctoral student, Adaeze Nnamani, at the Fairhaven School of Public Policy, had a question and a dataset and eight months of work already visible in a folder of exploratory regressions. The question was whether a municipal childcare fee cap raised maternal employment. The setting had 289 municipalities, of which 61 adopted the cap between 2016 and 2021 on their own timetable. Her supervisor had asked for a written design before the next committee meeting, six weeks away, and had specifically said the exploratory regressions should not be shown.

**Task.** One page. A design that could survive a committee member who works on staggered treatment timing, and an honest account of what had already been seen, because the plan was to preregister the analysis and that requires disclosure.

**Action.** The question sentence took two attempts. The first was "does childcare policy affect maternal labour supply", which failed the test in step 1 immediately: two readers would answer it differently because neither the policy nor the population was named. The second version fixed the population as mothers whose youngest child was aged one to five and the outcome as employment in the month of observation.

Step 4, the plain-words paragraph, exposed the first real problem. Municipalities that adopted early were not like those that adopted late: adoption correlated with council composition and with existing childcare capacity. That did not kill parallel trends by itself, but it made the assumption something to be argued rather than asserted.

The first wrong turn was an attempt to solve this with an instrument. The proposal was to instrument adoption with the left-of-centre share of the municipal council. It was abandoned within a day, and the reason is worth stating precisely: council composition plausibly affects maternal employment through several other channels, including local public sector hiring and other family policies adopted in the same period. The exclusion restriction was not merely hard to defend, it was false in a way any referee in the field would name in one sentence. Reaching for an instrument to rescue a difference-in-differences design is a common move and it usually produces a worse paper, because it swaps a debatable assumption for an indefensible one.

The second wrong turn was in the estimator. The exploratory work had used two-way fixed effects on the staggered panel. With adoption spread across six years, that estimator uses already-treated municipalities as controls for later adopters, and the effect was expected to grow over time, which is exactly the case where the weights go wrong. The design switched to an estimator that compares each treated cohort against not-yet-treated units, with the classic specification kept as a reported comparison rather than as the headline.

The third problem was found in step 8 and changed the data source. The outcome had been drawn from a labour force survey with municipality identifiers, but the survey sampled roughly 340 mothers per municipality per year in the median municipality, and far fewer in small ones. The design moved to the administrative employment register, which covered the full population, giving roughly 1.7 million mother-year observations and, more importantly, monthly employment status rather than an annual snapshot.

Clustering was set at the municipality level, giving 289 clusters, comfortably above the threshold where conventional inference becomes unreliable. That check took two minutes and mattered, because an earlier version of the design had proposed clustering at the level of the eleven administrative regions.

Kill criteria were written with numbers: fewer than forty adopting municipalities with three clean pre-periods; pre-treatment event-study coefficients jointly significant at the five percent level and trending; or the outcome variable unavailable before 2015, which would leave the early cohorts with no pre-period at all.

**Result.** The design document ran to one page plus a two page appendix holding the equation, the exhibit list and the data problems. The committee meeting spent its time on the parallel trends argument rather than on what the paper was about, which is the sign that a design document has done its job.

The pre-trends check, run first as the document required, came back flat for the 2018 and later cohorts and mildly sloped for the 2016 cohort. Under the kill criteria that was not a kill but a scope change: the 2016 cohort was dropped from the main specification and reported separately, a decision made against a written rule rather than against a coefficient.

Eight months of exploratory regressions were discarded. Roughly two of those months would have been saved by writing the design first, and the eight months of familiarity with the data was not worthless, but the student's own view afterwards was that a week in month one would have bought most of it.

### A second scenario, where it goes differently

A postdoctoral researcher at the same school had survey data on 2,400 small firms and a question about whether adopting a formal quality management system improved firm performance. There is no reform, no threshold, no lottery, and no plausible instrument. Every row of the decision table returns nothing except the last.

The design document changes shape in three places rather than being abandoned.

Step 2 changes the claim. The paper does not claim an effect; it claims a conditional association together with an honest account of how large an unobserved confounder would have to be to explain it away. That decision is made at the design stage and written into the question sentence, so the language of the eventual abstract is fixed before any estimate exists. This is the discipline that prevents causal verbs appearing in the conclusion of an associational paper, which is the most common reason this kind of work is rejected.

Step 6 changes content. The key assumption is conditional independence, which is not credible on its own, so the diagnostic is not a test but a bounding exercise: a sensitivity analysis reporting how strong selection on unobservables would need to be, relative to selection on observables, to overturn the result. That exhibit is listed in step 9 as a main table rather than as an appendix item, because in this design it is load-bearing.

Step 10 changes threshold. The kill criterion is not about pre-trends but about balance: if the treated and untreated firms differ so much that common support is thin, the estimate is extrapolation and the project becomes a descriptive paper about which firms adopt, which is a real paper and should be named as the fallback in advance.

What did not change: the one-sentence question, hypotheses mapped to exhibits, the equation with defined terms, the exhibit list, and the kill criteria with numbers in them.

## Output

One page, with an appendix for the equation and anything long.

```
RESEARCH DESIGN
Question:        [one sentence: population, variation, outcome]
Contribution:    [the gap, one sentence] / [who changes their mind, one sentence]
Claim type:      [causal / conditional association / descriptive]
Status:          [nothing seen yet / partial exploration, described below]

HYPOTHESES
| # | Hypothesis, falsifiable | Exhibit that tests it | Predicted sign |

IDENTIFICATION
Variation:       [one paragraph in plain words, no notation]
Design:          [DiD / RDD / IV / panel FE / matching / descriptive]
Key assumption:  [one sentence]
Biggest threat:  [one sentence, named]
Diagnostic:      [the exhibit that probes it]

MODEL
[Equation, every term defined. Fixed effects listed. Parameter of interest named.]
Clustering:      [level] because [reason]. Clusters: [n].
Missing data:    [rule]
Headline spec:   [which one, decided now]

DATA
Source, years, unit, expected N, treatment variable, outcome variable.
| Likely problem | How it would show up | Plan |

EXHIBITS
| # | Exhibit | Type | Tests which hypothesis or assumption |

KILL CRITERIA
[Numbered, with numbers in them. What stops or reshapes this project.]
```

## Failure modes

**Method before variation.** Recognise it when the project is described by its estimator. Fix by writing step 4 in plain words with all notation banned, and choosing again from the table.

**Naive two-way fixed effects on staggered timing.** Recognise it when adoption dates differ across units and the specification is a single treatment dummy with unit and time fixed effects. The estimator uses already-treated units as controls, and where effects grow over time the weights can be negative. Fix by naming a cohort-based estimator in the design and reporting the conventional one as a comparison.

**An instrument reached for to rescue a weak design.** Recognise it when the instrument appears after the difference-in-differences was questioned. Fix by asking whether the exclusion restriction is defensible in one sentence to someone who knows the setting. If not, the earlier design with an honest assumption is the better paper.

**Hypotheses with no possible disconfirming result.** Recognise them because the predicted sign column is empty or reads "an effect". Fix by writing the sign, or by rewriting the hypothesis until a result could contradict it.

**Exhibits with no hypothesis.** Recognise them in step 9 as the tables nobody can attach to a row in step 3. Cut them before they are produced.

**Clustering decided after the standard errors are seen.** Recognise it when the level of clustering changes between drafts. Fix by writing the level and the reason into the design and by naming the inference method for the few-clusters case in advance.

**Controls listed as "standard".** Recognise the phrase. It is not a specification and it permits silent addition and removal later. Fix by listing every variable.

**The design document that nobody rereads.** Recognise it when the paper's method has changed and the document has not. Fix by treating a material change as a reason to revise the document and date the revision, so the divergence between plan and practice is visible rather than accumulating.

**Designing around a variable that turns out not to exist.** Recognise it too late, usually in month three. Fix by making the first task after the design a verification pass over the actual data: does the variable exist, in which years, populated for what share of units.

## Edge cases

**No exogenous variation and none obtainable.** Do not decorate. Declare the claim type as conditional association or descriptive in the question sentence, add a bounding or sensitivity exhibit as a main table, and fix the vocabulary of the eventual abstract now. A well-executed descriptive paper on an important question publishes; a weakly identified paper claiming causality does not.

**Small number of treated clusters.** Below roughly forty, and severely below fifteen, conventional cluster-robust inference fails. Decide in the design: wild cluster bootstrap, randomisation inference, or a design change that moves identification to a lower level such as an eligibility threshold within units. Make this choice before the results exist.

**The treatment is measured with error or is partially misclassified.** Say what direction the bias runs, which for classical measurement error in a binary treatment is towards zero and therefore makes a null result uninformative. Where the main result may be null, this must be settled at design stage, because a null under attenuation cannot be interpreted afterwards.

**The data has already been explored.** Record exactly what was looked at, in the document, in the status line. This determines what can honestly be preregistered and what has to be labelled exploratory. Deciding this later, with results in hand, is deciding under pressure.

**Multiple treatments adopted in the same period.** Common in policy settings, where a childcare reform arrives alongside a parental leave change. Name the co-timed policies in the design, and say how they will be separated: different eligibility populations, different timing at the margin, or an explicit statement that the estimate is of the package rather than of one component.

**Qualitative or mixed-methods work.** The document survives with its identification section replaced by a warrant section: case selection logic, what makes the evidence adequate to the claim in this tradition, and what would count as disconfirming. Hypotheses become propositions, exhibits become the analytic products such as a coding framework or a cross-case matrix, and kill criteria become access thresholds. Everything else stands.

**A registered report or a preregistration is planned.** Write the design first and to a higher standard on the specification and exclusion rules, then hand it to `preregistration-and-analysis-plan`, which will demand decisions this document can leave open, particularly on multiple comparisons and on what counts as a null.

## Quality bar

- The research question is one sentence naming population, variation and outcome, and two readers would answer it the same way.
- The source of variation is stated in plain words before any method or notation appears.
- The method follows from the variation and the document shows that order.
- One key assumption and one diagnostic exhibit are named, and the biggest threat is stated in the author's own words.
- Every hypothesis has a predicted sign and a named exhibit; every exhibit maps to a hypothesis or to the assumption.
- The equation defines every term, lists fixed effects individually, and states the clustering level with its reason and the cluster count.
- The claim type is declared as causal, associational or descriptive, and the language of the paper is fixed to match.
- Kill criteria are written with numbers in them.

## Related skills

`research-question-ideation` produces the question this design is built around and should run first when the question is not settled. `theoretical-framework-review` supplies the mechanism argument for why the effect should exist, which this document assumes rather than establishes. `preregistration-and-analysis-plan` takes this document and hardens it into a commitment that can be registered. `identification-defense` goes deeper on the named threat once a referee attacks it. `econometric-model-writer` turns the equation and its assumptions into publishable methods prose. `data-profiling-and-cleaning` runs the verification pass that confirms the data actually contains what the design assumes. `research-proposal-and-grant` embeds this document in the wider proposal. `stata-project-scaffold` sets up the folder and code structure that the exhibit list implies.
