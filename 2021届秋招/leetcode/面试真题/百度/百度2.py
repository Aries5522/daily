N = int(input())
data = []
for _ in range(N):
    temp = [int(i) for i in input().split()]
    data.append(temp)


res = 1e9
visited = [[False] * N for _ in range(N)]
cur = data[0][0]
paths = []


def BFS(i, j, visited, temp, path):
    global cur
    global res
    global paths
    if i < 0 or j < 0 or i > N - 1 or j > N - 1 or visited[i][j]:
        return
    elif i == N-1  and j == N-1:
        paths.append(path)
        if temp < res:
            res = temp
        return
    visited[i][j] = True
    cur = data[i][j]
    if i+1<N:
        BFS(i + 1, j, visited, temp + abs(cur - data[i + 1][j]), path + str(cur))
    if j+1<N:
        BFS(i, j + 1, visited, temp + abs(cur - data[i][j + 1]), path + str(cur))
    if i-1>=0:
        BFS(i - 1, j, visited, temp + abs(cur - data[i - 1][j]), path + str(cur))
    if j-1>=0:
        BFS(i, j - 1, visited, temp + abs(cur - data[i][j - 1]), path + str(cur))

BFS(0, 0, visited, 0, "")
print(res)
print(paths)
"""
4
1 2 4 1
1 3 1 1
1 2 1 1
1 1 3 1

"""
