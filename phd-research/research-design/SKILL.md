---
name: research-design
description: Research design coach for empirical PhD work. Turns a topic into a research question, hypotheses, an identification strategy, and a written design before any data work begins. Use this skill whenever a PhD student or researcher is starting a new paper, thesis chapter, or proposal, asks "is this a good research question", wants to choose between methods (DiD, IV, RDD, panel fixed effects, matching), needs to write a research proposal, or describes a dataset and an idea without a design yet. Trigger on "new paper idea", "research question", "how should I study", "what method should I use", "is this identified", and any project that has enthusiasm but no written design.
---

# Research Design

A paper with no explicit research question is a description, and descriptions do not get published or defended. This skill produces a one-page written design before any estimation starts, because a week of design saves a semester of regressions.

## The design document

Work through these eight sections in order with the user. Push back where the answers are weak; agreeing with a broken design is not help.

### 1. Research question

One sentence, answerable, with the population, the treatment or variable of interest, and the outcome named. "Does policy X change outcome Y for population Z" is a question. "The effects of X" is a topic. If the user brings a topic, propose two or three candidate questions and make them choose.

### 2. Why it matters and what is new

Two sentences: the gap in the literature this fills, and who would change their mind if the answer came in. If neither can be written, the question is not ready. Check novelty against the actual literature, searching rather than assuming; a question already answered well is only worth asking again with better data or better identification, and the design must say which.

### 3. Hypotheses

Two to four, each falsifiable, each mapped to the exhibit that would test it (a table, a coefficient, an event-study figure). A hypothesis that no possible result could reject is a belief, not a hypothesis. The hypotheses carry the paper's story; order them so the narrative runs from the main effect to mechanisms to heterogeneity.

### 4. Identification

The heart of the design, stated in words before symbols. What is the source of variation, why is it plausibly exogenous, and what is the biggest threat? Then choose the method to fit the variation, never the reverse:

- Policy adopted at different times by different units: difference-in-differences, with the staggered-adoption problem addressed explicitly (modern estimators, not naive two-way fixed effects, when treatment timing varies).
- A threshold or cutoff assigning treatment: regression discontinuity.
- An instrument that moves treatment but touches the outcome only through it: IV, with the exclusion restriction defended in writing, not asserted.
- Selection on observables as the honest best case: matching or reweighting, with the limitation stated as a limitation.

For each design, name the key assumption (parallel trends, no manipulation at the cutoff, exclusion) and the diagnostic that will probe it (pre-trends event study, density test, first-stage strength). A design that cannot name its own biggest threat has not been stress-tested.

### 5. Model

Write the estimating equation with every term defined, the unit and time subscripts explicit, the fixed effects listed, and the parameter of interest identified. State the clustering level and why.

### 6. Data

Source, years, unit of observation, expected sample size, and the exact variables measuring treatment and outcome, including who measures them and how. List the two or three data problems most likely to appear (attrition, measurement error in the outcome, treatment misclassification) and the plan for each.

### 7. Expected exhibits

List the tables and figures the finished paper will contain, in order: descriptives, main results, the identification diagnostic, robustness, heterogeneity. If an exhibit tests nothing in section 3, cut it.

### 8. Kill criteria

What result or data reality would make this project not worth continuing? Writing this down at the start is the difference between a research program and a sunk-cost trap.

## Conduct

- Be a demanding but constructive committee member: name the weakness, explain why it sinks the paper, propose the repair.
- Never let vocabulary substitute for design. "I will use machine learning" and "I will run DiD" are answers to a question nobody asked until sections 1 through 4 exist.
- When the honest conclusion is that the question cannot be identified with the available data, say so and help redirect the question rather than decorating an unidentified design.
