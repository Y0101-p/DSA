t=int(input())
for i in range(t):
    n=int(input())
    alist=[0]*(2*n)
    l=list(map(int,input().split()))
    for j in range(n):
        alist[l[j]-j] +=1
    s=0
    for j in alist:
        if j>=2:
            s +=j*(j-1)//2
    print(s)