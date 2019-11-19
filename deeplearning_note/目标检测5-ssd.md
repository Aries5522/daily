ssd网络
=============
和yolo相比
* 多尺度的feature map：基于VGG的不同卷积段，输出feature map到回归器中。这一点试图提升小物体的检测精度。
* 更多的anchor box，每个网格点生成不同大小和长宽比例的box，并将类别预测概率基于box预测（YOLO是在网格上），得到的输出值个数为(C+4)×k×m×n，其中C为类别数，k为box个数，m×n为feature map的大小。