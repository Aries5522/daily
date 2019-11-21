mmdetection
=================

来自于open—mmlab的mmdetection框架使用入门
----------------------------------------------------



首先在github上按照说明文档搭建
[mmdetection](https://github.com/open-mmlab/mmdetection)

所需要的环境配置我并没有按照说明文档里面直接在anaconda下面单独创建一个open-mmlab环境，而是使用自己的本身创建的环境，只需要安装运行mmdetection所需要的安装包就够了。以下就是所安装的所有包了
```
mmcv>=0.2.10
numpy
matplotlib
six
terminaltables
pycocotools
torch>=1.1
torchvision
imagecorruptions
albumentations>=0.3.2
```

首先可以按照说明文档测试一下能否跑通coco数据集的目标检测

