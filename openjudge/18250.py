class DisjointSet:
    def __init__(self,n):
        self.parents = [x for x in range(n)]
        self.rank = [0 for x in range(n)]
    def find(self,x):
        if self.parents[x]!=x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self,x,y):
        xroot,yroot = self.find(x),self.find(y)
        if xroot==yroot:
            return True

        self.parents[yroot] = xroot
        return False



while True:
    try:
        n, m = map(int, input().split())
        dis = DisjointSet(n)
        for i in range(m):
            x, y = map(int, input().split())
            x, y = x-1, y-1
            if dis.union(x,y):
                print('Yes')
            else:
                print('No')

        res = []
        for i in range(n):
            if dis.find(i)==i:
                res.append(i+1)
        print(len(res))
        print(*res)
    except EOFError:
        break