# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 08:53:56 2019

@author: zhangtong

lesson_07 Canny Edge Detection
canny监测方法
在本章中，我们将学习
Canny边缘检测的概念
cv2.Canny() 函数
"""
#理论 Theory
"""
Canny边缘检测是一种常用的边缘检测算法。
它是由John F. Canny于1986年开发的。
这是一个多阶段的算法，下面我们将贯穿每个阶段。
1，降噪 Noise Reduction
由于边缘检测容易受到图像中噪声的影响，
第一步是用5x5高斯滤波器去除图像中的噪声
2,寻找图像的强度梯度
然后用Sobel核对平滑后的图像进行水平方向和垂直方向的滤波，
得到水平方向(Gx)和垂直方向(Gy)的一阶导数。
从这两幅图像中，我们可以找到每个像素的边缘梯度和方向如下

Edge_Gradient(G) = (Gx**2 + Gy**2) ** 0.5
Angle(θ) = tan(Gy/Gx) ** -1
***梯度方向总是垂直于边缘，
它是四角之一，代表垂直、水平和两个对角线方向。
3，非极大值抑制 Non-maximum Suppression
在得到梯度大小和方向后，对图像进行全扫描，
去除可能不构成边缘的任何不需要的像素，
为此，在每个像素处，检查像素在梯度方向上是否为其邻域内的局部最大值。

梯度方向垂直于边缘。点B和点C在梯度方向上。
因此，点A与点B和点C进行检查，看它是否形成局部最大值。
如果是，则将其考虑到下一阶段，否则将抑制它(使其为零)。
简而言之，得到的结果是一个边缘很细的二进制图像。

4,迟滞性界定 Hysteresis Thresholding
这个阶段决定哪些是边哪些不是。
为此，我们需要两个阈值，minVal和maxVal。
任何强度梯度大于maxVal的边都肯定是边，小于minVal的边肯定是非边，所以丢弃。
位于这两个阈值之间的根据它们的连接性对边缘或非边缘进行分类。
如果将它们连接到可靠边缘像素，则认为它们是边缘的一部分。
否则，它们也会被丢弃。见下图

边A在maxVal之上，因此被认为是可靠边。虽然C边低于maxVal，
但它与A边相连，所以这条边也被认为是有效的边，我们得到了完整的曲线。
但是B边虽然在minVal以上，与C边在同一区域，
但是没有连接到任何一个sure-edge，所以被丢弃。
因此，为了得到正确的结果，我们必须相应地选择minVal和maxVal，
这是非常重要的。
这个阶段是在消除了小像素噪声以及边缘是长线的假设下。
最终得到的是图像中的强边。
"""

#Opencv中的cany边缘监测
"""
Opencv 将上述所有功能放置于一个函数中cv2.Canny()
我们将看看如何使用它。第一个参数是输入图像。
第二个和第三个参数分别是minVal和maxVal。

第三个参数是孔径大小（aperture_size）。它是用来寻找图像梯度的Sobel内核的大小
默认情况下是3。最后一个参数是L2gradient，它指定了求梯度大小的方程
如果为真，则使用上述更精确的方程，否则使用这个函数:
Edge_Gradient(G) = |Gx| + |Gy|
默认情况下，它是假的。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.jpg',1)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()




#另外的一个例子，结合第一课的图像空间 变换，
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#    # define range of black color in HSV
#    lower_blue = np.array([0,0,0])
#    upper_blue = np.array([180,255,46])

#    # define range of red color in HSV
    lower_blue = np.array([0,50,50])
    upper_blue = np.array([10,255,255])

#    # define range of yellow color in HSV
#    lower_blue = np.array([26,43,46])
#    upper_blue = np.array([34,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    edges = cv2.Canny(frame,100,200)
#    加入下面两行，效果会好很多，主要是闭合处理图片
#    kernel = np.ones((5,5),np.uint8)
#    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('edges',edges)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

















