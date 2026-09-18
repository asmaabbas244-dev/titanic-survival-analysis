import os
import urllib.request

# 1. Folder Create karna
base_dir = r"C:\Users\muham\Downloads\Semester 7\Task 1"
os.makedirs(base_dir, exist_ok=True)

# 2. Dataset ko download karna
dataset_path = os.path.join(base_dir, "titanic.csv")
if not os.path.exists(dataset_path):
    print("Downloading Titanic dataset...")
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    urllib.request.urlretrieve(url, dataset_path)
    print("Dataset downloaded!")

# --- Common Code Blocks (Jo alag-alag files mein use honge) ---
preamble_raw = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")
'''

preamble_clean = preamble_raw + '''
# --- Data Cleaning (Applied from Tasks 16-18) ---
df = df.drop_duplicates().copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
'''

# 3. Har Task ka Code
tasks = {
    1: "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nprint('Libraries imported successfully.')\n",
    2: preamble_raw + "print('Dataset loaded successfully.')\n",
    3: preamble_raw + "print('--- First 5 rows ---')\nprint(df.head())\n",
    4: preamble_raw + "print('--- Random 10 rows ---')\nprint(df.sample(10))\n",
    5: preamble_raw + "print('--- Dataset Info ---')\ndf.info()\n",
    6: preamble_raw + "print('Number of rows =', df.shape[0])\nprint('Number of columns =', df.shape[1])\n",
    7: preamble_raw + "print('--- Data Types ---')\nprint(df.dtypes)\n",
    8: preamble_raw + "print('--- Non-Missing Values Count ---')\nprint(df.notnull().sum())\n",
    9: preamble_raw + "print('Duplicate Rows:', df.duplicated().sum())\n",
    10: preamble_raw + "print('--- Unique values in Survived ---')\nprint(df['Survived'].unique())\n",
    11: preamble_raw + "print('--- Unique values in every column ---')\nprint(df.nunique())\n",
    12: preamble_raw + "print('--- Descriptive Statistics ---')\nprint(df.describe())\n",
    13: preamble_raw + "print('--- Missing Values Count ---')\nprint(df.isnull().sum())\n",
    14: preamble_raw + "missing_values = df.isnull().sum()\nprint('--- Columns with Missing Values ---')\nprint(missing_values[missing_values > 0].sort_values(ascending=False))\n",
    15: preamble_raw + "missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)\nprint('--- Missing Values Percentage ---')\nprint(pd.DataFrame({'Missing Count': df.isnull().sum(), 'Missing Percentage': missing_percentage}))\n",
    16: preamble_raw + "df = df.drop_duplicates().copy()\nprint('Duplicates removed. New shape:', df.shape)\n",
    17: preamble_clean + "print('Missing ages handled using median.')\n",
    18: preamble_clean + "print('Missing Embarked handled using mode.')\n",
    19: preamble_clean + "print('Remaining missing values:')\nprint(df.isnull().sum())\n",
    20: preamble_clean + "survival_rate = df['Survived'].mean() * 100\nprint(f'Overall Survival Rate: {survival_rate:.2f}%')\n",
    21: preamble_clean + "print('--- Survival Rate by Sex ---')\nprint(df.groupby('Sex')['Survived'].mean() * 100)\n",
    22: preamble_clean + "print('--- Survival Rate by Pclass ---')\nprint(df.groupby('Pclass')['Survived'].mean() * 100)\n",
    23: preamble_clean + "numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']\ndf[numeric_cols].hist(bins=30, figsize=(10, 6), layout=(2, 2))\nplt.tight_layout()\nplt.show()\n",
    24: preamble_clean + "numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']\nplt.figure(figsize=(8, 4))\nsns.boxplot(data=df[numeric_cols])\nplt.title('Boxplots of Numerical Features')\nplt.show()\n",
    25: preamble_clean + "selected_cols = ['Age', 'SibSp', 'Parch', 'Pclass', 'Fare']\nprint('--- Correlation Matrix ---')\nprint(df[selected_cols].corr())\n",
    26: preamble_clean + "plt.figure(figsize=(8, 6))\nsns.heatmap(df[['Age', 'SibSp', 'Parch', 'Pclass', 'Fare']].corr(), annot=True, cmap='coolwarm', fmt='.2f')\nplt.title('Correlation Heatmap')\nplt.show()\n",
    27: preamble_clean + "sns.barplot(x='Sex', y='Survived', data=df, hue='Sex', legend=False)\nplt.title('Sex vs Survival')\nplt.xlabel('Sex')\nplt.ylabel('Average Survival Rate')\nplt.show()\n",
    28: preamble_clean + "topFares = df.sort_values(by='Fare', ascending=False)\ntop5 = topFares.head(5)\nprint('--- Top 5 Highest-Paying Passengers ---')\nprint(top5[['Name', 'Sex', 'Pclass', 'Fare']])\n",
    29: preamble_clean + "topFares = df.sort_values(by='Fare', ascending=False)\ntop5 = topFares.head(5)\nsns.barplot(x='Fare', y='Name', data=top5, hue='Sex')\nplt.title('Five Highest-Paying Passengers')\nplt.xlabel('Fare')\nplt.ylabel('Passenger Name')\nplt.show()\n"
}

# 4. Files generate karna
for task_num, code in tasks.items():
    file_path = os.path.join(base_dir, f"Task_{task_num:02d}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

print(f"\nKaam ho gaya! Total {len(tasks)} tasks ki files {base_dir} mein ban gayi hain.")