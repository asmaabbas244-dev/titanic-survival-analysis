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
sns.barplot(x='Fare', y='Name', data=top5, hue='Sex')
plt.title('Five Highest-Paying Passengers')
plt.xlabel('Fare')
plt.ylabel('Passenger Name')
plt.show()
