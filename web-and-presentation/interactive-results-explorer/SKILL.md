---
name: interactive-results-explorer
description: Builds a page where readers can explore results themselves rather than only read the author's chosen cut, without turning the page into a specification-searching machine. Ships the underlying rows with the page, shows uncertainty and the sample count on every estimate, suppresses cells below a stated threshold, keeps axes stable across selections, puts a table view behind every chart, allows download of the exact filtered data, keeps the state in the URL, and carries a dated method note on the page itself. Static files, no build step, readable with scripting disabled. Use this skill for a results explorer, an interactive appendix, a data-driven page for a paper or a report, a subgroup viewer, or when someone asks for a dashboard of findings other people will use.
---

# Interactive Results Explorer

Interactivity is worth building when a reader has a legitimate question the author cannot anticipate: their own country, their own sector, their own cohort, their own year. It is not worth building to make a static finding look sophisticated, and it is actively dangerous when it lets a reader wander through subgroups with no indication of how thin the cells are. A page that allows twelve filters over a dataset of four thousand rows is a specification-searching machine pointed at the author's own results, published under the author's own name, and operated by people who have no training in why the eighth subgroup they looked at is significant.

The failure is concrete and it has a shape. A reader slices to a small cell, sees an effect three times the headline, and repeats it. The author cannot correct it, because the page did show that number. The paper's careful language about the analysis being powered for main effects only sits in a PDF nobody in the chain has opened. The cost is a wrong number circulating with the study's authority attached, and the author's only defence is a page they built themselves.

Everything in this skill exists to let a reader ask their own question while making the answer's reliability impossible to miss.

## When to use this, and when not to

Use it when readers have a legitimate, unanticipatable question about which cut applies to them, when the number of reasonable views runs into the dozens or hundreds, when the estimates are stable enough at the level being shown to survive being read alone, and when the underlying rows can be published or aggregated to the level displayed.

Do not use it when five static figures would answer every reasonable question, which is more often than it appears; produce the five figures and stop. Do not use it when the honest answer is that the reader should look at one number, in which case show that number large and explain it. Do not use it for the paper's companion page, which is `research-paper-website` and should link to an explorer rather than becoming one. Do not use it for an operating metrics page for a team, which is `metrics-dashboard-page` and has different rules about ownership and refresh. Do not use it as a replacement for the replication package, which is `replication-package`; an explorer shows displayed cells, not the analysis path.

## What you need before starting

**The reader's question, in one sentence.** "Which sectors saw the largest fall, in my region" is a question a page can be built around. "Let people explore the data" is not, and pages built from it grow controls until nobody can use them. Missing: write the three questions the page is for and cut every control that serves none of them.

**The rows or cells behind every view, at the granularity you intend to display.** Missing: publish the aggregated cells the page actually shows, which is the same information the page is displaying anyway.

**An uncertainty measure for every estimate.** A confidence interval, a standard error, or a stated reason why one cannot be produced. Missing: do not build the explorer. A filterable page of point estimates with no uncertainty is the single most misleading artefact this track can produce.

**The sample count behind every cell.** Missing: it can usually be recovered from the analysis code, and it is worth the hour, because the count is what turns a suppression rule from arbitrary into defensible.

**A suppression threshold, and who set it.** Missing: default to suppressing cells with fewer than fifty observations, greying them rather than hiding them, and state on the page that the threshold is a default rather than a disclosure requirement.

**What the analysis does and does not support.** Which cuts were preregistered or powered, which are exploratory. Missing: treat everything beyond the main specification as exploratory and label it so on the page, next to the control, not in a footnote.

**The version and date of the data.** Missing: use the file's modification date, say that is what you have done, and fix it before publication, because someone will cite a number from this page and need to say which version produced it.

## The method

1. **Justify the interactivity before building it, in writing.** Count the views a reader would reasonably want. Under about five, build static figures. Between five and about twenty, consider small multiples, which show everything at once and cannot be misread as a search. Above that, an explorer earns its place. Record the decision in the method note, because the next person to ask for more controls needs to see the reasoning.

2. **Fix the default view.** It answers the main question, so a reader who touches nothing still leaves with the finding. Every control starts from there, and reset returns to it.

