from typing import List
#最优解使用并查集
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def dfs(pr):
            if visited[pr] == 0:
                visited[pr] = 1
                for i in graph[pr]:
                    if i == parent[pr]:
                        continue
                    if visited[i] == 0:
                        parent[i] = pr
                        bool_finish, res = dfs(i)
                        if bool_finish:
                            return True, res
                    if visited[i] == 1:
                        parent[i] = pr
                        return True, pr
            visited[pr] = 2
            return False, None

        n = len(edges)
        parent = [-1] * (n+1)
        visited = [0] * (n+1)
        graph = [[] for _ in range(n+1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        bool_finish, pr = dfs(1)
        loop = set()
        loop.add(pr)
        pr = parent[pr]
        while pr not in loop:
            loop.add(pr)
            pr = parent[pr]
        for a, b in edges[::-1]:
            if a in loop and b in loop:
                return [a, b]