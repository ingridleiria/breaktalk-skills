---
name: breaktalk-brand
description: Applies the BreakTalk identity, which belongs to Ingrid Leiria and her newsletter and public skills library, to any artifact she publishes: newsletter and post images, slide decks, one-pagers, PDFs, social cards, repository READMEs and workshop material. Holds the identity as checkable rules rather than adjectives: logo placement and minimum sizes, an eight-role monochrome palette with two accents, two type families with a line-length limit, numeric margins, monochrome chart discipline, and an editorial voice with banned vocabulary and a fixed sign-off. Use this skill whenever someone asks for anything BreakTalk-branded, mentions BreakTalk, "my newsletter brand", "make it look like BreakTalk", asks for a Substack header, a post image, a workshop deck, a one-pager or a README under that name, or says only "brand this" while working on that material. Read it as a worked example when building a brand skill for a different identity, since the structure transfers and the values do not.
---

# BreakTalk Brand

A personal publication accumulates recognition slowly and loses it quickly. The newsletter header is made in one tool, the workshop deck in another six weeks later, the LinkedIn card by a template with rounded cards and three colours that came free with a theme, and the repository README with whatever badges were to hand. Each artifact is defensible alone. Together they are four publications, and a reader who saw one does not recognise the next, so nothing compounds.

The second failure is the one that causes the first. Most brand documents are written in adjectives: clean, modern, human, approachable. Adjectives cannot be checked, so every artifact reopens the same argument, and under deadline the argument is settled by whatever the template did by default. A rule that says the margin is 2.5 cm and the logo sits bottom right at 15 percent of width is either followed or not, and can be verified in ten seconds by someone who was not there when it was made.

This file exists to hold one identity as rules of that kind. The identity is a coffee break: black ink on white, a hand-drawn cup, quiet space, and nothing loud. The masthead line is "Grab your coffee and let's have some talk over the week".

## When to use this, and when not to

Read this first, because it decides whether the file is usable at all.

**This is one person's identity.** The logo, the wordmark, the tagline, the palette as a signature and the sign-off belong to Ingrid Leiria and to BreakTalk. A stranger cannot use this file as written. Applying this mark, this tagline or this sign-off to material published by someone else is misattribution, not styling, and no amount of adjustment to the palette makes it otherwise.

**What is reusable is the structure.** Read this as a worked example of how a brand skill is built. Every section is a pattern that transfers to any identity: an identity stated as rules a stranger could check rather than as adjectives; one section per element, each naming the rules that can be broken and the consequence; a palette with one role per colour rather than a mood board; typography with numeric limits; layout with measurements; chart discipline that survives greyscale printing; an editorial voice with a banned vocabulary and a fixed sign-off; and a recipe per artifact type with real pixel dimensions. To build your own, copy the section shape, replace every single value, and keep the discipline that each rule must be checkable by someone holding the finished file. `skill-builder` covers the method for writing it.

Use this file for artifacts published under the BreakTalk name: newsletter and post images, LinkedIn cards, workshop and talk decks, one-pagers and PDFs, repository READMEs, and any public-facing material from the skills library.

Do not use it for another organisation's branding, including a client's or an employer's, which needs its own brand skill built with `skill-builder`. Do not use it for the writing itself: the argument and structure of a post belong to `newsletter-post-writer` or `linkedin-post-writer`, and the final voice pass to `human-voice-editor`; this file only constrains those. Do not use it for the mechanics of generating a document or a deck, which belong to whatever document or presentation skill the environment provides. Do not use it for figures in an academic paper, where the journal's requirements override any house palette, which is `academic-figures-monochrome`.

## What you need before starting

**The artifact type and its exact output dimensions.** A social card, a slide and a printed one-pager have different margin arithmetic, and a design built at the wrong aspect ratio cannot be rescued by cropping. Missing: take the dimensions from the recipe table below and confirm before delivering.

**Where it will be seen, and how that surface renders.** Email clients strip CSS and often ignore web fonts. Social platforms crop previews at a different ratio from the upload. Projectors lose mid greys and low-contrast rules. Dark mode inverts backgrounds in some readers and not others. Missing: assume the worst case for the medium, which is greyscale print for documents, an email client with images blocked for newsletters, and a poorly calibrated projector for decks.

