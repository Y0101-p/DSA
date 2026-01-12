class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def add_vertex(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1

n = int(input())
edges = []
disjoint = DisjointSet()
for i in range(n-1):
    data = list(input().split())
    u = data[0]
    disjoint.add_vertex(u)
    if data[1] == "0":
        continue
    else:
        for j in data[2:]:
            if j.isdigit():
                w = int(j)
                edges.append((w, u, v))
            else:
                v = j
                disjoint.add_vertex(v)
res = 0
edges.sort()
for w, u, v in edges:
    if disjoint.find(u) != disjoint.find(v):
        disjoint.union(u, v)
        res += w
print(res)