def dfs(x,y,m,n):
    if alist[x][y]==-1:
        return 0
    t=alist[x][y]
    alist[x][y]=-1
    path.append((x,y))
    for dx,dy in dic_direct[t]:
        if alist[x+dx][y+dy]==-1:
            continue
        dfs(x+dx,y+dy,m,n)


m=int(input())
n=int(input())
alist=[]
dic_direct={0:[(1,0),(-1,0),(0,1),(0,-1)],1:[(1,0),(-1,0),(0,1)],2:[(1,0),(0,1),(0,-1)],
            3:[(1,0),(0,1)],4:[(1,0),(-1,0),(0,-1)],
            5:[(1,0),(-1,0)],6:[(1,0),(0,-1)],7:[(1,0)],
            8:[(-1,0),(0,1),(0,-1)],9:[(-1,0),(0,1)],
            10:[(0,1),(0,-1)],11:[(0,1)],12:[(-1,0),(0,-1)],
            13:[(-1,0)],14:[(0,-1)],15:[]}
for i in range(m):
    alist.append(list(map(int,input().split())))
num=0
max_num=0
for i in range(m):
    for j in range(n):
        path=[]
        dfs(i,j,m,n)
        if path!=[]:
            num +=1
            max_num=max(max_num,len(path))
print(str(num)+'\n'+str(max_num))