**The logo file.** `assets/breaktalk_logo.png` in this skill folder, 500 by 500, black on white: the words BREAK TALK in spaced capitals arched over a line-drawn coffee cup with steam. Missing or unusable at the size needed: use the wordmark alone, BREAK TALK in spaced capitals, and never redraw the cup by hand.

**Which fonts are actually available.** A specification naming a font the environment does not have silently substitutes something else, usually with different metrics, and the layout shifts. Missing: use the system sans and record the substitution in the delivery note.

**The final text.** Headlines change layout more than any other variable, and designing around placeholder text guarantees a second pass. Missing: design with the longest plausible headline rather than a short one, so the layout survives the real copy.

**Whether the artifact is public or internal.** Public material carries the sign-off and the links and holds to the full standard; internal material does neither. Missing: assume public, which is stricter.

**Whether an accent is earned.** The palette allows one accent per artifact, and most artifacts do not need it. Missing: default to none. An artifact with no accent is always acceptable; an artifact with two unearned accents is not.

## The method

1. **Pull the recipe for the artifact type** from the table below and set the canvas to its exact dimensions before anything else. Everything downstream is measured from the canvas.

2. **Set the margins by number, not by eye.** At least 2.5 cm on documents, 8 percent of slide width on slides, and generous margins on cards where the platform may crop. Then do not encroach on them. White space is the identity, and the single commonest way this brand is lost is a layout that fills the space because the space was available.

3. **Write the headline as a claim, in spaced capitals where the recipe calls for it.** "Adoption stalls at the mapping step" rather than "Adoption". A topic headline forces the body to carry the point, and on a slide seen for forty seconds the body will not be read. Tracking is 0.15 em on capitalised titles, which is what echoes the wordmark.

4. **Decide whether an accent is earned, and if so which one.** The rule is one accent per artifact. Navy carries emphasis, links, and a single series in a chart. Wine carries a contrasting series or a warning. Two accents appear together only when a chart genuinely has two series that must be distinguished after the monochrome options are exhausted. If you cannot say in one sentence what the accent is signalling, it is decoration and the artifact goes out without it.

5. **Place the logo per the mark rules**, then check the two things that are actually violated: clear space equal to the height of the cup on all sides, and minimum reproduction size, 24 mm wide in print and 120 px wide on screen. Below that threshold the cup detail fills in and the mark reads as a smudge, so drop to the wordmark alone.

6. **Build any chart to the monochrome standard** in the layout section below. Decide series separation before choosing any colour: marker shape first, then dash pattern, then texture or fill density, and colour last and only if those are exhausted. A chart that works in greyscale works everywhere, and the reverse is not true.

7. **Run the editorial pass on every word in the artifact**, including headings, captions, alt text and the sign-off. The voice rules are as much a part of the identity as the palette, and a correctly styled slide with generic copy on it is off-brand.

8. **Test the rendering before delivering.** Export to greyscale and check that every distinction survives. View at the smallest size the artifact will be seen at: a phone thumbnail for a card, the back row for a slide. Check body text contrast against its background and any accent against white. Where a mid grey rule disappears, thicken it or darken it for that medium and record an exception, rather than changing the palette.

9. **Check the finished artifact against the quality bar** and deliver it with the delivery note described in the output section, so that the next artifact can be made consistent with this one without reopening any decisions.

## The identity, in rules

### The marks

The logo is the words BREAK TALK in spaced capitals arched over a line-drawn coffee cup with steam, supplied as `assets/breaktalk_logo.png` at 500 by 500, black on white. Use it as provided.

Never recolour it, stretch it, rotate it, or add a shadow, an outline, a gradient or a container. On dark backgrounds use an inverted version, white on black, and never a tinted one. Clear space on all sides is at least the height of the cup, and nothing crosses into it, including page furniture and slide numbers. Minimum reproduction is 24 mm wide in print and 120 px wide on screen; below that, the wordmark alone.

Placement is fixed by artifact so that it becomes predictable: bottom right on documents and slides, top left on social cards, centred on covers.

The coffee motif may appear at most once per artifact, as the logo or as a single small line drawing. It is a signature, not a pattern, and repeating it turns a quiet identity into a novelty one.

### Colour

Colour is a signal here, not decoration, and the palette is deliberately narrow enough to be memorised.

