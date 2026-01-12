def dfs(hax,deep,q,p,x,y,path,ans):
    hax[x][y]=1
    path.append((x,y))
    if deep==q*p-1:
        if ans==[]:
            ans=path[:]
        return ans
    for dx,dy in delta:
        if 0<=x+dx<q and 0<=y+dy<p:
            if hax[x+dx][y+dy]==0:
                ans=dfs(hax,deep+1,q,p,x+dx,y+dy,path,ans)
                if len(ans)!=0:
                    return ans
    hax[x][y]=0
    path.pop()
    return ans

n=int(input())
delta=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
for i in range(n):
    p,q=map(int,input().split())
    hax=[[0]*p for _ in range(q)]
    ans=[]
    for j in range(q):
        for k in range(p):
            ans=dfs(hax,0,q,p,j,k,[],ans)
            if len(ans)!=0:
                break
        if len(ans)!=0:
            break
    print(f'Scenario #{i+1}:')
    if len(ans)==0:
        print('impossible')
    else:
        res=''
        for zimu,num in ans:
            res +=chr(zimu+65)
            res +=str(num+1)
        print(res)
    if i!=n-1:
        print()