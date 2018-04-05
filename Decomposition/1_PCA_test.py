# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:47:45 2018

@author: Flame
"""
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
# 加载数据方法一：直接加载sklearn中数据
#from sklearn.datasets import load_iris
# 加载鸢尾花数据集导入数据
#data = load_iris()
#y = data.target
#X = data.data

# 加载数据方法二：读取本地文件中数据
X = []
y = []
fw = open("./Ch13_dimensionality_reduction/iris.data.txt")
for line in fw.readlines():
    #print(line)
    lineArr = line.strip().split(',')
    print(lineArr)
    #print(lineArr[0],lineArr[1],lineArr[2],lineArr[3])
    temp = np.array([float(lineArr[0]),float(lineArr[1]),float(lineArr[2]),float(lineArr[3])])
    X.append(temp)
    if lineArr[4]=='Iris-setosa':
        y.append(0)
    elif lineArr[4]=='Iris-versicolor':
        y.append(1)
    else:
        y.append(2)
fw.close()
pca = PCA(n_components=2)
# 加载PCA算法，设置降维后主成分数目为2
reduced_X = pca.fit_transform(X)
# 对原始数据进行降维，保存在reduced_X中
red_x,red_y = [],[]
blue_x,blue_y = [],[]
green_x,green_y = [],[]
for i in range(len(reduced_X)):
    if y[i]==0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i]==1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])
plt.scatter(red_x,red_y,c='r',marker='x')
plt.scatter(blue_x,blue_y,c='b',marker='D')
plt.scatter(green_x,green_y,c='g',marker='.')
plt.show()