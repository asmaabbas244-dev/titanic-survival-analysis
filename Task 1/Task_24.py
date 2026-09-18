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
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
plt.figure(figsize=(8, 4))
sns.boxplot(data=df[numeric_cols])
plt.title('Boxplots of Numerical Features')
plt.show()
