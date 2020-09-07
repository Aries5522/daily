m, n = map(int, input().split())
nums = [int(i) for i in input().split()]
res = 0
for l in range(1, m + 1):
    for r in range(1, m + 1):
        flag = True
        temp = None
        for num in nums:
            if (0 < num and num < l) or (r < num and num < m + 1):
                if temp:
                    if num >= temp:
                        continue
                    else:
                        flag = False
                        break
                temp = num
        if flag:
            res += 1
print(res)
"""
5 5
4 1 4 1 2

"""
