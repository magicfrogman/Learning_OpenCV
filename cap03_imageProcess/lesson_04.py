# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:53:02 2019

@author: zhangtong
lesson_04 Smoothing Images
图像平滑
本课内容：
通过各种低通滤波器模糊图像
应用自定义滤波器到图像(2D卷积)2D convolution
"""

#二维卷积(图像滤波) 2D Convolution ( Image Filtering )
"""
与一维信号一样，图像也可以用各种低通滤波器(LPF)、高通滤波器(HPF)等进行滤波。
LPF有助于去除噪声，模糊图像等。
HPF过滤器有助于在图像中找到边缘。

OpenCV提供了一个函数cv2.filter2D()来将内核与图像进行卷积。
例如，我们将尝试对图像进行平均滤波。下面是一个5x5平均滤波内核

关于卷积的知识，可以通过马同学的文章来了解，具体链接如下：
https://www.matongxue.com/madocs/32.html

K = 1/25 [
1 1 1 1 1            
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
]

运算过程如下：
①将内核保持在像素之上
②添加此内核下方的所有25个像素（可以想象成上下两层，这里用的below，就是正下方，对齐）
③取其平均值，用新的平均值替换中心像素（可以看成是一种信息有损压缩）
④对图像中所有像素进行如上操作。具体卷积图像和说明，可以参考：
https://mlnotebook.github.io/post/CNN1/
试试以下的代码
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()



#图像滤波(图像平滑)
"""
图像模糊是通过将图像与低通滤波核进行卷积来实现的。
它对消除噪音很有用。它实际上删除了图像中的高频内容(如:噪声、边缘)。
在这个操作中，边缘有点模糊。(当然，也有一些模糊技术不会模糊边缘)。
OpenCV主要提供四种类型的模糊技术。
①均值  Averaging
这是通过将图像与规范化的框过滤器进行卷积来实现的。
它只是取内核区域下所有像素的平均值并替换中心元素。
这是由函数cv2.blur()或cv2.boxFilter()完成的。
有关内核的更多细节，请查看文档。
我们应该指定内核的宽度和高度。
一个3x3归一化的框式滤波器如下图所示
k = 1/9 [
1 1 1
1 1 1
1 1 1
]

如果不希望使用规范化的框过滤器，请使用cv2.boxFilter()。
向函数传递一个参数normalize=False。
类似上面使用卷积进行图像处理，下面使用cv.blur函数实现
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.jpg')

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

#高斯滤波 Gaussian Blurring
"""
在这种情况下，用高斯核函数代替了盒形滤波器。
这是通过函数cv2.GaussianBlur()完成的。
我们应该指定内核的宽度和高度，它们应该是正的和奇数的。
我们还应该分别指定X和Y方向的标准差，sigmaX和sigmaY。
如果只指定sigmaX，则sigmaY与sigmaX相同。
如果两者都是零，则从内核大小计算它们。
高斯模糊是消除图像中高斯噪声的有效方法。

如果有需要，可以使用函数cv2.getGaussianKernel()创建高斯内核
下面的代码展示高斯滤波
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.jpg')
blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

#中值滤波 Median Blurring
"""
这里，函数cv2.medianBlur()取内核区域下所有像素的中值，然后用这个中值替换中心元素。
这种方法可以有效的针对图像中的噪点。
有趣的是，在上面的过滤器中，中心元素是一个新计算的值，
它可以是图像中的像素值，也可以是一个新值。
***但是在中值模糊中，中心元素总是被图像中的某个像素值所替代。有效降低噪音。
它的内核大小应该是一个正奇数。

在这个演示中，我为原始图像添加了50%的噪声，并应用了中值模糊。检查结果
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noise_img.jpg')
blur = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])


#双向滤波    Bilateral Filtering
"""
cv2.bilateralFilter() 在保持边缘锋利的同时，对噪声去除非常有效。
但是它的速度却比上述几个都要慢。

我们已经看到高斯滤波器取像素周围的a邻域并求其高斯加权平均，
高斯滤波器是一个单独的空间函数，即在滤波时考虑附近的像素。
它不考虑像素是否具有几乎相同的强度。
它不考虑像素是否是边缘像素。它也模糊了边缘，这不是我们想要的。

双侧滤波器在空间上也采用高斯滤波器，
但多了一个像素差的函数

空间高斯函数确保只考虑附近像素的模糊，
而强度差高斯函数确保只考虑与中心像素强度相似的像素的模糊

模糊处理采用高斯差函数，模糊处理时只考虑与中心像素强度相近的像素。
所以它保留了边缘，因为边缘上的像素会有很大的强度变化。
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bilateralFilter_img.png')
blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])