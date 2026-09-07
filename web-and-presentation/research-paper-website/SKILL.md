---
name: research-paper-website
description: Builds the companion page for a paper or research project as static files that will still open in ten years: the plain-language finding before the abstract, the headline figure with real alternative text, the paper in a version the publisher permits, the data and code with their licences, a copyable citation and BibTeX block, persistent identifiers, and an accurate publication status with a review date. Enforces no build step, no tracking, accessibility as a default, and figures identical to the print versions and following the house monochrome-first standard. Use this skill when someone wants a website for a paper, a project page, a landing page for a study, a place to send people that is not a PDF, or a page for a working paper they are about to circulate.
---

# Research Paper Website

A paper reaches people who will never open a PDF: a journalist on a deadline, a practitioner deciding whether the method applies to their own service, a hiring committee reading fifteen candidates in an afternoon, someone who saw a figure quoted on social media and wants to know what it actually showed. If the only public artefact is a publisher's landing page behind an institutional login, those people bounce, and the work reaches the twenty people who already knew about it.

The second failure is slower and does more damage. A project page gets built during the excitement of a first submission, says "under review", links a PDF, and is never touched again. Two years later it is the top result for the paper's title, the paper has been published with a different sample and a smaller headline effect, and the page is quietly circulating a superseded number under the author's name. A stale page is worse than no page, because everything on it is a claim about a current state.

Build it as static files. One HTML file with the CSS inline, a folder of figures, the documents beside them. No framework, no build step, no database. A page built that way opens in ten years; a page built on a toolchain stops building in three, and the person who could fix it has moved institutions.

## When to use this, and when not to

Use it for a single paper or a single project: a working paper about to circulate, a published article that needs a public home, a study with a data release, a report whose figures people will want to reuse.

Do not use it for the researcher's own homepage listing everything they have written, which is `academic-personal-site` and answers a different question for a different reader. Do not use it where the point is for readers to slice results themselves, which is `interactive-results-explorer`; a project page can link to one, but a page whose central content is a filter interface is a different build with different risks. Do not use it as the replication package: the archive of code, data and instructions is `replication-package`, and this page links to it rather than replacing it. Do not use it for an operating numbers page, which is `metrics-dashboard-page`. Do not use it as a substitute for the paper itself, which is `full-manuscript-build`.

## What you need before starting

**The finding, in one sentence you are willing to be quoted on.** Everything on the page is arranged around it. Missing: write three candidate sentences and make the author choose. This conversation usually improves the abstract as well.

**The publication status, and what the publisher's agreement permits you to post.** Whether the hosted file may be the published version, the accepted manuscript, or only the submitted preprint. Missing: host the accepted manuscript, label it explicitly as such, and check the policy before the page goes public. Getting this wrong is a copyright matter, not a style preference.

**Persistent identifiers.** A DOI for the article where one exists, a DOI or accession for the data, and a researcher identifier for each author. Missing: link the repository or preprint record as canonical and add the DOI when it is issued, with a note in the page's own to-do rather than in your memory.

**The figures, as the exact files used in the paper.** Vector where the format allows, plus a raster fallback at a resolution that survives a projector. Missing: regenerate them from the analysis code rather than exporting from the manuscript, and check them against the paper before publishing.

**Alternative text for every figure, written by someone who knows what the figure shows.** Missing: draft it from the caption and the underlying result, then have an author check it. Alternative text is a factual claim about the data and should be reviewed like one.

**The data and code location, with licences.** Missing: say plainly on the page that data are not available and why, since an unexplained absence reads worse than a stated restriction.

**Author list, affiliations, contact, funding and conflicts.** Missing: ask. A page with no contact address gets no replication requests, which is not the same as there being none.

**Where it will live.** A domain the authors control, or an institutional or repository host. Missing: publish under a repository's static hosting, which is free and versioned, and register a redirect from anywhere the link has already been shared.

## The method

1. **Write the plain-language paragraph before anything else.** What was asked, what was found, and why it matters, for an intelligent person outside the field. Not the abstract. The test is mechanical: read it aloud to someone in a different discipline and ask them to say the finding back. If they cannot, rewrite it. This paragraph does most of the page's work and deserves more drafting time than the rest combined.

