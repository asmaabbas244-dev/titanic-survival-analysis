import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
topFares = df.sort_values(by="Fare", ascending=False)
top5 = topFares.head(5)
print(top5[["Name", "Sex", "Pclass", "Fare"]])
