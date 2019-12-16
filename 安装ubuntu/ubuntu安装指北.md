# ubuntu安装与环境搭建


标签（空格分隔）： 折腾系统

[toc]

简介
----------------------------------------------------
介绍一下，这个文章主要要写我自己配置Ubuntu的一些软件环境的经历


##安装ubuntu16.04系统
2018.8.5尝试安装ubuntu
光影精灵4安装ubuntu教程
首先准备u 盘大于8g，去ubuntu官网下载16.04.5版本的ubuntu，64位
下载后解压缩得到iso文件
制作启动盘用ultraiso
[看介绍这个的博客][1]
具体安装可以参考下面博客
[双系统安装以及如何分区][2]
###关于如何删除efi系统分区的博客
[博客][3]

[分区efi删除][4]
##ubuntu关于python的常用指令


##启动过程中黑屏问题解决
启动黑屏解决
开机界面按e 
修改linux那行加nomodeset
这个只是暂时可开机
暂时开机后修改grub文件
```
sudo vi /etc/default/grub 或 sudo gedit /etc/default/grub
#编辑打开的文件，找到GRUB_CMDLINE_LINUX_DEFAULT那一行，在后面加上(在quiet splash后打一个空格) nomodeset（保险起见，nomodeset后面加多一个空格），保存，然后在终端输入 sudo update-grub 重启后就OK了!!!
```

修改引导启动项后更新grub然后重新开机
##搭建我所需要的python环境
安装pyenv
##pyenv安装
[相关博客][5]
**用pyenv安装python可能会出错等解决方案：**
最好先更新一下所有的安装包和库
```
sudo apt-get update
```
```
sudo apt-get install git
sudo apt-get install libbz2-dev
sudo apt-get install libssl-dev
sudo apt-get install libreadline6 libreadline6-dev
sudo apt-get install libsqlite3-dev

或者一条sudo apt-get install libbz2-dev libssl-dev libreadline6 libreadline6-dev libsqlite3-dev
```

安装pyenv,后面可以省略 不用安装这个工具,anaconda已经很好用了,不需要这个来控制anaconda的版本
```
sudo apt-get install curl git-core
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
sudo gedit ~/.bashrc
#添加下面这段：
export PYENV_ROOT="${HOME}/.pyenv"

if [ -d "${PYENV_ROOT}" ]; then
  export PATH="${PYENV_ROOT}/bin:${PATH}"
  eval "$(pyenv init -)"
fi
#然后激活bashrc
source ~/.bashrc
#可安装python版本查看
pyenv install --list
```
这里还有一种方式，当你查看可以安装的列表之后可以直接用安装python环境
```
pyenv install 3.6.5##比如安装3.6.5
```
还可以选择安装anaconda之后，在anaconda里面安装python。（这种办法主要是conda安装库比较方便），直接创建的话，可以使用pycharm来安装包

下面是使用pyenv来建立虚拟环境：
```
pyenv virtualenv 2.7.1 env271 #2.7.1是一个已经安装好等python版本 env271是名字
pyenv activate env271 #切换到虚拟环境
pyenv deactivate  #回到系统环境
rm -rf ~/.pyenv/versions/env271/ #删掉虚拟环境
```
我们其实还可以设置不同的环境范围：
```
pyenv global 3.5.1
 pyenv local 2.7.11
 pyenv shell 2.7.11
```


##更换pyenv和anaconda镜像源
[博客][6]
按照博客操作之后安装anaconda3-4.4.0
如果按照博客安装pip失败则可以采用离线下载安装的方式来安装。
原因应该主要是pip的环境变量有点问题。按照这种方法也可以不用更改镜像源地址。
离线下载地址https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
也可以直接按照之前博客那个网站下载速度还比较快
1. 下载对应版本的.sh文件。
对应版本是指，运行pyenv install anaconda3-4.4.0时候会有提示在下载Anaconda3-4.4.0-Linux-x86_64.sh文件，所以在镜像源里找到对应一样的下载下来就好了，速度炒鸡快
2. 把下载好的.sh文件放在/.pyenv/cache中，（没有的话自己新建该文件夹），再继续运行pyenv install anaconda3-4.4.0进行安装即可。
##安装anaconda
打开终端
```
pyenv install anaconda3-4.4.0
```
安装anaconda如果没办法使用conda指令
需要更改环境变量，记得在最后一行添加（此处容易炸裂，记得谨慎修改环境变量）
此处记得一定要修改anaconda的绝对路径地址信息。不要完全按照教程

