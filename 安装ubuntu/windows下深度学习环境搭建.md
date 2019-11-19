# windows下环境搭建

标签（空格分隔）： 折腾系统

[toc]

---
##安装anaconda来作为环境和包的管理软件
###安装过程以及一些常用的指令
打开anaconda promote
```
conda info --envs  #查看当前的python环境
conda create --name py3.6 python=3.6  #创建一个名字为py3.6的python3.6的环境
conda activate py3.6 #进入py3.6环境
conda deactivate #退出当前python环境（和上面那条一起与linux下指令不一样）
python -m pip install --upgrade pip #更新pip
```
进入环境后
使用pip和conda都可以安装包