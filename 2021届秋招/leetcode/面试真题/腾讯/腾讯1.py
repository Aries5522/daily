T = int(input())
# T = 3

ans=[]
def longest(nums):
    n = len(nums)
    nums1 = []
    for i in range(n):
        if nums[i] > nums[0]:
            nums1.append(nums[i])
    return findNumberOfLIS(nums1)


def findNumberOfLIS(nums):
    if nums == []:
        return (0)
    n = len(nums)
    length = [1] * n
    counter = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:  # 代表第一次遇到最长子序列
                    length[i] = 1 + length[j]
                    counter[i] = counter[j]
                elif length[j] + 1 == length[i]:  # 代表已经遇到过最长子序列
                    counter[i] = counter[i] + counter[j]
    tmp = max(length)
    return tmp

for _ in range(T):
    n = int(input())
    nums = [int(i) for i in input().split()]
    # n = 9
    # nums = [5, 4, 3, 2, 1, 2, 3, 4, 5]
    # n = 14
    # nums = [87, 70, 17, 12, 14, 86, 61, 51, 12, 90, 69, 89, 4, 65]
    res = 0
    i = 1
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                l = i
                r = j
                res = max(res, 2+2 * min(longest(nums[0:l+1][::-1]), longest(nums[r:])))
    ans.append(res)

for i in ans:
    print(i)
"""

3
9
5 4 3 2 1 2 3 4 5
5
1 2 3 4 5
14
87 70 17 12 14 86 61 51 12 90 69 89 4 65

"""
