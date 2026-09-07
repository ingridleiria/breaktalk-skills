---
name: stata-data-management
description: Takes raw files to an analysis-ready .dta that can be defended line by line. Covers import from csv, Excel and fixed width, the encode and destring decision, variable and value labels, Stata's numeric date representation, merge with reported match rates and a rule for every _merge value, joinby, append, reshape in both directions, duplicates and isid, missing value codes including extended missing, collapse against egen by group, xtset and panel structure checks including gaps and unbalanced panels, compress and saving with notes, and the rule that a raw file is never overwritten. Use this skill when someone is importing data into Stata, merging files, reshaping a panel, fixing identifiers that will not match, converting strings to numbers, handling missing value codes, building a panel dataset, or says the numbers changed after a merge, the observation count is wrong, or the data will not xtset. Trigger also on vague requests such as "get this into Stata", "my merge is dropping observations", or "why is my sample smaller than it should be".
---

# Stata Data Management

The failure this prevents is a dataset that looks finished and is wrong in a way no regression output will ever reveal. A municipality identifier read as a number lost its leading zero, so 1,400 of 12,000 rows failed to match and were dropped as though they were missing at random. An income variable coded minus ninety-nine for refusal was never recoded, so the mean is negative in three states and nobody looked at the mean. A survey wave appended to another used the same value label with different meanings, so category three means "part-time" in one year and "self-employed" in the next. A `reshape long` silently balanced the panel and added 6,000 rows of nothing.

None of these produce an error. All of them produce a table. The cost is that every subsequent decision, the specification, the sample, the interpretation, rests on a file whose defects are invisible from the estimation output, and they surface either when a referee asks how many observations were lost at each stage or when a coauthor rebuilds the file and gets a different number. By then the paper has been written around the wrong figure.

The discipline is that every operation which can change the number of rows, the number of units, or the meaning of a code is followed immediately by a check that says what should now be true, and the counts are written down as they happen.

## When to use this, and when not to

Use it for the work between the raw file and the saved analysis dataset: importing, typing, labelling, recoding, combining files, changing the unit of observation, establishing panel structure, and saving. Use it when a merge is not matching, when the row count changed unexpectedly, when a variable will not convert, when appending waves of a survey, and when preparing a file that someone else will use.

Do not use it for the diagnostic pass on a dataset you have just received, which is `data-profiling-and-cleaning`: that produces the quality report, the outlier and impossible-code review, and the cleaning log, and it is language agnostic. This skill is the Stata command craft that implements those decisions and the traps specific to how Stata represents things.

Do not use it for the do-file architecture the code sits in, which is `stata-do-file-craft`, or for the folder structure, which is `stata-project-scaffold`. Do not use it to write the data section of the paper, which is `data-section-writer`, or the summary statistics table, which is `descriptive-statistics-tables`. Do not use it to decide which observations belong in the estimation sample on substantive grounds; that judgement belongs with `econometrician` and the reasoning belongs in `identification-defense`.

## What you need before starting

**The raw files and their provenance.** Where each came from, when it was downloaded or received, and under what version. Missing: record the file name, size and modification date at minimum, and say the provenance is unknown, because a file with no provenance cannot be re-obtained and the project is not reproducible upstream of it.

**The codebook for each source.** This is what tells you that minus eight means "does not apply" and that `q17b` is asked only of respondents who answered yes to `q17a`. Missing: reconstruct what you can from the data, mark every reconstructed meaning as inferred, and do not recode anything you had to guess without flagging it.

**The intended unit of observation of the final file.** Person-year, firm-year, household, municipality-quarter. Everything downstream depends on it and almost every merge and collapse error is a unit-of-observation error. Missing: state it explicitly in one line before writing any code, because you cannot check a key you have not named.

**The key variables that should identify a row in each source.** Missing: find them empirically with `duplicates report` on candidate combinations, and treat the result as provisional until confirmed against the codebook.

**The expected match rate for each merge, before running it.** A number, even a rough one. Missing: state your expectation anyway, because the value of the expectation is that it turns a surprise into a signal rather than into a number you accept.