3. **Build the data file first, and make it the deliverable.** One row per displayed cell, plain CSV or JSON, human-readable, with the count and the interval alongside the estimate. Suppression is applied when the file is written, not in the browser, so a reader downloading the file cannot recover cells the page declines to show.

```csv
region,sector,period,estimate,ci_low,ci_high,n,suppressed
North,Manufacturing,2019-2024,-4.2,-6.1,-2.3,1840,0
North,Hospitality,2019-2024,-9.7,-14.8,-4.6,312,0
North,Mining,2019-2024,,,,41,1
```

4. **Write the no-script baseline before writing any JavaScript.** The page must carry, in markup: the headline finding, the method note, and a full table of the default view. That is what an archive keeps, what a screen reader reaches first, and what a reader on a failed network still gets. Controls come afterwards and enhance what is already there.

```html
<h1>Employment change by sector and region, 2019 to 2024</h1>
<p class="finding">Employment fell in every region, and the fall in hospitality
   was between two and three times the fall in manufacturing everywhere except
   the South East.</p>

<noscript>
  <p><strong>The interactive view needs scripting.</strong> The full table below
     shows all cells, and the complete dataset is available as
     <a href="data/estimates.csv">estimates.csv</a>.</p>
</noscript>

<table id="cells">
  <caption>Percentage change in employment, 2019 to 2024, with 95 percent
    intervals. Cells with fewer than 50 observations are suppressed.</caption>
  <thead>
    <tr><th scope="col">Region</th><th scope="col">Sector</th>
        <th scope="col">Change</th><th scope="col">95% interval</th>
        <th scope="col">Observations</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">North</th><td>Manufacturing</td><td>-4.2</td>
        <td>-6.1 to -2.3</td><td>1,840</td></tr>
    <tr><th scope="row">North</th><td>Mining</td><td>Suppressed</td>
        <td>Suppressed</td><td>41</td></tr>
  </tbody>
</table>
```

5. **Add controls sparingly, labelled in the reader's language.** Variable names belong in the data file, not on screen. Every control has a visible label, a visible reset, and works with the keyboard. Nothing important is behind hover, which does not exist on a phone. Cap the number of simultaneously active dimensions: two is usually right, three is the point at which cell sizes collapse, and if a third is genuinely needed, it should be a separate page with its own justification.

6. **Put the state in the URL, and read it on load.** This single feature is most of what makes a results page get shared, cited and checked. It also gives you a free bug report channel, since a reader can send the exact view that looks wrong.

```js
// State lives in the query string so a view can be linked, cited and reloaded.
function readState() {
  var p = new URLSearchParams(location.search);
  return { region: p.get('region') || 'All', sector: p.get('sector') || 'All' };
}
function writeState(s) {
  var p = new URLSearchParams(s);
  history.replaceState(null, '', location.pathname + '?' + p.toString());
}
function render(s) {
  var rows = ALL_ROWS.filter(function (r) {
    return (s.region === 'All' || r.region === s.region) &&
           (s.sector === 'All' || r.sector === s.sector);
  });
  drawChart(rows);       // fixed axes, see below
  fillTable(rows);       // the same rows, as a real table
  updateDownload(rows);  // the exact filtered view
}
```

7. **Draw the chart with axes that do not move.** Compute the domain once, across the entire dataset, and reuse it for every selection. Axes that rescale silently make every selection look equally dramatic, which is the commonest way an interactive chart misleads with nobody intending it. Where rescaling is genuinely needed, announce it in the chart's own subtitle for that view.

```js
// Fixed across every selection, computed once from the full dataset.
var Y_DOMAIN = [-20, 5];
// Never truncate a value axis on bars. On a bar chart the domain includes zero.
var Y_DOMAIN_BARS = [Math.min(0, dataMin), Math.max(0, dataMax)];
```

8. **Follow the house figure standard so the explorer looks like the paper.** Monochrome first, series separated by marker shape, dash pattern and fill texture rather than by colour, legend outside the plot area, and the two accents, a dark navy and a dark wine red, used sparingly and always meaning the same thing across every view. A series that is dashed in one selection and solid in another is a defect, not a style choice.

