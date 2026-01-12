def check(l,k):
    res=0
    for i in length_list:
        res+=i//l
        if res>=k:
            return True
    if res<k:
        return False
    else:
        return True
n,k=map(int,input().split())
length_list=[]
for i in range(n):
    length_list.append(int(float(input())*100))
left=1
right=max(length_list)
if sum(length_list)<k:
    print('0.00')
    exit()
while left<=right:
    mid=(left+right)//2
    if check(mid,k):
        left=mid+1
    else:
        right=mid-1
print(f'{float(right)/100:.2f}')