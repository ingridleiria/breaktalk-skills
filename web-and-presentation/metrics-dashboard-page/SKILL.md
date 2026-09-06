---
name: metrics-dashboard-page
description: Builds a metrics page a team will actually use: five to nine measures chosen because a named decision depends on each one, every metric carrying a written definition visible from the page, a named owner, a source and refresh time, a comparison against target and against the same period last year, a trend shown beside the level, volume shown beside every rate, annotations for launches and definition changes, and an explicit list of what the page deliberately does not show. Static files generated from a data file, no build step, readable with scripting disabled, and charts that follow the house monochrome-first standard rather than a colour rainbow. Use this skill for a metrics page, a team or company dashboard, a weekly numbers page, an investor or board metrics view, or when a leader asks for one place to see how things are going.
---

# Metrics Dashboard Page

Most dashboards fail the same way. They show everything that can be measured, nobody can say what any single number should trigger, and within a month people stop opening them because they have never once learned something they then acted on. The chart count grows, the understanding does not, and the page becomes a thing that is maintained rather than used.

Two costs follow. The first is that decisions get made on anecdote anyway, while the page sits there giving the impression that the organisation is data-led. The second is worse and quieter: definitions drift. A source system changes how it counts an event, nobody annotates it, and the page reports confidently through the change. A step in a line becomes a story about a successful initiative, and the story survives longer than the number that produced it.

The fix is not design. It is deciding, before building anything, which decisions this page supports, and cutting everything that supports none of them.

## When to use this, and when not to

Use it for a recurring conversation with a known cadence: a weekly leadership meeting, a monthly business review, a quarterly board update, a team's own operating page. Use it when someone asks for one place to see how things are going, which is a request that should always be answered with a question about which decisions.

Do not use it for research results where the reader's job is to explore rather than to act, which is `interactive-results-explorer` and has entirely different rules about uncertainty and subgroups. Do not use it for a paper's companion page, which is `research-paper-website`. Do not use it to build the narrative document that goes to a board or an investor, which is `board-deck` and `investor-update`; this page supplies numbers to those and does not replace them. Do not use it as the model that produces the forecast, which is `revenue-forecast` and `financial-model-builder`. Do not use it to set the goals themselves, which is `okr-planning`; a dashboard that quietly becomes the goal-setting instrument produces goals chosen for being measurable.

## What you need before starting

**The decisions or conversations this page feeds, and how often they happen.** A weekly leadership meeting, a monthly review and a board update need different pages, and one page serving all three serves none. Missing: ask what happens in the meeting this page is for, and if there is no meeting, ask who reads it alone and what they do next.

**For each candidate metric, what happens when it is bad.** Missing, and the honest answer is nothing: that number is context rather than a metric, and it goes lower on the page or off it.

**A written definition for each metric.** Precise enough that two people computing it independently get the same answer. Missing: write it, then have someone else compute the metric from your definition alone and compare. Most arguments about a dashboard are arguments about a definition.

**An owner for each metric, one named person.** Accountable for the number and for explaining it, not for the chart. Missing: the metric has no advocate and no one to notice when it breaks. Assign or remove.

**The source, and how often it refreshes.** Missing: the page cannot state when it was last updated, which makes every number on it unverifiable.

**Enough history for the comparison you intend.** Thirteen periods to show a year-on-year comparison on a monthly page, fifty-three weeks on a weekly one. Missing: show the trend against the prior period only, and say on the page that year-on-year is not yet available rather than showing a comparison built on four points.

**The denominator behind every rate.** Missing: recover it. A conversion rate without its volume is uninterpretable and invites confident conclusions from twelve observations.

**Targets and thresholds, and who set them.** Missing: show the metric without a target rather than inventing one, and note that no target is set, which is usually a finding in itself.

## The method

1. **Name the decisions, then cap the measures.** Five to nine for a leadership page. Write the decision beside each candidate metric in one line. Anything with no decision beside it comes off. When someone asks to add a tenth, the question is which of the nine it replaces, and that question should be in the page's own documentation so it is not a personal negotiation each time.

2. **Write the definitions before building anything.** Include the population, the time basis, the exclusions and the treatment of edge cases, because those are what differ between two people's versions.

```
Metric:       Weekly activated accounts
Definition:   Accounts that completed the setup flow and performed at least one
              qualifying action within 7 days of signup. Counted in the week of
              signup, not the week of activation.
Excludes:     Internal accounts, trial accounts converted from a prior account,
              accounts on the legacy plan.
Source:       product_events table, activation_v3 view
Owner:        Head of Product
Refresh:      Daily 06:00, from the previous complete day
Target:       38 percent of signups, set at the January planning round
```

