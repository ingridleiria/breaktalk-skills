---
name: image-to-spreadsheet
description: Converts data trapped in an image into a spreadsheet that states its own reliability: screenshots of tables, photographed invoices, receipts and forms, handwritten notes, and charts whose underlying values have to be reconstructed. Produces a workbook with every value carrying a confidence code, unreadable cells left visibly empty rather than filled, chart-derived figures labelled as estimates with their precision, an arithmetic integrity check against any total the source itself contains, and row and column counts the user can verify against the image in seconds. Enforces the standard that nothing is corrected, reformatted or computed that the source did not contain. Use this skill whenever an image is supplied and the deliverable is a file rather than an answer, including "digitise this", "OCR this into Excel", "type this form into a sheet", "pull the numbers off this graph", "get these receipts into a spreadsheet", and any request to turn a photo, screenshot or scan into data.
---

# Image to Spreadsheet

The failure mode of this task is not missing data. It is confident data. A smudged seven transcribed as a one, a chart estimate presented in the same column as a printed figure, a total silently computed that the source never contained, a date reformatted from one convention into another on the way in. Every one of those produces a clean, plausible spreadsheet, and the spreadsheet then becomes the source of truth while the image is filed and never opened again.

What that costs depends on where the file goes next, and it is rarely trivial: an expense reconciliation that fails by an amount nobody can locate, a competitor comparison built on values read off a bar chart to a precision the chart could not support, a model whose input cell nobody can trace back to a pixel. The repair cost is not the retyping, it is that once a number has been wrong for a week, every downstream figure has to be re-derived and every person who used it has to be told.

The discipline is therefore simple and it is not about accuracy alone: read everything before writing anything, transcribe exactly, never resolve an ambiguity silently, and make the file say which of its own values are certain.

## When to use this, and when not to

Use it whenever an image arrives and the deliverable is a file: screenshots of tables and interfaces, photographed or scanned invoices, receipts, forms and statements, handwritten notes and tally sheets, printed reports, and charts whose values have to be reconstructed. Use it for one image or for a stack of two hundred sharing a structure.

Do not use it to answer a question about an image where no file is wanted. "How much was this invoice for" is answered directly and the answer is the deliverable. Do not use it where the data is already machine readable: a CSV, an export, a PDF with a real text layer. Those are opened with the ordinary spreadsheet or document tooling, and treating a text-layer PDF as an image throws away accuracy for no reason; check for a text layer before assuming.

Do not use it for the analysis of the data once it is extracted. `spreadsheet-analysis-workbook` holds the discipline for analysing a workbook without breaking it or trusting it blindly, and `revenue-analysis-workbook` builds the standard revenue views. This skill hands those a clean, honestly labelled input and stops. Do not use it to redraw a chart for publication, which is `academic-figures-monochrome`. Where a chart's underlying values matter for a decision, the correct first move is often not extraction at all: find the source data, since the publisher of the chart usually has it and estimation from a picture is a fallback rather than a method.

## What you need before starting

**Every image, at the resolution it was captured.** A screenshot re-shared through a messaging application may have been recompressed; a photograph may have been downscaled. Missing: work with what you have, but state the limitation before extracting rather than after, and where the deliverable is financial, ask for the original once.

**What the data is for.** Precision requirement follows from this, and it is the input that most changes the work. A figure that will be summed and reconciled needs a second pass on every digit; an indicative comparison does not. Missing: assume it will be summed, which is the more expensive assumption and the safe one, and say you have assumed it.

**The expected structure, if the user knows it.** How many rows, what the columns should be, whether the image is one table or several. Missing: derive it from the image and show the structure back before building the file, since a structural misunderstanding is cheap to fix in a plain text sketch and expensive to fix in a workbook.

**The conventions in force.** Date order, decimal separator, thousands separator, currency, whether tax is inclusive in a line total. Missing: transcribe exactly as shown, do not normalise, and put the convention question in the reply. A date of 03/04 is not a small ambiguity in a financial file.

