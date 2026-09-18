import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")
df = df.drop_duplicates().copy()
print('Duplicates removed. New shape:', df.shape)
