---
name: python-for-econometrics
description: Runs an empirical economics project in Python to the same standard a Stata project is held to, and says honestly when Python is the wrong tool. Covers project layout with scripts rather than notebooks, a pinned and lockfiled environment, pandas operations mapped one by one onto their Stata equivalents with the silent traps named, estimation with statsmodels, linearmodels and the fixed effects packages, clustered and robust covariance including the sample alignment trap, seeded generators rather than global random state, testing a data pipeline, and exporting tables and monochrome figures that match the house standard. Use this skill when someone is doing econometrics in Python, converting a project between Stata and Python, asking how to cluster standard errors in Python, how to do a Stata command in pandas, why a merge lost rows, how to make a notebook reproducible, or whether to use Python or Stata for a piece of work. Trigger also on vague requests such as "should I do this in Python", "my notebook gives different numbers now", or "translate this do-file".
---

# Python for Econometrics

The failure this prevents has two halves. The first is a Python analysis that quietly loses data. A `merge` written without `how` defaults to an inner join and drops every unmatched row without a message; a `groupby` drops rows whose key is missing unless told not to; a chained assignment writes to a copy and the intended change never lands. Stata raises an error or leaves a `_merge` variable behind for most of these. Pandas returns a smaller DataFrame and no warning, and a smaller DataFrame looks exactly like a correct one.

The second half is the notebook that cannot be run again. It produced Table 3 in March, in cell order that no longer exists, against library versions nobody recorded, with a random seed set in a cell that was later deleted. In September the same notebook gives different numbers, and there is no way to establish which set was in the submitted paper. Stata projects fail this way too, but Python makes it easier, because the environment is a moving target and the notebook interface actively encourages running cells out of order.

The cost is the same in both cases: numbers that cannot be defended. What is different about Python is that the defences are not defaults. They have to be written in, and this skill is what to write in.

## When to use this, and when not to

Use it when the project is in Python and has to meet a publication standard, when a project is moving between Python and Stata in either direction, when a pandas operation is behaving differently from its Stata equivalent, when standard errors need to be clustered or bootstrapped in Python, and when the choice of language is still open.

Use it especially at the point where an exploratory notebook is about to become the source of a number in a document. That transition is where nearly all of the damage happens.

Do not use it to decide the estimator, the clustering level or the inference method, which is `econometrician`; this skill implements those decisions in a particular language. Do not use it for a Stata project, where `stata-do-file-craft` and `stata-data-management` are the equivalents. Do not use it for figure design, which is `academic-figures-monochrome`, or table typography, which is `academic-tables-booktabs`; this skill covers only how to generate them from Python without hand editing. Do not use it to assemble the deposit archive, which is `replication-package`.

## What you need before starting

**The Python version and an environment manager.** Not a list of imports. Missing: create the environment before writing any analysis code and pin the interpreter version, because an environment created later cannot be made to describe code that already ran.

**The list of estimation packages the analysis needs, with versions.** Estimation packages change defaults between releases more often than people expect, including default covariance estimators. Missing: install what you need, then lock immediately and record the lock in the run log.

**Who else has to run this, and on what.** A coauthor on Windows, a journal data editor, a secure server with no internet. Missing: assume a stranger on a clean machine with no internet, and prefer packages that install from a lockfile without compilation.

**The data, its size, and where it lives.** This decides whether pandas is adequate, whether an out-of-core tool is needed, and whether the data can travel at all. Missing: check the file size and the row count before choosing an approach, because the decision is different above and below roughly the machine's memory.

**Whether an equivalent Stata pipeline exists or is expected.** Missing: ask, because parallel implementations in two languages are a maintenance burden that is only worth carrying when the numbers are being cross-checked deliberately.

**The estimator and the inference method, already decided.** Missing: stop and get them from `econometrician`. Choosing an estimator because a Python package makes it convenient is how projects end up with an estimator nobody can justify.

## The method

1. **Write scripts, not notebooks, for anything that produces a result.** Notebooks are legitimate for exploration and for communicating a finished analysis. They are not a pipeline, because their execution order is not their reading order and their state is invisible. The rule: a notebook may read the outputs of the pipeline; it may not be a step in it. Where a notebook must be kept, pair it with a script that reproduces its outputs and treat the script as authoritative.

