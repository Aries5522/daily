Fast-R-CNN
==================
不同于Rcnn线切割然后分类，这样CNN分类网络运行次数太多，
导致速度很慢，那么该文章提出先将图片提取特征，的到feature map
用selective search算法提出ROI（region of interset），
映射到feature map，对单独的ROI进行 ROI pooling得到等长的
feature vector，进行正负样本整理，按照batch送入RCNN
网络分类回归，统一损失。

ROI分成等分成目标个数的网格，每个网格进行maxpooling
得到长度一样的ROI feature-vector

文章借鉴地方：


* multi-loss traing相比单独训练classification确有提升
+ multi-scale相比single-scale精度略有提升，但带来的时间开销更大。一定程度上说明CNN结构可以内在地学习尺度不变性
* 在更多的数据(VOC)上训练后，精度是有进一步提升的
* Softmax分类器比"one vs rest"型的SVM表现略好，引入了类间的竞争
* 更多的Proposal并不一定带来精度的提升`