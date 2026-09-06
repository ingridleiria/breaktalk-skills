---
name: human-voice-editor
description: Edits prose so it reads as written by a person who knows the subject, without lowering the register. Removes the punctuation, vocabulary, rhythm and structural tells of generated text, restores the agents, numbers and examples the draft gestures at, repairs sentence variety against the author's own samples, and returns a change report with counts so the next draft needs less work. Ships a mechanical dash check that reports and refuses to repair. Use this skill whenever someone says a draft sounds like AI, sounds generic, sounds robotic, sounds like a press release, does not sound like them, or asks to humanise, tighten, polish, or make something read naturally; as the final pass on any post, email, memo, report, chapter or paper that will carry a person's name; and when a draft shows the tells even though nobody mentioned voice.
---

# Human Voice Editor

Generated prose has a signature, and readers now recognise it inside two sentences. It is not a matter of grammar. It is the balanced clause, the reflexive triplet, the paragraph that ends by restating its first line, the noun where a verb belongs, and a vocabulary of about forty words that nobody uses at a kitchen table. Once a reader spots it, the rest of the document is read differently. They stop asking whether the argument is right and start asking whether anyone was actually behind it.

The cost lands where the writing had a job to do. An all-staff note that reads as generated makes people assume the decision behind it was also automatic, and the questions move from the substance to the process. A grant section that reads as generated invites a reviewer to look for fabricated citations. In each case the damage is to credit for work that was genuinely done.

The opposite failure is just as common and less discussed. A draft is stripped of every long sentence, every technical term and every hedge, and what emerges is fluent, friendly and empty. That is not a human voice, it is a different machine. This skill removes the machine and puts back the specifics; it does not lower the register.

## When to use this, and when not to

Use it as the last pass on anything going out under a person's name: a newsletter issue, a post, an executive note, a board paper, a cover letter, a thesis chapter, an email that matters. Use it when the author says the draft is fine but does not sound like them, which is usually a rhythm problem rather than a vocabulary one. Use it on inherited text: a section written by someone else, a paragraph copied from a previous document, a draft the author is about to sign.

Do not use it to write the thing in the first place. A draft that does not exist yet belongs to `newsletter-post-writer` for long form or `linkedin-post-writer` for short form, and both hand their output here for the final pass.

Do not use it to check facts. A sentence can read beautifully and cite a paper that does not exist; that is `literature-verification`, and it runs before this, not after.

Do not use it to enforce a publication's house rules on palette, typography, sign-off and title conventions; that is a brand skill, `breaktalk-brand` in this library, and it constrains what this edit may change. Do not use it as a gate on whether something should be published at all, which is `content-quality-gate`. And do not use it to defeat a detection tool: the goal is prose a knowledgeable reader accepts, which is a different and more durable target than a score.

## What you need before starting

**The draft in editable text.** A PDF or a screenshot forces retyping and loses the author's own line breaks, which carry information about their rhythm. Missing: ask for the source file. If only a PDF exists, extract the text and say that formatting decisions were lost.

**Two or three samples of the author's own writing.** Ideally unedited: sent emails, older posts, a chapter they wrote before they had help. Without samples the edit converges on a generic competent voice, which is an improvement but not a match. Missing: proceed, and mark the change report as unmatched voice, so the author knows the result is neutral rather than theirs.

**The audience and the register.** A methods section, a board paper and a Sunday newsletter tolerate entirely different sentence lengths and entirely different amounts of hedging. Missing: infer from the document type, state the inference in one line at the top of the report, and edit conservatively until it is confirmed.

**Whether substance may be changed.** Some drafts may be rewritten freely; some are approved text where only style is in scope. Missing: assume style only, and list the substantive gaps as queries rather than filling them. Inventing a number to replace a vague claim is a serious error, worse than the vague claim.

**The facts behind the vague sentences.** The number, the name, the date, the case the draft gestures at. This is the input that produces most of the improvement. Missing: mark each place with a visible query in the text, and list them in the report. Do not smooth over a missing specific, because a well written empty sentence is harder to notice than a clumsy one.

