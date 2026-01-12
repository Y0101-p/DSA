from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        class DisjointSet:
            def __init__(self, n):
                self.root = [x for x in range(n)]
                self.rank = [0 for x in range(n)]

            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]

            def union(self, x, y):
                xroot = self.find(x)
                yroot = self.find(y)
                if xroot == yroot:
                    return
                if self.rank[xroot] < self.rank[yroot]:
                    self.root[xroot] = yroot
                elif self.rank[yroot] < self.rank[xroot]:
                    self.root[yroot] = xroot
                else:
                    self.root[yroot] = xroot
                    self.rank[xroot] += 1

        disjointset = DisjointSet(n)
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                disjointset.union(i, i - 1)
        res = []
        for u, v in queries:
            if disjointset.find(u) == disjointset.find(v):
                res.append(True)
            else:
                res.append(False)
        return res