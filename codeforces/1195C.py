n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
dp=[[] for i in range(3)]
dp[0].append(alist[0])
dp[1].append(blist[0])
dp[2].append(0)
for i in range(1,n):
    dp[0].append(alist[i]+max(dp[1][i-1],dp[2][i-1]))
    dp[1].append(blist[i]+max(dp[0][i-1],dp[2][i-1]))
    dp[2].append(max(dp[1][i-1],dp[0][i-1],dp[2][i-1]))
print(max(dp[0][n-1],dp[1][n-1],dp[2][n-1]))