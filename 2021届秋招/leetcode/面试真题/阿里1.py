# n = int(input())
n = 5
data = {}
for i in range(n):
    for j in range(i + 1, n):
        data[(i, j)] = 0
        data[(j, i)] = 0
# C = [int(i) for i in input().split()]
C = [1, 2, 3, 4, 5]
C.sort()
C = C[::-1]
record = [0 * n]
res = 0
i = 0
j = 1
while True:
    if data[(i, j)] == 0:
        data[(i, j)] = 1
        data[(j, i)] = 1
        res += C[i] * C[j]
        temp1 = i
        temp = j
        i = j
        m = 0
        flag = False
        while m < n:
            if i == m:
                m+=1
                continue
            elif data[(i, m)] == 0:
                flag = True
                break
            else:
                m+=1
        j = m
        m = 0
        if not flag:
            break
        flag = False
print(res)

"""
n = int(input())
data = [[0] * n for _ in range(n)]
for i in range(n):
    data[i][i] = 1
C = [int(i) for i in input().split()]
C.sort()
C = C[::-1]
res = 0
i = 0
j = 1
while True:
    p = 0
    for k in range(n):
        p += data[i][k]
    if p == n:
        break
    if data[i][j] == 0:
        data[i][j] = 1
        data[j][i] = 1
        res += C[i] * C[j]
        temp1 = i
        temp = j
        i = j
        m=0
        while m<n:
            if data[i][m]==0:
                break
            else:
                m+=1
        j=m
        m=0
print(res)



"""
