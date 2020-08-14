def one_line(data):
    n = len(data)
    row = [0] * n  ##行和
    col = [0] * n
    for i in range(n):
        for j in range(n):
            row[i] += data[i][j]
            col[j] += data[i][j]
    max_ = 0
    res = (0, 0)
    for i in range(len(row)):
        for j in range(len(row)):
            if row[i] + col[j] - data[i][j] > max_:
                max_ = row[i] + col[j] - data[i][j]
                res = (i, j)
    return res


while True:
    try:
        N = int(input())
        data = []
        for i in range(N):
            temp = [int(k) for k in input().split()]
            data.append(temp)
        # N = 3
        # data = [[1, 0, 0],
        #         [0, 10, 10],
        #         [0, 10, 10]]
        while data:
            i, j = one_line(data)
            print(i + 1, j + 1)
            del data[i]
            for k in data:
                del k[j]
    except:
        break
