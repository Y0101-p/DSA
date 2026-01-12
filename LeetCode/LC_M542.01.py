from typing import List
from collections import deque
class Solution:
    def updateMatrix(mat):
        m, n = len(mat), len(mat[0])
        dist = [[-1] * n for _ in range(m)]
        queue = deque()
    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
                
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                
            return dist
if __name__ == '__main__':
    solution = Solution()
    mat = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
    res = solution.updateMatrix( mat)
    print(res)