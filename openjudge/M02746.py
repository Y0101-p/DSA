while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    alist=[i for i in range(1,n+1)]
    pr=0
    for j in range(n-1):
        pr +=(m-1)%len(alist)
        pr=pr%len(alist)
        alist.pop(pr)
    print(*alist)