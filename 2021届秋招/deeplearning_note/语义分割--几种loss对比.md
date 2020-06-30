pytorch中几种Loss对比
===========================

---


##L1Loss

```
CLASS torch.nn.L1Loss(size_average=None, reduce=None, reduction='mean')
```
可以单纯的理解为两个向量的距离，x和y形状任意，但是总的元素个数要是确定的。（最好一样shape）
其中reduction可以为mean和sum分别是求元素插值绝对值的均值和总和.
例子：
> loss = nn.L1Loss()
> input = torch.randn(3, 5, requires_grad=True)
> target = torch.randn(3, 5)
> output = loss(input, target)
> output.backward()

##MSELoss
```
CLASS torch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')
```
通常称为L2损失，最小均方误差，x和y形状任意，但是总的元素个数要是确定的。（最好一样shape）
例子：
> loss = nn.MSELoss()
> input = torch.randn(3, 5, requires_grad=True)
> target = torch.randn(3, 5)
> output = loss(input, target)
> output.backward()

##CrossEntropyLoss
```
CLASS torch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')
```
交叉熵损失
适用于多分类，分为c类的话，并且输入的形状最好是（minibatch，c）或者是（minibatch，c，d1，d2...）的tensor