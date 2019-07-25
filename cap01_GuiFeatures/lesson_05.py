# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:22:56 2019

@author: zhangtong
lesson_05
Trackbar as the Color Palette
调色器
在这里，我们将创建一个简单的应用程序，它显示您指定的颜色。
您有一个显示颜色的窗口和三个指定B、G、R颜色的跟踪条。
滑动跟踪条，相应的窗口颜色就会发生变化。
默认情况下，初始颜色将设置为黑色。

对于cv2.getTrackbarPos()函数，第一个参数是trackbar名称，
第二个参数是它所附加的窗口名称，
第三个参数是默认值，第四个参数是最大值，
第五个参数是回调函数，它在每次trackbar值更改时执行。
回调函数总是有一个默认参数，即trackbar位置。
在我们的例子中，函数什么也不做，所以我们只是传递。

trackbar的另一个重要应用是将其用作按钮或开关。
默认情况下，OpenCV没有按钮功能。所以你可以使用trackbar来获得这样的功能。
在我们的应用程序中，
我们创建了一个开关，只有在开关打开时应用程序才能工作，否则屏幕总是黑色的。
"""

import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()