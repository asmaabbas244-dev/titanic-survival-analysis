import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
print("Missing Age values:", df["Age"].isnull().sum())
