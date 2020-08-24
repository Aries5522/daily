#!/usr/bin/env python3
# coding: utf-8


if __name__ == '__main__':
    # TODO: write your code here

    def dfs(nums, cur, steps, N):
        global res
        if cur >= N:
            res = min(res, steps)
            return
        for i in [1, 2, 3]:
            temp = cur
            cur += i
            while cur < N:
                if nums[cur] > 0:
                    cur += nums[cur]
                else:
                    break
            dfs(nums, cur, steps + 1, N)
            cur = temp


    T=int(input())
    # T = 1
    t = 0
    while t < T:
        nums=[int(i) for i in input().split()]
        # nums = [5, 1, 1, 1, 1, 1]
        N = nums.pop(0)
        res = 1000000
        dfs(nums, 0, 0, N)
        print(res)
        t += 1
"""
4
5 0 3 2 1 0
5 0 1 0 2 4
6 0 2 1 0 2 1
8 0 3 1 0 0 3 1 0
"""
