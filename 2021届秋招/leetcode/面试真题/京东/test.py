import sys
import math

n, m = map(int,sys.stdin.readline().strip("\n").split())
# print(n, m)
res = 0
i = 0
while i < m:
    res += n
    n = math.sqrt(n)
    i += 1
print("%.2f" % res)

