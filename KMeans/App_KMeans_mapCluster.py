# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 01:18:57 2018

@author: Flame
"""
from GoogleMapAPI_2 import Geocoding
import ML_KMeans
import re
import numpy as np
import matplotlib.pyplot as plt


def getGeofromfile(fileName):
    #从原始文件中读取信息，利用google地图获得地址的经纬度,保存到my_places.txt中
    fw = open("./Ch10_K-Means/my_places.txt", 'w')
    for line in open(fileName).readlines():
        line = line.strip()
        lineArr = re.split(r'\t',line)
        #print(lineArr)
        address=lineArr[1] + ' ' + lineArr[2]
        #print(address)
        lat,lng = Geocoding(address)
        print(lineArr[0], lat, lng)
        if lat==0 or lng==0:
            print('error fetching')
        else:
            fw.write('%s\t%f\t%f\n'  % (line,lat,lng))
    fw.close()
    
    
def clusterClubs(k=5):
    dataList=[]  #存储每一个位置的经纬度
    fw = open("./Ch10_K-Means/my_places.txt")
    for line in fw.readlines():
        line = line.strip()
        lineArr = line.split('\t')
        dataList.append([float(lineArr[3]), float(lineArr[4])])
    dataSet = np.array(dataList)
    Centroids, clusterAss = ML_KMeans.biKMeans(dataSet,k,ML_KMeans.distSLC)
    fig = plt.figure()
    rect = [0.1, 0.1, 0.7, 0.8]
    scatterMatkers=['s','o','^','p','d','v','h','>','<']
    axprops = dict(xticks=[],yticks=[])
    ax0=fig.add_axes(rect, label='ax0',**axprops)
    imgP=plt.imread('./Ch10_K-Means/Portland.png') #加载图像
    ax0.imshow(imgP)
    ax1 = fig.add_axes(rect, label='ax1',frameon=False)
    for i in range(k):
        ptsIncurrCluster = dataSet[np.nonzero(clusterAss[:,0].A==i)[0],:]
        markerStyle = scatterMatkers[i % len(scatterMatkers)]
        ax1.scatter(ptsIncurrCluster[:,1], ptsIncurrCluster[:,0], marker=markerStyle,s=90)
    ax1.scatter(Centroids[:,1],Centroids[:,0],marker='+',s=300)
    plt.show()
    
#在开始阶段执行一次生成my_places.txt即可
#fileName='./Ch10_K-Means/portlandClubs.txt'
#getGeofromfile(fileName)
    
if __name__ == '__main__': 
    clusterClubs(5)
