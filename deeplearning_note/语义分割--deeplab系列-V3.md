deeplabV3
================
1. **使用了muti-grid策略，这个很重要，主要指的是，本来的deeplab结构中，resnet--->aspp---->upsample过程中，在aspp中推荐使用不同scale的dilation rate conv层，而 multi-scale，是在 Block4、5、6、7 的三个 Residual Block 中，分别使用不同的 dilation rate，最佳的 rate 是 (1,2,1) ，注意，每个 Residual Block 中的 dilation rate 是 unit rate*multi scale rate 得到的，比如 Block 4 本身的 dilation rate = 2，那么 Block 4 中的三个 Residual Block的 dilation rate 分别是 2*(1,2,1) = (2, 4, 2)。**
2. 将 batch normalization 加入到 ASPP模块.
3. 具有不同 atrous rates 的 ASPP 能够有效的捕获多尺度信息。不过，论文发现，随着sampling rate的增加，有效filter特征权重(即有效特征区域，而不是补零区域的权重)的数量会变小，极端情况下，当空洞卷积的 rate 和 feature map 的大小一致时， 3x3卷积会退化成 1x1 ：
为了保留较大视野的空洞卷积的同时解决这个问题，DeepLabv3 的 ASPP 加入了 全局池化层+conv1x1+双线性插值上采样 的模块.

四个展望：
--------------------------------

第一种：Image Pyramid，将输入图片放缩成不同比例，分别应用在DCNN上，将预测结果融合得到最终输出

第二种：Encoder-Decoder，将Encoder阶段的多尺度特征运用到Decoder阶段上来恢复空间分辨率

第三种：在原始模型的顶端叠加额外的模块，以捕捉像素间长距离信息。例如Dense CRF，或者叠加一些其他的卷积层

第四种：Spatial Pyramid Pooling空间金字塔池化，使用不同采样率和多种视野的卷积核，以捕捉多尺度对象