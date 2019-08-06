# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:44:47 2019

@author: zhangtong

lesson_08 图像金字塔 Image Pyramids
本章中，我们将学习到图像金字塔
①我们将使用图像金字塔创建一个新的水果~橘子~苹果（Orapple） :D
②我们将学习使用cv2.pyrUp(), cv2.pyrDown()
"""
#1 理论
"""
通常，我们使用的图像大小是固定的
但是在某些场景（occassions）下，我们需要处理同一副图像的不同分辨率
例如，需要查询图像中某一样东西的时候，比方说面部，我们不能确定对象在图像中的大小。
在这种情况下，我们需要创建一组具有不同分辨率的图像，并在所有图像中搜索对象。
这些具有不同分辨率的图像集被称为图像金字塔
(因为当它们被保存在一个堆栈中时，最大的图像在底部，最小的图像在顶部，看起来像一个金字塔)。
有两种金字塔类型，①高斯金字塔②拉普拉斯金字塔

高斯金字塔中的高阶(低分辨率)是通过去除低阶(高分辨率)图像中的连续行和列而形成的。
然后，较高层的每个像素由具有高斯权重的底层5个像素的贡献形成。
这样，图像M×N就变成了图像M/2 × N/2。面积减小到原来的四分之一。它被称为倍频程（Octave）。
同样的模式在金字塔的顶部继续(即，分辨率降低)。同样地，当膨胀时，每层的面积变成4倍。
我们可以使用cv2.pyrDown()和cv2.pyrUp()函数找到高斯金字塔。
"""
#import cv2
#import numpy as np
#from matplotlib import pyplot as plt
#img = cv2.imread('messi5.jpg')
#lower_reso = cv2.pyrDown(higher_reso)
##现在，您可以使用cv2.pyrUp()函数沿着图像金字塔向下走。
#higher_reso2 = cv2.pyrUp(lower_reso)
"""
请记住，higher_reso2不等于higher_reso，因为一旦降低了分辨率，就会丢失信息。 
下图是从前一种情况下的最小图像创建的金字塔下3级。 将其与原始图像进行比较：
"""

#拉普拉斯金字塔
"""
拉普拉斯金字塔是由高斯金字塔构成的。它没有唯一的函数。拉普拉斯金字塔图像就像边缘检测一样。
它们用于图像压缩。
拉普拉斯金字塔中的水平是由高斯金字塔中的水平与高斯金字塔上水平的扩展形式之差形成的
拉普拉斯层次的三个层次如下所示(为了增强内容，对对比度进行了调整)
"""


#图像金字塔在图像融合中的应用 Image Blending using Pyramids
"""
金字塔的一个应用是图像融合
例如，在图像拼接中，您需要将两个图像堆叠在一起，但是由于图像之间的不连续，这看起来可能不太好。
在这种情况下，使用金字塔进行图像混合可以无缝地进行混合，而不会在图像中留下太多数据。
其中一个经典的例子是两种水果的混合，橘子和苹果。现在就看结果本身来理解我在说什么
"""
import cv2
import numpy as np,sys

A = cv2.imread('apple.png')
B = cv2.imread('orange.png')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)

"""
请先查看附加资源中的参考资料，它有关于图像混合、拉普拉斯金字塔等的完整图表细节。
简单地做如下工作
①加载苹果和橘子的两个图像
②找到苹果和橘子的高斯金字塔(在本例中，层数为6)
③从高斯金字塔，找到他们的拉普拉斯金字塔
④现在将苹果的左半部分和橙子的右半部分加入到拉普拉斯金字塔的每一层中
⑤最后从这个联合图像金字塔，重建原始图像。
扩展阅读
http://pages.cs.wisc.edu/~csverma/CS766_09/ImageMosaic/imagemosaic.html
"""
























