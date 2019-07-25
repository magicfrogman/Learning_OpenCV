# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:32:18 2019

@author: zhangtong

lesson 04 
Mouse as a Paint-Brush
把鼠标当成绘图刷使用
①学习如何在OpenCV中处理鼠标事件
②学习使用 cv2.setMouseCallback()
鼠标回调函数
[i for i in dir(cv2) if 'EVENT' in i]

以下代码双击鼠标左键，会产生一个圆形
"""
#
#import cv2
#import numpy as np
#
## mouse callback function
#def draw_circle(event,x,y,flags,param):
#    if event == cv2.EVENT_LBUTTONDBLCLK:
#        cv2.circle(img,(x,y),100,(255,0,0),-1)
#
## Create a black image, a window and bind the function to window
#img = np.zeros((512,512,3), np.uint8)
#cv2.namedWindow('image')
#cv2.setMouseCallback('image',draw_circle)
#
#while(1):
#    cv2.imshow('image',img)
#    if cv2.waitKey(20) & 0xFF == 27:
#        break
#cv2.destroyAllWindows()





"""
我们通过拖动鼠标来绘制矩形或圆形(取决于我们选择的模式)，
就像我们在Paint应用程序中所做的那样。
我们的鼠标回调函数有两个部分，
一个用来绘制矩形，另一个用来绘制圆。
这个具体的例子将非常有助于创建和理解一些交互式应用程序，
如对象跟踪，图像分割等。
"""

import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()