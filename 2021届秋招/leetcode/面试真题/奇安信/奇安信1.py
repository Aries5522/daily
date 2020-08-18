# while True:
#     try:
#         n = int(input())
#         # n = 2
#         res = []
#
#         def dfs(n, path):
#             if n == 0:
#                 res.append(path)
#                 return
#             for i in range(1, n + 1):
#                 dfs(n - i, path + str(i))
#
#         dfs(n, "")
#         print(res)
#         print(len(res))
#     except:
#         break

#
# while True:
#     try:
#         n = int(input())
#         res = 0
#         def dfs(n):
#             global res
#             if n == 0:
#                 res+=1
#                 return
#             for i in range(1, n + 1):
#                 dfs(n - i)
#         dfs(n)
#         print(res)
#     except:
#         break


while True:
    try:
        n = int(input())
        print(2 ** (n - 1))
    except:
        break