```
project/
  pyproject.toml          dependencies, pinned
  uv.lock                 exact resolved versions, committed
  .python-version         interpreter version
  Makefile                or run_all.py; the single entry point
  src/
    config.py             ROOT and derived paths, nothing else
    s01_import.py
    s02_clean.py
    s03_construct.py
    s04_sample.py
    s05_descriptives.py
    s06_main.py
    s07_robustness.py
    s08_figures.py
    checks.py             assert_unique, assert_no_loss, assert_range
    tables.py             one export function per table style
    plotting.py           the house rcParams and figure helpers
  tests/
    test_checks.py
    test_construct.py
  data/raw  data/interim  data/clean
  output/tables  output/figures  output/logs
```

2. **Pin the environment and commit the lockfile.** A `requirements.txt` written by hand is a wish list; a lockfile is a record. Any of the modern tools produce one. Record the resolved versions into the run log as well as the lockfile, because the log is what travels with the results.

```python
# src/config.py
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA, OUT = ROOT / "data", ROOT / "output"
RAW, CLEAN = DATA / "raw", DATA / "clean"
SEED = 20260906
```

`Path(__file__).resolve().parents[1]` is the Python equivalent of the single machine-specific line in a Stata master do-file, and it is better because there is no line to edit. Nothing else in the project constructs a path from a string.

3. **Log every run to a timestamped file, and record the environment in it.** The standard library's `logging` module is sufficient and needs no dependency.

```python
import logging, sys, time, platform
from importlib.metadata import version

stamp = time.strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler(OUT / "logs" / f"run_{stamp}.log"),
              logging.StreamHandler(sys.stdout)],
)
logging.info("python %s on %s", platform.python_version(), platform.platform())
for p in ("pandas", "numpy", "statsmodels", "linearmodels", "pyfixest"):
    logging.info("%s %s", p, version(p))
logging.info("seed %s", SEED)
```

4. **Translate Stata operations deliberately, and add the guard that Stata gives you for free.** The table below is the working map. The third column is the part that matters: in nearly every row, the pandas default is more permissive than the Stata default, and the difference is silent.

| Stata | pandas | The guard you must add |
| `use` / `save` | `pd.read_parquet` / `to_parquet` | Use Parquet, not pickle: pickle is version-fragile and unreadable outside Python. Parquet preserves dtypes and categories |
| `merge 1:1 id year` | `left.merge(right, on=[...], how="left", validate="one_to_one", indicator=True)` | Default `how="inner"` drops unmatched rows silently and default validation is many-to-many. Always pass `how`, `validate` and `indicator`, then tabulate the indicator |
| `append` | `pd.concat([a, b], ignore_index=True)` | Mismatched dtypes coerce to `object`; categoricals with different category sets become object. Harmonise dtypes first and add a source column |
| `reshape long` | `pd.wide_to_long` or `df.melt` | Neither creates the balanced rectangle Stata does, which is usually an advantage; check the row count against expectation either way |
| `reshape wide` | `df.pivot` | Use `pivot`, not `pivot_table`: the latter silently averages duplicates instead of raising |
| `collapse` | `df.groupby(keys, dropna=False, observed=True).agg(...)` | `dropna=True` is the default and discards rows with a missing key. `observed=False` on categoricals produces empty groups |
| `bysort ...: egen` | `df.groupby(keys)[col].transform("mean")` | Same defaults apply; `transform` preserves row count, `agg` does not |
| `isid id year` | `assert not df.duplicated(["id", "year"]).any()` | There is no built-in; write it into `checks.py` and call it |
| `encode` | `pd.Categorical(s, categories=[...], ordered=False)` | Passing categories explicitly is the equivalent of encoding into a predefined label; without it the codes follow the observed data |
| `destring` | `pd.to_numeric(s, errors="coerce")` | This is `destring, force`. Count the new NaNs and inspect the strings that failed before accepting it |
| Missing comparison | `np.nan`, `pd.NA` | Stata missing is larger than any number, so `x > 1000` includes it; NumPy NaN comparisons are False, so `x > 1000` excludes it. The two languages give different samples from the same line and both are silent |
| `xtset id year` | `df.set_index(["id", "year"])` | linearmodels reads panel structure from the index; a non-unique index fails late and confusingly. Assert uniqueness first |
| `tsfill` | `df.reindex(full_index)` | Explicit and visible, which is better; check the row count change |
| `compress` | downcast numerics, `astype("category")` | Do it before writing Parquet; it changes file size and read time substantially |
| Editing in place | `df.loc[mask, col] = value` | Chained assignment such as `df[mask][col] = value` writes to a copy. Newer pandas raises on this; older versions warn or do nothing |

