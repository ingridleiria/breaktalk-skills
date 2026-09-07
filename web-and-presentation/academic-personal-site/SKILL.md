---
name: academic-personal-site
description: Builds a researcher's own site around the three people who actually visit one: a search committee with ninety seconds, an editor or referee who wants a paper immediately, and a potential collaborator or student deciding whether your interests overlap theirs. Produces a single static page with the work described in plain words above the fold, publications listed so they can be found and cited with resolvable links and labelled versions, working paper statuses that are accurate and dated, teaching and supervision including whether students are being taken, a CV that matches the page, and a maintenance rhythm that stops the whole thing going stale. No build step, accessible, fast on a slow connection, on a domain the author controls. Use this skill when someone wants an academic homepage, a personal research site, a publications page, a page before the job market or a grant round, or says their website is out of date.
---

# Academic Personal Site

Three people visit an academic site and they want different things. A search committee member, reading fifteen candidates in an evening, wants to know in ninety seconds what you work on and whether the record supports the claim. An editor looking for a referee, or a referee checking a citation, wants a specific paper, in one click, in a version they can read now. A potential collaborator or a prospective student wants to know whether your interests overlap theirs, whether you are taking students, and how to reach you.

Most academic sites serve none of the three. The work is described in field labels rather than in sentences, the publications are a list of titles with no links or a screenshot of a CV page, and the contact route is a form. The cost is invisible and real: the referee gives up and the citation goes unchecked, the student writes to someone else, and the committee member forms an impression from an outdated page and moves on.

The second failure is decay. A site is built in a fortnight of enthusiasm and then not touched, and everything on it silently becomes a claim about a past state: a paper listed as under review for three years reads as a paper rejected repeatedly, which may be unfair and is unavoidable. A stale site is worse than no site, so the maintenance model is part of the design rather than an afterthought.

## When to use this, and when not to

Use it for a researcher's own page: before a job market, before a grant round, on arrival at a new institution, or when an existing site has gone stale and needs rebuilding rather than patching.

Do not use it for the companion page to a single paper or project, which is `research-paper-website`; this site links to those. Do not use it for a page whose purpose is letting readers slice results, which is `interactive-results-explorer`. Do not use it for a team's operating numbers, which is `metrics-dashboard-page`. Do not use it to fix the bibliography itself: style conversion, BibTeX hygiene and consistent author ordering are `references-and-bibliography`, and this page should consume a clean list rather than becoming the place errors are discovered. Do not use it as a substitute for a professional network profile where the audience is employers outside research; that is a different document with a different reader.

## What you need before starting

**One or two sentences saying what you work on, in words a colleague in an adjacent field would understand.** Not a field label. What question, in what setting, using what kind of evidence. Missing: draft three versions from the abstracts of the three most recent papers and pick the one a non-specialist can repeat back.

**The publication list, with DOIs and the version status of each hosted file.** Missing a DOI: link the repository record or the publisher page, and add the DOI later. In fields where books, chapters and proceedings dominate and DOIs are rare, use the link order in the edge case below rather than waiting for one. Missing the version status: do not host the file until the publisher's policy is checked, because posting the published version where only the accepted manuscript is permitted is a copyright matter.

**The current status and date of every working paper.** Missing: ask the author for each, one line each. This conversation usually removes two or three entries, which is itself the value.

**A photograph.** People at conferences want to recognise you. Missing: proceed without one, and do not substitute a logo or an avatar.

**A working email address, written so a person can use it.** Missing: the site cannot do its third job. Get one, even an alias.

**The CV, as a dated PDF.** Missing: publish the site without it rather than linking a file that does not exist, and set a date to add it.

**A domain you control, or a plan to get one.** Missing: publish under a repository's static hosting now and move later, keeping the old address redirecting. An institutional page will disappear when you move institutions, taking every link with it.

**A researcher identifier and a scholar profile link.** Missing: create the identifier; it takes minutes and it is what disambiguates you from the other person with your surname and initials.

## The method

