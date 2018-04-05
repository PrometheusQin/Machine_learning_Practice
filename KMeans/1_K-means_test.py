# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:04:55 2017

@author: Flame
"""
import numpy as np
from sklearn.cluster import KMeans

def loadData(filePath):
    fr = open(filePath, 'r+')
    lines =fr.readlines()
    retData=[]
    retCityName=[]
    for line in lines:
        items=line.strip().split()
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1, len(items))])
    fr.close()
    return retData, retCityName

if __name__ == '__main__':
    Data, CityName=loadData('city.txt')
#    for i in range(len(CityName)):
#        print(CityName[i])
#        for num in Data[i]:
#            print(num)
    km = KMeans(n_clusters=4)
    label = km.fit_predict(Data)
    expenses = np.sum(km.cluster_centers_,axis=1)
    # print(expenses)
    CityCluster = [[],[],[],[]]
    for i in range(len(CityName)):
        CityCluster[label[i]].append(CityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])