```css
:root { --ink:#16181d; --rule:#d8d4cd; --navy:#1b2a4a; --wine:#6e1f2b; }
.series-a { stroke: var(--ink);  stroke-dasharray: none;  }
.series-b { stroke: var(--ink);  stroke-dasharray: 6 3;   }
.series-c { stroke: var(--ink);  stroke-dasharray: 1 4; stroke-linecap: round; }
.marker-a { fill: var(--ink); }                       /* circle  */
.marker-b { fill: none; stroke: var(--ink); }         /* hollow square */
.highlight { stroke: var(--wine); stroke-width: 2.5; } /* one series at a time */
.suppressed { fill: url(#hatch); }                     /* texture, not colour */
.legend { position: static; }                          /* outside the plot area */
```

9. **Render uncertainty and count on every estimate, not only the headline.** Intervals drawn on the chart, count printed in the table row and in any tooltip. A tooltip that gives a point estimate without its interval is a machine for producing overconfident readers.

10. **Make the empty and suppressed states explicit.** "No observations for this selection" as visible text, and suppressed cells drawn with a hatch texture and labelled, never left blank. A blank chart reads as zero, which is a specific false claim rather than a missing one.

11. **Offer two downloads.** The complete dataset, and the exact rows currently displayed. The second is what lets a reader check what they are seeing and is the cheapest credibility the page can buy.

```js
function updateDownload(rows) {
  var csv = ['region,sector,period,estimate,ci_low,ci_high,n']
    .concat(rows.map(function (r) {
      return [r.region, r.sector, r.period, r.estimate,
              r.ci_low, r.ci_high, r.n].join(',');
    })).join('\n');
  var link = document.getElementById('download-view');
  link.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }));
  link.download = 'view.csv';
  link.textContent = 'Download these ' + rows.length + ' rows';
}
```

12. **Write the method note on the page, not behind a link.** What the data is and where it came from, the period, what one row represents, how the estimates were produced, what the uncertainty means, the suppression threshold, and what the page does not support conclusions about. Version and date it, and put the version in the download filename. Where an archived copy of the data exists, cite it by its identifier and link `replication-package` for the deposit, licence and identifier decisions rather than restating them on the page.

13. **Test before publishing, in five ways.** With the data file replaced by one five times larger, because the version that runs on your machine with the small file is not the one your readers get. With scripting disabled, where the finding, the note and the default table must remain. At 320 pixels wide, where the table scrolls inside its own container rather than pushing the page sideways. With the keyboard alone. And by picking the three thinnest cells the controls allow and asking whether a reader would be misled by what they show.

## Worked example

**Situation.** A research group published estimates of employment change across 11 regions, 9 sectors and 6 years, from a survey with about 46,000 observations in total. The paper reported region-level and sector-level effects. A policy team asked for a page where their own region and sector could be looked up, and the group agreed because the request was repeated by four different organisations in a fortnight.

**Task.** A page that answered the lookup question, shipped in a week, that would not produce a wrong number in a newsletter.

**Action.** The justification was written first. Reasonable views numbered 11 times 9, roughly a hundred, which is well past the point where static figures serve, so the explorer earned its place. That count also set the shape: two displayed dimensions, region and sector, with the six years collapsed into the single 2019 to 2024 change the paper reports rather than becoming a third filter.

The first build ignored the second half of that decision. It offered region, sector, year and age band as four independent filters, because the analysis file had age in it and adding a control took ten minutes. It was tested by giving it to a colleague with the instruction to find something surprising, and they did so in ninety seconds: hospitality, one region, workers under twenty five, 2021, an estimated fall of 31 percent, from 23 observations. The point estimate was real, in the sense that the arithmetic was right, and it was meaningless. That build was abandoned. The age control came out, the years were collapsed into one change per cell, and the two remaining dimensions left 11 times 9, or 99 displayed cells, over about 46,000 observations. That is an average of roughly 465 observations a cell.

