def check(l,n,c,mid):
    prev=l[0]
    count =1
    for i in range(1,n):
        if l[i]-prev<mid:
            continue
        else:
            count +=1
            prev =l[i]
    if count>=c:
        return True
    else:
        return False

n,c=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
left=0
right=l[-1]
ans=0
while right>=left:
    mid =(left+right)//2
    if check(l,n,c,mid):
        left=mid+1
    else:
        right=mid-1
print(right)
