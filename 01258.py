import heapq
while True:
    try:
        n = int(input())
        dist_matrix = [list(map(int, input().split())) for i in range(n)]
        res = 0
        heap = []
        for i in range(1, n):
            heapq.heappush(heap, (dist_matrix[0][i], 0, i))
        visited_list = [False] * n
        visited_list[0] = True
        while heap:
            dist, u, v = heapq.heappop(heap)
            if visited_list[v]:
                continue
            res += dist
            visited_list[v] = True
            for i in range(n):
                if not visited_list[i]:
                    heapq.heappush(heap, (dist_matrix[v][i], v, i))
        print(res)
    except EOFError:
        break