2. **Choose one headline figure.** The rule: the figure that carries the finding, not the one that took longest to make and not the study design diagram. If two figures compete, the page is probably reporting two findings and the plain-language paragraph needs cutting first.

3. **Fix the section order and do not deviate.** Title and status, the finding in plain language, the headline figure, the abstract, get the paper, data and code, citation, all figures and tables, authors and contact. This order serves the reader who arrived from a link, and puts the abstract below the plain summary deliberately.

4. **Write semantic HTML, with the content in the markup rather than assembled by script.** Everything that is text must be present with scripting disabled. That is not an accessibility nicety here; it is what makes the page survive being archived, scraped, printed, or read on a hostile network.

```html
<article>
  <header>
    <h1>Ambulance response times and hospital handover delays in rural districts</h1>
    <p class="authors">
      <a href="https://orcid.org/0000-0000-0000-0000">R. Okonjo</a>,
      L. Marchetti, S. Haldorsen
    </p>
    <p class="status"><strong>Working paper</strong>, version 3, 14 April 2026.
       Under review. <a href="#cite">How to cite</a></p>
  </header>

  <section aria-labelledby="finding">
    <h2 id="finding">What we found</h2>
    <p class="lede">Handover delays at receiving hospitals explain more of the
       variation in rural ambulance response times than distance does. ...</p>
  </section>

  <figure>
    <img src="figures/fig1-handover-response.svg"
         alt="Scatter plot of 214 districts. Mean handover delay on the horizontal
              axis, from 5 to 62 minutes. Mean response time on the vertical axis,
              from 8 to 41 minutes. Points rise steadily together; districts above
              40 minutes of handover delay almost all exceed a 25 minute response.">
    <figcaption><strong>Figure 1.</strong> Handover delay against response time,
      214 districts, 2019 to 2024. Marker shape distinguishes urban, mixed and
      rural districts.</figcaption>
  </figure>
</article>
```

5. **Style with a small token block and system fonts.** No webfont request, because a page that waits on a font server is a page that fails on a slow connection and stops rendering correctly when that server changes. Define the palette once, honour the reader's colour scheme, and keep the measure readable.

```css
:root {
  --ink:        #16181d;   /* body text */
  --paper:      #fbfaf8;
  --rule:       #d8d4cd;
  --navy:       #1b2a4a;   /* accent one, used sparingly */
  --wine:       #6e1f2b;   /* accent two, used sparingly */
  --measure:    38rem;     /* about 70 characters */
}
@media (prefers-color-scheme: dark) {
  :root { --ink: #ece9e4; --paper: #14161a; --rule: #363b44;
          --navy: #93a9d4; --wine: #d99aa4; }
}
body { background: var(--paper); color: var(--ink); margin: 0 auto;
       padding: 2rem 1.25rem; max-width: var(--measure);
       font: 1.0625rem/1.6 system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
figure { margin: 2rem 0; }
figure img { width: 100%; height: auto; }
figcaption { font-size: 0.9375rem; color: var(--ink); opacity: 0.85;
             border-left: 3px solid var(--rule); padding-left: 0.75rem; }
a { color: var(--navy); }
a:focus-visible { outline: 3px solid var(--wine); outline-offset: 2px; }
@media print { a[href^="http"]::after { content: " (" attr(href) ")"; } }
```

6. **Prepare the figures to the house standard, and make them identical to the paper's.** A web version that differs from the print version is a small dishonesty that becomes an embarrassing one when a reader quotes the wrong number. The standard is monochrome first: series separated by marker shape, dash pattern and fill texture rather than by colour, the legend outside the plot area, and colour restricted to the two accents used sparingly and only where it carries meaning the shapes cannot. `academic-figures-monochrome` holds the method. Provide vector where the format allows, and give every figure a download link, because people take figures for talks and teaching and making that easy is how a paper travels.

7. **Make the citation copyable, with a fallback.** The formatted citation and the BibTeX block are always present as selectable text. A copy button is an enhancement added by script and must not be the only route.

