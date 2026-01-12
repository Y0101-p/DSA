a,b,k=map(int,input().split())
yes=[]
no=[]
for i in range(k):
    r,s,p,t=map(int,input().split())
    delta=p//2
    field=(max(r-1-delta,0),min(r-1+delta,a-1),max(s-1-delta,0),min(s-1+delta,b-1))
    if t==1:
        if len(yes)==0:
            yes.append(field)
        else:
            yes[0]=(max(yes[0][0],field[0]),min(yes[0][1],field[1]),max(yes[0][2],field[2]),min(yes[0][3],field[3]))
        continue
    if t==0:
        if len(yes)==0:
            no.append(field)
            continue
        if field[0]>yes[0][1] or field[1]<yes[0][0] or field[2]>yes[0][3] or field[3]<yes[0][2]:
            continue
        no.append(field)
finalno=[]
if len(yes)==0:
    ans=[]
    for i in range(a-1):
        for j in range(b-1):
            ans.append((i,j))
            for k in no:
                if k[0]<=i<=k[1] and k[2]<=j<=k[3]:
                    ans.pop()
                    break             
    print(len(ans))
    exit()
for j in no:
    if j[0]>yes[0][1] or j[1]<yes[0][0] or j[2]>yes[0][3] or j[3]<yes[0][2]:
        continue
    finalno.append(j)
ans=[]
for i in range(yes[0][0],yes[0][1]+1):
    for j in range(yes[0][2],yes[0][3]+1):
        ans.append((i,j))
        for k in finalno:
            if k[0]<=i<=k[1] and k[2]<=j<=k[3]:
                ans.pop()
                break
print(len(ans))