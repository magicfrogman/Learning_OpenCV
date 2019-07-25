# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:08:20 2019
@author: zhangtong
learning OpenCV
lesson 01
Getting Started with Images
加载图片，显示并保存
学习三个函数
cv2.imread()
cv2.imshow()
cv2.imwrite()
"""
"""
读取图片
cv2.IMREAD_COLOR 加载彩色图像，任何图像的透明效果都将被忽略，默认选项
cv2.IMREAD_GRAYSCALE 灰度处理模式
cv2.IMREAD_UNCHANGED 包括阿尔法通道的图像加载
这三种参数可以以此被1, 0 或者 -1替换

※即使路径是错误的，opencv不会抛出异常而是打印一条错误记录而已，这里需要特别注意
"""

#读取图片
import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)

"""
#显示图片
使用cv2.imshow()显示一张图片，窗口会自动适应图片尺寸
第一个参数是窗体的名称，第二参数是我们的图像，可以生成许多窗体，但是名称必须唯一

cv2.waitKey() 键盘映射函数，它的参数是以毫秒为单位的时间，
这个函数将等待设置的毫秒时间在按下任意键后，如果0秒过去，那么他将无限期的等待键盘按键事件

cv2.destroyAllWindows()简易的摧毁我们创建的所有窗口，
如果我们只想摧毁指定的某个窗口，可以使用
cv2.destroyWindow() ，在括号内传递窗口名称作为参数即可
"""
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
 cv2.namedWindow() 指定窗口大小
"""
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
cv2.imwrite('messigray.png',img)
写出函数
"""
cv2.imwrite('messigray.png',img)

"""
加总在一起
读取图片，显示图片，按esc直接跳出，啥也不做，按s
"""
import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()