1. **Write the ninety-second block first.** Name, position, institution, the one or two sentences, the photograph, the email address, and links to the scholar profile, the researcher identifier, the code repository and the CV. Nothing else goes above the fold. Test it by asking someone outside your subfield to say, after fifteen seconds, what you work on.

2. **Decide the canonical home and handle the institutional page.** Your own domain is canonical. Where the institution requires a page on their system, keep it short, point it at the canonical site, and add a canonical link element where the platform allows one. Keep every previous address redirecting; links you have already sent out are the most valuable thing the site has.

3. **Build the publications section as the centre of the page, in semantic markup with a stable anchor per paper.** Group by type, published first, then working papers, then work in progress, then other writing; reverse chronological within each. Full citation, all coauthors in the correct order, one line of plain description, and links that work.

```html
<h2 id="publications">Publications</h2>

<h3 id="pub-journal">Journal articles</h3>
<ol class="pubs" reversed>
  <li id="okonjo2026handover">
    <p class="cite">Okonjo, R., Marchetti, L., &amp; Haldorsen, S. (2026).
      Handover delays and rural ambulance response times.
      <em>Journal of Health Services Research</em>, 41(2), 188 to 213.</p>
    <p class="plain">Delays at the hospital door explain more of the variation
      in rural response times than driving distance does.</p>
    <p class="links">
      <a href="https://doi.org/10.0000/xxxx">DOI</a> |
      <a href="papers/okonjo-2026-accepted.pdf">Accepted manuscript (PDF)</a> |
      <a href="projects/handover/">Project page</a> |
      <a href="#cite-okonjo2026handover">BibTeX</a>
    </p>
  </li>
</ol>
```

   The stable `id` matters more than it looks. It lets you send someone a link straight to one paper, and it survives reordering when the next publication appears.

4. **Label every hosted file with which version it is.** Published version, accepted manuscript, or submitted preprint, in the link text, not in a note at the bottom. An unlabelled PDF is assumed to be the published article, and referees notice when it is not.

5. **Give each substantial paper one line of plain description.** A reader deciding whether to open a PDF decides on that line. It is also the line a journalist quotes and the line a committee member remembers.

6. **Separate working papers from work in progress, and date every status.** A working paper is circulating and can be read; work in progress is a title and a sentence. Listing an unwritten paper as available is a trap you set for yourself for the day someone asks for it. Write the status as "Under review, submitted March 2026" rather than "Under review", so the reader can judge for themselves and so you can see at a glance what has gone stale.

7. **Write the teaching, supervision and service section for the people who read it.** What you teach and at what level, whether you are taking students, which prospective students look for and almost nobody states, and editorial or refereeing service where the field values it. Say what you would like to be contacted about; most collaboration starts with someone reading a title and not knowing whether writing is welcome.

8. **Keep the CV and the site consistent, and check it mechanically.** One PDF, dated in the filename, matching the site exactly. A CV listing a paper the site does not is the inconsistency noticed by exactly the people you least want noticing it. The check is simple and takes five minutes: list the titles from each, sort both, and compare.

9. **Build it as one static page with the CSS inline.** No framework, no build step, no content system to upgrade. Add a print stylesheet, because committee members print, and keep the whole page under a couple of hundred kilobytes so it opens instantly on a conference network.

```css
:root { --ink:#16181d; --paper:#fbfaf8; --rule:#d8d4cd;
        --navy:#1b2a4a; --wine:#6e1f2b; }
@media (prefers-color-scheme: dark) {
  :root { --ink:#ece9e4; --paper:#14161a; --rule:#363b44;
          --navy:#93a9d4; --wine:#d99aa4; }
}
body { background:var(--paper); color:var(--ink); max-width:44rem;
       margin:0 auto; padding:2rem 1.25rem;
       font:1.0625rem/1.6 system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
.pubs { list-style:none; padding:0; }
.pubs li { border-top:1px solid var(--rule); padding:1rem 0; }
.plain { font-size:0.9375rem; opacity:0.85; }
a { color:var(--navy); }
a:focus-visible { outline:3px solid var(--wine); outline-offset:2px; }
.status-stale { border-left:3px solid var(--wine); padding-left:0.5rem; }
@media print {
  body { max-width:none; font-size:10.5pt; }
  .plain, nav, .photo { display:none; }
  a[href^="http"]::after { content:" (" attr(href) ")"; font-size:9pt; }
}
```

