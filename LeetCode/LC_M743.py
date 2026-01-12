from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def build_graph():
            graph = {}
            for u, v, w in times:
                graph.setdefault(u, {})
                graph[u][v] = w
            return graph
        def dijkstra(start):
            dist = [float('inf')] * (n+1)
            visited = [False] * (n+1)
            dist[start] = 0
            heap=[]
            heapq.heappush(heap, (0, start))
            while heap:
                d, u = heapq.heappop(heap)
                if visited[u]:
                    continue
                visited[u] = True
                for v in graph.get(u, {}):
                    if visited[v]:
                        continue
                    w = graph[u][v]
                    new_dist = d + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(heap, (new_dist, v))
            return dist


        graph = build_graph()
        dist = dijkstra(k)
        max_time = 0
        for i in dist[1:]:
            max_time = max(max_time, i)
        if max_time ==float('inf'):
            return -1
        else:
            return max_time

sol = Solution()
print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))