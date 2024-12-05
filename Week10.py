import pandas as pd
import matplotlib as plt
import numpy as np


data = {
    "Gender" : ['m','f','f','m','f','m','m'],
    "Height" : [172, 171, 169, 173, 170, 175, 178],
    "Weight" : [113, 96, 69, 73, 70, 57, 81]
}
df_sample = pd.DataFrame(data)

f_filter = df_sample['Gender'] == 'f'
m_filter = df_sample['Gender'] == 'm'

f_avg = df_sample[f_filter]['Height'].mean()
m_avg = df_sample[m_filter]['Height'].mean()

df_output = pd.DataFrame({   
            'Gender' : ['f','m'], 
            'Height' : [f_avg, m_avg]
        }
)

groupBySample = df_sample.groupby('Gender').mean()

print(groupBySample)
# print(df_output)
# print(df_sample[f_filter])
# print(f_avg)