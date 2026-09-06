---
name: replication-package
description: Assembles the replication package for a paper or thesis so a stranger can reproduce every table and figure from the raw data with one command: folder structure, a README that documents the run, data availability and access instructions, code cleaned of absolute paths and secrets, environment and package versions, a run log, and compliance with journal data policies and repository requirements. Use this skill whenever a researcher asks to prepare code and data for submission, "make my project reproducible", build a replication package, respond to a journal's data editor, deposit code and data, or clean up a project before sharing it with a coauthor. Trigger before every submission to a journal with a data policy and before every thesis deposit.
---

# Replication Package

Reproducibility is not a virtue added at the end; it is the property that a project either has or does not. A replication package makes it verifiable: a person with no access to the author can run one command and regenerate every number in the paper. This skill builds that package and tests it.

## Standard structure

```
paper-short-name-replication/
  README.md
  LICENSE
  data/
    raw/           original files or instructions to obtain them
    clean/         analysis files produced by the code
  code/
    00_master.*    runs everything in order
    01_...         numbered scripts, one per stage
    environment    package list with versions (requirements.txt, renv.lock, or a Stata package list with versions and install commands)
  output/
    tables/
    figures/
    logs/
  docs/
    codebook.md
    data_availability.md
    manifest.csv   every output file mapped to its script and to the paper's table or figure number
```

If the project was built with the stata-project-scaffold conventions, most of this exists already; the package is the cleaned copy plus the documentation and the test run.

## The README

The README is the document the data editor reads first and the replicator reads last; write it for both.

1. **Overview**: the paper's citation, what the package reproduces, and the total run time and hardware needed.
2. **Data availability**: for each dataset, whether it is included, its source, its license, how to obtain it if not included (exact URL or agency, form, expected wait), and any transformation applied before inclusion. If data cannot be shared, say why and provide a synthetic or simulated dataset with the same structure so the code can be run, clearly labeled.
3. **Software requirements**: language and version, packages with versions, operating system tested on, and the install commands.
4. **Instructions**: the one command that runs everything, and how to run a single stage. Expected outputs and where they appear.
5. **Mapping**: a table linking every table and figure in the paper to the script and output file that produces it (the manifest).
6. **Notes**: random seeds, known non-determinism, run time per stage, and any manual step (there should be none; if one exists, it is documented and justified).

## Cleaning the code

- No absolute paths; one root variable set in the master script.
- No credentials, API keys, or personal information in code or logs.
- Every script has a header: purpose, inputs, outputs.
- Dead code and abandoned experiments removed; the package contains what the paper uses.
- Package installation handled by the master script or the environment file, not assumed.
- Output written to the output folders, never to the working directory.
- Random seeds set wherever randomness enters (bootstrap, matching, sampling).

## The test run

The package is not finished until it has been run from scratch:

1. Copy the package to a clean location (or a fresh environment) with only the raw data present.
2. Run the master script.
3. Compare every output to the numbers in the submitted manuscript, table by table, using the manifest. Any discrepancy is a finding to fix before submission; it usually means a table in the paper was edited by hand.
4. Record the run log and the comparison in `docs/`.

Where a clean environment is available in the session, perform the test run; otherwise, provide the exact procedure and a checklist for the user.

## Journal and repository compliance

Fetch the target journal's data and code policy and the repository's requirements (many journals require deposit in a specific repository with a DOI, a data availability statement in the paper, and a license). Produce the compliance checklist: license chosen, DOI obtained, statement text for the paper (coordinate with data-section-writer), metadata filled, embargo handled if required.

## Confidential and restricted data

Document the access process in detail, include the code that would run on the restricted data, include a synthetic dataset for testing, and, where the data provider allows, include summary statistics of the real data so the replicator can check the synthetic structure. State what a replicator can and cannot verify.

## Quality bar

- One command reproduces every table and figure from raw data.
- The manifest maps every paper exhibit to a script and an output file.
- The test run from a clean location matched the manuscript, and the log is included.
- No absolute paths, credentials, or manual steps.
- The README answers every question a data editor asks.
