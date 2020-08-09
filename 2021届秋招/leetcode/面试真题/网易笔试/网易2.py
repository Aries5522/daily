T = int(input())
t = 0
while t < T:
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(j) for j in input().split()]
    dp = [0] * n
    dp[0] = a[0]
    if n>1:
        dp[1] = min(b[0], a[0] + a[1])
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1])
    res = dp[n - 1]
    time_hour = res // 3600
    time_min = (res % 3600) // 60
    time_sec = (res % 3600) % 60
    if time_hour >= 4:
        print("%02d:%02d:%02d pm" % (time_hour+8,time_min,time_sec))
    else:
        print("%02d:%02d:%02d am" % (time_hour+8,time_min,time_sec))
    t += 1
