# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:51:30 2019

@author: zhangtong
lesson_01
Basic Operations on Images
图像基础操作
    访问像素值并修改他们
    图像属性的访问
    图像区域设置（ROI ）
    拆分合并图像（边缘检测，多元感知）
"""
#
import cv2
import numpy as np
img = cv2.imread('messi6.jpg')
#
#img[100,100] = [255,255,255]
#
#cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
##更好的办法
#img.item(10,10,2)
#img.itemset((10,10,2),100)
#img.item(10,10,2)


"""
Image ROI
"""
#ball = img[280:340, 330:390]
#img[180:240, 230:290] = ball

#分割和合并图像通道
"""
有时你需要单独处理图像的B、G、R通道。然后需要将BGR图像分割为单个平面。
或者，您可能需要将这些单独的通道连接到BGR映像。你可以简单地做这件事
"""

b,g,r = cv2.split(img)
#img = cv2.merge((b,g,r))

"""
假设，你想让所有的红色像素都为零，你不需要像这样分割然后让它等于零。
您可以简单地使用Numpy索引，这样更快。
"""
#img[:,:,2] = 0


"""
加入边框
如果想在图像周围创建边框，比如相框，可以使用cv2.copyMakeBorder()函数。
但它在卷积运算、补零等方面有更多的应用。这个函数接受以下参数
src --输入图像
top bottom left right 边框宽度，以对应方向的像素数为单位
borderType 边框类型，可以是以下类型
    cv2.BORDER_CONSTANT 添加一个固定的彩色边框。
    该值应该作为下一个参数给出。
    cv2.BORDER_REFLECT 边框将是边框元素的镜像反射，
    如下所示:fedcba|abcdefgh|hgfedcb
    cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT
    同上，但有一个微小的变化，像这样:gfedcb|abcdefgh|gfedcba
    cv2.BORDER_REPLICATE
    最后一个元素被复制，就像这样:aaaaaa|abcdefgh|hhhhhhh
    cv2.BORDER_WRAP
    无法解释，它会是这样的:cdefgh|abcdefgh|abcdefg
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()


