参考博客：[博客][7]
##更新全局pip源更换
&emsp;仅针对ubuntu下，windows下估计也差不多;首先是
&emsp;操作方法：
&emsp;&emsp;第一查看隐藏文件，看看在```~```下面有没有```.pip```这个文件夹，没有的话就创建一个，然后```cd ~/.pip```接下来编辑一个文件，还是没有就新建一个```gedit pip.conf```然后里面加上内容：
```
[global] 
index-url = https://pypi.tuna.tsinghua.edu.cn/simple 
[install] 
trusted-host = pypi.tuna.tsinghua.edu.cn 
```
##更换pip镜像源（这个有问题，暂时别用，用上面的）
安装好anaconda之后创建py3.6的环境
```
conda create --name your_env_name python=3.6 #用conda来创建虚拟环境
conda create --name py3.6 python=3.6  #例如创建3.6的环境
```
准给更换pip镜像源

使用清华大学镜像源，还是很靠谱的。
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```
重要：conda在某个虚拟环境下安装必须要source activate （py3.6） 某某环境，然后在这个环境中安装东西，不然，包全部都安装在conda/bin 下面会出现混乱的，我觉得哈，但是总之改了这个之后，安装啥都很快。
##pip安装包和模块
###安装一些常用的依赖库
####如何使用anaconda来管理环境
见博客[知乎关于anaconda基本指令][8]
给哪个环境安装：
先打开环境，linux下在终端输入：
```
conda activate py3.6 #进入环境
conda list #显示安装的包
conda deactivate py3.6 #离开环境
which python #查看当前python版本
pip install --upgrade pip #更新pip
conda upgrade    --all #为避免出错可以直接更新所有
```
在当前环境下安装一些包的指令
```
pip install opencv-python #install cv2
pip install scipy
pip install matplotlib
pip install docopt
```
来一条组合命令
```
pip3 install opencv-python scipy matplotlib docopt pillow numpy
```
###离线下载安装模块的办法
##卸载cuda
按照之前安装的过程，最后cuda8.0和cudnn5版本下只能支持tensorflow到1.4版本及以下，因此决定重新安装cuda9版本加cudnn7版本，从而安装1.6版本以上的tensorflow。
首先就是卸载之前安装的cuda8.0
之前的安装是使用rubfile和deb安装的使用不同的方法
[卸载cuda8.0][9]
首先进入root用户，没有root用户的话，以root身份运行以下指令。（这是是用）
```
sudo -i  进入root身份
```
然后运行
```
apt autoremove cuda （使用apt指令的时候确保没有其他程序进程正在安装或者卸载程序，例如系统更新，否则会报错等待其他更新完毕在进行）
```
卸载残留的cuda文件。之前安装的是cuda8.0所以删除8.0。
```
cd /usr/local/
rm -rf cuda-8.0/
```

若是使用rubfile安装的，以卸载cuda9.2为例
```
cd /usr/local/cuda-9.2/bin
sudo ./uninstall_cuda_9.2.pl
```
卸载残留文件
```
cd /usr/local/
rm -rf cuda-8.0/
```
可以完成卸载。
##安装cuda8.0
官网下载cuda版本
然后进去文件夹之后，打开终端运行run文件，无线空格阅读完毕，accept接受
然后不安装驱动，其他全部是yes和默认,切记切记切记切记

```
sudo sh cuda_8.0.61_375.26_linux.run
```
参照博客[安装cuda][10]
全部完毕后重启
最后还有验证手段
```
sudo reboot
```
##安装cudnn
参照cuda8.0安装的过程我自己安装了cuda9.0的版本，然后对应官网去下载安装了cudnn7.3.0的版本。
这块之前一直有问题，现在自己重新全部安装一遍
安装好了cuda之后去nvida官网[nvidia cudnn下载网站][11]下载对应的cuda版本的cudnn
一般是下载第一个lib那个文件，然后解压，然后有两个copy指令
打开终端，cd到./CUDA/include，执行命令
```
sudo cp cudnn.h /usr/local/cuda-9.0/include/
```
cd到./CUDA/lib64，执行命令：
```
sudo cp lib* /usr/local/cuda-9.0/lib64/
```
这里苏和安装教程中有一点点和我的不一样，就是更新软链接之类的东西，但是我在cuda9.0+cudnn7.3.0的版本中没有进行后续的操作，运行tensorflow还是可以成功。

##安装一些模块
```
conda install numpy pyyaml mkl setuptools cmake cffi
```
来一条组合命令
```
pip install opencv-python scipy matplotlib docopt tqdm setproctitle colorama  tensorboardX --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple/
```
##安装pytorch
从官网上面点出来（尽量用pip3指令安装，因为查了下貌似pip是默认安装给anaconda中自带的py版本，而pip3则是安装到自己创建的py3.6版本）我是先把.whl文件下载后打开终端进入py3.6环境后安装的直接
```
pip3 install /home/peng/下载/torch-0.4.0-cp36-cp36m-linux_x86_64.whl
pip3 install torchvision
```
就可以安装好、
后面是其他的安装方式，可不用细看
```
conda install pytorch torchvision -c pytorch
```
这样自动安装的是0.1版本,但是我是很想装0.3版本的
,我记得以前弄过这个但是我忘了,哎,还是记笔记是最好的
[这个博客很完美，可用][12]
```
pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl
pip3 install torchvision
```
我要安装python35的pytorch：
```
pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.1-cp35-cp35m-linux_x86_64.whl
pip3 install torchvision
```
安装python3.6的pytorch，（安装速度较慢400m）还是要先进入py3.6的环境

```
source activate py3.6 #进入环境
pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.1-cp36-cp36m-linux_x86_64.whl
pip3 install torchvision
```
####安装后测试
安装成功pytorch和torchvision后，打开ipython，或者pycharm，输入：
```
import torch
```
可能会出现报错的情况，如下所示：
```
ImportError: numpy.core.multiarray failed to import
```
这是因为numpy的版本需要更新，直接使用pip更新numpy：
```
pip install numpy
```
进入之后import之后
```
print(torch.cuda.is_avilable())
true
```
至此，PyTorch安装成功.
##安装tensorflow
我记得的是安装的指令很简单，但是可以直接pip安装或者是直接conda（分三步）安装
先进入环境
```
source activate py3.6
pip3 install tensorflow-gpu=1.6.0(如果没有记错的话)
```
如果电脑已经安装了conda


    ***（谨慎貌似有点问题）参考[2.7下安装清华源tensorflow][13]然后套用到3.6 版本下（缺陷就是清华源上的gpu版本的只更新到1.5.0左右所以每法安装比较），过程如下：
    打开清华源的tensorflow的网站[清华源tensorflow][14]，找到自己版本对应的tensorflow。
    ```
    pip install --upgrade https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/gpu/tensorflow_gpu-1.５.0rc1-cp27-none-linux_x86_64.whl
    ```
    1.5.0：为Tensorflow版本号
    cp27：为对应于python2.7版本
    X86_64：表示64位系统32位系统都能够兼容*** 

我选择安装的是gpu版本的 tensorflow，如果出现问题参考[tensorflow大全][15]安装
[tensorflow][16]
[这个也还不错][17]
[这个是tensorflow安装并且有实例运行][18]但是这个是只针对2.7的版本的，比较落后。
py3.6上安装，不明白为什么，安装之后pycharm中总是会报错，所以一直安装失败。未解决
py2.7上尝试安装下。
目前遇到的问题：ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory
这个提示的是cuda版本不匹配，但是为什么广爷的是安装成功的。
这块后面自己全部安装成功了，两种环境下：
python2.7+cuda9.0+cudnn7.3.0（9.0对应）+tensorflow1.6.0
python3.6+cuda9.0+cudnn7.3.0（9.0对应）+tensorflow1.10.0

##安装pycharm和cmd_markdown按照教程走
###pycharm
[pycharm][19]
以后不要进博客直接安装的指令，进入pycharm中bin文件夹：
```
sh ./pycharm.sh
```
###安装网易云
[网易云][20]
##折腾nvidia驱动
###方法1：命令行直接装驱动，问题是下载速度太慢
```
ubuntu-drivers devices #查看你该装什么样的驱动
sudo apt-get install nvidia-390 #安装390对应的型号
sudo apt-get update 
sudo reboot #更新并重启
```
###方法2：自行去官网下载驱动[nvidia驱动网站][21]
自行下载好.run文件
先卸载已有驱动
```
#for case1: original driver installed by apt-get:
sudo apt-get remove --purge nvidia*
#for case2: original driver installed by runfile:
sudo chmod +x *.run
sudo ./NVIDIA-Linux-x86_64-384.59.run --uninstall
```
[nvidia驱动安装博客][22]
###方法3：使用ppa下载，此方法网速巨慢，需要翻墙
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-378 nvidia-prime

```
**##ubuntu16.04 加gtx1050ti折腾安装驱动**
安装之前关掉uefi安全启动关闭
今天终于弄好了，原来是万恶之源是双系统双显卡的原因，最开始系统更改grub文件是默认用intel集成显卡来打开屏幕
正确的安装方法是：
```
ubuntu-drivers devices #查看你该装什么样的驱动
sudo apt-get install nvidia-390 #安装390对应的型号
sudo apt-get update 
sudo reboot #更新并重启
```
**因为之前下载过了，可能会比较快，安装过程结束的时候会要求更改安全启动模式为禁用。至于重新启动的问题还是要在安装完成显卡驱动之后更改grub文件，其实就是之前的nomodeset没用，更改为acpi_osi=linux，详情见博客[双显卡如何安装N卡驱动][23]
哇，弄了好久终于搞定**。
```
sudo vi /etc/default/grub 或 sudo gedit /etc/default/grub
```
x

