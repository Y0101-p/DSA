t=int(input())
for i in range(t):
    n=int(input())
    num_list=list(map(int,input().split()))
    dp=[]
    mini=num_list[0]
    dp_max=0
    for i in range(n):
        mini=min(mini,num_list[i])
        dp_max=max(dp_max,num_list[i]-mini)
        dp.append(dp_max)
    maxi=num_list[-1]
    res=dp[-1]
    for i in range(1,n):
        maxi=max(maxi,num_list[-i])
        res=max(res,maxi-num_list[-i]+dp[-i-1])
    print(res)