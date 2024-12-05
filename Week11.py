import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


data = pd.read_csv('Pokemon.csv', index_col=0)

sb.lmplot(x='Attack', y='Defense', data=data)


