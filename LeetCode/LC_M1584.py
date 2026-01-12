import heapq
from typing import List


class Solution_Prime:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        res = 0
        heap = []
        length = len(points)
        disconnected = set([i for i in range(1,length)])
        for i in disconnected:
            heapq.heappush(heap, (manhattan(points[i], points[0]),0,i))
        while heap:
            dist, u, v = heapq.heappop(heap)
            if v not in disconnected:
                continue
            else:
                disconnected.remove(v)
                res += dist
                for i in disconnected:
                    heapq.heappush(heap, (manhattan(points[i], points[v]),v,i))
        return res

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class DisjointSet:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0 for _ in range(n)]

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                x_root = self.find(x)
                y_root = self.find(y)

                if x_root == y_root:
                    return
                if self.rank[x_root] < self.rank[y_root]:
                    self.parent[x_root] = y_root
                elif self.rank[x_root] > self.rank[y_root]:
                    self.parent[y_root] = x_root
                else:
                    self.parent[y_root] = x_root
                    self.rank[x_root] += 1

            def same(self, x, y):
                x_root = self.find(x)
                y_root = self.find(y)
                if x_root == y_root:
                    return True
                else:
                    return False

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        length = len(points)
        edges=[]
        res=0
        for i in range(length):
            for j in range(i+1,length):
                edges.append((manhattan(points[i],points[j]),i, j))
        edges.sort()
        disjoint = DisjointSet(length)
        for dist,i,j in edges:
            if disjoint.same(i,j):
                continue
            else:
                disjoint.union(i,j)
                res += dist
        return res
