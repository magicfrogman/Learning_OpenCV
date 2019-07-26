# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:54:49 2019

@author: zhangtong

lesson_03 Image Thresholding
图像二值化
学习使用全局阈值，自适应阈值，Otsu二值化等将图像二值化
函数学习cv2.threshold, 
cv2.adaptiveThreshold
"""

#建议二值化 Simple Thresholding
"""
事情在这里变得简单了，
如果像素值大于阈值，则分配一个值(可以是白色)，
否则分配另一个值(可以是黑色)。
函数使用 cv2.threshold
第一个参数是源图像，它应该是*灰度图像*
第二个参数是用于对像素值进行分类的阈值
第三个参数是maxVal，它表示如果像素值大于（有时小于）阈值则要给出的值。
OpenCV提供不同类型的阈值，它由函数的第四个参数决定。 不同的类型是：
    cv2.THRESH_BINARY
    cv2.THRESH_BINARY_INV
    cv2.THRESH_TRUNC
    cv2.THRESH_TOZERO
    cv2.THRESH_TOZERO_INV
文档中详细介绍了每种类型的含义，请在文档中检查他们
得到两个输出。第一个是retval，后面会解释。
第二个输出是我们的阈值图像。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


#二值化自适应  Adaptive Thresholding
"""
在上一节中，我们使用全局值作为阈值
在不同的照明条件和不同的区域内，不是所有的条件下，都能得到很好的效果
在这种情况下我们应该使用自适应阈值。
该算法对图像的小区域进行阈值计算。
那么我们对于相同图片上的不同区域采用不同的阈值，
结果是不同光照变化下得到不错的效果
函数有三个特殊的输入参数和一个输出参数
①Adaptive Method 决定如何计算阈值
    cv2.ADAPTIVE_THRESH_MEAN_C  阈值是邻域面积的均值
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C  阈值是权值为高斯窗的邻域值的加权和。
②Block Size 块大小它决定了附近区域的大小
③ C 是一个平均或加权平均计算后去除得到的常数
下面的代码比较了具有不同光照的图像的全局阈值和自适应阈值
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.png',0)
#img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()