3. **Choose the comparison for each metric deliberately.** A bare number means nothing. The default is three comparisons: against target, against the previous period, and against the same period last year wherever seasonality exists. The rule for when year-on-year is required: if the business has any weekly, monthly or annual cycle at all, which is nearly all of them, then the prior-period comparison alone will mislead in one direction or the other for most of the year.

4. **Show the trend beside the level, always.** A number that is good and falling and a number that is bad and rising need opposite responses, and the level alone hides which you have. A sparkline of the last thirteen periods beside the figure is enough.

5. **Order by what matters, and group by question.** The two or three metrics that decide the conversation go at the top, at a size that reads across a room. Group the rest by the question they answer, not by the system the data came from; readers think in questions and never in data sources.

6. **Show volume beside every rate, and put the definition within reach.** A conversion rate of 40 percent on ten observations belongs on the page differently from one on ten thousand. The definition belongs in a `details` element on the tile, which opens without scripting and keeps the page uncluttered.

```html
<article class="metric">
  <h3 id="m-activation">Weekly activated accounts</h3>
  <p class="level"><strong>34.1%</strong>
     <span class="volume">of 1,284 signups</span></p>
  <p class="compare">
    <span>Target 38.0%</span> |
    <span>Prior week 33.4%</span> |
    <span>Same week last year 29.8%</span>
  </p>
  <img src="charts/activation.svg" alt="Activation rate by week for 53 weeks.
       Rises from 29.8 percent a year ago to 34.1 percent now, with a step down
       of about 4 points in week 31 marked as a definition change.">
  <details>
    <summary>Definition, owner and source</summary>
    <p>Accounts completing setup and one qualifying action within 7 days of
       signup, counted in the week of signup. Excludes internal and trial
       accounts. Owner: Head of Product. Source: activation_v3.
       Refreshed 2026-09-05 06:04.</p>
  </details>
</article>
```

7. **Generate the page from a data file rather than querying live.** Most numbers refresh on a schedule, not continuously. A page regenerated when the file updates is faster, simpler, survives without maintenance far longer, and can be archived as it stood on any date. Where it genuinely must be live, keep the query layer thin, show the query time, and keep a static fallback.

8. **Make staleness impossible to miss.** Print the refresh time on the page, and mark the page when the data is older than the expected interval. A stale dashboard that nobody knows is stale is worse than no dashboard.

```js
// The only scripting on the page. Everything else is in the markup.
var refreshed = new Date(document.body.dataset.refreshed);
var expected  = Number(document.body.dataset.expectedHours) || 24;
var ageHours  = (Date.now() - refreshed) / 3.6e6;
if (ageHours > expected * 1.5) {
  var warn = document.createElement('p');
  warn.className = 'stale';
  warn.textContent = 'These figures were last refreshed ' +
    Math.round(ageHours) + ' hours ago, against an expected ' + expected +
    ' hours. Treat them as out of date.';
  document.body.prepend(warn);
}
```

9. **Draw the charts to the house standard.** Monochrome first, series separated by marker shape, dash pattern and fill texture rather than by colour, legend outside the plot area, and the two accents, a dark navy and a dark wine red, used sparingly and consistently. Targets are drawn as a line, not as a background colour. Thresholds, where used, are defined on the page, since a colour with no stated rule is an opinion rendered as a fact.

```css
:root { --ink:#16181d; --paper:#fbfaf8; --rule:#d8d4cd;
        --navy:#1b2a4a; --wine:#6e1f2b; }
.series-actual  { stroke:var(--ink); fill:none; }
.series-prior   { stroke:var(--ink); fill:none; stroke-dasharray:6 3; opacity:0.7; }
.line-target    { stroke:var(--navy); stroke-dasharray:2 3; }
.band-breach    { fill:url(#hatch); }        /* texture, not a red block */
.annotation     { stroke:var(--wine); }      /* the only routine use of wine */
.legend         { position:static; margin-top:0.5rem; }  /* outside the plot */
/* Never encode meaning in colour alone: every state also has a shape,
   a pattern or a label. */
```

10. **Annotate the page from an events file.** A launch, a price change, an outage, a definition change. A metric that stepped in March with a note saying why is a page people trust; a definition change with no annotation is how a dashboard silently starts lying.

```json
[
  {"date":"2026-07-29","metric":"activation","kind":"definition",
   "note":"activation_v3: qualifying action narrowed to exclude imports"},
  {"date":"2026-08-14","metric":"signups","kind":"event",
   "note":"Pricing page rebuild shipped"}
]
```

11. **State what the page does not show.** A short, explicit list at the bottom: the measures considered and left off, and why. This prevents the slow accumulation that kills every dashboard, and it gives an honest answer to the person who asks why their number is not there.

