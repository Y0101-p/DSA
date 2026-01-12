class VeryBigInt:
    def __init__(self,value):
        self.value=value
    def __str__(self):
        cnt=0
        for i in range(len(self.value)):
            if self.value[i]!='0':
                break
            cnt+=1
        if cnt==len(self.value):
            return '0'
        return self.value[cnt:]
    def add(self,other):
        ans=[0]*(max(len(self.value),len(other.value))+1)
        cnt=0
        while cnt<len(self.value) or cnt<len(other.value):
            a,b=0,0
            if cnt<len(other.value):
                a=int(other.value[-cnt-1])
            if cnt<len(self.value):
                b=int(self.value[-cnt-1])
            num=a+b
            ans[cnt]=num+ans[cnt]
            ans[cnt+1]+=ans[cnt]//10
            ans[cnt]=ans[cnt]%10
            cnt+=1
        res=''.join(list(map(str,ans[::-1])))
        return VeryBigInt(res)
a=input()
num_a=VeryBigInt(a)
b=input()
num_b=VeryBigInt(b)
c=num_a.add(num_b)
print(c)