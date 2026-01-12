from collections import defaultdict
import heapq


n, m = map(int, input().split())
graph = defaultdict(dict)
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

heap = []
res = 0
cnt = 1
visited = [False] * (n+1)
visited[1] = True
for i in graph[1]:
    heapq.heappush(heap, (graph[1][i], i))

while heap:
    w, u = heapq.heappop(heap)
    if visited[u]:
        continue
    visited[u] = True
    res += w
    cnt += 1
    for i in graph[u]:
        heapq.heappush(heap, (graph[u][i], i))

if cnt == n :
    print(res)
else:
    print('orz')
