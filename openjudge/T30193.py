from collections import deque

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def distance_check(pr,t):
    for target_x,target_y,target_t in demand[1:]:
        if target_t >= t:
            target = (target_x,target_y)
            distance = manhattan_distance(pr,target)
            if visited[target_x][target_y]:
                return False
            if target in bad:
                return False
            if distance > target_t-t:
                return False
    return True

def connect_check(pr,n,m):
    que = deque()
    que.append(pr)
    reachable = set()
    while que:
        x,y = que.popleft()
        for dx,dy in delta:
            if 1<=x+dx<=n and 1<=y+dy<=m and not visited[x+dx][y+dy] and (x+dx,y+dy) not in reachable and (x+dx,y+dy) not in bad:
                que.append((x+dx,y+dy))
                reachable.add((x+dx,y+dy))
    if reachable == un_visited:
        return True
    else:
        return False

def count_neighbors(pr,n,m):
    cnt = 0
    for dx,dy in delta:
        x = dx+pr[0]
        y = dy+pr[1]
        if 1<=x<=n and 1<=y<=m and not visited[x][y] and (x,y) not in bad:
           cnt += 1
    return cnt



def dfs(pr,t,n,m,path,cnt,end):

    if cnt == end:
        ans.append(path[:])
        return True
    if not connect_check(pr,n,m):
        return False

    candidate = []
    for dx, dy in delta:
        new_pr = (pr[0] + dx, pr[1] + dy)
        if 1 <= new_pr[0] <= n and 1 <= new_pr[1] <= m and not visited[new_pr[0]][new_pr[1]] and new_pr not in bad:
            if distance_check(new_pr, t + 1):
                count = count_neighbors(new_pr, n, m)
                candidate.append((count, new_pr[0], new_pr[1]))
    candidate.sort()

    for cnt_0, x, y in candidate:
        visited[x][y] = True
        un_visited.discard((x, y))
        if dfs((x, y), t + 1, n, m, path + [(x, y)], cnt + 1, end):
            return True
        visited[x][y] = False
        un_visited.add((x, y))
    return False


n,m,k,b = map(int,input().split())
demand = [list(map(int,input().split())) for i in range(k)]
demand.sort(key=lambda x:x[2])
bad = [ tuple(map(int,input().split())) for i in range(b)]
bad = set(bad)
delta = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[False]*(m+1) for _ in range(n+1)]
un_visited = set()
for x in range(1,n+1):
    for y in range(1,m+1):
        if (x,y) not in bad:
            un_visited.add((x,y))
begin_pr = tuple(demand[0][:2])
path = [begin_pr]
visited[begin_pr[0]][begin_pr[1]] = True
un_visited.discard(begin_pr)
ans = []
dfs(begin_pr,1,n,m,path,1,n*m-len(bad))
if not ans:
    print(-1)
else:
    for x,y in ans[0]:
        print(x,y)