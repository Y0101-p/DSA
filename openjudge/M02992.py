n=int(input())
dp_up=[1]*n
dp_down=[1]*n
h_list=list(map(int,input().split()))
for i in range(1,n):
    for j in range(i):
        if h_list[j]>h_list[i]:
            dp_down[i]=max(dp_down[i],dp_down[j]+1)
        elif h_list[j]<h_list[i]:
            dp_up[i]=max(dp_up[i],dp_up[j]+1)
    dp_down[i]=max(dp_down[i],dp_up[i])
print(max(max(dp_up),max(dp_down)))