```html
<section id="cite">
  <h2>How to cite</h2>
  <p>Okonjo, R., Marchetti, L., &amp; Haldorsen, S. (2026). Handover delays and
     rural ambulance response times. <em>Working paper</em>. https://doi.org/10.0000/xxxx</p>
  <pre id="bib"><code>@article{okonjo2026handover,
  author  = {Okonjo, Rebecca and Marchetti, Luca and Haldorsen, Sunniva},
  title   = {Handover delays and rural ambulance response times},
  year    = {2026},
  doi     = {10.0000/xxxx}
}</code></pre>
</section>

<script>
  // Progressive enhancement only. Without this script the BibTeX is still
  // present, selectable and printable.
  var pre = document.getElementById('bib');
  if (pre && navigator.clipboard) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.textContent = 'Copy BibTeX';
    btn.addEventListener('click', function () {
      navigator.clipboard.writeText(pre.innerText).then(function () {
        btn.textContent = 'Copied';
        setTimeout(function () { btn.textContent = 'Copy BibTeX'; }, 2000);
      });
    });
    pre.parentNode.insertBefore(btn, pre);
  }
</script>
```

8. **State the data and code position exactly.** Where they are, under what licence, what a person needs in order to reproduce the results, and what is restricted. Link the archive rather than attaching a zip, so there is one canonical copy with a version. The decisions behind that, which archive, which licence, what the deposit contains and which identifier cites it, belong to `replication-package` and are made there. This page states the outcome in three or four lines and links to it, because a second account of the same reasoning will disagree with the archive's own README inside a year.

9. **Add discovery metadata, and nothing that tracks.** A descriptive title, a meta description that is the plain-language sentence, an image for social previews showing the headline figure, and the bibliographic meta tags that reference managers read.

```html
<meta name="description" content="Handover delays explain more of the variation in
      rural ambulance response times than distance does. 214 districts, 2019 to 2024.">
<meta name="citation_title" content="Handover delays and rural ambulance response times">
<meta name="citation_author" content="Okonjo, Rebecca">
<meta name="citation_publication_date" content="2026/04/14">
<meta name="citation_pdf_url" content="https://example.org/paper/okonjo-2026-v3.pdf">
<meta property="og:image" content="https://example.org/paper/figures/fig1-social.png">
```

   No analytics script, no embedded video player, no font service, no comment widget. Research pages have readers who reasonably object to being tracked, and a server log answers the only question worth asking.

10. **Test the page in four ways before publishing.** With scripting disabled, where all text content must remain. At 320 pixels wide, where nothing may scroll sideways. With the keyboard alone, where every link must be reachable and the focus visible. And with the images failing to load, where the alternative text should still convey each finding. These four take fifteen minutes together and catch nearly everything.

11. **Set a status review date on the page and in a calendar.** Publication status and version are the parts that rot. Six months is a reasonable interval, and a note in the page source saying when it was last reviewed keeps the next person honest.

12. **Archive the page and the files.** Where the page holds anything not published elsewhere, deposit a copy in an archive that issues an identifier, and keep the URL stable. A project page that moves loses every link anyone made to it, which is most of its value. Where the thing being deposited is the code and data rather than the page, that deposit is `replication-package`'s job: cite its identifier and do not create a second archive of the same files.

## What to leave out

A slideshow. A hero image with no information in it. Animation on scroll. A newsletter signup. A chat widget. Author photographs at the top, which push the finding below the fold. A "read more" that hides the abstract. Anything that requires a login. Any script that contacts a third party, which includes the convenient ones.

## Worked example

**Situation.** Three authors had a working paper on hospital handover delays, forty-one pages and eight figures, about to be circulated to a policy audience before submission. The data were a licensed administrative extract that could not be redistributed; the code could. One author had a personal domain, and the institutional pages sat behind a template that could not host files.

**Task.** A public page in two days, usable by a policy reader who would not open a PDF, and stable enough that the link could go into a submission and an email to twelve people who would forward it.

**Action.** The first attempt used a static site generator, chosen because one author had it running for a course. It was abandoned after four hours: two of the three authors could not preview a change without installing a toolchain, the theme wanted a palette that fought the figures, and the build produced eleven files where the content was one page. The wrong turn is worth naming, because it is common. A generator is a reasonable choice for fifty pages and a bad one for a single page maintained by people who will not touch it again for six months. The rebuild was one `index.html` with the CSS inline, a `figures/` folder and two PDFs, and every author could edit it.