| Role | Colour | Hex |
| Ink | Black | #000000 |
| Paper | White | #FFFFFF |
| Body text | Near black | #1A1A1A |
| Secondary text | Dark grey | #404040 |
| Rules and captions | Mid grey | #7F7F7F |
| Backgrounds and table shading | Light grey | #F2F2F2 |
| Accent one: emphasis, links, one chart series | Navy | #1F3864 |
| Accent two: contrasting series, warnings | Wine | #7B1E28 |

One accent per artifact unless a chart needs two series distinguished. Mid grey is for rules and captions and never for body text, because it fails contrast at body sizes and disappears on projection. Light grey shades a single emphasised row and is not used for alternating rows.

### Typography

Headlines and the wordmark use a geometric or humanist sans with generous letterspacing: Montserrat, Inter, or the system sans where neither is available. Section titles are set in capitals at 0.15 em tracking.

Body text is the same sans at 11 pt in documents and 18 pt or larger on slides. For long-form PDFs and academic-adjacent material, a serif body, Times New Roman or Georgia, under sans headlines.

Never more than two families in one artifact. No decorative or script faces at all. Line length runs 60 to 75 characters, left aligned, ragged right, never justified.

### Layout

Margins are wide: at least 2.5 cm on documents, 8 percent of slide width on slides. One idea per slide and per section. Headlines state the point.

Rules and dividers are 0.5 pt mid grey lines. Content is never boxed. Tables carry three horizontal rules only, above the header, below the header, and at the foot, with no vertical lines and no zebra striping beyond a single light grey emphasised row.

Imagery is line drawing, monochrome photography, or nothing. No stock photography, no gradients, no icons in circles, no card shadows.

Charts are monochrome first. Series are separated by marker shape, dash pattern and fill texture before any colour is considered, and where colour is unavoidable it is one accent, or two only for two series. The legend sits outside the plot area. The background is white, gridlines are light grey and minimal, and axis labels carry their units. The test is that the chart survives being photocopied.

### Editorial voice

The written identity is as fixed as the visual one. First person. A concrete scene or a specific problem before any argument. Numbers with their sources. Economics used as a working lens rather than as a reference. A plain ending on the point, never an uplift line.

No em dashes or en dashes anywhere: use a comma, a colon, or a new sentence. No stock vocabulary: delve, landscape, crucial, leverage, seamless, transformative, unlock, journey, game-changer. Sentence lengths vary and paragraph lengths vary. Titles use the colon form where a subtitle is needed: a broad concept, a colon, then the specific mechanism.

The sign-off on public material is "Ingrid Leiria, BreakTalk", with the Substack link, and with the repository link on library material.

## Artifact recipes

| Artifact | Size | Layout | Logo | Accent |
| Newsletter or post image | 1200 by 675 | White ground, one headline line in spaced capitals, wide margins | Bottom right at 15 percent of width | Optional single navy rule |
| Social card | 1080 by 1080 or 1200 by 627 | One strong statement, one supporting number | Wordmark top left | Navy on the number only |
| Workshop or talk deck | 16 by 9 | White slides, black headline top left, near-black body, 8 percent margins | Bottom right, small, every slide | One navy accent across the deck |
| Closing slide | 16 by 9 | Black ground, white wordmark, links | Centred | None |
| One-pager or PDF | A4 or Letter | Title in spaced capitals, 0.5 pt grey rule, two columns where length allows | Bottom right | One navy rule or heading |
| Repository README | Markdown | Logo at reduced width at the top, plain prose, no badges beyond a licence badge | Top, centred or left | None |

## Worked example

**Situation.** A regional operations group asked for a 40 minute session on how small teams adopt new tools, to be delivered on a Thursday, with the request arriving on the Tuesday. Three artifacts were needed: an 18 slide deck, a post image announcing the session, and a one-page handout. The only starting material was an existing deck built on a purchased theme with three brand colours, rounded cards with drop shadows, and icons in coloured circles.

**Task.** Deliver all three by Wednesday evening, recognisably from the same publication as the newsletter, and legible from the back of a room with a projector of unknown quality.

**Action.** The first attempt was to restyle the purchased theme: swap its three colours for navy and wine, change the fonts, and keep the layouts. Ninety minutes in, it was abandoned. Recolouring had removed the theme's colours but kept its shapes, and shapes are what a reader recognises. The rounded cards, the drop shadows and the icon circles all violate the layout rules, and each one was a separate fight against a master slide. Starting from blank white slides took forty minutes and produced something correct.

