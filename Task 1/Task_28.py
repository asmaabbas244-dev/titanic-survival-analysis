import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")

# --- Data Cleaning (Applied from Tasks 16-18) ---
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
topFares = df.sort_values(by='Fare', ascending=False)
top5 = topFares.head(5)
print('--- Top 5 Highest-Paying Passengers ---')
print(top5[['Name', 'Sex', 'Pclass', 'Fare']])
