from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        if len(nums) < 3:
            return []
        for i in range(0, n - 2):
            left = i + 1
            right = n - 1
            if nums[i] == nums[i - 1] and i > 0:
                continue
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp < 0:
                    left += 1
                elif temp > 0:
                    right -= 1
                else:
                    res.append([nums[left], nums[i], nums[right]])
                    while nums[left + 1] == nums[left] and left < right - 1:
                        left += 1
                    while nums[right - 1] == nums[right] and right > left + 1:
                        right -= 1
                    left+=1
                    right-=1
        return res

print(Solution().threeSum([0,0,0,0]))