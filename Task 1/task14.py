import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0].sort_values(ascending=False))