**The deadline and how many passes are possible.** One pass prioritises substance and structure; two passes can afford rhythm and read-aloud work. Missing: assume one pass and order the work as the method does.

**Any hard constraints.** A legal phrase that cannot be reworded, a regulated disclosure, a quoted passage, a term of art. Missing: ask, because rewriting a term of art into plain English is the fastest way to lose a specialist reader.

## The diagnostic

Read the whole draft once before touching anything, and mark the sentence where you stopped believing a person wrote it. That sentence is usually the clearest example of the dominant tell and is worth quoting in the report.

Then mark every instance below and count them. Counts, not impressions: an author shown that they used eleven em dashes and six triplets in 900 words changes their next draft, whereas an author told the piece "reads a bit generic" does not.

**Punctuation.** Em dashes and en dashes used as clause breaks. Semicolons used decoratively between clauses that want to be two sentences. Colons introducing a punchline. Quotation marks placed around ordinary words for ironic distance. Ellipses used for suspense.

**Vocabulary.** Delve, landscape, crucial, pivotal, leverage, seamless, transformative, navigate, unlock, robust outside statistics, holistic, nuanced, tapestry, multifaceted, testament, underscore, foster, realm, journey, game-changer, at the end of the day, in today's fast-paced world, it is worth noting, importantly, notably, moreover, furthermore. Intensifiers doing no work: very, truly, genuinely, really, deeply. Stacked hedges: may potentially, could perhaps. Nominalisations where a verb exists: the implementation of, the utilisation of.

**Rhythm and structure.** Tricolons by reflex, where three was not the true count. The "not X, but Y" and "not only X but also Y" frames. Rhetorical questions in series. Sentences of uniform length. Paragraphs of uniform length. Paragraphs that close by restating their opening. Sections that begin "In this section" or end "In summary". Balanced antithesis every other sentence. Openings that establish the topic's importance before saying anything. Closings that lift into the future.

**Substance.** Claims with no agent: it is widely recognised, research shows, many organisations. Numbers absent where a number exists. Examples absent where a concrete case would carry the point. Passive constructions concealing who acted. Bullet lists standing where reasoning belongs. Headings naming a topic rather than making a point.

## The method

1. **Read once, mark once, edit nothing.** Record the counts and the sentence where belief failed. Editing while first reading produces local fixes and misses the pattern, and the pattern is what the author needs to see.

2. **Decide the depth from the counts and the register.** If substance markers dominate, the edit is a substance edit and stylistic repair alone will not save it. If substance is solid and rhythm markers dominate, it is a one-hour edit. If both are heavy and the deadline is short, fix substance and structure and leave vocabulary; a specific draft with two stock words reads better than a polished draft with none and nothing in it.

3. **Substance first, always.** Add the agent, the number, the example, the date. Where the fact is not available, insert a visible query rather than a smoother sentence. One restored number does more than an hour of stylistic repair, because the tells are mostly symptoms of having nothing particular to say.

4. **Structure second.** Cut the self-summary, the importance-establishing opening and the lift-off close. Merge or split paragraphs so that lengths differ visibly. Rewrite headings as claims: "Adoption stalls at the mapping step" rather than "Adoption". Where a bulleted list has replaced an argument, convert the two or three items that carry reasoning back into prose and keep the list only where the items are genuinely parallel and countable.

5. **Rhythm third.** Break the balanced sentences. Let one sentence run long and stop the next one short. Reduce every reflexive triplet to its true count, which is usually two and sometimes one. Remove the "not X, but Y" scaffolding and state Y. The target is variance, not brevity: uniformly short sentences are as machine-like as uniformly medium ones.

6. **Vocabulary fourth.** Replace each stock word with the specific word the sentence needs, or delete it and check whether the sentence lost anything. Delete intensifiers. Restore verbs from nominalisations. Keep any term of art. The test for a word is whether an expert would say it aloud to a colleague.