5. **Estimate with a package that implements the covariance you need rather than assembling it yourself.** Three libraries cover almost everything an applied paper needs, and choosing between them is mostly about the fixed effects.

```python
# statsmodels: cross-section, GLM, Poisson, flexible formulas
import statsmodels.formula.api as smf

est = df.dropna(subset=["lwage", "treat", "age", "state"]).copy()
m = smf.ols("lwage ~ treat + age + I(age**2) + C(year)", data=est).fit(
    cov_type="cluster", cov_kwds={"groups": est["state"]}
)
```

The subtle failure there is the reason for the `dropna` line. Statsmodels drops rows with missing values in the formula variables, but the `groups` array you pass is built from the frame you handed it, so if that frame is larger than the estimation sample the cluster assignment is misaligned and the standard errors are wrong without an error being raised. Build the estimation frame explicitly first, then take the groups from the same frame. This single trap accounts for a large share of wrong standard errors in Python papers.

```python
# linearmodels: panel estimators and instrumental variables
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS

d = est.set_index(["worker_id", "year"])
assert d.index.is_unique
pan = PanelOLS.from_formula(
    "lwage ~ treat + age + EntityEffects + TimeEffects", data=d
).fit(cov_type="clustered", clusters=d["state"])

iv = IV2SLS.from_formula(
    "lwage ~ 1 + age + [adopt ~ distance]", data=est
).fit(cov_type="clustered", clusters=est["state"])
print(iv.first_stage)
```

```python
# pyfixest: high-dimensional fixed effects, Poisson with fixed effects,
# wild cluster bootstrap, and table export in one place
import pyfixest as pf

f1 = pf.feols("lwage ~ treat | worker_id + year", data=est, vcov={"CRV1": "state"})
f2 = pf.feols("lwage ~ treat + age | worker_id + year", data=est, vcov={"CRV1": "state"})
f1.wildboottest(param="treat", reps=9999)          # for few clusters
pf.etable([f1, f2], type="tex", file_name=OUT / "tables" / "tab03_main.tex")
```

Two-way clustering, heteroskedasticity-robust variants and bootstrap options exist in all three libraries under different names and different defaults. Read the default before relying on it: a `cov_type` left unspecified is not the same choice in statsmodels as in linearmodels.

6. **Seed explicitly with a generator object, not with global state.** `np.random.seed` sets a global that any library can consume or reset, so results become dependent on import order and on which cells ran. A generator passed as an argument is reproducible and testable.

```python
import numpy as np
rng = np.random.default_rng(SEED)
draws = rng.choice(df.index, size=1000, replace=False)
```

Pass `random_state` explicitly to any scikit-learn object, seed the bootstrap in whichever estimation package performs it, and record every seed in the log. Where an operation depends on row order, sort on a genuinely unique key first; `groupby` preserves order within groups and `sort_values` is not stable unless you ask for `kind="stable"`.

7. **Test the pipeline, which mostly means testing the transformations and asserting the invariants.** A data pipeline is testable in a way a regression is not: the functions that construct variables take a small DataFrame and return a known answer.

```python
# src/checks.py
def assert_unique(df, keys):
    dupes = df.duplicated(keys).sum()
    if dupes:
        raise ValueError(f"{dupes} duplicate rows on {keys}")
    return df

def assert_no_loss(before, after, name):
    if len(after) != len(before):
        raise ValueError(f"{name}: {len(before)} rows in, {len(after)} out")
    return after

# tests/test_construct.py
import pandas as pd
from src.s03_construct import real_hourly_wage

def test_real_hourly_wage_deflates_and_divides():
    d = pd.DataFrame({"income": [2000.0], "hours": [100.0], "cpi": [1.25]})
    out = real_hourly_wage(d)
    assert out.loc[0, "wage_real"] == 16.0

def test_zero_hours_gives_missing_not_inf():
    d = pd.DataFrame({"income": [2000.0], "hours": [0.0], "cpi": [1.0]})
    assert pd.isna(real_hourly_wage(d).loc[0, "wage_real"])
```

