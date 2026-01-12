def fenjie(a,path):
    if a==1:
        if path not in res:
            res.append(path.copy())
    for i in range(2,a+1):
        if a%i==0:
            path.setdefault(i,0)
            path[i] +=1
            fenjie(a//i,path)
            path[i] -=1
            if path[i]==0:
                del path[i]
n=int(input())
for i in range(n):
    a=int(input())
    res=[]
    fenjie(a,{})
    print(len(res))