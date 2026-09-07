# Using these skills, and making them yours

Every file in this library is a written method. It came out of two jobs, an operating role in a B2B services company and an empirical economics doctorate, and it carries the assumptions of those two jobs whether or not it says so. That is not a defect you should work around. It is the normal condition of any method that came from somewhere, and it is the reason this page exists.

The short version: run one file unchanged on work you have already done, see where it disagrees with you, and edit it. That loop is the whole product. What follows is the longer version.

---

## Part one: getting a skill running

A skill is a folder with a `SKILL.md` file in it. The file is plain Markdown. There is nothing to install.

**Claude.** On claude.ai, go to Settings, Capabilities, Skills, and upload the skill folder as a zip. In Claude Code, copy the folder into `.claude/skills/` in your project, or `~/.claude/skills/` to have it everywhere. Each skill is also published zipped individually on the releases page.

**ChatGPT.** Paste the body of the `SKILL.md` into a Project's instructions, or into the instructions of a custom GPT, and name the GPT after the skill so you can find it again. For a one-off, paste the file at the top of a new conversation and then give it your material.

**Gemini, Copilot, Mistral, or anything else that takes written instructions.** Paste the body into the system prompt, the custom instructions, or the top of the conversation. A Gem works the same way as a custom GPT.

**Coding assistants.** The same text works as a rules file, for example in `.cursor/rules/` or `.github/copilot-instructions.md`, for the skills that produce written deliverables inside a repository.

**Your own tooling or the API.** Send the body as the system prompt for that task.

**No assistant at all.** Read it and follow it. Several of these were written for people before they were written for models, and the checklists work on paper.

Two notes for the non-Claude routes. The frontmatter `description` is what decides whether Claude loads a skill automatically. Everywhere else you are choosing the file yourself, so that block can be dropped, though it is a useful summary of when to reach for it. And where a skill talks about reading or writing files, hand the assistant the material directly instead.

Several skills use connected tools where they exist, a data provider for account research, an academic search tool for literature, a CRM for pipeline data, and fall back to web research or to what you paste in when they do not. None of them require a paid tool.

---

## Part two: your first run

Do not read the library. Take one file.

Pick a piece of work you have **already finished**, where you know what good looked like. Run the skill on it. Then compare the output to what you actually produced.

You are looking for three things, and all three are useful:

- **Places the skill caught something you missed.** Keep the file.
- **Places the skill is wrong for your setting.** That is your first edit, and part three tells you how to make it.
- **Places the skill asked for an input you do not have.** That is either a gap in your data or a default the file should not have assumed. Both are worth knowing before a live deadline.

Running a method for the first time on live work, against a deadline, is how people conclude that written methods do not help. Run it once on something finished, where being wrong costs nothing.

---

## Part three: the three layers, and which ones you change

Every file here has three layers stacked on top of each other, and the whole art of adopting somebody else's method is telling them apart.

**Layer one, the method.** The sequence, the order of operations, the thing that would be true in any organisation. Sizing a market two independent ways and treating the gap between them as the interesting part. Counting every row you drop from a dataset. Naming the decision before producing the analysis. This layer is why the file exists, and if you change it you are no longer running this method, you are running yours, which is allowed but should be a decision rather than an accident.

**Layer two, the defaults.** Every number, cadence, threshold, currency, org shape and tool. Sixteen billable days a month. A quarterly board pack of fifteen to twenty five pages. Clustering thresholds. A minimum cell size of five. These came from one setting and they should almost always be changed. A default you have not examined is a borrowed opinion.

**Layer three, the illustration.** The worked example, the second scenario, the names, the industry. These exist to show the method in motion. They are not instructions and you should feel free to ignore them entirely, or better, to replace them with a case of your own.

Each file now carries an **Adapting this to your context** section that names its own layer two and layer three, and states plainly what belongs to layer one under the label **What not to change**. Read that section second, straight after **When to use this, and when not to**, and before the method.

**A quick test for telling the layers apart.** Cover every number in a step with your hand. If the step still tells you what to do, you are looking at layer one. If it becomes meaningless, the number was doing the work and it is layer two, so it needs to be your number.

---

## Part four: making a skill yours, in about forty minutes

1. **Read three sections, not the whole file.** When to use this, What you need before starting, and the Quality bar. If the quality bar is not the standard you are actually held to, that is the first thing to change, because everything upstream of it is in service of it.

2. **Rewrite the quality bar first.** It is the shortest section and it governs the rest. Make every line checkable by someone reading the output who was not involved in producing it. If a line cannot be checked that way, it is decoration.

3. **Replace the defaults.** Go through the Adapting section, take each number and each cadence, and either substitute yours or write down that you are keeping it and why. Your figures should come from your own history, not from your instinct about your own history. Two quarters of timesheets beat a feeling about billable days.

4. **Write your missing input rules.** For every input the file lists, decide now what happens when it is absent: proceed and flag, proceed on a stated assumption, or stop. Deciding in advance is the difference between a file that produces useful work and a file that produces confident rubbish.

5. **Delete what does not apply.** A shorter file that fits your situation beats a complete file that does not. Cut whole steps if your work does not contain them. Nobody is grading completeness.

6. **Replace the worked example with one of your own.** This is the strongest single edit and the one people skip. Take something you did last quarter, write it up in the same shape, situation, task, action including the approach you abandoned, result with real numbers. The file becomes yours at the moment its example is yours, and anyone else on your team will trust it more because they were there.

7. **Give it to somebody else and do not help them.** Whatever comes back is the real edit list.

