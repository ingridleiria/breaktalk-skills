---
name: research-paper-website
description: Builds the companion website for a paper or a research project: a single page carrying the plain-language summary, the finding, the figures at full resolution, the paper and appendix, the data and code with their licences, the citation in copyable form, and the authors, built as static files that will still work in ten years. Covers structure, accessibility, figures that match the print versions, persistent identifiers, and hosting that costs nothing. Use this skill when someone wants a website for a paper, a project page, a landing page for a study, or a place to send people that is not a PDF.
---

# Research Paper Website

A paper reaches people who will never open a PDF: journalists, practitioners, a hiring committee, someone who saw a figure on social media. A project page is the version they can read, and it is the canonical place the paper's material lives once the journal has put the article behind a login.

Build it as static files. No framework, no build step, no database. A single HTML file with the CSS inline, a folder of figures, and the documents beside it. That page will still open in ten years, which almost nothing built on a framework will.

## Structure, in this order

**Title, authors, affiliations, date, and status.** Say plainly whether this is a working paper, under review, or published, and update it. A page that still says "under review" two years later damages the author more than no page.

**The finding, in one paragraph, in plain language.** Not the abstract. What was asked, what was found, and why it matters, written for an intelligent person outside the field. This paragraph does most of the work of the page and is worth more drafting time than the rest combined.

**The headline figure**, large, with a caption that stands alone. One figure, chosen because it carries the finding. Everything else goes lower.

**The abstract**, as written for the paper, for the readers who want it.

**Get the paper.** The PDF, with the version and date. Where a journal version exists, link the DOI as the canonical version and be clear about which version the hosted file is, since publisher agreements differ on what may be posted.

**Data and code.** Where they are, what licence applies, and what a person needs to reproduce the results. Link the repository or the archive rather than attaching a zip. `replication-package` covers what should be in it.

**Citation**, in copyable form: a formatted citation and a BibTeX block in a code block a reader can select cleanly.

**Figures and tables**, all of them, at full resolution, each downloadable, each with its caption. People take figures for talks and teaching, and making that easy is how a paper travels.

**Authors and contact**, with links, and a funding and conflicts statement where one applies.

## Figures

Use the same figures as the paper. A web version that differs from the print version is a small dishonesty and eventually an embarrassing one.

Follow the house standard: monochrome first, series separated by marker, dash pattern, and texture rather than colour, legends outside the plot area, and where colour is used at all, restricted to the accent palette. `academic-figures-monochrome` has the method. Export at a resolution that survives a projector, provide a vector version where the format allows, and give every figure real alternative text describing what it shows rather than repeating the caption.

## Accessibility, which is not optional for public research

Semantic headings in order. Alternative text on every figure that conveys the finding, not the file name. Contrast that passes at normal body size. Text that reflows on a phone, since a large share of readers will arrive on one. Tables marked up as tables with headers rather than as images. Nothing that requires a mouse.

A research page that a screen reader cannot use excludes exactly the readers who most rely on the text rather than the picture.

## Persistence

Use a persistent identifier for the paper and for the data, and put them on the page. Archive the page itself if it holds anything not published elsewhere.

Keep the URL stable. A project page that moves loses every link anyone made to it, which is most of its value. Prefer an institutional or a personal domain you control over a platform that may not exist in five years.

## Hosting

Static hosting from a repository is free, versioned, and outlives most alternatives. The repository is also the natural home for the code, which means the page and the material stay together.

Add a plain sitemap and descriptive page metadata so the page is findable, and a social preview image so a shared link shows the headline figure rather than a blank card.

## What to leave out

A slideshow. A hero image with no information in it. Animation. A newsletter signup. Anything that loads a tracker, since research pages have readers who reasonably object to being tracked, and there is nothing here worth measuring that a server log would not tell you.

## Quality bar

- Static files, no build step, and the page opens correctly with scripting disabled.
- The plain-language paragraph is written for someone outside the field and appears before the abstract.
- Publication status is accurate and dated.
- Figures match the paper exactly and follow the house figure standard.
- Every figure has alternative text describing what it shows.
- The citation is present in both a formatted and a BibTeX form, copyable.
- Data and code are linked with their licence, or their absence is explained.
- Persistent identifiers are used and the URL is one that will not move.
