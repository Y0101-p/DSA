from collections import defaultdict
from typing import List
from collections import deque



class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        def bfs(start):
            queue = deque([start])
            visited = [False] * n
            visited[start] = True

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
                        parent[neighbor] = node
            return node

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        parent = [0]*n

        x = bfs(0)
        y = bfs(x)

        path = []
        parent[x] = -1
        while y!=-1:
            path.append(y)
            y = parent[y]
        m = len(path)
        if m % 2 == 0:
            return [path[m//2],path[m//2-1]]
        else:
            return [path[m//2]]


n = 4
edges = [[1,0],[1,2],[1,3]]
res = Solution().findMinHeightTrees(n, edges)
print(res)