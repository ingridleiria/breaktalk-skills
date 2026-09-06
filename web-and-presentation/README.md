# Web and presentation track

Four skills for the moment the work is finished and has to be seen by someone who was not involved in it. A paper that only exists as a PDF behind a login, and a set of numbers that only exists in the analyst's workbook, both reach far fewer people than they should.

Everything here is built the same way: static files, no build step, accessible by default, and figures that follow the same monochrome-first standard as the print versions. A page built on a framework stops working in three years when the build no longer runs. A page that is one HTML file and a folder of figures opens in ten.

## The skills

| # | Skill | What it enforces |
| --- | --- | --- |
| 107 | [research-paper-website](research-paper-website/SKILL.md) | The plain-language finding, the figures, the data and the citation, as files that outlive frameworks |
| 108 | [interactive-results-explorer](interactive-results-explorer/SKILL.md) | The rows shipped with the page, uncertainty on every estimate, and axes that stay honest |
| 109 | [academic-personal-site](academic-personal-site/SKILL.md) | What a committee, an editor and a collaborator each came for, and nothing else |
| 110 | [metrics-dashboard-page](metrics-dashboard-page/SKILL.md) | Five to nine measures a decision depends on, each with a definition, an owner and a comparison |

## Choosing between them

`research-paper-website` is the companion page for one paper or project: the plain-language finding, the figures at full resolution, the data and code, and the citation. It is where you send someone who asks what you found.

`interactive-results-explorer` is for when readers have legitimate questions you cannot anticipate, such as their own country or sector. It also carries the warning that most explorers need: a page that lets people slice freely without showing uncertainty and sample counts is a specification-searching machine pointed at your own results.

`academic-personal-site` is the researcher's own page, built around the three people who actually visit one and want different things.

`metrics-dashboard-page` is the operating version of the same discipline, and belongs as much to the Chief of Staff track as to this one. Its rule is that a measure earns its place only if a decision depends on it.

## The shared standard

Semantic headings in order. Real alternative text that says what a figure shows rather than what it is called. Contrast that passes at body size. Text that reflows on a phone, since a large share of readers arrive on one. Tables marked up as tables rather than as images. Nothing that requires a mouse, and nothing that requires scripting to read the content.