**Whether identifiers are stable over time.** Firms merge, municipalities split, schools are renumbered. Missing: check whether the count of distinct identifiers is stable across waves and whether any appears under two names, and use the publisher's crosswalk where one exists rather than inventing one.

## The method

1. **Copy nothing into `data/raw` and write nothing out of it.** The raw directory holds the files as received and is read-only. Every operation on it is a `use` or an `import`, never a `save`. Where the platform allows it, set the directory read-only at the file system level, because the accident this prevents is a `save, replace` with the wrong path in it, which is unrecoverable when the source cannot be re-obtained. Record a checksum or the file size and date of each raw file so a later change is detectable.

2. **Import with the types you intend, not the types Stata guesses.** The single most expensive import error is an identifier read as numeric and stripped of leading zeros, because the damage appears later as a failed merge that looks like missing data. The rule: any variable that is a code rather than a quantity is imported as a string and stays a string until you have a reason to change it.

```stata
* csv: force codes to stay strings; state the encoding
import delimited using "$data/raw/survey_2023.csv", ///
    varnames(1) stringcols(1 2 7) encoding("UTF-8") bindquote(strict) clear

* Excel: name the sheet and the range; never rely on the default
import excel using "$data/raw/accounts.xlsx", ///
    sheet("Panel") cellrange(A4:AK5210) firstrow clear

* fixed width, driven by a dictionary file that is itself version controlled.
* The dictionary's own first line names the data file, so the two travel together:
*     infix dictionary using "census2010.txt" {
*         str5 state  1-5
*         int  age    6-8
*     }
infix using "$code/dict/census2010.dct", clear
```

For Excel, check what the first row actually is before using `firstrow`: merged header cells, a title row, or a units row will become variable names and produce silent nonsense. For fixed width, the data file is named inside the dictionary rather than passed as a second `using`, and the dictionary is part of the code and belongs under version control, because a one-character offset shifts every field on the line.

3. **Convert strings to numbers deliberately, and check what the conversion lost.** `destring` is for numbers that happen to be stored as text. `encode` is for genuine categories. Using one where the other belongs is the second most common typing error.

```stata
* destring: never use force blind. Convert to a new variable and inspect the losses.
destring wage_str, generate(wage) ignore("$,")
count if missing(wage) & !missing(wage_str) & wage_str != ""
list wage_str if missing(wage) & !missing(wage_str) & wage_str != "", clean
```

`ignore()` strips characters silently, so ignoring a comma also silently converts "1,2" into 12 in a file that uses comma decimals. `force` converts what it can and sets the rest to missing with no record of what it discarded, which is why the count-and-list pattern above exists.

`encode` maps a string to integers with a value label attached, and the codes are assigned in alphabetical order of the string. That is the trap: encoding the same variable in two files, or in two waves, gives different numbers to the same category whenever the set of observed strings differs. The rule: define the label first and encode into it, so the mapping is fixed by the code rather than by the data.

```stata
label define sector 1 "Agriculture" 2 "Manufacturing" 3 "Services" 4 "Public"
encode sector_str, generate(sector) label(sector)
assert !missing(sector) if !missing(sector_str)   // catches unexpected strings
```

Never `encode` an identifier. A person or firm code with tens of thousands of distinct values produces a value label with tens of thousands of entries, bloats the file, and hides the identifier behind a display label. Use `egen id = group(id_str)` for a compact numeric panel identifier, and keep the original string alongside it.

4. **Label everything, and make the labels part of the deliverable.** A clean file has a variable label on every variable and a value label on every categorical. The reason is not tidiness: it is that the next person to open the file, including you in eight months, reads the labels and not the code.

```stata
label variable lwage    "Log real hourly wage, 2015 prices"
label variable female   "=1 if respondent is female"
label define yesno 0 "No" 1 "Yes"
label values female yesno
numlabel yesno, add          // tabulations show "1 Yes", not just "Yes"
labelbook, problems          // finds unused, duplicated and truncated labels
```

Run `labelbook, problems` before saving any file that will be shared. It finds labels attached to no variable, labels whose text is duplicated across different codes, and labels truncated by an export, all of which are silent until somebody misreads a table.

