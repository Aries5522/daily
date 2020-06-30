deeplabv1
=====================
Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs(Deeplab v1)

主要贡献:
* 空洞卷积
* 空间金字塔池化
* 全连接条件随机场


1. 首先它是个 VGG-16
2. 然后为了使图像语义分割更准确，5 个 max-pooling 层 skip 了后两个（具体实现上，看G站上的代码，似乎没有去除，而是保留了后两个 max-pooling ，只是将 stride = 2 改为 stride = 1，kernal = 3），最后卷积层的输出整体 stride 从 32x 下降至 8x。
3. 参考 Uno Whoiam：空洞卷积（Dilated Convolution）：有之以为利，无之以为用 ，由于后两个 max-pooling 影响了其后的卷积层，使其视野分别下降了 2x 和 4x，为了保持其原来的视野，便将其改成空洞卷积，dilation 分别为 2 和 4，理念与DRN一致。
4. 当然，它也是一个全卷积网络 Uno Whoiam：FCN：从图片分类到像素分类 ，即将全连接层替换成 [公式] 的卷积层，输出和原特征图大小一致的特征图，对每个像素分类。
5. 使用双线性插值上采样 8x 得到和原图大小一致的像素分类图。
6. 使用 CRF（条件随机场）使最后分类结果的边缘更加精细(V3以及之后就不用了，简单来说使用了马尔科夫场的思想，对某一个像素分类的时候考虑到他周围像素点的类别)