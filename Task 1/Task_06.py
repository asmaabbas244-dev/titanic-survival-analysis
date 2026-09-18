import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")
print('Number of rows =', df.shape[0])
print('Number of columns =', df.shape[1])
