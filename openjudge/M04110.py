import heapq
n,weight_max=map(int,input().split())
tangguo=[]
res=0
for i in range(n):
    v,w=list(map(int,input().split()))
    heapq.heappush(tangguo,(-v/w,v,w))
while tangguo:
    t=heapq.heappop(tangguo)
    if weight_max>=t[2]:
        res+=t[1]
        weight_max-=t[2]
    else:
        res+=(t[1]/t[2])*weight_max
        break
print(f'{res:.1f}')