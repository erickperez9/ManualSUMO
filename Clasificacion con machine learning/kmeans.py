# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 8:35:11 2024

@author: PCX
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('tripinfo-emissions.csv')
df.head()

df_sub =  df[['emissions_CO2_abs','emissions_CO2_abs']]

kmeans = KMeans(n_clusters=3, n_init=10).fit(df_sub.values)

df['Cluster'] = kmeans.labels_

plt.figure(figsize=(5,5), dpi=100)
colors = ['blue', 'red', 'green']

# graficar puntos de clusters
for cluster in range(kmeans.n_clusters):
    plt.scatter(df[df["Cluster"] == cluster]['emissions_CO2_abs'],
                df[df["Cluster"] == cluster]['emissions_CO2_abs'],
                marker='o', s=5, color=colors[cluster])

# graficar centroides
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            marker='*', s=20, linewidths=3, color='purple', label='Centroides')

plt.title("Clasificación de emisiones CO2 absolutas")
plt.xlabel("emissions_CO2_abs")
plt.ylabel("emissions_CO2_abs")
plt.grid(visible=True)
plt.show()






