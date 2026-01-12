from collections import defaultdict
from collections import deque


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    cnt = 0
    while queue:
        u = queue.popleft()
        cnt += 1
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if cnt == n:
        print('No')
    else:
        print('Yes')