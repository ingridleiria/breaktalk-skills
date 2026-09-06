---
name: interactive-results-explorer
description: Builds a page where a reader can explore results themselves rather than only read the author's chosen cut: the underlying rows shipped with the page, filters and comparisons that are honest about uncertainty, charts that keep their axes stable when the selection changes, a table view behind every chart, download of the exact filtered data, and a stated method note. Covers when interactivity earns its place and when a static figure is better. Use this skill for a results explorer, an interactive appendix, a data-driven page for a paper or a report, or when someone wants a dashboard of findings that other people will use.
---

# Interactive Results Explorer

Interactivity is worth building when a reader has a legitimate question the author cannot anticipate: their own country, their own sector, their own cohort. It is not worth building to make a static finding look sophisticated, and an explorer that lets people wander through subgroups without warning is a specification-searching machine pointed at your own results.

Decide first. If there are fewer than about five views anyone would reasonably want, produce five static figures and stop. If the honest answer is that the reader should look at one number, show them that number.

## The one rule about subgroups

If the page allows slicing, it must say what the slices mean statistically. Small subgroups produce large apparent effects and a reader who does not work with data will believe them.

Two mechanics fix most of this. Show uncertainty on every estimate, not only on the headline. And show the underlying count with every cell, greying out or explicitly suppressing anything below a stated threshold, with the threshold on the page rather than in a note.

Where the paper's claims are limited to certain cuts, say so where the reader is making other cuts, not in a footnote at the bottom.

## Ship the data with the page

The rows behind the page live in a plain file loaded by the page: CSV or JSON, human-readable, documented. That file is downloadable in full and the current filtered view is downloadable separately, so a reader can check what they are seeing.

If the data cannot be published at that granularity, publish the aggregated cells that the page actually displays, which is what it is showing anyway.

## Charts that stay honest under interaction

Keep axes fixed across selections unless there is a reason not to, and say when they rescale. Axes that rescale silently make every selection look equally dramatic, which is the most common way an interactive chart misleads without anyone intending it.

Never truncate a value axis on a bar chart. Keep colour and marker meaning stable across every view. Show empty states explicitly: "no observations for this selection" rather than a blank chart, which reads as zero.

Follow the house figure standard so the explorer looks like the paper: monochrome first, series separated by pattern and marker, legend outside the plot area, accent colours used sparingly and consistently.

Put a table view behind every chart, reachable in one click. Some readers want the numbers, screen readers need them, and it is the cheapest accessibility win available.

## Interaction design

Default to the view that answers the main question, so a reader who touches nothing still gets the finding.

Put the state in the URL, so a reader can send a link to what they are looking at. This single feature is most of what makes a results page get shared and cited.

Keep the controls few and labelled in the reader's language, not the variable names. Every control needs a visible reset. Nothing important should be hidden behind hover, which does not exist on a phone.

Make it work on a phone, which is where a meaningful share of readers will open a shared link, and make sure the table scrolls inside its own container rather than pushing the page sideways.

## The method note, on the page

Short, visible, not a PDF link: what the data is and where it came from, the period, what one row represents, how the estimates were produced, what the uncertainty shown means, what the suppression threshold is, and what the page does not support conclusions about.

Version the page and date it. Anyone citing a number from it needs to know which version produced it.

## Build

Static files, one page, no build step, no server. A chart library loaded from a fixed version is acceptable; a framework and a build pipeline for a results page is not, because in three years the build will not run and the page will be gone.

Test with the data file replaced by a larger one before publishing, since the version that runs on your machine with the small file is not the one your readers get.

## Quality bar

- Interactivity was justified before it was built, and a static set of figures was the alternative considered.
- The rows behind the page are downloadable, in full and as filtered.
- Uncertainty and the underlying count appear on every estimate, with a stated suppression threshold.
- Axes stay stable across selections, and any rescaling is announced.
- Every chart has a table view.
- The state is in the URL and the page works on a phone.
- The method note is on the page, and the page is versioned and dated.
- No build step, and the page still works with the chart library cached from a fixed version.
