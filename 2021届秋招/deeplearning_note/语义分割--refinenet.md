RefineNet
=========================


主要贡献：

* 带有精心设计解码器模块的编码器-解码器结构；
* 所有组件遵循残差连接的设计方式。
使用空洞卷积的方法也存在一定的缺点，它的计算成本比较高，同时由于需处理大量高分辨率特征图谱，会占用大量内存，这个问题阻碍了高分辨率预测的计算研究。

DeepLab得到的预测结果只有原始输入的1/8大小。


作者认为高级语义特征可以更好地进行分类识别，而低级别视觉特征有助于生成清晰、详细的边界。所以作者认为第3点是很好的思路。基于此，作者提出了RefineNet，其主要贡献为：
提出一种多路径refinement网络，称为RefineNet。这种网络可以使用各个层级的features，使得语义分割更为精准。
RefineNet中所有部分都利用residual connections（identity mappings），使得梯度更容易短向或者长向前传，使段端对端的训练变得更加容易和高效。
提出了一种叫做chained residual pooling的模块，它可以从一个大的图像区域捕捉背景上下文信息。

![](.//images//refinenet.png)

所以，这篇论文提出了相应的编码器-解码器结构，其中编码器是ResNet-101模块，**解码器为能融合编码器高分辨率特征和先前RefineNet模块低分辨率特征的RefineNet模块。**