# ChEMBL Glucagon-like peptide 1 receptor (GLP-1) Bioactivity Dataset

An exploratory data analysis (EDA) of the bioactivities reported in the ChEMBL database for the Glucagon-like peptide 1 receptor (GLP-1) target.

## Project Overview

This repository contains a Jupyter Notebook analysing an extract of the ChEMBL database covering all reported bioactivities for the GLP-1 target. This target is associated with the GLP-1 class of blockbuster weight-loss drugs.

The core question driving the analysis: **do simple molecular descriptors (AlogP, Molecular Weight) predict receptor potency in this dataset?** In practice, most of the analytical effort went into diagnosing and resolving data quality issues in the raw ChEMBL export before that question could be answered.

## Data Source

EBI-ChEMBL database — Target CHEMBL1784

- https://www.ebi.ac.uk/chembl/
- https://www.ebi.ac.uk/chembl/explore/activities/STATE_ID:3gjC0SVT3LlwiY5hwBTIGg%3D%3D

## Analysis Approach

The analysis follows a five-step EDA methodology, run in sequence in the main notebook:

1. **Structural audit** - schema, datatypes, missing values, duplicates, and unit/measurement-type consistency. This step revealed the key data quality finding: the raw export mixes three distinct assays, two of which measure opposite receptor pharmacology (agonist vs. inverse agonist). The dataset is filtered to the single largest assay.
2. **Univariate analysis** - distribution of the potency measure (`Standard Value`), including investigation of a large cluster of values at a single concentration (28183.8 nM), identified as a placeholder artifact rather than an actual measurement and excluded accordingly.
3. **Bivariate analysis** - correlation between numeric columns (`Value` vs `Standard Value`; `#RO5 Violations` vs `AlogP`/`Molecular Weight`), including identification of redundant/derived columns.
4. **Multivariate analysis** - relationship between AlogP, Molecular Weight, and potency across the cleaned dataset.
5. **Pipeline integrity diagnostics** - audit of constant/zero-variance columns, derived/redundant columns, sparse columns, and a set of reusable schema-verification checks.

AlogP shows a gating effect where activity appears to be markedly more likely at > ca. 2 and there is a slight preference for higher molecular weight compounds. But generally the SAR appears to be flat when judged by these simple molecular descriptors. It is likely that specific structural changes are driving Standard Value (potency), which are not captured in the dataset as it is.

## Project Structure

```
Week_9_ChEMBL_EDA/
├── .gitignore
├── README.md
├── notebooks/
│   ├── Full_5_step_GLP1_EDA.ipynb      <- main deliverable, run this first
│   └── daily/                          <- working notebooks, one per EDA step
│       ├── Day_1_GLP1_EDA_Audit.ipynb
│       ├── Day_2_GLP1_EDA_univariate.ipynb
│       ├── Day_3_GLP1_EDA_bivariate.ipynb
│       ├── Day_4_GLP1_EDA_multivariate.ipynb
│       └── Day_5_GLP1_EDA_integrity.ipynb
├── data/
│   └── raw/                            (gitignored)
└── logs/
    ├── day1_validation_log.md
    ├── day2_univariate_log.md
    ├── day3_bivariate_log.md
    ├── day4_multivariate_log.md
    └── day5_integrity_log.md
```

`notebooks/Full_5_step_GLP1_EDA.ipynb` is the complete analysis. The `daily/` notebooks and `logs/` are the working history, kept for reference to show the analysis as it was originally developed, including the discovery process behind key decisions (e.g. the assay-mixing finding, the placeholder-value investigation).

## Setup and Run Instructions

**Requirements:** Python 3, Pandas, NumPy, Matplotlib, Seaborn, Jupyter.

```
pip install -r requirements.txt
```

**Data:** place the raw ChEMBL export (`chembl_glp1.csv`) in `data/raw/`. This is not included in the repository (see `.gitignore`) — re-export from the ChEMBL link above if needed. Note the raw export is not pre-filtered; the notebook performs all filtering from the full, unfiltered pull.

**Run:** open `notebooks/Full_5_step_GLP1_EDA.ipynb` and run top to bottom.