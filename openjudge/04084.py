import heapq
n,m = map(int, input().split())
graph = {}
in_degree = [0]*(n+1)
for i in range(m):
    u,v = map(int, input().split())
    graph.setdefault(u,[]).append(v)
    in_degree[v] +=1
for i in graph:
    graph[i].sort()

heap = []
for i in range(1,n+1):
    if in_degree[i]==0:
        heap.append(i)
res = []
while heap:
    u = heapq.heappop(heap)
    res.append(f'v{u}')
    for v in graph.get(u,[]):
        in_degree[v] -= 1
        if in_degree[v]==0:
            heapq.heappush(heap,v)

print(*res)