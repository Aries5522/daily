"""

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

作者：labuladong
链接：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""


class Solution:
    def permute(self, nums):
        n=len(nums)
        if not nums:
            return []
        res=[]
        def traceback(first=0):
            if first==n:
                res.append(nums[:])
            for i in range(first,n):
                nums[i],nums[first]=nums[first],nums[i]
                traceback(first+1)
                nums[i],nums[first]=nums[first],nums[i]
        traceback()
        return res


print(Solution().permute([1,2,3]))