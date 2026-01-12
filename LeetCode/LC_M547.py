from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class DisjointSet:
            def __init__(self, n):
                self.root=[i for i in range(n)]
                self.rank=[0]*n
            def find_root(self,x):
                if self.root[x] != x:
                    self.root[x]=self.find_root(self.root[x])
                return self.root[x]
            def union(self,x,y):
                x_root=self.find_root(x)
                y_root=self.find_root(y)
                if x_root==y_root:
                    return
                if self.rank[x_root]>self.rank[y_root]:
                    self.root[y_root]=x_root
                elif self.rank[x_root]<self.rank[y_root]:
                    self.root[x_root]=y_root
                else:
                    self.root[y_root]=x_root
                    self.rank[x_root]+=1
        a=DisjointSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    a.union(i, j)
        root_set=[]
        for i in a.root:
            root=a.find_root(i)
            if root not in root_set:
                root_set.append(root)
        return len(root_set)
