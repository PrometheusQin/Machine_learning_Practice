# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:16:29 2018

# 该程序是对博客http://blog.jobbole.com/86905/的复现。复习一下计算的各个公式。
@author: Flame
"""
import numpy as np

# a为10个样本，每个样本2维数据
a = np.array([[2.5,2.4],[0.5,0.7],[2.2,2.9],[1.9,2.2],[3.1,3],[2.3,2.7],[2,1.6],[1,1.1],[1.5,1.6],[1.1,0.9]])


row,col=a.shape

# 计算列方向的均值np.mean(a,axis = 0)
# 等价于 a.mean(axis=0)或者a.mean(0)
mean_a=np.mean(a,0) 
print(mean_a)
new_a=np.mat(a-mean_a)

#使用np.cov计算得到的协方差--
# array([[ 0.61655556,  0.61544444],
#       [ 0.61544444,  0.71655556]])

covMat=np.cov(new_a,rowvar=0)


#直接使用定义计算
#matrix([[ 0.61655556,  0.61544444],
#       [ 0.61544444,  0.71655556]])

cov_2 = new_a.T*new_a/(row-1)


#数据标准化后计算协方差
# 计算标准差，使用的是样本个数row，不是row-1计算的，和np.std结果一样。
#a_std1：matrix([[ 0.7449161]])
#a_std2：matrix([[ 0.80305666]])
#a_std3： matrix([[ 0.7449161 ,  0.80305666]])

a_std1=np.sqrt(new_a[:,0].T*new_a[:,0]/(row))
a_std2=np.sqrt(new_a[:,1].T*new_a[:,1]/(row))

a_std3=np.std(new_a,axis=0)

#标准化之后的a
normal_a = new_a/a_std3
# 计算协方差矩阵

# array([[ 1.11111111,  1.0288103 ],
#      [ 1.0288103 ,  1.11111111]])
nor_cov_mat =normal_a.T*normal_a/(row-1)

nor_covMat=np.cov(normal_a,rowvar=0)

# 得到两个协方差矩阵
#计算特征值和特征向量
k=1
#eigValue,eigVects=np.linalg.eig(covMat)
eigValue,eigVects=np.linalg.eig(nor_cov_mat)
#使用和不适用标准差计算的结果一致。在本例中无影响
eigValInd = np.argsort(eigValue)  #从小到大排序
eigValInd = eigValInd[:-(k+1):-1] #倒序后k个数
redEigVects = eigVects[:,eigValInd]
lowDdataMat = new_a * redEigVects


