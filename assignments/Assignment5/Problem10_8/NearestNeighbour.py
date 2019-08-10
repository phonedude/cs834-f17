'''
Created on Dec 11, 2017

@author: nauman
'''

import numpy as np
from sklearn.cluster import KMeans
import xlrd

def readXLSFile():
    file = "F:\\Fall2017\\InformationRetreival\\Assignment5\\Problem10_8\\jester-data-3\\jester-data-3.xls"
    book = xlrd.open_workbook(file)
    print(book.nsheets)
    sh = book.sheet_by_index(0)
    print(sh.name)
    sheet = book.sheet_by_name(sh.name)
    data = [None] * 10
    for c in range(0,10):
        data[c] = [None] * (9)
 
    for c in range(0,10):
        for r in range(1, 10):
            data[c][r-1] = sheet.cell_value(c,r)
        print(data[c])
        print("\n")
    return data

def kMeans(num):
    print("run")
    file = open("Kmeans.txt", "a+")
    inputData = readXLSFile()
    print(inputData)
    inputArray = np.asarray(inputData)
    print(inputArray)
    kmeans = KMeans(n_clusters=num, random_state=0).fit(inputArray)
    file.write("K means output for cluster size : "+ str(num) + "\n")
    file.write("Clusters index of points" + "\n")
    file.write(str(kmeans.labels_) + "\n")
    file.write("Center of Clusters\n")
    file.write(str(kmeans.cluster_centers_) + "\n")
    file.close()
    print("end")
    
kMeans(3)