The deck was rebuilt at 16 by 9 with margins at 8 percent of slide width, which is 2.7 cm on a 33.87 cm slide, marked as guides before any content was placed. Every headline was rewritten as a claim: "Teams adopt the tool that removes a step they hate" rather than "Adoption drivers". That rewrite cut four slides, because two of the original headlines turned out to be the same claim stated twice, which is a structural problem topic headlines conceal.

One accent was earned. The deck had a single chart, tool usage over eleven weeks for two teams. The series were separated first by marker shape, circle and square, then by dash pattern, solid and dashed, with the legend outside the plot area. Navy was added to one series only, which meant the chart still worked when the handout was photocopied in black and white, which it was.

The post image was 1200 by 675, white, one line in spaced capitals at 0.15 em tracking, logo bottom right at 15 percent of width, no accent. The handout was A4 with the title in spaced capitals, one 0.5 pt grey rule, two columns, and the sign-off with both links in the footer.

The failure appeared in the projection test on Wednesday evening. The 0.5 pt rules at #7F7F7F were invisible beyond about four metres on a low-contrast projector. Rather than changing the palette, a projection exception was recorded: rules thickened to 1 pt and darkened to #404040 for the projected version only, with the source file left correct, and the exception written into the delivery note so the next deck starts from it.

**Result.** All three artifacts went out on the Wednesday. The deck ran to 14 slides after the headline rewrite. Two attendees asked afterwards whether the session and the newsletter were by the same person, having seen one but not the other, which is the only outcome this file is really trying to produce.

What remains unresolved: the handout was photocopied by the host onto light grey paper, which pushed the light grey table shading at #F2F2F2 to invisibility. That is not a projection problem and cannot be fixed by an exception; the honest answer is that the shading role does not survive reproduction on tinted stock, and a future revision of the palette may need a rule instead of a shade for emphasised rows.

### A second scenario, where it goes differently

A conference invited a talk and required its own slide master: their colours, their type, their footer, their logo on every slide. Nothing in the visual identity survives that constraint, and arguing about it wastes goodwill on a point the audience will never notice.

The identity retreats to the parts that are behavioural rather than visual, and those turn out to be most of it. Headlines are still written as claims. One idea per slide still holds. Charts are still built monochrome with series separated by marker and dash pattern, which is compatible with any host palette and usually better than theirs. Line length, sentence variety and the banned vocabulary are unaffected. The BreakTalk mark appears once, on the closing slide, alongside the sign-off and links, where a host template normally permits a speaker's own details.

What changed: the constraint removed the visual layer entirely, and what remained was still recognisable, which is the useful discovery. A brand held only in a palette does not survive contact with someone else's template. A brand held in how headlines are written, how charts separate series, and how a piece ends does.

## Output

Deliver the artifact files at their exact specified dimensions, plus a short delivery note so the next artifact is consistent without reopening decisions:

```
DELIVERY NOTE
Artifact:        [type, from the recipe table]
Dimensions:      [exact, as delivered]
Fonts used:      [family, and any substitution forced by the environment]
Accent:          [none / navy / navy and wine, and what it signals]
Logo:            [placement, width as a percentage, clear space confirmed]
Chart separation: [marker, dash, texture, colour: which were used]
Rendering checks: [greyscale, thumbnail, projection, dark mode: pass or note]
Exceptions:      [any value changed for this medium, and why]
Voice pass:      [done, and anything the editorial rules forced]
```

For a set of artifacts produced together, one note covers the set and lists the files.

## Failure modes

**Restyling a template instead of starting blank.** Recognise it by any rounded card, drop shadow, icon circle or coloured band that no rule asked for. Shapes carry more recognition than colours, so a recoloured template still reads as the template. Start from a blank canvas; it is usually faster.

**Accent inflation.** Recognise it when the artifact has navy headings, a wine callout, a light grey panel and a coloured chart. One accent per artifact. If two elements both claim it, one of them is not as important as its author thinks.

**The logo too small or too crowded.** Recognise it when the cup detail fills into a blur, or when a slide number or footer sits inside the clear space. Below the minimum size, use the wordmark alone.

**Colour doing the work a marker should do.** Recognise it by printing the chart in greyscale and finding the series indistinguishable. Rebuild with marker shape and dash pattern, then add colour back if it still helps.

