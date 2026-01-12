from typing import List, Tuple

def dijkstra_array(graph:List[List[Tuple[int,int]]], start:int)->List[int]:
    """
    不使用heapq的Dijkstra算法（使用数组）
    适用于稠密图
    """
    n = len(graph)
    # 初始化距离数组
    dist = [float('inf')] * n
    dist[start] = 0

    # 记录节点是否已访问
    visited = [False] * n

    for _ in range(n):
        # 找到未访问节点中距离最小的节点
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        # 所有可达节点都已处理完毕
        if u == -1:
            break

        visited[u] = True

        # 更新邻居节点的距离
        for v, weight in graph[u]:
            if not visited[v]:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist

    return dist


# 测试用例
def test_dijkstra_array():
    # 使用相同的测试图
    graph = [
        [(1, 4), (2, 1)],  # 节点0
        [(3, 1)],  # 节点1
        [(1, 2), (3, 5)],  # 节点2
        []  # 节点3
    ]

    start_node = 0
    distances = dijkstra_array(graph, start_node)

    print("不使用heapq的Dijkstra算法结果:")
    for i, d in enumerate(distances):
        print(f"从节点{start_node}到节点{i}的最短距离: {d}")

# test_dijkstra_array()


import heapq
import sys


def dijkstra_heapq(graph:List[List[Tuple[int,int]]], start:int)->List[int]:
    """
    使用heapq优化的Dijkstra算法
    适用于稀疏图
    """
    n = len(graph)
    # 初始化距离数组
    dist = [float('inf')] * n
    dist[start] = 0

    # 使用最小堆存储(距离, 节点)
    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        # 如果当前距离大于已知最短距离，跳过
        if current_dist > dist[u]:
            continue

        # 遍历所有邻居
        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            # 如果找到更短路径
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist


# 测试用例
def test_dijkstra_heapq():
    # 图的邻接表表示
    # graph[u] = [(v, weight), ...]
    graph = [
        [(1, 4), (2, 1)],  # 节点0
        [(3, 1)],  # 节点1
        [(1, 2), (3, 5)],  # 节点2
        []  # 节点3
    ]

    start_node = 0
    distances = dijkstra_heapq(graph, start_node)

    print("使用heapq的Dijkstra算法结果:")
    for i, d in enumerate(distances):
        print(f"从节点{start_node}到节点{i}的最短距离: {d}")

# test_dijkstra_heapq()