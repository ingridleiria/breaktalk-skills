<p align="center"><img src="brand-and-writing/breaktalk-brand/assets/breaktalk_logo.png" width="160" alt="BreakTalk"></p>

# BreakTalk Skills: an open library of AI working instructions for Chief of Staff work, empirical PhD research, and writing

<p align="center">
<img src="https://img.shields.io/badge/skills-110-1F3864" alt="110 skills">
<img src="https://img.shields.io/badge/tracks-5-1F3864" alt="5 tracks">
<a href="https://github.com/ingridleiria/breaktalk-skills/releases/latest"><img src="https://img.shields.io/github/v/release/ingridleiria/breaktalk-skills?color=7B1E28" alt="latest release"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-7B1E28" alt="MIT"></a>
</p>

I work two jobs that look unrelated and are not. I am Chief of Staff at a US B2B consulting firm, and I am a PhD candidate in Economics at Korea University. Both jobs are the same discipline applied to different material: take something complicated and messy, structure it, attach evidence to every claim, and hand someone a document they can act on.

Over the past two years I wrote these methods down as instruction files so an AI assistant would hold the standard for me, first for the consulting side, then for the research pipeline. This repository is the public, generalized version of that library: 110 skills across five tracks. They are plain Markdown and they work with Claude, ChatGPT, Gemini, and any other assistant that accepts written instructions. Nothing here contains employer or client material; these are the methods, rebuilt from scratch to be usable by anyone.

