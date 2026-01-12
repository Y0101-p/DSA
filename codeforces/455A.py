from collections import Counter
n=int(input())
data=map(int,input().split())
counts = Counter(data)

dp=[[] for i in range(2)]
dp[0].append(0)
dp[1].append(0)
for i in range(1,max(counts)+1):
    if i not in counts:
        dp[0].append(max(dp[0][i-1],dp[1][i-1]))
        dp[1].append(-1)
        continue
    else:
        dp[0].append(max(dp[0][i-1],dp[1][i-1]))
        dp[1].append(dp[0][i-1]+i*counts[i])
print(max(dp[0][-1],dp[1][-1]))