5. **Convert dates into Stata's numeric representation, and stop treating them as text.** A Stata daily date is an integer counting days from 1 January 1960, displayed by a `%td` format. The format is display only; the underlying number is what arithmetic and comparisons use. Monthly dates are `%tm`, counting months from January 1960, and quarterly are `%tq`.

```stata
generate date = date(date_str, "DMY", 2050)   // topyear resolves two-digit years
format date %td
assert !missing(date) if !missing(date_str)

generate mdate = mofd(date)
format mdate %tm

* an Excel serial number, using Excel's own epoch
generate xdate = excel_serial + mdy(12, 30, 1899)
format xdate %td

* comparisons use date constants, never strings
count if date >= td(01jan2015) & date < td(01jan2020)
```

The two failures here are a two-digit year read into the wrong century, which the `topyear` argument fixes, and a date variable left as a string, where "02/03/2019" sorts before "10/01/2015" and every comparison is wrong without warning.

6. **Merge with an expectation, and account for every `_merge` value.** The standard here is not this skill's. `data-profiling-and-cleaning` owns it: state an expected match rate before the merge, report the actual rate, and characterise the unmatched rows on observables rather than counting them. Read the reasoning there. What follows is how Stata executes it. `_merge` takes 1 for master only, 2 for using only, and 3 for matched. Every one of those three needs a stated disposition before the variable is dropped. The rule: tabulate first, decide second, assert third, and never let `keep if _merge == 3` be the first thing written.

```stata
merge m:1 muni_code year using "$data/clean/muni_controls.dta", generate(_m_muni)
tabulate _m_muni, missing

tabulate year if _m_muni == 1          // are the failures systematic?

* only after understanding it, state the rule and enforce it
assert _m_muni != 2                    // the using file should contain no extras
generate byte has_muni = _m_muni == 3
drop _m_muni
```

Use `1:1` for a merge onto a unique key on both sides, `m:1` for a lookup table, and `1:m` for the reverse. `m:m` is almost never what anyone wants: it pairs rows by position within key groups and produces results that depend on sort order. If you are reaching for `m:m`, either your key is wrong or you want `joinby`.

Zero matches on a merge that should have matched is almost always a key type mismatch, a string key against a numeric key, or padded against unpadded codes. Check with `describe` on both files before assuming the data is at fault.

7. **Use `joinby` when the combination is the point, and know the row count you expect.** `joinby` forms all pairwise combinations within each key group, which is correct for questions like matching every worker to every firm in their region. It is also how a 12,000-row dataset becomes 4 million rows. Compute the expected count before running it and assert it afterwards.

```stata
* expected rows = sum over regions of (workers in region * firms in region)
joinby region using "$data/clean/firms.dta"
assert _N == 386412
```

8. **Append with harmonised types and labels, and always keep a source variable.** Appending is where two waves of a survey silently disagree. If a variable is a string in one file and numeric in another, `append` will refuse or coerce; worse, if both are numeric with the same value label name but different meanings, the master's label wins and the using file's codes are relabelled without warning.

```stata
use "$data/interim/wave2021.dta", clear
generate int wave = 2021
append using "$data/interim/wave2022.dta", generate(from_2022)
replace wave = 2022 if from_2022 == 1
drop from_2022

* every variable present in only one wave is a harmonisation question, not a fact
misstable summarize, all
tabulate sector wave, missing
```

Cross-tabulate every recoded categorical against the wave variable after appending. A category that exists in only one wave is either a genuine change in the questionnaire, which belongs in the codebook, or a labelling error, which needs fixing.

9. **Reshape in one direction at a time, and assert the key afterwards.** `reshape long` needs a stub, the `i()` identifier, and the `j()` name; it fails when a variable varies within `i` but is not in the reshape list, and that failure is useful because it means you had two units of observation mixed in one file. `reshape wide` fails when `i` and `j` do not uniquely identify a row.

```stata
* wide to long
reshape long inc@ emp@, i(firm_id) j(year)
isid firm_id year
drop if missing(inc) & missing(emp)   // rows created for years never observed
```

