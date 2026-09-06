# Commercial and data track

Sixteen skills that sit between the two main tracks: commercial work that needs analytical discipline, and analytical work that has to end in a commercial decision. They extend the [Chief of Staff track](../chief-of-staff/README.md) rather than standing apart from it.

This track came out of an audit rather than a plan. Going back through the skills built privately for client work, the question for each was whether the value sat in the method or in the employer's material. Where it sat in the material, the skill stayed private. Where it sat in the method, the skill was rewritten from scratch with the frameworks, client names, personnel, approved claims, and branded assets removed and replaced by a local file the user supplies. That separation is a useful test to run on any private library before publishing part of it.

## The skills

| # | Skill | What it enforces |
| --- | --- | --- |
| 74 | [content-quality-gate](content-quality-gate/SKILL.md) | Nine checks every piece of buyer-facing content clears before it ships |
| 75 | [account-reengagement-plan](account-reengagement-plan/SKILL.md) | Restarting a paused account: diagnosis before proposal, objection playbook, rehearsal personas |
| 76 | [client-economics-analysis](client-economics-analysis/SKILL.md) | Lifetime value, health scoring, cost of loss, whitespace, net revenue retention, per client |
| 77 | [economics-report-from-data](economics-report-from-data/SKILL.md) | Four levels of analysis, seven economic frameworks, traceable and falsifiable claims |
| 78 | [contractor-msa-and-task-order](contractor-msa-and-task-order/SKILL.md) | The two contractor documents, in the right order, with full clause anatomy |
| 79 | [sales-roleplay](sales-roleplay/SKILL.md) | A buyer who does not volunteer pain, and coaching that hands over exact language |
| 80 | [image-to-spreadsheet](image-to-spreadsheet/SKILL.md) | Transcription with nothing invented, and chart estimates labelled as estimates |
| 81 | [spreadsheet-analysis-workbook](spreadsheet-analysis-workbook/SKILL.md) | Reading someone else's workbook before trusting it, and building tabs that reconcile |
| 82 | [revenue-analysis-workbook](revenue-analysis-workbook/SKILL.md) | The seven standard tabs, every figure a live formula, a verification tab that proves it |
| 83 | [revenue-concentration-risk](revenue-concentration-risk/SKILL.md) | Share weighted by how hard it is to leave, and what losing each account really costs |
| 84 | [expected-revenue-estimation](expected-revenue-estimation/SKILL.md) | Five methods ranked by reliability, three scenarios, sensitivity, and an update trigger |
| 85 | [discovery-to-proposal-deck](discovery-to-proposal-deck/SKILL.md) | Discovery played back in the client's words before any solution is proposed |
| 86 | [business-agreements-drafting](business-agreements-drafting/SKILL.md) | Equity, employment, NDA, partnership, and vendor agreements with the risk flags surfaced |
| 87 | [sales-call-analysis](sales-call-analysis/SKILL.md) | Eight deal dimensions scored on quoted evidence, never on a seller assertion |
| 88 | [demo-call-transcript-generator](demo-call-transcript-generator/SKILL.md) | Synthetic call histories where partial evidence is correct rather than a gap |
| 89 | [sales-team-competency-assessment](sales-team-competency-assessment/SKILL.md) | Self and leadership scores blended, with the perception gap as the coaching signal |

## Local configuration

Three of these expect a file you write once and keep beside the skill, because the method is public and the specifics are yours.

- `content-quality-gate/standard.md`: your buyer segments, core beliefs, named method, terminology rules, approved claims, and default call to action.
- `contractor-msa-and-task-order/standing-terms.md`: governing law and forum, dispute resolution, the non-solicitation period, the intellectual property position, and payment timing.
- `contractor-msa-and-task-order/`: a blank intake template and one filled example, which teach tone and depth better than any instruction about them.
- `business-agreements-drafting/party-defaults.md`: entity name and form, registered address, authorised signatory, governing law and forum, and standard payment terms.
- `sales-team-competency-assessment/framework.json`: the map from instrument questions to competency areas, the crosswalk of names, and the leader text to number mapping.

Without those files the skills still run, but the checks they can apply are structural rather than specific.

## Workbook discipline

Six of these skills share one non-negotiable standard. Raw data lives in the workbook as its own sheet. Every analysis cell is a live formula reading from it, never a pasted number. Derived fields reference the cells above them rather than recomputing. A visible reconciliation cell reads zero. Assumptions sit in labelled input cells. The test is simple: change one row of raw data and every figure in the report moves.

## The analytical chain

`spreadsheet-analysis-workbook` is the foundation and the others assume it rather than repeating it. `revenue-analysis-workbook` builds the standard seven tabs from a raw extract. `revenue-concentration-risk` and `client-economics-analysis` read the entity table it produces, one looking at portfolio exposure and the other at individual relationships. `expected-revenue-estimation` handles anything without a track record. `economics-report-from-data` turns any of them into the written argument.

## The commercial chain

`sales-roleplay` rehearses the conversation, `sales-call-analysis` scores the real one, `demo-call-transcript-generator` produces the material to test that scoring against, and `sales-team-competency-assessment` looks at the team behind it. `discovery-to-proposal-deck` picks up where discovery ends, and hands to `proposal-writer` and `sow-and-scope` in the Chief of Staff track. `business-agreements-drafting` covers the agreements those two do not.
