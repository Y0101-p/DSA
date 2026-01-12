from collections import defaultdict
from collections import deque


def exchange(present, r, c):
    return (present - c) * r


n, m, s, v = input().split()
n, m, s = int(n), int(m), int(s)
v = float(v)
graph = defaultdict(dict)
for i in range(m):
    a, b, ra_b, ca_b, rb_a, cb_a = input().split()
    a, b = int(a), int(b)
    ra_b, ca_b, rb_a, cb_a = float(ra_b), float(ca_b), float(rb_a), float(cb_a)
    graph[a].setdefault(b, []).append((ra_b, ca_b))
    graph[b].setdefault(a, []).append((rb_a, cb_a))
queue = deque([])
queue.append((s, v))
possible_list = [0] * (n+1)

while queue and possible_list[s] <= v:
    num_s, num_v = queue.popleft()
    if num_v > possible_list[num_s]:
        possible_list[num_s] = num_v
    else:
        continue

    for next_s in graph[num_s]:
        for r, c in graph[num_s][next_s]:
            queue.append((next_s, exchange(num_v, r, c)))

if possible_list[s] > v:
    print('YES')
else:
    print('NO')