The trap in `reshape long` is that it produces a complete rectangle of `i` by `j`, so a firm observed in three of eleven years gains eight rows of missing values, and the observation count in the summary statistics table is then whatever the estimation command happens to drop. Decide explicitly whether those rows should exist and delete them if not. `reshape` is also slow on large files; where it becomes the bottleneck, `greshape` from the gtools package does the same job faster, and the checks afterwards are identical.

10. **Establish uniqueness with `isid`, and resolve duplicates with a written rule.** Examine, write a rule, apply the rule, record how many cases it touched: that sequence is `data-profiling-and-cleaning`'s and the argument for it lives there. The Stata-specific hazard is that `duplicates drop` resolves ties by whatever sort order the file happens to be in, silently, so the surviving row is chosen by the file rather than by you.

```stata
duplicates report firm_id year
duplicates tag firm_id year, generate(dup)
list firm_id year employment revenue if dup > 0, sepby(firm_id) sortedby(firm_id year)

* an explicit tie-break, stated in the code and in the codebook
bysort firm_id year (revenue): keep if _n == _N   // keep the highest revenue record
isid firm_id year
```

Where duplicates are genuine conflicts rather than exact copies, the tie-break rule goes in the cleaning log and in the data section of the paper, with the number of affected rows.

11. **Handle missing codes at import, and use extended missing to preserve the reason.** Finding the sentinel codes is `data-profiling-and-cleaning`'s step and it explains why they are the most damaging silent defect there is. Converting them without losing the reason is Stata's, and so is the trap underneath: Stata's numeric missing values are larger than any number, so `if income > 50000` includes every missing value. That is the most frequently made mistake in the language and it produces a sample that is silently wrong rather than an error.

```stata
* recode source codes into extended missing, preserving what each meant
mvdecode income hours, mv(-99 = .a \ -98 = .b \ -97 = .c)
label define whymiss 1 "refused" 2 "don't know" 3 "not applicable"
notes income: .a refused, .b don't know, .c not applicable

* every comparison guards against missing
count if income > 50000 & !missing(income)
generate byte high_earner = income > 50000 if !missing(income)

misstable summarize income hours
misstable patterns income hours educ
```

Extended missing values `.a` to `.z` are all missing for estimation purposes but distinguishable for description, which is what lets you report separately how many respondents refused and how many were never asked. String missing is the empty string and is not `.`; a string variable full of `"NA"` is not missing until you make it so.

12. **Choose between `collapse` and `egen ... , by()` by asking whether the unit of observation changes.** `collapse` changes it and returns one row per group. `egen` keeps every row and adds a group-level column. Doing one when you meant the other is a unit-of-observation error and it survives into the estimates.

```stata
* changing the unit: person-year to municipality-year
collapse (mean) wage hours (sum) employed (count) n_obs = person_id, ///
    by(muni_code year)
label variable wage "Mean wage, municipality-year"   // collapse loses good labels

* keeping the unit: attach a group mean to every person-year row
bysort muni_code year: egen wage_muni = mean(wage)
bysort muni_code year: egen n_muni    = count(wage)
```

`collapse` computes each statistic over the observations that are non-missing for that variable, so different columns can be means over different samples. Where a consistent sample matters, use the `cw` option or restrict beforehand. `collapse` also discards variable labels, so relabel immediately afterwards or the clean file arrives unlabelled.

13. **Declare the panel and inspect its shape before estimating anything on it.** Panel coherence, meaning who enters, who leaves, whether identifiers persist and whether gaps sit inside a unit's series, is `data-profiling-and-cleaning`'s check and its account of why attrition is a result rather than a nuisance. `xtset` and `xtdescribe` are how that check is run in Stata. `xtset` requires the panel identifier and time variable to uniquely identify rows and the time variable to be a proper integer with an interpretable spacing.

```stata
xtset firm_id year
xtdescribe                        // pattern of participation, balance, gaps
xtsum lwage size                  // between and within variation
```

`xtdescribe` shows the participation patterns and how many units follow each. Gaps matter because the lag and lead operators respect real time: after a gap, `L.x` is missing, which is correct and which silently shrinks the estimation sample. Count the loss before you accept it.

```stata
generate byte has_gap = missing(L.year) & year != .    // conceptual check
count if missing(L.lwage) & !missing(lwage)
```

