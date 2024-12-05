import pandas as pd
import matplotlib as plt
import numpy as np
import warnings as wrn

wrn.filterwarnings()

veri = pd.read_csv("personel.csv", delimiter=';')

veri.drop('Department', axis=1, inplace=True)

for idx in veri.index:
    if veri.loc[idx, "Education"] == " ":
        veri.drop(idx, inplace=True)
veri = veri[veri["Education"].notna()]

ort = int(veri["Age"].mean())
veri["Age"].fillna(ort,inplace=True)

veri.Age

print(veri)