7. **Punctuation last, by sentence logic.** For each dash used as a clause break, choose by what the clause is doing: a comma when it is an aside, a colon when the second half explains the first, parentheses when it is genuinely subordinate, a full stop when it is a second thought. Vary the substitution, because replacing every dash with the same mark produces a new tell, a document of identical comma-spliced asides.

8. **Run the dash check and review every hit.** See the section below. Fix what it finds by rewriting, then run it again.

9. **Read the result aloud.** Any sentence an expert could not say to a colleague is rewritten. This catches what the lists miss, particularly inverted clauses and sentences whose subject arrives too late.

10. **Match the voice against the samples.** Compare four things: median sentence length, longest sentence, the connectives the author actually uses, and how they open and close. Adjust toward the author, not toward an abstract standard. Where the author has a habit you would otherwise edit out, keep it; a habit is what makes prose theirs, and a first-person aside or a favourite construction is signature rather than error.

11. **Write the change report.** Counts before, categories changed, three before-and-after pairs chosen to teach rather than to impress, and the list of queries the author must answer. The report is half the deliverable, because it is what makes the next draft cheaper.

## The dash check

`scripts/check_dashes.py` is the mechanical part of step 8. It is deliberately narrow.

```bash
python3 scripts/check_dashes.py draft.md
python3 scripts/check_dashes.py chapter1.md chapter2.md
cat draft.md | python3 scripts/check_dashes.py
```

**What it catches.** Three patterns, reported with file, line number and the full line so the fix can be judged in context: the em dash character, the en dash character, and a lone hyphen with whitespace on both sides used as a clause break. It prints a total to standard error and exits non-zero while any remain, so it can sit in a pre-commit hook or a publishing script. With no file arguments it reads standard input.

**What it deliberately does not do.**

It does not fix anything. This is the important part. Substituting a comma for every dash is mechanical and produces its own signature, a page of clauses hung on commas in exactly the same shape the dashes had. The choice among comma, colon, parentheses and full stop depends on what the clause is doing, and that judgement is step 7, not a script.

It does not judge whether a dash was correct. A quoted passage, a range in a citation, source code, a command line example and a URL will all be reported. That is intended: the job is to surface every instance for a human decision, and a checker that guessed which ones were fine would let through the ones that matter. Review each hit rather than trusting the count. It is not markdown-aware or language-aware either: it knows nothing about fenced code blocks, front matter or tables, and works line by line on plain UTF-8 text.

It does not catch the double hyphen used as an improvised dash, or any of the vocabulary, rhythm and structural tells in the diagnostic above. Those are not mechanical, and a clean run says nothing at all about whether the prose reads as human. It is one check, run last, on one failure that is easy to miss by eye and embarrassing to publish.

When the script cannot be run, do the same check by searching for the two characters directly, and record in the report that the check was manual.

## Worked example

**Situation.** Priya Raman, head of people at a 340-person manufacturing business, had drafted a 2,400-word note to all staff announcing a change to shift patterns at two sites. The change was real and defensible: a third shift was being added at one site and removed at the other, affecting about 90 people. She had drafted it with an assistant on a Friday afternoon and it was due to go out on Monday morning, ahead of the site meetings.

The draft was competent and said almost nothing. It contained eleven em dashes in 2,400 words, six three-item lists where the true count was two, nine words from the stock list including "navigate", "transformative" and "journey" twice, and an opening paragraph on the importance of manufacturing flexibility that ran 140 words before mentioning the change. Median sentence length was 21 words and 30 of the 96 sentences fell between 19 and 23 words, which is the flattest distribution the editor had seen that year. It ended: "As we look ahead, we are excited about the opportunities this transformation will unlock."

**Task.** Return it by Sunday evening in a form Priya would sign, in her voice, with the register unchanged: this was a serious note about people's working hours and could not become chatty.

**Action.** The wrong turn came first and is worth recording because it is the usual one. The editor began with punctuation and vocabulary, because those are visible and quick. Ninety minutes later the eleven dashes were gone, the stock words were gone, and the note read exactly as generated as before. Nothing had changed, because the tells were symptoms. The draft had no numbers in it, and every sentence was general because there was nothing particular to say.

