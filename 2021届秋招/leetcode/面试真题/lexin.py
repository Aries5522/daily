# if __name__ == "__main__":
#     s = input()
#     a = [int(i) for i in s.split()]
#     M = a[0]
#     N = a[1]
#     m = 0
#     data = []
#     while m < M:
#         temp = []
#         s = input()
#         if s != "":
#             temp = [int(i) for i in s.split()]
#             data.append(temp)
#             m += 1
#         else:
#             break
#     res = 0
#
#
#     def dfs(i, j):
#
#         while
def main(a):
    res = 0
    for i in range(3, a + 1):
        if is_ok(i):
            res += 1
    return res


def is_ok(a):
    while a >= 3:
        if a % 2 == 1 and (a // 2) % 2 == 1:
            return True
        a = a // 2
    return False


print(main(7))
