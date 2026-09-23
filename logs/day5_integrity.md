# Day 5 - Integrity Diagnostics

* Loaded data: excluding Comment = 'inconclusive' and Standard Value = 28183.8 nM, and filtering to 'Assay ChEMBL ID' = 'CHEMBL2114788' (see day 2 & 4 logs for explanation)
* Shape: (21412, 28)

### Zero-variance / constant column audit

* There are 17 columns containing a single unique value (no nulls in these columns):
    Standard Type = Potency
    Standard Units = nM
    Uo Units = UO_0000065
    Potential Duplicate = 0
    Assay ChEMBL ID = CHEMBL2114788
    Assay Description = PubChem BioAssay. qHTS of GLP-1 Receptor Inverse Agonists (Inhibition Mode). (Class of assay: confirmatory) 
    Assay Type = F
    BAO Format ID = BAO_0000019
    BAO Label = assay format
    Assay Organism = Homo sapiens
    Target ChEMBL ID = CHEMBL1784
    Target Name = Glucagon-like peptide 1 receptor
    Target Organism = Homo sapiens
    Target Type = SINGLE PROTEIN
    Document ChEMBL ID = CHEMBL1201862
    Source ID = 7
    Source Description = PubChem BioAssays
* Created df_modelling_ready with columns above dropped. Shape: (21412, 11)
    * A one-off demonstration snapshot, main dataframe retains these columns. 

### Derived/redundant column audit

* The lipinski rule of 5 that is used to determine '#RO5 Violations' is:  
    * Molecular Weight < 500
    * LogP <= 5
    * Hydrogen Bond Donors <= 5
    * Hydrogen Bond Acceptors: <= 10
    Meaning that #RO5 Violations is derived from Molecular Weight and (a version of) AlogP
* Standard Value and Value are the same potency values scaled to different units (nM vs µM)

### Sparse columns

* Molecule Name (141 non-null, 0.7%) and Molecule Max Phase (74 non-null, 0.35%) have a very small fraction non-null

### Schema verification checks

* Wrote functions to check:
    * check_columns to compare column list against expected
    * check_single_assay to check there is only one unique value in Assay ChEMBL ID
    * check_no_placeholder_value to confirm that the 28183.8nM placeholder in Standard Value has been filtered out
    * check_value_range to confirm there are no Standard Value values below zero
    * check_allowed_categories to check categories in Comment against an allowed list