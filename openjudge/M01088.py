def dfs(alist,dp,x,y,r,c):
    if dp[x][y]==0:
        dp[x][y]=1
    for dx,dy in delta:
        if 0<=x+dx<r and 0<=y+dy<c:
            if alist[x+dx][y+dy]<alist[x][y]:
                if dp[x+dx][y+dy]==0:
                    dfs(alist,dp,x+dx,y+dy,r,c)
                dp[x][y]=max(dp[x][y],dp[x+dx][y+dy]+1)

r,c=map(int,input().split())
alist=[]
delta=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(r):
    alist.append(list(map(int,input().split())))
dp=[[0]*c for _ in range(r)]
ans=1
for i in range(r):
    for j in range(c):
        if dp[i][j]==0:
            dfs(alist,dp,i,j,r,c)
        ans=max(ans,dp[i][j])
print(ans)