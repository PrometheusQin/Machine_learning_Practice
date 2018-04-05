# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:26:27 2018
#KMeans算法应用：图像分割
@author: Flame
"""
from PIL import Image
from sklearn import cluster

# 载入图像并预处理
im=Image.open('0.jpg')
row,col=im.size
data=[]
for i in range(row):
    for j in range(col):
        x,y,z=im.getpixel((i,j))
        data.append([x/256.0,y/256.0,z/256.0])
label=cluster.KMeans(n_clusters=4).fit_predict(data)
label=label.reshape([row,col])
pic_new=Image.new('L',(row,col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j),int(256/(label[i][j]+1)))

#生成灰度图，并且灰度图颜色随机。
pic_new.save("result_0.jpg", 'JPEG')