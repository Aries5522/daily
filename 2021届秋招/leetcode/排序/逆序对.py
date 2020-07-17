"""

堆排
"""
from typing import List


class Solution:
    # @classmethod
    def __init__(self):
        self.res = 0

    def reversePairs(self, nums: List[int]) -> int:
        k = self.guibing_sort(nums=nums)
        print(k)
        return self.res

    def guibing_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        mid = n // 2
        left = nums[0:mid]
        right = nums[mid:]
        return self.merge(self.guibing_sort(left), self.guibing_sort(right))

    def merge(self, list1, list2):
        list3 = []

        print(list1,list2)
        l=0
        r=0
        while l<len(list1) and r<len(list2):
            if list1[l] <= list2[r]:
                self.res+=r
                list3.append(list1[l])
                l+=1
            else:
                list3.append(list2[r])
                r+=1
        while l<len(list1):
            list3.append(list1[l])
            self.res+=r
            l+=1
        while r<len(list2):
            list3.append(list2[r])
            r+=1
        return list3


print(Solution().reversePairs(nums=[7, 5, 6, 4]))