**A control total, or anything the arithmetic can be checked against.** An invoice total, a page subtotal, a stated row count. Missing: say that no independent check was possible, which is a material statement about the file's reliability and is not the same as saying the file is fine.

**The output shape.** One workbook or several, sheet naming, whether the user has an existing template. Missing: one workbook, one sheet per logical table, notes and confidence columns at the end, and say that is what you did.

## The method

1. **Look at every image before writing anything down.** All of them, including the last one. Structure changes partway through a stack more often than anyone expects: a supplier changes an invoice layout, a form has a continuation page with different columns, page two of a table drops the header. Inferring page two's structure from page one is the single most productive error in this task.

2. **Say what is wrong with the images, first.** Rotation, crop through a column, glare across a total, low resolution, a fold through a row, part of a page missing. State it at the start rather than discovering it in the reply. Judgement call: whether to proceed or ask for a rescan. Rule: proceed when the deliverable is indicative and the damage is localised; ask when a total, an identifier or more than about one value in twenty is affected, because a rescan takes the user two minutes and a reconstruction takes you an hour and is worse.

3. **Classify each image, because the method differs by type.** A clean digital capture such as a screenshot or an export should extract near exactly. A photographed printed document brings glare, perspective skew and cut edges, and it usually contains its own arithmetic, which is the best integrity test available. Handwriting is low confidence in every field and stays that way. A chart is not reading at all, it is reconstruction from a visual encoding, and it is an estimate by definition. One image can be a mix, and a photographed form with handwritten entries is two classifications in one page.

4. **Draft the structure in plain text before touching any workbook.** Rows, columns, headers, merged cells, footnotes, units. Show it back where the structure is not obvious. A header spanning two columns, a total row embedded mid-table, a footnote that redefines a column: all cheap to resolve here, all expensive to unpick later.

5. **Transcribe exactly as shown.** Do not correct apparent typos. Do not reformat dates or numbers into another convention. Do not compute a total the source does not contain. Do not expand an abbreviation. Where the source is internally inconsistent, for example a line total that does not match quantity times price, transcribe both and flag the inconsistency; it belongs to the source, not to you.

6. **Code every value for confidence as you go.** Four codes, and they go in the file, not only in the reply. A: read directly and unambiguously. B: read with difficulty, or inferred from context such as a value constrained by a total. C: estimated from a chart or a partial glyph. X: unreadable, cell left empty. The judgement call is the boundary between A and B, and the rule is that any hesitation at all makes it B, because a code that only marks the values you already know are bad adds nothing.

7. **Never resolve an ambiguity silently.** Where a digit could be a 1 or a 7, a 3 or an 8, a 0 or a 6, record the reading you think most likely, code it B, and put both candidates in the notes column. Choosing quietly produces a file that cannot be audited, and the cost of the flag is one cell of text.

8. **Run the arithmetic check wherever the source contains one.** Line items against a stated subtotal, subtotals against a total, quantities times unit prices against line totals, columns against a stated column sum. This is the highest-value five minutes in the whole method, because it catches transcription errors that look perfectly plausible in isolation. Where the check fails, do not adjust a value to make it balance. Locate the discrepancy, and where it cannot be located, record it in the verification block as an unexplained difference with its amount.

9. **Reconstruct charts by the procedure below**, and never mix chart-derived values into a column of read values without the confidence code distinguishing them.

10. **Build the workbook.** Bold header row, numbers stored as numbers so sorting and totals behave, sensible column widths, header frozen for anything over about fifteen rows. Keep a value as text only where it is genuinely not a number, such as "approximately 200", and say why in the notes column. One sheet per logical table, one workbook per job unless separate files are asked for. Where several images share a structure, consolidate into one sheet with a source image column identifying each row's origin. Notes and confidence columns go at the end, never interleaved with the data.

11. **Write the verification block into the file**, not only into the reply, and close with the counts.

## Reading a chart

Chart extraction is estimation and the file must say so. Work through the encoding in order.