The pass was abandoned and restarted at step 3. The editor sent Priya seven questions on Saturday morning, all of the form "what is the actual figure". She answered five within the hour. Those five answers changed the document: the number of affected people at each site, 62 and 28; the notice period, 11 weeks; the date the new pattern begins, 6 January; the fact that no role was being removed and that this was the sentence people actually needed in the first paragraph; and the shift premium, unchanged at 18 percent, which had been the loudest rumour on one of the sites. Two questions she could not answer, about the transport timetable at the earlier start time, and those became a visible line in the note saying that transport was being worked on and would be confirmed by 20 December, with a named person to ask.

Structure came next. The 140-word opening was cut to two sentences: what is changing, and that no role is being removed. Headings became claims, so "Next Steps" became "What happens between now and 6 January". Three of the six triplets were genuinely pairs; one was a list of five squeezed into three, which was the more damaging error.

Rhythm followed. Priya's own samples, three long emails written before she had drafting help, had a median sentence length of 14 words with a spread from 4 to 38. She opens paragraphs with "So" and never writes "however". The edit moved the draft toward that distribution and removed four instances of "however".

Punctuation last. Of the eleven dashes, four became full stops, three became colons, two became commas, one became parentheses, and one sentence was rewritten because none of the four helped. The dash check then returned one hit, in a line quoted from the existing shift agreement, which was left alone on purpose with the decision recorded in the report.

**Result.** The note went out at 07:00 on Monday at 1,650 words, with the first specific fact in the second sentence rather than on the second page.

What can be claimed honestly is narrow. The site meetings that week ran on the transport question and the January start date, the two things the note had actually said, rather than on the shift premium rumour, which had circulated for nine days and did not come up. Priya's own view was that the change had been decided in November and the note had simply stopped hiding it. Whether it changed anyone's mind is unknowable, and claiming otherwise would be inventing a clean ending. The lasting effect was the change report: Priya asked for counts on her next two drafts before sending them, and the second had two stock words and no dashes.

### A second scenario, where it goes differently

The same method applied to a methods section of an economics paper produces a much smaller edit, and several diagnostic markers are ignored on purpose.

Passive voice stays where the actor is genuinely irrelevant and the convention expects it: "the sample was restricted to firms with at least ten employees" is correct and rewriting it into the first person makes the sentence about the author rather than the sample. Hedges stay where they are accurate rather than evasive: "the estimate is consistent with" is a precise claim about what the data supports, and hardening it to "shows" is a substantive error dressed as a style fix. "Moreover" and "furthermore" are ordinary connectives in this register and are cut only where they connect nothing.

What is still edited: the uniform sentence length, which is as flat in academic prose as anywhere else; the tricolons; the paragraph that restates its first line; the nominalisations, since "we estimate" beats "estimation was performed"; and every dash. The substance step also runs differently, because the missing specifics are not names and dates but sample sizes, definitions and the reason a restriction was applied.

What changed: the register sets which markers are tells and which are conventions. Applying the full list to a technical document damages it, and the failure looks like a paper that reads pleasantly and no longer states precisely what was done.

## Output

Two things, always together.

First, the edited text in the format it arrived in, with every unresolved query left visibly in place as `[query: exact figure for Q3 attrition?]` so it cannot be published by accident. Second, the change report:

```
CHANGE REPORT
Document:        [name]        Words before / after:  [n] / [n]
Register:        [inferred or confirmed]
Voice samples:   [used, or none supplied and the edit is unmatched]

COUNTS BEFORE
| Marker                          | Count |
| Em and en dashes as clause breaks |     |
| Stock vocabulary                  |     |
| Reflexive triplets                |     |
| Claims with no agent              |     |
| Paragraphs restating their opening|     |
| Median sentence length (words)    |     |
| Sentences within 3 words of median|     |

WHAT WAS CHANGED
[Three to six lines by category, most consequential first.]

BEFORE AND AFTER
1. Before: [sentence]   After: [sentence]   Why: [one clause]
2. Before: [sentence]   After: [sentence]   Why: [one clause]
3. Before: [sentence]   After: [sentence]   Why: [one clause]

QUERIES FOR THE AUTHOR
[Each missing specific, with the sentence it belongs to.]

DELIBERATE EXCEPTIONS
[Anything the diagnostic flagged that was kept, and why.]

DASH CHECK
[Clean, or the hits kept on purpose with the reason.]
```

