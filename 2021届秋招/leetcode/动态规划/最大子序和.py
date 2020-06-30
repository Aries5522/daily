'''

输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[]
        dp.append(nums[0])
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1]+nums[i],nums[i]))
        return max(dp)

##动态规划