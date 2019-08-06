# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:36:07 2019

@author: zhangtong

lesson_06 Image Gradients
图像梯度
在本课程中我们将学习到
找到图像的梯度，边缘等。
我们将学到的函数有 cv2.Sobel(), cv2.Scharr(), cv2.Laplacian()  等
"""

#理论 Theory
"""
OpenCV提供三种类型的梯度滤波器或高通滤波器，
Sobel、Scharr和Laplacian。
下面我们将看到每一种方法的使用
"""

#索贝尔及斯查尔  边缘监测及衍生  Sobel and Scharr Derivatives
"""
索贝尔算子是一种高斯平滑加微分的联合算子,更抗噪音
你可以指定导数的方向，垂直或水平(分别由参数yorder和xorder表示)
您还可以通过参数ksize指定内核的大小，
如果ksize = -1，则使用3x3的Scharr滤波器，其结果优于3x3的Sobel滤波器。请参阅使用内核的文档。
"""

#拉普拉斯边缘监测   Laplacian Derivatives
"""
它计算由关系给出的图像的拉普拉斯变换，
Δsrc=(δ**2src/δx**2) + (δ**2src/δy**2)
其中每个导数都是用索贝尔导数求出来的。
如果ksize = 1，则使用下面的kernel进行过滤
kernel = [
0  1 0
1 -4 1
0  1 0
]
"""

#代码  Code
"""
下面的代码显示了单个图表中的所有运算符。 所有内核都是5x5大小。 
输出图像的深度为-1，以获得np.uint8类型的结果。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.png',0)#必须采用灰度处理，不然效果会差很多

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()


#一个重要的事情！ One Important Matter!
"""
在上一个示例中，输出数据类型为cv2.CV_8U或np.uint8。但是有一个小问题，
黑白转换为正斜率（具有正值），而白转黑转换为负斜率（具有负值）
所以，当你将数据转换为np.uint8时，所有负斜率都为零。简单地说，这个边缘被抛弃了。

如果你想更好的检测两条边缘，更好的选择是将输出数据保存为更高级的数据类型，
比如cv2.CV_16S, cv2.CV_64F等。
取它的绝对值，然后再转换回cv2.CV_8U
下面的代码演示了水平Sobel过滤器过程以及结果的差异。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('box.png',0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()

























