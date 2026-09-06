---
name: process-documentation-sop
description: Documents business processes as standard operating procedures that someone new can follow without asking: purpose, trigger, owner, roles, step-by-step instructions with the exact systems and inputs, decision points, exceptions, quality checks, timing, and a change log; also maps the current process before writing to expose the gaps. Use this skill whenever the user asks to document a process, write an SOP or runbook, "write down how we do X", capture what someone does before they leave, create a checklist, or standardize a task across people. Trigger whenever knowledge lives in one person's head and needs to survive their absence.
---

# Process Documentation, SOP

A process that lives in someone's head is a risk with a name. Documenting it does two things: it lets a new person do the work without interrupting the expert, and it exposes the steps that only worked because the expert was quietly compensating for a gap. The second is usually the more valuable.

## Step 1: Map before writing

Interview the person who does the work (or observe it) and build the map:

- **Trigger**: what starts the process (a date, a request, an event, a threshold).
- **Steps** in order, each with who does it, in which system, with what input, producing what output, taking how long.
- **Decision points**: where the path branches and the rule that decides.
- **Handoffs**: where the work moves between people or teams, and how the receiver knows it has arrived.
- **Exceptions**: the cases that do not fit, and what actually happens (often the most interesting part).
- **Failure history**: where it has gone wrong before and why.

Draw the map as a simple flow (a numbered list or a swimlane diagram) and confirm it with the expert. Ask about each step: why is this here, what happens if it is skipped, who else can do it. Steps nobody can justify are candidates for removal; the process gets fixed before it gets documented, within reason.

## Step 2: The SOP document

1. **Title and identifier**: process name, version, owner, date of last review.
2. **Purpose**: one paragraph, what the process achieves and for whom.
3. **Scope**: what is covered and what is not; related processes named.
4. **Trigger and timing**: when it starts, how often it runs, and the deadline or service level it must meet.
5. **Roles**: each role involved with its responsibilities; use roles rather than names, with a current-holder table that can be updated.
6. **Inputs and prerequisites**: what must exist before starting (data, approvals, access).
7. **Procedure**: numbered steps, one action each, in the imperative, with the exact system, menu, or template named, screenshots where the interface is not obvious, and the expected result stated so the person knows they succeeded. Decision points written as "If X, go to step N; otherwise continue."
8. **Exceptions**: the known non-standard cases and how to handle each, plus the escalation path for the unknown ones.
9. **Quality checks**: what to verify before declaring the process complete, and what a correct output looks like.
10. **Outputs and records**: what is produced, where it is stored, who is notified.
11. **Metrics**: how the process's performance is measured (cycle time, error rate, volume), if measured.
12. **Change log**: date, change, author, so the document's history is visible.

## Writing rules

- Written for a competent person who has never done this task; assume no tribal knowledge.
- One action per step. "Export the report and email it to finance" is two steps.
- Names of systems, buttons, folders, templates, and fields, exactly as they appear.
- Time estimates per step or phase, so the reader can plan.
- The expected result after each significant step, so errors are caught where they happen.
- Plain language; no internal jargon without definition.

## The test

Before publishing, someone who has not done the process follows the document while the author watches without helping. Every question they ask is a gap in the document. Fix the gaps, then publish. A document that has not been tested this way is a draft.

## Maintenance

Each SOP has an owner and a review date (quarterly for volatile processes, annually for stable ones). Changes to systems or roles trigger a review. Retired processes are marked as such, not deleted, so history remains.

## Checklist variant

For simple, frequent processes, produce a one-page checklist derived from the procedure: the steps as checkboxes, the quality checks at the end, the owner and date fields. The full SOP remains the reference.

## Deliverables

The process map, the SOP document (with the environment's document skill when a file is needed), the checklist where useful, and a short list of process improvements identified during mapping, with the owner's agreement on which to adopt.

## Quality bar

- A new person completed the process from the document without asking a question.
- Every step names the system and the expected result.
- Exceptions and escalation are documented.
- The document has an owner, a version, and a review date.
