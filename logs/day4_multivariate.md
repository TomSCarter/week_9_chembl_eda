## Day 4 Multivariate analysis

**This log reflects the state of the analysis before the assay filter was identified and moved upstream to Day 1 — the starting n=22,326 here still contains all three assays; see Day 1 for the retrofitted pipeline.**

* Loaded data filtered conclusive rows: excluding 'inconclusive' and value = 28183.8 nM (excluded n= 64666 on inconclusive then n= 20585 on 28183.8 nM value), n = 22326

* Initial Pairgrid analysis does not show any clear relationships between Standard Value and Molecular Weight, AlogP or #RO5 Violations. #RO5 has a relationship with the other descriptors, as they are used in its calculation.

* Investigation to see if a mixture of data is clouding any trends:
    * Value_counts on Standard Type, Target Name and Assay Type show only one unique value for each
    * Molecule Max Phase would be useful but only covers 80 compounds (0.3%).
    * Comment contains inactive and active
    * Potential Duplicate is marked 0 for all rows
    * Standard Value shows many values in a half log dilution series, with 10000 as the most common value
        * Possible that some of these are not true values, and the max assay concentration has been reported (e.g. inactive >10000), potentially even with different assay max concentrations combined into the same dataset. But it is not clear how best this could be determined. No operators have been given.
    * Comparing the distribution of Standard Value for 'Active' and 'Inactive' compounds.
        * 'Active shows a tighter distribution with very little < ca. 10^3 or > ca. 10^4. Shape is less noisey with a clear left tail.
        * Both have major peaks at 10000 (10^4)
    * Value counts on Source ID and Document ChEMBL ID show a single source.
    * Assay ChEMBL ID and Assay Description show 3 sources
        * Description shows that one set is Inverse Agonists (Inhibition mode, 21412) and two are Agonists (891 and 23). These measure opposite pharmacology, so should be separated.
        * Filtered on Assay ChEMBL ID (CHEMBL2114788), n=22,326 to n=21,412

* Scatterplot of Standard Value vs AlogP coloured by Comment
    * No relationship between Standard Value and AlogP, a broad cloud 
    * Comment hue shows majority of active compounds are clustered between AlogP = 3 and 7, where inactive compounds span 0 to 5

* Scatterplot of Standard Value vs Molecular Weight coloured by Comment
    * No relationship between Standard Value and Molecular weight
    * Comment Hue shows a weak bias of active compounds to higher molecular weight (400 - 650) vs inactive (200 -500)

* Activity appears to be markedly more likely at AlogP > ca. 2 and there is a slight preference for higher molecular weight compounds. But generally the SAR appears to be flat when judged by these simple molecular descriptors. It is likely that specific structural changes are driving Standard Value (potency), which are not captured in the dataset as it is.