import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")
missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
print('--- Missing Values Percentage ---')
print(pd.DataFrame({'Missing Count': df.isnull().sum(), 'Missing Percentage': missing_percentage}))
