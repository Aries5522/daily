"""
查找左边界
lower bound A[i] > x
def lowwer_bound(self, nums, target):
    # find in range [left, right)
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

 右边边界
upper bound: find index of i, such that A[i] > x

def higher_bound(self, nums, target):
    # find in range [left, right)
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


"""
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/


"""

##
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.lower_bound(nums,target)
        right=self.upper_bound(nums,target)
        if left==right:
            return [-1,-1]
        return [left,right-1]
    def lower_bound(self,nums,target):
        l=0
        r=len(nums)
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        return l
    def upper_bound(self,nums,target):
        l=0
        r=len(nums)
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid
        return l
print(Solution().searchRange([5,7,7,8,8,10],8))