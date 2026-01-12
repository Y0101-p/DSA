def exchange(present, r, c):
    return (present - c) * r


def dfs(pr, cash):
    visited[pr] = 1
    for new_pr, r, c in graph[pr]:
        new_cash = exchange(cash, r, c)
        if new_cash <= possible_max[new_pr]:
            continue
        else:
            if visited[new_pr] == 0:
                possible_max[new_pr] = new_cash
                if dfs(new_pr, new_cash):
                    return True
            elif visited[new_pr] == 1:
                return True
    visited[pr] = 0
    return False


n, m, s, v = input().split()
n, m, s = int(n), int(m), int(s)
v = float(v)
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b, ra_b, ca_b, rb_a, cb_a = input().split()
    a, b = int(a), int(b)
    ra_b, ca_b, rb_a, cb_a = float(ra_b), float(ca_b), float(rb_a), float(cb_a)
    graph[a].append((b, ra_b, ca_b))
    graph[b].append((a, rb_a, cb_a))
visited = [0] * (n + 1)
possible_max = [0] * (n + 1)
possible_max[s] = v
if dfs(s, v):
    print('YES')
else:
    print('NO')