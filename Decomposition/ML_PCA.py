# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:18:44 2018

@author: Flame
"""
import numpy as np
def load_data(fileName, delim='\t'): 
    #载入带鸢尾花数据导入
    X = []
    y = []
    fw = open(fileName)
    for line in fw.readlines():
        #print(line)
        lineArr = line.strip().split(delim)   
        if len(lineArr)<3:
            continue
        else:
            temp = np.array([float(lineArr[0]),float(lineArr[1]),float(lineArr[2]),float(lineArr[3])])
            X.append(temp)
            if lineArr[4]=='Iris-setosa':
                y.append(0)
            elif lineArr[4]=='Iris-versicolor':
                y.append(1)
            else:
                y.append(2)
    fw.close()
    return np.mat(X), y

def load_data_2(fileName, delim='\t'): 
    fr = open(fileName)
    lineArr = [line.strip().split(delim) for line in fr.readlines()]
    #print(lineArr[0][0],type(lineArr[0][0]),len(lineArr),len(lineArr[0]))
    dataArr = [list(map(float, line)) for line in lineArr]
    #print(len(dataArr),len(dataArr[0]))
    fr.close()
    return np.mat(dataArr)
    
 
def PCA(dataSet, k=99999):
    meanVals = np.mean(dataSet,axis=0) #对列操作
    meanRemove = dataSet.T - meanVals.T
    covMat = np.cov(dataSet,rowvar=False)
    eigValue,eigVects = np.linalg.eig(covMat)
    eigValInd = np.argsort(eigValue)  #从小到大排序
    sumeigValue = np.sum(eigValue)
    eigValInd = eigValInd[:-(k+1):-1] #倒序后k个数
    eigValper = eigValue[eigValInd]/sumeigValue
    redEigVects = eigVects[:,eigValInd]
    lowDdataMat = np.mat(meanRemove) * np.mat(redEigVects)
    reconMat = (lowDdataMat * redEigVects.T) + meanVals
    return np.array(lowDdataMat),reconMat,eigValper
# 缺失数据用Nan使用平均值来代替
def replaceNanWithMean(dataSet):
    numFeat = np.shape(dataSet[0])[1]
    for i in range(numFeat):
        meanVal = np.mean(dataSet[np.nonzero(~np.isnan(dataSet[:,i].A))[0],i])
        dataSet[np.nonzero(np.isnan(dataSet[:,i].A))[0],i] = meanVal
    return dataSet
    

    

