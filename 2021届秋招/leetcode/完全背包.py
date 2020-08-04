import numpy as np


def solve(v, w, tw, l):
    resArr = np.zeros((tw), dtype=np.int32)
    for i in range(l):
        for j in range(tw):
            if w[i] <= j:
                resArr[j] = max(resArr[j], resArr[j - w[i]] + v[i])
    return resArr[-1]


while True:
    try:
        # 完全背包问题
        max_money = int(input())
        cols = int(input())
        price = []
        value = []
        i = 0
        for i in range(cols):
            k, v = input().split()
            price.append(int(k))
            value.append(int(v))
        print(solve(value, price, max_money, cols))
    except:
        break

