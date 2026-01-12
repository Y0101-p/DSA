import heapq


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

heap = []
dist = [float('inf')] * (n+1)
dist[1] = 0
heap.append((0, 1))
while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]:
        continue
    for neighbor, w in graph[u]:
        new_w = w + dist[u]
        if new_w < dist[neighbor]:
            dist[neighbor] = new_w
            heapq.heappush(heap, (new_w, neighbor))

print(dist[-1])