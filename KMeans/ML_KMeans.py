# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:53:33 2017

@author: Flame
"""
import numpy as np
import math
import re

def loadDataSet(fileName):
    dataMat=[]
    fr = open(fileName)
    for line in fr.readlines():
        # curLine = line.strip().split()[0:2]  #只取前两维数据
        curLine = re.split(r'\t|,| *', line.strip())
        fltLine = list(map(float, curLine))
        # map(),filter()这些的返回值已经不再是list,而是iterators, 
        # 所以想要使用，只用将iterator 转换成list 即可， 比如 list(map()) 
        dataMat.append(fltLine)
    dataMat = np.array(dataMat)
    fr.close()
    return dataMat

def distEclud(vecA, vecB):
    return math.sqrt(sum(np.power(vecA-vecB, 2)))

def distSLC(pointA, pointB):
    #计算在地球上任意两个地点的距离：根据经纬度计算，目前能计算同一个半球两点距离
    #point：1*2矩阵，point[0,0]:纬度，point[0,1]:经度
    R = 6371 #地球半径
    x1 = math.cos(pointA[0]/180*math.pi)*math.cos(pointA[1]*math.pi/180)
    y1 = math.cos(pointA[0]/180*math.pi)*math.sin(pointA[1]*math.pi/180)
    z1 = math.sin(pointA[0]/180*math.pi)
    x2 = math.cos(pointB[0]/180*math.pi)*math.cos(pointB[1]*math.pi/180)
    y2 = math.cos(pointB[0]/180*math.pi)*math.sin(pointB[1]*math.pi/180)
    z2 = math.sin(pointB[0]/180*math.pi)
    Angle = math.acos(x1*x2+y1*y2+z1*z2)
    Dist = Angle*R
    return Dist

def randCent(dataSet, k):
   
    n = dataSet.shape[1]  #属性数目
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j])-minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k, 1)
    centroids=np.array(centroids)
    return centroids

def KMeans(dataSet, k, distMeans=distEclud, createCent=randCent):
    # dataSet array类型
    m = dataSet.shape[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChange = True
    kk = 0
    while clusterChange:
        kk = kk + 1
        print(kk)
        clusterChange=False
        for i in range(m):
            minDist = float('inf')
            minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,0] !=minIndex:
                clusterChange=True
            clusterAssment[i]=minIndex, minDist**2
        # 计算质心
        print (centroids)
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:]=np.mean(ptsInClust,axis=0)
    return centroids, clusterAssment
    # 返回类型：centroids：array
    # clusterAssment：mat类型

def biKMeans(dataSet, k, distMeans=distEclud):
    m = dataSet.shape[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroid0 = np.mean(dataSet,axis=0)   # array类型
    centList = [centroid0]   #centList list类型,存储质心信息，每个质心均为array类型
    for j in range(m):
        clusterAssment[j,1]=distMeans(centroid0, dataSet[j,:])**2
    # lowestSSE = float('inf')
    lowestSSE = np.sum(clusterAssment[:,1])
    while (len(centList)<k):
        for i in range(len(centList)):
            ptsIncurrCluster = dataSet[np.nonzero(clusterAssment[:, 0].A==i)[0]]  #array类型
            centroidnarray,splitClustASS=KMeans(ptsIncurrCluster, 2, distMeans)  #centroidMat  array类型
            # splitClustASS mat类型
            sseSplit = np.sum(splitClustASS[:,1])
            ssenotSplit=np.sum(clusterAssment[np.nonzero(clusterAssment[:, 0].A!=i)[0], 1])
            print('sseSplit:',sseSplit)
            if (sseSplit + ssenotSplit < lowestSSE):
                bestCenToSplit = i
                bestNewCents = centroidnarray  # 分割质心信息
                bestClustAss = splitClustASS.copy()  #创建新的mat矩阵bestClustAss，并且将splitClustASS复制进去
                #并不是直接等于，直接等于的话，两者指向同一内存
                lowestSSE = sseSplit + ssenotSplit
            #循环得到最佳的分割集合，使SSE最小
        #重新更新簇及分配结果
        #将集合分割的部分其中一块设为新簇
        # bestClustAss分到了第几块，新簇
        bestClustAss[np.array(np.nonzero(bestClustAss[:,0].A==1)[0]),0]=len(centList)
        # 分的原数据集之前的簇数，旧簇
        bestClustAss[np.nonzero(bestClustAss[:,0].A==0)[0],0]=bestCenToSplit
        print('第',len(centList),'次分割的最好的簇号：', bestCenToSplit)
        print('待分割簇的数据个数：',len(bestClustAss))
        #修改质心信息数据点
        centList[bestCenToSplit]=bestNewCents[0,:]
        centList.append(bestNewCents[1,:])
        # 原始的簇号信息和距离信息，原簇号中为bestCenToSplit的重新更新簇号和距离信息
        clusterAssment[np.nonzero(clusterAssment[:,0].A==bestCenToSplit)[0],:]=bestClustAss
    return np.array(centList),clusterAssment
    # 返回类型：质心位置信息：array
    # 距离和簇号clusterAssment：mat类型
    


        
            


