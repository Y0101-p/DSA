from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        ladders_heap = [float('inf')]
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                delta = heights[i] - heights[i - 1]
                if len(ladders_heap) <= ladders:
                    heapq.heappush(ladders_heap, delta)
                    continue
                else:
                    if delta > ladders_heap[0]:
                        trans = heapq.heappop(ladders_heap)
                        heapq.heappush(ladders_heap, delta)
                    else:
                        trans = delta

                    if bricks >= trans:
                        bricks -= trans
                    else:
                        return i - 1

        return len(heights) - 1