10. **Use no scripting for anything that is content.** Publications, statuses, contact details and teaching information all live in the markup. Where a long abstract would clutter the list, use a `details` element, which expands without JavaScript and is reachable by keyboard.

11. **Test the four things that actually break.** Every link resolves, checked with a link checker or by hand at least twice a year. The page reflows at 320 pixels. Headings are in order with no level skipped, and images have real alternative text. The page is usable by keyboard with a visible focus indicator.

12. **Set the maintenance rhythm and write it into the repository.** Twice a year on fixed dates, plus a trigger update whenever a paper changes status, a new paper circulates, or you move institutions. Keep a short `MAINTENANCE.md` beside the page listing what to check, because the reason sites go stale is never intent, it is that nobody remembers what the checklist was.

## What to leave out

A blog you will abandon after three posts, which dates the site more precisely than anything else on it. A landing animation. A hero image with no information. A publications list that is an image or an embedded PDF viewer, which cannot be searched, copied or read by a screen reader. A contact form instead of an address. A visitor counter. A carousel of institution logos. A page that requires a login. Anything that loads a third-party script, which on an academic site buys nothing and costs the reader their privacy.

## Worked example

**Situation.** A postdoc in her fourth year, going on the job market in eight weeks, with fourteen publications, six working papers, and an existing site on a content platform that had not been updated in nineteen months. Two working papers listed as under review had been published; one listed as in progress had been abandoned; the hosted PDF of her best-cited paper was the submitted version, which differed materially from the published one.

**Task.** A site a committee member could read in ninety seconds and a referee could use in one click, ready in a week, maintainable by her alone.

**Action.** The first attempt was a rebuild on the same platform with a cleaner theme, on the reasoning that the content was the problem rather than the tooling. It was abandoned after two days. The theme controlled the publications layout, which meant every entry had to be a blog post with fields that did not match a citation, the plain-language line had nowhere to go, and a platform update mid-build changed the heading levels. The general lesson is worth stating: for a page that is one page, a system whose job is to manage many pages is pure cost, and the cost is paid in exactly the week you have least time.

The rebuild was one `index.html`, a `papers/` folder and a `MAINTENANCE.md`, edited directly. It took eleven hours across three days, of which about seven were content rather than code.

The ninety-second block took eight drafts. The version that worked named the setting and the evidence rather than the literature: what happens to patients when ambulance services and hospitals are managed by different organisations, using administrative records from four countries. A colleague in political science could repeat it back, which was the test.

The publication audit produced the real work. Fourteen entries, of which three had no resolvable link, two pointed at a departmental page that had been retired, and one had two coauthors in the wrong order. Two working papers moved to published. The abandoned project came off entirely, which she resisted and then agreed to, on the reasoning that a title with no paper behind it costs more in the one conversation where somebody asks for it than it gains in the many where nobody looks.

Version labelling caught the significant defect. The submitted-version PDF had a headline coefficient that had changed by roughly a fifth in the published version. It was replaced with the accepted manuscript, labelled as such, with the DOI as canonical, and she wrote to the two people she could remember sending the old file to.

The university page was left in place, cut to four lines and a link, with a canonical link element added, which the platform supported. Her own domain was already registered and had been pointing at the old platform, so the redirect was a one-line change.

**Result.** One page, 96 kilobytes with the photograph, no external requests, loading in well under a second on a hotel network. She was asked about the plain-language line in two of her five first-round interviews, in both cases quoted back at her, which is the clearest evidence available that the ninety-second block is what gets read.

Maintenance held for the following year: two scheduled updates and four trigger updates, each under fifteen minutes, because the file is a file. The status of every working paper was dated, and at the second scheduled update two of them had passed a year under review, which prompted a different and more useful conversation with her coauthors.

