from collections import deque


n, m = map(int, input().split())
graph = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j] or graph[i][j] == 0:
            continue
        else:
            queue = deque([(i, j)])
            iso = True
            visited[i][j] = True
            while queue:
                a, b = queue.popleft()
                for dx, dy in directions:
                    if 0<=a+dx<n and 0<=b+dy<m and graph[a+dx][b+dy] == 1 and not visited[a+dx][b+dy]:
                        queue.append((a+dx, b+dy))
                        visited[a+dx][b+dy] = True
                if a == 0 or b == 0 or a == n-1 or b == m-1:
                    iso = False
            if iso:
                queue.append((i, j))
                graph[i][j] = 0
                while queue:
                    a, b = queue.popleft()
                    for dx, dy in directions:
                        if 0<=a+dx<n and 0<=b+dy<m and graph[a+dx][b+dy] == 1:
                            queue.append((a+dx, b+dy))
                            graph[a+dx][b+dy] = 0
for i in range(n):
    print(*graph[i])
