from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [[float('inf')] * n for _ in range(k+2)]
        distance[0][src] = 0
        for t in range(1, k+2):
            for j, i, price in flights:
                distance[t][i] = min(distance[t][j], distance[t-1][j] + price)

        res = float('inf')
        for i in range(k+2):
            res = min(res, distance[i][dst])
        if res == float('inf'):
            return -1
        else:
            return res


n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))