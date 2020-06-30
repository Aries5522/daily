第一题：全景拼接
====================

步骤1、图像读取（imread）

步骤2、将原始彩色图像转换为灰度图像（cvtColor）

步骤3、图像缩放（resize）

步骤4、使用ORB算法进行特征点检测(或者sift算子，特征点检测)（orb.detectAndCompute）

步骤5、将左右两幅图像中的特征点进行匹配（bf.match）

步骤6、使用匹配点计算从左图到右图的旋转矩阵M（findHomography）

步骤7、对M求逆，得到从右图到左图的旋转矩阵H（np.linalg.inv(M)）

步骤8、将右图旋转到左图的成像平面（warpPerspective）

步骤9、找到左右两幅图像的重叠区域的左边界和右边界。

步骤10、对于只在左图中出现的区域，使用左图中的像素填充拼接后的图像区域。

步骤11、对于只在右图中出现的区域，使用右图中的像素填充拼接后的图像区域

步骤12、对于左右图像的重叠区域，使用如下方法计算拼接后的像素值：

alpha = srcImgLen / (srcImgLen + testImgLen)

res[row, col] = np.clip(img1[row, col] * (1-alpha) + warpImg[row, col] * alpha, 0, 255)




难度系数:	★★★☆

描述：在全景拼接中，会用到许多 OpenCV 函数，练习的是组装积木的能力。本题基于全景拼接问题衍生出三道题,		练做积木的能力。
1) 不使用 OpenCV 中的 warpPerspective 函数，手写一个图像 bilinear	inverse	warping 算
法。
2)	不使用 OpenCV 中的 findHomography 函数，手写一个单应性矩阵估计。
3)	不使用 OpenCV 中的 RANSAC，手写一个 RANSAC 鲁棒估计。
要求：手动实现 OpenCV 的三个函数,	并和 OpenCV 原生函数对比效
