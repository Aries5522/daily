##小美追小团
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


N, x, y = map(int, input().split())
lines = {}
for _ in range(N - 1):
    a, b = map(int, input().split())
#     if a not in lines:
#         lines[a] = [b]
#     else:
#         lines[a] += [b]
#     if b not in lines:
#         lines[b] = [a]
#     else:
#         lines[b] += [a]
# print(lines)
# res = 0
#
# def dfs(x, y, step):
#     global res
#     if x == y:
#         if step > res:
#             res = step
#         return
#     for k in lines[x]:
#         for v in lines[y]:
#             dfs(k, y, step + 1)
#             dfs(k, v, step + 1)
#
# dfs(x, y, 0)
# print(res)

"""
5 1 2
2 1
3 1
4 2
5 3

"""