Identify the chart type and what each element encodes: axes, legend, series, segments, stacking. Read the scale and, most importantly, the gridline increment, because the increment sets the precision you are entitled to claim. An increment of 10 supports reading to about 5; an increment of 25 supports about 12.5, and a value recorded as 137 off a chart with 25-unit gridlines claims a precision the picture does not contain. Record the increment in the file.

Then estimate each point against the scale: the top of the bar for columns, the labelled vertex for lines, the printed data label wherever one exists. Where the image includes a data table or data labels, use those exact values and code them A; a chart with labels is not a chart-reading problem at all. For pie segments, use printed labels in preference to judging angles, which are read badly by everyone.

Three rules stop chart data from becoming false precision. Round every estimate to the gridline increment or half of it, never to a spuriously exact figure. State the precision in the file, for example "estimated, gridlines at 25, precision about plus or minus 12". And do not compute totals, growth rates or shares from chart estimates and present them as figures; where a derived number is genuinely needed, present it as a range.

Where the extracted values are to be replotted, plot them monochrome, separating series by marker shape and dash pattern rather than by colour, with the legend outside the plot area and any accent colour used sparingly on the one series that carries the argument. A chart rebuilt from estimates should also carry its precision in the axis label or the caption.

## The verification block

Every workbook gets one, on the first sheet or its own sheet, filled in.

```
EXTRACTION VERIFICATION
Source images:        [count, file names]
Extracted:            [rows] x [columns]  per sheet
Confidence counts:    A [n]   B [n]   C [n]   X [n]
Unreadable cells:     [count, with cell references]
Ambiguous readings:   [count, with cell references and both candidates]
Arithmetic check:     [what was checked against what]
                      Source total: [figure]   Sum of extracted: [figure]   Difference: [figure]
Unexplained:          [amount, and what is known about it]
Chart-derived values: [count, which columns, gridline increment, stated precision]
Conventions assumed:  [date order, decimal separator, currency, tax treatment]
Not transcribed:      [anything visible in the image and deliberately omitted, and why]
```

## Worked example

**Situation.** A finance manager at a facilities company sent 34 photographs of supplier invoices and receipts, taken on a phone across a table, for a quarterly expense reconciliation. The stated control total from the accounting system was 18,442.60. Roughly two thirds were printed invoices from four suppliers and the rest were till receipts, two of them creased. The deliverable was a spreadsheet the finance manager would reconcile line by line against the ledger the following morning.

**Task.** One workbook, every line item, by the end of the day, with anything uncertain visible rather than smoothed away. Good meant the finance manager could reconcile without opening the photographs, except for the cells the file told her to check.

**Action.** The wrong turn happened at image one. The first invoice, from Ardwick Supplies, had a clean layout: description, quantity, unit price, line total, with tax shown once at the foot. The structure was drafted from it and extraction proceeded through the stack at speed. By image 22 there were 212 line items in a plain text draft.

The arithmetic check caught it. Invoice subtotals were being computed against the extracted lines as each supplier's block finished, and from image 12 onwards every one of them overstated the invoice by between 18 and 21 percent. Image 12 was the first from a different supplier, Pellworth Trade, whose layout showed tax inclusive in each line total and no separate tax row. Every line from image 12 to image 22 had been extracted into a column that meant something different from the same column in images 1 to 11.

Twenty-two rows spanning eleven images were re-extracted, and the sheet gained a column for tax treatment per line rather than per invoice. The two hours lost produced the rule that is now step one of the method: look at every image before writing anything down. Ten minutes of looking would have shown two layouts.

The completed extraction ran to 212 line items across 34 source images, consolidated into one sheet with a source image column. Six cells were left empty and coded X: four on a creased till receipt where the fold ran through the amounts, and two on a receipt where thermal print had faded. Three values were coded B for ambiguous digits, each with both candidates in the notes column, including one where a quantity was either 11 or 17 on a handwritten delivery note. Nothing was corrected: one invoice showed a line total of 84.00 where quantity times unit price gave 84.60, and both figures were transcribed with the inconsistency flagged, because it was the supplier's arithmetic and the finance manager would need to raise it.

