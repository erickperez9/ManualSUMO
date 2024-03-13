# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

tripinfo_file = 'Desktop/practica1/tripinfo.csv'
df = pd.read_csv(tripinfo_file)
data=pd.read_csv(tripinfo_file, usecols=['emissions_CO2_abs','tripinfo_routeLength'])
data=data.dropna()

scaler=StandardScaler()
data_scaled = scaler.fit_transform(data)

silhouette_scores = []

for k in range(2,10):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data_scaled)
    score = silhouette_score(data_scaled,kmeans.labels_)
    silhouette_scores.append(score)


plt.plot(range(2,10),silhouette_scores,marker='o')
plt.xlabel('Numero de Clusters (k)')
plt.ylabel('Coefficiente de silueta')
plt.title('Coefficiente de silueta para diferentes k')
plt.show()


k=3
kmeans=KMeans(n_clusters=k, init='k-means++',random_state=42)
kmeans.fit(data_scaled)
centroids = kmeans.cluster_centers_
labels=kmeans.labels_
plt.scatter(data_scaled[:,0],data_scaled[:,1],c=labels,s=50,cmap='viridis')
plt.scatter(centroids[:,0],centroids[:,1],marker='*',s=300,c='red')
plt.xlabel('Scaled Emisiones')
plt.ylabel('Scaled Route Length')
plt.show()


