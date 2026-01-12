from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(u,path):
            if u == len(graph)-1:
                res.append(path[:])
                return
            for v in graph[u]:
                dfs(v,path+[v])
            return

        res=[]
        dfs(0,[0])
        return res
sol = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(sol.allPathsSourceTarget(graph))