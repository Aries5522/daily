from typing import List
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for digit in nums:
                while drop and stack and stack[-1] < digit:
                    stack.pop()
                    drop -= 1
                stack.append(digit)
            return stack[:k]

        def merge(A, B):
            if not A and not B:
                return 0
            res = []
            while A or B:
                bigger = A if A > B else B
                res.append(str(bigger[0]))
                bigger.pop(0)
            return "".join(res)

        ans = 0
        for i in range(k+1):
            A = pick_max(nums1, min(i, len(nums1)))
            B = pick_max(nums2, min(k - i, len(nums2)))
            ans = max(int(merge(A, B)), ans)
        return [int(i) for i in list(str(ans))]
nums1=[1,2]
nums2=[]
k=2

print(Solution().maxNumber(nums1,nums2,k=2))