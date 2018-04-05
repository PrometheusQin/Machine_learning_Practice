# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:36:44 2018
#人脸图像特征抽取与对比使用NMF和PCA
@author: Flame
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition
import scipy.io

n_row=2
n_col=3
n_components=n_row*n_col
image_shape=(64,64)

def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    plt.figure(figsize=(2*n_col,2.26*n_row))
    plt.suptitle(title,size=16) #标题和字号大小
    for i,comp in enumerate(images):
        plt.subplot(n_row,n_col,i+1)
        #vmax=max(comp.max(),-comp.min())
        plt.imshow(comp.reshape(image_shape).transpose(),cmap=plt.cm.gray)
        # ,interpolation='nearest',vmin=-vmax,vmax=vmax)
        plt.xticks(())
        plt.yticks(())
        #去除子图坐标轴标签
    plt.subplots_adjust(0.01,0.05,0.99,0.93,0.04,0.)


dataset = scipy.io.loadmat('olivettifaces.mat')
faces = dataset['faces'].T  #400*4096 样本*维数
#face1=faces[0,:].reshape(64,64)
#im1=Image.fromarray(face1)

#显示前六个原始图像
plot_gallery("First centered Olivetti faces", faces[:n_components])

#方法一：协方差矩阵为4096*4096
pca = decomposition.PCA(n_components=6,whiten=True)
pca.fit(faces)
pca.n_features_ #特征个数4096
pca.n_components_  #降维数 6
#前k个特征向量,即代表特征脸
components_ = pca.components_ #6*4096
new_faces_data=pca.transform(faces) #400*6 降维后数据，成功
plot_gallery("Eigenfaces - PCA using randomized SVD",components_[:n_components]) #画出特征脸

#方法二：协方差矩阵为400*400
faces_2=faces.T  #4096*400
pca = decomposition.PCA(n_components=6,whiten=True)
pca.fit(faces_2)
pca.n_features_ #特征个数400
pca.n_components_  #降维数 6
components_2 = pca.components_ #6*400
eigenfaces2=np.array(np.mat(faces_2)*np.mat(components_2.T)).T 
#6*4096
plot_gallery("Eigenfaces_2 - PCA using randomized SVD",eigenfaces2[:n_components]) #画出特征脸

#使用NMF非负矩阵分解找特征脸
nmf=decomposition.NMF(n_components=6, init='nndsvda', tol=5e-3)
nmf.fit(faces)
nmf_eigenface=nmf.components_ #6*4096

plot_gallery("Non-negative components - NMF",nmf_eigenface[:n_components]) #画出特征脸







