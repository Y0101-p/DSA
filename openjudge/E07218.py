from collections import deque

def find_start():
    for j in range(r):
        for k in range(c):
            if matrix[j][k] == 'S':
                return j, k

def bfs(start,r,c):
    queue = deque([(start[0],start[1],0)])
    finished = set()
    finished.add(start)
    delta=[(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        x,y,steps=queue.popleft()
        for dx,dy in delta:
            if 0<=x+dx<r and 0<=y+dy<c:
                if (x+dx,y+dy) not in finished:
                    finished.add((x+dx,y+dy))
                    if matrix[x+dx][y+dy] == '.':
                        queue.append((x+dx,y+dy,steps+1))
                    if matrix[x+dx][y+dy] == 'E':
                        return str(steps+1)
    return 'oop!'

t=int(input())
for i in range(t):
    r,c=map(int,input().split())
    matrix=[]
    for j in range(r):
        matrix.append(list(input()))
    start=find_start()
    print(bfs(start,r,c))