### A second scenario, where it goes differently

A full professor running a group of eleven, with a lab site as well as a personal one, and a stated preference for not maintaining anything personally.

The design pressure inverts. The personal page still serves the three readers and stays a single file, but the group site carries people, vacancies, funding and current projects, all of which change more often than a publication list, and none of which the professor will update. So the maintenance model becomes the design: one named owner among the postdocs, a rota that transfers with a documented handover, a `MAINTENANCE.md` written for someone who has never seen the files, and a hard rule that a page nobody owns gets deleted rather than left to rot.

Two structural differences follow. Vacancies carry an explicit closing date and are removed on it, since nothing damages a group's credibility with applicants faster than an open position that closed two years ago. And people pages carry a leaving date and stay up afterwards as alumni, because former members' pages accumulate links and deleting them breaks the record of who did the work.

What does not change: static files, no build step, plain words above the fold, resolvable links, real alternative text, and a domain the group controls rather than an institutional path that will move at the next reorganisation.

## Output

```
site/
  index.html          one page, CSS inline, all content in the markup
  cv-okonjo-2026-04.pdf
  papers/
    okonjo-2026-accepted.pdf
    ...
  img/photo.jpg
  MAINTENANCE.md      the checklist and the two fixed dates
```

The page carries these sections in this order.

| Order | Section | Non-negotiable content |
| --- | --- | --- |
| 1 | Above the fold | Name, position, one or two plain sentences, photograph, email, identifiers, CV link |
| 2 | Publications | Grouped by type, reverse chronological, resolvable links, version labels, one plain line each |
| 3 | Working papers | Status and date on each, hosted file where permitted |
| 4 | Work in progress | Titles and one sentence, clearly not available |
| 5 | Teaching and supervision | Courses and level, whether taking students, what to contact you about |
| 6 | Service | Editorial and refereeing, where the field values it |
| 7 | Contact | Working address, and where you are based |

Each publication entry follows one shape.

```
[Authors] ([year]). [Title]. [Venue, volume, pages].
[One plain sentence on what it finds.]
DOI | [Version label] (PDF) | Project page | BibTeX | Data and code
```

## Failure modes

**Stale statuses.** Recognise it by any status line without a date, or with a date over a year old. Fix by dating every status and reviewing on the two fixed dates.

**A publications list that cannot be read by a machine.** Recognise it when the list is an image, an embedded viewer, or a link to a CV PDF. It cannot be searched, copied, or read aloud, which fails the referee and the screen reader in one move.

**No email address.** Recognise it when the only contact route is a form or a social profile. The third reader, the one who might become a collaborator or a student, simply leaves.

**The abandoned blog.** Recognise it by a most-recent post more than a year old. Remove the section; a dormant blog dates a site more precisely than anything else on it.

**The institutional page ranking above your own.** Recognise it by searching your own name. Fix with a canonical link where supported, a short institutional page that points onward, and consistent use of your own address in papers and profiles.

**CV and site diverging.** Recognise it by sorting both title lists and comparing. Fix by updating them together, always, as one task.

**A hosted file that is the wrong version.** Recognise it by opening your own PDF and comparing the headline number to the published article. Fix by hosting the permitted version and labelling it.

**A theme or platform upgrade that breaks the page.** Recognise it when something changes that you did not change. This cannot happen to a static file, which is the argument for one.

**Everything above the fold except the work.** Recognise it when a photograph, a set of logos and a navigation bar push the description below the first screen. The committee member does not scroll.

## Edge cases

**A name change.** List both names on the page, keep the old one findable in the markup and in the identifier record, and never quietly rewrite past authorship. The purpose is that a citation under either name resolves to you.

**A name that appears in more than one script or transliteration.** Give the primary form in the heading, the alternative form in the markup with a `lang` attribute, and use one consistent romanisation in citations. Ambiguity here costs citations that are attributed to a phantom second person.