```
nvidia-smi#查看驱动属性
nvidia-settings#设置驱动
```
###关于安装驱动之后循环启动的问题
不要直接选择重装系统
在登录界面按e，会进入grub界面，修改nomodeset先临时进入系统再说，或者直接进入非图形界面卸载invidia相关的驱动，在重启就好了，这一段写的太简单，后面有机会把他补齐。

恢复文件属性
```
sudo chmod 644 /etc/modprobe.d/blacklist.conf
```
更行内核
```
sudo update-initramfs -u
```
##关于LINUX的常用指令
打开默认grub指令并修改
```
sudo gedit /etc/default/grub
sudo update-grub  #然后重启
```

###修改环境变量导致指令失效
切记以后不要随便修改环境变量
[环境变量恢复][24]
##windowsubuntu系统时间不一致的解决办法
[bantu和windows时间不一致解决][25]
其实很简单
先在ubuntu下更新一下时间，确保时间无误：
```
sudo apt-get install ntpdate
sudo ntpdate time.windows.com
```
然后将时间更新到硬件上：
```
sudo hwclock --localtime --systohc
```
重新启动完美解决问题。

##使用root身份
```
sudo -i，输入当前用户密码后以root权限登录shell，无时间限制。使用exit或logout退出
```

/home/peng/ubuntu/NVIDIA-Linux-x86_64-390.77.run

