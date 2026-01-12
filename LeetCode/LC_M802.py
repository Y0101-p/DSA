from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if visited[node] == 2:
                return True
            elif visited[node] == 1 or visited[node] == -1:
                visited[node] = -1
                return False
            visited[node] = 1
            for i in graph[node]:
                if visited[i] == 0:
                    if not dfs(i):
                        visited[i] = -1
                        return False
                elif visited[i] == 1:
                    visited[i] = -1
                    return False
                elif visited[i] == -1:
                    visited[i] = -1
                    return False
                elif visited[i] == 2:
                    continue
            visited[node] = 2
            return True


        n = len(graph)
        trans_graph = [[] for _ in range(n)]
        for i in range(len(graph)):
            for j in graph[i]:
                trans_graph[j].append(i)

        visited = [0] * n

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res