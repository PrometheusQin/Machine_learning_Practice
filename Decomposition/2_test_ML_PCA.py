# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:03:04 2018

@author: Flame
"""
import matplotlib.pyplot as plt
import ML_PCA 
def test_iris(): #鸢尾花数据降维测试
    fileName = "./Ch13_dimensionality_reduction/iris.data.txt"
    dataSet,y=ML_PCA.load_data(fileName, delim=',')
    k=3
    lowData, reconmat, eigValper= ML_PCA.PCA(dataSet, k)
    red_x,red_y = [],[]
    blue_x,blue_y = [],[]
    green_x,green_y = [],[]
    for i in range(len(lowData)):
        if y[i]==0:
            red_x.append(lowData[i][0])
            red_y.append(lowData[i][1])
        elif y[i]==1:
            blue_x.append(lowData[i][0])
            blue_y.append(lowData[i][1])
        else:
            green_x.append(lowData[i][0])
            green_y.append(lowData[i][1])
    plt.figure(1)
    plt.axis([0.9, k+1, 0, 1])
    plt.grid()
    cosum = []
    for i in range(k):
        if i == 0:
            cosum.append(eigValper[i])
        else:
            cosum.append(cosum[i-1] + eigValper[i])
    plt.plot(range(1,k+1),eigValper,'ob-',range(1,k+1),cosum,'*r-')
    plt.figure(2)
    plt.scatter(red_x,red_y,c='r',marker='x')
    plt.scatter(blue_x,blue_y,c='b',marker='D')
    plt.scatter(green_x,green_y,c='g',marker='.')
    plt.show()
    
def test_secom():
    fileName = "./Ch13_dimensionality_reduction/secom.data"
    dataSet = ML_PCA.load_data_2(fileName, delim=' ')
    dataSet = ML_PCA.replaceNanWithMean(dataSet)
    k=30
    lowData, reconmat, eigValper = ML_PCA.PCA(dataSet, k)
    plt.figure(1)
    plt.axis([0, k+1, 0, 1])
    plt.grid()
    cosum = []
    for i in range(k):
        if i == 0:
            cosum.append(eigValper[i])
        else:
            cosum.append(cosum[i-1] + eigValper[i])
    plt.plot(range(1,k+1),eigValper,'ob-',range(1,k+1),cosum,'*r-')
    return dataSet
    
    
if __name__ == "__main__":
    #test_iris()
    dataSet = test_secom()