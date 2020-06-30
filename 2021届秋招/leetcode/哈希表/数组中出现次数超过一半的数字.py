'''

数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。



你可以假设数组是非空的，并且给定的数组总是存在多数元素。

'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        n=len(nums)
 #       if n==0:
#          return None
        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
                if hash_map[i]>int(n/2):
                    return i
            else:
                hash_map[i]+=1
                if hash_map[i]>int(n/2):
                    return i
        return None
'''
O(1)空间解法

'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
 #       if n==0:
#          return None
        ans=nums[0]
        t=1
        for i in range(1,n):
            if nums[i] == ans:
                t+=1
            else:
                t-=1
                if t==0:
                    ans=nums[i]
                    t=1
        return ans