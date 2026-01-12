def oula(max):
    prime=[0 for i in range(max+1)]
    common=[]
    for i in range(2,max+1):
        if prime[i]==0:
            common.append(i)
        for j in common:
            if i*j>max:
                break
            prime[i*j]=1
            if i%j==0:
                break
    return common
