# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:47:18 2019

@author: zhangtong
lesson_01 Changing Colorspaces
改变颜色
学习在不同的颜色空间之间改变图像。
①在本课中，你将学习如何将图片从一个color-space转换到另外一个，
比如 BGR <---> Gray, BGR <---> HSV 等等
②除此之外，我们将提取视频中的彩色对象
③cv2.cvtColor(), cv2.inRange() 学习函数
"""
#改变色彩空间，Changing Color-space
"""
OpenCV中有150多种颜色空间转换方法。
但我们将只研究两个最广泛使用的，BGR<-->gray和BGR<--->HSV。
"""
