


"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

哈希表计数
但是也可以用位运算好像
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:return []
        temp={}
        for i in nums:
            if i not in temp:
                temp[i]=1
            else:
                temp[i]+=1
        for i in temp:
            if temp[i]==1:
                return i


