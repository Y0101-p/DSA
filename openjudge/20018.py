import sys
class Bit:
    def __init__(self, arr):
        self.n = len(arr)
        self.bits = [0 for i in range(self.n+1)]
        for i in range(self.n):
            self.bit_update(i+1, arr[i])

    def bit_sum(self, i):
        s = 0
        while i > 0:
            s += self.bits[i]
            i -= i & -i
        return s

    def bit_update(self, i, v):
        while i<=self.n:
            self.bits[i] += v
            i += i & -i

data=sys.stdin.read()
data=list(map(int,data.split()))
index=0
while index<len(data):
    n=data[index]
    index+=1

    v_list=data[index:index+n]
    index+=n
    sorted_v_list=sorted(v_list)
    v_to_num={v:i+1 for i,v in enumerate(sorted_v_list)}
    BIT=Bit([0]*(n+1))
    cnt=0
    for v in v_list:
        num = v_to_num[v]
        cnt += BIT.bit_sum(num-1)
        BIT.bit_update(num, 1)

    print(cnt)