# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:16:42 2017

@author: Flame
"""

import ML_KMeans
import numpy as np
import matplotlib.pyplot as plt

## 测试distEclud
#vecA = np.array([1,2,3])
#vecB = np.array([3,6,9])
#dist=ML_KMeans.distEclud(vecA, vecB)
#print(dist)
#
## 测试loadDataSet
#
#dataSet = ML_KMeans.loadDataSet('city_1.txt')
#print(dataSet)
#
## 测试randCent
#centroids=ML_KMeans.randCent(dataSet, 3)


# 测试KMeans
dataSet = ML_KMeans.loadDataSet('./Ch10_K-Means/testSet2.txt')

k=3
#centroids, clusterAssment=ML_KMeans.KMeans(dataSet, k, ML_KMeans.distEclud, ML_KMeans.randCent)
#centroids, clusterAssment=ML_KMeans.KMeans(dataSet, k)
## 画出聚类结果示意图
#plt.plot(centroids[:,0],centroids[:,1],'kD')
#for i in range(len(dataSet)):
#    if clusterAssment[i,0]==0:
#        plt.plot(dataSet[i,0],dataSet[i,1],'r+')
#    elif clusterAssment[i,0]==1:
#        plt.plot(dataSet[i,0],dataSet[i,1],'bx')
#    elif clusterAssment[i,0]==2:
#        plt.plot(dataSet[i,0],dataSet[i,1],'y*')
##    else:
##        plt.plot(dataSet[i,0],dataSet[i,1],'g^')
#plt.show()

centroids, clusterAssment=ML_KMeans.biKMeans(dataSet, k)
plt.plot(centroids[:,0],centroids[:,1],'kD')
for i in range(len(dataSet)):
    if clusterAssment[i,0]==0:
        plt.plot(dataSet[i,0],dataSet[i,1],'r+')
    elif clusterAssment[i,0]==1:
        plt.plot(dataSet[i,0],dataSet[i,1],'bx')
    elif clusterAssment[i,0]==2:
        plt.plot(dataSet[i,0],dataSet[i,1],'y*')
#    else:
#        plt.plot(dataSet[i,0],dataSet[i,1],'g^')
plt.show()