## Failure modes

**Editing the style of an empty draft.** Recognise it when the edit is nearly finished and the piece still says nothing anyone could disagree with. Stop, and go and get the facts. Style repair on a hollow draft produces polished nothing, which is worse because it is harder to see.

**Flattening the expertise.** Recognise it when a specialist reader would now find the text imprecise: a term of art replaced with a plain word, a hedge hardened into a claim, a conditional dropped. Restore the precision and accept the longer sentence.

**The single substitution.** Recognise it by a document in which every former dash is now a comma. Vary by sentence logic.

**Inventing the specific.** The worst failure available here. A plausible number filled into a sentence that had none is a fabrication with the editor's fingerprints on it. Use a visible query every time.

**Erasing the author's habits.** Recognise it when the author says the result is better but not theirs. A favourite opening, sentence fragments, a willingness to start with "So": these are signature. Check the samples before removing anything that recurs.

**Trusting the script.** A clean dash check means one specific thing is absent. It says nothing about rhythm, vocabulary or substance. Recognise this failure when the only evidence offered that a draft reads as human is that the checker passed.

**Editing without the counts.** Recognise it when the report says the draft "read generically". The author cannot act on that. Counts change behaviour; adjectives do not.

## Edge cases

**No samples of the author's writing exist.** Edit to a neutral register, state in the report that the voice is unmatched, and ask for two samples before the next piece. Do not guess at a personality.

**The author writes in a second language.** Separate the two problems. Idiom and article errors are corrections; sentence length, directness and formality are voice, and often reflect the conventions of their first language rather than a machine. Correct the first, ask before changing the second, and never smooth a construction into blandness because it is unfamiliar.

**Legal, regulated or quoted text.** Do not touch it. Edit around it and note the boundary in the report. A rewritten warranty clause or a paraphrased quotation is a liability, not an improvement.

**The draft is genuinely good and the author is wrong about it.** Say so, with two pieces of evidence: the sentence length distribution and the number of specifics per hundred words. Make the small edit where a real improvement exists and resist changing things to demonstrate effort.

**Long documents under deadline.** Do not edit uniformly. Apply the full method to the opening, the closing and the first paragraph of each section, which is where readers decide, and apply substance and punctuation only to the rest. Say in the report which parts got which treatment.

**The piece is a translation.** Run the diagnostic on the target language only. Tells do not translate, and a construction that is a tell in English may be ordinary in the source language.

## Quality bar

- No em dash or en dash used as a clause break, verified by the script, with any deliberate exception named in the report.
- Every general claim has an agent, a number, or an example, or carries a visible query saying it does not.
- No number, name or date appears in the edited text that was not supplied by the author or the source.
- Sentence length varies visibly, and the median sits within about three words of the author's own samples where samples exist.
- No word from the stock vocabulary list survives except where it is the technically correct term.
- The register is unchanged: a specialist reader would find the text no less precise than before.
- The change report gives counts before, three before-and-after pairs, and the list of unanswered queries.
- A reader who knows the author would accept the result as theirs.

## Related skills

`newsletter-post-writer` and `linkedin-post-writer` produce the drafts that come here for the final pass, and both name this skill as their last step. `literature-verification` runs before this on anything carrying citations, because verified sources are a precondition for editing rather than a consequence. `breaktalk-brand` supplies the editorial rules that constrain the edit when the piece is published under that identity. `content-quality-gate` decides whether the piece should go out at all, which this skill assumes has already been settled. `ceo-communications` and `thesis-chapter-review` both hand their near-final drafts here.
