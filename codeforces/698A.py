n=int(input())
alist=list(map(int,input().split()))
dp=[[] for _ in range(3)]
if alist[0]==0:
    dp[0].append(1)
    dp[1].append(float("inf"))
    dp[2].append(float("inf"))
elif alist[0]==1:
    dp[0].append(1)
    dp[1].append(0)
    dp[2].append(float("inf"))
elif alist[0]==2:
    dp[0].append(1)
    dp[1].append(float("inf"))
    dp[2].append(0)
elif alist[0]==3:
    dp[0].append(1)
    dp[1].append(0)
    dp[2].append(0)
for i in range(1,n):
    a = dp[0][i-1]
    b = dp[1][i-1]
    c = dp[2][i-1]
    dp[0].append(min(a,b,c)+1)
    if alist[i]==0:
        dp[1].append(float("inf"))
        dp[2].append(float("inf"))
    elif alist[i]==1:
        dp[1].append(min(a,c))
        dp[2].append(float("inf"))
    elif alist[i]==2:
        dp[1].append(float("inf"))
        dp[2].append(min(a,b))
    elif alist[i]==3:
        dp[1].append(min(a,c))
        dp[2].append(min(a,b))
print(min(dp[0][-1],dp[1][-1],dp[2][-1]))