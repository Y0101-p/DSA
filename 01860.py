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

possible_max = [0] * (n + 1)
possible_max[s] = v

for i in range(n-1):
    for j in range(1,n+1):
        if possible_max[j] != 0:
            for b, r, c in graph[j]:
                new_cash = exchange(possible_max[j], r, c)
                if new_cash > possible_max[b]:
                    possible_max[b] = new_cash

for j in range(1,n+1):
    if possible_max[j] != 0:
        for b, r, c in graph[j]:
            new_cash = exchange(possible_max[j], r, c)
            if new_cash > possible_max[b]:
                print('YES')
                exit()
print('NO')
