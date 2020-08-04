class Solution:
    def permute(self, nums):
        if not nums: return 0
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + str(nums[i]))

        backtrack(nums, '')
        print(len(res))
        ans = 0
        for i in res:
            if int(i) % 7 == 0:
                ans += 1
        return ans


print(Solution().permute(nums=[]))
