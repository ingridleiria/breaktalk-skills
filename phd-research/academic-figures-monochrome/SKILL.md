---
name: academic-figures-monochrome
description: Produces journal-ready, print-safe academic figures (event studies, coefficient plots, trends, distributions, scatter and binned plots, bar charts, maps) in a monochrome house style where series are separated by line pattern, marker shape, and grey value rather than colour, with the legend always outside the plot area, in Stata, matplotlib, or R. Use this skill whenever a researcher asks for a figure for a paper, thesis, or presentation, an event-study plot, a coefficient plot, parallel trends, "make this figure publication quality", "my figure is too colourful", "Stata style figure", or needs to restyle an existing chart to a journal standard. Trigger for any figure destined for an academic document.
---

# Academic Figures, Monochrome

A figure in a paper must survive three conditions: a black-and-white printer, a colour-blind reader, and a referee with no patience. Colour fails the first two. This skill separates series by pattern and shape, keeps the legend out of the data, and makes each figure carry exactly one message.

## The house palette

Colour is used as an ordered grey ramp, with at most two accent colours allowed when more than four series are unavoidable or when a single series must stand out.

| Role | Hex |
| --- | --- |
| Primary series | #000000 |
| Second series | #404040 |
| Third series | #7F7F7F |
| Fourth series | #A6A6A6 |
| Accent one (only if needed) | #1F3864 navy |
| Accent two (only if needed) | #7B1E28 wine |
| Confidence bands | grey fill at 20 to 30% opacity, or dashed lines |
| Reference lines (zero, cutoff, treatment date) | thin, black or dark grey, dashed |

Background white, no gridlines or light dotted horizontal gridlines only, no chart border box, no 3D, no shading gradients.

## Separation rules

- Line series: solid, dashed, dotted, dash-dot, in that order, before any change of grey value. Combine pattern and grey for four series.
- Marker series: circle, square, triangle, diamond, filled versus hollow. Always a marker on point estimates in coefficient and event-study plots.
- Bars: separated by hatching (none, diagonal, cross, dots) and grey value, never by colour.
- Confidence intervals: capped vertical lines on point estimates, or a shaded band for continuous event-time; never both.

## Legend and labels

- Legend outside the plot area, above or below, in one row where it fits. Never inside the plotting region and never covering data.
- Axis titles with units. Y-axis for the outcome in the units the reader will interpret (standard deviations, percentage points, log points).
- Direct labels at line ends are preferred to a legend when two or three series are clearly separable.
- No chart title inside the figure file; the caption in the document carries the title and the note.
- Font: a serif matching the document (Times New Roman for most journals) or the document's sans; one family, sizes readable at the printed width (8 to 10 pt at final size).

## Standard figure types

- **Event study**: event time on the x-axis with the reference period marked at zero, point estimates with confidence intervals, a horizontal line at zero, a vertical dashed line before treatment, binned endpoints labeled as such. Pre-period coefficients are the identification evidence; give them the same visual weight as post-period ones.
- **Coefficient plot**: estimates from several specifications or outcomes on a common scale, sorted meaningfully, with a zero line; specification labels on the y-axis.
- **Trends by group**: treated and comparison group means over time, treatment date marked, series separated by pattern, direct labels.
- **Distributions**: kernel densities or histograms by group, hatched or grey-stepped, with a vertical line at the cutoff for RDD.
- **Binned scatter (RDD)**: bins as hollow circles, fitted lines on each side of the cutoff, cutoff marked, bandwidth stated in the note.
- **Maps**: grey ramp choropleth with a legend outside, boundaries thin, no basemap clutter.

## Implementation

- **Stata**: a scheme file plus a graph preferences do-file that defines the line patterns, markers, grey values, and legend position as globals, so every figure in the project uses the same settings. Export to PDF or EPS for LaTeX, high-resolution PNG for Word.
- **matplotlib**: a style file (rcParams) implementing the palette, patterns, and legend placement, with helper functions for event-study and coefficient plots.
- **R (ggplot2)**: a theme function and scale definitions for linetype, shape, and grey.

Every figure is produced by a script saved with the project, so a change in results regenerates the figure without manual editing. Follow the environment's figure-generation skills for mechanics.

## Caption and note

Each figure's caption states what is plotted, the sample, the years, and the estimator; the note states the confidence level, the clustering, the reference period, and the source. A figure that needs the text to be understood has an incomplete caption.

## Quality bar

- Printed in greyscale, every series is still distinguishable.
- Legend is outside the plot area.
- One message per figure, visible within five seconds.
- Units on the axes; confidence level and clustering in the note.
- Regenerated by code, not edited by hand.
