## Day 2 — Univariate Analysis: Standard Value

### Filtering
* Filtered Standard Type to Potency only. Giving comparable values, all in nM. Filtered Assay ChEMBL ID to 'CHEMBL2114788' giving inverse agonists only (excluding the small agonists datasets)
    * Tested filtering Standard Units to nM, but that pulled in a few other assay types.
* Now entirely null: `Standard Relation`, `pChEMBL Value`, `Data Validity Comment`, `Ligand Efficiency BEI`, `Ligand Efficiency LE`, `Ligand Efficiency LLE`, `Ligand Efficiency SEI`, `Assay Tissue ChEMBL ID`, `Assay Tissue Name`, `Assay Cell Type`, `Assay Subcellular Fraction`, `Assay Parameters`, `Assay Variant Accession`, `Assay Variant Mutation`, `Document Journal`, `Document Year`, `Cell ChEMBL ID`, `Properties`, `Action Type`, `Standard Text Value`.
    * No Standard Relation values to distort the potency data.
    * Dropped null columns.

### Shape of Distribution of Standard Value
* Mean = 14167, median = 11220.
* Skew = 0.54, meaning the tail extends to the right.
* Excess kurtosis = -0.999, meaning the distribution is platykurtic — flatter than a normal distribution (0).
* Plotting a histogram shows a distribution centred at 10000 nM with a longer right tail. But with a second peak due to a single highly populated bin at ca. 27000 nM. This may be an artifact, if that was determined to be the lower detection limit in many of the assays.
* Investigating the outlier peak bin [ca. 27,000 nM], there are 20546 rows all with Standard Value = 28183.8 nM. Clearly this is not a real biological value as it must relate to a systemic artifact (detection limit, placeholder, etc). Needs tracing to source assays before it could be included as a valid measurement.
    * Confirmed: all come from two assays (Assay ChEMBL ID) and all have Comment = 'inconclusive' or 'inactive'. Indicating this is likely a placeholder value.
        * **Decision:** exclude these rows from any further analysis.

### Re-analysis After Excluding Standard Value = 28183.8 nM
* Standard Value mean = 10895.81, median = 10000.00. Standard Value skew = 1.23, excess kurtosis = 1.94.
* Median is suspicious.
* Top Standard Value counts (10000.0, 11220.2, 12589.3, 8912.5, etc) form a geometric series (ratio ≈ 1.122 ≈ 10^0.05) — consistent with standard half-log dilution assay design. Therefore the 10000 median is a result of assay design rather than an artifact.
* **Correction:** 28183.8 nM falls exactly on the half-log dilution series (10000 × 10^0.45, 9 steps up). Therefore it is likely the maximum tested concentration in these 2 assays, reported when no activity was observed (Comment = inconclusive/inactive). Decision to exclude from downstream potency analysis still stands, as it isn't a true potency value.

### Comments
* Within the filtered dataset: 61943 (74%) inconclusive, 14980 (18%) inactive, 6432 (7%) active.
* Looking at just those results labelled as inconclusive, the distribution of Standard Value is very similar to the wider dataset. Inconclusive rows are not concentration-dependent, ruling out any ceiling/floor artifact explanation.
* **Decision:** excluding "inconclusive" is a scope choice (to measure resolved potency values only), rather than a data-quality correction. 'Inconclusive' rows will be filtered out and 'inactive' rows will be retained, as they represent a conclusive result.
    * New Standard Value mean = 8845.67, median = 10000.00. Standard Value skew = 1.09, excess kurtosis = 2.16.

### IQR Outlier Analysis
*(Conclusive rows: excluding 'inconclusive' and value = 28183.8 nM, n = 22326)*
* Q1: 3981.1, Q3: 11220.2, interquartile range: 7239.1.
* Lower fence: -6877.6, upper fence: 22078.9.
* There are 0 rows below the lower fence, and 1037 above the upper fence (ca. 5%).
* Outliers above the top fence resolve into four values (22387.2, 25118.9, 31622.8, 35481.3), consistent with the same half-log dilution series (from 10000 baseline). Not anomalous data — just the highest tested concentrations. IQR correctly flags them as statistically extreme relative to the bulk of the distribution, but they represent valid, real measurements rather than errors.
* **Conclusion:** no further row exclusions warranted from the IQR pass.

### Box Plot
* Box plot visually confirms IQR analysis — outlier points beyond the upper whisker match the four dilution-series values identified above.