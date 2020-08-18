# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray: return 0
        n = len(rotateArray)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            elif rotateArray[mid] < rotateArray[r]:
                r = mid
            else:
                r -= 1

        return rotateArray[l]
        # write code here


nums = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
print(Solution().minNumberInRotateArray(nums))
