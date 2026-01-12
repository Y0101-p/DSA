def dfs(x,y,steps,n,m):
    if steps == m*n:
        cnt[0] +=1
        return
    for dx,dy in delta:
        if 0<=x+dx<n and 0<=y+dy<m and not visited[x+dx][y+dy]:
            visited[x+dx][y+dy] = True
            dfs(x+dx,y+dy,steps+1,n,m)
            visited[x+dx][y+dy] = False
    return
t = int(input())
delta=[(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-2,-1),(-1,-2)]
for i in range(t):
    n,m,begin_x,begin_y = map(int,input().split())
    cnt=[0]
    visited = [[False]*m for _ in range(n)]
    visited[begin_x][begin_y] = True
    dfs(begin_x,begin_y,1,n,m)
    print(cnt[0])