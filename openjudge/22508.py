from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
out_degree = [0 for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    out_degree[u] += 1

queue = deque()
for i in range(n):
    if out_degree[i] == 0:
        queue.append((i, 0))


res = n*100
while queue:
    v, height = queue.popleft()
    res += height
    for u in graph[v]:
        out_degree[u] -= 1
        if out_degree[u] == 0:
            queue.append((u, height+1))

print(res)