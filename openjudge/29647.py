def dfs(root):
    if dp[root]:
        return dp[root]

    child_come_max = 0
    child_not_come_max = 0
    for child in graph[root]:
        come, not_come = dfs(child)
        child_come_max += max(come, not_come)
        child_not_come_max += not_come
    dp[root] = (child_not_come_max + happy[root]
                    , max(child_not_come_max, child_come_max))

    return dp[root]

n = int(input())
happy = [0]
graph = [[] for i in range(n+1)]
for i in range(n):
    happy.append(int(input()))

for i in range(n-1):
    l, k = map(int, input().split())
    graph[k].append(l)

dp = [None] * (n+1)
res = 0
for i in range(1, n+1):
    a, b = dfs(i)
    res = max(res, a, b)
print(res)