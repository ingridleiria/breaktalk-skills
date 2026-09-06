---
name: sales-team-competency-assessment
description: Assesses a sales team against a defined ideal profile using two perspectives on competency, the seller's own self-assessment and their leaders' evaluation, blended into a single score per competency area and per person, with an optional personality component from whatever validated instrument the organisation licenses. Produces a team dashboard, a perception-gap view, per-person profiles, and individual coaching plans. Use this skill when the user has self-assessment and manager-evaluation data for a sales team and wants it scored, when they ask for an ideal seller profile assessment, a team capability review, or per-rep coaching plans.
---

# Sales Team Competency Assessment

Two things make this assessment useful rather than decorative. The blended score, because a self-assessment alone measures confidence and a manager assessment alone measures visibility. And the gap between the two, because a person who rates themselves two points above their leaders has a different problem from a person who rates themselves below.

## Inputs

A self-assessment instrument with numeric responses per person, a leader evaluation covering the same competency areas with one response set per leader per person, and optionally a personality profile from a validated instrument the organisation licenses. Where a leader did not evaluate someone, they are simply absent and the consensus uses whoever did.

Never invent a response, a note, or a personality result. Open-ended comments are reproduced from source or omitted.

## The competency framework

Map the instrument's questions to five or so competency areas and record the mapping in a `framework.json` beside this skill, so the framework can be retuned without touching the method. A workable default set for a business-to-business sales team: relationship management, executive communication, industry and domain insight, managing accounts and opportunities, and adaptability including digital fluency.

Record the crosswalk between the instrument's names for the areas and the names used in the output, because they are rarely the same and the mismatch is where reports lose credibility.

## Scoring

```
area self          = mean of that area's questions, self responses
area leadership    = mean across leaders of each leader's area mean
area combined      = mean(area self, area leadership)
gap                = area leadership - area self
overall per source = grand mean of all questions for that source
overall combined   = mean(overall self, overall leadership)
```

Where leaders answer in words rather than numbers, record the text to number mapping explicitly in the framework file, and use it consistently.

**The fit scale**, read on the blended score across a one to four instrument: 3.5 and above high, 3.0 to 3.49 moderate to high, 2.5 to 2.99 moderate, 2.0 to 2.49 low to moderate, below 2.0 low. Use the same five labels for the competency score, the personality fit, and the overall fit, so the three read on one scale rather than three vocabularies.

Overall fit is the blend of competency fit and personality fit, converted to numbers, averaged, and mapped back to the same five labels.

Flag any person whose self and leadership scores differ by more than two points. That flag is a coaching conversation regardless of the underlying level.

## Deliverables

**Team assessment.** An executive summary saying the situation, the headline, what stands out, and the recommendation. A dashboard with one row per person: competency score, competency fit, personality fit, overall fit. A quadrant placing each person by competency against personality, coloured by overall fit. A perception-gap view showing self against leadership per person. The ideal profile itself, with an explanation of where the rating comes from and what the scale means. Then the findings, written as the story behind the numbers rather than a restatement of the table.

**Leadership report.** An auditable workbook with the three averages per area and overall, self, leadership consensus, and combined, plus the open-ended comments as written. This is the file that gets challenged, so every figure is a formula reading the response data.

**Coaching plans, one per person.** Their profile against the ideal, the personality component where available, the competency detail with all three averages and their own reflections, and a development plan seeded from the blended results and from what the person themselves asked for. The specifics are set in the live conversation, and the document says so rather than inventing objectives.

## Presentation conventions

Three colours only, and they carry meaning: strong, adequate, weak. One scale and one vocabulary throughout. Every table uses the same column order: self, each leader, leadership average, combined, fit. Reproduce source text rather than paraphrasing it in a document that people will recognise their own words in.

## Quality bar

- The blended score, not the self score, drives every fit label and every ranking.
- The leader text to number mapping recorded explicitly, not applied ad hoc.
- Gaps above two points flagged on the individual's profile.
- Open-ended comments and any personality text reproduced from source, never invented.
- Coaching objectives presented as a data-grounded scaffold, with the note that specifics are agreed live.
