# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:03:47 2019

@author: zhangtong
lesson_02 Geometric Transformations of Images
图像中的几何变换
本科中将学习到
①学习将不同的几何变换应用于图像的平移、旋转、仿射变换等。
②学习到的函数：cv2.getPerspectiveTransform
"""

#转换 Transformations
"""
opencv 提供了两个转换函数，
cv2.warpAffine
cv2.warpPerspective
使用这两个函数可以任意种转换
cv2.warpAffine函数2x3变换矩阵作为输入
cv2.warpPerspective函数3x3变换矩阵作为输入
"""

#缩放 Scaling
"""
缩放的意思就是调整图片的大小（resizing）
为此opencv提供cv2.resize()函数
可以手动指定图像的大小，也可以指定缩放因子
使用不同的插值方法。
"""
import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)




#平移 Translation
"""
平移是物体位置的移动。
如果你知道(x,y)方向的位移，让它等于(Tx,Ty)，你可以创建如下的变换矩阵

M = [1 0 Tx
     0 1 Ty]

您可以将其放入类型为np的Numpy数组中。
然后将它传递给cv2.warpAffine()函数。
请参阅下面的示例了解(100,50)的移位

注意：cv2.warpAffine()函数的第三个参数是输出图像的大小，
其形式应该是(宽度、高度)。记住宽度=列数，高度=行数。
"""
import cv2
import numpy as np

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


#旋转 Rotation
"""
旋转一个角度的图像是通过变换矩阵的形式实现的
M = [cosθ -sinθ
     sinθ cosθ]


但是OpenCV提供了可调节旋转中心的缩放旋转，
所以你可以在任何你喜欢的位置旋转。
修正后的变换矩阵由

[
α  β (1-α)·center.x-β·center.y
-β α β·center.x + (1-α)·center.y
]

到
α=scale·cosθ,
β=scale·sinθ

为了找到这个转换矩阵，
OpenCV提供了一个函数cv2.getRotationMatrix2D。
检查下面的例子，它旋转图像90度相对于中心没有任何缩放。
"""
img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))




#仿射变换  Affine Transformation
"""
在仿射变换中，原图像中的所有平行线在输出图像中仍然是平行的。
为了找到变换矩阵，我们需要从输入图像中选取三个点，
以及它们在输出图像中的对应位置。然后
cv2.getAffineTransform将创建一个2x3矩阵，
该矩阵将传递给cv2.warpAffine。
"""

img = cv2.imread('drawing.png')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')


#透视变换 Perspective Transformation
"""
对于透视变换，你需要一个3x3的变换矩阵。
直线在变换之后仍然是直线。要找到这个变换矩阵，
需要输入图像上的4个点和输出图像上的对应点。
在这4个点中，有3个点不应该是共线的。
然后通过函数cv2.getPerspectiveTransform可以找到转换矩阵。
然后用这个3x3矩阵用于cv2.warpPerspective。
"""
img = cv2.imread('sudokusmall.png')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()












