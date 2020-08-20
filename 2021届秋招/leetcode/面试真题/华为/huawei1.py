while True:
    try:
        M, N = map(int, input().split())
        # M,N=10,10
        def is_ok(num):
            if num % 10 == 7 and num // 10 % 10 % 2 == 1:
                return True
            else:
                return False
        # print(is_ok(17))
        if M < 10 or N < 10 or M > 1000 or N > 1000:
            print([])
            break
        data = []
        res = []
        for i in range(M):
            data.append([k + i * N for k in range(N)])
        # print(data)
        record = 0
        l, r, t, b = 0, len(data[0]) - 1, 0, len(data) - 1
        while True:
            for i in range(l, r + 1):
                record += 1
                if is_ok(record):
                    res.append([t, i])
            t += 1
            if t > b: break
            for i in range(t, b + 1):
                record += 1
                if is_ok(record):
                    res.append([i,r])
            r -= 1
            if r < l: break
            for i in range(r, l - 1, -1):
                record += 1
                if is_ok(record):
                    res.append([b, i])
            b -= 1
            if b < t: break
            for i in range(b, t - 1, -1):
                record += 1
                if is_ok(record):
                    res.append([i, l])
            l += 1
            if r < l: break
        print(res)
    except:
        break
