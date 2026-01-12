class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))#根节点
        self.rank = [0] * (n + 1)#树高度

    def find(self, x):
        if self.parent[x] != x:              # 如果x不是根节点
            self.parent[x] = self.find(self.parent[x])  # 递归查找并压缩路径
        return self.parent[x]                 # 返回根节点
    def union(self, x, y):
        root_x = self.find(x)                # 找到x的根节点
        root_y = self.find(y)                # 找到y的根节点
    
        if root_x == root_y:                 # 如果已经在同一集合
            return                           # 直接返回，无需合并
    
    # 按秩合并（优化步骤）
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y     # 将较矮的树连接到较高的树
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x     # 将较矮的树连接到较高的树
        else:
            self.parent[root_y] = root_x     # 高度相等，任意连接
            self.rank[root_x] += 1           # 高度增加1