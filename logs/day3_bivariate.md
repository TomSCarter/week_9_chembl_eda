## Day 3 — Bivariate Analysis

* Loaded data filtered conclusive rows: excluding 'inconclusive' and value = 28183.8 nM, n = 22326, filtering to 'Potency' type and 'CHEMBL2114788' assay ID.

* Computed correlation matrices between all numerical columns (Pearson and Spearman) and generated heatmaps
    * Pearson and Spearman agree closely, with the largest shift in ALogP vs Molecule Max Phase and ALogP vs #RO5 violations (both ca. 0.05). This indicates the relationships are well described by either method and are not driven by nonlinear effects.
    * 'Standard value' and 'Value' show a perfect correlation. It appears that value is just a version scaled to uM. Scatter plot is linear.
    * 'Standard value' and 'Molecule Max Phase' show a weak correlation (Pearson = 0.16). 'Molecule Max Phase' contains only 80 non-null values, which makes sense as most compounds do not reach clinical trials.
    * Stronger correlations between '#RO5 Violations' and 'AlogP' (Pearson = 0.49) or 'Molecular Weight' (Pearson = 0.50). This is logical as logP and Molecular weight form part of the rule-of-5 (RO5)

* Violin plot of 'Standard Value' vs 'Comment' shows a peak of active compounds at 10000, and a longer tail of inactive compounds extending to 35000+ (very slim beyond 15000 for active)

* Violin plot of 'Standard Value' vs '#RO5 Violations' don't show any clear differences. Distribution of compounds with 0, 1 or 2 shows two peaks and long tails. With 3 violations the distribution is much flatter and wider.
    * A value_count shows that the group with 3 violations only contains 11 rows, therefore the change in distribution is likely a result of the small sample.