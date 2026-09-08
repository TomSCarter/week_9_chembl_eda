* Filtered Standard Type to Potency only. Giving comparable values, all in nM
    * Tested filtering Standard Units to nM, but that pulled in a few other assay types
* Now entirely null: Standard Relation', 'pChEMBL Value', 'Data Validity Comment', 'Ligand Efficiency BEI', 'Ligand Efficiency LE', 'Ligand Efficiency LLE', 'Ligand Efficiency SEI', 'Assay Tissue ChEMBL ID', 'Assay Tissue Name', 'Assay Cell Type', 'Assay Subcellular Fraction', 'Assay Parameters', 'Assay Variant Accession', 'Assay Variant Mutation', 'Document Journal', 'Document Year', 'Cell ChEMBL ID', 'Properties', 'Action Type', 'Standard Text Value'
    * No Standard Relation values to distort the potency data
    * Dropped null columns

## Shape of distribution of Standard Value

* mean = 14203, median = 11220
* Skew = 0.55, meaning the tail extends to the right
* Excess kurtosis = -0.95, meaning the distribuion is platykurtic flatter than a normal distribution (0) 
* Plotting a histogram shows a distribution centred at 10000 nM with a longer right tail. But with a second peak due to a single highly populated bin at ca. 27000 nM. This may be an artifact, if that was determined to be the lower detection limit in many of the assays.
* Investigating the outlier peak bin [ca. 27,000 nM], there are 20585 rows all with Standard Value = 28183.8 nM. Clearly this is not a real biological value as must related to a systemic artifact (detection limit, placeholder etc). Needs tracing to source assays before it could be included as a valid measurement.
    * Confirmed: All come from two assays (Assay ChEMBL ID) and all have Comment = 'inconclusive' or 'inactive'. Indicating this is likely a placeholder value.
        * Decision: Exclude these rows from any further analysis