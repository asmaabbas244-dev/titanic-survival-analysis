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
sns.barplot(x='Sex', y='Survived', data=df, hue='Sex', legend=False)
plt.title('Sex vs Survival')
plt.xlabel('Sex')
plt.ylabel('Average Survival Rate')
plt.show()
