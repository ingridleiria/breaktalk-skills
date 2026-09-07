# Brand and writing track

How to run one of these in any assistant, and how to adapt it to your own numbers, tools and field: [USING_THESE_SKILLS.md](../USING_THESE_SKILLS.md). Every skill below carries an **Adapting this to your context** section naming its own assumptions.

Six skills for the writing itself, and for the identity the writing carries. They serve both main tracks, because a board memo and a discussion section fail in the same ways.

## The skills

| # | Skill | What it enforces |
| --- | --- | --- |
| 85 | [breaktalk-brand](breaktalk-brand/SKILL.md) | The BreakTalk identity: logo rules, monochrome palette with navy and wine, typography, layout, voice |
| 86 | [newsletter-post-writer](newsletter-post-writer/SKILL.md) | Long-form posts that open on a scene, argue with evidence, and end on the point |
| 87 | [linkedin-post-writer](linkedin-post-writer/SKILL.md) | 120 to 300 word posts with one idea and no engagement bait |
| 88 | [human-voice-editor](human-voice-editor/SKILL.md) | Removing the punctuation, vocabulary, and rhythm tells of generated prose |
| 89 | [skill-builder](skill-builder/SKILL.md) | How to write a skill that triggers reliably and enforces a standard |
| 90 | [weekly-review-and-planning](weekly-review-and-planning/SKILL.md) | A personal operating rhythm for people running two jobs |

## Using them together

`skill-builder` is the one to read first if you plan to write your own. It is the method behind every other file in this repository, including the trigger phrasing in the descriptions, which is what actually decides whether a skill loads when it should.

`human-voice-editor` is the last pass on anything that will carry your name. It ships with `scripts/check_dashes.py`, which reports every em dash, en dash, and spaced hyphen used as punctuation and exits non-zero while any remain. It finds them and deliberately does not fix them, because swapping a comma in for every dash produces a tell of its own.

`breaktalk-brand` is mine. Fork it and replace the identity with yours; the structure of the file is the reusable part.
