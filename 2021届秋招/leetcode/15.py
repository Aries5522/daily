from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        # print(nums)
        if n <= 2:
            return []
        for i in range(n):
            left = i + 1
            right = n - 1
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif (nums[i] + nums[left] + nums[right]) < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while nums[left]==nums[left+1] and left<right-1:
                        left+=1
                    while nums[right]==nums[right-1] and left <right-1:
                        right-=1
                    left+=1
                    right-=1
        return res

print(Solution().threeSum(nums=[0,0,0,0]))
