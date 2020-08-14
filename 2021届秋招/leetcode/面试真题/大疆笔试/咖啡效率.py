while True:
    try:
        N = int(input())  # bug数量
        A = int(input())  # 倍数
        X = int(input())  # 咖啡数
        data = []
        for i in range(N):
            data.append(int(input()))
        # N, A, X = 4, 3, 3
        # data = [333, 77, 100, 13]
        max_time = A * 60 * X
        res = 0
        cur = 0
        left = 0
        flg = 0
        for i in range(N):
            cur += data[i]
            if cur > max_time:
                if flg == 0:
                    res = 0
                    flg = 1
                    res += 60 * X + cur - max_time
                res += data[i]
                X = 0
            else:
                res += data[i] // A
                left += data[i] % A
        res += left // A if left % A == 0 else left // A + 1
        print(res)
    except:
        break
"""
8
2
8
60
60
60
60
60
60
60
60



4
3
3
333
77
100
13



"""
