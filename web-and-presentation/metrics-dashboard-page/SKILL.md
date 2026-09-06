---
name: metrics-dashboard-page
description: Builds a metrics page a team will actually use: a small number of measures chosen because a decision depends on them, each with a written definition and an owner, comparison against a target and against the same period last year rather than a bare number, the trend shown alongside the level, the source and refresh time stated on the page, and an explicit list of what the page deliberately does not show. Use this skill for a metrics page, a team or company dashboard, a weekly numbers page, an investor or board metrics view, or when a leader asks for one place to see how things are going.
---

# Metrics Dashboard Page

Most dashboards fail in the same way. They show everything that can be measured, nobody can say what any of it should trigger, and after a month people stop opening them because they never learn anything. The number of charts grows and the amount of understanding does not.

The fix is not design. It is deciding, before building anything, which decisions this page supports and cutting everything that supports none of them.

## Decide what the page is for

Ask what decisions or conversations this page feeds, and how often. A weekly leadership meeting, a monthly business review, and a board update need different pages, and one page trying to serve all three serves none.

Then ask what happens when a number is bad. If the honest answer is nothing, that number is context rather than a metric, and it belongs lower on the page or not on it.

Cap it. Five to nine measures for a leadership page. If someone insists on more, ask which of the current ones it replaces.

## Every metric needs five things

**A definition in writing**, precise enough that two people computing it get the same answer, visible from the page rather than in a document nobody opens. Most arguments about a dashboard are actually arguments about a definition.

**An owner**, one named person who is accountable for the number and for explaining it, not for the chart.

**A source**, named, with when it last refreshed shown on the page. A stale dashboard nobody knows is stale is worse than no dashboard.

**A comparison.** A bare number means nothing. Show it against the target, against the previous period, and against the same period last year where seasonality exists. The comparison is what makes it readable in a glance.

**A trend**, alongside the level. A number that is good and falling and a number that is bad and rising need opposite responses, and the level alone hides which you have.

## Layout

Order by what matters, not by what is available. The two or three that decide the conversation go at the top at a size that reads across a room.

Group the rest by the question they answer rather than by which system they came from. A reader thinks in questions, not in data sources.

Show sample size or volume beside any rate. A conversion rate of forty percent on ten observations belongs on a page differently from one on ten thousand.

Where a target exists, show it as a line rather than a colour. Where thresholds are used, define them on the page, since a colour with no stated rule is an opinion rendered as a fact.

Follow the house figure standard: restrained, monochrome first, series separated by pattern and marker rather than by colour alone, accent colours used sparingly and consistently. A dashboard using twelve colours is unreadable to anyone with a common colour vision deficiency and looks unserious to everyone else.

## Say what the page does not show

A short, explicit list at the bottom: the measures that were considered and left off, and why. This prevents the slow accumulation that kills every dashboard, and it gives an honest answer to the person who asks why their number is not there.

## Annotate

Let the page carry short notes on the chart: a launch, a price change, an outage, a definition change. A metric that stepped in March and a note saying why is a page people trust. A definition change with no annotation is how a dashboard silently starts lying.

## Build

Static where the numbers refresh on a schedule rather than continuously, which is most cases. A page generated from a data file, regenerated when the file updates, is simpler, faster, and survives without maintenance far longer than a live connection to a warehouse.

Where it must be live, keep the query layer thin and show the query time. Either way the underlying rows should be downloadable, because someone will need to check the number and asking them to trust it is how the page loses its authority.

Make it work on a phone, since the person who most needs it will look at it in a taxi.

## Review it

Once a quarter, ask of every metric: has anyone acted on this since the last review. Anything unacted-on comes off. Also check that the definitions still match the systems, since systems change silently and dashboards keep reporting confidently through it.

## Quality bar

- Every metric is on the page because a decision depends on it, and the decision can be named.
- Five to nine measures, and adding one means removing one.
- Every metric has a written definition visible from the page, a named owner, a source, and a refresh time.
- Nothing appears as a bare number; every figure carries a comparison and a trend.
- Rates are shown with their volume.
- Thresholds and targets are defined on the page rather than implied by colour.
- What the page deliberately excludes is listed.
- Definition changes and material events are annotated on the charts.
