# Abundance
# Language: Python
# Input: CSV
# Output: NOA
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to take a CSV file of abundances and produce an output
Node Attribute file (NOA) for Cytoscape, consisting of the 
average abundance of each node across all samples.

The CSV file is thus assumed to be in matrix form, with samples
as rows and taxa as columns.  Entry (i, j) is thus assumed
to be the amount of taxon j in sample i.  These can be absolute
or normalized abundances.

The output NOA file will be in tabular form, with the first column
as nodes and the second the average abundances.