Suppression was then set at fifty observations, chosen because the survey's own documentation used it, which made the threshold defensible rather than invented. Suppressed cells were drawn with a hatch and labelled "suppressed, fewer than 50 observations" rather than left blank, and the same rule was applied when the CSV was written, so the file could not be used to recover them. Two of the 99 cells fell below it, mining in the two smallest regions, at 41 and 44 observations. Of the 97 that remained, the thinnest carried 112, which is the number quoted below.

Two further problems appeared in testing. The chart's vertical axis had been computed from the visible selection, so filtering to a single small sector produced a chart where a fall of 2 percent filled the frame and looked identical to a fall of 18 percent elsewhere. Fixing the domain to the full data range, from -20 to +5, cost nothing and removed the problem entirely. And the tooltip showed only the point estimate, because that is what tooltips usually show; it was rewritten to show the estimate, the interval and the count on three lines, and the count line is the one readers mentioned afterwards.

The no-script baseline was built last and took forty minutes: the headline sentence, the method note and the full 99-row table of displayed cells in the markup. Total page weight was 118 kilobytes including the data file, with no external requests.

**Result.** Published in six days. Over the first quarter it was used by three of the four organisations who had asked, and one of them found and reported a genuine defect: two sector labels had been transposed in the data file, which they spotted because they knew their own sector's number. They sent a URL, which located the view exactly, and the fix took twenty minutes and produced a version 1.1 with a dated note.

No small-cell number reached publication, which is the outcome the page was built for and is impossible to prove; what can be said is that the smallest cell the page could display carried 112 observations and its interval spanned nine percentage points, which is visible to anyone who looks.

### A second scenario, where it goes differently

The same group, a second study, this time an experiment with two arms, one preregistered primary outcome and four secondary outcomes.

The count of reasonable views is six. An explorer is the wrong instrument, and building one would invite exactly the subgroup wandering the preregistration exists to prevent. What was built instead: six static figures as small multiples on one page, all sharing an axis, plus the estimates table and the full dataset for download. Total build time was under a day and the page cannot be misused, because there is nothing to operate.

One interactive element survived, and it is worth naming as the exception. A single toggle switching all six panels between the intention-to-treat and per-protocol specifications, with a sentence explaining the difference and which one the paper reports. That is not a filter over subgroups; it is a comparison the authors want the reader to make, both views are preregistered, and it changes every panel at once so nothing can be cherry-picked. The rule it illustrates: interaction that shows the reader a comparison the authors chose is safe, interaction that lets the reader search for a result is not.

## Output

```
explorer/
  index.html          one page, CSS inline, default table in the markup
  data/
    estimates.csv     one row per displayed cell, with n and interval, suppression applied
    codebook.md       what one row means, every column, units, provenance
  README.md           version, date, how the file was produced
```

The page carries these parts in this order.

| Order | Part | Requirement |
| --- | --- | --- |
| 1 | Headline finding | One sentence, in the markup, present without scripting |
| 2 | Default view | Answers the main question before any control is touched |
| 3 | Controls | Few, labelled in reader language, with a visible reset |
| 4 | Chart | Fixed axes, house figure standard, uncertainty drawn, legend outside |
| 5 | Table view | The same rows as a real table, one click away, always present |
| 6 | Downloads | Full dataset, and the exact filtered rows |
| 7 | Method note | On the page: source, period, unit, estimation, uncertainty, threshold, limits |
| 8 | Version and date | Visible, and repeated in the download filename |

## Failure modes

**Interactivity that was never justified.** Recognise it when the controls produce views nobody asked for and the default is the only one anyone uses. Fix by counting the reasonable views and replacing the page with static figures if the count is small.

**Silent axis rescaling.** Recognise it by selecting the smallest subgroup and seeing a chart that looks as dramatic as the largest. Fix by computing the domain once from the full dataset.

**Point estimates without intervals.** Recognise it in the tooltip, which is where this failure usually hides. Every place a number appears, its interval and count appear with it.

**A third and fourth filter added because the column exists.** Recognise it when the minimum cell size drops below the suppression threshold for a large share of combinations. Fix by removing dimensions until the thin cells are rare, not by suppressing more.

**Suppression applied in the browser only.** Recognise it by opening the data file and finding the suppressed values. Apply suppression when writing the file.