The plain-language paragraph took four drafts and one test. The first version said the study estimated the association between handover delay and response time controlling for district characteristics, which a policy reader in another team read twice and could not summarise. The fourth version led with the comparison that mattered: delays at the hospital door explained more of the difference between districts than how far the ambulance had to drive. That sentence became the meta description, the social preview caption, and eventually the first line of the abstract.

Figures were regenerated from the analysis code rather than exported from the manuscript, which caught a real defect: figure 4 in the circulating PDF was from an earlier specification with 198 districts rather than 214. The page and the paper were corrected together.

Alternative text took roughly twenty-five minutes for eight figures, because each one is a factual claim and two needed an author to check the range. The scatter plot's text runs to forty-one words and names the axes, their ranges and the direction, which is what a reader without the image needs.

Copy-to-clipboard was added last, and the first version replaced the BibTeX block with a button that generated the text on click. Testing with scripting disabled showed an empty section, invisible to everyone who tested it normally. The fix is the version above: the text is always in the markup and the button is an addition.

**Result.** One page, 312 kilobytes including all eight figures as compressed SVG, and no external requests. It loaded in under a second on a throttled connection and rendered correctly with scripting off.

Over eleven weeks the page produced three concrete things: two requests for the code from teams doing similar work, one of which found a bug in a helper function that changed a robustness table, and an invitation to present. Figures were downloaded ninety-four times, mostly the headline one, which is what a downloadable figure is for. The status line was updated once, from version 3 to version 4, in two minutes, because the status, version and date live in one place in the markup.

### A second scenario, where it goes differently

A registered project with a preregistration, data collection under way, and no results for a year.

The page shape changes because the finding does not exist yet. The plain-language paragraph describes the question and what would count as an answer, the headline figure becomes a design diagram showing the sampling frame, and the get-the-paper section becomes the preregistration with its identifier and date. The status line does more work than anything else on the page, and it carries an explicit next-update date so that a reader in six months knows whether silence means delay or abandonment.

The rules that do not change: static files, no build step, no tracking, real alternative text, and a stable URL. When the results arrive the page is rewritten in place, the preregistration stays linked and clearly marked as prior, and the earlier version stays available so that anyone who cited the design can still see what it said. That last point is the reason to keep the page in a versioned repository from the first day.

## Output

A folder, publishable as-is.

```
paper-page/
  index.html            one page, CSS inline, content in the markup
  okonjo-2026-v3.pdf    the version the publisher permits, named with version
  appendix.pdf
  figures/
    fig1-handover-response.svg    vector, as used in the paper
    fig1-handover-response.png    raster fallback, 2000px wide
    fig1-social.png               1200 by 630 for link previews
    ...
  sitemap.xml
  README.md             where the code and data live, and the review date
```

The page carries these sections in this order.

| Order | Section | Non-negotiable content |
| --- | --- | --- |
| 1 | Title and status | Authors with identifiers, version, date, publication status |
| 2 | What we found | One paragraph, plain language, no jargon, before the abstract |
| 3 | Headline figure | Full width, standalone caption, real alternative text |
| 4 | Abstract | As written for the paper |
| 5 | Get the paper | Version, date, DOI as canonical where it exists, which version is hosted |
| 6 | Data and code | Location, licence, what is restricted and why |
| 7 | How to cite | Formatted citation and BibTeX, both selectable |
| 8 | All figures and tables | Full resolution, downloadable, each with caption and alternative text |
| 9 | Authors and contact | Working email, funding, conflicts |

## Failure modes

**The stale status.** Recognise it by a page that still says under review more than a year after the date beside it. Fix with a review date on the page and the status held in one place in the markup so updating it is a two-minute job.

**The abstract used as the summary.** Recognise it when the first paragraph contains a method name in the first line. The abstract is written for referees and is the wrong instrument for the reader who arrived from a link. Both belong on the page, in that order.

**Figures that drifted from the paper.** Recognise it by regenerating one and comparing. Fix by generating page figures from the analysis code, never by exporting from the manuscript file.

**Alternative text that repeats the caption.** Recognise it when the text says "Figure 1. Handover delay against response time" and nothing else. A reader who cannot see the image needs the axes, the ranges and the direction of the relationship.

