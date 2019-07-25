# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:43:03 2019

@author: zhangtong
lesson_03 Performance Measurement and Improvement Techniques
绩效评估和改进技术
通过计算消耗时间及其他一些技术，改进代码质量

在图像处理中，由于每秒要处理大量的操作，
所以必须让代码不仅提供正确的解决方案，
而且以最快的方式提供正确的解决方案。
所以在这一章中，你会学到
①度量代码性能
②提高代码性能的一些技巧
③会使用到的函数 cv2.getTickCount, cv2.getTickFrequency etc
除了opencv,python还提供了time模块用于度量执行时间
另外一个模块profile 有助于我们得到代码细节报告.
比如代码中的每个函数花费了多少时间,
"""

#度量性能  Measuring Performance with OpenCV
"""
cv2.getTickCount 函数返回一个引用事件
(比如打开机器的时刻)之后到调用该函数的时刻的时钟周期数
如果在函数执行之前和之后调用它，就会得到用于执行函数的时钟周期数。

cv2.getTickFrequency函数返回时钟周期的频率，或者每秒时钟周期的数量。
因此，要计算以秒为单位的执行时间，可以执行以下操作
e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()


我们将通过以下示例进行演示。下面的示例应用中值滤波，
其内核大小为奇数，范围从5到49。(不要担心结果会怎样，这不是我们的目标)
"""
img1 = cv2.imread('messi5.jpg')

e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)
#
#time 模块也可以这样做。
#而不是cv2。函数的作用是:使用time.time()函数。然后取两倍的差。


#opencv 的默认优化 Default Optimization in OpenCV
"""
许多OpenCV功能都使用SSE2，
AVX等进行了优化。它还包含未经优化的代码。 
因此，如果我们的系统支持这些功能，
我们应该利用它们（几乎所有现代处理器都支持它们）。 
编译时默认启用它。 因此，OpenCV在启用时运行优化代码，
否则运行未优化代码。 
您可以使用cv2.useOptimized（）来检查它是否已启用/禁用，
并使用cv2.setUseOptimized（）来启用/禁用它。
让我们看一个简单的例子。
# check if optimization is enabled
In [5]: cv2.useOptimized()
Out[5]: True

In [6]: %timeit res = cv2.medianBlur(img,49)
10 loops, best of 3: 34.9 ms per loop

# Disable it
In [7]: cv2.setUseOptimized(False)

In [8]: cv2.useOptimized()
Out[8]: False

In [9]: %timeit res = cv2.medianBlur(img,49)
10 loops, best of 3: 64.1 ms per loop
"""

#ipython 中的性能度量
"""
有时您可能需要比较两个类似操作的性能。
IPython提供了一个神奇的命令%timeit来执行此操作。
它运行代码几次以获得更精确的结果。
同样，它们也适用于测量单行代码。
In [10]: x = 5

In [11]: %timeit y=x**2
10000000 loops, best of 3: 73 ns per loop

In [12]: %timeit y=x*x
10000000 loops, best of 3: 58.3 ns per loop

In [15]: z = np.uint8([5])

In [17]: %timeit y=z*z
1000000 loops, best of 3: 1.25 us per loop

In [19]: %timeit y=np.square(z)
1000000 loops, best of 3: 1.16 us per loop

Python标量操作比Numpy标量操作快。
因此，对于包含一两个元素的操作，Python标量优于Numpy数组。
当数组的大小稍微大一点时，Numpy就会发挥作用。
"""


#优化建议
"""
尽量避免在Python中使用循环，尤其是双循环/三循环等。它们本质上很慢。

将算法/代码矢量化到最大可能范围，因为Numpy和OpenCV针对向量运算进行了优化。

利用缓存一致性。

除非需要，否则永远不要复制数组。 尝试使用视图。 阵列复制是一项昂贵的操作。
"""





















