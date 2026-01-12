from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class DisjointSet:
            def __init__(self):
                self.parents = {}
                self.ranks = {}
                self.graph = defaultdict(dict)

            def add_edge(self, u, v, weight):
                self.graph[u][v] = weight
                self.graph[v][u] = 1/weight
                self.add_vertex(u)
                self.add_vertex(v)
                self.union_vertex(u,v)
                for i in self.graph[v]:
                    if i!=u:
                        self.graph[u][i] = weight*self.graph[v][i]
                        self.graph[i][u] = 1/self.graph[u][i]
                        for j in self.graph[u]:
                            if j!=v:
                                self.graph[j][i] = weight*self.graph[v][i]*self.graph[j][u]
                                self.graph[i][j] = 1/self.graph[j][i]

                for i in self.graph[u]:
                    if i!=v:
                        self.graph[v][i] = 1/weight*self.graph[u][i]
                        self.graph[i][v] = 1/self.graph[v][i]

            def add_vertex(self,x):
                if x not in self.parents:
                    self.parents[x] = x
                    self.ranks[x] = 0

            def find(self, x):
                if self.parents.get(x):
                    if x!=self.parents[x]:
                        self.parents[x] = self.find(self.parents[x])
                    return self.parents[x]
                else:
                    return None

            def union_vertex(self,x,y):
                x_root = self.find(x)
                y_root = self.find(y)
                if x_root == y_root:
                    return
                if self.ranks[x_root] > self.ranks[y_root]:
                    self.parents[y_root] = x_root
                elif self.ranks[x_root] < self.ranks[y_root]:
                    self.parents[x_root] = y_root
                else:
                    self.parents[y_root] = x_root
                    self.ranks[x_root] += 1

            def find_edge(self,x,y):
                x_root = self.find(x)
                y_root = self.find(y)
                if x_root == y_root and x_root and y_root:
                    if x == y:
                        return 1.0
                    else:
                        return self.graph[x][y]
                else:
                    return -1.0

        disjoint_set = DisjointSet()
        for i in range(len(equations)):
            disjoint_set.add_edge(equations[i][0], equations[i][1], values[i])
        res = []
        for u,v in queries:
            res.append(disjoint_set.find_edge(u,v))
        return res

equations = [["a","b"],["e","f"],["b","e"]]
values = [3.4,1.4,2.3]
queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
sol = Solution()
print(sol.calcEquation(equations, values, queries))