n=int(input())
alist=[]
for i in range(n):
    alist.append(list(map(int,input().split())))
dp=[[alist[0][0]]]
for i in range(1,n):
    dp.append([])
    for j in range(len(alist[i])):
        if j==0:
            dp[-1].append(dp[-2][0]+alist[i][j])
        elif j==len(alist[i])-1:
            dp[-1].append(dp[-2][-1]+alist[i][j])
        else:
            dp[-1].append(max(dp[-2][j-1],dp[-2][j])+alist[i][j])
print(max(dp[-1]))