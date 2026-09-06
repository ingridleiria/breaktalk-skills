---
name: image-to-spreadsheet
description: Converts data trapped in an image into a clean spreadsheet: screenshots of tables, photographed invoices and receipts, printed forms, handwritten notes, and charts whose underlying values have to be reconstructed. Enforces reading before writing, exact transcription with no silent corrections, explicit flags on anything illegible or ambiguous, and a stated distinction between values read directly and values estimated from a chart. Use this skill whenever an image is supplied and the deliverable is a spreadsheet rather than an answer, including "digitise this", "OCR this into Excel", "pull the numbers off this graph", and "type this form into a sheet".
---

# Image to Spreadsheet

Read carefully, never invent, flag anything uncertain, and only then build the file. The failure mode of this task is not missing data, it is confident data: a smudged seven transcribed as a one, a chart estimate presented as a printed figure, a total silently computed that the source never contained.

## Step 1: Look at every image

Study the image directly if it is already visible in the conversation. If it is only referenced by path, open it first. For a multi-page or multi-image job, look at all of them before writing anything down; do not infer page two's structure from page one. If an image is rotated, cropped mid-table, low resolution, or otherwise hard to read, say so at the start rather than guessing quietly.

## Step 2: Classify the source

The method differs by type, and one image can be a mix.

- **Clean digital capture**, such as a screenshot of a table, a user interface, or a document export. Text is crisp and extraction should be near exact.
- **Photographed printed document**, such as a receipt, invoice, or form. Watch for glare, perspective skew, and edges cut off. Where both line items and totals are visible, check the arithmetic; printed maths is a good integrity test.
- **Handwriting.** Every field is lower confidence. Never resolve ambiguous handwriting into a confident-looking number.
- **Chart or graph.** This is not reading, it is reconstruction from a visual encoding, and it is an estimate by definition.

## Step 3: Extract

For tables, forms, and text, draft the structure in plain text before touching any code: rows, columns, headers, merged cells, footnotes. Structural problems such as a header spanning two columns are cheap to fix here and expensive to fix in the workbook.

Transcribe exactly as shown. Do not correct apparent typos, do not reformat dates or numbers into another convention, and do not compute totals the source does not contain. Write `[unreadable]` where a cell genuinely cannot be read, and flag any value that could be read two ways rather than choosing one. Keep units, currency symbols, and percentages either in their own column or attached consistently, so that the numeric columns stay calculable.

For charts, work through the encoding: identify the chart type and what the axes, legend, and segments represent; read the scale and the gridline increment, because an increment of ten and an increment of twenty five imply different precision; then estimate each point against the scale, using the top of the bar for columns, the labelled vertices for lines, and any printed data labels for pie segments in preference to judging angles. Where the image includes a data table or data labels, always use those exact values instead of estimating. Carry every chart-derived figure into the workbook with a note saying it was estimated from a chart and should be verified against source data if precision matters.

## Step 4: Handle uncertainty in the file, not only in the reply

Leave genuinely unreadable cells blank and record why in a notes column. Mark chart-derived values as estimates in the file itself. Mention any judgement call, such as how a merged header was split, in the reply so the user can check it against the image.

## Step 5: Build the workbook

Follow the standard spreadsheet conventions for the environment: a bold header row, sensible column widths, the header frozen for anything longer than about fifteen rows, and numbers stored as numbers so that sorting and totals work. Keep a value as text only when it is not a clean number, such as "approximately 200", and say why.

One sheet per logical table, one workbook per job unless separate files are requested. Where several images share a recurring structure, such as a stack of receipts, consolidate them into one sheet with a source image column identifying each row's origin. Put any notes or confidence column at the end rather than interleaved with the data.

## Step 6: Confirm

Present the file with a short, unburied summary: the cells left unreadable, whether anything came from chart estimation, and the row and column counts as a check the user can run against the image in a glance. Do not ask permission for ordinary extraction. Ask only when the image is ambiguous enough that guessing wrong would be worse than waiting.

## Not for this skill

A question about what an image shows, with no file wanted, is answered directly. Data already in a machine-readable file, such as a CSV or a PDF with a real text layer, is handled with the spreadsheet or PDF tooling rather than treated as an image problem.

## Quality bar

- Every image looked at before any transcription begins.
- Nothing corrected, reformatted, or computed that the source did not contain.
- Unreadable and ambiguous cells visible in the file, not smoothed away.
- Chart-derived numbers labelled as estimates wherever they appear.
- Row and column counts reported so the user can verify in seconds.
