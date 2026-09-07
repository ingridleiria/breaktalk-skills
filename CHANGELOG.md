# Changelog

All notable changes to this library are recorded here. Dates are the date of release.

## 2026-09-07

- Every one of the 110 skills now carries an **Adapting this to your context** section naming its own defaults, its illustration, and the rules that hold in any setting under **What not to change**.
- New [USING_THESE_SKILLS.md](USING_THESE_SKILLS.md): loading a skill into any assistant, a first run that teaches you something, the three layers of a skill and which ones to edit, a forty minute adaptation method, what to do when a skill is too specific or too general, a map for reading across the two tracks, and the six things these files silently assume about the reader.
- The research track is now usable outside economics. R, SPSS, SAS, Mplus, NVivo, MAXQDA and ggplot2 named as alternatives; APA table style alongside booktabs; PRISMA, PRISMA-P and PROSPERO named; OSF, AsPredicted, ClinicalTrials.gov and the AEA RCT Registry named; MeSH, PsycINFO and ERIC descriptors alongside JEL codes; multilevel and mixed models given first class treatment rather than an economics footnote.
- Audit pass over every worked example: about twenty five arithmetic and internal consistency errors corrected, currencies made explicit throughout, duplicated standards given a single owner with the others linking, and jurisdiction warnings added to the contract skills.
- The validator now gates the adaptation section as part of the house standard.

## [1.0.0] - 2026-09-06

First public release. 110 skills across five tracks: Chief of Staff (44), PhD research (40), brand and writing (6),
commercial and data (16), and web and presentation (4).

- Chief of Staff track opens with the stage skills, from seed through Series D, because the role is several
  different jobs under one title.
- PhD research track covers the pipeline from a vague topic through to a replication package, and beyond it into
  examining and refereeing.
- Every skill follows one structure: when to use it and when not to, the inputs and what to do when one is missing,
  the method with decision rules stated rather than implied, a worked example with real numbers including a wrong
  turn that was abandoned, failure modes, edge cases, and a checkable quality bar.
- Every skill is self-contained plain Markdown, usable in Claude, ChatGPT, Gemini, a coding assistant or an API
  system prompt.
- Individual skill archives are attached to this release for direct upload.

Update the counts in this entry and in CITATION.cff whenever the library grows.
