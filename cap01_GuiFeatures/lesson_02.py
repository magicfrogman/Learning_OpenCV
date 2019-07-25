# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:19:03 2019
@author: zhangtong

lesson 02
Getting Started with Videos
学习读取，显示，保存图像
学习捕获图像
cv2.VideoCapture(), cv2.VideoWriter()
"""

"""
摄像头捕获图像
通常我们通过摄像头捕获实时图像，
为了捕获视频，需要创建一个VideoCapture 对象，
他的参数可以是设备索引，也可以是文件名称，
设备索引只是用来指定哪个摄像头的数字。
一旦捕获开启，会一帧一帧捕获，最后别忘记释放掉捕获对象

cap.read() 返回一个布尔值，如果读贞正确，那么返回一个真值
有时，cap无法初始化捕获对象，那种情况下代码会报错，可以使用
方法 cap.isOpened()检查初始化，如果为真，那么可以使用
cap.open().方法继续检查
playing video和网络相机类似，
设置cv2.waitKey()的适当值，当这个值越小的时候播放速度则越快，否则越慢
"""
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #[a for a in dir(cv2) if a.startswith('COLOR')]
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""
捕获视频并且一帧一帧的保存，办法非常简单，使用
cv2.imwrite()方法就可以了
①创建一个VideoWriter 对象，指定输出名称，
②然后我们应该指定FourCC代码
③设置每秒传输的帧数和帧大小
④最后一步是 isColor flag,如果为真，则与期待帧色一致，否则进行grayscale操作

FourCC是一个4字节的代码，用于指定视频编解码器。
可用代码列表可以在fourcc.org中找到。
它依赖于平台。以下编码规则在我看来正常
    在Fedora中:DIVX、XVID、MJPG、X264、WMV1、WMV2。
    (XVID更可取。MJPG的结果在大尺寸的视频。X264视频非常小)
    In Windows: DIVX (More to be tested and added)
    In OSX : (I don’t have access to OSX. Can some one fill this?)
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('20190723output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

















