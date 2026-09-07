# Validation log

* Shape: 48 columns x 113886 rows

* Datatypes
    * All appear to be correct. float64(17), int64(2), str(29)
    * Assay subcellular fraction is flagged as having mixed types (only has 9 values)
    * It looks like Standard units flags some standard values as % and others as EC50 uM etc
* Missing values
    * 48 columns
    * Columns 27, 28, 31-33 have 0 non-null values
    * There are 22 columns with >90% null rows (inc 5 above)
    * 16 columns with no null rows
* Distinct values
    * The max unique values in a column is 107368 in Molecule ChEMBL ID, which is 6518 short of the 113886 rows
    * So some compounds have multiple rows
* Units
    * There are 17 different units, but nM covers 97.6% of the entries
* Duplicate
    * There are 3811 compounds with more than 1 row, and they have up to 59 rows
    * CHEMBL4518483 has been tested in 49 unique assays, each with up to 6 values. To give 59 rows