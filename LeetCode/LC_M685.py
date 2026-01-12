from typing import List
from collections import deque

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        def find_loop(begin):
            if visited[begin]:
                return False, None
            path_set = set()
            path_set.add(begin)
            visited[begin] = True
            pr = parents[begin]
            while pr != -1:
                if pr in path_set:
                    return True, pr
                else:
                    path_set.add(pr)
                if visited[pr]:
                    return False, None
                visited[pr] = True
                pr = parents[pr]
            return False, None


        n = len(edges)
        graph = [[] for _ in range(n+1)]
        double_edge = None
        parents = [-1] * (n+1)
        for u, v in edges:
            if parents[v] == -1:
                parents[v] = u
                graph[u].append(v)
            else:
                double_edge = [u, v]
        visited = [False] * (n+1)

        if double_edge is not None:
            u, v = double_edge
            for i in range(1,n+1):
                if parents[i] == -1:
                    root = i
                    break
            visited[root] = True
            queue = deque([root])
            cnt = 0
            while queue:
                u = queue.popleft()
                cnt += 1
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            v = double_edge[1]
            if cnt == n:
                return double_edge
            else:
                return [parents[v],v]


        for i in range(1, n+1):
            judge, loop_begin = find_loop(i)
            if judge:
                res = set()
                res.add(loop_begin)
                pr = parents[loop_begin]
                while pr not in res:
                    res.add(pr)
                    pr = parents[pr]
                for u, v in edges[::-1]:
                    if u in res and v in res:
                        return [u, v]

edges = [[4,2],[1,5],[5,2],[5,3],[2,4]]
solution = Solution()
print(solution.findRedundantDirectedConnection(edges))