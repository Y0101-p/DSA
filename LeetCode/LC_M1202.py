from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class DisjointSet:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

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

        disjoint = DisjointSet(len(s))
        for a, b in pairs:
            disjoint.union(a, b)

        res = ''
        parent_list = {}
        parent_cnt = {}
        for i in range(len(s)):
            parent = disjoint.find(i)
            if parent not in parent_list:
                parent_list[parent] = [s[i]]
                parent_cnt[parent] = 0
            else:
                parent_list[parent].append(s[i])
        for i in parent_list:
            parent_list[i].sort()

        for i in range(len(s)):
            parent = disjoint.find(i)
            res += parent_list[parent][parent_cnt[parent]]
            parent_cnt[parent] += 1

        return res

s = 'dcab'
pairs = [[0,3],[1,2]]
res = Solution().smallestStringWithSwaps(s, pairs)
print(res)