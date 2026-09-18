import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
topFares = df.sort_values(by="Fare", ascending=False)
top5 = topFares.head(5)
sns.barplot(
    x="Fare",
    y="Name",
    data=top5,
    hue="Sex"
)
plt.title("Five Highest-Paying Passengers")
plt.xlabel("Fare")
plt.ylabel("Passenger Name")
plt.show()
