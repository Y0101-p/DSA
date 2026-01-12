def oula(num):
    prime=[]
    hax=[True]*(num+1)
    for i in range(2,num+1):
        if hax[i]:
            prime.append(i)
            hax[i] = False
        for j in prime:
            if i*j>num:
                break
            hax[i*j]=False
            if i%j==0:
                break
    return prime
def judge(num):
    for i in prime:
        if num%i==0:
            return False
        if i*i>num:
            return True

def build_num():
    res=0
    for i in range(len(num_list)):
        res+=num_list[i]*10**i
        res+=num_list[i]*10**(len(num_list)*2-i-2)
    res-=num_list[-1]*10**i
    return res
def weici(index):
    if index==(n+1)//2:
        num=build_num()
        if judge(num):
            results.append(str(num))
        return
    for i in range(0,10):
        num_list[index]=i
        weici(index+1)
    return
n=int(input().strip())
if n%2==0:
    if n==2:
        print(1)
        print(11)
    else:
        print(0)
        print()
elif n==1:
        print(4)
        print(2,3,5,7)
else:
    prime=oula(10**5)
    results=[]
    num_list=[1]+[0]*((n-1)//2)
    for i in range(1,10,2):
        num_list[0]=i
        weici(1)
    print(len(results))
    print(' '.join(results))