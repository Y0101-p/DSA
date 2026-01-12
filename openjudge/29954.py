from collections import deque
def xieru(i,j,k,steps):
    if l[i][j]=='.':
        if (i,j,k) not in finishi_set:
            duilie.append((i,j,k,steps+1))
            finishi_set.add((i,j,k))
    if l[i][j]=='#' and k>0:
        if (i,j,k-1) not in finishi_set:
            duilie.append((i,j,k-1,steps+1))
            finishi_set.add((i,j,k-1))
    if l[i][j]=='E':
        return True
    return False


r,c,k=map(int,input().split())
l=[]
for i in range(r):
    l.append(input())
    for j in range(c):
        if l[-1][j]=='S':
            begin=(i,j)
duilie=deque([(begin[0],begin[1],k,0)])
finishi_set={(begin[0],begin[1],k)}
huitou_set=set()
delta=[(0,1),(0,-1),(1,0),(-1,0)]
while duilie:
    t=duilie.popleft()
    huitou_set.add((t[0],t[1]))
    for di,dj in delta:
        if 0<=di+t[0]<r and 0<=dj+t[1]<c:
            if (di+t[0],dj+t[1]) not in huitou_set:
                if xieru(di+t[0],dj+t[1],t[2],t[3]):
                    print(t[3]+1)
                    exit()

print(-1)