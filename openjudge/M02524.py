class disjointset:
    def __init__(self,n):
        self.parent =list(range(n+1))
        self.rank=[0]*(n+1)
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)

        if root_x == root_y:
            return
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
        else:
            self.parent[root_y]=root_x
            self.rank[root_x] +=1


if __name__=='__main__':
    Case=0
    while True:
        n,m=map(int,input().split())
        if n==0 and m==0:
            break
        Case +=1
        ans=disjointset(n)
        for i in range(m):
            a,b=map(int,input().split())
            ans.union(a,b)
        alist=[]
        for i in range(1,n+1):
            t=ans.find(i)
            if t not in alist:
                alist.append(t)
        print(f'Case {Case}: {len(alist)}')        