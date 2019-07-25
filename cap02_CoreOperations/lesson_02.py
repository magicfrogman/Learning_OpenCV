# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:50:21 2019

@author: zhangtong
lesson_02 Arithmetic Operations on Images
图像中的算数运算
①学习几种图像的算术运算，如加法、减法、位运算等。
②学习用到的函数cv2.add(), cv2.addWeighted() 
"""

#图像加法  Image Addition
"""
你可以使用cv2.add() 对图像相加，或者numpy操作res = img1 + img2
两张图片必须具有相同的类型，深度，或者第二张图片仅仅是一个标量
对于两种加法实现的办法，是有本质不同的，OpenCV加法是 饱和运算，
Numpy加法是 取模运算。
当您添加两个图像时，它将更加可见。OpenCV函数将提供更好的结果。
所以最好还是使用OpenCV函数。
"""
import numpy as np
import cv2
#
#x = np.uint8([250])
#y = np.uint8([10])
#print(cv2.add(x,y)) # 250+10 = 260 => 255
#print(x+y)          # 250+10 = 260 % 256 = 4

#
#cv2.imshow('image',x)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#图像融合 Image Blending
"""
这也是图像的相加，
但是给图像不同的权重，
因此它给人一种混合或透明的感觉。图像按下式添加
g(x) = (1-α)f0(x) + αf1(x)
α取值从0-1，你可以干一些非常酷的将一张图片转换为另一张
这里我拍了两张照片来把它们混合在一起。第一幅图像的权值为0.7，
第二幅图像的权值为0.3。
cv2.addWeighted()对图像应用如下公式。
"""
#img1 = cv2.imread('me.png')
#img2 = cv2.imread('sis.png')
#dst = cv2.addWeighted(img1,0.1,img2,0.9,0)
#
#cv2.imshow('image',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#位运算 Bitwise Operations
"""
这包括位和、OR、NOT和XOR操作。
它们在提取图像的任何部分
(我们将在接下来的章节中看到)、定义和处理非矩形ROI等方面都非常有用。
下面我们将看到一个关于如何更改图像特定区域的示例。
"""
# Load two images
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


