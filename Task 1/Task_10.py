import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")
print('--- Unique values in Survived ---')
print(df['Survived'].unique())