I write about how this works in practice at [BreakTalk](https://breaktalk.substack.com).

**New here?** [USING_THESE_SKILLS.md](USING_THESE_SKILLS.md) explains how to run one of these in any assistant, and how to adapt it to your own numbers, tools and field. Take one file, run it on work you have already finished, and edit it where it disagreed with you and you were right.

## What is a skill

A skill is a folder with a `SKILL.md` file inside it: a short frontmatter block saying what the skill is for, then the method written out in plain Markdown. Nothing else. No code, no dependencies, no framework.

Skills do not make a model know more. They make it work to a standard, in a repeatable way, so the tenth market analysis follows the same method as the first. Everything an expert would do and a rushed person would skip is written down, and the file ends with a quality bar that says what finished means.

The folder-and-frontmatter shape comes from [Anthropic's skills format](https://docs.claude.com), which is where I first built these. The content is not specific to any model. It is a written method, and any assistant that accepts written instructions can follow it.

## Using them, whichever assistant you use

**[USING_THESE_SKILLS.md](USING_THESE_SKILLS.md) is the full guide**: how to load a skill into any assistant, how to make a first run that teaches you something, and a method for adapting a file to your own numbers, tools, field and jurisdiction. If you only read one page before taking something from here, read that one.

The short version. A skill is a folder with a `SKILL.md` file in it, in plain Markdown, with nothing to install.

**Claude**: on claude.ai, Settings, Capabilities, Skills, then upload a skill folder as a zip. In Claude Code, copy the folder into `.claude/skills/` in your project, or `~/.claude/skills/` for all projects. The releases page carries each skill zipped individually.

**ChatGPT**: paste the body of the `SKILL.md` into a Project's instructions, or into the instructions of a custom GPT. Name the GPT after the skill so you can find it. For a one-off, paste the file at the top of a new conversation and then give it your material.

**Gemini, Copilot, Mistral, or any other assistant**: paste the body into the system prompt, the custom instructions, or the top of the conversation. That is all a skill is.

**Coding assistants**: the same text works as a rules file, for example `.cursor/rules/` or `.github/copilot-instructions.md`, for the skills that apply to written deliverables in a repository.

**API or your own tooling**: send the body as the system prompt for that task.

Two notes for the non-Claude routes. The frontmatter `description` is the field that decides when Claude loads a skill automatically; elsewhere you are choosing the skill yourself, so that block can be dropped, though it is a useful summary of when to reach for the file. And where a skill mentions reading or writing files, hand the assistant the material directly instead.

Several skills use connected tools when they are available, such as a data provider for account research, an academic search tool for literature, or a CRM for pipeline data, and fall back to web research or to what you paste in when they are not. None of them require a paid tool to work.

Each skill is self-contained. Take only the ones that match your work.

## Two audiences

The library is built for two kinds of reader, and it is worth starting from the one you are.

**If you run the operating layer of a company**, start with the [Chief of Staff track](chief-of-staff/README.md). Forty-four skills, opening with five that act as the Chief of Staff of a company at a specific stage, from seed through Series D, because the same title is four or five different jobs. Then the memo, the model, the board, the plan, the raise, the cadence, and the commercial document, extended by the [commercial and data track](commercial-and-data/README.md) into revenue and client analytics, content quality, account re-engagement, sales coaching, and commercial paperwork. Sixty skills in total.

**If you are doing empirical research**, start with the [PhD research track](phd-research/README.md). Forty skills covering the pipeline from a vague topic to a replication package and beyond it into examining and refereeing, with the standard a referee applies built into each stage. Quantitative and qualitative: preregistration, instrument design, coding, systematic review, ethics, a research assistant working to your brief, and a full econometrics workbench covering do-file craft, data management, estimator choice, table production, the Python equivalent, and an audit that rebuilds the headline number from raw data.

**Either way**, two tracks apply. The [brand and writing track](brand-and-writing/README.md), because a board memo and a discussion section fail in the same ways, and it includes the one that teaches you to write your own skills. And the [web and presentation track](web-and-presentation/README.md), for the point at which the work has to be seen by someone who was not involved in it: a paper's companion site, a results explorer, an academic homepage, a metrics page a team will actually use.

I use both halves in the same week, which is the reason they sit in one repository. The discipline is identical: structure the mess, attach evidence to every claim, hand someone a document they can act on.

## Start here

Reading a hundred and ten files is not the way in. Take one, run it on work you are already doing this week, and see whether the output is better than what you would have got without it.

| If you are | Start with | Because |
| --- | --- | --- |
| A Chief of Staff or operator | [chief-of-staff-by-stage](chief-of-staff/chief-of-staff-by-stage/SKILL.md) | The role is four different jobs depending on company stage, and most of the unhappiness in it comes from doing the previous stage's version well. Then take the playbook for your stage, from [seed](chief-of-staff/cos-at-seed/SKILL.md) to [Series D](chief-of-staff/cos-at-series-d/SKILL.md) |
| New in the role, or scoping it | [structured-problem-solving](chief-of-staff/structured-problem-solving/SKILL.md) | The thinking layer everything else sits on: find the decision, structure before gathering, commit to an answer early, then synthesise rather than summarise |
| Running a sales or revenue function | [pipeline-deep-dive](chief-of-staff/pipeline-deep-dive/SKILL.md) | It turns a CRM export into coverage, conversion, velocity, concentration, and an action list with owners |
| A doctoral student starting a paper | [research-design](phd-research/research-design/SKILL.md) | It forces the one-page design, with hypotheses mapped to exhibits and a kill criterion, before any estimation |
| Writing up results you already have | [results-writing](phd-research/results-writing/SKILL.md) | Findings first, magnitudes translated, causal language calibrated to what the design supports |
| Handed a spreadsheet you did not build | [spreadsheet-analysis-workbook](commercial-and-data/spreadsheet-analysis-workbook/SKILL.md) | It is the sequence that stops you answering confidently from a column you have misunderstood |
| Deep in a doctoral thesis | [thesis-advisor](phd-research/thesis-advisor/SKILL.md) | It takes a supervisor's position on what to do next and what to cut, against the time that actually remains |
| Asking a leadership team for something | [principal-simulator](chief-of-staff/principal-simulator/SKILL.md) | It plays the executive you are writing to, so the objection arrives before the meeting does |
| Executing research for someone else | [research-assistant](phd-research/research-assistant/SKILL.md) | The habits that make a supervisor able to trust the output without redoing it, starting with never inventing anything |
| Running the empirical work | [econometrician](phd-research/econometrician/SKILL.md) | Estimator choice, the clustering level, and which diagnostics are worth running, before the paper gets written |
| Checking an analysis before it ships | [analysis-audit](phd-research/analysis-audit/SKILL.md) | Rebuild the headline number from raw data and trace every number in the text to a file that produced it |
| Needing the work to be seen | [research-paper-website](web-and-presentation/research-paper-website/SKILL.md) | The companion page for a paper, built as static files that will still open in ten years |
| Wanting to write your own | [skill-builder](brand-and-writing/skill-builder/SKILL.md) | It is the method behind every file here, including how to phrase a description so the skill actually loads |

## The catalog

All 110 skills are built. Each row links to the skill.

### [Chief of Staff track (44)](chief-of-staff/README.md)

| # | Skill | What it enforces | Status |
| --- | --- | --- | --- |
| 1 | [chief-of-staff-by-stage](chief-of-staff/chief-of-staff-by-stage/SKILL.md) | What the role actually is at seed, Series A, B, C and beyond, and what to stop doing | built |
| 2 | [cos-at-seed](chief-of-staff/cos-at-seed/SKILL.md) | Five to thirty people, nothing exists, and the founder is the routing table for every decision | built |
| 3 | [cos-at-series-a](chief-of-staff/cos-at-series-a/SKILL.md) | Thirty to a hundred, the seed systems are breaking, and everything owned has to be handed over | built |
| 4 | [cos-at-series-b](chief-of-staff/cos-at-series-b/SKILL.md) | A hundred to three hundred, no functions owned, synthesis across a leadership team that now exists | built |
| 5 | [cos-at-series-c](chief-of-staff/cos-at-series-c/SKILL.md) | A written mandate, governance becoming real, and professionalising without killing the speed | built |
| 6 | [cos-at-series-d](chief-of-staff/cos-at-series-d/SKILL.md) | Acting in place of the chief executive inside an authority that is written down and reviewed | built |
| 7 | [structured-problem-solving](chief-of-staff/structured-problem-solving/SKILL.md) | Find the decision, a MECE tree, a day-one hypothesis attacked not defended, synthesis, answer first | built |
| 8 | [program-management](chief-of-staff/program-management/SKILL.md) | Single owners, dated milestones, honest status, decision logs, recovery of slipping programs | built |
| 9 | [market-research](chief-of-staff/market-research/SKILL.md) | Two-method market sizing, sourced competitor tables, research framed by the decision it feeds | built |
| 10 | [ideation-deck](chief-of-staff/ideation-deck/SKILL.md) | Raw idea to decision-ready concept deck: options, evidence, pilot metric, kill criterion, ask | built |
| 11 | [tailored-client-deck](chief-of-staff/tailored-client-deck/SKILL.md) | Client-specific decks rebuilt around one account, with correct logo and co-branding handling | built |
| 12 | [outreach-email](chief-of-staff/outreach-email/SKILL.md) | Research-first B2B outreach and follow-ups, ZoomInfo-grounded when connected | built |
| 13 | [external-insights](chief-of-staff/external-insights/SKILL.md) | Outside-in intelligence briefs, verified and dated, before any meeting or pitch | built |
| 14 | [pipeline-deep-dive](chief-of-staff/pipeline-deep-dive/SKILL.md) | Coverage, conversion, velocity, concentration, hygiene, three-way forecast, action list | built |
| 15 | [executive-briefing](chief-of-staff/executive-briefing/SKILL.md) | One-page briefs for a leader walking into a meeting cold | built |
| 16 | [decision-memo](chief-of-staff/decision-memo/SKILL.md) | A closed question, the recommendation first, reversibility stated, one named decider | built |
| 17 | [board-deck](chief-of-staff/board-deck/SKILL.md) | Board materials with headline titles, one idea per page, decisions requested | built |
| 18 | [board-and-investor-management](chief-of-staff/board-and-investor-management/SKILL.md) | A pre-read that gets read, decisions pre-wired, and no director surprised in the room | built |
| 19 | [investor-update](chief-of-staff/investor-update/SKILL.md) | Monthly and quarterly investor updates: metrics, wins, misses, asks | built |
| 20 | [weekly-status-update](chief-of-staff/weekly-status-update/SKILL.md) | Three-line workstream status and the exceptions-only leadership summary | built |
| 21 | [meeting-to-decisions](chief-of-staff/meeting-to-decisions/SKILL.md) | Notes or transcripts into decisions, owners, dates, and a circulated summary | built |
| 22 | [operating-cadence-design](chief-of-staff/operating-cadence-design/SKILL.md) | Designing the weekly, monthly, and quarterly rhythm of a company | built |
| 23 | [strategic-plan-and-action-plan](chief-of-staff/strategic-plan-and-action-plan/SKILL.md) | One destination, a few falsifiable bets, what will not be done, dated owners | built |
| 24 | [okr-planning](chief-of-staff/okr-planning/SKILL.md) | Objectives and key results that are measurable, owned, and few | built |
| 25 | [annual-planning-and-headcount](chief-of-staff/annual-planning-and-headcount/SKILL.md) | Top down meets bottom up, hires sequenced by output, and the pause trigger written early | built |
| 26 | [financial-model-builder](chief-of-staff/financial-model-builder/SKILL.md) | Driver-based financial models with stated assumptions and scenario toggles | built |
| 27 | [pricing-and-resourcing-model](chief-of-staff/pricing-and-resourcing-model/SKILL.md) | Engagement pricing, staffing, ramp, and margin models for services businesses | built |
| 28 | [revenue-forecast](chief-of-staff/revenue-forecast/SKILL.md) | Annual revenue forecast from pipeline, run-rate, and capacity, board-ready | built |
| 29 | [fundraise-readiness](chief-of-staff/fundraise-readiness/SKILL.md) | One definition per metric, a data room that answers before it is asked, weaknesses named first | built |
| 30 | [pitch-deck](chief-of-staff/pitch-deck/SKILL.md) | The argument for a commitment: why now, the insight, a bottom-up market, a specific ask | built |
| 31 | [proposal-writer](chief-of-staff/proposal-writer/SKILL.md) | Client proposals structured by what the client needs to decide | built |
| 32 | [sow-and-scope](chief-of-staff/sow-and-scope/SKILL.md) | Statements of work with explicit scope, exclusions, assumptions, and acceptance | built |
| 33 | [hiring-scorecard-and-interview-kit](chief-of-staff/hiring-scorecard-and-interview-kit/SKILL.md) | Role scorecards, structured interview questions, and evaluation rubrics | built |
| 34 | [onboarding-plan](chief-of-staff/onboarding-plan/SKILL.md) | 30-60-90 day plans with owners, milestones, and check-ins | built |
| 35 | [process-documentation-sop](chief-of-staff/process-documentation-sop/SKILL.md) | Standard operating procedures that someone new can follow without asking | built |
| 36 | [ai-adoption-program](chief-of-staff/ai-adoption-program/SKILL.md) | A capability audit, two or three measured pilots, and a policy written before the tools arrive | built |
| 37 | [vendor-evaluation](chief-of-staff/vendor-evaluation/SKILL.md) | Vendor comparison with total cost, risk, and negotiation points | built |
| 38 | [partnership-assessment](chief-of-staff/partnership-assessment/SKILL.md) | Strategic partnership evaluation: fit, economics, governance, exit | built |
| 39 | [competitive-battlecard](chief-of-staff/competitive-battlecard/SKILL.md) | Evidence-based battlecards: positioning, pricing, objections, traps | built |
| 40 | [customer-interview-synthesis](chief-of-staff/customer-interview-synthesis/SKILL.md) | Interview notes into themes, frequency, and roadmap implications | built |
| 41 | [event-and-offsite-planning](chief-of-staff/event-and-offsite-planning/SKILL.md) | Agendas, logistics, outcomes, and follow-up for events and leadership offsites | built |
| 42 | [ceo-communications](chief-of-staff/ceo-communications/SKILL.md) | Talking points, all-hands scripts, and internal announcements in the CEO's voice | built |
| 43 | [crisis-and-incident-comms](chief-of-staff/crisis-and-incident-comms/SKILL.md) | Stakeholder communication under pressure: what to say, to whom, when | built |
| 44 | [principal-simulator](chief-of-staff/principal-simulator/SKILL.md) | Playing the executive you support, so the objection arrives before the meeting does | built |

### [PhD research track (40)](phd-research/README.md)

| # | Skill | What it enforces | Status |
| --- | --- | --- | --- |
| 45 | [research-question-ideation](phd-research/research-question-ideation/SKILL.md) | From topic to candidate questions with novelty check and feasibility triage | built |
| 46 | [research-design](phd-research/research-design/SKILL.md) | A written one-page design before estimation: question, hypotheses, identification, kill criteria | built |
| 47 | [preregistration-and-analysis-plan](phd-research/preregistration-and-analysis-plan/SKILL.md) | Specific enough that two analysts get the same result, written before outcomes are seen | built |
| 48 | [research-ethics-and-data-protection](phd-research/research-ethics-and-data-protection/SKILL.md) | Consent that informs, anonymisation that survives combination, a data plan that is operational | built |
| 49 | [literature-verification](phd-research/literature-verification/SKILL.md) | No citation enters a draft until verified; reviews built from an evidence matrix | built |
| 50 | [systematic-review-protocol](phd-research/systematic-review-protocol/SKILL.md) | A registered protocol, search strings that rerun exactly, and counts that reconcile | built |
| 51 | [theoretical-framework-review](phd-research/theoretical-framework-review/SKILL.md) | Referencial teórico built or diagnosed mechanism by mechanism, Consensus-grounded when connected | built |
| 52 | [survey-and-instrument-design](phd-research/survey-and-instrument-design/SKILL.md) | Constructs before questions, validated scales where they exist, cognitive interviews before fielding | built |
| 53 | [data-profiling-and-cleaning](phd-research/data-profiling-and-cleaning/SKILL.md) | Profiling a research dataset: missingness, outliers, codebook checks, panel coherence | built |
| 54 | [stata-project-scaffold](phd-research/stata-project-scaffold/SKILL.md) | Numbered do-file skeleton from setup to first regressions | built |
| 55 | [stata-do-file-craft](phd-research/stata-do-file-craft/SKILL.md) | Do-files another person can run from a clean session, logged, asserted, never hand-edited | built |
| 56 | [stata-data-management](phd-research/stata-data-management/SKILL.md) | Merges with match rates, labels, dates, panel checks, and raw files never overwritten | built |
| 57 | [python-for-econometrics](phd-research/python-for-econometrics/SKILL.md) | The same work in Python, and an honest account of when it beats Stata and when it does not | built |
| 58 | [research-assistant](phd-research/research-assistant/SKILL.md) | Working to a brief, a log written as you go, nothing invented, and the dead ends reported | built |
| 59 | [econometrician](phd-research/econometrician/SKILL.md) | Choosing the estimator, the clustering level, and which diagnostics are worth running | built |
| 60 | [econometric-model-writer](phd-research/econometric-model-writer/SKILL.md) | The empirical strategy section: equation, terms, assumptions, threats, clustering | built |
| 61 | [identification-defense](phd-research/identification-defense/SKILL.md) | Defending DiD, IV, RDD, and matching designs to a committee or referee | built |
| 62 | [qualitative-coding-and-analysis](phd-research/qualitative-coding-and-analysis/SKILL.md) | A codebook with boundary rules, agreement measured, negative cases sought, an audit trail | built |
| 63 | [descriptive-statistics-tables](phd-research/descriptive-statistics-tables/SKILL.md) | Table 1 and balance tables that are honest and journal-ready | built |
| 64 | [academic-figures-monochrome](phd-research/academic-figures-monochrome/SKILL.md) | Print-safe figures with series separated by pattern and marker, legend outside the plot | built |
| 65 | [academic-tables-booktabs](phd-research/academic-tables-booktabs/SKILL.md) | Regression and summary tables with three rules and no vertical lines | built |
| 66 | [regression-table-production](phd-research/regression-table-production/SKILL.md) | Estimation output into a table a journal will print, with a note that carries the design | built |
| 67 | [analysis-audit](phd-research/analysis-audit/SKILL.md) | Rebuilding the headline number from raw data and tracing every number in the text to a file | built |
| 68 | [full-manuscript-build](phd-research/full-manuscript-build/SKILL.md) | The whole paper written in the right order, then ten checks on the seams | built |
| 69 | [introduction-writer](phd-research/introduction-writer/SKILL.md) | The five moves: problem, gap, what the paper does, what it finds, contribution | built |
| 70 | [data-section-writer](phd-research/data-section-writer/SKILL.md) | Sources, sample construction with counts, variable definitions, availability statement | built |
| 71 | [results-writing](phd-research/results-writing/SKILL.md) | Findings first, magnitudes translated, causal language calibrated, honest nulls | built |
| 72 | [discussion-and-conclusion](phd-research/discussion-and-conclusion/SKILL.md) | Restating at the level of the question, mechanisms, limitations, sized implications | built |
| 73 | [abstract-and-title](phd-research/abstract-and-title/SKILL.md) | Abstracts traceable to results, titles that state the finding, keywords and JEL codes | built |
| 74 | [references-and-bibliography](phd-research/references-and-bibliography/SKILL.md) | Style conversion (APA, Chicago, ABNT, house styles), BibTeX hygiene, DOI checks | built |
| 75 | [journal-targeting](phd-research/journal-targeting/SKILL.md) | Scope fit, indexing checks, predatory screening, a ranked submission ladder | built |
| 76 | [peer-review-simulator](phd-research/peer-review-simulator/SKILL.md) | Adversarial pre-submission review from methodologist, field expert, and editor | built |
| 77 | [response-to-reviewers](phd-research/response-to-reviewers/SKILL.md) | Point-by-point responses and revision plans for a revise-and-resubmit | built |
| 78 | [refereeing-for-a-journal](phd-research/refereeing-for-a-journal/SKILL.md) | Writing the referee report when you are the reviewer, with scope creep resisted | built |
| 79 | [conference-presentation-deck](phd-research/conference-presentation-deck/SKILL.md) | Research talks that lead with the finding and survive a hostile Q&A | built |
| 80 | [thesis-advisor](phd-research/thesis-advisor/SKILL.md) | A supervisor's position on what to do next, what to cut, and when to start writing | built |
| 81 | [thesis-chapter-review](phd-research/thesis-chapter-review/SKILL.md) | An examiner's reading, with the fatal separated from the fixable and the optional | built |
| 82 | [thesis-defense-prep](phd-research/thesis-defense-prep/SKILL.md) | Committee questions, identification challenges, and answer rehearsal | built |
| 83 | [research-proposal-and-grant](phd-research/research-proposal-and-grant/SKILL.md) | Proposals with a question, hypotheses, design, timeline, and budget | built |
| 84 | [replication-package](phd-research/replication-package/SKILL.md) | Code, data, and documentation organized so a stranger can reproduce every table | built |

### [Brand and writing track (6)](brand-and-writing/README.md)

| # | Skill | What it enforces | Status |
| --- | --- | --- | --- |
| 85 | [breaktalk-brand](brand-and-writing/breaktalk-brand/SKILL.md) | The BreakTalk identity: logo rules, monochrome palette with navy and wine, typography, layout, voice | built |
| 86 | [newsletter-post-writer](brand-and-writing/newsletter-post-writer/SKILL.md) | Long-form posts that open on a scene, argue with evidence, and end on the point | built |
| 87 | [linkedin-post-writer](brand-and-writing/linkedin-post-writer/SKILL.md) | 120 to 300 word posts with one idea and no engagement bait | built |
| 88 | [human-voice-editor](brand-and-writing/human-voice-editor/SKILL.md) | Removing the punctuation, vocabulary, and rhythm tells of generated prose | built |
| 89 | [skill-builder](brand-and-writing/skill-builder/SKILL.md) | How to write a skill that triggers reliably and enforces a standard | built |
| 90 | [weekly-review-and-planning](brand-and-writing/weekly-review-and-planning/SKILL.md) | A personal operating rhythm for people running two jobs | built |

### [Commercial and data track (16)](commercial-and-data/README.md)

| # | Skill | What it enforces | Status |
| --- | --- | --- | --- |
| 91 | [content-quality-gate](commercial-and-data/content-quality-gate/SKILL.md) | Nine checks every piece of buyer-facing content clears before it ships | built |
| 92 | [account-reengagement-plan](commercial-and-data/account-reengagement-plan/SKILL.md) | Restarting a paused account: diagnosis before proposal, objection playbook, rehearsal personas | built |
| 93 | [client-economics-analysis](commercial-and-data/client-economics-analysis/SKILL.md) | Lifetime value, health scoring, cost of loss, whitespace, net revenue retention, per client | built |
| 94 | [economics-report-from-data](commercial-and-data/economics-report-from-data/SKILL.md) | Four levels of analysis, seven economic frameworks, traceable and falsifiable claims | built |
| 95 | [contractor-msa-and-task-order](commercial-and-data/contractor-msa-and-task-order/SKILL.md) | The two contractor documents, in the right order, with full clause anatomy | built |
| 96 | [sales-roleplay](commercial-and-data/sales-roleplay/SKILL.md) | A buyer who does not volunteer pain, and coaching that hands over exact language | built |
| 97 | [image-to-spreadsheet](commercial-and-data/image-to-spreadsheet/SKILL.md) | Transcription with nothing invented, and chart estimates labelled as estimates | built |
| 98 | [spreadsheet-analysis-workbook](commercial-and-data/spreadsheet-analysis-workbook/SKILL.md) | Reading someone else's workbook before trusting it, and building tabs that reconcile | built |
| 99 | [revenue-analysis-workbook](commercial-and-data/revenue-analysis-workbook/SKILL.md) | The seven standard tabs, every figure a live formula, a verification tab that proves it | built |
| 100 | [revenue-concentration-risk](commercial-and-data/revenue-concentration-risk/SKILL.md) | Share weighted by how hard it is to leave, and what losing each account really costs | built |
| 101 | [expected-revenue-estimation](commercial-and-data/expected-revenue-estimation/SKILL.md) | Five methods ranked by reliability, three scenarios, sensitivity, and an update trigger | built |
| 102 | [discovery-to-proposal-deck](commercial-and-data/discovery-to-proposal-deck/SKILL.md) | Discovery played back in the client's words before any solution is proposed | built |
| 103 | [business-agreements-drafting](commercial-and-data/business-agreements-drafting/SKILL.md) | Equity, employment, NDA, partnership, and vendor agreements with the risk flags surfaced | built |
| 104 | [sales-call-analysis](commercial-and-data/sales-call-analysis/SKILL.md) | Four passes over the transcript, and nothing established on a seller assertion | built |
| 105 | [demo-call-transcript-generator](commercial-and-data/demo-call-transcript-generator/SKILL.md) | Synthetic call histories where partial evidence is correct rather than a gap | built |
| 106 | [sales-team-competency-assessment](commercial-and-data/sales-team-competency-assessment/SKILL.md) | Self and leadership scores blended, with the perception gap as the coaching signal | built |

### [Web and presentation track (4)](web-and-presentation/README.md)

| # | Skill | What it enforces | Status |
| --- | --- | --- | --- |
| 107 | [research-paper-website](web-and-presentation/research-paper-website/SKILL.md) | The plain-language finding, the figures, the data and the citation, as files that outlive frameworks | built |
| 108 | [interactive-results-explorer](web-and-presentation/interactive-results-explorer/SKILL.md) | The rows shipped with the page, uncertainty on every estimate, and axes that stay honest | built |
| 109 | [academic-personal-site](web-and-presentation/academic-personal-site/SKILL.md) | What a committee, an editor and a collaborator each came for, and nothing else | built |
| 110 | [metrics-dashboard-page](web-and-presentation/metrics-dashboard-page/SKILL.md) | Five to nine measures a decision depends on, each with a definition, an owner and a comparison | built |

## How a skill is written

Every file follows one structure, set out in [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md): when to use it and when not to, the inputs it needs with a rule for what to do when one is missing, the method with its decision rules stated rather than implied, at least one worked example in situation, task, action, result form with real numbers and a wrong turn that was abandoned, a second scenario where the method behaves differently, the output shape close enough to copy, the failure modes with how to recognise each one, the edge cases, a quality bar you can check by reading the output, and the related skills.

The worked example is the part that makes a skill useful rather than merely correct. Abstract instructions produce abstract output. A scenario with a number in it, a constraint, and a decision that turned out wrong shows the judgement the numbered steps cannot carry.

## Adapting a skill

These encode my standards, which came from a B2B services company and an economics doctorate. Yours will differ, and the version you edit is worth more to you than the version you installed. Every skill now carries an **Adapting this to your context** section naming its own assumptions, and the full method is in [USING_THESE_SKILLS.md](USING_THESE_SKILLS.md).

The idea in one paragraph. Every file here has three layers. The **method** is the sequence that would hold in any organisation, and it is why the file exists. The **defaults** are every number, cadence, threshold, currency, org shape and tool, and they came from one setting, so they should almost always be changed. The **illustration** is the worked example, which exists to show the method moving and can be replaced wholesale. The adaptation section in each file names its own defaults and illustration, and states what belongs to the method under the label **What not to change**.

A quick test for telling them apart: cover every number in a step with your hand. If the step still tells you what to do, it is method. If it becomes meaningless, the number was doing the work, so it needs to be your number.

The order that works, in about forty minutes:

1. Read three sections, not the whole file: when to use it, what you need before starting, and the quality bar.
2. Rewrite the quality bar first. It is the shortest section and it governs the rest.
3. Replace the defaults with figures from your own history, not from your instinct about your own history.
4. Decide what happens when each input is missing: proceed and flag, proceed on a stated assumption, or stop.
5. Delete what does not apply. A shorter file that fits beats a complete file that does not.
6. Replace the worked example with one of your own. This is the strongest edit and the one people skip.
7. Give it to somebody else and do not help them.

Where a skill expects a local file, such as a standards file or a competency framework, write yours. Those exist so the method can be public while the specifics stay yours. [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) is the empty shape if you would rather start from scratch, and [skill-builder](brand-and-writing/skill-builder/SKILL.md) is the skill that writes skills.

**If you work outside economics**, the research track will name tools and conventions you do not use. Separate the rule from the dialect: "raw data is never edited, every dropped row is counted, every merge is followed by an assertion on the match rate" holds in R, SPSS, SAS or by hand, and only the syntax is Stata. Substitute the standard rather than the step: APA where a file says booktabs, MeSH or PsycINFO or ERIC descriptors where it says JEL codes, OSF or PROSPERO or ClinicalTrials.gov where it says the AEA RCT Registry. Each software and reporting skill now carries that split explicitly.

## What these are not

They are not prompts, and they are not a personality. A skill does not make a model know more. It makes it work to a standard, in a repeatable way, so the tenth market analysis follows the same method as the first. That is why they are not tied to one assistant: a written method is portable, and a clever prompt for one model usually is not.

There is nothing here for taste, judgment, or relationships. I do not believe instructions enforce those, and a skill that claims to would be teaching you to trust something that has not earned it.

Nothing in this repository contains employer or client material. Where I had built a private version against a specific firm's frameworks, clients, and approved claims, the public skill is the method rewritten from scratch with those removed. That test, whether the value sits in the method or in the material, is worth running on your own library before you publish any of it.

## Why these hundred and ten

They are the tasks I repeat most, and the tasks where quality depends on discipline rather than inspiration: a market analysis is good because every number has a source, a results section is good because the causal language matches the design. That kind of quality is exactly what instructions can enforce. Skills for taste, judgment, or relationships are not in this library because I do not believe they work.

Nothing in the commercial and data track is an employer artefact. Where I had built a private version against a specific firm's frameworks, clients, and approved claims, the public skill is the method rewritten from scratch with the organisation's specifics moved into a local file the user supplies.

## A run from end to end

Every skill carries a worked example inside its own file. [`examples/`](examples/) holds something the skill files cannot: a complete run, starting from the messy brief a person actually receives, through what came back, to the two points where the method refused the request and produced a better document for it.

[A decision that had been deferred three times](examples/decision-memo-end-to-end.md) is the first. The interesting part of it is not the memo at the end. It is that the first thing the skill returned was a question rather than a document.

## The catalog as data

[`skills.json`](skills.json) and [`skills.csv`](skills.csv) carry every skill with its name, track, path and description, generated from the frontmatter rather than maintained by hand. Use them to build your own index, filter the library down to the tracks you want, or script an install.

[`scripts/validate_skills.py`](scripts/validate_skills.py) checks the library against its own standard: frontmatter present, the name matching the folder, a when to use section, a worked example, a quality bar, an adaptation section naming the file's own defaults and what must not change, a size floor that a stub cannot pass, and no dashes. It runs in a second and exits non zero on failure, so nothing ships below the bar.

```
python3 scripts/validate_skills.py
checked 110 skills across 5 tracks
all skills pass the house standard
```

## Releases and contributions

New skills and revisions are announced on [BreakTalk](https://breaktalk.substack.com). Each release attaches the skills zipped individually for upload, alongside the whole library in one archive.

If you improve one, [CONTRIBUTING.md](CONTRIBUTING.md) says how to send it back. Issues are open for anything that is wrong, unclear, or missing.

## License

MIT. Use them, fork them, adapt them to your own standards. If you improve one, I would like to see it.

Ingrid Rafaele Rodrigues Leiria
[LinkedIn](https://www.linkedin.com/in/ingrid-leiria-25b4767a) | [BreakTalk](https://breaktalk.substack.com) | [GitHub](https://github.com/ingridleiria) | [ingrid@leiriaconsulting.com](mailto:ingrid@leiriaconsulting.com)
