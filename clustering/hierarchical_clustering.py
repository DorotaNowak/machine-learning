import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values

#Using the dendrogram
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customrs')
plt.ylabel('Euclidian distance')
plt.show()
#Optimal number of clusters = 5

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)

plt.scatter(X[y_hc == 0,0], X[y_hc==0,1], s = 100, c='red', label='cluster1')
plt.scatter(X[y_hc == 1,0], X[y_hc==1,1], s = 100, c='blue', label='cluster2')
plt.scatter(X[y_hc == 2,0], X[y_hc==2,1], s = 100, c='green', label='TARGET')
plt.scatter(X[y_hc == 3,0], X[y_hc==3,1], s = 100, c='cyan', label='cluster4')
plt.scatter(X[y_hc == 4,0], X[y_hc==4,1], s = 100, c='magenta', label='cluster5')
plt.xlabel('Annual income')
plt.ylabel('Spending score')
plt.legend()
plt.show()