12. **Make the numbers checkable and the page readable without scripting.** The underlying rows are downloadable, because someone will need to verify a figure and asking them to trust it is how the page loses its authority. Every chart has a table equivalent in the markup. The page works at 320 pixels wide, since the person who most needs it will look at it in a taxi.

13. **Review it quarterly, against two questions.** Has anyone acted on this metric since the last review, and does its definition still match the system. Anything unacted-on comes off. Systems change silently and dashboards report confidently through it, so the definition audit is the half of the review that finds the real problems.

## Worked example

**Situation.** A sixty-person software company had a dashboard with thirty-one charts across four tabs, built over two years by three different people. The weekly leadership meeting opened with twenty minutes of screen-sharing it. Nobody could say what any chart should trigger, two of them had been broken since a warehouse migration in March, and the chief executive had started asking for numbers by direct message instead.

**Task.** One page for the weekly leadership meeting, in two weeks, that would shorten the numbers section rather than lengthen it, and that would still be in use six months later.

**Action.** The first pass tried to keep the thirty-one and organise them better: three tiers, a summary view and a drill-down. It was abandoned after the first review. The reorganised version was easier to look at and no easier to act on, because the problem was never layout. The test that killed it was asking, for each chart, what decision it fed. Nineteen had no answer at all. Four had the same answer as another chart. Two were broken. That left six, and the seventh was added later.

The seven were: weekly new revenue, net revenue retention, activated accounts, support first-response time, open critical defects, cash runway, and voluntary attrition. Each got a decision written beside it. Activation's read: if it falls below 30 percent for three consecutive weeks, product stops new feature work and spends a cycle on onboarding.

Definitions were written next and took longer than the build. Two of the seven turned out to be genuinely contested. Net revenue retention had two versions in circulation, one including and one excluding accounts that downgraded and later re-expanded, differing by 6 percentage points, and both had appeared in board materials in the same quarter. Fixing that required a decision by the finance lead, recorded in the definition and annotated on the chart from the date it applied.

Thresholds were the second wrong turn, smaller but instructive. The first build used red, amber and green backgrounds on each tile because it read well. The rule behind the colours had never been written down, so the amber boundary was effectively the opinion of whoever built the tile, and two of the seven tiles were amber for reasons nobody could reconstruct. The colours came out. Targets were drawn as a dashed navy line on the chart, breaches were shown as a hatched band with a label, and the rule was printed on the page. That change also fixed the accessibility problem nobody had raised: two people in the leadership team could not reliably distinguish the red and green tiles.

The definition audit found the thing worth finding. Activation had stepped up 4 points in week 31 of the previous year and the step had been attributed at the time to an onboarding redesign, which had been described as a success in two board decks. The event file showed a definition change in the same week, narrowing the qualifying action. Recomputing on the old definition showed the redesign had moved activation by roughly a point, not four. That correction was uncomfortable and it was the single most valuable output of the exercise.

**Result.** One page, seven metrics, 214 kilobytes including thirteen charts as inline SVG, generated from a nightly file. The numbers section of the weekly meeting went from about twenty minutes to about seven, measured over the following six weeks, and the time went into the two metrics that were off target rather than into the twenty-nine that were not.

At the first quarterly review, two metrics came off: open critical defects, which had not been acted on in a quarter because the engineering team tracked it more precisely elsewhere, and voluntary attrition, which at this size moved by whole percentage points when one person left and was better read quarterly than weekly. One was added, sales cycle length, with a decision beside it. The page stayed at seven.

### A second scenario, where it goes differently

The same company's quarterly board metrics view, built six months later.

The reader changes and so does the design. Board members see the numbers four times a year, remember the previous version imperfectly, and will ask about a figure they recall from two quarters ago. So stability outranks currency: the metric set is frozen for the year, the definitions are printed in full rather than tucked into an expandable element, and every definition change is annotated on the chart permanently rather than for a quarter.

The comparisons change too. Against plan rather than against a rolling target, with the plan's own vintage stated, since a comparison against a plan that was revised in June is a different claim from one against the plan set in January. Cohort views replace week-on-week movement, because a quarterly reader cannot use weekly noise.

The refresh model relaxes: quarterly data means a page generated once per quarter and archived exactly as it stood, so the version a board member read in March can be reopened in September. The staleness warning is unnecessary and would be misread; the page instead carries the reporting period prominently in the heading.

What does not change: a small number of measures, a decision behind each one, a definition and an owner, volume beside every rate, targets as lines rather than colours, and the list of what the page does not show.

## Output

```
dashboard/
  index.html          one page, CSS inline, tables present in the markup
  data/
    metrics.json      one record per metric per period, with volume
    events.json       annotations: launches, incidents, definition changes
    definitions.md    the full written definition of every metric
  charts/             generated SVG, one per metric
  rows/latest.csv     the underlying rows, downloadable
  README.md           how the page is regenerated, and by whom
```

