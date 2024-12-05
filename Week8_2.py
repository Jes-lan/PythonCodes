import pandas as pd
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("data.csv")

for idx in df.index:
    if df.loc[idx, "Duration"] > 120:
        df.loc[idx, "Duration"] = 120

print(df.Duration.to_string())