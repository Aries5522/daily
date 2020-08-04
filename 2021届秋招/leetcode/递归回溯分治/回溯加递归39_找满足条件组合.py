from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def backtrace(nums,start,target,path,res):
            if target==0:
                res.append(path.copy())
                return
            if target<0:
                return

            for i in range(start,n):
                path.append(nums[i])
                backtrace(nums,i,target-nums[i],path,res)
                path.pop(-1)
        res=[]
        path=[]
        backtrace(candidates,0,target,path,res)

        return res

print(Solution().combinationSum(candidates=[2,3,6,7],target=7))