`tsfill` inserts rows for missing periods and `tsfill, full` balances the panel outright. Both change the row count, so use them only when the analysis genuinely requires a rectangle, and report the count change. For an unbalanced panel, record and report the number of units, the total observations, and the minimum, mean and maximum number of periods per unit; those four numbers belong in the data section.

14. **Compress, note, sign and save, and never over the raw file.** `compress` reduces storage types without losing information and often halves the file. Notes travel with the dataset and are the only documentation that cannot be separated from it. A data signature detects later change.

```stata
compress
notes drop _all
notes: Built by 03_clean.do on `c(current_date)' by `c(username)'.
notes: Sources: survey_2023.csv (received 2026-04-12), muni_controls.dta.
notes: Unit of observation: person-year. Key: person_id year.
notes: Income codes -99/-98/-97 recoded to .a/.b/.c.
datasignature set, reset
save "$data/clean/analysis_panel.dta", replace
describe, fullnames
codebook, compact
```

Where a coauthor runs an older Stata release, add a `saveold` copy rather than downgrading the project. Where the clean file will be read by anything outside Stata, export a csv alongside it and note that the labels do not travel with it.

## The build log

This is `data-profiling-and-cleaning`'s sample construction table, kept in Stata's vocabulary. That skill owns the requirement that every step between the raw row count and the estimation sample is counted and given a reason; the columns below are the version that fits Stata operations, and the counts recorded here fill in its merge report rather than starting a second one.

Every operation that can change the number of rows or units is recorded as it happens, with the counts either side. It cannot be reconstructed later from the code alone, because the counts are not in the code.

| Step | Operation | Rows before | Rows after | Units before | Units after | Check | Result |
| 1 | Import survey_2023.csv | 0 | 41,206 | 0 | 41,206 | `isid person_id` | pass |
| 2 | Append wave 2022 | 41,206 | 83,914 | 41,206 | 44,120 | `isid person_id year` | pass |
| 3 | Merge m:1 municipality controls | 83,914 | 83,914 | 44,120 | 44,120 | match rate 98.4% | 1,342 unmatched, listed below |
| 4 | Drop under 18 and over 65 | 83,914 | 71,558 | 44,120 | 38,904 | age range asserted | pass |
| 5 | Drop missing wage or hours | 71,558 | 66,201 | 38,904 | 36,880 | `misstable` rerun | pass |

## Worked example

**Situation.** A doctoral researcher was building a person-year panel from three annual waves of a national household survey, to be merged with a municipal administrative file holding local unemployment and public spending. The survey came as three csv files of roughly 41,000 rows each; the administrative file was an Excel workbook with one sheet per year and a two-row header. The final unit was to be person-year, with municipality controls attached.

**Task.** Produce a saved analysis file with a defensible observation count, within a week, with every dropped observation accounted for. The supervisor had asked one question in advance: how many people appear in all three waves.

**Action.** The first import used the Stata defaults, which read the municipality code as numeric. The merge to the administrative file then matched 89.4 percent of rows. That number was accepted for two days and used to build a first set of descriptives. The wrong turn was accepting it: 89 percent looks like ordinary attrition in an administrative match, and there was a ready explanation to hand, namely small municipalities missing from the spending file.

It was caught by tabulating the unmatched rows by municipality rather than counting them. Every unmatched code was under four digits. The survey codes were five-digit strings with a leading zero in one region, and reading them as numeric had removed it, so an entire region failed to match while everything else matched perfectly. The pattern was invisible in the match rate and obvious in the tabulation. Re-importing with `stringcols()` moved the match rate to 99.7 percent; the remaining 0.3 percent were three municipalities created by a boundary change, for which the statistical agency published a crosswalk.

Three further problems surfaced once the checks were systematic. Income carried minus ninety-nine for refusal and minus ninety-eight for don't know, both treated as values, which put mean income about 4 percent below the published figure, small enough to have passed unnoticed. `mvdecode` into `.a` and `.b` fixed it and preserved the distinction, which mattered because refusal correlated with the top of the distribution.

Employment status had been `encode`d separately in each wave. The 2021 extract contained no self-employed respondents, so alphabetical coding gave "Public sector" the code that "Self-employed" carried in the other two waves, and roughly 1,900 respondents changed sector between waves without changing jobs. Defining the label first and re-encoding removed it. Finally, the Excel import had used `firstrow` against a workbook whose first row was a title, so names came from the units row and two of the three sheets were read one row short; an explicit `cellrange` fixed it, confirmed against the published annual totals.

**Result.** The final file held 71,412 person-year rows on 38,904 individuals, of whom 21,663 appeared in all three waves. Every step from 124,000 raw rows to that number appeared in a build log table that went straight into the data section of the chapter with no rewriting. Total time was six days, of which two were spent on the wrong municipality codes and about half a day was the entire cost of the checks that would have prevented it.

### A second scenario, where it goes differently

A colleague on the same project received a single clean administrative extract from a national registry: one file, one year, 2.4 million firm records, with a published codebook, fixed field widths and documented missing codes. Almost none of the method above applied, because the source was already an analysis file maintained by a statistical agency: nothing to merge, nothing to append, nothing to reshape. The build reduced to five things in forty lines. Import with the published dictionary, verify the record count against the agency's published total, apply the documented missing codes, apply the published labels, `isid` on the firm identifier.

Two things did not reduce. The raw-file rule mattered more than usual, because the extract was licensed and could not be re-requested quickly. And `compress` mattered more than usual, taking the file from 3.1 gigabytes to 780 megabytes, which decided whether it could be worked on at all on the machine available. What generalises is that the size of a data management task is set by the number of sources and the number of unit-of-observation changes, not by the number of rows.

## Output

The deliverable is three things: a saved `.dta`, the build log table above, and a codebook entry for every constructed variable. The merge report is not a fourth: match rates recorded here go into the one `data-profiling-and-cleaning` defines, so a project has one merge report and not two.

```
data/clean/analysis_panel.dta
  Unit of observation : person-year
  Key                 : person_id year        (isid enforced)
  Rows                : 71,412
  Units               : 38,904 individuals, 2021 to 2023
  Panel               : unbalanced; T min 1, mean 1.84, max 3
  Built by            : code/03_clean.do, run 2026-09-06
  Sources             : survey_2021/22/23.csv; muni_controls.xlsx (sheet Panel)
  Signature           : datasignature set on save
  Missing conventions : .a refused, .b don't know, .c not applicable
