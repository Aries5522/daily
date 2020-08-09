T = int(input())
t = 0
while t < T:
    n = int(input())
    nums = [int(i) for i in input().split()]
    sum_ = sum(nums)
    vis = [0] * n
    res = float('inf')

    def dfs(data, vis, sum_1, sum_2, sum_):
        global res
        if sum_1 > sum_ // 2 or sum_2 > sum_ // 2:
            return
        if sum_1 == sum_2:
            res = min(res, sum_ - sum_1 * 2)
        for i in range(n):
            if not vis[i]:
                if sum_1 > sum_2:
                    sum_2 += data[i]
                    vis[i] = 1
                    dfs(data, vis, sum_1, sum_2, sum_)
                    vis[i] = 0
                    sum_2 -= data[i]
                else:
                    sum_1 += data[i]
                    vis[i] = 1
                    dfs(data, vis, sum_1, sum_2, sum_)
                    vis[i] = 0
                    sum_1 -= data[i]
    dfs(nums, vis, 0, 0, sum_)
    print(res)
    t += 1
