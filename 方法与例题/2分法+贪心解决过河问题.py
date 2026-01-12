l,n,m=map(int,input().split())
alist=[0]
for i in range(n):
    alist.append(int(input()))
alist.append(l)
left=0
right=l
ans=0
while left<=right:
    mid=(left+right)//2
    count=0
    prev=0
    for i in range(1,len(alist)):
        if alist[i]-prev<mid:
            count +=1
        else:
            prev=alist[i]
    if count<=m:
        ans=mid
        left=mid+1
    else: 
        right =mid-1
print(ans)