import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print("Duplicate Rows:", df.duplicated().sum())
