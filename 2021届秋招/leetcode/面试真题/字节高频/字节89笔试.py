"""

多米诺骨牌
"""
while True:
    try:
        n = int(input())
        data = []
        for i in range(n):
            h, w = map(int, input().split())
            data.append((h, w))
        sorted(data, key=lambda x: x[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if data[i][1] > data[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))
    except:
        break

"""
5
5 5
3 1
2 6
4 2
1 4


"""