**Filling the margins.** Recognise it by a slide with content in the outer 8 percent, usually a logo, a footer or an overflowing table. Cut the content or split the slide. The margin is not spare space.

**Correct styling with generic copy.** Recognise it when the headline names a topic and the body could belong to any publication. The editorial rules are part of the identity, and a well set generic slide is still off-brand.

**Silent font substitution.** Recognise it when line breaks fall in unexpected places or the tracking looks wrong. Check which font actually rendered, and record any substitution in the delivery note.

## Edge cases

**A host organisation's template is mandatory.** Do not fight it. Keep the behavioural rules, headline as claim, one idea per slide, monochrome chart separation, and place the mark once on the closing slide. This is the second scenario above.

**Co-branded material.** Two marks need equal visual weight and their own clear space, and neither may be modified to harmonise with the other. Where the partner's guidelines conflict with these rules, theirs govern their mark and these govern this one, and neither identity is adjusted to split the difference.

**Dark mode and inverting readers.** Some email clients invert backgrounds unpredictably. Supply the inverted logo, avoid white shapes on transparent backgrounds, and check that near-black body text does not become an unreadable near-white against a mid tone. At sizes under 120 px, including favicons and avatars, use the wordmark alone, or the cup alone where the wordmark would be illegible.

**Academic or journal output.** The journal's requirements win on figures, fonts and captions without exception. Use `academic-figures-monochrome`, which is compatible with this identity in spirit because both are monochrome first, and do not apply the BreakTalk palette to a submitted figure.

**Material someone else will publish under their own name.** The identity does not travel. Strip the mark, the tagline and the sign-off, and hand over the content. Where the work is genuinely joint, agree attribution in words rather than by placing a mark.

**A medium where a rule cannot be met.** Record it as an exception in the delivery note, with the reason and the value used, and leave the source file correct. Repeated exceptions for the same medium are evidence that the palette or the layout rule needs revising, which is a deliberate decision and not something to make silently under deadline.

## Quality bar

- Every value used comes from this file: a hex code from the palette table, a margin from the layout rules, a size from the recipe table.
- At most one accent, and its purpose can be stated in one sentence.
- The logo is at or above minimum size, in its specified position, with clear space equal to the cup height, and unmodified.
- Every chart is legible in greyscale, with series separated by marker and dash pattern and the legend outside the plot area.
- No boxed content, no drop shadow, no icon circle, no gradient, no stock photograph.
- Body text is #1A1A1A at the specified size, with line length between 60 and 75 characters, left aligned.
- Every word in the artifact passes the editorial rules, including headings and captions, and public material carries the sign-off with its links.
- The delivery note records the fonts actually rendered and any exception made for the medium.

## Adapting this to your context

Every value here belongs to one person and one publication: the mark, the masthead line, the accents, the sign-off. Fork this as a template, replace the values, keep the shape.

- **The identity.** The name, wordmark, coffee motif and masthead line are Ingrid Leiria's. Replace all four, and delete `assets/breaktalk_logo.png` rather than recolour it.
- **The palette.** Eight monochrome roles with navy and wine. Replace every hex, but keep one role per colour and one accent per artifact.
- **The numeric limits.** 0.15 em tracking, 2.5 cm and 8 percent margins, 60 to 75 characters a line, 11 pt body, 18 pt on slides. Reset each from your own longest headline and furthest viewing distance.
- **Voice rules.** The banned word list, the colon title form and the fixed sign-off are one writer's habits. Build your list from the words that keep reappearing in your own drafts.
- **The recipe table.** Its rows cover a Substack, LinkedIn, decks and READMEs. Replace them with the surfaces you publish on, at this year's dimensions.
- **What not to change.** Adjectives cannot be enforced, so every rule must be checkable in ten seconds by someone holding the finished file. Keep that, and keep the behavioural rules that survive a host's template: headline as a claim, one idea per slide, series separated before colour.

## Related skills

`newsletter-post-writer` and `linkedin-post-writer` write the content this file styles, and both defer to the editorial rules here when the piece is published under this name. `human-voice-editor` runs the final language pass and enforces the dash and vocabulary rules mechanically. `skill-builder` is the method for building a brand skill for a different identity, using this file's structure and none of its values. `academic-figures-monochrome` governs figures where a journal's requirements override any house palette. Document and presentation generation mechanics belong to whichever such skill the environment provides; this file supplies the appearance rules they apply.
