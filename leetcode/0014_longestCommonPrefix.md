最长公共前缀
===========================
题目链接：
[最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

![题目描述](images/image1.14.png)

自己思路：
+ 第一种当然是暴力求解：让列表中的每个元素当成字符串，依次判断同位置上的字符是否一样、不一样结束。
+ 或者前两个查找公共字符串，在于后面的的第三个查找，依次进行。

参考别人的；
+ 神奇解法一：感觉算取巧吧，python中字符串可以比较大小，根据ASCII码来比较。所以只需要找到，最大最小值，对比最大最小值的公共前缀就好了、
  ```
  class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:return ""
        max_str = max(strs)
        min_str = min(strs)
        for i in range(min(len(max_str), len(min_str))):
            if min_str[i] == max_str[i]:
                continue
            else:
                return min_str[0:i]
        return min_str
  ```
  但是这题提交了很多次都不对，主要是因为里面存在[],[""]和["","b"]这些例子，这时候就要返回"",那么首先在最前面判断下有空字符串的话直接返回"".另外判断字符串里面没东西的话就要返回min_str,其实就是返回"".

> 执行用时 :28 ms, 在所有 python3 提交中击败99.14%的用户
> 
> 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.68%的用户
