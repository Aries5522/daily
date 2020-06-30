from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans=0
        return self.guibing_sort(nums)
    def guibing_sort(self,nums):
        n=len(nums)
        if n<=1:
            return nums[0]
        mid=n//2
        left=nums[0:mid]
        right=nums[mid:]
        return self.merge(self.guibing_sort(left),self.guibing_sort(right))
    def merge(self,list1,list2):
        ans=0
        if not list1 or not list2:
            return list1+list2
        res=[]
        i=0
        j=0
        while i<len(list1) and j<len(list2):
            if list1[i]<list2[j]:
                i+=1
                res.append(list1[i])
            if list1[i]>list2[j]:
                j+=1
                res.append(list2[j])
                ans+=1

        ans+=(len(list1)-i)*len(list2)
        return res



print(Solution().reversePairs([7,5,6,4]))