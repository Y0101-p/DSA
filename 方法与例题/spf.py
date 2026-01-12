def spf_shai(max_a):
    spf=list(range(max_a+1))
    for i in range(2,int(max_a**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,max_a+1,i):
                if spf[j]==j:
                    spf[j]=i
    return spf

print(spf_shai(100))