import pandas as pd
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

df = pd.read_csv("data.csv")

df.Calories.plot(kind="hist")

plt.show()