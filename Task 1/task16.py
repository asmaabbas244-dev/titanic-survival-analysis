import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
print("Duplicate Rows after removal:", df.duplicated().sum())