The arithmetic check summed to 18,410.10 against the control total of 18,442.60, a difference of 32.50. Rather than adjusting anything, the difference was traced: 32.50 was the amount visible on the creased receipt's total line, which was legible, while its four line items were not. That was recorded in the verification block as an identified but unallocated difference, with the receipt named.

**Result.** The file was delivered with 212 rows, the verification block filled in, and a four-line reply naming the six unreadable cells, the three ambiguous readings, and the 32.50 with its explanation. The finance manager reconciled it the next morning and needed the photographs for two cells: the 11-or-17 quantity, which was 17, and one of the faded amounts.

The 84.00 against 84.60 line turned out to be a supplier error worth 0.60 on that invoice and, once queried, about 340 across the quarter, because the same rounding appeared on every invoice from that supplier. That was found by transcribing exactly rather than by any cleverness, and it would have been invisible had the extraction quietly recomputed the line total.

### A second scenario, where it goes differently

A market analyst supplied one image: a stacked bar chart from a published industry report showing revenue by segment for six years, with no data labels, no data table, and gridlines at 25 on an axis running 0 to 200.

Almost nothing from the first scenario applied. There was no exact transcription, no arithmetic check available in the source, and no control total. Every one of the 24 values was coded C, and the file recorded the gridline increment of 25 with a stated precision of about plus or minus 12. The top segment of each bar was read against the axis; the lower segments were read as differences between boundaries, which compounds error, so those were coded C with a note that they carry roughly twice the uncertainty of the top segment. That distinction does not appear in the picture and would have been lost in a flat extraction.

The request that followed was to compute each segment's compound annual growth rate over the six years. That was declined as a figure and delivered as a range: with a precision of plus or minus 12 on values between 30 and 80, the growth rates for the two smaller segments spanned ranges wide enough that their ordering could not be established, so the file gave the range and said which comparisons the chart could and could not support. Producing a table of growth percentages to one decimal place from that image would have been the exact failure this skill exists to prevent, and it would have looked entirely professional.

The last step was the one that mattered most: the report's methodology page named the underlying data provider, and the analyst was told that half an hour finding the source would beat any estimate from the picture. It did. The published figures differed from the chart estimates by up to 9 in two of the six years, within the stated precision but enough to reverse one of the comparisons the analyst had intended to make.

What changed: with no source arithmetic and no labels, the deliverable moved from a data file to an estimate file with a stated precision, and the most useful output was not the numbers but the statement of which questions the image could not answer.

## Output

One workbook, plus a short reply that does not bury the caveats.

**Data sheet**, one per logical table:

| Source image | Row identifier | [data columns, transcribed exactly] | Confidence | Notes |
| --- | --- | --- | --- | --- |

Confidence takes A, B, C or X. The notes column carries both candidates for an ambiguous reading, the reason a value is stored as text, any internal inconsistency in the source, and how a merged or ambiguous header was resolved.

**Verification sheet**, the block above, filled in.

**Reply**, four to six lines: row and column counts per sheet so the user can check against the image at a glance; the cells left unreadable, by reference; the ambiguous readings and their candidates; whether anything came from chart estimation and at what precision; and the arithmetic check result including any unexplained difference. Do not ask permission for ordinary extraction. Ask only where the image is ambiguous enough that guessing wrong would be worse than waiting.

## Failure modes

**Inferring the structure of image two from image one.** The most productive error in this task. Recognise it when an arithmetic check starts failing partway through a stack, which is the lucky case, or never, which is the usual one. Look at every image first.

**Silently resolving an ambiguous digit.** Recognise it by the absence of any B codes in a file extracted from photographs or handwriting, which is not plausible. Record the reading, the code and both candidates.

