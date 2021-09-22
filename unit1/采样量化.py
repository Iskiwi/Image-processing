# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 17:10
# @Author  : B612
# @File    : 采样&量化.py

import matplotlib.pyplot as plt
from skimage import data
import numpy as np

image1 = data.coffee()
# 设置像素的大小
pixel = 20
# 设置新图像的大小
image2 = np.zeros((int(image1.shape[0]/pixel), int(image1.shape[1]/pixel), image1.shape[2]), dtype="int32")
# 设置图像的灰度值级
level = 128

# 遍历图片
for i in range(image2.shape[0]):
    for j in range(image2.shape[1]):
        for k in range(image2.shape[2]):
            # 采样
            image2[i, j, k] = np.mean(image1[pixel*i: pixel*(i+1), pixel*j: pixel*(j+1), k])
            # print(image2[i][j][k])
            # 量化
            image2[i][j][k] = int(image2[i][j][k]/level)*level


plt.imshow(image2)
plt.show()
