from collections import deque


def exchange(present, r, c):
    return (present - c) * r


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

queue = deque()
queue.append(s)
possible_max = [0] * (n + 1)
possible_max[s] = v
in_queue_cnt = [0] * (n + 1)
in_queue_cnt[s] = 1
in_queue = [False] * (n + 1)
in_queue[s] = True
while queue:
    pr = queue.popleft()
    in_queue[pr] = False
    for b, r, c in graph[pr]:
        new_cash = exchange(possible_max[pr], r, c)
        if new_cash > possible_max[b]:
            possible_max[b] = new_cash
            if not in_queue[b]:
                in_queue[b] = True
                in_queue_cnt[b] += 1
                queue.append(b)
                if in_queue_cnt[b] >= n:
                    print('YES')
                    exit()
print('NO')