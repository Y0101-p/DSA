from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        class DisjointSet:
            def __init__(self, n):
                self.parent = list(range(2*n))
                self.rank = [0]*2*n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                x = self.find(x)
                y = self.find(y)
                if x == y:
                    return
                else:
                    if self.rank[x] > self.rank[y]:
                        self.parent[y] = x
                    else:
                        self.parent[x] = y
                        if self.rank[x] == self.rank[y]:
                            self.rank[y] += 1
                    return

        n = len(graph)
        disjoint = DisjointSet(n)
        for i in range(n):
            for j in graph[i]:
                if disjoint.find(j) == disjoint.find(i) or disjoint.find(i+n) == disjoint.find(j+n):
                    return False
                else:
                    disjoint.union(i, j + n)
                    disjoint.union(j, i + n)
        return True
