第一种:暴力求解
```
class Solution:
    def twoSum(self,nums, target):
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if (nums[i]+nums[j])==target:
                    return [i,j]
```
6192ms,速度特别慢

第二种:字典模拟哈希求解

```
class Solution:
    def twoSum(self,nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
```
52ms比较快捷