import math
def oula(n):
    prime=[]
    hax=[True]*(n+1)
    for i in range(2,n+1):
        if hax[i]:
            prime.append(i)
            hax[i]=False
        for j in prime:
            if i*j>n:
                break
            hax[i*j]=False
            if j%i==0:
                break
    return set(prime)


prime=oula(10**6)
n=int(input())
num_list=list(map(int,input().split()))
for i in range(n):
    judge=0
    if math.sqrt(num_list[i]) in prime:
        print('YES')
    else:
        print('NO')