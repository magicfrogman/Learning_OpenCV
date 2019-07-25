# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:49:57 2019

@author: zhangtong
lesson 03
Drawing Functions in OpenCV
opencv中的绘图函数

cv2.line(), 线
cv2.circle() ,圈 
cv2.rectangle(), 矩形
cv2.ellipse(), 椭圆
cv2.putText() 文字
以上方法具有共同的参数
img 要在其中绘制图形的图像
color 形状的颜色。对于BGR，将其作为元组传递，
    例如:(255,0,0)对于blue。对于灰度，只需传递标量值。
    
thickness  线条或圆形等的厚度如果对于像圆圈这样的闭合图形通过-1，
    它将填充形状。 默认厚度= 1
lineType: 线的类型，是否8连接，抗锯齿线等。默认情况下，它是8连接的。cv2。
    直线AA给出了反锯齿的曲线，这看起来很不错。
"""

"""
划线，
需要输入线段的开始和结束坐标，
"""
import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

#Drawing Rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#Drawing Circle
cv2.circle(img,(447,63), 63, (0,0,255), -1)


#Drawing Ellipse
"""
要绘制椭圆，我们需要传递几个参数。一个参数是中心位置(x,y)。
下一个参数是轴长(长轴，短轴)。角是椭圆逆时针方向旋转的角度。
起始角和结束角表示从主轴顺时针方向测量的椭圆圆弧的起始和结束。
也就是说，给定值0和360表示整个椭圆。
要了解更多细节，请查看cv2.ellipse()的文档。
下面的例子在图像的中心绘制了一个半椭圆。
"""
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)





#Drawing Polygon 锯齿
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))



#Adding Text to Images:

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)




#show it 
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



