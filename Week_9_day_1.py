import pandas as pd

df = pd.read_csv("Week_9/chembl_glp1.csv", nrows=100, sep=';')

print(df.head())
print(df.info())