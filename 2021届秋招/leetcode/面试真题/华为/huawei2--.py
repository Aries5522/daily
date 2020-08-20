import collections
import math


def C(n, m):  # C(4,2) = 6
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


def sol():
    N = int(input())
    depths = list(map(int, input().split()))
    # 0 1 2 2
    counter = collections.Counter(depths)
    ds = [counter[i] for i in range(len(counter))]
    if N == 1:
        print(N)
        return
    rst = 1
    for i in range(1, len(ds)):
        if ds[i] > ds[i - 1] * 2 or ds[i] == 0:
            print(0)
            return
        rst *= C(ds[i - 1] * 2, ds[i]) % (10 ** 9 + 7)
    print(int(rst) % (10 ** 9 + 7))

sol()