```

Codebook rows for constructed variables:

| Variable | Label | Type | Definition | Source | Missing |
| `lwage` | Log real hourly wage, 2015 prices | double | `ln(income/hours)` deflated by national CPI | survey q22, q24 | 5,357 rows, mostly `.a` |
| `sector` | Sector of main job | byte | `encode` into fixed label `sector` | survey q31 | 212 rows |
| `unemp_muni` | Municipal unemployment rate | float | merged `m:1` on `muni_code year` | administrative file | 0 after crosswalk |

## Failure modes

**Identifiers read as numbers.** Recognise it by a merge failure concentrated in codes of one length, or by a distinct count of the identifier that is lower than expected. Fix by re-importing with `stringcols()`; do not attempt to restore leading zeros afterwards by padding, because you cannot tell how many were lost.

**`destring, force` used as the first attempt.** Recognise it because the code contains `force` and no count of what became missing. Fix with the generate-and-count pattern, and read the values that failed.

**`encode` applied independently to two files.** Recognise it by cross-tabulating the encoded variable against the file or wave indicator after appending; a category present in only one is the signal. Fix by defining the label once and encoding into it everywhere.

**`keep if _merge == 3` written before the tabulation.** Recognise it by the absence of a reported match rate. Fix by tabulating, characterising the unmatched rows on observables, and reporting both in the data section.

**`m:m` merges.** Recognise the command itself; there is no legitimate ordinary use. Fix by finding the real key, or by using `joinby` if the pairing is genuinely many to many.

**Missing values compared with an inequality.** Recognise it by searching the code for `>` and `>=` and checking each for a missing guard. Fix with `& !missing(x)`, and prefer generating indicators with `if !missing(x)` so the indicator is missing rather than zero.

**`reshape long` leaving a balanced rectangle.** Recognise it because the row count after reshaping is exactly the number of units times the number of periods. Fix by deciding explicitly whether unobserved periods should exist as rows, and dropping them if not.

**`collapse` used where `egen ... , by()` was meant.** Recognise it when the row count falls and a person-level variable has become a group mean. Fix by reverting to the pre-collapse file, which is why intermediate files are saved.

## Edge cases

**A source with no codebook and no documentation.** Reconstruct the meaning from the data, mark every inference as an inference in the notes, and do not recode anything you inferred without recording it. Where a variable's meaning cannot be established, keep it in the file unrecoded rather than guessing, and exclude it from the analysis.

**Identifiers that change over time.** A firm that is acquired, a municipality that splits. Use the publisher's crosswalk where one exists. Where none exists, construct one explicitly as a separate file with its own rule, never as an inline recode, because the crosswalk is a research decision that a referee may want to see.

**Data too large for memory.** Import once, keep only the variables you need, `compress`, and save an extract. Where even that fails, process in chunks by an outer variable such as year and append the compressed results, and never let the chunking change a computation that spans chunks, such as a within-person mean.

**A file received in a format Stata cannot read.** Convert with a documented, scripted step rather than by opening and re-saving in a spreadsheet application, which silently changes date formats and truncates long numeric codes. If a manual conversion is unavoidable, treat its output as a new raw file with its own provenance record.

**Survey data with weights and a complex design.** Set the design with `svyset` at the same time as the panel structure, and record the strata, primary sampling unit and weight variables in the file notes. A weighted mean computed without `svy` will not match the published figure, and that mismatch is the usual first sign that the design was never declared.

## Quality bar

- No file in `data/raw` was written to, and every raw file has a recorded provenance and date.
- Every merge reports its match rate, and each of the three `_merge` values has a stated disposition in the code.
- Every operation that can change the row count is followed by an `isid`, an `assert`, or a recorded count.
- Every variable in the saved file has a variable label, and every categorical has a value label defined in code rather than assigned alphabetically.
- Dates are numeric with a `%t` format, and no comparison in the project is made against a date string.
- Source missing codes are converted to extended missing values at import, and every inequality in the code guards against missing.
- The saved file carries notes recording its unit of observation, key, sources, build script and date, and `compress` was run before saving.
- The build log accounts for every observation between the raw row count and the estimation sample.

## Adapting this to your context

Two layers. The method: raw data stays read only, the unit of observation is named before any code, every step that can change the row count is checked, every merge reports its match rate, one script rebuilds the file from raw. The commands are dialect.

- **Checks.** `assert` and `isid` are Stata names. Use `stopifnot()` or `assertr` in R, a raised exception in Python, an explicit abort in SAS. What matters is that a failed check stops the run.
- **Merge outcomes.** `_merge` is Stata's. `dplyr` with `anti_join` for the unmatched, pandas `merge(indicator=True)`, SAS `MERGE ... IN=`, SPSS `MATCH FILES` with `IN=` give the same three counts. Report all three.
- **Identifiers as text.** `stringcols()` becomes `col_character()` in readr, `dtype=str` in pandas, a `$` informat in SAS. A dropped leading zero is unrecoverable in every language.
- **Missing codes and categories.** Extended missing `.a` to `.z` maps onto SAS special missings and SPSS user-missing values; R and Python have one NA, so carry the reason in a parallel column. `encode`'s alphabetical coding is the trap R factor levels and pandas categoricals share: declare levels in code.
- **What not to change.** Raw files stay read only, every drop is counted and logged with a reason, one script rebuilds the analysis file from raw. That is the method; the rest is syntax.

## Related skills

`data-profiling-and-cleaning` runs first and decides what needs fixing; this skill implements those decisions in Stata and adds the traps specific to it. `stata-do-file-craft` provides the do-file structure, logging and assertion discipline that this work sits inside, and `stata-project-scaffold` provides the folder layout. `data-section-writer` turns the build log and codebook into the paper's data section, and `descriptive-statistics-tables` produces the summary table from the saved file. `econometrician` takes the analysis file and chooses the estimator. `python-for-econometrics` gives the pandas equivalents of these operations for projects that are not in Stata. `analysis-audit` checks, from the outside, that the file the tables were built from is the file the code produces.
