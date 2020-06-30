
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        i=0
        j=1
        while i<n-1 :
            sum_=nums[i]+nums[j]
            if sum_==target:
                return [nums[i],nums[j]]
            elif sum_ < target:
                j+=1
                if j==n:
                    i+=1
                    j=i+1
            elif sum_>target:
                i+=1



nums=[14,15,16,22,53,60]
target=76
print(Solution().twoSum(nums,target))