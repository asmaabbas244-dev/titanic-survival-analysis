import os

tasks = {
    "task1.py": """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Libraries imported successfully!")
""",
    "task2.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print("Dataset loaded successfully!")
""",
    "task3.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.head())
""",
    "task4.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.sample(10))
""",
    "task5.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df.info()
""",
    "task6.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
rows, columns = df.shape
print(f"Number of rows = {rows}")
print(f"Number of columns = {columns}")
""",
    "task7.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.dtypes)
""",
    "task8.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.notnull().sum())
""",
    "task9.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print("Duplicate Rows:", df.duplicated().sum())
""",
    "task10.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df["Survived"].unique())
""",
    "task11.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.nunique())
""",
    "task12.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.describe())
""",
    "task13.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df.isnull().sum())
""",
    "task14.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0].sort_values(ascending=False))
""",
    "task15.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
result = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage": missing_percentage
})
print(result)
""",
    "task16.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
print("Duplicate Rows after removal:", df.duplicated().sum())
""",
    "task17.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
print("Missing Age values:", df["Age"].isnull().sum())
""",
    "task18.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print("Missing Embarked values:", df["Embarked"].isnull().sum())
""",
    "task19.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print("Missing values after cleaning:")
print(df.isnull().sum())
""",
    "task20.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
survival_rate = df["Survived"].mean() * 100
print(f"Overall Survival Rate: {survival_rate:.2f}%")
""",
    "task21.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.groupby("Sex")["Survived"].mean() * 100)
""",
    "task22.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.groupby("Pclass")["Survived"].mean() * 100)
""",
    "task23.py": """import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
numeric_cols = ["Age", "Fare", "SibSp", "Parch"]
df[numeric_cols].hist(bins=30, figsize=(10, 6), layout=(2, 2))
plt.tight_layout()
plt.show()
""",
    "task24.py": """import pandas as pd
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
""",
    "task25.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]
print(df[selected_cols].corr())
""",
    "task26.py": """import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
plt.figure(figsize=(8, 6))
sns.heatmap(
    df[["Age", "SibSp", "Parch", "Pclass", "Fare"]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.show()
""",
    "task27.py": """import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
sns.barplot(
    x="Sex",
    y="Survived",
    data=df,
    hue="Sex",
    legend=False
)
plt.title("Sex vs Survival")
plt.xlabel("Sex")
plt.ylabel("Average Survival Rate")
plt.show()
""",
    "task28.py": """import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
topFares = df.sort_values(by="Fare", ascending=False)
top5 = topFares.head(5)
print(top5[["Name", "Sex", "Pclass", "Fare"]])
""",
    "task29.py": """import pandas as pd
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
"""
}

for filename, content in tasks.items():
    with open(filename, "w") as f:
        f.write(content)

print("Created 29 task files successfully!")