The second test is the kind that earns its keep: division by zero gives `inf` in pandas rather than an error, and `inf` survives into a mean and destroys it. Add a smoke test that runs the whole pipeline on a one percent sample so a structural break is caught in seconds rather than at the end of a long run.

8. **Export tables and figures from code, to the house standard, with no hand editing.** For tables, `pyfixest.etable` and the stargazer-style packages both produce LaTeX and Word output; where neither fits the required layout, write one function that takes the fitted models and emits the LaTeX body, and keep it in `tables.py`. The rules about what belongs in the table and in its note are in `regression-table-production`, and they are language independent.

For figures, put the house style in one place and import it everywhere. Monochrome first: series are separated by marker shape, dash pattern and hatch texture rather than by colour, the legend sits outside the plot area, and accent colour appears only where one series must be singled out.

```python
# src/plotting.py
import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.figsize": (6.5, 4.0), "figure.dpi": 200,
    "font.size": 10, "axes.grid": False,
    "axes.spines.top": False, "axes.spines.right": False,
    "savefig.bbox": "tight", "pdf.fonttype": 42,
})

STYLES = [
    {"color": "black", "linestyle": "-",  "marker": "o", "markerfacecolor": "white"},
    {"color": "black", "linestyle": "--", "marker": "s", "markerfacecolor": "black"},
    {"color": "0.45",  "linestyle": ":",  "marker": "^", "markerfacecolor": "white"},
]

def legend_outside(ax, ncol=1):
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0),
              frameon=False, ncol=ncol)
```

Save figures as PDF for LaTeX and as high-resolution PNG only where a format demands it. Never save a figure that was tweaked in a viewer.

9. **Decide the language per task, not per project, and write the decision down.** The comparison below is the honest one, across the three languages that actually compete for this work. It changes over time, and the entries where Python has been catching up fastest are the fixed effects and difference-in-differences estimators.

R belongs in this comparison and is left out of most Stata-versus-Python arguments for no better reason than that economics adopted the other two first. Outside economics it is frequently the default: psychology, ecology, biostatistics, epidemiology and increasingly education and sociology run on it. For applied microeconometrics specifically, `fixest` is the fastest high-dimensional fixed effects estimator in any of the three, `did` and `didimputation` implement the heterogeneity-robust difference-in-differences estimators, `sandwich` and `clubSandwich` cover robust and small-sample cluster-robust variance, `survey` is a genuine equivalent of Stata's `svy` suite, `lme4` and `nlme` are the reference implementations for multilevel and mixed models, `lavaan` for structural equation models, and `ggplot2` for figures. On reproducibility, `renv` does what a lockfile does and `targets` does what a master do-file does. R is also free, which matters for the same reasons Python being free matters.

| Task | Better tool now | Why |
| Panel fixed effects, instrumental variables, standard difference-in-differences | Stata or R | Stata for defaults referees expect; R's `fixest` is faster than either alternative and its syntax is closer to the algebra. Python's `pyfixest` and `linearmodels` are close and closing |
| Heterogeneity-robust staggered difference-in-differences | R, narrowly | The new estimators tend to appear as R packages first, then Stata, then Python |
| Survey design estimation with strata, clusters and finite population correction | Stata or R | Stata's `svy` suite and R's `survey` package are both validated implementations. Python has no complete equivalent, and reimplementing it is a way to get a published statistic wrong |
| Multilevel and mixed models, structural equation models, item response and measurement models | R, clearly | `lme4`, `nlme`, `lavaan`, `mirt`. Stata's `mixed` and `sem` are capable; Python's are thin. This is the row that matters most for readers outside economics |
| Postestimation margins, predicted probabilities, contrasts across complex models | Stata or R | Stata's `margins`, or R's `marginaleffects` and `emmeans`, which now cover most of the same ground. Both require substantial custom work in Python |
| Data larger than memory | Python | Out-of-core and columnar tools handle it; Stata requires the data to fit or to be chunked by hand |
| Text, documents, web sources, APIs | Python, decisively | Not a contest |
| Publication figures | R or Python | `ggplot2` and matplotlib both do it well and both are scriptable. Stata is workable and more effort per figure |
| Literate documents combining code, tables and prose | R, narrowly | Quarto and R Markdown are mature and widely used for supplements and theses; Quarto also runs Python |
| Simulation, custom estimators, anything requiring a written likelihood or a bootstrap of an unusual statistic | Python | Faster to write, easier to test, and the result is a function you can unit test |
| Machine learning inside a causal design, including cross-fitting and double machine learning | Python | The libraries and the sample-splitting machinery live there |
| Reproducible environments | Python | Lockfiles pin every dependency exactly; Stata pins the language but not the user-written packages, which have to be shipped by hand |
| Cost and access | Python | No licence, which matters for coauthors without one, for students, and for anyone reproducing the work |
| Team familiarity and referee familiarity | Whichever the team has | A language nobody on the project can debug is the wrong language regardless of its merits |

