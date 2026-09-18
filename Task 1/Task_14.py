import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")
missing_values = df.isnull().sum()
print('--- Columns with Missing Values ---')
print(missing_values[missing_values > 0].sort_values(ascending=False))
