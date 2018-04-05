# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 18:58:37 2018

功能：读取mat文件数据转化为jpg图片文件

@author: Flame
"""

#import logging
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


# 1. Load faces data 读取数据集
dataset = scipy.io.loadmat('olivettifaces.mat')

#dataset类型：dict
#元素：__globals__ --> []
#  __version__  --> 1.0
# faces --> array类型，（4096，400）即64*64 400张图片
# p --> 1*40 都是0.25

# u --> 4096*40

# v --> 4096*40

faces = dataset['faces']
# 读取行列数
row,col = np.shape(faces)

def test_1():
    facename = 'face/test_'+str(1)+'.jpg'
    per_image = faces[:,0].reshape(64,64)
    b=per_image.transpose()
    mpimg.imsave(facename,b,cmap=plt.cm.gray)

def test_2():
    facename = 'face/test_'+str(2)+'.jpg'
    per_image = faces[:,0].reshape(64,64)
    b=per_image.transpose()
    new_im = Image.fromarray(b)
    new_im.save(facename)
     
def genere_picture():   
    for i in range(col):
        facename = 'face/face'+str(i+1)+'.jpg'
        # 保存图片
        per_image = faces[:,i].reshape(64,64)
        b=per_image.transpose()
       #mpimg.imsave(facename,per_image,cmap=plt.cm.gray)
        mpimg.imsave(facename,b,cmap=plt.cm.gray)
    
    
if __name__ == "__main__":
    #test_2()
    genere_picture()

    