**Content assembled by script.** Recognise it by disabling scripting and finding an empty section. Fix by putting the text in the markup and using script only for enhancements.

**A toolchain nobody else can run.** Recognise it when one author is the only person who can publish a change. The consequence is not inconvenience, it is that the page stops being updated the week that person gets busy.

**Hosting the wrong version.** Recognise it by checking the publisher's self-archiving policy against the file you posted. Fix by hosting the permitted version and labelling it clearly, since an unlabelled PDF is assumed to be the published article.

**Third-party scripts arriving quietly.** Recognise them in the network requests: a font service, an embedded player, an analytics tag added by a colleague. Fix by keeping the page to files you host, and check after anyone else edits it.

## Edge cases

**Data that cannot be shared.** State the restriction, the licence holder, and the process by which someone else could obtain the same extract. Publish whatever can be published: the code, the derived aggregates behind the figures, the variable definitions. Silence is read as unwillingness. Keep it to the restriction and the route in one short block, and link `replication-package`, where the licence terms and the application process are documented in full.

**A retracted or corrected paper.** The page says so at the top, in the status line, permanently, with the date and the nature of the correction. Removing the page is the worst option available, because the citations remain.

**A paper with fifteen authors.** List them all in the correct order in the markup, showing the first three with the rest inside a `details` element so it works without scripting. Do not reorder them for aesthetics.

**An embargo.** Publish the page with the finding, the status and the embargo date, and hold the file. A page that exists and says when the paper will be available is more useful than an absence.

**A non-English audience.** Provide the plain-language paragraph in both languages, with `lang` attributes on each so screen readers pronounce them correctly. Translating the whole page doubles the maintenance and the summary is where most of the value is.

**The institution insists on their template.** Build the real page on a domain the authors control, put the canonical link on the institutional page, and add a canonical link element on the institutional copy where the platform permits it. Institutional pages disappear when people move.

**A project spanning several papers.** One page per paper plus a short index. Resist the single long page: readers arrive looking for one result, and the section they need should be the whole page.

## Quality bar

- Static files with no build step, and every word of text present with scripting disabled.
- The plain-language paragraph appears before the abstract and was tested on someone outside the field.
- Publication status, version and date are accurate, in one place in the markup, with a review date set.
- Figures are identical to the paper's, follow the monochrome-first house standard, and are downloadable.
- Every figure has alternative text stating what it shows, checked by an author.
- The citation is present as formatted text and as BibTeX, both selectable without scripting.
- Data and code are linked with their licences, or their absence is explained on the page.
- Persistent identifiers are used, the URL is stable, and no third-party request is made by the page.

## Adapting this to your context

The defaults come from quantitative social science: a working paper circulated before submission, a DOI on the article, greyscale figures, one page per paper.

- **Preprint norms.** Posting a working paper is routine in economics and physics, unusual in parts of medicine and the humanities, and in computer science the conference version is the article. Read the venue's policy before deciding what the page hosts.
- **Persistent identifiers.** A DOI for article and data. Where none exists, use what your field resolves on: an arXiv or SSRN identifier, a handle or ARK, a study accession, an ISBN, a repository record.
- **The headline figure.** A results chart here. For a systematic review it is the PRISMA flow diagram, for a trial the CONSORT diagram, for a qualitative study a coding framework. The rule survives: one figure, and it carries the finding.
- **The figure standard.** Monochrome first, series separated by shape and dash. For maps, photographs or imaging, keep only the part that matters: meaning is never carried by colour alone.
- **The status review interval.** Six months. Three while data collection is live or turnaround is fast; a year for a monograph.
- **What not to change.** Static files with no build step, the plain-language finding above the abstract, real alternative text checked by an author, a status and version dated on the page.

## Related skills

`academic-figures-monochrome` produces the figures and holds the house standard this page inherits. `replication-package` builds the archive this page links to. `academic-personal-site` is the author's own page and links to project pages like this one. `interactive-results-explorer` is what to build when readers need to slice the results themselves, and it links back here for the paper and the citation. `abstract-and-title` sharpens the sentences this page is arranged around. `full-manuscript-build` produces the paper itself.
