---
name: breaktalk-brand
description: Applies the BreakTalk visual and editorial identity (Ingrid Leiria's newsletter and public skills library) to any artifact: newsletter graphics, LinkedIn images, slide decks, one-pagers, PDFs, social cards, repository READMEs, and workshop material. Use this skill whenever the user asks for anything BreakTalk-branded, mentions "BreakTalk", "my newsletter brand", "make it look like BreakTalk", asks for a Substack header or post image, a workshop deck under the BreakTalk name, or any public-facing material from the skills library. Trigger even when the user only says "brand this" while working on BreakTalk content. For other organizations' branding, use their own brand skill instead.
---

# BreakTalk Brand

BreakTalk is a newsletter about Chief of Staff practice, AI adoption in real teams, and economics applied to work, written by Ingrid Leiria and published on Substack. The tagline on the masthead is "Grab your coffee and let's have some talk over the week". The visual identity is the coffee break itself: black ink on white, a hand-drawn cup, plenty of quiet space. Nothing loud.

## Logo

The logo is in `assets/breaktalk_logo.png` in this skill folder (500 by 500, black on white): the words BREAK TALK in spaced capitals arched over a line-drawn coffee cup with steam. Use it as provided.

Rules:
- Minimum clear space around the logo equal to the height of the cup. Never crowd it with text or other marks.
- Never recolor, stretch, rotate, add shadows, outlines, or gradients. On dark backgrounds use an inverted (white on black) version only; do not tint.
- Minimum reproduction size: 24 mm wide in print, 120 px wide on screen. Below that use the wordmark alone (BREAK TALK in spaced capitals) without the cup.
- Placement: bottom right of documents and slides, top left of social cards, centered on covers.

## Color

The palette is deliberately narrow. Colour is a signal, not decoration.

| Role | Colour | Hex |
| --- | --- | --- |
| Ink | Black | #000000 |
| Paper | White | #FFFFFF |
| Body text | Near-black | #1A1A1A |
| Secondary text | Dark grey | #404040 |
| Rules, captions | Mid grey | #7F7F7F |
| Backgrounds, table shading | Light grey | #F2F2F2 |
| Accent one (emphasis, links, one series in a chart) | Navy | #1F3864 |
| Accent two (contrast series, warnings) | Wine | #7B1E28 |

Use at most one accent per artifact unless a chart needs two series distinguished. Charts otherwise follow monochrome discipline: black, greys, line pattern and marker shape separate series, legend outside the plot area, white background.

## Typography

- Headlines and wordmark: a geometric or humanist sans-serif with generous letterspacing (Montserrat, Inter, or the system sans available), capitals for section titles with 0.15 em tracking to echo the wordmark.
- Body: the same sans at 11 pt for documents and 18 pt or larger for slides; for long-form PDFs and academic-adjacent material, Times New Roman or Georgia body with sans headlines.
- Never more than two families in one artifact. No decorative or script faces.
- Line length 60 to 75 characters for body text. Left aligned, ragged right, never justified.

## Layout principles

- White space is the brand. Margins are wide (at least 2.5 cm on documents, 8% of slide width on slides).
- One idea per slide or per section. Headlines state the point ("Adoption stalls at the mapping step"), not the topic ("Adoption").
- Rules and dividers are thin (0.5 pt) mid-grey lines, never boxes around content.
- Tables: three horizontal rules only (above header, below header, at the bottom), no vertical lines, no zebra striping beyond the light grey for a single emphasized row.
- Imagery: line drawings, monochrome photographs, or none. No stock photography, no gradients, no icons in circles.
- Coffee motif may appear once per artifact at most, as the logo or a small line drawing; it is not wallpaper.

## Editorial voice

Written material under the BreakTalk name follows Ingrid's own register: first person, a concrete scene or specific problem before the argument, numbers with sources, economics used as a lens, and a plain ending on the point rather than an uplift line. No em dashes anywhere; use commas, colons, or a new sentence. No stock AI vocabulary (delve, landscape, crucial, leverage, seamless, transformative). Sentences vary in length; paragraphs vary in length. Titles use the colon form when a subtitle is needed: a broad concept, a colon, then the specific mechanism.

Standard sign-off for public material: "Ingrid Leiria, BreakTalk", with the Substack link, and, for library material, the GitHub repository link.

## Artifact recipes

- **Substack post image** (1200 by 675): white background, one line of the headline in spaced capitals, logo bottom right at 15% width, optional single navy rule.
- **LinkedIn card** (1080 by 1080 or 1200 by 627): headline as a single strong statement, one supporting number in navy, wordmark top left, generous margins.
- **Workshop or talk deck**: white slides, black headline top left, body in near-black, one navy accent, logo bottom right on every slide at small size, black closing slide with white wordmark and the links.
- **One-pager or PDF**: title in spaced capitals, thin grey rule, two-column body where length allows, logo bottom right, footer with the Substack and GitHub links.
- **Repository README**: plain Markdown, no badges beyond a license badge, the logo at the top at reduced width, the same voice as the newsletter.

When producing files, follow the environment's document or presentation skill for generation mechanics and apply the rules above for appearance. Verify the rendered output against the palette and logo rules before delivering.
