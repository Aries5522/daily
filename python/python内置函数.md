map(),filter(),reduce()
==================================

map()
----------------------
map(func,seq)
传入两个参数，第一个是一个函数，第二个是一个可迭代的对象，map函数的作用就是，将seq中依次迭代，然后将seq中的数据传入到func中依次输出，保存成为一个列表。

比如：
```
a=map(lambda x : "pic"+str(x)+".png" ,range(7))

for i in a:
    print(i)
```
输出结果为：
```
pic0.png
pic1.png
pic2.png
pic3.png
pic4.png
pic5.png
pic6.png
```
写到这里就想起另外一个函数zip()
zip(a,b,c....)是python的一个内建函数，传入的参数a，b，c是一个个可迭代对象，zip的作用就是将可迭代对象中的对应的元素打包成元组，以列表的形式输出，其中a，b，c的长度可以不一致，但是zip长度按照最短的那个算。
比如：
```
a=[1,2,3,4]
b=[5,6,7]
m=zip(a,b)
for i in m:
    (k,j)=i
    print(i)
    print(k,j)
```
输出为：
```
(1, 5)
1 5
(2, 6)
2 6
(3, 7)
3 7
```


filter()
--------------
filter(function, iterable)

* function -- 判断函数。
* iterable -- 可迭代对象。

判断函数为真时候，取出该值
比如说：
```
a=filter(lambda x : x%3 ,range(10))
##输出0到9中不是3的整数倍的值
for i in a:
    print(i)
```
输出为：
```
1
2
4
5
7
8
```
reduce()
-------------------
网上主要是
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
但是我试了python3.7中没看到这个函数。

此篇完结

