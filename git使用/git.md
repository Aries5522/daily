[TOC]

星期日, 29. 九月 2019 07:14下午 
author：彭清

#一份完整的github使用教程
小白的github入门之路

##首先去github上申请一个账户是必须的
至于具体的申请步骤的话百度搜索得到

##建立本地电脑和远程仓库的链接
本篇主要讲的是ubuntu下使用github

###ubuntu下使用ssh链接github远程仓库

####第一步：创建线下本机的秘钥

在终端下面

```
ssh-keygen -t rsa -C "youremail@example.com"
```
之后可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

####第二步，登陆GitHub

打开“Account settings”，“SSH Keys”页面，然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容。

需要注意的是，github允许添加多个SSH Keys，假定我们有自己的笔记本和实验室/办公室的电脑，需要将每台电脑的key添加到github，然后可以使用每台电脑往github推送了。

然后，在github上创建一个名为dailywork的空的仓库（不包含README文件）。
将本地仓库与github仓库相关联并推送内容包含下面两步：

首先在本地文件夹下打开终端
```
git init
```
这是初始化一个git仓库，在本文件夹下有个隐藏文件夹.git,代表初始化成功
```
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:Aries5522/dailywork.git
#这一步经常会出错。报错：fatal: 远程 origin 已经存在。
#解决办法是先删除远程配置，然后再添加
git remote rm origin
git remote add origin git@github.com:Aries5522/dailywork.git

git push -u origin master
```
这样就完成了将线下的仓库提交到github上的整个过程了。这个只是初步教程。这是第一次提交时候需要的代码后面简化一下
```
git add .
git commit -m“标签”
git push
```
这三个指令就足够应付了

>另外，git pull将远程的仓库下载到本地
如果添加整个文件夹那个和添加文件一样

```
git add .
#这里add整个文件夹就好了
git commit -m "first commit"
git remote add origin git@github.com:Aries5522/dailywork.git
#这一步经常会出错。报错：fatal: 远程 origin 已经存在。
#解决办法是先删除远程配置，然后再添加
git remote rm origin
git remote add origin git@github.com:Aries5522/dailywork.git

git push -u origin master
```
[知乎——github](https://zhuanlan.zhihu.com/p/44181150) 


还有一种情况本地，重装系统之后，那么闲杂的电脑需要重新和之前的远仓库建立链接，