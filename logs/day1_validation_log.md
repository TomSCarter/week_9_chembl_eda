# Validation log

**Assay ID filter added after downstream analysis revealed the raw pull mixed two distinct pharmacological assays; see Day 4 log for the diagnostic trail**

**Shape**: 48 columns x 113886 rows

* Datatypes
    * All appear to be correct. float64(17), int64(2), str(29)
    * Assay subcellular fraction is flagged as having mixed types (only has 9 values)
    
* Missing values
    * 48 columns
    * Columns 27, 28, 31-33 have 0 non-null values
    * There are 22 columns with >90% null rows (inc 5 above)
    * 16 columns with no null rows
    * Standard Relation has 107696 null values. These operators are usually used when a rate/potency is above/below the accurate detection limit. But I do see '=' being used, so it could be different reporting by the different assays.

* Distinct values
    * The max unique values in a column is 107368 in Molecule ChEMBL ID, which is 6518 short of the 113886 rows
        * So some compounds have multiple rows
    * Assay Organism has only 1 unique value but also 1770 nulls. The dataset I downloaded said it was 100% Homo Sapiens

* Units & Measurement types
    * **Key finding**: Standard units contains a mixture of rates, concentrations and percentages. This will need to be filtered/separated
    * There are 17 different units, but nM covers 97.6% of the entries so could reasonably filter to nM only.
    * Standard Type contains 25 unique values. 107577 are 'Potency', with EC50 second (2365). But there are also, %Inhib, %Max, various ratios and rates (kon, koff) etc

* Duplicates
    * Only 1 fully duplicated row 
    * There are 3811 compounds with more than 1 row, and they have up to 59 rows (CHEMBL4518483)
    * CHEMBL4518483 has been tested in 49 unique assays, each with up to 6 values

* Filtering
    * Filtered Standard Type to 'Potency'
    * Assay Description shows three different assays. Large set of inverse agonists (103901), but also two sets of agonists (3541 & 141). Given the opposite pharmacology, the data was filtered to the inverse agonists only (Assay ChEMBL ID = CHEMBL2114788).