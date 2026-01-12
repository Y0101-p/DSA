#11：02
def shai(n):
    prime=[]
    hax=[0]*(n+1)
    for i in range(2,n+1):
        if hax[i]==0:
            prime.append(i)
        for k in prime:
            if k*i>n:
                break
            hax[k*i]=1
            if i%k==0:
                break
    return prime
s=int(input())
prime=shai(s)
for i in prime:
    if s-i in prime:
        print(i,s-i)
        exit()
