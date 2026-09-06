---
name: tailored-client-deck
description: Builds client-specific presentation decks for sales, proposals, kickoffs, quarterly reviews, and partnership pitches, tailored to the named client's context and carrying the correct branding (the user's brand, the client's logo, or both). Use this skill whenever the user asks to prepare a deck for a specific company, personalize a standard deck for a prospect, add a client's logo to a presentation, build a proposal or pitch deck for a named account, prepare a QBR or kickoff presentation, or says "make this deck for [company]", "customize our pitch for [client]", "co-branded deck". Trigger whenever a presentation is destined for an external, named audience, even if the user does not mention branding.
---

# Tailored Client Deck

A tailored deck is a standard deck that has been rebuilt around one client, not a template with a logo pasted on the cover. The client should recognize their own situation on every slide before slide four, or the tailoring did not happen.

## Tailoring workflow

### 1. Build the client context sheet first

Before touching slides, assemble a one-page context sheet and confirm it with the user:

- Who the audience is by name and role, and who the decision maker is.
- What the client is trying to achieve this year, in their own words where available (their website, annual report, job postings, leadership interviews, earnings calls for public companies).
- The specific problem or opportunity this meeting addresses.
- What they already know about the user's organization and what has been discussed before.
- Their vocabulary: how they name their customers, products, regions, and teams. Use their words, not the user's internal terms.
- Constraints: budget cycle, procurement rules, competing vendors in play, timing.

Use the external-insights skill in this library when the context needs research; use connected data tools (CRM, enrichment services) when available. Gather and cite; never invent a client fact.

### 2. Map the standard content to the client

Take the user's baseline deck or narrative and run each slide through one question: what does this mean for this client specifically? Three outcomes are possible:

- **Rewrite**: the slide's point is relevant but must be restated in the client's terms, with their numbers, their example, their vocabulary.
- **Keep**: the slide is general and still lands (rare; usually credentials and methodology).
- **Cut**: the slide does not bear on this client's decision. Cut it, even if it is beautiful.

Add slides the standard deck lacks: the client's situation as the opening, a slide showing how the offer maps to their stated priorities, and a concrete first step sized to their constraints.

### 3. Deck structure for a named client

1. **Their situation** (title states it as a fact about them, sourced). This slide proves the homework was done.
2. **What is at stake** for them: the cost of the problem or the size of the opportunity in their numbers.
3. **The approach**, mapped to their priorities, in their vocabulary.
4. **Evidence it works**: relevant cases, similar clients (anonymized where required), results with numbers.
5. **What it would look like for them**: a mock deliverable, a timeline against their calendar, the team.
6. **Investment and terms**, plainly.
7. **Next step**, one action with a date.

### 4. Branding and logos

- **Whose brand leads**: the presenter's brand governs the template; the client's logo appears on the cover and, if desired, in a small "prepared for" position on section dividers. Never place the client's logo in the presenter's logo position or resize it to dominate.
- **Logo handling**: use the client's official logo files (their brand or press page, or a file the user provides). Preserve aspect ratio; never stretch, recolor, or apply effects. Respect clear space equal to at least the logo's height on all sides. Use the version (full-color, mono, reversed) that fits the slide background. If only a low-resolution version is available, say so and ask for a better file rather than shipping a blurry logo.
- **Presenter brand**: apply the organization's brand skill if one exists in the environment (colors, fonts, cover and closing slides, footer). For BreakTalk-branded material, use the breaktalk-brand skill in this library. When no brand is defined, use one dark neutral, one accent color, one sans-serif family.
- **Co-branded decks**: cover carries both logos, presenter's left, client's right, same visual weight, separated by clear space. Interior slides stay in the presenter's system.

### 5. File building

Follow the environment's presentation-building skill for layout and file generation. Charts state one message each, labeled directly, legend outside the plot area, consistent palette across the deck. Speaker notes carry the talk track and the client facts behind each slide.

## Quality bar

- A slide-by-slide test: could this slide be sent to a different client unchanged? If more than three slides pass, the deck is not tailored.
- Every client fact carries its source in the speaker notes.
- Client name spelled and capitalized exactly as they write it, everywhere.
- Logos verified for aspect ratio, resolution, and clear space.
- The next step is one action, one date, one owner.
