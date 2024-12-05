import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

import warnings
warnings.filterwarnings("ignore")


veri = pd.read_csv("olimpiyatlar.csv")

veri.rename(columns={'ID': 'id',
                    'Name': 'İsim',
                    'Sex': 'Cinsiyet',
                    'Age': 'Yas',
                    'Height': 'Boy',
                    'Weight': 'Kilo',
                    'Team': 'Takim',
                    'NOC': 'Kod',
                    'Games': 'Oyunlar',
                    'Year': 'Yil',
                    'Season': 'Mevsim',
                    'City': 'Sehir',
                    'Sport': 'Spor',
                    'Event': 'Etkinlik',
                    'Medal': 'Medal'}, inplace=True)

veri.drop(["id","Oyunlar"],axis=1,inplace=True)

def yas_ort():
    orta = np.round(np.mean(veri.Yas), 2)
    veri.Yas.fillna(orta, inplace=True)

def boyVeKilo(veri):
    essiz_etkinlik = pd.unique(veri.Etkinlik)

    veri_gecici = veri.copy()

    nan_listesi = ["Boy","Kilo"]


    for e in essiz_etkinlik:
        etkinlik_filtre = veri_gecici.Etkinlik == e
        fitreli_veri = veri_gecici[etkinlik_filtre]
        for s in nan_listesi:
            orta = np.round(np.mean(fitreli_veri[s]), 2)
            if ~np.isnan(orta):
                fitreli_veri[s].fillna(orta, inplace=True)
            else:
                orta = np.round(np.mean(veri_gecici[s]), 2)
                fitreli_veri[s].fillna(orta, inplace=True)

        veri = veri_gecici.copy()
        print(veri.info)

        veri_gecici[etkinlik_filtre] = fitreli_veri
        break
    
def medal():
    global veri
    madalya_fitresi = ~pd.isnull(veri.Medal)
    veri = veri[madalya_fitresi]
    veri.to_csv("olimpiyatlar_madalya.csv", index=False)

def plotHistogram(var):
    plt.figure()
    plt.hist(veri[var], bins=75, color="blue")
    plt.xlabel(var)
    plt.ylabel("Frekans")
    plt.title(f"{var} Histogramı")
    plt.show()

# sayisal = ["Yas","Boy", "Kilo", "Yıl"]
# for i in sayisal:
#     plotHistogram(i)

def plotBar(var, n=5):
    veri_sayma = veri[var].value_counts()
    veri_sayma = veri_sayma[:n]
    plt.figure()
    plt.bar(veri_sayma.index, veri_sayma, color="orange")
    plt.xticks(veri_sayma.index, veri_sayma.index.values)
    plt.xticks(rotation=60)
    plt.ylabel("Frekans")
    plt.title(var + "Veri Sıklığı")
    plt.show()

# kategori = ['İsim', 'Cinsiyet', 'Takım', 'Kod', 'Mevsim', 'Şehir', 'Spor', 'Etkinlik', 'Medal']

# for i in kategori:
#     plotBar(i)

def pltKiloBoy(veri):
    erkek = veri[veri.Cinsiyet == 'M']
    kadin = veri[veri.Cinsiyet == 'F']
    # print(erkek.head(3))
    # print(kadin.head(3))

    plt.figure()
    plt.scatter(kadin.Boy, kadin.Kilo, alpha=0.5, label='Kadin')
    plt.scatter(erkek.Boy, erkek.Kilo, alpha=0.5, label='Erkek')
    plt.xlabel('Boy')
    plt.ylabel('Kilo')
    plt.title("Boy-Kilo Iliskisi")
    plt.legend()
    plt.show()

# pltKIloBoy(veri)


# print(veri.loc[:,['Yas', 'Boy', 'Kilo']].corr())


veri_gecici = veri.copy()
veri_gecici = pd.get_dummies(veri_gecici,columns=['Medal'], dtype=int)
# print(veri_gecici.head(3))


# print(veri_gecici[["Cinsiyet", 'Medal_Gold', 'Medal_Silver', 'Medal_Bronze']].groupby(['Cinsiyet']).sum().sort_values(by="Medal_Gold",ascending=False)[:10])

# def BoyKiloYasPivot(veri):
#     veri_pivot = veri.pivot_table(index='Medal', columns="Cinsiyet", values=['Boy', 'Kilo', 'Yas'], 
#                                 aggfunc= {
#                                     "Boy": np.mean,
#                                     "Kilo": np.mean,
#                                     "Yas": [min,max,np.std]
#                                 })

#     print(veri_pivot.head(10))

# BoyKiloYasPivot(veri)


def anomalyDetector(df, ozellik):
    outlier_indices = []

    for c in ozellik:
        Q1 = np.percentile(df[c],25) #1.ceyrek
        Q3 = np.percentile(df[c],75) #3.ceyrek

        IQR = Q3 - Q1
        outlier_step = IQR * 1.5
        outlier_list_col = df[( df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step )].index
        outlier_indices.extend(outlier_list_col)
    
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(i for i, v in outlier_indices.items() if v > 1 )
    return multiple_outliers

yas_ort()
medal()


veri_anomali = veri.loc[anomalyDetector(veri, ["Yas", "Boy", "Kilo"])]

veri_gym = veri_anomali[veri_anomali.Spor == "Gymnastics"]



print(veri_gym.Etkinlik.value_counts())
