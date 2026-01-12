while True:
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:
        break
    res=[]
    p=p-1
    index_list=[i for i in range(1,n+1)]
    while index_list:
        p +=m-1
        p %=len(index_list)
        res.append(index_list.pop(p))
    print(','.join(map(str,res)))