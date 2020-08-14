"""

    def lower_bound(self, nums, target):  ##查找大于等于target的最小的下标
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] >= target:
            return l
        else:
            return -1

    def upper_bound(self, nums, target):  ##查找小于等于target的最大的下标,所以nums[mid]>target的时候
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        if nums[l] <= target:
            return l
        else:
            return -1

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
        left = self.lower_bound(nums, target)
        right = self.upper_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right]

    def lower_bound(self, nums, target):  ##查找大于等于target的最小的下标
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] >= target:
            return l
        else:
            return -1

    def upper_bound(self, nums, target):  ##查找小于等于target的最大的下标
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        if nums[l] <= target:
            return l
        else:
            return -1


print(Solution().searchRange([5, 5, 7, 8, 10], 6))
