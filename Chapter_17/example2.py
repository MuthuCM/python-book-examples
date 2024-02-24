# Example 17.2
# K-Means Clustering

# Import the libraries
import numpy as np
import pandas as pd

# Read data from a CSV file
dataset = pd.read_csv('VehicleData2.csv')
#X = dataset.iloc[:, 0:-1]
X = dataset.iloc[:, 0].values
X = X.reshape(-1,1)

# Do Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)


# Fit K-Means Model to the dataset
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++')
y_kmeans = kmeans.fit_predict(X)
print(y_kmeans)