The rule that decides most cases: choose the tool that requires the fewest lines of code you have to write yourself, because every custom line is a line that can be wrong and that nobody will check. A project that reimplements survey weighting or `margins` in pandas has chosen wrong. A project that scrapes 40,000 documents with a Stata shell command has also chosen wrong. A project that writes its own mixed model likelihood in Python because the team does not know R has also chosen wrong.

Mixed projects are legitimate and often correct, and this holds across all three languages. Do the data assembly in whichever language handles the sources, hand over a documented Parquet or `.dta` file, which all three read and write, and do the estimation in whichever language has the estimator. Document the handoff file as an interface with its unit of observation and key, and make the handoff a step in the pipeline rather than a manual export.

## Worked example

**Situation.** A team was studying whether firms that win public contracts subsequently grow. The contract data existed only as 41,000 tender notices published as web pages, with no bulk download. The outcome data were an annual firm panel of 220,000 firms over eleven years, already held as a `.dta` file. Two of the three researchers worked in Stata; one worked in Python.

**Task.** Build the linked dataset and estimate a panel fixed effects specification with clustering at the sector level, in six weeks, with a result that the Stata users could rerun and check.

**Action.** The scraping and parsing were never in doubt: Python, with the raw HTML archived to disk before any parsing, so the parsing could be rerun without re-scraping. That decision paid for itself twice when the parser was corrected.

The linkage was done in pandas and this is where the first failure occurred. The initial merge of the parsed tenders to the firm registry was written as `tenders.merge(firms, on="tax_id")`, which defaults to an inner join. It returned 37,800 rows from 41,000 tenders and the team read that as a 92 percent match rate, which sounded reasonable. Adding `how="left"`, `validate="many_to_one"` and `indicator=True` showed something different: the `validate` argument raised immediately, because the registry contained 61 tax identifiers twice, from firms that had re-registered after a legal form change. The inner join had been silently duplicating rows for those firms and dropping the unmatched ones in the same operation, so the 92 percent figure was two errors partially cancelling.

The second failure was the standard errors. The first estimation used statsmodels with `cov_kwds={"groups": df["sector"]}` where `df` was the full frame, while the formula dropped 4,900 rows with missing lagged employment. The cluster labels were therefore offset against the estimation sample. It did not raise an error and it produced plausible standard errors that were wrong. It was caught only because the same specification was run in Stata as a cross-check and the standard errors differed by about 15 percent. The fix was to build the estimation frame with an explicit `dropna` and take the groups from it, after which the two languages agreed to four decimal places.

The wrong turn worth recording came later. The paper needed a subgroup analysis using the official survey weights and strata from a firm survey used for one robustness table. The Python-based researcher began implementing stratified variance estimation by hand. Two days in, the estimates still did not match the published aggregates from the statistical agency. That work was abandoned and the robustness table was produced in Stata with `svyset` and `svy: mean` in about twenty minutes, matching the published figures on the first attempt. The general lesson was written into the project's README: any statistic that a statistical agency also publishes must be reproduced using a tool whose implementation has been validated, and reimplementation is a research project in its own right.

The environment was pinned from the start with a lockfile, and the run log recorded package versions. That mattered in week five, when a pandas upgrade on one machine changed the behaviour of a chained assignment from a warning to an error, which was a genuine bug in the cleaning code that the older version had been hiding.

