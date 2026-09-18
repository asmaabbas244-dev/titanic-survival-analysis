import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
numerical_cols = ["Age", "Fare", "SibSp", "Parch"]
plt.figure(figsize=(8, 4))
sns.boxplot(data=df[numerical_cols])
plt.title("Boxplots of Numerical Features")
plt.show()
