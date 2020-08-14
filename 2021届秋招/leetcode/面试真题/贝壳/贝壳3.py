import copy

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(input()))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(p, AA, N, M):
    que = [p]
    max_ = 0
    while que:
        cur = que.pop(0)
        x, y, s = cur[0], cur[1], cur[2]
        max_ = max(max_, s)
        for dd in directions:
            nx, ny = x + dd[0], y + dd[1]
            if 0 <= nx < N and 0 <= ny < M and AA[nx][ny] != "#":
                AA[nx][ny] = "#"
                que.append((nx, ny, s + 1))
    return max_


max_ = 0
count = 0
for idx in range(N):
    for jdx in range(M):
        if A[idx][jdx] != "#":
            tt = bfs((idx, jdx, 0), copy.deepcopy(A), N, M)
            max_ = max(max_, tt)
            count += 1
        if count >= 100:
            break
print(max_)
