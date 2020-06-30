"""

给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=1
        
        k=len(nums)
        while i<k:
            if nums[i] == nums[nums[i]]:
                del nums[nums[i]]
                continue
            if  nums[i]!=i:
                nums[i],nums[nums[i]]=nums[nums[i]],nums[i]
            else:
                i+=1
        m=len(nums)
        for i in range(1,m):
            if nums[i]!=i:
                return i


print(Solution().firstMissingPositive( [3,4,-1,1]))