import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
result = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage": missing_percentage
})
print(result)
