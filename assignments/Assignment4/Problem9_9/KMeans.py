'''
Created on Nov 24, 2017

@author: nauman
'''
import numpy as np
from sklearn.cluster import KMeans
from spherecluster import SphericalKMeans

def kMeans(num):
    
    file = open("Kmeans.txt", "a+")
    input = np.array ([[-4, -2], [-3, -2], [-2, -2], [-1, -2], [1, -1], [1, 1], [2, 3], [3, 2], [3, 4], [4,3]])
    kmeans = KMeans(n_clusters=num, random_state=0).fit(input)
    file.write("K means output for cluster size : "+ str(num) + "\n")
    file.write("Clusters index of points" + "\n")
    file.write(str(kmeans.labels_) + "\n")
    file.write("Center of Clusters\n")
    file.write(str(kmeans.cluster_centers_) + "\n")
    file.close()
    
def sphericalKMeans(num):
    num = 4
    file = open("Kmeans.txt", "a+")
    input = np.array ([[-4, -2], [-3, -2], [-2, -2], [-1, -2], [1, -1], [1, 1], [2, 3], [3, 2], [3, 4], [4,3]])
    kmeans = SphericalKMeans(n_clusters=num).fit(input)
    file.write("Spherical K means output for cluster size : "+ str(num) + "\n")
    file.write("Clusters index of points" + "\n")
    file.write(str(kmeans.labels_) + "\n")
    file.write("Center of Clusters\n")
    file.write(str(kmeans.cluster_centers_) + "\n")
    file.close()
        
    
kMeans(4)
sphericalKMeans(4)