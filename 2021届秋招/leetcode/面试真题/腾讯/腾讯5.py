n, m, T = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().split())
    adj[x - 1].append((d, y - 1))

def djstl(adj, start, target):
    import heapq
    n = len(adj)
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    visited = [0 for _ in range(n)]
    prioqueue = [(0, start)]
    while prioqueue:
        distance, t = heapq.heappop(prioqueue)
        if visited[t] == 1:
            continue
        visited[t] = 1
        for d, j in adj[t]:
            if dist[j] > dist[t] + d:
                dist[j] = dist[t] + d
                heapq.heappush(prioqueue, (dist[j], j))
    return dist[target] if dist[target] != float('inf') else -1

ans = djstl(adj, 0, n - 1)
ans += djstl(adj, n - 1, 0)
print(ans * T)