**Result.** The pipeline ran end to end in 34 minutes, excluding the scrape, and the two Stata users could rerun the estimation from the handoff Parquet file. Two tables were produced in Python and one in Stata, all from code, with the handoff file documented as an interface. The team's estimate of time lost to the two silent pandas failures was about four days, and the cost of the cross-language check that caught the second one was under an hour.

### A second scenario, where it goes differently

A doctoral student with an entirely conventional project, a balanced country-year panel of 46 countries over 24 years with a fixed effects specification and no unusual data sources, asked whether to convert the project from Stata to Python because a referee had mentioned reproducibility.

The answer was no, and the reasoning is worth stating because the request is common. Nothing in the project needed Python. Every estimator was one line of Stata, the survey and postestimation tools were in use, and neither the student nor the supervisor could debug Python under deadline. Converting would have introduced translation risk into a working analysis in exchange for no capability.

What the referee actually wanted was reproducibility, which is a different thing from a language. That was delivered inside Stata: a master do-file, a timestamped log, user-written packages installed into a project-local directory with their versions recorded, a clean-session test, and a deposited archive. The one Python element added was a short script that read the exported estimates and rebuilt the figures to the house monochrome standard, because matplotlib gave finer control over the event study plot than the alternative and that script was small enough for the supervisor to check line by line.

What changed between the two scenarios was not preference. It was whether any task in the project actually required the capabilities Python has and Stata does not.

## Output

The deliverable is a repository that a stranger can clone, install and run in three commands, plus the run record.

```
$ uv sync                 # or: pip install -r requirements.lock
$ make all                # or: python -m src.run_all
$ ls output/tables output/figures
```

The run record, written to the log and reproduced in the replication README:

| Field | Value |
| Entry point | `make all` |
| Python | 3.12.7 |
| Key packages | pandas 2.2.3, numpy 2.1.2, statsmodels 0.14.4, linearmodels 6.1, pyfixest 0.25.3 |
| Lockfile | `uv.lock`, committed, resolved 2026-08-14 |
| Seed | 20260906, passed to `default_rng`; bootstrap seeds logged per call |
| Runtime | 34 minutes on 8 cores, 32 GB |
| Inputs | `data/raw/tenders_html/` (41,206 files), `data/raw/firm_panel.dta` |
| Outputs | 7 tables, 5 figures, listed with their producing script |
| Tests | 24 unit tests, 1 smoke test on a one percent sample, all passing |
| Cross-checks | Table 3 column 3 reproduced in Stata; agreement to 4 decimal places |

Each output file is mapped to the script and the paper exhibit that uses it, which is the manifest `replication-package` expects.

## Failure modes

**Merges without `how`, `validate` and `indicator`.** Recognise it by searching for `.merge(` and checking each call for all three arguments. Fix by adding them and tabulating the indicator; the row count before and after belongs in the log.

**Cluster groups misaligned with the estimation sample.** Recognise it when the standard errors differ from an equivalent estimate elsewhere, or when the length of the groups array does not equal the model's number of observations. Fix by constructing the estimation frame with an explicit `dropna` and taking the groups from that frame.

**Notebooks as pipeline steps.** Recognise it when reproducing a result requires running cells in a particular non-linear order. Fix by moving every step that writes an output into a script.

**No lockfile.** Recognise it when the repository has a `requirements.txt` with no version pins or with loose ones. Fix by locking, committing the lock, and recording the resolved versions in the run log.

**`np.random.seed` for reproducibility.** Recognise it by the call itself. Fix with a generator object passed explicitly, and by passing `random_state` to every library object that accepts one.

**Chained assignment.** Recognise it by `df[mask][col] = value` or a `SettingWithCopyWarning` in the log. Fix with `.loc`, and treat the warning as an error rather than filtering it out.

**Silent aggregation from `pivot_table`.** Recognise it when a reshape succeeds on data you expected to have duplicates. Fix by using `pivot`, which raises, and resolving the duplicates explicitly.

**`groupby` dropping missing keys.** Recognise it by comparing the summed group sizes against the row count. Fix with `dropna=False` and an explicit decision about the missing category.

**Reimplementing an established procedure.** Recognise it when a hand-written function is being validated against a published figure and not matching. Fix by using the validated implementation, in whichever language it lives, and documenting the handoff.

**Pickle as a storage format.** Recognise it by `.pkl` files in `data/`. Fix by moving to Parquet, which is versioned, typed, portable and readable outside Python.

