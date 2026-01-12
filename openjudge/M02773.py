t,m=map(int,input().split())
data_list=[]
for i in range(m):
    data_list.append(list(map(int,input().split())))
    if data_list[-1][0]>t:
        data_list.pop()
data_list.sort(key=lambda x:x[0])
m=len(data_list)
dp=[[0]*(m+1) for _ in range(t+1)]
for j in range(1,m+1):
    data=data_list[j-1]
    for k in range(data[0],len(dp)):
        dp[k][j]=max(dp[k][j-1],data[1]+dp[k-data[0]][j-1])
print(dp[t][m])


"""
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(index,last_t,m):
    if index==m or last_t<=0:
        return 0
    max_value=dfs(index+1,last_t,m)
    if last_t>=data_list[index][0]:
        max_value=max(max_value,data_list[index][1]+dfs(index+1,last_t-data_list[index][0],m))
    return max_value

t,m=map(int,input().split())
data_list=[]
for i in range(m):
    data_list.append(tuple(map(int,input().split())))

print(dfs(0,t,m))
"""