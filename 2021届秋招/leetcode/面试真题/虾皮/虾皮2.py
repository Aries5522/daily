n = int(input())
res = 0
import math

def C(m, n):  ##m大
    return math.factorial(m) / (math.factorial(m - n) * math.factorial(n))

for i in range(n + 1, 2 * n + 2):  ##i代表第i次打开,发现这本已经做完了,实际做了i-1个题目
    print(C(i - 1, n) * (0.5) ** i * (2 * n - i + 1) * 2)
    res += C(i - 1, n) * (0.5) ** i * (2 * n - i + 1) * 2
print(res)
# print(math.floor(res))
