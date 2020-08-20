import math

def C(n, m):
    return math.factorial(n) / (
            math.factorial(n - m) * math.factorial(m)) % (10 ** 9 + 7)

def main():
    N = int(input())
    data = [int(i) for i in input().split()]
    k = max(data)
    from collections import Counter
    dict = Counter(data)
    data = [0] * (k + 1)
    for i in range(k + 1):
        data[i] = dict[i]
    ans = 1
    for i in range(k + 1):
        if i == 0 and data[i] == 0:
            print(0)
            return
        if i != 0 and data[i] > data[i - 1] * 2 or data[i] == 0:
            print(0)
            return
        if i != 0:
            ans *= C(2 * data[i - 1], data[i]) % (10 ** 9 + 7)
    print(int(ans))
main()