##双屏教程

```
想去左边的屏，需要往右滑，想去右边的屏，需要往左滑。不过还好有  xrandr，试了一下，三条命令：

 xrandr     (查看显示屏设置)
 xrandr --output HDMI2 --auto --primary
 xrandr --output eDP1 --right-of HDMI2 --auto
还算比较好理解：
xrandr 是查看和设置的命令

HDMI2 是显示屏的名字

auto 是自动分辨率

primary 是主屏

eDP1 是笔记本显示屏的名字

--right-of HDMI2  就是放在HDMI2 显示器的右边
```


  [1]: https://blog.csdn.net/ZingHd/article/details/80036449
  [2]: https://blog.csdn.net/ysy950803/article/details/52643737
  [3]: https://jingyan.baidu.com/article/91f5db1b3c289f1c7f05e3a6.html
  [4]: https://blog.csdn.net/weixin_39837402/article/details/79961912
  [5]: https://blog.csdn.net/databatman/article/details/53955828
  [6]: https://blog.csdn.net/l1216766050/article/details/77526455
  [7]: https://blog.csdn.net/caomin1hao/article/details/78341568
  [8]: https://www.zhihu.com/question/58033789
  [9]: https://blog.csdn.net/huang_owen/article/details/80811738
  [10]: https://blog.csdn.net/u010837794/article/details/63251725/
  [11]: https://developer.nvidia.com/rdp/cudnn-archive
  [12]: https://ptorch.com/news/145.html
  [13]: https://blog.csdn.net/qq_35451572/article/details/79598308
  [14]: https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/gpu/
  [15]: https://www.tensorflow.org/install/install_sources#common_installation_problems
  [16]: https://blog.csdn.net/y1250056491/article/details/78670710/
  [17]: https://blog.csdn.net/qq_35451572/article/details/79598308
  [18]: https://blog.csdn.net/zhengleibo/article/details/78049925
  [19]: https://blog.csdn.net/zhuanshu666/article/details/73554885
  [20]: https://blog.csdn.net/qq910689331/article/details/78819964
  [21]: https://www.geforce.cn/drivers
  [22]: https://blog.csdn.net/ghw15221836342/article/details/79571559
  [23]: https://blog.csdn.net/mmz_xiaokong/article/details/79416156
  [24]: https://zhidao.baidu.com/question/2116592127561248347.html
  [25]: https://blog.csdn.net/UNIONDONG/article/details/78317612