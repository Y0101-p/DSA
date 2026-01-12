import sys
from collections import defaultdict


def build_tree(edges, n):
    """ 构建树的邻接表 """
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    return tree


def count_leaves(tree, n):
    """ 计算每个节点的叶子数 (使用迭代 DFS) """
    leaves_count = {i: 0 for i in range(1, n + 1)}
    parent = {1: -1}
    stack = [(1, 0)]  # (当前节点, 状态 0-首次访问 1-回溯)

    order = []  # 记录 DFS 访问顺序

    while stack:
        node, state = stack.pop()
        if state == 0:  # 首次访问
            stack.append((node, 1))
            order.append(node)
            for child in tree[node]:
                if child == parent.get(node):
                    continue
                parent[child] = node
                stack.append((child, 0))

    # 反向遍历 order 计算叶子数。确保每个节点在其所有子节点之后被处理
    for node in reversed(order):
        if len(tree[node]) == 1 and node != 1:  # 叶子节点（根节点除外）
            leaves_count[node] = 1
        else:
            leaves_count[node] = sum(leaves_count[child] for child in tree[node] if child != parent[node])

    return leaves_count


def process_queries(leaves_count, queries):
    """ 处理查询，计算答案 """
    results = []
    for x, y in queries:
        results.append(str(leaves_count[x] * leaves_count[y]))
    sys.stdout.write("\n".join(results) + "\n")


def solve():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1

        edges = []
        for _ in range(n - 1):
            u, v = int(data[index]), int(data[index + 1])
            index += 2
            edges.append((u, v))

        tree = build_tree(edges, n)
        leaves_count = count_leaves(tree, n)

        q = int(data[index])
        index += 1

        queries = []
        for _ in range(q):
            x, y = int(data[index]), int(data[index + 1])
            index += 2
            queries.append((x, y))

        process_queries(leaves_count, queries)


if __name__ == "__main__":
    # sys.setrecursionlimit(300000)  # 提高递归深度
    solve()
