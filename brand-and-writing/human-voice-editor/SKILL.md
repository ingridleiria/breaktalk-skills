---
name: human-voice-editor
description: Edits prose so it reads as written by a person rather than generated, without lowering the register: removes the punctuation, vocabulary, rhythm, and structural tells of machine text, restores specifics and agents, repairs sentence variety, and reports what was changed and why. Use this skill whenever the user says a draft sounds like AI, sounds generic, sounds robotic, does not sound like them, or asks to humanize, polish, tighten, or make something read naturally; and as the final pass on any document, email, post, or paper that will carry the user's name. Trigger even when the user does not mention voice, if the draft shows the tells.
---

# Human Voice Editor

Generated prose has a signature that readers now recognize in a sentence or two: a particular punctuation, a particular vocabulary, a particular rhythm of balanced clauses and reflexive triplets, and a habit of summarizing itself. Removing the signature is not the same as simplifying; expert prose stays expert. This skill takes out the tells and puts back the specifics.

## The diagnostic

Read the whole draft, then mark every instance of the following. Report counts before editing so the pattern is visible to the author.

**Punctuation**
- Em dashes and en dashes used as clause breaks. Replace with a comma, a colon, parentheses, or a new sentence, choosing by the logic of the sentence, not always the same substitute.
- Semicolons used decoratively between clauses that would be better as two sentences.
- Colons introducing a punchline.
- Quotation marks around ordinary words for ironic distance.

**Vocabulary**
- Stock words: delve, landscape, crucial, pivotal, leverage, seamless, transformative, navigate, unlock, robust (outside statistics), holistic, nuanced, tapestry, multifaceted, testament, underscore, foster, realm, journey, game-changer, at the end of the day, in today's fast-paced world, it is worth noting, importantly, notably, moreover, furthermore.
- Intensifiers doing no work: very, truly, genuinely, really, deeply, incredibly.
- Hedges stacked: "may potentially", "could perhaps".
- Nominalizations where a verb exists: "the implementation of" for "implementing"; "utilization" for "use".

**Rhythm and structure**
- Tricolons by reflex: three adjectives, three nouns, three parallel clauses, wherever three was not the true count.
- "It's not X, it's Y" and "not only X but also Y" constructions.
- Rhetorical questions in series.
- Sentences of uniform length; paragraphs of uniform length.
- Paragraphs that end by restating their first sentence.
- Sections that open with "In this section" or close with "In summary".
- Balanced antithesis in every other sentence.
- Openings that state the topic's importance before saying anything ("In an era of...").
- Closings that lift off into the future ("As we look ahead...").

**Substance**
- Claims without a named agent: "it is widely recognized", "research shows", "many organizations" (who?).
- Numbers absent where a number is available.
- Examples absent where a concrete case would carry the point.
- Passive voice hiding who did what.
- Lists where prose would show the reasoning.
- Headers that name a topic rather than make a point.

## The edit

Work in this order:

1. **Substance first.** Add the agent, the number, the example, the case. Ask the author for specifics the draft gestures at; a sentence with a real number beats any amount of stylistic repair.
2. **Structure.** Cut self-summaries, topic-importance openings, and lift-off closings. Merge or split paragraphs to vary length. Rewrite headers as points.
3. **Rhythm.** Break the balanced sentences; let one sentence run and the next stop short. Reduce every reflexive triplet to the true count. Remove the "not X but Y" scaffolding and say Y.
4. **Vocabulary.** Replace stock words with the specific word the sentence needs, or delete them. Remove intensifiers; restore verbs.
5. **Punctuation.** Replace dashes by sentence logic. Keep semicolons only where two clauses truly belong together.
6. **Read aloud.** Any sentence that could not be said in conversation by an expert is rewritten.

Preserve the register: an academic paper stays academic, a legal memo stays precise, a newsletter stays personal. The edit removes the machine, not the expertise.

## Voice matching

When samples of the author's own writing exist, calibrate: their sentence length distribution, their connectives, their habits of opening and closing, the words they use and never use. Match those rather than an abstract "human" standard; there are many human voices and the author has one.

## Reporting

Return the edited text and a short change report: the counts from the diagnostic, the categories of change made, three before-and-after examples, and any places where the author must supply a specific that the draft lacked. The report teaches the pattern so the next draft needs less editing.

## Mechanical check

`scripts/check_dashes.py` reports every em dash, en dash, and spaced hyphen used as punctuation, with file, line number, and the offending line. Run it over the finished draft as the last step, before the report:

```bash
python3 scripts/check_dashes.py draft.md
```

It exits non-zero while any remain. The script finds them; it does not fix them, because mechanical substitution of a comma for every dash produces its own tell. Rewrite the sentence or choose the punctuation the meaning calls for.

## Quality bar

- Zero em dashes used as clause breaks; zero stock vocabulary from the list.
- Sentence and paragraph lengths visibly vary.
- Every general claim has an agent, a number, or an example, or is flagged for one.
- The register is unchanged.
- A reader who knows the author would accept it as theirs.
