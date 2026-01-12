import sys
def spf_shai(max_a):
    spf=list(range(max_a+1))
    for i in range(2,int(max_a**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,max_a+1,i):
                if spf[j]==j:
                    spf[j]=i
    return spf
data=sys.stdin.read()
readin=data.splitlines()
n=int(readin[0])
res1=['-1']*n
res2=['-1']*n
num_list=list(map(int,readin[1].split()))
spf=spf_shai(10**7)
for i in range(n):
    min_prime_divisor=spf[num_list[i]]
    while num_list[i]%min_prime_divisor==0:
        num_list[i]//=min_prime_divisor
    if num_list[i]!=1:
        res1[i]=str(min_prime_divisor)
        res2[i]=str(num_list[i])
res=' '.join(res1)+'\n'+' '.join(res2)
sys.stdout.write(res)