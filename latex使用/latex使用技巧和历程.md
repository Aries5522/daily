# latex使用技巧和历程

标签（空格分隔）：latex使用

[toc]

#latex安装过程

   之前在windows上安装由于不熟悉操作安装的自带的texworks编译器，贼难用，建议使用texstudio简单好用，强烈推荐。
安装过程参考这个文章还是蛮不错的。
https://www.jianshu.com/p/d185aad1f915

学习过程：
latex有许多不同的编译器，我之前安装过CTEX但是不知道怎么使用就卸载了，后面安装了texworks，目前正在使用中，安装过程很繁杂。
ubuntu下的安装很简单，但是时间要很久，具体可以参考视频，我觉得讲的很好。
[这个是bilibili上的视频教程，基于texstudio][1]
安装好texstudio之后呢，首先需要进去option界面更改下界面的语言CN-zh就是中文简体。
然后更改下默认编译的方式，一般要用的中文的话需要改为celatex方式。关于编译方式的简介，latex是直接编译，pdflatex是直接会输出pdf文档的编译方式，但是新型的编译方式celatex会对utf-8的编码方式的文档直接编译，对中文的编译很友好。

声明：以下很多内容出自latex使用中文文档，安装之后在终端使用
```
texdoc lshort-zh  %打开中文参考文档很好用
```
可以打开此中文文档。
后面准备自己按照视频都去实现一遍，然后后面需要就直接从自己的文档里面拷贝源代码就好了。舒服

#这几天又看了好多视频
重新接上上次的教程，很久之前重装系统再也没有用过latex了，最近做视频作业的时候想着全部用这个写一下文档，于是开始了作死之路。
但是这次的安装过程异常不顺利，好像教研室的网可以打开texstudio官网但是寝室的打不开，tex live安装还是简单，直接默认安装就ok了，安装之后，总是无法编译，试过更改环境变量也没有用，但是最后找到一篇博客，意外解决。
建议安装好tex live之后更新一下，防止和其他编译器出现不相容无法编译的问题。

这是error log
···
Use of uninitialized value $ver in scalar chomp at E:/texlive/2018/tlpkg/TeXLive/TLWinGoo.pm line 206. Use of uninitialized value $ver in substitution (s///) at E:/texlive/2018/tlpkg/TeXLive/TLWinGoo.pm line 207. Use of uninitialized value $ver in substitution (s///) at E:/texlive/2018/tlpkg/TeXLive/TLWinGoo.pm line 207.
···
以下为解决办法：cmd用管理员身份打开
···
fmtutil-sys --all
···
然后等待更新完。留下了不学无术的泪水，无敌关键。

好了然后把在overleaf上写好的复制过来。
#怎么去创建一个新的源文件
创建一个新的文件并保存下来，但是这个文件命名需要英文。

讲下语法：
首先要创建你写作的内容，一般分三种，第一种是文章article ，book ，letter
我们常用的肯定是article
写作框主要分为两部分，上面的一部分是导言区，主要包括文章类型，然后是要使用的宏包，一般包括celatex（中文编译包）amsmath（数学公式包）等等，然后还有文章的title data author等信息，但是这些在文章中要起作用的话需要在环境开头写上\maketitle使之生效。
#下面讲解下几大板块
##第一大板块：
简单的文本和框架的写作。
首先，导演部分写作好了之后，那么可以开始整个文档目录，也就是结构部分的写作了。这块特别简单，简单来说就是构建文章主体部分。然后一级二级三级标题的书写。
注意正文部分空行等于word里面的分段。不然字都会连在一起。

···
\begin{document}

\maketitle #让导演部分能显示出来

\begin{abstract}
简单摘要
\end{abstract}
\section{基本原理} ##一级标题
\section{算法和程序设计}
\subsection{算法设计}##二级标题
\subsection{程序流程}
\begin{itemize}
	\item 读入图片
	\item 提取RGB分量
	\item 计算出其他颜色空间的分量
	\item 将其他分量可视化
	\item 计算相关系数
\end{itemize}
\section{仿真实验与结果分析}
\subsection{实验}
\subsection{结果分析}
\section{结论}

\begin{thebibliography}{99}  ##参考文献部分
	\bibitem{ref1}冈萨雷斯, et al., 数字图像处理，第三版.  
	\bibitem{ref2}田玉敏，梁若莹 ，计算机彩色输入输出设备常用颜色空间及其转换
\end{thebibliography}
\end{document}

···

##第二大板块：
首先这里说一下数学公式的插入
```
$这样可以在行内插入公式$

\begin{equation}
公式内容，这样可以插入行间公式，但是只能插入一个公式而且会带标号。
\end{equation}

\begin{equation*}
公式内容，这样可以插入行间公式，加了星号就没有公式标号
\end{equation*}
```

公式，图片，表格插入
##第三大板块：



  [1]: https://www.bilibili.com/video/av16002978/?p=4