## Edge cases

**Data too large for memory.** Move the heavy filtering and aggregation into a columnar engine or a database and bring only the analysis extract into pandas. Keep the query in version control as part of the pipeline; a query typed into a console is the same failure as an interactive edit in Stata.

**A journal data editor who does not accept Python.** Rare and shrinking, but check the policy before submission rather than after. Where it happens, the handoff-file structure is the answer: deliver the cleaned analysis file plus estimation code in the accepted language, and deposit the Python assembly code as supplementary material with its lockfile.

**A coauthor who will only open a notebook.** Give them a notebook that imports the pipeline modules and calls them, so the notebook is a viewer and the logic stays in tested functions. Never let logic accumulate in cells.

**An estimator that exists in Stata or R and not in Python.** Do not reimplement it under deadline. Either call it through a documented handoff, or choose a different estimator and justify the choice on its own merits, not on tooling convenience. Multilevel models, structural equation models and survey variance estimation are the three cases where this comes up most, and R has all three.

**Results that differ between Stata, R and Python for the same specification.** Investigate rather than choosing. The usual causes, in order of frequency, are a different default covariance estimator, a different treatment of missing values, a different degrees-of-freedom correction for clustering, and a different reference category for a factor variable. R's `sandwich` and Stata's `robust` differ by a finite-sample correction by default, which accounts for a large share of the small discrepancies people report. All are findable in under an hour and all have a right answer.

**Long-running estimation inside a pipeline.** Cache the fitted results to disk keyed on a hash of the inputs and the specification, so downstream table building can be rerun without refitting, and make the cache invalidate on any input change rather than on a manual flag.

## Quality bar

- The pipeline runs from a clean checkout in one command, on a machine that has never seen the project.
- The environment is locked, the lockfile is committed, and the resolved versions appear in the run log.
- Every merge specifies `how`, `validate` and `indicator`, and its row counts are logged.
- The cluster or group array passed to any covariance estimator comes from the same frame the model was fitted on.
- Every random draw comes from a seeded generator passed explicitly, and every seed appears in the log.
- The transformation functions have unit tests, and the pipeline has a smoke test on a small sample.
- Tables and figures are written by code, never edited afterwards, and figures follow the monochrome standard with the legend outside the plot area.
- The language choice for each part of the project is written down with its reason, and no established published procedure has been reimplemented by hand.

## Adapting this to your context

This is written for applied microeconometrics in Python against Stata, because that is the comparison economics arguments actually have. The engineering discipline is language-neutral; the package names are not.

- **The whole pipeline, in R.** Step for step: `here::here()` replaces `config.py`; `renv::snapshot()` writes the lockfile; `targets` or a plain `run_all.R` is the master script; `dplyr` or `data.table` replaces pandas, with `left_join(relationship = "one-to-one")` as the guard `validate=` gives you; `fixest::feols` replaces `pyfixest` and `linearmodels`; `sandwich` and `clubSandwich` replace the covariance arguments; `testthat` replaces `pytest`; `modelsummary` or `fixest::etable` writes the tables; `ggplot2` and `ggsave` the figures; `set.seed()` at the top of each script.
- **The estimator set.** A causal inference set. For multilevel models, structural equation models or item response theory, R is where they live: `lme4`, `lavaan`, `mirt`. Mplus is still the reference for complex latent variable models.
- **The Stata to pandas map.** Read it as a map of silent defaults. Base `merge()` in R defaults to an inner join, and `dplyr` joins expand many-to-many unless `relationship` is set.
- **SPSS and SAS shops.** The reproducibility rules hold unchanged: syntax files rather than menus, one entry point, no result from a dialog box.
- **What not to change.** A result comes from a script that runs end to end in a clean session, environment pinned and seed set, and no number reaches the paper by hand.

## Related skills

`econometrician` decides the estimator, the clustering and the inference that this skill implements. `stata-do-file-craft` and `stata-data-management` are the equivalents for a Stata project and the reference points for the translation table here. `regression-table-production` specifies what belongs in the exported tables, and `academic-tables-booktabs` their typography. `academic-figures-monochrome` sets the figure standard that `plotting.py` encodes. `replication-package` takes the locked environment and the manifest and assembles the deposit. `analysis-audit` verifies from the outside that the numbers in the paper came from this pipeline.
