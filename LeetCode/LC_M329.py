from typing import List
from collections import deque

class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        delta = [(0,1),(0,-1),(1,0),(-1,0)]
        res =[[0]*n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                judge = True
                for di,dj in delta:
                    if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj]>matrix[i][j]:
                        judge = False
                        break
                if judge:
                    queue.append((i,j,0))

        while queue:
            i,j,steps = queue.popleft()
            for di,dj in delta:
                if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj]<matrix[i][j]:
                    if res[i+di][j+dj]<steps+1:
                        res[i+di][j+dj]=steps+1
                        queue.append((i+di,j+dj,steps+1))
        return steps+1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(i,j,m,n):
            if visited[i][j]==1:
                return res[i][j]
            for di,dj in delta:
                if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj]>matrix[i][j]:
                    if visited[i+di][j+dj]==1:
                        res[i][j]=max(res[i+di][j+dj]+1,res[i][j])
                        continue
                    elif visited[i+di][j+dj]==0:
                        dfs(i+di,j+dj,m,n)
                        res[i][j] = max(res[i + di][j + dj] + 1, res[i][j])
                        continue
            visited[i][j] = 1
            return res[i][j]
        m = len(matrix)
        n = len(matrix[0])
        delta = [(0,1),(0,-1),(1,0),(-1,0)]
        res =[[0]*n for _ in range(m)]
        visited = [[0]*n for _ in range(m)]
        maxi=1
        for i in range(m):
            for j in range(n):
                maxi=max(maxi,dfs(i,j,m,n)+1)
        return maxi


solution = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(solution.longestIncreasingPath(matrix))