**A blank chart for an empty selection.** Recognise it by selecting an impossible combination. A blank frame reads as zero. Fix with explicit text.

**Content assembled entirely by script.** Recognise it by disabling scripting and finding an empty page. The finding, the note and the default table live in the markup.

**A build pipeline.** Recognise it by a `node_modules` folder in the deliverable. In three years the build will not run and the page will be gone. One HTML file, one data file, one charting library at a pinned version if any.

**The page that outlives its data.** Recognise it when the method note has no date and the file has no version. Someone will cite a number from it and be unable to say which version produced it.

## Edge cases

**Data that cannot be published at row level.** Publish the displayed cells with counts and intervals, which is what the page shows anyway, and say in the method note why the microdata is not available and how a researcher could apply for it. Keep that to one line and a link: the reasoning about licences, restricted-access routes, where the archived copy lives and which identifier cites it belongs to `replication-package`, and repeating it here produces two statements that will disagree within a year.

**A dataset too large to ship with the page.** Above roughly ten megabytes, precompute the cells rather than shipping the rows, which is almost always possible because the page displays aggregates. Where a live query layer is genuinely required, show the query time on the page and keep the static fallback table.

**Estimates that are not comparable across the filter.** Where a change in definition, coverage or instrument means two selections cannot be placed on one axis, break the series visibly and annotate the break rather than drawing a continuous line across it.

**A hostile or adversarial audience.** Where the results are contested, ship the full dataset, the codebook and the estimation code, and expect the page to be used against the study. That is the correct use of it, and a page that cannot survive it should not have been published.

**One reader, one recurring question.** Where an explorer is being built because a single team asks the same question monthly, send them the data file and a short script instead. A page built for one reader is maintenance without an audience.

**Longitudinal data with revisions.** Keep every published version of the data file, name it with its version, and let the page state which version it is showing. Silent revision of a number a reader cited is the fastest way to lose them.

## Quality bar

- The decision to build an explorer rather than static figures is written down, with the count of reasonable views.
- The finding, the method note and the default table are present with scripting disabled.
- Every estimate carries its interval and its sample count, everywhere it appears.
- The suppression threshold is stated on the page, applied when the data file is written, and shown as texture rather than as a blank.
- Axes are fixed across selections, and any rescaling is announced in the view itself.
- Every chart has a table view, and the exact filtered rows are downloadable.
- The state is in the URL and a shared link reproduces the view.
- The page is static, has no build step, and works at 320 pixels wide and by keyboard alone.
- The page carries a version and a date, and the version appears in the download filename.

## Adapting this to your context

The thresholds come from a public survey with a published disclosure rule and frequentist estimates. Both are field choices, and the suppression number is usually not yours to set.

- **The suppression threshold.** Fifty observations, from one survey's documentation. Health and administrative data are often bound to five or ten by a rule you do not choose, and official statistics may require rounding instead. Take the number from the provider.
- **The uncertainty measure.** A 95 percent confidence interval. Substitute a credible interval, a design-based standard error, or a cluster-robust one, and name which it is on the page.
- **The view counts.** Five and twenty, where static figures, small multiples and an explorer each win. They come from a two-dimension grid. Recount for yours.
- **Preregistration.** The file assumes some cuts are confirmatory. Name the registry if there is one: OSF, AsPredicted, PROSPERO, ClinicalTrials.gov, the AEA RCT Registry. Otherwise label every cut exploratory.
- **The tooling.** Plain HTML and one pinned charting library. R with Shiny, a Python app or an Observable notebook do the same job but need a server, and a page needing a server dies when the grant does.
- **What not to change.** Interval and sample count wherever a number appears, axes fixed across selections, suppression applied when the file is written rather than in the browser.

## Related skills

`research-paper-website` is the companion page for the paper and should link to this explorer rather than absorbing it. `academic-figures-monochrome` holds the figure standard the charts follow, so the page looks like the paper. `replication-package` holds the code and the analysis path, which this page deliberately does not show. `metrics-dashboard-page` is the operating equivalent for a team's own numbers, where ownership and refresh matter more than uncertainty. `descriptive-statistics-tables` and `regression-table-production` produce the cells this page displays.
