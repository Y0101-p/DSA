from typing import List
import heapq
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        if k==0:
            return 0
        for i in range(m):
            grid[i].sort(reverse=True)
        l=[]
        for i in range(m):
            for j in range(min(limits[i],n)):
                if len(l)<k:
                    heapq.heappush(l,grid[i][j])
                else:
                    if grid[i][j]<l[0]:
                        break
                    heapq.heappushpop(l,grid[i][j])
        return sum(l)


if __name__ == '__main__':
    solution = Solution()
    res = solution.maxSum([[29,13]],[2],0)
    print(res)