# Worked runs

Each skill carries its own worked example inside `SKILL.md`, and the validator refuses to ship one that does not.
This folder holds something different: a complete run, from the messy input a person actually has, through what the
assistant produced, to the places where the skill overruled the request and why that was the right outcome.

The point of these is not the output. It is the middle column: what a written method does that a good prompt does
not, which is refuse to give you what you asked for when what you asked for was the wrong shape.

| Run | Skill | What it demonstrates |
| --- | --- | --- |
| [A decision that had been deferred three times](decision-memo-end-to-end.md) | [decision-memo](../chief-of-staff/decision-memo/SKILL.md) | The skill rejecting the question it was given, and the memo that ended the loop |

More of these are being added. If you run one of these skills on real work and the result is worth showing, with
everything identifying removed, [CONTRIBUTING.md](../CONTRIBUTING.md) says how to send it.
