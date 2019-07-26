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
对于图像转换，我们使用函数cv2.cvtColor(input_image, flag)
flag决定转换的类型
BGR<-->Gray 使用 flag cv2.COLOR_BGR2GRAY
BGR<-->HSV 使用 flag cv2.COLOR_BGR2HSV
要获得其他flag，只需在Python终端中运行以下命令
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

HSV色相范围为[0,179]，饱和度范围为[0,255]，值范围为[0,255]。
不同的软件使用不同的尺度。
因此，如果要比较OpenCV值和它们，需要对这些范围进行标准化。
"""
#对象追踪 Object Tracking


"""
现在我们知道了如何将BGR图像转换为HSV，我们可以使用它来提取一个彩色对象。
在HSV中，表示颜色比RGB颜色空间更容易。
在我们的应用程序中，我们将尝试提取一个蓝色的对象。方法是这样的
①获取视频中的每一帧
②将BGR转换为HSV色彩空间
    HSV颜色空间通过将颜色从饱和度和伪光照中分离出来来抽象颜色(色调)。
    这使得它对于实际应用程序(如您提供的应用程序)非常实用。
③我们对HSV图像设置一个蓝色范围的阈值
④现在只提取蓝色对象，我们可以对图像做任何我们想做的事情。
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#    # define range of blue color in HSV
#    lower_blue = np.array([110,50,50])
#    upper_blue = np.array([130,255,255])
    
#    # define range of black color in HSV
#    lower_blue = np.array([0,0,0])
#    upper_blue = np.array([180,255,46])

#    # define range of red color in HSV
#    lower_blue = np.array([0,50,50])
#    upper_blue = np.array([10,255,255])

    # define range of yellow color in HSV
    lower_blue = np.array([26,43,46])
    upper_blue = np.array([34,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
"""
上例中仅仅是最简单的目标追踪办法，一旦你学会了轮廓函数，你可以干许多事情，
比如找到物体质心的轮廓，并且跟踪它就可以了，
仅仅通过在相机前移动你的手和许多其他有趣的东西来画图。
如何找到hsv 值去追踪呢？万能的stackoverflow在此~~：
另外你可以使用函数 cv2.cvtColor()
您只需传递所需的BGR值，而不是传递图像。例如，要查找绿色的HSV值，
请在Python终端中尝试以下命令
"""

green = np.uint8([[[0,255,0 ]]])#RBG
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)






