**Job market timing.** Freeze the structure four weeks before applications and change only content afterwards. A site rebuilt the week applications open will have a broken link on the day it is read.

**Work that cannot be listed.** Classified, commercially confidential or embargoed work is described at a level the agreement permits, with the restriction stated. An unexplained four-year gap invites a worse inference than a stated restriction.

**Leaving academia, or working across both.** Keep the research record intact and accurate, add a plain line saying what you do now, and do not delete papers. The record is the asset and it will be checked.

**Student and coauthored work.** Where a student led, say so in one line. It costs nothing, it is true, and the people who matter notice both its presence and its absence.

**Books, chapters and proceedings rather than journal articles.** In much of the humanities and in computer science the record is monographs, chapters in edited volumes, conference papers, and sometimes editions, translations or catalogues, and DOIs are often absent. Keep the grouping rule and change the groups: books first, then edited volumes and chapters, then peer-reviewed conference papers, then journal articles and other writing. Name the venue and its acceptance year on every conference paper, because a reader outside the field cannot tell a workshop from a flagship conference and will not guess. Where there is no DOI, link in this order: a repository record with a permanent identifier such as a handle or an ARK, the publisher's page, the ACM or IEEE Digital Library record, arXiv or another preprint server, then a library catalogue record with its ISBN. A chapter you cannot host still needs the volume, the editors, the publisher and the pages, since that is what a citation is made of. For a monograph, one plain line, the publisher link and a catalogue link is the whole entry, and reviews of the book belong under other writing rather than in the publication list.

**An institution that mandates a template.** Build the real site on your own domain and treat the institutional page as an advertisement for it. Do not fight the template.

**Readers on slow or metered connections.** Keep total page weight under about two hundred kilobytes, compress the photograph, and do not load a font service. A large share of the international readers this page is for are on a connection that makes a heavy page unusable.

## Quality bar

- What you work on is stated in plain sentences above the fold, with a working email address on the same screen.
- Every publication has a resolvable link, and every hosted file is labelled with which version it is.
- Every working paper status carries a date, and nothing is listed as available that is not.
- Whether you are taking students is stated explicitly.
- The CV matches the site, and both were updated in the same session.
- The site is static, has no build step, and all content is present with scripting disabled.
- Headings are in order, images have real alternative text, and the page works at 320 pixels wide and by keyboard.
- A maintenance checklist exists in the repository with two fixed dates in the year.

## Adapting this to your context

The defaults come from a quantitative social science page: journal articles first, DOIs everywhere, preprints normal, a job market on a calendar.

- **The three readers.** A search committee, a referee, a prospective student. If your field hires mostly into industry or government, replace a reader and rebuild the above-the-fold block for whoever takes their place.
- **The publication grouping.** Journal articles first. Book-first and proceedings-first fields regroup as the edge case above describes, and where author order carries meaning, state the convention in one line.
- **Identifiers and profiles.** ORCID plus a general scholar profile. Add the ones your field reads: arXiv, SSRN, RePEc, dblp, PhilPapers, PubMed, or an institutional repository handle.
- **Preprint norms.** Posting a working paper is standard in economics and physics and contested in parts of medicine and the humanities. Check the venue's policy before hosting anything, and keep the version label either way.
- **The maintenance rhythm.** Twice a year plus triggers, sized for about twenty entries kept by one person. A fast-publishing field or a group site needs quarterly and a named owner.
- **What not to change.** Plain sentences and a working email address above the fold, a dated status on every unpublished item, a resolvable link on every entry, static files with no build step.

## Related skills

`research-paper-website` builds the project pages this site links to, and inherits the same static, accessible, no-build standard. `references-and-bibliography` cleans the citation list before it reaches this page, including author ordering and BibTeX consistency. `academic-figures-monochrome` supplies any figure shown here, so the site matches the papers. `interactive-results-explorer` is what to link when a paper has an explorable dataset. `journal-targeting` and `abstract-and-title` shape the sentences the publications section reuses. `weekly-review-and-planning` is where the twice-yearly maintenance dates belong so they actually happen.
