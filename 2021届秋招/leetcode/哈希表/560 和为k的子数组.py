from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        sum_dict = {0: 1}
        sum_temp = 0
        for i in range(n):
            sum_temp += nums[i]  # 当前前缀和元素B[i]
            ans += sum_dict.get(sum_temp - k, 0)  # 之前有多少个B[i]-k,没有的话默认返回0
            # 要先寻找答案，再将当前和放入字典。先放入字典的话，如果k=0，那么答案必定+1，这是不对
            sum_dict[sum_temp] = sum_dict.get(sum_temp, 0) + 1
        return ans


print(Solution().subarraySum(nums=[1, 1,0, 1], k=2))
