'''
剑指 Offer 56 - I. 数组中数字出现的次数

一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。


https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
'''

## 位运算的性质
## 两个只出现一次的数字,经过异或操作剩下的肯定是两个不同数字的异或结果 ,
# 在于分组,按照最后&1操作可以分成奇数偶数两组.那如果按照最终的异或结果中不为0的那一位异或 ,不同的两个数肯定在不同的两个组了

from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = []
        k = 0
        for i in nums:  ##得到不同两个数的 异或结果
            k = k ^ i
        h = 1
        while k & h == 0:  # 寻找异或结果为1的那一位
            h <<= 1
        a = 0
        b = 0
        for i in nums:
            if i & h == 0:  # 按照那一位对所有数字分组异或
                a = a ^ i
            else:
                b = b ^ i
        return [a, b]
