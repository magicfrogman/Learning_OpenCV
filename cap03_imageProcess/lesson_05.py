# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:11:47 2019
@author: zhangtong

lesson_05 Morphological Transformations
转变形态
在本课中，我们将学习形态操作，比如腐蚀，膨胀，打开，关闭等
用到的函数有 cv2.erode(), cv2.dilate(), cv2.morphologyEx()
"""

#理论 Theory
"""
形态学变换是一些基于图像形状的简单操作
它通常在二进制图像上执行。
它需要两个输入，一个是原始图像，
另一个是决定操作性质的结构化元素(structuring element)或内核(kernel)。
它决定了操作的性质。侵蚀和膨胀是两种基本的形态操作符。然后它的变体形式，
如打开，关闭，梯度等也发挥作用。
"""

#1. Erosion 侵蚀
"""
侵蚀的基本思想就像土壤侵蚀一样，它侵蚀前景对象的边界(总是尽量保持前景为白色)。
那么它是做什么的呢?内核在图像中滑动(就像在2D卷积中一样)。
只有当内核下的所有像素都是1时，原始图像中的像素(1或0)才会被认为是1，否则就会被侵蚀(变为0)。
结果是，所有边界附近的像素都会被丢弃，这取决于内核的大小。
因此，前景对象的厚度或大小减小，或只是图像中的白色区域减小。
它有助于去除小的白色噪声(正如我们在色彩空间一章中看到的)，分离两个连接的物体等。
在这里，作为一个例子，我将使用一个包含所有1的5x5内核。让我们看看它是如何工作的
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('j.png',0)#这里采用了灰度处理模式，所以结果可能颜色不太一样，可以不选参数
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
plt.imshow(erosion)

#2    膨胀 Dilation
"""
它正好与侵蚀相反。这里，如果内核下至少有一个像素为1，则像素元素为1
所以它增加了图像中的白色区域或前景对象的大小增加。
***通常，在去除噪音等情况下，侵蚀之后是膨胀。
因为，侵蚀消除了白噪音，但也缩小了我们的物体。
我们把它放大。由于噪声消失了，它们不会再出现，
但我们的目标面积增加了。它在连接对象的破碎部分时也很有用。
"""

dilation = cv2.dilate(img,kernel,iterations = 1)

#3    开放 Opening
"""
opening 是侵蚀后再膨胀的另外一个叫法，
如上所述，它在消除噪声方面很有用。这里我们使用函数cv2.morphologyEx()
"""
img = cv2.imread('opening.jpg',0)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.imshow(opening)


#4    封闭 Closing
"""
closing与opening相反，先膨胀之后是侵蚀。
它在封闭的前景对象内部的噪点或对象上的小黑点时非常有用。
"""
img = cv2.imread('closing.jpg',0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.imshow(closing)

#5    梯度形变    Morphological Gradient
"""
它是图像膨胀和侵蚀的区别。
结果将看起来像对象的轮廓。
"""
img = cv2.imread('j.png',0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.imshow(gradient)

# 6 Top Hat #这个实在有点懵逼，不知道怎么翻译了
"""
它是输入图像和打开图像之间的区别。下面的示例是针对9x9内核完成的。
"""
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

#7. Black Hat
"""
它是输入图像关闭和输入图像之间的差异。
"""
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


#结构元素    Structuring Element
"""
在前面的示例中，我们在Numpy的帮助下手动创建了一个结构化元素。
它的形状是矩形，但在某些情况下，您可能需要椭圆/圆形内核。 
为此，OpenCV有一个函数cv2.getStructuringElement（）。
 您只需传递内核的形状和大小，即可获得所需的内核。
"""
# Rectangular Kernel   矩形
cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# Elliptical Kernel 椭圆
cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

# Cross-shaped Kernel 十字形内核
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