---

## Part five: when a skill is too specific

Some of these are narrow, and the research track is the narrowest, because it was written by an economist who works in Stata. If you are in psychology, education, public health, sociology or a qualitative field, several files will name a tool you do not use and a convention your reviewers do not follow.

The method usually survives the translation even when the syntax does not. Work through it like this:

- **Separate the rule from the dialect.** "Raw data is never edited, every dropped row is counted and logged, every merge is followed by an assertion on the match rate, one script rebuilds everything from raw" is a rule and it holds in R, SPSS, SAS, Python or by hand. The Stata command that implements it is dialect. The Adapting section in each of the software skills now makes that split explicitly.
- **Substitute the standard, not the step.** Where a file says booktabs, your field may say APA. Where it says JEL codes, yours may say MeSH, PsycINFO or ERIC descriptors. Where it says the AEA RCT Registry, yours may be OSF, AsPredicted, PROSPERO or ClinicalTrials.gov. The step, register the analysis plan before you see outcomes, is the same step.
- **Where the default estimator is wrong for your field, say so in the file.** Fixed effects is the economics default for a reason that is stated. If you work in education or psychology, multilevel and mixed models are yours, and the file should be edited to reflect that rather than argued with every time you use it.
- **If more than half of a file is dialect, do not adapt it. Write your own** using [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) and the [skill-builder](brand-and-writing/skill-builder/SKILL.md) skill, and take only the quality bar from the original.

## When a skill is too general

The opposite failure. If a step tells you to consider something, weigh something, or ensure something, without saying how much, how many or by when, it will not change what you do.

Fix it by attaching a number and a consequence. "Review the pipeline regularly" does nothing. "Any deal past its close date by more than thirty days comes out of the forecast until the owner gives a new date and a reason" changes the forecast. If you cannot name the threshold, you have found something worth arguing about with your team, and the argument is more valuable than the file.

---

## Part six: reading the other half of the library

The two big tracks were written for different readers, but the underlying work rhymes more than people expect, and I have taken more from the research track into my operating week than the other way around. If a file in the other track looks useful, this is roughly how the vocabulary maps.

| Operating work | Research work | What actually transfers |
| --- | --- | --- |
| The decision this analysis feeds | The research question | Both stop you producing a thorough answer to nothing |
| Two independent market sizings that must be reconciled | Two identification strategies that should agree | Triangulation, and treating the disagreement as the finding |
| Every number carries its source and its year | Every claim carries its citation, verified | The same discipline, and the same failure when it is skipped |
| A reconciliation cell that must read zero | A sample construction table where every exclusion is counted | Nothing is finished while a number is unexplained |
| The board pack pre-read | The abstract and introduction | Somebody decides whether to engage in ninety seconds |
| A pre-mortem before a launch | A preregistered analysis plan | Committing to the criteria before you can see the outcome |
| The decision log | The version-controlled analysis file | The record of what changed and why, so nobody re-argues it |
| A quality bar somebody else can check | A replication package a stranger can run | The same standard, which is that the work stands without you |

Two concrete crossings worth trying. If you run an operating team, [literature-verification](phd-research/literature-verification/SKILL.md) works on any document where somebody has asserted a number, including your own board deck, and [analysis-audit](phd-research/analysis-audit/SKILL.md) will take apart a spreadsheet you inherited. If you are a researcher, [decision-memo](chief-of-staff/decision-memo/SKILL.md) is the fastest way to stop a supervision meeting going in circles, and [meeting-to-decisions](chief-of-staff/meeting-to-decisions/SKILL.md) will do the same for a research group.

---

## Part seven: what these files quietly assume

Before you trust any file here on real work, check it against this list. These are the six things the library assumes without always saying so.

1. **A document you have never written.** Several skills expect a local reference file: a standards file, a defaults file, an approved claims register, a competency framework. Where one is missing, the skill degrades quietly rather than failing loudly. If a skill names a file you do not have, either build the minimal version first or delete the step.
2. **A tool stack.** A spreadsheet with a raw sheet and live formulas. A CRM with stage probabilities. A calendar whose blocks hold. A data warehouse with a nightly job. A licensed assessment instrument. Static hosting on a domain you control.
3. **A company shape.** B2B services or software, roughly forty to two hundred and fifty people, one seller per deal, an account team, a board. Public sector, solo practice, agency of record, marketplace, franchise, university department and NGO all need the shape substituted before the method runs.
4. **A jurisdiction and a currency.** Contract skills assume enforceable non-solicitation clauses and US early stage venture instruments. Both are wrong in several jurisdictions, California among them. Research skills assume DOI and self-archiving norms. Every worked example now names its currency, but the thresholds behind the numbers still came from one place.
5. **A data shape.** Two to three years of clean line-level history with a stable entity key. Grant funding, usage-based billing, event revenue and public sector budgets break several methods before the first tab.
6. **A cadence, and the authority to hold it.** A weekly leadership meeting, a monthly review, a quarterly board, a Monday-start week. And a reader who can decline an invitation, set a target and take a metric off a page. If you cannot do those things, the skill is describing a job you do not currently have, and that is worth knowing.

---

## Part eight: sending it back

If you adapt one of these and the adapted version is better, the pull request is welcome, and a correction is worth more than a new skill. See [CONTRIBUTING.md](CONTRIBUTING.md).

The most valuable thing you can send is the case where a file produced confident output that was wrong. That is the highest priority item in this repository, and it should be reported even if you cannot say why it happened.

Everything here is MIT licensed. Fork it, break it, and keep the version that works.
