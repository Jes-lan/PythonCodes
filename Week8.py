import warnings
warnings.filterwarnings("ignore")

import pandas as pd

df = pd.read_csv("data.csv")

x = round(df.Calories.mean())

df.Calories.fillna(x, inplace=True)

print("Mode =",df.Calories.mode()[0])
print("Mode =",df.Calories.mean())