Each metric tile carries the same fields, in the same order.

```
[Metric name]
[Level]  [volume or denominator]
Target [x] | Prior period [y] | Same period last year [z]
[Sparkline or chart, 13 or 53 periods, with annotations]
Definition | Owner | Source | Last refreshed [timestamp]
```

And the page carries these parts in this order.

| Order | Part | Requirement |
| --- | --- | --- |
| 1 | Heading and period | What page this is, which period, refresh time |
| 2 | Top two or three metrics | Large, readable across a room |
| 3 | Remaining metrics | Grouped by question, never by source system |
| 4 | Annotations key | What the marks on the charts mean |
| 5 | What this page does not show | Measures considered and left off, with reasons |
| 6 | Data download and definitions | The rows, and the full definitions document |

## Failure modes

**A metric with no decision behind it.** Recognise it by asking what happens when the number is bad and getting no answer. It is context, and it belongs lower or off.

**Colour carrying the rule.** Recognise it when a tile is amber and nobody can state the boundary. Fix by writing the rule on the page and encoding state in shape, pattern and label as well as colour.

**Bare numbers.** Recognise it when a figure appears with no target, no prior period and no trend. A number alone cannot be read, so readers supply their own baseline, usually the last one they happen to remember.

**Rates without volume.** Recognise it when a percentage moves several points a week. Print the denominator beside every rate.

**Silent staleness.** Recognise it by checking the refresh time against the expected interval; if the page does not print one, that is the finding.

**Definition drift.** Recognise it by a step change with no annotation on the same date. Audit definitions against the source quarterly, and annotate every change permanently.

**Growth by accretion.** Recognise it when the page has more measures this quarter than last with no removals. Adding one means removing one, and the rule belongs in the page's documentation.

**A live query the page cannot survive.** Recognise it when the warehouse is slow and the page is blank. Generate from a file, and where live is required, keep the last good file as a fallback and label it.

**Numbers that cannot be checked.** Recognise it when someone questions a figure and the answer is that the query is complicated. Publish the rows.

## Edge cases

**A metric that cannot be defined precisely.** Where the true measure is unavailable, show the proxy, name it as a proxy in the tile, and state what it systematically misses. A labelled proxy is useful; an unlabelled one is a false claim.

**Very small volumes.** Where a rate moves by whole points on one event, show the count rather than the rate, or move the metric to a longer period. Weekly attrition in a team of sixty is noise presented as a trend.

**A partial current period.** Show it, mark it as incomplete, and either exclude it from the trend line or draw it in a distinguishable pattern. A part-month sitting at the end of a chart of complete months is read as a collapse.

**Data that arrives late.** Where a source reports on a lag, state the lag beside the metric and date the last complete period. Otherwise every reader assumes the most recent point is current.

**A metric nobody owns.** Do not publish it. An unowned number has no one to explain a movement and no one to notice a break, and it will be the one that is wrong.

**Confidential measures.** Where cash runway or individual performance data cannot go to everyone, split the page rather than the number: a general page and a restricted one, each complete for its audience. A page with a redacted tile invites worse speculation than its absence.

**During an incident.** An operating page is not an incident page. Incidents need a different cadence and a different audience; keep the dashboard on its schedule and let `crisis-and-incident-comms` handle the live communication.

**A brand new company or product with no history.** Show the level and the trend with the periods you have, state the number of periods, and do not draw a year-on-year comparison from four points. Say when it will become available.

## Quality bar

- Every metric is on the page because a named decision depends on it, and that decision is written down.
- Five to nine measures, and adding one means removing one.
- Every metric has a written definition reachable from the page, a named owner, a source, and a refresh time.
- No bare numbers: every figure carries a comparison and a trend, and every rate carries its volume.
- Targets and thresholds are stated as rules and drawn as lines, never implied by colour alone.
- Definition changes and material events are annotated on the charts, with dates.
- What the page deliberately excludes is listed, with reasons.
- The underlying rows are downloadable, the page works at 320 pixels wide, and every chart has a table equivalent in the markup.

## Related skills

`interactive-results-explorer` is the research equivalent and shares the figure standard, but its rules about uncertainty and subgroup suppression do not apply here, and this page's rules about owners and refresh do not apply there. `research-paper-website` shares the static, accessible, no-build discipline. `board-deck` and `investor-update` consume the numbers this page produces and add the narrative. `revenue-forecast` and `financial-model-builder` produce the forward-looking figures a dashboard should report rather than recompute. `okr-planning` sets the targets the page compares against. `operating-cadence-design` decides which meeting this page serves, which is the question that determines everything else about it.
