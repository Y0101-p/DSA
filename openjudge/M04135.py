n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
right=sum(l)+1
left=max(l)
peak=0
while left<=right:
    mid=(left+right)//2
    s=0
    t=1
    for i in l:
        if s+i<=mid:
            s +=i
        else:
            t +=1
            s=i
    if t>m:
        left =mid+1
    else:
        right=mid-1
    
print(left)