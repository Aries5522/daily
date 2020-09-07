n, w = map(int, input().split())
a = [int(i) for i in input().split()]
# n,w=2,2
# a=[1,1]
res = 0
visited_l = [False] * n
visited_r = [False] * n


def dfs(a, w, l, r, visited_l, visited_r):
    global res
    if max(a) > w or visited_l[l] or visited_r[r]:
        return
    if max(a) == min(a) == w:
        res += 1
        res = res % (1e9 + 7)
        return

    for l in range(n):
        for r in range(l, n):
            visited_r[r] = True
            visited_l[l] = True
            for i in range(l, r + 1):
                a[i] += 1
            dfs(a, w, l, r, visited_l, visited_r)
            for i in range(l, r + 1):
                a[i] -= 1
            visited_r[r] = False
            visited_l[l] = False

dfs(a, w, 0, 0, visited_l, visited_r)
print(res)
