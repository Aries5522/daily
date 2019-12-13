class Solution:
    def twoSum(nums, target) :
        dict={}
        for ind,num in enumerate(nums):
            dict[num]=ind
        for i ,num in enumerate(nums):
            if (target-num) in nums and i !=dict[target-num] :
                return[i,dict[target-num]]

nums=[2,7,11,15]
target=9
print(Solution.twoSum(nums,target))


class Solution:
    def twoSum(self,nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