**Computing a total the source did not contain.** A sum appears in the file, then in a report, then in a conversation, and its provenance is gone. Recognise it by asking which pixels the number came from. Totals the source contains are transcribed; totals the user needs are built as visible formulas and labelled as derived.

**Normalising on the way in.** Dates reordered, decimal separators swapped, currency symbols dropped, abbreviations expanded. Recognise it when the file is tidier than the image. Transcribe exactly and put the convention question in the reply.

**Adjusting a value to make a total balance.** The most damaging error in the list, because it destroys the evidence that something was wrong. Recognise it when a difference disappeared without being explained. Never adjust; locate, or record as unexplained.

**Chart estimates carried as figures.** Recognise them by a value more precise than the gridlines allow, or by a derived percentage computed from estimates. Round to the increment, code C, state the precision, and give derived numbers as ranges.

**Treating a text-layer PDF as an image.** Recognise it by trying to select the text. Extraction from the text layer is exact and free; reading it visually is neither.

**Burying the caveats.** Six unreadable cells mentioned in the eleventh line of a reply is the same as not mentioning them. Counts and unreadable cells go in the first four lines and in the file.

## Edge cases

**A stack of images with more than one layout.** Consolidate into one sheet only where the columns genuinely mean the same thing. Where they do not, either add a column that captures the difference, such as tax treatment per line, or use separate sheets with a mapping note. Never force two meanings into one column.

**The image is a photograph of a screen.** Expect moire, glare and skew, and expect the worst legibility exactly where the screen was brightest, which is often the total. Ask for a screenshot; it costs the user one keystroke.

**Handwriting.** Every field is B at best. Do not resolve ambiguous digits, do not infer a name from a partial one, and where a whole entry is a guess, code it X rather than producing a plausible line. A handwritten tally with 5 of 40 entries unreadable is a usable file; the same file with 5 invented entries is not.

**Redacted or partially covered data.** Transcribe what is visible, code the rest X, and record in the verification block that the omission was in the source rather than in the reading. Never interpolate across a redaction.

**Personal or sensitive information in the image.** Bank details, identification numbers, health information, home addresses. Extract only the fields the task requires, say what you have omitted and why, and do not copy sensitive fields into a working file merely because they were visible.

**The image contains a chart and its own data table.** Use the table, always, and code the values A. Mention that the chart was not used, since a reader may otherwise assume estimation and discount the file.

**Multi-page tables with a repeated header.** Extract as one logical table with a source image column, and check that the last row of a page and the first of the next are not the same row appearing twice, which happens whenever pages overlap.

**A very large stack, over about a hundred images.** Extract a sample of ten spanning the range first, confirm the structure and the confidence profile with the user, then proceed. Discovering a systematic misreading at image 180 is the same error as scenario one at a cost that cannot be absorbed.

## Quality bar

- Every image was viewed before any transcription began, and layout changes across the stack are recorded.
- Nothing was corrected, reformatted, expanded or computed that the source did not contain.
- Every value carries a confidence code in the file, and any hesitation was coded B rather than A.
- Unreadable cells are empty and referenced by cell address; ambiguous readings carry both candidates.
- Chart-derived values are coded C, rounded to the gridline increment, and carry a stated precision, and no derived figure is presented from them without a range.
- The arithmetic check against any total the source contains is recorded with its result, and any difference is located or declared unexplained with its amount.
- The verification block is in the file, not only in the reply, and the reply gives row and column counts in its first lines.
- Numbers are stored as numbers, and any value kept as text says why.

## Related skills

`spreadsheet-analysis-workbook` takes the extracted file and holds the discipline for analysing it without trusting it blindly; hand it a file whose confidence codes are intact so it can decide what the analysis may rest on. `revenue-analysis-workbook` and `economics-report-from-data` build the standard views and the argument once the data is clean. `academic-figures-monochrome` handles redrawing a chart for publication, which is a different job from recovering its values. `data-profiling-and-cleaning` takes over where the problem is a large messy dataset rather than an image. Where the deliverable is an answer rather than a file, no skill is needed: read the image and say what it says.
